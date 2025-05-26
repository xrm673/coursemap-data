from common import db

def get_course(course_id):
    course_ref = db.collection("courses").document(course_id)
    course_doc = course_ref.get()
    result = course_doc.to_dict()
    return result


def get_courses_by_subject(subject, min_credit=0, excluded=[], included=[]):
    courses_ref = db.collection("courses")
    query = courses_ref.where("sbj", "==", subject)
    results = query.stream()
    course_ids = []
    for doc in results:
        doc_data = doc.to_dict()
        if doc.id in excluded:
            continue
        qualified = False
        # Check credits in each enrollGroup
        if "enrollGroups" in doc_data:
            for group in doc_data["enrollGroups"]:
                if "credits" in group:
                    for credit in group["credits"]:
                        if credit >= min_credit:
                            qualified = True
                            break
                if qualified:
                    break
        if qualified:
            course_ids.append(doc.id)
    course_ids = course_ids + included
    return course_ids


def get_courses_by_subject_level(
    subject, level, min_credit=0, excluded=[], included=[]
):
    """
    Retrieves the IDs of all courses for a specific subject and level.
    Returns:
        list: A list of course IDs (strings) matching the criteria.
    """
    courses_ref = db.collection("courses")
    query = courses_ref.where("sbj", "==", subject).where("lvl", "==", level)
    results = query.stream()

    course_ids = []
    for doc in results:
        if doc.id in excluded:
            continue
        doc_data = doc.to_dict()
        qualified = False
        # Check credits in each enrollGroup
        if "enrollGroups" in doc_data:
            for group in doc_data["enrollGroups"]:
                if "credits" in group:
                    for credit in group["credits"]:
                        if credit >= min_credit:
                            qualified = True
                            break
                if qualified:
                    break
        if qualified:
            course_ids.append(doc.id)
    course_ids = course_ids + included
    return course_ids


def get_courses_by_subject_min_level(
    subject, min_level, max_level=5, min_credit=0, excluded=[], included=[]
):
    course_ids = []
    for level in range(min_level, max_level + 1):
        courses = get_courses_by_subject_level(subject, level, min_credit, excluded)
        course_ids.extend(courses)

    for course_id in included:
        if course_id not in course_ids:
            course_ids.append(course_id)
    return course_ids