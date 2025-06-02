from service import *
from common import *

def commit_ARTH():
    major = {
        "_id": "ARTH",
        "name": "History of Art",
        "needsYear": False,
        "needsCollege": False,
        "colleges": [{"collegeId": "CAS", "name": "College of Arts and Sciences"}],
        "numberOfRequiredCourses": 10,
        "rawBasicRequirements": [
            {
                "requirements": [
                    "arth1",
                    "arth2",
                    "arth3",
                    "arth4",
                    "arth5",
                ],
            }
        ],
        "onboardingCourses": [
            "ARTH1100",
            "ARTH2000",
            "ARTH1178",
            "ARTH1154",
            "ARTH2750",
            "ARTH4101",
        ],
    }
    add_major(major)

    req1 = {
        "_id": "arth1",
        "type": "C",
        "major": "ARTH",
        "name": "Core",
        "tag": "ARTH Core",
        "tagDescr": "This is a core course of Art History major",
        "descr": [
            "The History of Art major requires the completion of all three courses listed below.",
            "Students must receive a grade of B or higher in ARTH 1100.",
            "If students have not taken ARTH 1100 by the spring of sophomore year, they must complete a 4000-level tutorial course and receive a grade of B or higher in order to qualify for the major.",
            "A grade of B- or higher is required of all other courses to receive credit toward the major.",
        ],
        "number": 3,
        "courseGrps": [
            {"courseIds": ["ARTH1100"]},
            {"courseIds": ["ARTH2000"]},
            {"courseIds": ["ARTH4101"]},
        ],
    }
    add_requirement(req1)

    req2_courses = get_courses_by_subject_level("ARTH", 2, excluded=["ARTH2000"])
    req2 = {
        "_id": "arth2",
        "type": "E",
        "major": "ARTH",
        "name": "2000-level",
        "tag": "2000 ARTH",
        "tagDescr": "This is a 2000 level Art History course.",
        "descr": ["Take at least one ARTH course at the 2000-level."],
        "number": 1,
        "courseIds": req2_courses,
    }
    add_requirement(req2)

    req3_courses = get_courses_by_subject_level("ARTH", 3)
    req3 = {
        "_id": "arth3",
        "type": "E",
        "major": "ARTH",
        "name": "3000-level",
        "tag": "3000 ARTH",
        "tagDescr": "This is a 3000 level Art History course.",
        "descr": ["Take at least one ARTH course at the 3000-level."],
        "number": 1,
        "courseIds": req3_courses,
    }
    add_requirement(req3)

    req4_courses = get_courses_by_subject_level("ARTH", 4, excluded=["ARTH4101"])
    req4 = {
        "_id": "arth4",
        "type": "E",
        "major": "ARTH",
        "name": "4000-level",
        "tag": "4000 ARTH",
        "tagDescr": "This is a 4000 level Art History course.",
        "descr": ["Take at least one ARTH course at the 4000-level."],
        "number": 2,
        "courseIds": req4_courses,
    }
    add_requirement(req4)

    req5_courses = get_courses_by_subject_min_level(
        "ARTH", 3, excluded=["ARTH2000", "ARTH4101"]
    )
    req5 = {
        "_id": "arth5",
        "type": "E",
        "major": "ARTH",
        "name": "Electives",
        "tag": "ARTH Electives",
        "tagDescr": "This can be counted as an elective for Art History major.",
        "descr": ["Take three additional ARTH electives at the 3000-level or higher."],
        "number": 3,
        "courseIds": req5_courses,
    }
    add_requirement(req5)


if __name__ == "__main__":
    commit_ARTH()
