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
        "rawBasicRequirements": [
            {
                "requirements": ["info1", "info2", "info3", "info4"],
            },
        ],
        "concentrations": [
            {
                "concentrationName": "Behavioral Science",
                "requirements": ["info6", "info7", "info8"],
            },
            {
                "concentrationName": "Data Science",
                "requirements": ["info9", "info10", "info11", "info12"],
            },
            {
                "concentrationName": "Digital Culture and Production (Design Focused)",
                "requirements": ["info13", "info14", "info15"],
            },
            {
                "concentrationName": "Digital Culture and Production (Culture Focused)",
                "requirements": ["info16", "info17"],
            },
            {
                "concentrationName": "Information Ethics, Law, and Policy",
                "requirements": ["info18", "info19", "info20", "info21"],
            },
            {
                "concentrationName": "Interactive Technology",
                "requirements": ["info22", "info23", "info24", "info25"],
            },
            {
                "concentrationName": "Networks, Crowds, and Markets",
                "requirements": ["info26", "info27", "info28"],
            },
            {
                "concentrationName": "UX Design",
                "requirements": ["info29", "info30", "info31", "info32"],
            },
        ],
        "rawEndRequirements" : [
            {
                "requirements": ["info5"],
            },
        ],
        "onboardingCourses": [
            "INFO1200",
            "INFO1260",
            "INFO1300",
            "INFO1998",
            "CS1110",
            "MATH1110",
            "INFO2040",
            "INFO2450",
            "INFO2950",
            "INFO2951",
        ],
    }
    add_major(major)

    req1 = {
        "_id": "info1",
        "type": "C",
        "majorId": "INFO",
        "name": "Core",
        "tag": "INFO Core",
        "tagDescr": "This is a core course of Information Science major",
        "descr": [
            "Information Science students must take at lease one course from each of the course group listed below.",
        ],
        "numberOfRequiredCourses": 5,
        "courseGrps": [
            {"_id": 1, "courseIds": ["INFO1200", "INFO1260"]},
            {"_id": 2, "courseIds": ["INFO1300"]},
            {"_id": 3, "courseIds": ["INFO2040"]},
            {"_id": 4, "courseIds": ["INFO2450"]},
            {"_id": 5, "courseIds": ["INFO2950", "INFO2951"]},
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
        "type": "E",
        "majorId": "INFO",
        "name": "Programming",
        "tag": "INFO Programming",
        "tagDescr": "This can be counted as a programming course for Information Science major",
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
        "type": "E",
        "majorId": "INFO",
        "name": "Math",
        "tag": "INFO Math",
        "tagDescr": "This can be counted as a math course for Information Science major",
        "descr": [
            "Take a Calculus I course (MATH 1106, MATH 1110, or MATH 1910) for letter grade to fulfill the math requirement. ",
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
        "type": "E",
        "majorId": "INFO",
        "name": "Statistics",
        "tag": "INFO Stats",
        "tagDescr": "This can be counted as a statistic course for Information Science major",
        "descr": [
            "Take one of the statistics courses provided below. ",
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
        excluded=["INFO4998", "INFO4910", "INFO5900"],
        included=["INFO2300", "INFO2310", "CS2110", "CS2112", "CS3110", "CS3410"],
    )
    req5 = {
        "_id": "info5",
        "type": "E",
        "majorId": "INFO",
        "name": "Electives",
        "tag": "INFO Electives",
        "tagDescr": "This can be counted as an elective for Information Science major",
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
        "type": "E",
        "majorId": "INFO",
        "name": "Social Behavior",
        "tag": "Social Behavior",
        "tagDescr": "This can be counted as a Social Behavior course for the Behavioral Science concentration in Information Science major.",
        "descr": ["Take two of the courses listed below."],
        "numberOfRequiredCourses": 2,
        "courseIds": [
            "INFO3460",
            "INFO4430",
            "INFO4450",
            "INFO4490",
            "INFO4500",
            "INFO4505",
            "INFO4800",
            "COMM4380",
            "PSYCH3800",
        ],
        "overlap": ["info1", "info2", "info3", "info4", "info5", "info7", "info8"]
    }
    add_requirement(req6)

    req7 = {
        "_id": "info7",
        "type": "E",
        "majorId": "INFO",
        "name": "Social Data Analytics",
        "tag": "Behavioral Data",
        "tagDescr": "This can be counted as a Social Data Analytics course for the Behavioral Science concentration in Information Science major.",
        "descr": [
            "Take one of the courses listed below",
        ],
        "numberOfRequiredCourses": 1,
        "courseIds": [
            "INFO3300",
            "INFO3950",
            "INFO4100",
            "INFO4300",
            "INFO4350",
            "COMM4242",
            "CS4740",
            "CS3780",
        ],
        "overlap": ["info1", "info2", "info3", "info4", "info5", "info6", "info8"]
    }
    add_requirement(req7)

    req8 = {
        "_id": "info8",
        "type": "E",
        "majorId": "INFO",
        "name": "Behavior in Context",
        "tag": "Behavior in Context",
        "tagDescr": "This can be counted as a Behavior in Sociological Context course for the Behavioral Science concentration in Information Science major.",
        "descr": [
            "Take one of the courses listed below.",
        ],
        "numberOfRequiredCourses": 1,
        "courseIds": [
            "INFO3200",
            "INFO3561",
            "INFO4650",
            "STS3440",
            "INFO4360",
            "SOC3350",
            "INFO3450",
            "INFO4240",
            "INFO4400",
        ],
        "overlap": ["info1", "info2", "info3", "info4", "info5", "info6", "info7"]
    }
    add_requirement(req8)

    req9 = {
        "_id": "info9",
        "type": "E",
        "majorId": "INFO",
        "name": "Data Analysis",
        "tag": "Data Analysis",
        "tagDescr": "This can be counted as a Data Analysis course for the Data Science concentration in Information Science major.",
        "descr": [
            "Consists of advanced courses in machine learning, data mining, and analytics across departments.",
            "Take one of the courses listed below.",
        ],
        "numberOfRequiredCourses": 1,
        "courseIds": [
            "INFO3300",
            "INFO3900",
            "INFO3950",
            "CS3780",
            "CS4786",
            "ORIE3120",
            "ORIE4740",
            "ORIE3741",
            "STSCI3740",
        ],
        "overlap": ["info1", "info2", "info3", "info4", "info5", "info10", "info11", "info12"]
    }
    add_requirement(req9)

    req10 = {
        "_id": "info10",
        "type": "E",
        "majorId": "INFO",
        "name": "Domain Expertise",
        "tag": "Data Domain",
        "tagDescr": "This can be counted as a Domain Expertise course for the Data Science concentration in Information Science major.",
        "descr": [
            "Features specialized courses applying data science across diverse fields including sustainability, language processing, and social science.",
            "Take one of the courses listed below.",
        ],
        "numberOfRequiredCourses": 1,
        "courseIds": [
            "INFO2770",
            "INFO3350",
            "INFO3370",
            "INFO4100",
            "INFO4120",
            "INFO4300",
            "INFO4350",
            "CS4740",
            "PUBPOL2130",
        ],
        "overlap": ["info1", "info2", "info3", "info4", "info5", "info9", "info11", "info12"]
    }
    add_requirement(req10)

    req11 = {
        "_id": "info11",
        "type": "E",
        "majorId": "INFO",
        "name": "Big Data Ethics, Policy and Society",
        "tag": "Data Ethics",
        "tagDescr": "This can be counted as a Big Data Ethics, Policy and Society course for the Data Science concentration in Information Science major.",
        "descr": [
            "Includes courses examining the social, ethical, legal, and policy implications of data science and technology.",
            "Take one of the courses listed below.",
        ],
        "numberOfRequiredCourses": 1,
        "courseIds": [
            "INFO3200",
            "INFO3561",
            "INFO4145",
            "INFO4200",
            "INFO4240",
            "INFO4250",
            "INFO4260",
            "INFO4270",
            "INFO4390",
            "INFO4561",
            "COMM4242",
            "ENGL3778",
            "PUBPOL3460",
            "STS3440",
        ],
        "overlap": ["info1", "info2", "info3", "info4", "info5", "info9", "info10", "info12"]
    }
    add_requirement(req11)

    req12 = {
        "_id": "info12",
        "type": "E",
        "majorId": "INFO",
        "name": "Data Communication",
        "tag": "Data Communication",
        "tagDescr": "This can be counted as a Data Communication course for the Data Science concentration in Information Science major.",
        "descr": [
            "Covers courses in data visualization, information communication, and data-oriented research methods.",
            "Take one of the courses listed below.",
        ],
        "numberOfRequiredCourses": 1,
        "courseIds": [
            "INFO3312",
            "INFO4310",
            "COMM3150",
            "COMM3189",
            "COMM4200",
            "COMM4860",
            "GOVT2169",
            "SOC3580",
        ],
        "overlap": ["info1", "info2", "info3", "info4", "info5", "info9", "info10", "info11"]
    }
    add_requirement(req12)

    req13 = {
        "_id": "info13",
        "type": "E",
        "majorId": "INFO",
        "name": "Digital Culture and History",
        "tag": "Digital Culture",
        "tagDescr": "This can be counted as a Digital Culture and History course for the Digital Culture and Production concentration in Information Science major.",
        "descr": [
            "You can choose to take 1 course in this section and 2 courses in the Design section."
            "You can also choose to take 3 courses in this section and 0 course in the Design section."
        ],
        "numberOfRequiredCourses": 1,
        "courseIds": [
            "INFO2921",
            "INFO3200",
            "INFO3561",
            "INFO4260",
            "STS3440",
            "STS4040",
        ],
        "overlap": ["info1", "info2", "info3", "info4", "info5", "info14", "info15"]
    }
    add_requirement(req13)

    req14 = {
        "_id": "info14",
        "type": "E",
        "majorId": "INFO",
        "name": "Digital Production",
        "tag": "Digital Production",
        "tagDescr": "This can be counted as a Digital Production course for the Digital Culture and Production concentration in Information Science major.",
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
        "overlap": ["info1", "info2", "info3", "info4", "info5", "info13", "info15"]
    }
    add_requirement(req14)

    req15 = {
        "_id": "info15",
        "type": "E",
        "majorId": "INFO",
        "name": "Media, Art, Design",
        "tag": "Media Design",
        "tagDescr": "This can be counted as a Media, Art, Design course for the Digital Culture and Production concentration in Information Science major.",
        "descr": [
            "Take two courses in this section.",
            "You do not need to take course in this section if you plan to take three courses in the Digital Culture and History section.",
        ],
        "numberOfRequiredCourses": 2,
        "courseIds": [
            "INFO2750",
            "INFO3450",
            "INFO3660",
            "INFO4152",
            "INFO4240",
            "INFO4400",
            "INFO4420",
            "ART3705",
            "ARTH4151",
            "ARTH4154",
            "COML3115",
            "HIST2293",
        ],
        "overlap": ["info1", "info2", "info3", "info4", "info5", "info13", "info14"]
    }
    add_requirement(req15)
    
    req16 = {
        "_id": "info16",
        "type": "E",
        "majorId": "INFO",
        "name": "Digital Culture and History",
        "tag": "Digital Culture",
        "tagDescr": "This can be counted as a Digital Culture and History course for the Digital Culture and Production concentration in Information Science major.",
        "descr": [
            "You can choose to take 1 course in this section and 2 courses in the Design section."
            "You can also choose to take 3 courses in this section and 0 course in the Design section."
        ],
        "numberOfRequiredCourses": 3,
        "courseIds": [
            "INFO2921",
            "INFO3200",
            "INFO3561",
            "INFO4260",
            "STS3440",
            "STS4040",
        ],
        "overlap": ["info1", "info2", "info3", "info4", "info5", "info17"]
    }
    add_requirement(req16)
    
    req17 = {
        "_id": "info17",
        "type": "E",
        "majorId": "INFO",
        "name": "Digital Production",
        "tag": "Digital Production",
        "tagDescr": "This can be counted as a Digital Production course for the Digital Culture and Production concentration in Information Science major.",
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
        "type": "E",
        "majorId": "INFO",
        "name": "Frameworks and Institutions",
        "tag": "Ethics Frameworks",
        "tagDescr": "This can be counted as a Frameworks and Institutions course for the Information Ethics, Law, and Policy concentration in Information Science major.",
        "descr": ["Take one course in this section."],
        "numberOfRequiredCourses": 1,
        "courseIds": [
            "INFO4113",
            "INFO4200",
            "INFO4250",
            "INFO4301",
            "HADM4890",
            "PUBPOL3460",
            "STS2761",
        ],
        "overlap": ["info1", "info2", "info3", "info4", "info5", "info19", "info20", "info21"]
    }
    add_requirement(req18)

    req19 = {
        "_id": "info19",
        "type": "E",
        "majorId": "INFO",
        "name": "Methods and Analysis",
        "tag": "Ethics Methods",
        "tagDescr": "This can be counted as a Methods and Analysis course for the Information Ethics, Law, and Policy concentration in Information Science major.",
        "descr": ["Take one course in this section."],
        "numberOfRequiredCourses": 1,
        "courseIds": [
            "INFO2921",
            "INFO4240",
            "INFO4800",
            "COMM4242",
            "CRP3210",
            "PUBPOL2300",
        ],
        "overlap": ["info1", "info2", "info3", "info4", "info5", "info18", "info20", "info21"]
    }
    add_requirement(req19)

    req20 = {
        "_id": "info20",
        "type": "E",
        "majorId": "INFO",
        "name": "Cases / Topics",
        "tag": "Ethics Cases",
        "tagDescr": "This can be counted as a Cases / Topics course for the Information Ethics, Law, and Policy concentration in Information Science major.",
        "descr": ["Take one course in this section."],
        "numberOfRequiredCourses": 1,
        "courseIds": [
            "INFO3200",
            "INFO3460",
            "INFO3561",
            "INFO4145",
            "INFO4260",
            "INFO4270",
            "INFO4390",
            "INFO4561",
            "STS3440",
            "STS4040",
        ],
        "overlap": ["info1", "info2", "info3", "info4", "info5", "info18", "info19", "info21"]
    }
    add_requirement(req20)

    req21 = {
        "_id": "info21",
        "type": "E",
        "majorId": "INFO",
        "name": "Tools and Technical Domains",
        "tag": "Ethics Tools",
        "tagDescr": "This can be counted as a Tools and Technical Domains course for the Information Ethics, Law, and Policy concentration in Information Science major.",
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
        "type": "E",
        "majorId": "INFO",
        "name": "Object-Oriented Programming",
        "tag": "OOP",
        "tagDescr": "This is a core course for the Interactive Technologies concentration in Information Science major.",
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
        "type": "E",
        "majorId": "INFO",
        "name": "Building with Hardware",
        "tag": "IT Hardware",
        "tagDescr": "This can be counted as a Building with Hardware course for the Interactive Technologies concentration in Information Science major.",
        "descr": [
            "Take one of the three courses for this requirement.",
        ],
        "numberOfRequiredCourses": 1,
        "courseIds": ["INFO4120", "INFO4320", "CS4758"],
        "overlap": ["info1", "info2", "info3", "info4", "info5", "info22", "info24", "info25"]
    }
    add_requirement(req23)

    req24 = {
        "_id": "info24",
        "type": "E",
        "majorId": "INFO",
        "name": "Working with Data/Software",
        "tag": "IT Software",
        "tagDescr": "This can be counted as a Working with Data/Software course for the Interactive Technologies concentration in Information Science major.",
        "descr": [
            "Take one of the courses for this requirement.",
        ],
        "numberOfRequiredCourses": 1,
        "courseIds": [
            "INFO3300",
            "INFO4340",
            "INFO4555",
            "CS4620",
            "CS3780",
            "CS4786",
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
        "type": "E",
        "majorId": "INFO",
        "name": "Context/Application Domains",
        "tag": "IT Context",
        "tagDescr": "This can be counted as a Context/Application Domains course for the Interactive Technologies concentration in Information Science major.",
        "descr": [
            "Take one of the courses for this requirement.",
        ],
        "numberOfRequiredCourses": 1,
        "courseIds": [
            "INFO4152",
            "INFO4154",
            "INFO4275",
            "INFO4310",
            "INFO4410",
            "INFO4430",
            "INFO4505",
            "INFO4940",
            "INFO4940",
            "CS4752",
        ],
        "overlap": ["info1", "info2", "info3", "info4", "info5", "info22", "info23", "info24"]
    }
    add_requirement(req25)
    
    req26 = {
        "_id": "info26",
        "type": "E",
        "majorId": "INFO",
        "name": "Models",
        "tag": "Network Models",
        "tagDescr": "This can be counted as a Models course for the Networks, Crowds, and Markets concentration in Information Science major.",
        "descr": [
            "Take two of the courses for this requirement.",
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
        "overlap": ["info1", "info2", "info3", "info4", "info5", "info27", "info28"]
    }
    add_requirement(req26)
    
    req27 = {
        "_id": "info27",
        "type": "E",
        "majorId": "INFO",
        "name": "Data",
        "tag": "Network Data",
        "tagDescr": "This can be counted as a Data course for the Networks, Crowds, and Markets concentration in Information Science major.",
        "descr": [
            "Take one of the courses for this requirement.",
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
        "overlap": ["info1", "info2", "info3", "info4", "info5", "info26", "info28"]
    }
    add_requirement(req27)
    
    req28 = {
        "_id": "info28",
        "type": "E",
        "majorId": "INFO",
        "name": "Policy / Values",
        "tag": "Network Policy",
        "tagDescr": "This can be counted as a Policy / Values course for the Networks, Crowds, and Markets concentration in Information Science major.",
        "descr": [
            "Take one of the courses for this requirement.",
        ],
        "numberOfRequiredCourses": 1,
        "courseIds": [
            "INFO4140",
            "INFO4145",
            "INFO4200",
            "INFO4240",
            "INFO4250",
            "INFO4940",
            "PUBPOL3460",
        ],
        "overlap": ["info1", "info2", "info3", "info4", "info5", "info26", "info27"]
    }
    add_requirement(req28)

    req29 = {
        "_id": "info29",
        "type": "E",
        "majorId": "INFO",
        "name": "Core Principles of Design",
        "tag": "UX Principles",
        "tagDescr": "This can be counted as a Core Principle course for the UX Design concentration in Information Science major.",
        "descr": [
            "Take one of the courses for this requirement.",
        ],
        "numberOfRequiredCourses": 1,
        "courseIds": [
            "INFO3450",
            "INFO4400",
            "INFO4410",
        ],
        "overlap": ["info1", "info2", "info3", "info4", "info5", "info30", "info31", "info32"]
    }
    add_requirement(req29)

    req30 = {
        "_id": "info30",
        "type": "E",
        "majorId": "INFO",
        "name": "Design in Context",
        "tag": "UX Context",
        "tagDescr": "This can be counted as a Context course for the UX Design concentration in Information Science major.",
        "descr": [
            "Take one of the courses for this requirement.",
        ],
        "numberOfRequiredCourses": 1,
        "courseIds": ["INFO2921", "INFO4240", "INFO4420", "INFO4505"],
        "overlap": ["info1", "info2", "info3", "info4", "info5", "info29", "info31", "info32"]
    }
    add_requirement(req30)

    req31 = {
        "_id": "info31",
        "type": "E",
        "majorId": "INFO",
        "name": "Knowing the User",
        "tag": "UX User",
        "tagDescr": "This can be counted as a Knowing the User course for the UX Design concentration in Information Science major.",
        "descr": [
            "Take one of the courses for this requirement.",
        ],
        "numberOfRequiredCourses": 1,
        "courseIds": [
            "INFO3460",
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
        "type": "E",
        "majorId": "INFO",
        "name": "Knowing the Technology",
        "tag": "UX Technology",
        "tagDescr": "This can be counted as a Knowing the Technology course for the UX Design concentration in Information Science major.",
        "descr": [
            "Take one of the courses for this requirement.",
        ],
        "numberOfRequiredCourses": 1,
        "courseIds": [
            "INFO3152",
            "INFO4152",
            "INFO4154",
            "INFO4275",
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