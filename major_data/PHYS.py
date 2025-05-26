from service import *
from common import *


def commit_PHYS():
    major = {
        "id": "PHYS",
        "name": "Physics",
        "needsYear": False,
        "needsCollege": False,
        "colleges": [{"id": "CAS", "name": "Arts and Sciences"}],
        "requiredCourses": None,
        "basicRequirements": [
            {
                "requirements": ["PHYS_req1", "PHYS_req2", "PHYS_req3", "PHYS_req4"
                ],
            }
        ],
        "concentrations": [
            {
                "concentration": "Physics (Inside) Concentration",
                "requirements": ["PHYS_req5", "PHYS_req6","PHYS_req7"],
            },
            {
                "concentration": "Outside Concentration",
                "requirements": ["PHYS_req8"],
            },
        ],
        "endRequirements":[
            {
                "requirements": ["PHYS_req9"]
            }
        ],
        "init": ["PHYS1112","PHYS1116","PHYS2213","PHYS2217","PHYS2214","PHYS2218",
                 "MATH1910","MATH1920","MATH2930","MATH2940"
        ],
    }
    add_major(major)

    req1 = {
        "id": "PHYS_req1",
        "type": "C",
        "major": "PHYS",
        "name": "Introductory Physics",
        "tag": "PHYS Intro",
        "tagDescr": "This is a Introductory Physics course of Physics major",
        "descr": [
            "All physics majors must complete three-semester introductory physics sequence plus special relativity.",
            "PHYS 1116, 2217, and 2218 are augmented courses, recommended to students planning professional or graduate work in physics."
        ],
        "number": 3,
        "courseGrps": [
            {"id": 1, "courses": ["PHYS1116", "PHYS1112", "PHYS2207"]},
            {"id": 2, "courses": ["PHYS2217", "PHYS2213", "PHYS2208"]},
            {"id": 3, "courses": ["PHYS2218", "PHYS2214"]},
        ],
        "note": "Students who take PHYS 1112 must either complete PHYS 2216 (1 cr) or take PHYS 1116 to learn Special Relativity.",
    }
    add_requirement(req1)

    req2 = {
        "id": "PHYS_req2",
        "type": "C",
        "major": "PHYS",
        "name": "Mathematics",
        "tag": "PHYS Math",
        "tagDescr": "This can be counted as a Mathematics course for Physics major",
        "descr": [
            "Mathematics courses covering single and multivariable calculus, linear algebra, series representations, and complex analysis.",
        ],
        "number": 4,
        "courseGrps": [
            {"id": 1, "courses": ["MATH1910","MATH1120"]},
            {"id": 2, "courses": ["MATH1920","MATH2220","MATH2130","MATH2240"]},
            {"id": 3, "courses": ["MATH2930","MATH3270"]},
            {"id": 4, "courses": ["MATH2940","MATH2210","MATH2310","MATH2230"]},
        ],
        "note": None,
    }
    add_requirement(req2)

    req3 = {
        "id": "PHYS_req3",
        "type": "C",
        "major": "PHYS",
        "name": "Quantum Mechanics",
        "tag": "PHYS Quantum",
        "tagDescr": "This is a Quantum Mechanics course of Physics major",
        "descr": [
            "All physics majors must complete the two-course sequence in modern physics"
        ],
        "number": 2,
        "courseGrps": [
            {"id": 1, "courses": ["PHYS3316"]},
            {"id": 2, "courses": ["PHYS3317"]},
        ],
        "note": None,
    }
    add_requirement(req3)

    req4 = {
        "id": "PHYS_req4",
        "type": "C",
        "major": "PHYS",
        "name": "Intermediate Mechanics and Electromagnetism",
        "tag": "PHYS Intermediate",
        "tagDescr": "This is an Intermediate Mechanics or Electromagnetism course for Physics major",
        "descr": [
            "All physics majors must complete an intermediate classical mechanics course and an electromagnetism course.",
        ],
        "number": 2,
        "courseGrps": [{"id": 1, "courses": ["PHYS3318"]},
                       {"id": 2, "courses": ["PHYS3327"]}],
        "note": None,
    }
    add_requirement(req4)

    req5 = {
        "id": "PHYS_req5",
        "type": "C",
        "major": "PHYS",
        "name": "Inside Concentration Core",
        "tag": "PHYS Isd-Core",
        "tagDescr": "This can be counted as a core course for the Inside Concentration of Physics major.",
        "descr": [
            "Inside Concentrators must complete PHYS 4410 and PHYS 4230.",
        ],
        "number": 2,
        "courseGrps": [{"id": 1, "courses": ["PHYS4410"]},
                       {"id": 2, "courses": ["PHYS4230"]}],
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
        "id": "PHYS_req6",
        "type": "E",
        "major": "PHYS",
        "name": "Inside Concentration Electives",
        "tag": "PHYS Isd-Elctv",
        "tagDescr": "This can be counted as an elective course for the Inside Concentration of Physics major",
        "descr": [
            "Complete 7 additional credits of 3000+ level physics classes.",
            "PHYS 4443 is recommended, ASTRO 3302, ASTRO 4431, and AEP 4340 may also be counted.",
            "At most 4 credits of independent study (PHYS 4490) may be used towards this requirement.",
            "PHYS 4484-4487 may not be used toward this requirement."
        ],
        "number": 2,
        "courses": req6_courses,
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
        "id": "PHYS_req7",
        "type": "E",
        "major": "PHYS",
        "name": "Inside Concentration Math",
        "tag": "PHYS Isd-Math",
        "tagDescr": "This can be counted as a math course for the Inside Concentration of Physics major",
        "descr": [
            "Complete 2 additional 3000+ level math courses.",
            "AEP 3200 and AEP 4200 are included and recommended."
        ],
        "number": 2,
        "courses": req7_courses,
        "note": None,
    }
    add_requirement(req7)

    req8 = {
        "id": "PHYS_req8",
        "type": "E",
        "major": "PHYS",
        "name": "Outside Concentration Courses",
        "tag": "PHYS Outside",
        "tagDescr": "This can be counted as a course for the Outside Concentration of Physics major",
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
        "number": 5,
        "courses": [],
        "note": None,
    }
    add_requirement(req8)

    req9 = {
        "id": "PHYS_req9",
        "type": "E",
        "major": "PHYS",
        "name": "Laboratory Works",
        "tag": "PHYS Lab",
        "tagDescr": "This can be counted as a Laboratory course for Physics major",
        "descr": [
            "All physics majors must complete one laboratory course selected from the following courses.",
        ],
        "number": 1,
        "courses": ["PHYS3310","PHYS3330", "PHYS3360", "PHYS4410", "AEP3640", "ASTRO4410", "BEE4500"],
        "note": None,
    }
    add_requirement(req9)


if __name__ == "__main__":
    commit_PHYS() 