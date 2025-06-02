from pymongo import MongoClient
from dotenv import load_dotenv
import certifi
import os

load_dotenv()
mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri, tlsCAFile=certifi.where())  # Add SSL certificate verification
db = client["CourseMap"]
majors_collection = db["majors"]
requirements_collection = db["requirements"]
courses_collection = db["courses"]

# Set up indexes
majors_collection.create_index([("name", 1)])
majors_collection.create_index([("colleges._id", 1)])

def add_major(major_data):
    majors_collection.replace_one({"_id": major_data["_id"]}, major_data, upsert=True)
    print(f"Added/Updated major: {major_data['_id']}")


def add_requirement(req_data):
    requirements_collection.replace_one({"_id": req_data["_id"]}, req_data, upsert=True)
    print(f"Added/Updated requirement: {req_data['_id']}") 