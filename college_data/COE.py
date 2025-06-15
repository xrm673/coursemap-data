from common import *

def commit_COE():
    college = {
        "_id": "COE",
        "name": "College of Engineering",
        "type": "college",
        "yearDependent": False,
        "majorDependent": False,
        "collegeDependent": False,
        "rawBasicSections": [],
        "majors": [
            {
                "majorId": "CS",
                "name": "Computer Science",
            }
        ]
    }
    add_college(college)
    
if __name__ == "__main__":
    commit_COE()