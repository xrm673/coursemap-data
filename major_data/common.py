from pymongo import MongoClient
from dotenv import load_dotenv
import certifi
import os

load_dotenv()
mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri, tlsCAFile=certifi.where())  # Add SSL certificate verification
db = client["CourseMap"]
programs_collection = db["programs"]
requirements_collection = db["requirements"]
courses_collection = db["courses"]

# Set up indexes
programs_collection.create_index([("name", 1)])
programs_collection.create_index([("colleges.collegeId", 1)])

def add_major(major_data):
    programs_collection.replace_one({"_id": major_data["_id"]}, major_data, upsert=True)
    print(f"Added/Updated major: {major_data['_id']}")


def add_requirement(req_data):
    requirements_collection.replace_one({"_id": req_data["_id"]}, req_data, upsert=True)
    print(f"Added/Updated requirement: {req_data['_id']}") 