from common import *

def commit_CALS():
    college = {
        "_id": "CALS",
        "name": "College of Agriculture and Life Sciences",
        "type": "college",
        "needsYear": False,
        "needsMajor": False,
        "needsCollege": False,
        "rawBasicSections": [],
        "majors": [
            {
                "majorId": "INFO",
                "name": "Information Science",
            }
        ]
    }
    add_college(college)
    
if __name__ == "__main__":
    commit_CALS()