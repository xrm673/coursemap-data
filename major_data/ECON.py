from service import *
from common import *


def commit_ECON():
    major = {
        "id": "ECON",
        "name": "Economics",
        "colleges": [
            {"id": "CAS", "name": "Arts and Sciences"},
        ],
        "requiredCourses": 15,
        "basicRequirements": [
            {
                "requirements": [
                    "ECON_req1",
                    "ECON_req2",
                    "ECON_req3",
                ]
            }
        ],
        "init": [
            "ECON1110",
            "ECON1120",
            "MATH1110",
            "ECON3030",
            "ECON3040",
            "ECON3110",
            "ECON3130",
            "ECON3120",
            "ECON3140",
        ]
    }
    add_major(major)

    req1 = {
        "id": "ECON_req1",
        "type": "C",
        "major": "ECON",
        "name": "Basic Courses",
        "tag": "ECON Basic",
        "tagDescr": "This is a basic course of Economics major",
        "descr": [
            "Take ECON 1100, ECON 1120, and MATH 1110 before declare the major.",
        ],
        "number": 3,
        "courseGrps": [
            {"id": 1, "courses": ["ECON1110"]},
            {"id": 2, "courses": ["ECON1120"]},
            {"id": 3, "courses": ["MATH1110"]},
        ],
        "note": None,
    }
    add_requirement(req1)
    
    req2 = {
        "id": "ECON_req2",
        "type": "C",
        "major": "ECON",
        "name": "Core Courses",
        "tag": "ECON Core",
        "tagDescr": "This is a core course of Economics major",
        "descr": [
            "All economics students must take four core economics courses.",
        ],
        "number": 4,
        "courseGrps": [
            {"id": 1, "courses": ["ECON3030"]},
            {"id": 2, "courses": ["ECON3040"]},
            {"id": 3, "courses": ["ECON3110", "ECON3130"]},
            {"id": 4, "courses": ["ECON3120", "ECON3140"]},
        ],
        "note": None,
    }
    add_requirement(req2)

    req3_courses = get_courses_by_subject_min_level(
        "ECON",
        min_level=4,
        min_credit=3,
        excluded=["ECON4999"],
    )
    req3 = {
        "id": "ECON_req3",
        "type": "E",
        "major": "ECON",
        "name": "Electives",
        "tag": "ECON Electives",
        "tagDescr": "This can be counted as an elective course for Economics major",
        "descr": [
            "All economicsstudents must take at least three courses at the 4000-level.",
            "The Economics Department recommends taking at least one seminar courses(ECON 4900-4989).",
            "ECON 4999 is not counted for this requirement.",
        ],
        "number": 3,
        "courses": req3_courses,
        "note": None,
    }
    add_requirement(req3)


if __name__ == "__main__":
    commit_ECON() 