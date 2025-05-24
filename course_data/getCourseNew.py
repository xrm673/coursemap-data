# if the course does not exist in the database,
# initialize the course data
# if the course exists in the database,
# update the course data

import firebase_admin
from firebase_admin import credentials, firestore
import json
import sys
import os
import requests
from typing import List, Dict, Any, Tuple
import time

# Add the root directory to the Python path
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(root_dir)

from const import *

# Import local modules
from parseText import *

cred = credentials.Certificate(SERVICE_ACCOUNT_PATH)
firebase_admin.initialize_app(cred)
db = firestore.client()


def fetch_subjects_courses(
    semester: str,
) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    """
    Fetch subject and course data from class roster API for a specific semester.

    Args:
        semester: The semester code (e.g., "SP25")

    Returns:
        Tuple containing:
            - List of subject dictionaries
            - List of course data dictionaries
    """
    print(f"Fetching data for {semester}...")

    # Step 1: Fetch subjects from the subjects API
    subjects_url = (
        f"https://classes.cornell.edu/api/2.0/config/subjects.json?roster={semester}"
    )
    subjects_response = requests.get(subjects_url)

    if subjects_response.status_code != 200:
        print(
            f"Error fetching subjects for {semester}: {subjects_response.status_code}"
        )
        return [], []

    subjects_data = subjects_response.json()
    if subjects_data.get("status") != "success":
        print(
            f"API error for subjects in {semester}: {subjects_data.get('message', 'Unknown error')}"
        )
        return [], []

    subjects = subjects_data["data"]["subjects"]
    print(f"Fetched {len(subjects)} subjects for {semester}")

    # Step 2: Fetch courses for each subject
    all_courses = []
    for subject in subjects:
        subject_code = subject["value"]
        course_url = f"https://classes.cornell.edu/api/2.0/search/classes.json?roster={semester}&subject={subject_code}"
        course_response = requests.get(course_url)

        if (
            course_response.status_code == 200
            and course_response.json()["status"] == "success"
        ):
            courses = course_response.json()["data"]["classes"]
            all_courses.extend(courses)
            print(f"Fetched {len(courses)} courses for {subject_code} in {semester}")

    return subjects, all_courses


def upload_subjects(subjects: List[Dict[str, Any]], semester: str) -> None:
    """
    Process subject data and upload to Firestore.
    Only adds subjects that don't already exist.

    Args:
        subjects: List of subject data from the API
        semester: The semester code (e.g., "SP25")
    """
    # Process subjects with proper names from the API
    subject_batch = db.batch()
    subject_count = 0
    subjects_added = 0

    for subject in subjects:
        subject_code = subject["value"]

        # Check if subject already exists
        subject_ref = db.collection("subjects").document(subject_code)
        subject_doc = subject_ref.get()
        if subject_doc.exists:
            # Subject exists, update the subject data
            existing_data = subject_doc.to_dict()
            semesters = existing_data.get("semesters", [])
            if semester not in semesters:
                semesters.append(semester)
                subject_ref.update({"semesters": semesters})
        else:
            # Subject doesn't exist, add it
            subject_data = {
                "code": subject_code,
                "name": subject["descr"],
                "formalName": subject["descrformal"],
                "semesters": [semester],
            }

            subject_batch.set(subject_ref, subject_data)
            subject_count += 1
            subjects_added += 1

            # Commit in smaller batches if needed
            if subject_count >= 200:
                subject_batch.commit()
                subject_batch = db.batch()
                subject_count = 0

    # Commit any remaining subjects
    if subject_count > 0:
        subject_batch.commit()

    print(f"Added {subjects_added} new subjects for {semester}")
    
    
def upload_courses(courses: List[Dict[str, Any]], semester: str) -> None:
    """
    Process course data and upload to Firestore with semester tracking.
    Includes enrollment groups, sections, meetings, and instructors.

    Args:
        courses: List of course data from the API
        semester: The semester code (e.g., "SP25")
    """
    # Track batch operations to stay within Firestore limits
    batch = db.batch()
    batch_count = 0
    MAX_BATCH_SIZE = 500  # Firestore limit

    # Process and upload courses with semester tracking
    for course in courses:
        course_id = f"{course['subject']}{course['catalogNbr']}"

        # Check if the course already exists
        existing_course_ref = db.collection("courses").document(course_id)
        existing_course_doc = existing_course_ref.get()

        if existing_course_doc.exists:
            # Initialize update_data dictionary
            update_data = {}
            
            # Course exists, update the course data
            existing_data = existing_course_doc.to_dict()
            update_data["smst"] = add_early_semester(existing_data, semester)
                
            for early_group in course.get("enrollGroups", []):
                identifier, has_topic = get_group_identifier(early_group)
                # Check if identifier is not in any dictionary's identifier field
                if not any(existing_group.get("grpIdentifier") == identifier for existing_group in existing_data["enrollGroups"]):
                    group_data = initialize_enroll_group(early_group, semester, identifier, has_topic)
                    existing_data["enrollGroups"].append(group_data)
                else:
                    # a enroll group with the same identifier already exists
                    # Find the existing group and its index
                    for i, existing_group in enumerate(existing_data["enrollGroups"]):
                        if existing_group.get("grpIdentifier") == identifier:
                            # Update the existing group with early semester data
                            updated_group = add_early_group_data(existing_group, early_group, semester)
                            # Replace the original enroll group with the updated one
                            existing_data["enrollGroups"][i] = updated_group
                            break
            
            # Add enrollGroups to update_data since we know it's been modified
            update_data["enrollGroups"] = existing_data["enrollGroups"]
            batch.update(existing_course_ref, update_data)
            batch_count += 1
            
        else:
            # New course, create full document
            course_data = initialize_single_course(course, semester)
            course_data["enrollGroups"] = []
            for enroll_group in course.get("enrollGroups", []):
                identifier, has_topic = get_group_identifier(enroll_group)
                group_data = initialize_enroll_group(enroll_group, semester, identifier, has_topic)
                course_data["enrollGroups"].append(group_data)
            batch.set(existing_course_ref, course_data)
            batch_count += 1
            
        # Commit batch if we've reached the maximum size
        if batch_count >= MAX_BATCH_SIZE:
            batch.commit()
            batch = db.batch()  # Start a new batch
            batch_count = 0
        
        print(f"Processed {course_id} for {semester}")
            
    # Commit any remaining operations in the final batch
    if batch_count > 0:
        batch.commit()


def initialize_single_course(course: Dict[str, Any], semester: str) -> Dict[str, Any]:
    single_course = {}
    course_id = course["subject"] + course["catalogNbr"]

    single_course["id"] = course_id
    single_course["sbj"] = course["subject"]
    single_course["nbr"] = course["catalogNbr"]
    single_course["lvl"] = int(course["catalogNbr"][0])
    single_course["smst"] = [semester]
    single_course["ttl"] = course["titleLong"]
    single_course["tts"] = course["titleShort"]
    single_course["dsrpn"] = clean(course["description"])

    req = clean(course["catalogPrereqCoreq"])
    cmts = clean(course["catalogComments"])
    if cmts:
        if has_recommend_preco(cmts):
            # comment that has recommended prerequisite info
            single_course["rcmdReq"] = cmts
        elif has_preco(cmts) and not req:
            # comment that has prerequisite info
            req = cmts
        else:
            # regular comments that don't have any prerequisite info
            single_course["cmts"] = cmts

    if req:
        single_course["req"] = req
        preco_dict = parse_preco(req)
        if preco_dict["prereq"]:
            single_course["prereq"] = json.dumps(preco_dict["prereq"])
        if preco_dict["coreq"]:
            single_course["coreq"] = json.dumps(preco_dict["coreq"])
        if preco_dict["preco"]:
            single_course["preco"] = json.dumps(preco_dict["preco"])
        single_course["needNote"] = preco_dict["note"]

    if course["catalogWhenOffered"]:
        single_course["when"] = parse_when_offered(course["catalogWhenOffered"])
    if course["catalogBreadth"]:
        single_course["breadth"] = course["catalogBreadth"]
    if course["catalogDistr"]:
        single_course["distr"] = parse_distr(course["catalogDistr"])
    if course["catalogAttribute"]:
        single_course["attr"] = parse_distr(course["catalogAttribute"])
    if course["catalogLang"]:
        single_course["lanreq"] = clean(course["catalogLang"])
    if course["catalogForbiddenOverlaps"]:
        single_course["ovlpText"] = clean(course["catalogForbiddenOverlaps"])
        single_course["ovlp"] = parse_overlap(course["catalogForbiddenOverlaps"])
    if course["catalogFee"]:
        single_course["fee"] = clean(course["catalogFee"])
    if course["catalogSatisfiesReq"]:
        single_course["satisfies"] = clean(course["catalogSatisfiesReq"])
    if course["catalogPermission"]:
        single_course["pmsn"] = course["catalogPermission"]
    if course["catalogOutcomes"]:
        single_course["otcm"] = clean_list(course["catalogOutcomes"])
    if course["catalogCourseSubfield"]:
        single_course["subfield"] = clean(course["catalogCourseSubfield"])
    single_course["career"] = course["acadCareer"]
    single_course["acadgrp"] = course["acadGroup"]
    return single_course


def initialize_enroll_group(
    group: Dict[str, Any],
    semester: str,
    identifier: str,
    has_topic: bool
) -> Dict[str, Any]:
    """
    Get the enroll group data.
    """
    enroll_group = {} 
    enroll_group["grpIdentifier"] = identifier
    enroll_group["hasTopic"] = has_topic
    enroll_group["grpSmst"] = [semester]
    enroll_group["credits"] = parse_credit(group["unitsMaximum"], group["unitsMinimum"])
    enroll_group["grading"] = group["gradingBasis"]
    enroll_group["components"] = group["componentsRequired"]
    if group["componentsOptional"]:
        enroll_group["componentsOptional"] = group["componentsOptional"]
    enroll_group["instructors"] = {semester: get_instructors(group)}
    
    location_conflicts = get_location_conflicts(group)
    if location_conflicts:
        enroll_group["locationConflicts"] = True
    
    consent = get_consent_type(group)
    if consent != "N":
        enroll_group["consent"] = consent
    
    if group["sessionCode"] != "1":
        enroll_group["session"] = group["sessionCode"]
        
    enroll_group["sections"] = [get_sections(group, semester)]
    
    combined_groups = get_combined_groups(group)
    if combined_groups:
        enroll_group["comb"] = combined_groups
    
    mode = get_instruction_mode(group)
    if mode != "P":
        enroll_group["mode"] = mode
    
    notes = get_section_notes(group)
    limitations = get_limitations(notes)
    if limitations:
        enroll_group["limitation"] = limitations
    
    prerequisites = get_grp_prerequisites(notes)
    if prerequisites["prereq"]:
        enroll_group["grpPrereq"] = prerequisites["prereq"]
    if prerequisites["coreq"]:
        enroll_group["grpCoreq"] = prerequisites["coreq"]
    if prerequisites["preco"]:
        enroll_group["grpPreco"] = prerequisites["preco"]
    if prerequisites["needNote"]:
        enroll_group["needNote"] = prerequisites["needNote"]
    
    return enroll_group


def add_early_semester(
    existing_course_data: Dict[str, Any], 
    semester: str) -> List[str]:
    """
    Add a new semester to the course's semester list if it doesn't already exist.
    
    Args:
        existing_course_data: The existing course data dictionary
        semester: The new semester to add
        
    Returns:
        Updated list of semesters
    """
    # Create a new list to avoid modifying the original
    semesters = list(existing_course_data.get("smst", []))
    if semester not in semesters:
        semesters.append(semester)
    return semesters


def add_early_group_data(
    existing_group_data: Dict[str, Any], 
    early_semester_group_data: Dict[str, Any],
    semester: str) -> Dict[str, Any]:
    """
    Add early semester data to an existing enrollment group.
    
    Args:
        existing_group_data: The existing group data dictionary
        early_semester_group_data: The new group data for the early semester
        semester: The early semester string
        
    Returns:
        Updated group data dictionary
    """
    # Create a copy of the existing data to avoid modifying the original
    updated_group = existing_group_data.copy()
    
    # 1. Add the early semester to grpSmst list
    if semester not in updated_group["grpSmst"]:
        updated_group["grpSmst"].append(semester)
    
    # 2. Add instructors for the early semester
    if "instructors" not in updated_group:
        updated_group["instructors"] = {}
    updated_group["instructors"][semester] = get_instructors(early_semester_group_data)
    
    # 3. Add sections for the early semester
    if semester in CURRENT_YEAR:
        if "sections" not in updated_group:
            updated_group["sections"] = []
        updated_group["sections"].append(get_sections(early_semester_group_data, semester))
    
    return updated_group


def get_group_identifier(group: Dict[str, Any]) -> tuple[str, bool]:
    """
    Get the identifier for an enrollment group based on priority rules:
    1. If any section has a topic, use that topic
    2. If no topic and has IND section, use first instructor's last name
    3. Otherwise, use first section's key
    
    Args:
        group: The enrollment group dictionary
        
    Returns:
        tuple containing:
            - identifier string
            - boolean indicating if the identifier is from a topic
    """
    # Check all sections for a topic
    for section in group.get("classSections", []):
        if section.get("topicDescription"):
            return section["topicDescription"], True
    
    # Check for IND section and get first instructor's last name
    for section in group.get("classSections", []):
        if section.get("ssrComponent") == "IND":
            # Get first instructor's last name from any meeting
            for meeting in section.get("meetings", []):
                for instructor in meeting.get("instructors", []):
                    if instructor.get("lastName"):
                        return instructor["lastName"], False
    
    # Default to first section's key
    if group.get("classSections"):
        first_section = group["classSections"][0]
        return f"{first_section['ssrComponent']}-{first_section['section']}", False
    
    # Fallback if no sections exist (shouldn't happen in practice)
    return "", False


def get_instructors(group: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Extract instructor information from an enrollment group.
    
    Args:
        group: The enrollment group dictionary from the API
        
    Returns:
        List of instructor dictionaries with netid and name
    """
    instructors = []
    seen_netids = set()  # To avoid duplicates
    
    # Iterate through all sections in the group
    for section in group.get("classSections", []):
        # Iterate through all meetings in the section
        for meeting in section.get("meetings", []):
            # Process each instructor in the meeting
            for instructor in meeting.get("instructors", []):
                netid = instructor.get("netid", "")
                if not netid or netid in seen_netids:
                    continue
                    
                # Build full name
                first_name = instructor.get("firstName", "")
                middle_name = instructor.get("middleName", "")
                last_name = instructor.get("lastName", "")
                
                # Combine name parts, filtering out empty strings
                name_parts = [first_name]
                if middle_name:
                    name_parts.append(middle_name)
                name_parts.append(last_name)
                full_name = " ".join(filter(None, name_parts))
                
                # Add instructor to list
                instructors.append({
                    "netid": netid,
                    "name": full_name
                    # rmp and rmpid will be added later if available
                })
                
                seen_netids.add(netid)
    
    return instructors


def get_location_conflicts(group: Dict[str, Any]) -> bool:
    """
    Check if any section in the group has a location in the specified list.
    
    Args:
        group: The enrollment group dictionary
        
    Returns:
        True if any section's location is in ["ARNYC", "BEIJING", "DC", "NYCTECH", "ROME"]
        False otherwise
    """
    conflict_locations = {"ARNYC", "BEIJING", "DC", "NYCTECH", "ROME"}
    
    # Check all sections in the group
    for section in group.get("classSections", []):
        if section.get("location") in conflict_locations:
            return True
            
    return False


def get_consent_type(group: Dict[str, Any]) -> str:
    """
    Check consent type across all sections in the group.
    
    Args:
        group: The enrollment group dictionary
        
    Returns:
        "D" if any section has consent type "D" (department)
        "I" if any section has consent type "I" (instructor) and no "D" found
        "N" if neither "D" nor "I" is found (no consent required)
    """
    # Check all sections in the group
    for section in group.get("classSections", []):
        consent = section.get("addConsent")
        if consent == "D":
            return "D"  # Return immediately if found
        elif consent == "I":
            return "I"  # Return immediately if found
            
    return "N"  # Default if neither D nor I found


def get_sections(group: Dict[str, Any], semester: str) -> Dict[str, Any]:
    """
    Get section information for an enrollment group.
    
    Args:
        group: The enrollment group dictionary
        semester: The semester code
        
    Returns:
        Dictionary containing:
            - semester: string
            - sections: Array of section dictionaries with:
                - tp: section type (LEC, LAB, DIS, IND, etc.)
                - nbr: section number
                - open: optional status (C for closed, W for waitlist)
                - mode: optional instruction mode
                - location: optional location (only if not in Ithaca)
    """
    sections_data = {
        "semester": semester,
        "secInfo": []
    }
    
    # Process each section in the group
    for section in group.get("classSections", []):
        section_info = {
            "type": section.get("ssrComponent", ""),
            "nbr": section.get("section", ""),
            "meetings": []
        }
        
        # Get time information from meetings
        for i in range(len(section.get("meetings", []))):
            meeting = section.get("meetings", [])[i]
            meeting_data = {
                "no": i + 1,
                "stTm": meeting.get("timeStart"),
                "edTm": meeting.get("timeEnd"),
                "stDt": meeting.get("startDt"),
                "edDt": meeting.get("endDt"),
                "pt": meeting.get("pattern"),
                "instructors": [instructor.get("netid") for instructor in meeting.get("instructors", [])]
            }
            
            # Add topic if meetingTopicDescription exists
            if meeting.get("meetingTopicDescription"):
                meeting_data["topic"] = meeting.get("meetingTopicDescription")
                
            section_info["meetings"].append(meeting_data)
        
        # Add open status if not "O" (open)
        if section.get("openStatus") != "O":
            section_info["open"] = section["openStatus"]
        
        # Add instruction mode if not "P" (in-person)
        if section.get("instructionMode") != "P":
            section_info["mode"] = section["instructionMode"]
        
        # Add location if not in Ithaca
        if section.get("location") and section["location"] != "ITH":
            section_info["location"] = section["location"]
        
        sections_data["secInfo"].append(section_info)
    
    return sections_data


def get_combined_groups(group: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Get combined course information from the group.
    
    Args:
        group: The enrollment group dictionary
        
    Returns:
        List of dictionaries containing:
            - courseId: string (subject + catalog number)
            - type: string (combination type)
    """
    combined_groups = []
    
    # Process each combination in the group
    for comb in group.get("simpleCombinations", []):
        # Create the courseId by combining subject and catalog number
        course_id = f"{comb.get('subject', '')}{comb.get('catalogNbr', '')}"
        
        # Add to list if we have both required fields
        if course_id and comb.get("type"):
            combined_groups.append({
                "courseId": course_id,
                "type": comb["type"]
            })
    
    return combined_groups


def get_instruction_mode(group: Dict[str, Any]) -> str:
    """
    Get the instruction mode for the group.
    
    Args:
        group: The enrollment group dictionary
        
    Returns:
        The first non-"P" mode found in any section, or "P" if all sections are in-person
    """
    # Check all sections in the group
    for section in group.get("classSections", []):
        mode = section.get("instructionMode")
        if mode and mode != "P":
            return mode
            
    return "P"  # Default if all sections are in-person or no sections


def get_section_notes(group: Dict[str, Any]) -> List[str]:
    """
    Get all notes from all sections in the group.
    
    Args:
        group: The enrollment group dictionary
        
    Returns:
        List of note strings from all sections
    """
    section_notes = []
    
    # Process each section in the group
    for section in group.get("classSections", []):
        # Get notes from the section
        for note in section.get("notes", []):
            if note.get("descrlong"):
                section_notes.append(note["descrlong"])
    
    return section_notes


def get_limitations(notes: List[str]) -> str:
    """
    Extract limitation text from notes that contain "Enrollment limited to: ".
    
    Args:
        notes: List of note strings
        
    Returns:
        The limitation text (words after "Enrollment limited to: " until first period or end)
        Empty string if no limitation found
    """
    for note in notes:
        if "Enrollment limited to: " in note:
            # Get the text after "Enrollment limited to: "
            limitation = note.split("Enrollment limited to: ")[1]
            # Get text until first period or end
            limitation = limitation.split(".")[0]
            return limitation.strip()
            
    return ""  # Return empty string if no limitation found


def get_grp_prerequisites(notes: List[str]) -> Dict[str, str]:
    """
    Extract all prerequisite information from notes in a single pass.
    
    Args:
        notes: List of note strings
        
    Returns:
        Dictionary containing:
            - prereq: JSON string of prerequisite requirements
            - coreq: JSON string of corequisite requirements
            - preco: JSON string of prerequisite or corequisite requirements
            - needNote: boolean indicating if additional notes are needed
    """
    result = {
        "prereq": "",
        "coreq": "",
        "preco": "",
        "needNote": False
    }
    
    for note in notes:
        if has_preco(note):
            preco_dict = parse_preco(note)
            if preco_dict["prereq"]:
                result["prereq"] = json.dumps(preco_dict["prereq"])
            if preco_dict["coreq"]:
                result["coreq"] = json.dumps(preco_dict["coreq"])
            if preco_dict["preco"]:
                result["preco"] = json.dumps(preco_dict["preco"])
            result["needNote"] = preco_dict["note"]
            break  # Stop after finding the first note with prerequisite information
            
    return result


if __name__ == "__main__":
    SEMESTERS = ["FA25", "SU25", "SP25", "WI25", "FA24", "SU24", "SP24"] # completed
    for semester in SEMESTERS:
        subjects, courses = fetch_subjects_courses(semester)
        upload_subjects(subjects, semester)
        upload_courses(courses, semester)
        print(f"Completed processing for {semester}")
