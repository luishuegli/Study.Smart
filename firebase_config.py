
import firebase_admin
from firebase_admin import credentials
import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def initialize_firebase_admin():
    """Initializes the Firebase Admin SDK.
    
    Supports two modes:
    1. Local development: Uses serviceAccountKey.json file
    2. Streamlit Cloud: Uses st.secrets["FIREBASE_SERVICE_ACCOUNT"]
    """
    # Check if already initialized to avoid errors on rerun
    if not firebase_admin._apps:
        cred = None
        
        # Try 1: Load from Streamlit Secrets (for Cloud deployment)
        try:
            if "FIREBASE_SERVICE_ACCOUNT" in st.secrets:
                service_account_info = dict(st.secrets["FIREBASE_SERVICE_ACCOUNT"])
                cred = credentials.Certificate(service_account_info)
                print("Firebase Admin initialized from Streamlit Secrets.")
        except Exception as e:
            print(f"Could not load from Streamlit Secrets: {e}")
        
        # Try 2: Load from local file (for development)
        if cred is None:
            cred_path = "serviceAccountKey.json"
            if os.path.exists(cred_path):
                try:
                    cred = credentials.Certificate(cred_path)
                    print("Firebase Admin initialized from local file.")
                except Exception as e:
                    print(f"Error loading from file: {e}")
            else:
                print(f"Warning: {cred_path} not found and no Streamlit Secrets. Firebase Admin not initialized.")
        
        # Initialize if we have credentials
        if cred:
            try:
                firebase_admin.initialize_app(cred)
            except Exception as e:
                print(f"Error initializing Firebase Admin: {e}")

def get_firebase_analytics_script():
    """Returns the HTML script for Firebase Analytics."""
    # Values fetched from environment variables
    api_key = os.getenv("FIREBASE_API_KEY")
    auth_domain = os.getenv("FIREBASE_AUTH_DOMAIN")
    project_id = os.getenv("FIREBASE_PROJECT_ID")
    storage_bucket = os.getenv("FIREBASE_STORAGE_BUCKET")
    sender_id = os.getenv("FIREBASE_MESSAGING_SENDER_ID")
    app_id = os.getenv("FIREBASE_APP_ID")
    measurement_id = os.getenv("FIREBASE_MEASUREMENT_ID")

    return f"""
    <script type="module">
      import {{ initializeApp }} from "https://www.gstatic.com/firebasejs/10.7.1/firebase-app.js";
      import {{ getAnalytics }} from "https://www.gstatic.com/firebasejs/10.7.1/firebase-analytics.js";

      const firebaseConfig = {{
        apiKey: "{api_key}",
        authDomain: "{auth_domain}",
        projectId: "{project_id}",
        storageBucket: "{storage_bucket}",
        messagingSenderId: "{sender_id}",
        appId: "{app_id}",
        measurementId: "{measurement_id}"
      }};

      // Initialize Firebase
      const app = initializeApp(firebaseConfig);
      const analytics = getAnalytics(app);
      console.log("Firebase Analytics initialized");
    </script>
    """

import requests
import json

# Firebase Web API Key
FIREBASE_WEB_API_KEY = os.getenv("FIREBASE_API_KEY")

def sign_in_user(email, password):
    """Signs in a user using Firebase REST API."""
    request_url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={FIREBASE_WEB_API_KEY}"
    payload = {
        "email": email,
        "password": password,
        "returnSecureToken": True
    }
    try:
        response = requests.post(request_url, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        error_json = e.response.json()
        error_message = error_json.get("error", {}).get("message", "Unknown error")
        return {"error": error_message}
    except Exception as e:
        return {"error": str(e)}

def sign_up_user(email, password):
    """Signs up a new user using Firebase REST API."""
    request_url = f"https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={FIREBASE_WEB_API_KEY}"
    payload = {
        "email": email,
        "password": password,
        "returnSecureToken": True
    }
    try:
        response = requests.post(request_url, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        error_json = e.response.json()
        error_message = error_json.get("error", {}).get("message", "Unknown error")
        return {"error": error_message}
    except Exception as e:
        return {"error": str(e)}

def update_user_profile(id_token, display_name=None, photo_url=None):
    """Updates user profile (displayName, photoUrl) using Firebase REST API."""
    request_url = f"https://identitytoolkit.googleapis.com/v1/accounts:update?key={FIREBASE_WEB_API_KEY}"
    payload = {
        "idToken": id_token,
        "returnSecureToken": True
    }
    if display_name:
        payload["displayName"] = display_name
    if photo_url:
        payload["photoUrl"] = photo_url
        
    try:
        response = requests.post(request_url, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        error_json = e.response.json()
        error_message = error_json.get("error", {}).get("message", "Unknown error")
        return {"error": error_message}
    except Exception as e:
        return {"error": str(e)}

def save_progress(user_id, course_id, progress_data):
    """
    Saves user progress to Firestore (Admin SDK).
    Structure: users/{user_id}/{course_id}/progress
    """
    try:
        db = firebase_admin.firestore.client()
        # Create/Update document in users collection
        # We store progress in a map under the course_id
        user_ref = db.collection("users").document(user_id)
        user_ref.set({
            "progress": {
                course_id: progress_data
            }
        }, merge=True)
        return True
    except Exception as e:
        print(f"Error saving progress: {e}")
        return False

def load_progress(user_id):
    """
    Loads user progress from Firestore.
    Returns a dictionary of progress data or empty dict.
    """
    try:
        db = firebase_admin.firestore.client()
        user_ref = db.collection("users").document(user_id)
        doc = user_ref.get()
        if doc.exists:
            data = doc.to_dict()
            return data.get("progress", {})
        return {}
    except Exception as e:
        print(f"Error loading progress: {e}")
        return {}

def get_account_info(id_token):
    """
    Get user info using ID token to verify session.
    """
    rest_api_url = f"https://identitytoolkit.googleapis.com/v1/accounts:lookup?key={FIREBASE_WEB_API_KEY}"
    payload = {
        "idToken": id_token
    }
    try:
        response = requests.post(rest_api_url, json=payload)
        return response.json()
    except Exception as e:
        print(f"Error verifying token: {e}")
        return {}
