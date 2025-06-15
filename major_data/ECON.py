from service import *
from common import *


def commit_ECON():
    major = {
        "_id": "ECON",
        "name": "Economics",
        "type": "major",
        "yearDependent": False,
        "majorDependent": False,
        "collegeDependent": False,
        "colleges": [
            {"collegeId": "CAS", "name": "College of Arts and Sciences"},
        ],
        "numberOfRequiredCourses": 10,
        "rawBasicSections": [
            {
                "requirementIds": ["econ1", "econ2", "econ3"],
            }
        ],
        "onboardingCourses": [
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
        "_id": "econ1",
        "type": "group",
        "majorId": "ECON",
        "name": "Basic",
        "descr": [
            "Take ECON 1100, ECON 1120, and MATH 1110 before declare the major.",
        ],
        "numberOfRequiredCourses": 3,
        "courseGrps": [
            {"_id": 1, "topic": "Micro", "courseIds": ["ECON1110"]},
            {"_id": 2, "topic": "Macro", "courseIds": ["ECON1120"]},
            {"_id": 3, "topic": "Math", "courseIds": ["MATH1110"]},
        ],
        "overlap": ["econ2", "econ3"],
        "note": None,
    }
    add_requirement(req1)
    
    req2 = {
        "_id": "econ2",
        "type": "group",
        "majorId": "ECON",
        "name": "Core",
        "descr": [
            "All economics students must take four core economics courses.",
        ],
        "numberOfRequiredCourses": 4,
        "courseGrps": [
            {"_id": 1, "topic": "Intermed Micro", "courseIds": ["ECON3030"]},
            {"_id": 2, "topic": "Intermed Macro", "courseIds": ["ECON3040"]},
            {"_id": 3, "topic": "Statistics", "courseIds": ["ECON3110", "ECON3130"]},
            {"_id": 4, "topic": "Econometrics", "courseIds": ["ECON3120", "ECON3140"]},
        ],
        "overlap": ["econ1", "econ3"],
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
        "_id": "econ3",
        "type": "list",
        "majorId": "ECON",
        "name": "Elective",
        "descr": [
            "All economicsstudents must take at least three courses at the 4000-level.",
            "The Economics Department recommends taking at least one seminar courses(ECON 4900-4989).",
            "ECON 4999 is not counted for this requirement.",
        ],
        "numberOfRequiredCourses": 3,
        "courseIds": req3_courses,
        "overlap": ["econ1", "econ2"],
        "note": None,
    }
    add_requirement(req3)


if __name__ == "__main__":
    commit_ECON() 