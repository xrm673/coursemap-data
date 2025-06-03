from pymongo import MongoClient
from dotenv import load_dotenv
import certifi
import os

load_dotenv()
mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri, tlsCAFile=certifi.where())  # Add SSL certificate verification
db = client["CourseMap"]
colleges_collection = db["colleges"]

# Set up indexes
colleges_collection.create_index([("name", 1)])

def add_college(college_data):
    colleges_collection.replace_one({"_id": college_data["_id"]}, college_data, upsert=True)
    print(f"Added/Updated college: {college_data['_id']}")