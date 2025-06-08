# if the course does not exist in the database,
# initialize the course data
# if the course exists in the database,
# update the course data

from pymongo import MongoClient, UpdateOne, InsertOne
from dotenv import load_dotenv
import certifi
import os
import requests
from typing import List, Dict, Any, Tuple
from const import *
from parse_text import *

load_dotenv()
mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri, tlsCAFile=certifi.where())  # Add SSL certificate verification
db = client["CourseMap"]
courses_collection = db["courses"]
subjects_collection = db["subjects"]
instructors_collection = db["instructors"]


def setup_indexes():
    """
    Set up MongoDB indexes for better query performance.
    """
    # Courses indexes
    courses_collection.create_index([("ttl", 1)])  # Title index
    courses_collection.create_index([("distr", 1)])  # Distribution index
    courses_collection.create_index([("enrollGroups.grpIdentifier", 1)])  # Enrollment group index
    
    # Instructors index
    instructors_collection.create_index([("netid", 1)], unique=True)

# Call setup_indexes when module is imported
setup_indexes()


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
        subject_id = subject["value"]
        course_url = f"https://classes.cornell.edu/api/2.0/search/classes.json?roster={semester}&subject={subject_id}"
        course_response = requests.get(course_url)

        if (
            course_response.status_code == 200
            and course_response.json()["status"] == "success"
        ):
            courses = course_response.json()["data"]["classes"]
            all_courses.extend(courses)
            print(f"Fetched {len(courses)} courses for {subject_id} in {semester}")

    return subjects, all_courses


def upload_subjects(subjects: List[Dict[str, Any]], semester: str) -> None:
    """
    Process subject data and upload to MongoDB.
    Only adds subjects that don't already exist.

    Args:
        subjects: List of subject data from the API
        semester: The semester code (e.g., "SP25")
    """
    subjects_added = 0

    for subject in subjects:
        subject_id = subject["value"]

        # Check if subject exists
        existing_subject = subjects_collection.find_one({"_id": subject_id})
        
        if existing_subject:
            # Subject exists, update the semesters array if needed
            if semester not in existing_subject.get("semesters", []):
                subjects_collection.update_one(
                    {"_id": subject_id},
                    {"$addToSet": {"semesters": semester}}
                )
        else:
            # Subject doesn't exist, add it
            subject_data = {
                "_id": subject_id,
                "name": subject["descr"],
                "formalName": subject["descrformal"],
                "semesters": [semester]
            }
            
            subjects_collection.insert_one(subject_data)
            subjects_added += 1

    print(f"Added {subjects_added} new subjects for {semester}")
    
    
def upload_courses(courses: List[Dict[str, Any]], semester: str, batch_size: int = 100) -> None:
    """
    Process course data and upload to MongoDB with semester tracking.
    Includes enrollment groups, sections, meetings, and instructors.

    Args:
        courses: List of course data from the API
        semester: The semester code (e.g., "SP25")
        batch_size: Number of operations to batch together (default: 100)
    """
    bulk_operations = []
    instructor_operations = []
    
    for course in courses:
        try:
            course_id = f"{course['subject']}{course['catalogNbr']}"
            
            # Check if any group has a topic
            has_topic = False
            for group in course.get("enrollGroups", []):
                _, is_topic = get_group_identifier(group)
                if is_topic:
                    has_topic = True
                    break
            
            # Check if course exists to determine update strategy
            existing_course = courses_collection.find_one({"_id": course_id})
            
            if not existing_course:
                # New course - prepare complete course document
                course_data = initialize_single_course(course, semester)
                course_data["_id"] = course_id  # Use _id instead of id
                course_data["enrollGroups"] = []
                
                # Add all enrollment groups
                for enroll_group in course.get("enrollGroups", []):
                    identifier, has_topic = get_group_identifier(enroll_group)
                    group_data = initialize_enroll_group(enroll_group, semester, identifier, has_topic, instructor_operations)
                    course_data["enrollGroups"].append(group_data)
                
                # Insert new course
                bulk_operations.append(
                    InsertOne(course_data)
                )
            else:
                # Existing course - update semester and courseHasTopic if needed
                update_fields = {"$addToSet": {"smst": semester}}
                if has_topic and not existing_course.get("courseHasTopic"):
                    update_fields["$set"] = {"courseHasTopic": True}
                
                semester_update = UpdateOne(
                    {"_id": course_id},
                    update_fields
                )
                bulk_operations.append(semester_update)
                
                # Process each enrollment group
                for enroll_group in course.get("enrollGroups", []):
                    identifier, has_topic = get_group_identifier(enroll_group)
                    group_data = initialize_enroll_group(enroll_group, semester, identifier, has_topic, instructor_operations)
                    
                    # Check if this group exists
                    group_exists = any(
                        group.get("grpIdentifier") == identifier 
                        for group in existing_course.get("enrollGroups", [])
                    )
                    
                    if group_exists:
                        # Update existing group
                        group_update = UpdateOne(
                            {
                                "_id": course_id,
                                "enrollGroups.grpIdentifier": identifier
                            },
                            {
                                "$addToSet": {
                                    "enrollGroups.$.grpSmst": semester
                                },
                                "$push": {
                                    "enrollGroups.$.instructorHistory": {
                                        "semester": semester,
                                        "instructors": group_data["instructorHistory"][0]["instructors"]
                                    },
                                    "enrollGroups.$.sections": {
                                        "$each": group_data["sections"]
                                    }
                                }
                            }
                        )
                    else:
                        # Add new group
                        group_update = UpdateOne(
                            {"_id": course_id},
                            {"$push": {"enrollGroups": group_data}}
                        )
                    
                    bulk_operations.append(group_update)
            
            # Execute batch if we've reached batch_size
            if len(bulk_operations) >= batch_size or len(instructor_operations) >= batch_size:
                try:
                    # First upload instructors
                    if instructor_operations:
                        instructors_collection.bulk_write(instructor_operations, ordered=False)
                        print(f"Uploaded {len(instructor_operations)} instructor operations")
                        instructor_operations = []
                    
                    # Then upload courses
                    if bulk_operations:
                        courses_collection.bulk_write(bulk_operations, ordered=False)
                        print(f"Processed batch of {len(bulk_operations)} course operations")
                        bulk_operations = []
                except Exception as e:
                    print(f"Error executing batch operations: {str(e)}")
                    # Clear the failed batches and continue
                    bulk_operations = []
                    instructor_operations = []
                
            print(f"Processed course {course_id} for {semester}")
                
        except Exception as e:
            print(f"Error processing course {course_id}: {str(e)}")
    
    # Process any remaining operations
    if instructor_operations or bulk_operations:
        try:
            if instructor_operations:
                instructors_collection.bulk_write(instructor_operations, ordered=False)
                print(f"Uploaded final {len(instructor_operations)} instructor operations")
            
            if bulk_operations:
                courses_collection.bulk_write(bulk_operations, ordered=False)
                print(f"Processed final batch of {len(bulk_operations)} course operations")
        except Exception as e:
            print(f"Error processing final batch: {str(e)}")


def initialize_single_course(course: Dict[str, Any], semester: str) -> Dict[str, Any]:
    """
    Initialize a new course document.
    
    Args:
        course: The course dictionary from the API
        semester: The semester code
        
    Returns:
        Dictionary containing the course data
    """
    single_course = {}
    course_id = course["subject"] + course["catalogNbr"]

    single_course["_id"] = course_id  # Use _id instead of id
    single_course["sbj"] = course["subject"]
    single_course["nbr"] = course["catalogNbr"]
    single_course["lvl"] = int(course["catalogNbr"][0])
    single_course["smst"] = [semester]
    single_course["ttl"] = course["titleLong"]
    single_course["tts"] = course["titleShort"]
    single_course["dsrpn"] = clean(course["description"])
    
    # Check if any enrollment group has a topic using get_group_identifier
    has_topic = False
    for group in course.get("enrollGroups", []):
        _, is_topic = get_group_identifier(group)
        if is_topic:
            has_topic = True
            break
    if has_topic:
        single_course["courseHasTopic"] = True
    
    if course["catalogDistr"]:
        single_course["distr"] = parse_distr(course["catalogDistr"])
    if course["catalogOutcomes"]:
        single_course["otcm"] = clean_list(course["catalogOutcomes"])
    
    eligibility = {}
    req = clean(course["catalogPrereqCoreq"])
    cmts = clean(course["catalogComments"])
    if cmts:
        if has_recommend_preco(cmts):
            # comment that has recommended prerequisite info
            eligibility["rcmdReq"] = cmts
        elif has_preco(cmts) and not req:
            # comment that has prerequisite info
            req = cmts
        else:
            # regular comments that don't have any prerequisite info
            eligibility["cmts"] = cmts
    if req:
        eligibility["req"] = req
        preco_dict = parse_preco(req)
        if preco_dict["prereq"]:
            eligibility["prereq"] = nested_list_to_dict_list(preco_dict["prereq"])
        if preco_dict["coreq"]:
            eligibility["coreq"] = nested_list_to_dict_list(preco_dict["coreq"])
        if preco_dict["preco"]:
            eligibility["preco"] = nested_list_to_dict_list(preco_dict["preco"])
        eligibility["needNote"] = preco_dict["note"]
    if course["catalogLang"]:
        eligibility["lanreq"] = clean(course["catalogLang"])
    if course["catalogForbiddenOverlaps"]:
        eligibility["ovlpText"] = clean(course["catalogForbiddenOverlaps"])
        eligibility["ovlp"] = parse_overlap(course["catalogForbiddenOverlaps"])
    if course["catalogPermission"]:
        eligibility["pmsn"] = course["catalogPermission"]
    single_course["eligibility"] = eligibility

    metadata = {}
    if course["catalogWhenOffered"]:
        metadata["when"] = parse_when_offered(course["catalogWhenOffered"])
    if course["catalogBreadth"]:
        metadata["breadth"] = course["catalogBreadth"]
    if course["catalogAttribute"]:
        metadata["attr"] = parse_distr(course["catalogAttribute"])
    if course["catalogFee"]:
        metadata["fee"] = clean(course["catalogFee"])
    if course["catalogSatisfiesReq"]:
        metadata["satisfies"] = clean(course["catalogSatisfiesReq"])
    if course["catalogCourseSubfield"]:
        metadata["subfield"] = clean(course["catalogCourseSubfield"])
    metadata["career"] = course["acadCareer"]
    metadata["acadgrp"] = course["acadGroup"]
    single_course["metadata"] = metadata
    return single_course


def initialize_enroll_group(
    group: Dict[str, Any],
    semester: str,
    identifier: str,
    has_topic: bool,
    instructor_operations: List[UpdateOne] = None
) -> Dict[str, Any]:
    """
    Get the enroll group data.
    """
    enroll_group = {} 
    enroll_group["grpIdentifier"] = identifier
    enroll_group["hasTopic"] = has_topic
    if has_topic:
        enroll_group["topic"] = identifier
    enroll_group["grpSmst"] = [semester]
    enroll_group["credits"] = parse_credit(group["unitsMaximum"], group["unitsMinimum"])
    enroll_group["grading"] = group["gradingBasis"]
    enroll_group["components"] = group["componentsRequired"]
    if group["componentsOptional"]:
        enroll_group["componentsOptional"] = group["componentsOptional"]
    enroll_group["instructorHistory"] = [{"semester": semester, "instructors": get_instructors(group, instructor_operations)}]
    
    location_conflicts = get_location_conflicts(group)
    if location_conflicts:
        enroll_group["locationConflicts"] = True
    
    consent = get_consent_type(group)
    if consent != "N":
        enroll_group["consent"] = consent
    
    if group["sessionCode"] != "1":
        enroll_group["session"] = group["sessionCode"]
        
    enroll_group["sections"] = get_sections(group, semester)
    
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
    if "instructorHistory" not in updated_group:
        updated_group["instructorHistory"] = []
    updated_group["instructorHistory"].append({
        "semester": semester, 
        "instructors": get_instructors(early_semester_group_data)
    })
    
    # 3. Add sections for the early semester
    if semester in CURRENT_YEAR:
        sections = get_sections(early_semester_group_data, semester)
        if not updated_group.get("sections"):
            updated_group["sections"] = []
        updated_group["sections"].extend(sections)
    
    return updated_group


def get_group_identifier(group: Dict[str, Any]) -> tuple[str, bool]:
    """
    Get the identifier for an enrollment group based on priority rules:
    1. If any section has a topic, use that topic
    2. If no topic and has IND section, use first instructor's netid
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
    
    # Check for IND section and get first instructor's netid
    for section in group.get("classSections", []):
        if section.get("ssrComponent") == "IND":
            # Get first instructor's netid from any meeting
            for meeting in section.get("meetings", []):
                for instructor in meeting.get("instructors", []):
                    if instructor.get("netid"):
                        return instructor["netid"], False
    
    # Default to first section's key
    if group.get("classSections"):
        first_section = group["classSections"][0]
        return f"{first_section['ssrComponent']}-{first_section['section']}", False
    
    # Fallback if no sections exist (shouldn't happen in practice)
    return "", False


def get_instructors(group: Dict[str, Any], instructor_operations: List[UpdateOne] = None) -> List[Dict[str, Any]]:
    """
    Extract instructor data from an enrollment group.
    
    Args:
        group: The enrollment group dictionary from the API
        instructor_operations: List to collect instructor bulk operations
        
    Returns:
        List of unique instructor data dictionaries
    """
    instructors = {}  # Use dict for deduplication since dicts aren't hashable
    
    # Iterate through all sections in the group
    for section in group.get("classSections", []):
        # Iterate through all meetings in the section
        for meeting in section.get("meetings", []):
            # Process each instructor in the meeting
            for instructor in meeting.get("instructors", []):
                netid = instructor.get("netid")
                if netid:  # Only process instructors with netids
                    instructor_data = {
                        "netid": netid,
                        "lNm": instructor.get("lastName", ""),
                        "fNm": instructor.get("firstName", ""),
                        "mNm": instructor.get("middleName", "")
                    }
                    if instructor_operations is not None:
                        prepare_instructor_operation(instructor_data, instructor_operations)
                    instructors[netid] = instructor_data  # Use netid as key for deduplication
    
    return list(instructors.values())  # Return just the list of instructor data dictionaries


def prepare_instructor_operation(instructor: Dict[str, Any], instructor_operations: List[UpdateOne]) -> None:
    """
    Prepare a bulk operation for instructor upload.
    
    Args:
        instructor: Dictionary containing instructor data from the API
        instructor_operations: List to collect instructor bulk operations
    """
    netid = instructor.get("netid")
    if not netid:
        return
        
    instructor_data = {
        "netid": netid,
        "lNm": instructor.get("lNm", ""),
        "fNm": instructor.get("fNm", ""),
        "mNm": instructor.get("mNm", "")
    }
    
    # Use upsert to handle both insert and update cases
    instructor_operations.append(
        UpdateOne(
            {"netid": netid},
            {"$set": instructor_data},
            upsert=True
        )
    )


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
    result = []
    
    # Process each section in the group
    for section in group.get("classSections", []):
        section_data = {
            "semester": semester,
            "type": section.get("ssrComponent", ""),
            "nbr": section.get("section", ""),
            "meetings": []
        }
        
        # Get time information from meetings
        for i in range(len(section.get("meetings", []))):
            meeting = section.get("meetings", [])[i]
            meeting_data = {
                "stTm": meeting.get("timeStart"),
                "edTm": meeting.get("timeEnd"),
                "stDt": meeting.get("startDt"),
                "edDt": meeting.get("endDt"),
                "pt": meeting.get("pattern"),
            }
            
            # Add topic if meetingTopicDescription exists
            if meeting.get("meetingTopicDescription"):
                meeting_data["topic"] = meeting.get("meetingTopicDescription")
                
            section_data["meetings"].append(meeting_data)
        
        # Add open status if not "O" (open)
        if section.get("openStatus") != "O":
            section_data["open"] = section["openStatus"]
        
        # Add instruction mode if not "P" (in-person)
        if section.get("instructionMode") != "P":
            section_data["mode"] = section["instructionMode"]
        
        # Add location if not in Ithaca
        if section.get("location") and section["location"] != "ITH":
            section_data["location"] = section["location"]
        
        result.append(section_data)
    
    return result


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
                result["prereq"] = nested_list_to_dict_list(preco_dict["prereq"])
            if preco_dict["coreq"]:
                result["coreq"] = nested_list_to_dict_list(preco_dict["coreq"])
            if preco_dict["preco"]:
                result["preco"] = nested_list_to_dict_list(preco_dict["preco"])
            result["needNote"] = preco_dict["note"]
            break  # Stop after finding the first note with prerequisite information
            
    return result


if __name__ == "__main__":
    SEMESTERS = ["FA25", "SU25", "SP25", "WI25"]
    for semester in SEMESTERS:
        subjects, courses = fetch_subjects_courses(semester)
        upload_subjects(subjects, semester)
        upload_courses(courses, semester)
        print(f"Completed processing for {semester}")
