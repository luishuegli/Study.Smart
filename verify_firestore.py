import firebase_admin
from firebase_admin import credentials, firestore
import os

# Initialize Firebase (simulating app start)
if not firebase_admin._apps:
    cred = credentials.Certificate("serviceAccountKey.json")
    firebase_admin.initialize_app(cred)

def verify_data():
    db = firestore.client()
    user_id = "dev_user_123"
    
    print(f"Checking data for user: {user_id}")
    doc_ref = db.collection("users").document(user_id)
    doc = doc_ref.get()
    
    if doc.exists:
        data = doc.to_dict()
        print("Document exists!")
        print(f"Data: {data}")
        
        progress = data.get("progress", {})
        if progress:
            print("✅ Progress data found.")
            return True
        else:
            print("⚠️ Document exists but 'progress' field is empty or missing.")
            return False
    else:
        print("❌ Document does not exist. Data saving failed.")
        return False

if __name__ == "__main__":
    verify_data()
