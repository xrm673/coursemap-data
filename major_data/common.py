import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from const import SERVICE_ACCOUNT_PATH

# Initialize Firebase if not already initialized
if not firebase_admin._apps:
    if not os.path.exists(SERVICE_ACCOUNT_PATH):
        raise FileNotFoundError(f"Firebase key file not found at: {SERVICE_ACCOUNT_PATH}")
    cred = credentials.Certificate(SERVICE_ACCOUNT_PATH)
    firebase_admin.initialize_app(cred)

db = firestore.client()

def add_major(major_data):
    major_ref = db.collection("majors").document(major_data["id"])
    major_ref.set(major_data)
    print(f"Added major: {major_data['id']}")


def add_requirement(req_data):
    req_ref = db.collection("requirements").document(req_data["id"])
    req_ref.set(req_data)
    print(f"Added requirement: {req_data['id']}") 