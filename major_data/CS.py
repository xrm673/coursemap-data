from service import *
from common import *


def commit_CS():
    major = {
        "id": "CS",
        "name": "Computer Science",
        "colleges": [
            {"id": "CAS", "name": "Arts and Sciences"},
            {"id": "COE", "name": "Cornell Engineering"},
        ],
        "requiredCourses": None,
        "basicRequirements": [
            {
                "college": "CAS",
                "year": 2026,
                "requirements": [
                    "CS_req1",
                    "CS_req2",
                    "CS_req5",
                    "CS_req7",
                    "CS_req8",
                    "CS_req9",
                ]
            },
            {
                "college": "CAS",
                "year": 2027,
                "requirements": [
                    "CS_req1",
                    "CS_req2",
                    "CS_req5",
                    "CS_req7",
                    "CS_req8",
                    "CS_req9",
                ]
            },
            {
                "college": "CAS",
                "year": 2028,
                "requirements": [
                    "CS_req1",
                    "CS_req2",
                    "CS_req4",
                    "CS_req6",
                    "CS_req9",
                ]
            },
            {
                "college": "CAS",
                "year": 2029,
                "requirements": [
                    "CS_req1",
                    "CS_req2",
                    "CS_req4",
                    "CS_req6",
                    "CS_req9",
                ]
            },
            {
                "college": "COE",
                "year": 2026,
                "requirements": [
                    "CS_req1",
                    "CS_req3",
                    "CS_req5",
                    "CS_req7",
                    "CS_req8",
                    "CS_req9",
                ]
            },
            {
                "college": "COE",
                "year": 2027,
                "requirements": [
                    "CS_req1",
                    "CS_req3",
                    "CS_req5",
                    "CS_req7",
                    "CS_req8",
                    "CS_req9",
                ]
            },
            {
                "college": "COE",
                "year": 2028,
                "requirements": [
                    "CS_req1",
                    "CS_req3",
                    "CS_req4",
                    "CS_req6",
                    "CS_req9",
                ]
            },
            {
                "college": "COE",
                "year": 2029,
                "requirements": [
                    "CS_req1",
                    "CS_req3",
                    "CS_req4",
                    "CS_req6",
                    "CS_req9",
                ]
            },
        ],
        "init": [
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
        "id": "CS_req1",
        "type": "C",
        "major": "CS",
        "name": "Introductory Programming",
        "tag": "Intro Programming",
        "tagDescr": "This is a Introductory Programming course of Computer Science major",
        "descr": [
            "Take two introductory programming courses CS 111X and CS 2110 (or equivalent).",
        ],
        "number": 2,
        "courseGrps": [
            {"id": 1, "courses": ["CS1110", "CS1112"]},
            {"id": 2, "courses": ["CS2110", "CS2112"]},
        ],
        "note": None,
    }
    add_requirement(req1)

    # math requirement for A&S students
    req2 = {
        "id": "CS_req2",
        "type": "C",
        "major": "CS",
        "name": "Calculus",
        "tag": "CS Calculus",
        "tagDescr": "This is a calculus course of Computer Science major",
        "descr": [
            "Take a calculus sequence of 3 courses.",
            "A&S students can take either MATH 1110-1120-2210 sequence or MATH 1910-1920-2940 sequence.",
        ],
        "number": 3,
        "courseGrps": [
            {"id": 1, "courses": ["MATH1110", "MATH1910"]},
            {"id": 2, "courses": ["MATH1120", "MATH1920"]},
            {"id": 3, "courses": ["MATH2210", "MATH2940"]},
        ],
        "note": None,
    }
    add_requirement(req2)

    # math requirement for Engineering students
    req3 = {
        "id": "CS_req3",
        "type": "C",
        "major": "CS",
        "name": "Calculus",
        "tag": "CS Calculus",
        "tagDescr": "This is a calculus course of Computer Science major",
        "descr": [
            "Take a calculus sequence of 3 courses.",
            "Engineering students can only take MATH 1910-1920-2940 sequence.",
        ],
        "number": 3,
        "courseGrps": [
            {"id": 1, "courses": ["MATH1910"]},
            {"id": 2, "courses": ["MATH1920"]},
            {"id": 3, "courses": ["MATH2940"]},
        ],
        "note": None,
    }
    add_requirement(req3)

    # core requirement for 2028 and after-2028 students
    req4 = {
        "id": "CS_req4",
        "type": "C",
        "major": "CS",
        "name": "Core Courses",
        "tag": "CS Core",
        "tagDescr": "This is a core course of Computer Science major",
        "descr": [
            "All FA24 and later matriculants must take one course from each of the following course group listed below.",
        ],
        "number": 6,
        "courseGrps": [
            {"id": 1, "courses": ["CS2800", "CS2802"]},
            {"id": 2, "courses": ["CS3110"]},
            {"id": 3, "courses": ["CS3410", "CS3420"]},
            {"id": 4, "courses": ["CS3700", "CS3780"]},
            {"id": 5, "courses": ["CS4410", "CS4414"]},
            {"id": 6, "courses": ["CS4820"]},
        ],
        "note": None,
    }
    add_requirement(req4)

    # core requirement for 2027 and pre-2027 students
    req5 = {
        "id": "CS_req5",
        "type": "C",
        "major": "CS",
        "name": "Core Courses",
        "tag": "CS Core",
        "tagDescr": "This is a core course of Computer Science major",
        "descr": [
            "All Pre FA24 matriculants must take one course from each of the following course group listed below.",
        ],
        "number": 5,
        "courseGrps": [
            {"id": 1, "courses": ["CS2800", "CS2802"]},
            {"id": 2, "courses": ["CS3110"]},
            {"id": 3, "courses": ["CS3410", "CS3420"]},
            {"id": 4, "courses": ["CS4410", "CS4414"]},
            {"id": 5, "courses": ["CS4820"]},
        ],
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
        "id": "CS_req6",
        "type": "E",
        "major": "CS",
        "name": "Electives",
        "tag": "CS Electives",
        "tagDescr": "This can be counted as an elective course for Computer Science major",
        "descr": [
            "All FA24 and later matriculants must take two CS 4000+ courses (3+ credits each).",
            "CS 4090, CS 4998, and CS 4999 are NOT allowed. CS 3700 or CS 3780 allowed if not used in CS core.",
        ],
        "number": 2,
        "courses": req6_courses,
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
        "id": "CS_req7",
        "type": "E",
        "major": "CS",
        "name": "Electives",
        "tag": "CS Electives",
        "tagDescr": "This can be counted as an elective course for Computer Science major",
        "descr": [
            "All pre-fall 2024 matriculants must take three CS 4000+ courses (3+ credits each).",
            "CS 4090, CS 4998, and CS 4999 are NOT allowed. CS 3700 or CS 3780 allowed if not used in CS core.",
        ],
        "number": 3,
        "courses": req7_courses,
        "note": None,
    }
    add_requirement(req7)

    # probability course for 2027 and pre-2027 students
    req8 = {
        "id": "CS_req8",
        "type": "E",
        "major": "CS",
        "name": "Probability",
        "tag": "CS Probability",
        "tagDescr": "This can be counted as a probability course for Computer Science major",
        "descr": [
            "All pre-fall 2024 matriculants must take one CS-approved Probability course.",
            "This probability course can be used to satisfy another major requirement.",
        ],
        "number": 1,
        "courses": ["BTRY3080", "STSCI3080", "CS4850", "ECE3100", "ECON3130", 
                    "ENGRD2700", "MATH4710"],
        "note": None,
    }
    add_requirement(req8)

    req9_courses = get_CS_practicum(included=["CS3152", "CS4152", "CS4154", "CS4740", "CS4752", 
                                              "CS5150", "CS5152", "CS5412", "CS5414", "CS5431", 
                                              "CS5625", "CS5643"])
    req9 = {
        "id": "CS_req9",
        "type": "E",
        "major": "CS",
        "name": "Practicum or Project",
        "tag": "CS Practicum",
        "tagDescr": "This can be counted as a Practicum or Project course for Computer Science major",
        "descr": [
            "Accepted courses are CS practicums (CS 4xx1), or CS 3152, CS 4152, CS 4154, CS 4740, CS 4752, CS 5150, CS 5152, CS 5412, CS 5414, CS 5431, CS 5625, or CS 5643.",
        ],
        "number": 1,
        "courses": req9_courses,
        "note": None,
    }
    add_requirement(req9)


if __name__ == "__main__":
    commit_CS() 