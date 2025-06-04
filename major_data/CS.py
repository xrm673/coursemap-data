from common import *  # This initializes Firebase
from service import *  # This uses Firebase after initialization


def commit_CS():
    major = {
        "_id": "CS",
        "name": "Computer Science",
        "needsYear": True,
        "needsCollege": True,
        "colleges": [
            {"collegeId": "CAS", "name": "College of Arts and Sciences"},
            {"collegeId": "COE", "name": "College of Engineering"},
        ],
        "numberOfRequiredCourses": None,
        "rawBasicRequirements": [
            {
                "collegeId": "CAS",
                "year": "2026",
                "requirements": ["cs1", "cs2", "cs5", "cs7", "cs8", "cs9"],
            },
            {
                "collegeId": "CAS",
                "year": "2027",
                "requirements": ["cs1", "cs2", "cs5", "cs7", "cs8", "cs9"],
            },
            {
                "collegeId": "CAS",
                "year": "2028",
                "requirements": ["cs1", "cs2", "cs4", "cs6", "cs9"],
            },
            {
                "collegeId": "CAS",
                "year": "2029",
                "requirements": ["cs1", "cs2", "cs4", "cs6", "cs9"],
            },
            {
                "collegeId": "COE",
                "year": "2026",
                "requirements": ["cs1", "cs3", "cs5", "cs7", "cs8", "cs9"],
            },
            {
                "collegeId": "COE",
                "year": "2027",
                "requirements": ["cs1", "cs3", "cs5", "cs7", "cs8", "cs9"],
            },
            {
                "collegeId": "COE",
                "year": "2028",
                "requirements": ["cs1", "cs3", "cs4", "cs6", "cs9"],
            },
            {
                "collegeId": "COE",
                "year": "2029",
                "requirements": ["cs1", "cs3", "cs4", "cs6", "cs9"],
            },
        ],
        "onboardingCourses": [
            "CS1110",
            "CS1112",
            "CS2110",
            "CS2800",
            "CS3110",
            "MATH1120",
            "MATH2210",
            "MATH1910",
            "MATH1920",
        ],
    }
    add_major(major)

    req1 = {
        "_id": "cs1",
        "type": "C",
        "majorId": "CS",
        "name": "Intro Programming",
        "descr": [
            "Take two introductory programming courses CS 111X and CS 2110 (or equivalent).",
        ],
        "numberOfRequiredCourses": 2,
        "courseGrps": [
            {"_id": 1, "courseIds": ["CS1110", "CS1112"]},
            {"_id": 2, "courseIds": ["CS2110", "CS2112"]},
        ],
        "overlap": ["cs2", "cs3", "cs4", "cs5", "cs6", "cs7", "cs9"],
        "note": None,
    }
    add_requirement(req1)

    # math requirement for A&S students
    req2 = {
        "_id": "cs2",
        "type": "C",
        "majorId": "CS",
        "name": "Math",
        "descr": [
            "Take a calculus sequence of 3 courses.",
            "A&S students can take either MATH 1110-1120-2210 sequence or MATH 1910-1920-2940 sequence.",
        ],
        "numberOfRequiredCourses": 3,
        "courseGrps": [
            {"_id": 1, "courseIds": ["MATH1110", "MATH1910"]},
            {"_id": 2, "courseIds": ["MATH1120", "MATH1920"]},
            {"_id": 3, "courseIds": ["MATH2210", "MATH2940"]},
        ],
        "overlap": ["cs1", "cs3", "cs4", "cs5", "cs6", "cs7", "cs9"],
        "note": None,
    }
    add_requirement(req2)

    # math requirement for Engineering students
    req3 = {
        "_id": "cs3",
        "type": "C",
        "majorId": "CS",
        "name": "Engineering Math",
        "descr": [
            "Take a calculus sequence of 3 courses.",
            "Engineering students can only take MATH 1910-1920-2940 sequence.",
        ],
        "numberOfRequiredCourses": 3,
        "courseGrps": [
            {"_id": 1, "courseIds": ["MATH1910"]},
            {"_id": 2, "courseIds": ["MATH1920"]},
            {"_id": 3, "courseIds": ["MATH2940"]},
        ],
        "overlap": ["cs1", "cs2", "cs4", "cs5", "cs6", "cs7", "cs9"],
        "note": None,
    }
    add_requirement(req3)

    # core requirement for 2028 and after-2028 students
    req4 = {
        "_id": "cs4",
        "type": "C",
        "majorId": "CS",
        "name": "Core",
        "descr": [
            "All FA24 and later matriculants must take one course from each of the following course group listed below.",
        ],
        "numberOfRequiredCourses": 6,
        "courseGrps": [
            {"_id": 1, "courseIds": ["CS2800", "CS2802"]},
            {"_id": 2, "courseIds": ["CS3110"]},
            {"_id": 3, "courseIds": ["CS3410", "CS3420"]},
            {"_id": 4, "courseIds": ["CS3700", "CS3780"]},
            {"_id": 5, "courseIds": ["CS4410", "CS4414"]},
            {"_id": 6, "courseIds": ["CS4820"]},
        ],
        "overlap": ["cs1", "cs2", "cs3", "cs5", "cs6", "cs7", "cs9"],
        "note": None,
    }
    add_requirement(req4)

    # core requirement for 2027 and pre-2027 students
    req5 = {
        "_id": "cs5",
        "type": "C",
        "majorId": "CS",
        "name": "Core",
        "descr": [
            "All Pre FA24 matriculants must take one course from each of the following course group listed below.",
        ],
        "numberOfRequiredCourses": 5,
        "courseGrps": [
            {"_id": 1, "courseIds": ["CS2800", "CS2802"]},
            {"_id": 2, "courseIds": ["CS3110"]},
            {"_id": 3, "courseIds": ["CS3410", "CS3420"]},
            {"_id": 4, "courseIds": ["CS4410", "CS4414"]},
            {"_id": 5, "courseIds": ["CS4820"]},
        ],
        "overlap": ["cs1", "cs2", "cs3", "cs4", "cs6", "cs7", "cs9"],
        "note": None,
    }
    add_requirement(req5)

    # cs electives for 2028 and after-2028 students
    req6_courses = get_courses_by_subject_min_level(
        "CS",
        min_level=4,
        min_credit=3,
        excluded=["CS4090", "CS4998", "CS4999"],
        included=["CS3700", "CS3780"],
    )
    req6 = {
        "_id": "cs6",
        "type": "E",
        "majorId": "CS",
        "name": "Elective",
        "descr": [
            "All FA24 and later matriculants must take two CS 4000+ courses (3+ credits each).",
            "CS 4090, CS 4998, and CS 4999 are NOT allowed. CS 3700 or CS 3780 allowed if not used in CS core.",
        ],
        "numberOfRequiredCourses": 2,
        "courseIds": req6_courses,
        "overlap": ["cs1", "cs2", "cs3", "cs4", "cs5", "cs7", "cs9"],
        "note": None,
    }
    add_requirement(req6)

    # cs electives for 2027 and pre-2027 students
    req7_courses = get_courses_by_subject_min_level(
        "CS",
        min_level=4,
        min_credit=3,
        excluded=["CS4090", "CS4998", "CS4999"],
        included=["CS3700", "CS3780"],
    )
    req7 = {
        "_id": "cs7",
        "type": "E",
        "majorId": "CS",
        "name": "Electives",
        "descr": [
            "All pre-fall 2024 matriculants must take three CS 4000+ courses (3+ credits each).",
            "CS 4090, CS 4998, and CS 4999 are NOT allowed. CS 3700 or CS 3780 allowed if not used in CS core.",
        ],
        "numberOfRequiredCourses": 3,
        "courseIds": req7_courses,
        "overlap": ["cs1", "cs2", "cs3", "cs4", "cs5", "cs6", "cs9"],
        "note": None,   
    }
    add_requirement(req7)

    # probability course for 2027 and pre-2027 students
    req8 = {
        "_id": "cs8",
        "type": "E",
        "majorId": "CS",
        "name": "Probability",
        "descr": [
            "All pre-fall 2024 matriculants must take one CS-approved Probability course.",
            "This probability course can be used to satisfy another major requirement.",
        ],
        "numberOfRequiredCourses": 1,
        "courseIds": ["BTRY3080", "STSCI3080", "CS4850", "ECE3100", "ECON3130", 
                    "ENGRD2700", "MATH4710"],
        "note": None,
    }
    add_requirement(req8)

    req9_courses = get_CS_practicum(included=["CS3152", "CS4152", "CS4154", "CS4740", "CS4752", 
                                              "CS5150", "CS5152", "CS5412", "CS5414", "CS5431", 
                                              "CS5625", "CS5643"])
    req9 = {
        "_id": "cs9",
        "type": "E",
        "majorId": "CS",
        "name": "Practicum or Project",
        "descr": [
            "Accepted courses are CS practicums (CS 4xx1), or CS 3152, CS 4152, CS 4154, CS 4740, CS 4752, CS 5150, CS 5152, CS 5412, CS 5414, CS 5431, CS 5625, or CS 5643.",
        ],
        "numberOfRequiredCourses": 1,
        "courseIds": req9_courses,
        "overlap": ["cs1", "cs2", "cs3", "cs4", "cs5", "cs6", "cs7"],
        "note": None,
    }
    add_requirement(req9)
    
def get_CS_practicum(included=[]):
    course_ids = []
    CS_4000 = get_courses_by_subject_level(subject="CS", level=4)
    for course_id in CS_4000:
        if course_id[-1] == "1":
            course_ids.append(course_id)
    course_ids.extend(included)
    return course_ids 


if __name__ == "__main__":
    commit_CS() 