from service import *
from common import *

def commit_ARTH():
    major = {
        "id": "ARTH",
        "name": "History of Art",
        "colleges": [{"id": "CAS", "name": "Arts and Sciences"}],
        "requiredCourses": 10,
        "basicRequirements": [
            {
                "requirements": [
                    "ARTH_req1",
                    "ARTH_req2",
                    "ARTH_req3",
                    "ARTH_req4",
                    "ARTH_req5",
                ],
            }
        ],
        "init": [
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
        "id": "ARTH_req1",
        "type": "C",
        "major": "ARTH",
        "name": "Core Courses",
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
            {"id": 1, "courses": ["ARTH1100"]},
            {"id": 2, "courses": ["ARTH2000"]},
            {"id": 3, "courses": ["ARTH4101"]},
        ],
    }
    add_requirement(req1)

    req2_courses = get_courses_by_subject_level("ARTH", 2, excluded=["ARTH2000"])
    req2 = {
        "id": "ARTH_req2",
        "type": "E",
        "major": "ARTH",
        "name": "2000 Level",
        "tag": "2000 ARTH",
        "tagDescr": "This is a 2000 level Art History course.",
        "descr": ["Take at least one ARTH course at the 2000-level."],
        "number": 1,
        "courses": req2_courses,
    }
    add_requirement(req2)

    req3_courses = get_courses_by_subject_level("ARTH", 3)
    req3 = {
        "id": "ARTH_req3",
        "type": "E",
        "major": "ARTH",
        "name": "3000 Level",
        "tag": "3000 ARTH",
        "tagDescr": "This is a 3000 level Art History course.",
        "descr": ["Take at least one ARTH course at the 3000-level."],
        "number": 1,
        "courses": req3_courses,
    }
    add_requirement(req3)

    req4_courses = get_courses_by_subject_level("ARTH", 4, excluded=["ARTH4101"])
    req4 = {
        "id": "ARTH_req4",
        "type": "E",
        "major": "ARTH",
        "name": "4000 Level",
        "tag": "4000 ARTH",
        "tagDescr": "This is a 4000 level Art History course.",
        "descr": ["Take at least one ARTH course at the 4000-level."],
        "number": 2,
        "courses": req4_courses,
    }
    add_requirement(req4)

    req5_courses = get_courses_by_subject_min_level(
        "ARTH", 3, excluded=["ARTH2000", "ARTH4101"]
    )
    req5 = {
        "id": "ARTH_req5",
        "type": "E",
        "major": "ARTH",
        "name": "Electives",
        "tag": "ARTH Electives",
        "tagDescr": "This can be counted as an elective for Art History major.",
        "descr": ["Take three additional ARTH electives at the 3000-level or higher."],
        "number": 3,
        "courses": req5_courses,
    }
    add_requirement(req5)


if __name__ == "__main__":
    commit_ARTH()
