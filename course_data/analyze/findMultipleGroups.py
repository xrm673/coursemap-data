import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from collections import defaultdict
import json
from pathlib import Path
import os

# Initialize Firebase (replace with your actual path to credentials file)
home_dir = str(Path.home())
service_account_path = os.path.join(home_dir, '.config', 'firebase', 'service-account.json')
cred = credentials.Certificate(service_account_path)
firebase_admin.initialize_app(cred)

db = firestore.client()

def find_multiple_enrollgroups():
    # Get all enrollment groups
    enrollgroups = db.collection('enrollGroups').get()
    
    # Create a dictionary to track courses and their enrollment groups by semester
    course_semester_groups = defaultdict(lambda: defaultdict(list))
    
    # Organize enrollment groups by course and semester
    for group in enrollgroups:
        group_data = group.to_dict()
        course_id = group_data.get('courseId')
        semester = group_data.get('semester')
        group_id = group_data.get('id')
        
        if course_id and semester:
            course_semester_groups[course_id][semester].append(group_id)
    
    # Find courses with multiple enrollment groups in the same semester
    results = {}
    for course_id, semesters in course_semester_groups.items():
        multiple_groups = {}
        for semester, groups in semesters.items():
            if len(groups) > 1:
                multiple_groups[semester] = groups
        
        if multiple_groups:
            results[course_id] = multiple_groups
    
    return results

# Execute the function
multiple_enrollgroups = find_multiple_enrollgroups()
print(f"Found {len(multiple_enrollgroups)} courses with multiple enrollment groups in the same semester")

# Format results for JSON export
json_results = {}
for course_id, semesters in multiple_enrollgroups.items():
    json_results[course_id] = {}
    for semester, groups in semesters.items():
        json_results[course_id][semester] = groups

# Write to JSON file
with open('courses_with_multiple_enrollgroups.json', 'w') as json_file:
    json.dump(json_results, json_file, indent=2)

print("Results saved to courses_with_multiple_enrollgroups.json")