from service import *
from common import *


def commit_PHYS():
    major = {
        "_id": "PHYS",
        "name": "Physics",
        "needsYear": False,
        "needsCollege": False,
        "colleges": [{"collegeId": "CAS", "name": "College of Arts and Sciences"}],
        "numberOfRequiredCourses": None,
        "rawBasicSections": [
            {
                "requirementIds": ["phys1", "phys2", "phys3", "phys4"],
            }
        ],
        "rawConcentrations": [
            {
                "concentrationName": "Physics (Inside) Concentration",
                "requirementIds": ["phys5", "phys6","phys7"],
            },
            {
                "concentrationName": "Outside Concentration",
                "requirementIds": ["phys8"],
            },
        ],
        "rawEndSections":[
            {
                "requirementIds": ["phys9"]
            }
        ],
        "onboardingCourses": ["PHYS1112","PHYS1116","PHYS2213","PHYS2217","PHYS2214","PHYS2218",
                 "MATH1910","MATH1920","MATH2930","MATH2940"
        ],
    }
    add_major(major)

    req1 = {
        "_id": "phys1",
        "type": "group",
        "majorId": "PHYS",
        "name": "Intro Physics",
        "descr": [
            "All physics majors must complete three-semester introductory physics sequence plus special relativity.",
            "PHYS 1116, 2217, and 2218 are augmented courses, recommended to students planning professional or graduate work in physics."
        ],
        "numberOfRequiredCourses": 3,
        "courseGrps": [
            {"_id": 1, "topic": "Physics I", "courseIds": ["PHYS1116", "PHYS1112", "PHYS2207"]},
            {"_id": 2, "topic": "Physics II", "courseIds": ["PHYS2217", "PHYS2213", "PHYS2208"]},
            {"_id": 3, "topic": "Physics III", "courseIds": ["PHYS2218", "PHYS2214"]},
        ],
        "overlap": ["phys2", "phys3", "phys4", "phys5", "phys6", "phys7", "phys8", "phys9"],
        "note": "Students who take PHYS 1112 must either complete PHYS 2216 (1 cr) or take PHYS 1116 to learn Special Relativity.",
    }
    add_requirement(req1)

    req2 = {
        "_id": "phys2",
        "type": "group",
        "majorId": "PHYS",
        "name": "Math",
        "descr": [
            "Mathematics courses covering single and multivariable calculus, linear algebra, series representations, and complex analysis.",
        ],
        "numberOfRequiredCourses": 4,
        "courseGrps": [
            {"_id": 1, "topic": "Calculus", "courseIds": ["MATH1910","MATH1120"]},
            {"_id": 2, "topic": "Multivariable Calculus", "courseIds": ["MATH1920","MATH2220","MATH2130","MATH2240"]},
            {"_id": 3, "topic": "Differential Equations", "courseIds": ["MATH2930","MATH3270"]},
            {"_id": 4, "topic": "Linear Algebra", "courseIds": ["MATH2940","MATH2210","MATH2310","MATH2230"]},
        ],
        "overlap": ["phys1", "phys3", "phys4", "phys5", "phys6", "phys7", "phys8", "phys9"],
        "note": None,
    }
    add_requirement(req2)

    req3 = {
        "_id": "phys3",
        "type": "group",
        "majorId": "PHYS",
        "name": "Quantum Mechanics",
        "descr": [
            "All physics majors must complete the two-course sequence in modern physics"
        ],
        "numberOfRequiredCourses": 2,
        "courseGrps": [
            {"_id": 1, "topic": "Basics", "courseIds": ["PHYS3316"]},
            {"_id": 2, "topic": "Applications", "courseIds": ["PHYS3317"]},
        ],
        "overlap": ["phys1", "phys2", "phys4", "phys5", "phys6", "phys7", "phys8", "phys9"],
        "note": None,
    }
    add_requirement(req3)

    req4 = {
        "_id": "phys4",
        "type": "group",
        "majorId": "PHYS",
        "name": "Intermediate Physics",
        "descr": [
            "All physics majors must complete an intermediate classical mechanics course and an electromagnetism course.",
        ],
        "numberOfRequiredCourses": 2,
        "courseGrps": [{"_id": 1, "topic": "Mechanics", "courseIds": ["PHYS3318"]},
                       {"_id": 2, "topic": "Electromagnetism", "courseIds": ["PHYS3327"]}],
        "overlap": ["phys1", "phys2", "phys3", "phys5", "phys6", "phys7", "phys8", "phys9"],
        "note": None,
    }
    add_requirement(req4)

    req5 = {
        "_id": "phys5",
        "type": "group",
        "majorId": "PHYS",
        "name": "Inside Concentration Core",
        "descr": [
            "Inside Concentrators must complete PHYS 4410 and PHYS 4230.",
        ],
        "numberOfRequiredCourses": 2,
        "courseGrps": [{"_id": 1, "courseIds": ["PHYS4410"]},
                       {"_id": 2, "courseIds": ["PHYS4230"]}],
        "overlap": ["phys1", "phys2", "phys3", "phys4", "phys6", "phys7", "phys8", "phys9"],
        "note": None,
    }
    add_requirement(req5)

    req6_courses = get_courses_by_subject_min_level(
        "PHYS",
        min_level=3,
        min_credit=3,
        excluded=["PHYS3316","PHYS3317","PHYS4410","PHYS4230","PHYS4484","PHYS4487"],
        included=["ASTRO3302", "ASTRO4431", "AEP4340"],
    )
    req6 = {
        "_id": "phys6",
        "type": "list",
        "majorId": "PHYS",
        "name": "Inside Concentration Electives",
        "descr": [
            "Complete 7 additional credits of 3000+ level physics classes.",
            "PHYS 4443 is recommended, ASTRO 3302, ASTRO 4431, and AEP 4340 may also be counted.",
            "At most 4 credits of independent study (PHYS 4490) may be used towards this requirement.",
            "PHYS 4484-4487 may not be used toward this requirement."
        ],
        "numberOfRequiredCourses": 2,
        "courseIds": req6_courses,
        "overlap": ["phys1", "phys2", "phys3", "phys4", "phys5", "phys7", "phys8", "phys9"],
        "note": None, 
    }
    add_requirement(req6)

    req7_courses = get_courses_by_subject_min_level(
        "MATH",
        min_level=3,
        min_credit=3,
        excluded=[],
        included=["AEP3200","AEP4200"],
    )
    req7 = {
        "_id": "phys7",
        "type": "list",
        "majorId": "PHYS",
        "name": "Inside Concentration Math",
        "descr": [
            "Complete 2 additional 3000+ level math courses.",
            "AEP 3200 and AEP 4200 are included and recommended."
        ],
        "numberOfRequiredCourses": 2,
        "courseIds": req7_courses,
        "overlap": ["phys1", "phys2", "phys3", "phys4", "phys5", "phys6", "phys8", "phys9"],
        "note": None,
    }
    add_requirement(req7)

    req8 = {
        "_id": "phys8",
        "type": "list",
        "majorId": "PHYS",
        "name": "Outside Concentration",
        "descr": [
            "Complete 15 credits in an internally coherent concentration outside of physics.",
            "At least 8 of the 15 credits must be for 3000+ level classes",
            "The outside concentration is designed in coordination with your major advisor, and classes must be agreed upon by your advisor.",
            "At most 4 credits of S/U classes or independent study may be used.",
            "Classes from the physics department should not be used towards the outside concentration.",
            "Classes used for your outside concentration cannot also be counted towards another major or minor.",
            "An outside concentration cannot be in a subfield of physics (e.g. atomic physics).",
            "Classes used for the outside concentration can span different departments or Colleges."
        ],
        "numberOfRequiredCourses": 5,
        "courseIds": [],
        "overlap": ["phys1", "phys2", "phys3", "phys4", "phys5", "phys6", "phys7", "phys9"],
        "note": None,
    }
    add_requirement(req8)

    req9 = {
        "_id": "phys9",
        "type": "list",
        "majorId": "PHYS",
        "name": "Lab",
        "descr": [
            "All physics majors must complete one laboratory course selected from the following courses.",
        ],
        "numberOfRequiredCourses": 1,
        "courseIds": ["PHYS3310","PHYS3330", "PHYS3360", "PHYS4410", "AEP3640", "ASTRO4410", "BEE4500"],
        "overlap": ["phys1", "phys2", "phys3", "phys4", "phys5", "phys6", "phys7", "phys8"],
        "note": None,
    }
    add_requirement(req9)


if __name__ == "__main__":
    commit_PHYS() 