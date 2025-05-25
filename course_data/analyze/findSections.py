import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os
from pathlib import Path
import json
from collections import Counter

# Get the home directory and construct path to service account
home_dir = str(Path.home())
service_account_path = os.path.join(home_dir, '.config', 'firebase', 'service-account.json')

print(f"Using service account from: {service_account_path}")

# Initialize Firebase
try:
    firebase_admin.get_app()
except ValueError:
    cred = credentials.Certificate(service_account_path)
    firebase_admin.initialize_app(cred)

db = firestore.client()

def find_section_types_with_examples():
    # Get all sections
    print("Fetching sections from Firestore...")
    sections = db.collection('sections').get()
    
    # Create a dictionary to track unique section types and example course codes
    section_types_dict = {}
    
    # Extract the 'type' field and courseId from each section
    print("Processing sections...")
    section_count = 0
    for section in sections:
        section_count += 1
        section_data = section.to_dict()
        section_type = section_data.get('type')
        course_id = section_data.get('courseId')
        
        if section_type and course_id:
            # Only store the first example we find for each type
            if section_type not in section_types_dict:
                section_types_dict[section_type] = course_id
    
    # Convert dictionary to list of dictionaries for output
    section_types_list = [
        {"type": type_name, "example_course": course_id}
        for type_name, course_id in sorted(section_types_dict.items())
    ]
    
    print(f"Processed {section_count} sections.")
    return section_types_list

def find_component_combinations():
    # Get all enrollment groups
    print("Fetching enrollment groups from Firestore...")
    enrollgroups = db.collection('enrollGroups').get()
    
    # Dictionary to track combinations with counts
    combination_counts = Counter()
    
    # Dictionary to track example course IDs for each combination
    combination_examples = {}
    
    # Process enrollment groups
    print("Processing enrollment groups...")
    group_count = 0
    for group in enrollgroups:
        group_count += 1
        group_data = group.to_dict()
        
        # Get components array and course ID
        components = group_data.get('components', [])
        course_id = group_data.get('courseId')
        
        if components:
            # Sort and convert to tuple to use as dictionary key
            components_tuple = tuple(sorted(components))
            
            # Increment counter
            combination_counts[components_tuple] += 1
            
            # Store an example course ID if we don't have one yet
            if components_tuple not in combination_examples and course_id:
                combination_examples[components_tuple] = course_id
    
    # Convert to a list of dictionaries with combination, count, and example
    combinations_list = []
    for components_tuple, count in combination_counts.most_common():
        combinations_list.append({
            "components": list(components_tuple),
            "count": count,
            "example_course": combination_examples.get(components_tuple, "")
        })
    
    print(f"Processed {group_count} enrollment groups.")
    print(f"Found {len(combinations_list)} unique component combinations.")
    
    return combinations_list

# Execute both functions
print("Step 1: Finding section types...")
section_types = find_section_types_with_examples()

print("\nStep 2: Finding component combinations...")
combinations = find_component_combinations()

# Create combined results
combined_results = {
    "section_types": section_types,
    "component_combinations": combinations
}

# Print summary
print("\nAnalysis complete:")
print(f"- Found {len(section_types)} unique section types")
print(f"- Found {len(combinations)} unique component combinations")

# Save to JSON file in the current directory
output_path = "sections_analysis.json"
with open(output_path, 'w') as json_file:
    json.dump(combined_results, json_file, indent=2)

print(f"\nCombined results saved to {output_path}")