
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
