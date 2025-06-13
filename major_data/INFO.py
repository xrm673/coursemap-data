from service import *
from common import *


def commit_INFO():
    major = {
        "_id": "INFO",
        "name": "Information Science",
        "needsYear": False,
        "needsCollege": False,
        "colleges": [
            {"collegeId": "CAS", "name": "College of Arts and Sciences"},
            {"collegeId": "CALS", "name": "College of Agriculture and Life Sciences"},
        ],
        "numberOfRequiredCourses": 15,
        "rawBasicSections": [
            {
                "requirementIds": ["info1", "info2", "info3", "info4"],
            },
        ],
        "rawConcentrations": [
            {
                "concentrationName": "Behavioral Science",
                "requirementIds": ["info6", "info7", "info8"],
            },
            {
                "concentrationName": "Data Science",
                "requirementIds": ["info9", "info10", "info11", "info12"],
            },
            {
                "concentrationName": "Digital Culture and Production (Design Focused)",
                "requirementIds": ["info13", "info14", "info15"],
            },
            {
                "concentrationName": "Digital Culture and Production (Culture Focused)",
                "requirementIds": ["info16", "info17"],
            },
            {
                "concentrationName": "Information Ethics, Law, and Policy",
                "requirementIds": ["info18", "info19", "info20", "info21"],
            },
            {
                "concentrationName": "Interactive Technology",
                "requirementIds": ["info22", "info23", "info24", "info25"],
            },
            {
                "concentrationName": "Networks, Crowds, and Markets",
                "requirementIds": ["info26", "info27", "info28"],
            },
            {
                "concentrationName": "UX Design",
                "requirementIds": ["info29", "info30", "info31", "info32"],
            },
        ],
        "rawEndSections" : [
            {
                "requirementIds": ["info5"],
            },
        ],
        "onboardingCourses": [
            "INFO1200",
            "INFO1260",
            "INFO1300",
            "CS1110",
            "MATH1110",
            "INFO2040",
            "INFO2450",
            "INFO2950",
        ],
    }
    add_major(major)

    req1 = {
        "_id": "info1",
        "type": "group",
        "majorId": "INFO",
        "name": "Core",
        "descr": [
            "Take at least one course from each of the course groups listed below.",
        ],
        "numberOfRequiredCourses": 5,
        "courseGrps": [
            {"_id": 1, "topic": "Ethics & Law", "courseIds": ["INFO1200", "INFO1260"]},
            {"_id": 2, "topic": "Web Programming", "courseIds": ["INFO1300"]},
            {"_id": 3, "topic": "Networks", "courseIds": ["INFO2040"]},
            {"_id": 4, "topic": "Communication & Tech", "courseIds": ["INFO2450"]},
            {"_id": 5, "topic": "Data Science", "courseIds": ["INFO2950", "INFO2951"]},
        ],
        "overlap": ["info2", "info3", "info4", "info5", "info6", "info7",
                    "info8", "info9", "info10", "info11", "info12", "info13",
                    "info14", "info15", "info16", "info17", "info18", "info19",
                    "info20", "info21", "info22", "info23", "info24", "info25",
                    "info26", "info27", "info28", "info29", "info30", "info31", "info32"],
        "note": "Data Science (DS) concentrators should take INFO 2950 during the fall semester, if possible. Otherwise, DS concentrators should plan to build upon their Python programming skills in preparation for upper-level DS courses.",
    }
    add_requirement(req1)

    req2 = {
        "_id": "info2",
        "type": "list",
        "majorId": "INFO",
        "name": "Programming",
        "descr": [
            "Take CS 1110 or CS 1112 for letter grade to fulfill the programming requirement."
        ],
        "numberOfRequiredCourses": 1,
        "courseIds": ["CS1110", "CS1112"],
        "overlap": ["info1", "info3", "info4", "info5", "info6", "info7",
                    "info8", "info9", "info10", "info11", "info12", "info13",
                    "info14", "info15", "info16", "info17", "info18", "info19",
                    "info20", "info21", "info22", "info23", "info24", "info25",
                    "info26", "info27", "info28", "info29", "info30", "info31", "info32"],
        "note": None,
    }
    add_requirement(req2)

    req3 = {
        "_id": "info3",
        "type": "list",
        "majorId": "INFO",
        "name": "Math",
        "descr": [
            "Take a Calculus I course for letter grade to fulfill the math requirement. ",
            "AP credits can fulfill this requirement.",
        ],
        "numberOfRequiredCourses": 1,
        "courseIds": ["MATH1106", "MATH1110", "MATH1910"],
        "overlap": ["info1", "info2", "info4", "info5", "info6", "info7",
                    "info8", "info9", "info10", "info11", "info12", "info13",
                    "info14", "info15", "info16", "info17", "info18", "info19",
                    "info20", "info21", "info22", "info23", "info24", "info25",
                    "info26", "info27", "info28", "info29", "info30", "info31", "info32"],
        "note": None,
    }
    add_requirement(req3)

    req4 = {
        "_id": "info4",
        "type": "list",
        "majorId": "INFO",
        "name": "Statistics",
        "descr": [
            "Take ONE statistics course provided below. ",
            "AP credits may NOT be used to fulfill this requirement.",
        ],
        "numberOfRequiredCourses": 1,
        "courseIds": [
            "AEM2100",
            "BTRY3010",
            "CEE3040",
            "ECON3110",
            "ECON3130",
            "ENGRD2700",
            "ILRST2100",
            "MATH1710",
            "PSYCH2500",
            "PUBPOL2100",
            "SOC3010",
            "STSCI2100",
            "STSCI2150",
            "STSCI2200",
        ],
        "overlap": ["info1", "info2", "info3", "info5", "info6", "info7",
                    "info8", "info9", "info10", "info11", "info12", "info13",
                    "info14", "info15", "info16", "info17", "info18", "info19",
                    "info20", "info21", "info22", "info23", "info24", "info25",
                    "info26", "info27", "info28", "info29", "info30", "info31", "info32"],
    }
    add_requirement(req4)

    req5_courses = get_courses_by_subject_min_level(
        "INFO",
        3,
        excluded=["INFO4998", "INFO4910", "INFO4997", "INFO5000", "INFO5900", "INFO5905"],
        included=["INFO2300", "INFO2310", "CS2110", "CS2112", "CS3110", "CS3410"],
    )
    req5 = {
        "_id": "info5",
        "type": "list",
        "majorId": "INFO",
        "name": "Electives",
        "descr": [
            "Complete three electives from any INFO 3000+ course (including INFO 4900 but excluding INFO 4998 and INFO 4910).",
            "INFO 2300/2310 (one of them), CS 2110/2112, CS 3110, and CS 3410 may also be counted.",
            "Up to two courses from qualifying study abroad programs may be transfered to Cornell and applied as major "
            "elective credit. Please review the Study Abroad guidelines for details. ",
            "Electives must be taken for a letter grade, each must earn three or more credit hours, and "
            "must be completed with a grade of C- or higher (a grade of C or higher is required for "
            "courses taken abroad).",
            "Students may only fulfill one of their electives with INFO 4900.",
        ],
        "numberOfRequiredCourses": 3,
        "courseIds": req5_courses,
        "overlap": ["info1", "info2", "info3", "info4", "info6", "info7",
                    "info8", "info9", "info10", "info11", "info12", "info13",
                    "info14", "info15", "info16", "info17", "info18", "info19",
                    "info20", "info21", "info22", "info23", "info24", "info25",
                    "info26", "info27", "info28", "info29", "info30", "info31", "info32"],
    }
    add_requirement(req5)

    req6 = {
        "_id": "info6",
        "type": "list",
        "majorId": "INFO",
        "concentrationName": "Behavioral Science",
        "name": "Social Behavior",
        "descr": ["Take TWO courses listed below."],
        "numberOfRequiredCourses": 2,
        "courseIds": [
            "INFO3460",
            "INFO4430",
            "INFO4450",
            "INFO4490",
            "INFO4500",
            "INFO4505",
            "INFO4800",
            "INFO4940",
            "COMM4380",
            "PSYCH3800",
        ],
        "courseNotes": [
            {
                "courseId": "INFO4940",
                "grpIdentifierArray": ["Building Inclusive Computing Organizations",
                                       "Technology and Underserved Communities"]
            }
        ],
        "overlap": ["info1", "info2", "info3", "info4", "info5", "info7", "info8"]
    }
    add_requirement(req6)

    req7 = {
        "_id": "info7",
        "type": "list",
        "majorId": "INFO",
        "concentrationName": "Behavioral Science",
        "name": "Social Data Analytics",
        "descr": [
            "Take ONE course listed below",
        ],
        "numberOfRequiredCourses": 1,
        "courseIds": [
            "INFO3300",
            "INFO3950",
            "INFO4100",
            "INFO4300",
            "INFO4350",
            "INFO4940",
            "COMM4242",
            "CS4740",
            "CS3780",
        ],
        "courseNotes": [{
            "courseId": "INFO4940",
            "grpIdentifierArray": ["How LLMs Work, Their Potential, and Limitations",
                                   "Applied Machine Learning: Methods and Applications"]
        }],
        "overlap": ["info1", "info2", "info3", "info4", "info5", "info6", "info8"]
    }
    add_requirement(req7)

    req8 = {
        "_id": "info8",
        "type": "list",
        "majorId": "INFO",
        "concentrationName": "Behavioral Science",
        "name": "Behavior in Context",
        "descr": [
            "Take ONE course listed below.",
        ],
        "numberOfRequiredCourses": 1,
        "courseIds": [
            "INFO3200",
            "INFO4140",
            "INFO4940",
            "COMM4940",
            "INFO4360",
            "INFO3450",
            "INFO4240",
            "INFO4400",
        ],
        "courseNotes": [
            {
            "courseId": "INFO4940",
            "grpIdentifierArray": ["Law, Policy, and Politics of AI",
                                   "Technology and Social Change Practicum"]
            },
            {
            "courseId": "COMM4940",
            "grpIdentifierArray": ["Human-Algorithm Behavior"]
            },
        ],
        "overlap": ["info1", "info2", "info3", "info4", "info5", "info6", "info7"]
    }
    add_requirement(req8)

    req9 = {
        "_id": "info9",
        "type": "list",
        "majorId": "INFO",
        "concentrationName": "Data Science",
        "name": "Data Analysis",
        "descr": [
            "Take ONE course listed below.",
        ],
        "numberOfRequiredCourses": 1,
        "courseIds": [
            "INFO3300",
            "INFO3900",
            "INFO3950",
            "INFO4940",
            "CS3780",
            "ORIE3120",
            "ORIE4740",
            "ORIE3741",
            "STSCI3740",
        ],
        "courseNotes": [{
            "courseId": "INFO4940",
            "grpIdentifierArray": ["Applied Machine Learning: Methods and Applications"]
        }],
        "overlap": ["info1", "info2", "info3", "info4", "info5", "info10", "info11", "info12"]
    }
    add_requirement(req9)

    req10 = {
        "_id": "info10",
        "type": "list",
        "majorId": "INFO",
        "concentrationName": "Data Science",
        "name": "Domain Expertise",
        "descr": [
            "Take ONE course listed below.",
        ],
        "numberOfRequiredCourses": 1,
        "courseIds": [
            "INFO2770",
            "INFO3130",
            "INFO3350",
            "INFO3370",
            "INFO4100",
            "INFO4120",
            "INFO4300",
            "INFO4350",
            "INFO4940",
            "CS4740",
        ],
        "courseNotes": [{
            "courseId": "INFO4940",
            "grpIdentifierArray": ["How LLMs Work, Their Potential, and Limitations",
                                   "Advanced NLP for Humanities Research"]
        }],
        "overlap": ["info1", "info2", "info3", "info4", "info5", "info9", "info11", "info12"]
    }
    add_requirement(req10)

    req11 = {
        "_id": "info11",
        "type": "list",
        "majorId": "INFO",
        "concentrationName": "Data Science",
        "name": "Big Data Ethics, Policy and Society",
        "descr": [
            "Take ONE course listed below.",
        ],
        "numberOfRequiredCourses": 1,
        "courseIds": [
            "INFO3200",
            "INFO4140",
            "INFO4145",
            "INFO4200",
            "INFO4240",
            "INFO4250",
            "INFO4260",
            "INFO4390",
            "INFO4561",
            "INFO4940",
            "ENGL3778",
            "PUBPOL3460"
        ],
        "courseNotes": [{
            "courseId": "INFO4940",
            "grpIdentifierArray": ["Building Inclusive Computing Organizations",
                                   "Law, Policy and Politics of AI",
                                   "Technology and Social Change Practicum",
                                   "U.S. Copyright Law"]
        }],
        "overlap": ["info1", "info2", "info3", "info4", "info5", "info9", "info10", "info12"]
    }
    add_requirement(req11)

    req12 = {
        "_id": "info12",
        "type": "list",
        "majorId": "INFO",
        "concentrationName": "Data Science",
        "name": "Data Communication",
        "descr": [
            "Take ONE course listed below.",
        ],
        "numberOfRequiredCourses": 1,
        "courseIds": [
            "INFO3312",
            "INFO4310",
            "COMM3150",
            "COMM3189",
            "COMM4860",
            "COMM4940",
            "SOC3580",
        ],
        "courseNotes": [{
            "courseId": "COMM4940",
            "grpIdentifierArray": ["Data and Technology for Organizing"]
        }],
        "overlap": ["info1", "info2", "info3", "info4", "info5", "info9", "info10", "info11"]
    }
    add_requirement(req12)

    req13 = {
        "_id": "info13",
        "type": "list",
        "majorId": "INFO",
        "concentrationName": "Digital Culture and Production (Design Focused)",
        "name": "Digital Culture and History",
        "descr": [
            "Choose either ONE course from this section, or choose THREE courses for a culture-focused curriculum."
        ],
        "numberOfRequiredCourses": 1,
        "courseIds": [
            "INFO2921",
            "INFO3200",
            "INFO4140",
            "INFO4260",
            "INFO4940",
            "STS4040",
        ],
        "courseNotes": [{
            "courseId": "INFO4940",
            "grpIdentifierArray": ["Clockwork: Infrastructure, Work, and Time",
                                   "Law, Policy and Politics of AI",
                                   "U.S. Copyright Law"]
        }],
        "overlap": ["info1", "info2", "info3", "info4", "info5", "info14", "info15"]
    }
    add_requirement(req13)

    req14 = {
        "_id": "info14",
        "type": "list",
        "majorId": "INFO",
        "concentrationName": "Digital Culture and Production (Design Focused)",
        "name": "Digital Production",
        "descr": ["Take ONE course in this section."],
        "numberOfRequiredCourses": 1,
        "courseIds": [
            "​INFO2300",
            "INFO2310",
            "INFO3152",
            "INFO3300",
            "INFO4320",
            "CS3758",
            "CS4620",
        ],
        "overlap": ["info1", "info2", "info3", "info4", "info5", "info13", "info15"]
    }
    add_requirement(req14)

    req15 = {
        "_id": "info15",
        "type": "list",
        "majorId": "INFO",
        "concentrationName": "Digital Culture and Production (Design Focused)",
        "name": "Media, Art, Design",
        "descr": [
            "Choose either TWO courses from this section, or skip this section for a culture-focused curriculum.",
            ],
        "numberOfRequiredCourses": 2,
        "courseIds": [
            "INFO3450",
            "INFO3660",
            "INFO4152",
            "INFO4240",
            "INFO4400",
            "INFO4420",
            "INFO4940",
            "ART3705",
            "ARTH4151",
            "COML3115",
        ],
        "courseNotes": [{
            "courseId": "INFO4940",
            "grpIdentifierArray": ["Design Thinking, Media, and Community",
                                   "Human Centered Design and Engaged Media",
                                   "Producing Culture About, With, and Through Tech",
                                   "Technology and Social Change Practicum"]
        }],
        "overlap": ["info1", "info2", "info3", "info4", "info5", "info13", "info14"]
    }
    add_requirement(req15)
    
    req16 = {
        "_id": "info16",
        "type": "list",
        "majorId": "INFO",
        "concentrationName": "Digital Culture and Production (Culture Focused)",
        "name": "Digital Culture and History",
        "descr": [
            "Choose either THREE courses from this section, or choose ONE course for a design-focused curriculum.",
        ],
        "numberOfRequiredCourses": 3,
        "courseIds": [
            "INFO2921",
            "INFO3200",
            "INFO4140",
            "INFO4260",
            "INFO4940",
            "STS4040",
        ],
        "courseNotes": [{
            "courseId": "INFO4940",
            "grpIdentifierArray": ["Clockwork: Infrastructure, Work, and Time",
                                   "Law, Policy and Politics of AI",
                                   "U.S. Copyright Law"]
        }],
        "overlap": ["info1", "info2", "info3", "info4", "info5", "info17"]
    }
    add_requirement(req16)
    
    req17 = {
        "_id": "info17",
        "type": "list",
        "majorId": "INFO",
        "concentrationName": "Digital Culture and Production (Culture Focused)",
        "name": "Digital Production",
        "descr": ["Take one course in this section."],
        "numberOfRequiredCourses": 1,
        "courseIds": [
            "​INFO2300",
            "INFO2310",
            "INFO3152",
            "INFO3300",
            "INFO4320",
            "CS3758",
            "CS4620",
        ],
        "overlap": ["info1", "info2", "info3", "info4", "info5", "info16"]
    }
    add_requirement(req17)

    req18 = {
        "_id": "info18",
        "type": "list",
        "majorId": "INFO",
        "concentrationName": "Information Ethics, Law, and Policy",
        "name": "Frameworks and Institutions",
        "descr": ["Take one course in this section."],
        "numberOfRequiredCourses": 1,
        "courseIds": [
            "INFO4113",
            "INFO4140",
            "INFO4200",
            "INFO4250",
            "INFO4301",
            "INFO4940",
            "HADM4890",
            "PUBPOL3460",
        ],
        "courseNotes": [{
            "courseId": "INFO4940",
            "grpIdentifierArray": ["Law, Policy and Politics of AI",
                                   "U.S. Copyright Law"]
        }],
        "overlap": ["info1", "info2", "info3", "info4", "info5", "info19", "info20", "info21"]
    }
    add_requirement(req18)

    req19 = {
        "_id": "info19",
        "type": "list",
        "majorId": "INFO",
        "concentrationName": "Information Ethics, Law, and Policy",
        "name": "Methods and Analysis",
        "descr": ["Take one course in this section."],
        "numberOfRequiredCourses": 1,
        "courseIds": [
            "INFO2921",
            "INFO4240",
            "INFO4940",
            "PUBPOL2300",
            "PUBPOL2301"
        ],
        "courseNotes": [{
            "courseId": "INFO4940",
            "grpIdentifierArray": ["Clockwork: Infrastructure, Work, and Time",
                                   "Technology and Social Change Practicum"]
        }],
        "overlap": ["info1", "info2", "info3", "info4", "info5", "info18", "info20", "info21"]
    }
    add_requirement(req19)

    req20 = {
        "_id": "info20",
        "type": "list",
        "majorId": "INFO",
        "concentrationName": "Information Ethics, Law, and Policy",
        "name": "Cases / Topics",
        "descr": ["Take one course in this section."],
        "numberOfRequiredCourses": 1,
        "courseIds": [
            "INFO3200",
            "INFO4145",
            "INFO4260",
            "INFO4390",
            "INFO4561",
            "COMM4940",
            "STS4040",
        ],
        "courseNotes": [{
            "courseId": "COMM4940",
            "grpIdentifierArray": ["Human-Algorithm Behavior"]
        }],
        "overlap": ["info1", "info2", "info3", "info4", "info5", "info18", "info19", "info21"]
    }
    add_requirement(req20)

    req21 = {
        "_id": "info21",
        "type": "list",
        "majorId": "INFO",
        "concentrationName": "Information Ethics, Law, and Policy",
        "name": "Tools and Technical Domains",
        "descr": [
            "Take one course in this section.",
            "Students may petition the Director of Undergraduate Studies to allow any upper-level (3000 or above) technical IS course relevant to their work in ELP to satisfy this category.",
        ],
        "numberOfRequiredCourses": 1,
        "courseIds": [
            "INFO3300",
            "INFO3350",
            "INFO3370",
            "INFO4100",
            "INFO4120",
            "INFO4300",
            "INFO4350",
        ],  
        "overlap": ["info1", "info2", "info3", "info4", "info5", "info18", "info19", "info20"]
    }
    add_requirement(req21)

    req22 = {
        "_id": "info22",
        "type": "list",
        "majorId": "INFO",
        "concentrationName": "Interactive Technology",
        "name": "Object-Oriented Programming",
        "descr": [
            "CS 2110 is a required course for this concentration.",
        ],
        "numberOfRequiredCourses": 1,
        "courseIds": ["CS2110", "CS2112"],
        "overlap": ["info1", "info2", "info3", "info4", "info5", "info23", "info24", "info25"]
    }
    add_requirement(req22)

    req23 = {
        "_id": "info23",
        "type": "list",
        "majorId": "INFO",
        "concentrationName": "Interactive Technology",
        "name": "Building with Hardware",
        "descr": [
            "Take ONE course for this requirement.",
        ],
        "numberOfRequiredCourses": 1,
        "courseIds": ["INFO4120", "INFO4320", "CS4758"],
        "overlap": ["info1", "info2", "info3", "info4", "info5", "info22", "info24", "info25"]
    }
    add_requirement(req23)

    req24 = {
        "_id": "info24",
        "type": "list",
        "majorId": "INFO",
        "concentrationName": "Interactive Technology",
        "name": "Working with Data/Software",
        "descr": [
            "Take ONE course for this requirement.",
        ],
        "numberOfRequiredCourses": 1,
        "courseIds": [
            "INFO3300",
            "INFO4340",
            "INFO4555",
            "CS4620",
            "CS3780",
            "CS5150",
            "ORIE3120",
            "ORIE4740",
            "ORIE3741",
            "STSCI3740",
        ],
        "overlap": ["info1", "info2", "info3", "info4", "info5", "info22", "info23", "info25"]
    }
    add_requirement(req24)

    req25 = {
        "_id": "info25",
        "type": "list",
        "majorId": "INFO",
        "concentrationName": "Interactive Technology",
        "name": "Context/Application Domains",
        "descr": [
            "Take ONE course for this requirement.",
        ],
        "numberOfRequiredCourses": 1,
        "courseIds": [
            "INFO4152",
            "INFO4310",
            "INFO4410",
            "INFO4430",
            "INFO4505",
        ],
        "courseNotes": [{
            "courseId": "INFO4940",
            "grpIdentifierArray": ["Human-AI Interaction Design Research",
                                   "Producing Culture About, With, and Through Tech"]
        }],
        "overlap": ["info1", "info2", "info3", "info4", "info5", "info22", "info23", "info24"]
    }
    add_requirement(req25)
    
    req26 = {
        "_id": "info26",
        "type": "list",
        "majorId": "INFO",
        "concentrationName": "Networks, Crowds, and Markets",
        "name": "Models",
        "descr": [
            "Take TWO courses for this requirement.",
        ],
        "numberOfRequiredCourses": 2,
        "courseIds": [
            "INFO4220",
            "INFO4360",
            "INFO4940",
            "COMM3150",
            "ECON3810",
            "ECON4020",
            "ECON4610",
            "ECON4660",
            "ORIE4350",
            "SOC3080",
        ],
        "courseNotes": [{
            "courseId": "INFO4940",
            "grpIdentifierArray": ["Social Dynamics and Network Analytics"]
        }],
        "overlap": ["info1", "info2", "info3", "info4", "info5", "info27", "info28"]
    }
    add_requirement(req26)
    
    req27 = {
        "_id": "info27",
        "type": "list",
        "majorId": "INFO",
        "concentrationName": "Networks, Crowds, and Markets",
        "name": "Data",
        "descr": [
            "Take ONE course for this requirement.",
        ],
        "numberOfRequiredCourses": 1,
        "courseIds": [
            "INFO3300",
            "INFO4300",
            "INFO4350",
            "INFO3950",
            "INFO4940",
            "CS4740",
            "CS3780",
            "ECON3120",
            "ECON3140",
        ],
        "courseNotes": [{
            "courseId": "INFO4940",
            "grpIdentifierArray": ["Applied Machine Learning: Methods and Applications"]
        }],
        "overlap": ["info1", "info2", "info3", "info4", "info5", "info26", "info28"]
    }
    add_requirement(req27)
    
    req28 = {
        "_id": "info28",
        "type": "list",
        "majorId": "INFO",
        "concentrationName": "Networks, Crowds, and Markets",
        "name": "Policy / Values",
        "descr": [
            "Take ONE course for this requirement.",
        ],
        "numberOfRequiredCourses": 1,
        "courseIds": [
            "INFO4140",
            "INFO4145",
            "INFO4200",
            "INFO4240",
            "INFO4250",
            "INFO4940",
            "COMM4940",
            "PUBPOL3460",
        ],
        "courseNotes": [
            {
            "courseId": "INFO4940",
            "grpIdentifierArray": ["Law, Policy and Politics of AI",
                                   "Technology and Social Change Practicum",
                                   "U.S. Copyright Law"]
            }, 
            {
                "courseId": "COMM4940",
                "grpIdentifierArray": ["Human-Algorithm Behavior"]
            }
        ],
        "overlap": ["info1", "info2", "info3", "info4", "info5", "info26", "info27"]
    }
    add_requirement(req28)

    req29 = {
        "_id": "info29",
        "type": "list",
        "majorId": "INFO",
        "concentrationName": "UX Design",
        "name": "Core Principles of Design",
        "descr": [
            "Take ONE course for this requirement.",
        ],
        "numberOfRequiredCourses": 1,
        "courseIds": [
            "INFO3450",
            "INFO4400",
            "INFO4410",
            "INFO4940",
        ],
        "courseNotes": [{
            "courseId": "INFO4940",
            "grpIdentifierArray": ["Designing AI Products and Services"]
        }],
        "overlap": ["info1", "info2", "info3", "info4", "info5", "info30", "info31", "info32"]
    }
    add_requirement(req29)

    req30 = {
        "_id": "info30",
        "type": "list",
        "majorId": "INFO",
        "concentrationName": "UX Design",
        "name": "Design in Context",
        "descr": [
            "Take ONE course for this requirement.",
        ],
        "numberOfRequiredCourses": 1,
        "courseIds": ["INFO2921", "INFO4240", "INFO4420", "INFO4505", "INFO4940"],
        "courseNotes": [{
            "courseId": "INFO4940",
            "grpIdentifierArray": ["Clockwork: Infrastructure, Work, and Time",
                                   "Design Thinking, Media, and Community",
                                   "Human-AI Interaction Design Research",
                                   "Technology and Social Change Practicum"]
        }],
        "overlap": ["info1", "info2", "info3", "info4", "info5", "info29", "info31", "info32"]
    }
    add_requirement(req30)

    req31 = {
        "_id": "info31",
        "type": "list",
        "majorId": "INFO",
        "concentrationName": "UX Design",
        "name": "Knowing the User",
        "descr": [
            "Take ONE course for this requirement.",
        ],
        "numberOfRequiredCourses": 1,
        "courseIds": [
            "INFO4125",
            "INFO4430",
            "INFO4450",
            "INFO4490",
            "COMM4380",
            "PSYCH3420",
        ],
        "overlap": ["info1", "info2", "info3", "info4", "info5", "info29", "info30", "info32"]
    }
    add_requirement(req31)

    req32 = {
        "_id": "info32",
        "type": "list",
        "majorId": "INFO",
        "concentrationName": "UX Design",
        "name": "Knowing the Technology",
        "descr": [
            "Take ONE course for this requirement.",
        ],
        "numberOfRequiredCourses": 1,
        "courseIds": [
            "INFO3152",
            "INFO4152",
            "INFO4310",
            "INFO4320",
            "INFO4340",
            "CS5150",
        ],
        "overlap": ["info1", "info2", "info3", "info4", "info5", "info29", "info30", "info31"]
    }
    add_requirement(req32)


if __name__ == "__main__":
    commit_INFO() 