import firebase_admin
from firebase_admin import credentials, firestore

# Load Firebase credentials
cred = credentials.Certificate("config/credentials.json")
firebase_admin.initialize_app(cred)

# Initialize Firestore
db = firestore.client()

print("✅ Firebase Firestore connection successful!")