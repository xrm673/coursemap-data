from common import *

def commit_CAS():
    college = {
        "_id": "CAS",
        "name": "College of Arts and Sciences",
        "type": "college",
        "needsYear": False,
        "needsMajor": False,
        "needsCollege": False,
        "rawBasicSections": [],
        "majors": [
        {
            "majorId": "ARTH",
            "name": "History of Art",
        },
        {
            "majorId": "CS",
            "name": "Computer Science",
        },
        {
            "majorId": "ECON",
            "name": "Economics",
        },
        {
            "majorId": "INFO",
            "name": "Information Science",
        },
        {
            "majorId": "PHYS",
            "name": "Physics",
        },
        ],
    }
    add_college(college)
    
if __name__ == "__main__":
    commit_CAS()