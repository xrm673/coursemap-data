from service import *
from common import *

def commit_ARTH():
    major = {
        "_id": "ARTH",
        "name": "History of Art",
        "type": "major",
        "needsYear": False,
        "needsMajor": False,
        "needsCollege": False,
        "colleges": [{"collegeId": "CAS", "name": "College of Arts and Sciences"}],
        "numberOfRequiredCourses": 10,
        "rawBasicSections": [
            {
                "requirementIds": [
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
        "type": "group",
        "majorId": "ARTH",
        "name": "Core",
        "descr": [
            "The History of Art major requires the completion of all three courses listed below.",
            "Students must receive a grade of B or higher in ARTH 1100.",
            "If students have not taken ARTH 1100 by the spring of sophomore year, they must complete a 4000-level tutorial course and receive a grade of B or higher in order to qualify for the major.",
            "A grade of B- or higher is required of all other courses to receive credit toward the major.",
        ],
        "numberOfRequiredCourses": 3,
        "courseGrps": [
            {"_id": 1, "topic": "Art History", "courseIds": ["ARTH1100"]},
            {"_id": 2, "topic": "Visual Studies", "courseIds": ["ARTH2000"]},
            {"_id": 3, "topic": "Methods Seminar", "courseIds": ["ARTH4101"]},
        ],
        "overlap": ["arth2", "arth3", "arth4", "arth5"],
    }
    add_requirement(req1)

    req2_courses = get_courses_by_subject_level("ARTH", 2, excluded=["ARTH2000"])
    req2 = {
        "_id": "arth2",
        "type": "list",
        "majorId": "ARTH",
        "name": "2000-level",
        "descr": ["Take at least one ARTH course at the 2000-level."],
        "numberOfRequiredCourses": 1,
        "courseIds": req2_courses,
        "overlap": ["arth1", "arth3", "arth4", "arth5"],
    }
    add_requirement(req2)

    req3_courses = get_courses_by_subject_level("ARTH", 3)
    req3 = {
        "_id": "arth3",
        "type": "list",
        "majorId": "ARTH",
        "name": "3000-level",
        "descr": ["Take at least one ARTH course at the 3000-level."],
        "numberOfRequiredCourses": 1,
        "courseIds": req3_courses,
        "overlap": ["arth1", "arth2", "arth4", "arth5"],
    }
    add_requirement(req3)

    req4_courses = get_courses_by_subject_level("ARTH", 4, excluded=["ARTH4101"])
    req4 = {
        "_id": "arth4",
        "type": "list",
        "majorId": "ARTH",
        "name": "4000-level",
        "descr": ["Take at least two ARTH course at the 4000-level."],
        "numberOfRequiredCourses": 2,
        "courseIds": req4_courses,
        "overlap": ["arth1", "arth2", "arth3", "arth5"],
    }
    add_requirement(req4)

    req5_courses = get_courses_by_subject_min_level(
        "ARTH", 3, excluded=["ARTH2000", "ARTH4101"]
    )
    req5 = {
        "_id": "arth5",
        "type": "list",
        "majorId": "ARTH",
        "name": "Electives",
        "descr": ["Take three additional ARTH electives at the 3000-level or higher."],
        "numberOfRequiredCourses": 3,
        "courseIds": req5_courses,
        "overlap": ["arth1", "arth2", "arth3", "arth4"],
    }
    add_requirement(req5)


if __name__ == "__main__":
    commit_ARTH()
