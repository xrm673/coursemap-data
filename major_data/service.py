from common import *


def get_course(course_id):
    """
    Get a single course by its ID.
    
    Args:
        course_id: The course ID (e.g., 'CS1110')
        
    Returns:
        The course document or None if not found
    """
    return courses_collection.find_one({"_id": course_id})


def get_courses_by_subject(subject, min_credit=0, excluded=[], included=[]):
    """
    Get all courses for a subject that meet the minimum credit requirement.
    
    Args:
        subject: The subject code (e.g., 'CS')
        min_credit: Minimum credits required (default: 0)
        excluded: List of course IDs to exclude
        included: List of course IDs to include regardless of criteria
        
    Returns:
        List of course IDs meeting the criteria
    """
    # Query by subject field
    query = {"sbj": subject}
    
    # Exclude specific courses if any
    if excluded:
        query["_id"] = {"$nin": excluded}
    
    results = courses_collection.find(query)
    course_ids = []
    
    for doc in results:
        if meets_credit_requirement(doc, min_credit):
            course_ids.append(doc["_id"])
    
    # Add included courses if not already in list
    for course_id in included:
        if course_id not in course_ids:
            course_ids.append(course_id)
            
    return course_ids


def get_courses_by_subject_level(
    subject, level, min_credit=0, excluded=[], included=[]
):
    """
    Get all courses for a subject and level that meet the minimum credit requirement.
    
    Args:
        subject: The subject code (e.g., 'CS')
        level: The course level (1-5)
        min_credit: Minimum credits required (default: 0)
        excluded: List of course IDs to exclude
        included: List of course IDs to include regardless of criteria
        
    Returns:
        List of course IDs meeting the criteria
    """
    # Query by subject and level fields
    query = {
        "sbj": subject,
        "lvl": level
    }
    
    # Exclude specific courses if any
    if excluded:
        query["_id"] = {"$nin": excluded}
    
    results = courses_collection.find(query)
    course_ids = []
    
    for doc in results:
        if meets_credit_requirement(doc, min_credit):
            course_ids.append(doc["_id"])
    
    # Add included courses if not already in list
    for course_id in included:
        if course_id not in course_ids:
            course_ids.append(course_id)
            
    return course_ids


def get_courses_by_subject_min_level(
    subject, min_level, max_level=5, min_credit=0, excluded=[], included=[]
):
    """
    Get all courses for a subject between min_level and max_level that meet the minimum credit requirement.
    
    Args:
        subject: The subject code (e.g., 'CS')
        min_level: Minimum course level (1-5)
        max_level: Maximum course level (default: 5)
        min_credit: Minimum credits required (default: 0)
        excluded: List of course IDs to exclude
        included: List of course IDs to include regardless of criteria
        
    Returns:
        List of course IDs meeting the criteria
    """
    # Query by subject and level range
    query = {
        "sbj": subject,
        "lvl": {"$gte": min_level, "$lte": max_level}
    }
    
    # Exclude specific courses if any
    if excluded:
        query["_id"] = {"$nin": excluded}
    
    results = courses_collection.find(query)
    course_ids = []
    
    for doc in results:
        if meets_credit_requirement(doc, min_credit):
            course_ids.append(doc["_id"])
    
    # Add included courses if not already in list
    for course_id in included:
        if course_id not in course_ids:
            course_ids.append(course_id)
            
    return course_ids

def meets_credit_requirement(course: dict, min_credit: float) -> bool:
    """
    Check if any enrollment group in the course meets the minimum credit requirement.
    
    Args:
        course: Course document from MongoDB
        min_credit: Minimum credits required
        
    Returns:
        True if any enrollment group has a credit value >= min_credit, False otherwise
    """
    if "enrollGroups" not in course:
        return False
        
    for group in course["enrollGroups"]:
        if "credits" in group:
            if any(credit >= min_credit for credit in group["credits"]):
                return True
    return False