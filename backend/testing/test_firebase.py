from config.firebase_setup import db

# Reference to Firestore collection
test_ref = db.collection("test_collection")

# Write sample data
test_ref.document("test_doc").set({"message": "Firebase is working!"})

# Read sample data
doc = test_ref.document("test_doc").get()

if doc.exists:
    print(f"✅ Firestore Test Passed: {doc.to_dict()}")
else:
    print("❌ Firestore Test Failed: Document not found")