
import firebase_admin
from firebase_admin import credentials
import streamlit as st
import os

def initialize_firebase_admin():
    """Initializes the Firebase Admin SDK."""
    # Check if already initialized to avoid errors on rerun
    if not firebase_admin._apps:
        # Load credentials from the service account key file
        # USER MUST PROVIDE THIS FILE
        cred_path = "serviceAccountKey.json"
        
        if os.path.exists(cred_path):
            try:
                cred = credentials.Certificate(cred_path)
                firebase_admin.initialize_app(cred)
                print("Firebase Admin initialized successfully.")
            except Exception as e:
                print(f"Error initializing Firebase Admin: {e}")
        else:
            print(f"Warning: {cred_path} not found. Firebase Admin not initialized.")

def get_firebase_analytics_script():
    """Returns the HTML script for Firebase Analytics."""
    # This config matches the one provided by the user
    return """
    <script type="module">
      import { initializeApp } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-app.js";
      import { getAnalytics } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-analytics.js";

      const firebaseConfig = {
        apiKey: "AIzaSyBzKUmu5uNFzz1h0J7wrW0iy-zVkJ8yfiY",
        authDomain: "study-smart-a0cbf.firebaseapp.com",
        projectId: "study-smart-a0cbf",
        storageBucket: "study-smart-a0cbf.firebasestorage.app",
        messagingSenderId: "505742105384",
        appId: "1:505742105384:web:f7da31c53348233bd94e1d",
        measurementId: "G-836JT7D6N7"
      };

      // Initialize Firebase
      const app = initializeApp(firebaseConfig);
      const analytics = getAnalytics(app);
      console.log("Firebase Analytics initialized");
    </script>
    """

import requests
import json

# Firebase Web API Key (from your config snippet)
FIREBASE_WEB_API_KEY = "AIzaSyBzKUmu5uNFzz1h0J7wrW0iy-zVkJ8yfiY"

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
