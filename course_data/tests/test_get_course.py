import unittest
import sys
import os
import requests
from typing import Dict, Any, List

# Add the root directory to the Python path
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.append(root_dir)

# Now we can import from both the root and the course_data directory
from const import *
from course_data.get_course import (
    get_instructors,
    get_group_identifier
)

def fetch_course_data(subject: str, catalog_nbr: str, semester: str) -> Dict[str, Any]:
    """
    Fetch course data from the Class Roster API.
    
    Args:
        subject: Course subject code (e.g., "CS")
        catalog_nbr: Course number (e.g., "1110")
        semester: Semester code (e.g., "SP25")
        
    Returns:
        Dictionary containing the course data
    """
    url = f"https://classes.cornell.edu/api/2.0/search/classes.json"
    params = {
        "roster": semester,
        "subject": subject,
        "catalogNbr": catalog_nbr
    }
    
    response = requests.get(url, params=params)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch data: {response.status_code}")
        
    data = response.json()
    if data["status"] != "success":
        raise Exception(f"API returned error: {data.get('message', 'Unknown error')}")
        
    # Find the specific course in the results
    courses = data["data"]["classes"]
    for course in courses:
        if course["subject"] == subject and course["catalogNbr"] == catalog_nbr:
            return course
            
    raise Exception(f"Course {subject} {catalog_nbr} not found in {semester}")

class TestGetCourseNew(unittest.TestCase):
    def setUp(self):
        """Set up test cases with real data from the API"""
        # Category 1: Single section courses
        self.single_section = fetch_course_data("INFO", "2040", "FA25")
        
        # Category 2: Multiple sections courses
        self.multiple_sections = fetch_course_data("INFO", "1200", "FA25")
        
        # Category 3: Courses with topics
        self.with_topics = fetch_course_data("INFO", "1998", "FA25")
        
        # Category 4: Independent study courses
        self.independent_study = fetch_course_data("INFO", "4900", "FA25")

    # Test get_instructors function
    def test_get_instructors(self):
        """Test getting instructors from a single section course"""
        
        # INFO 2040 FA25
        result = get_instructors(self.single_section["enrollGroups"][0])
        self.assertEqual([
            {"netid": "rl932", "name": "Rohit Lamba"},
            {"netid": "yy994", "name": "Yian Yin"}
        ], result)
        
        # INFO 1200 FA25
        result = get_instructors(self.multiple_sections["enrollGroups"][0])
        self.assertEqual([
            {"netid": "ds2423", "name": "Daniel Susser"},
            {"netid": "gv232", "name": "Gili Vidan"}
        ], result)

        # INFO 1998 FA25
        result = get_instructors(self.with_topics["enrollGroups"][0])
        self.assertEqual([
            {"netid": "wmw2", "name": "Walker Mcmillan White"},
        ], result)

        # INFO 4900 FA25
        result = get_instructors(self.independent_study["enrollGroups"][0])
        self.assertEqual([
            {"netid": "sb882", "name": "Solon Barocas"},
        ], result)

    # Test get_group_identifier function
    def test_get_group_identifier(self):
        """Test getting group identifier when sections have topics"""
        # With Topics (INFO 1998 FA25)
        identifier, has_topic = get_group_identifier(self.with_topics["enrollGroups"][0])
        self.assertTrue(has_topic)
        self.assertEqual(identifier, "Intro to Digital Product Design")
        
        # IND Sections (INFO 4900 FA25)
        identifier, has_topic = get_group_identifier(self.independent_study["enrollGroups"][0])
        self.assertFalse(has_topic)
        self.assertEqual(identifier, "Barocas")
        
        # Regular Sections (INFO 2040 FA25)
        identifier, has_topic = get_group_identifier(self.single_section["enrollGroups"][0])
        self.assertFalse(has_topic)
        self.assertIn("LEC-001", identifier) 

if __name__ == '__main__':
    # Create a test instance to access the test data
    test = TestGetCourseNew()
    test.setUp()  # Initialize the test data
    
    # Also run the tests
    unittest.main()