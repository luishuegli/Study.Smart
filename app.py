import streamlit as st
import course_config as config
from views.dashboard import dashboard_view
from views.course_overview import course_overview_view
from views.lesson import lesson_view
from views.auth import render_auth
from views.styles import load_design_system
from firebase_config import initialize_firebase_admin, get_firebase_analytics_script
from dotenv import load_dotenv
import os
import utils.localization as loc
import extra_streamlit_components as stx

# Load Env first (for Firebase config)
load_dotenv()

# Initialize Firebase
initialize_firebase_admin()

# Configure page settings
st.set_page_config(
    page_title="Study.Smart",
    page_icon="tao.png",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Initialize Language State
loc.init_lang()

# Inject Global Styles
load_design_system()

# Inject Firebase Analytics
st.markdown(get_firebase_analytics_script(), unsafe_allow_html=True)

# --- PRESERVE NAVIGATION STATE BEFORE AUTH (Critical for refresh persistence) ---
# Read query params into session state BEFORE auth check
# This ensures navigation survives the auth rerun cycle
if "current_page" not in st.session_state:
    st.session_state.current_page = st.query_params.get("page", "dashboard")
if "selected_course" not in st.session_state:
    st.session_state.selected_course = st.query_params.get("course", "vwl")
if "selected_topic" not in st.session_state:
    st.session_state.selected_topic = st.query_params.get("topic")
if "selected_subtopic" not in st.session_state:
    st.session_state.selected_subtopic = st.query_params.get("subtopic")

# --- AUTHENTICATION ---
# Cookie manager for session persistence (cannot be cached - it's a widget)
cookie_manager = stx.CookieManager(key="study_smart_auth")

# Check for existing session or restore from cookie
if "user" not in st.session_state:
    # Try to restore session from cookie
    saved_token = cookie_manager.get("token")
    
    if saved_token:
        # Show loading placeholder instead of login (prevents flash)
        st.markdown("""
        <div style="display: flex; justify-content: center; align-items: center; height: 80vh;">
            <div style="text-align: center; color: #6B7280;">
                <div style="font-size: 1.1rem; margin-bottom: 8px;">Loading...</div>
                <div style="width: 24px; height: 24px; border: 3px solid #e5e7eb; border-top: 3px solid #1f2937; border-radius: 50%; animation: spin 1s linear infinite; margin: 0 auto;"></div>
            </div>
        </div>
        <style>
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        </style>
        """, unsafe_allow_html=True)
        
        # Verify token and restore session
        from firebase_config import get_account_info
        auth_success = False
        try:
            account_info = get_account_info(saved_token)
            if account_info and "users" in account_info and len(account_info["users"]) > 0:
                user_data = account_info["users"][0]
                # Reconstruct user session
                st.session_state["user"] = {
                    "localId": user_data.get("localId"),
                    "email": user_data.get("email"),
                    "displayName": user_data.get("displayName"),
                    "idToken": saved_token  # Keep the token for API calls
                }
                auth_success = True
                st.rerun()  # Rerun to proceed with authenticated state
        except Exception as e:
            # Token invalid or expired
            auth_success = False
        
        # If auth failed, show login (don't stay stuck on loading)
        if not auth_success:
            render_auth(cookie_manager=cookie_manager)
            st.stop()
    else:
        # No token - show login immediately
        render_auth(cookie_manager=cookie_manager)
        st.stop()


def main():
    # --- QUERY PARAM SYNC (PERSISTENCE) ---
    # 1. On FIRST LOAD (session state is empty), read from URL
    # This ensures refresh restores the last location, but button clicks are not overwritten.
    
    if "current_page" not in st.session_state:
        if "page" in st.query_params:
            st.session_state.current_page = st.query_params["page"]
        else:
            st.session_state.current_page = "dashboard"
    
    if "selected_course" not in st.session_state:
        if "course" in st.query_params:
            st.session_state.selected_course = st.query_params["course"]
        else:
            st.session_state.selected_course = "vwl"
    
    # Topic and subtopic: only load from URL if not already set
    if "selected_topic" not in st.session_state and "topic" in st.query_params:
        st.session_state.selected_topic = st.query_params["topic"]
    
    if "selected_subtopic" not in st.session_state and "subtopic" in st.query_params:
        st.session_state.selected_subtopic = st.query_params["subtopic"]

    # 2. Sync FROM Session State to URL (always, for URL bar consistency)
    st.query_params.page = st.session_state.current_page
    st.query_params.course = st.session_state.selected_course
    
    if st.session_state.get("selected_topic"):
        st.query_params.topic = st.session_state.selected_topic
    else:
        if "topic" in st.query_params:
            del st.query_params.topic
            
    if st.session_state.get("selected_subtopic"):
        st.query_params.subtopic = st.session_state.selected_subtopic
    else:
        if "subtopic" in st.query_params:
            del st.query_params.subtopic

    # Router
    if st.session_state.current_page == "dashboard":
        dashboard_view()
    elif st.session_state.current_page == "course_overview":
        course_overview_view()
    elif st.session_state.current_page == "lesson":
        lesson_view()
    else:
        st.error("Page not found")
        if st.button("Go Home"):
            st.session_state.current_page = "dashboard"
            st.rerun()

if __name__ == "__main__":
    main()

