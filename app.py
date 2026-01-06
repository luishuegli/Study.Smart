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

# --- 1. ATOMIC HYDRATION (The "Shield") ---
# We must capture URL params BEFORE any auth logic triggers a rerun.
# This ensures that when st.rerun() happens, the session state is already populated
# and preserved, preventing the app from falling back to default "dashboard".
if "session_hydrated" not in st.session_state:
    # Aggressively Hydrate from URL -> Session State
    st.session_state.current_page = st.query_params.get("page", "dashboard")
    st.session_state.selected_course = st.query_params.get("course", "vwl")
    st.session_state.selected_topic = st.query_params.get("topic")
    st.session_state.selected_subtopic = st.query_params.get("subtopic")
    
    # Mark as hydrated so we don't overwrite user actions later
    st.session_state.session_hydrated = True

# --- AUTHENTICATION (Tri-State Logic) ---
# Cookie manager for session persistence
cookie_manager = stx.CookieManager(key="study_smart_auth")

# 1. Initialize Auth State
if "auth_status" not in st.session_state:
    st.session_state.auth_status = "unknown"

# 2. Check for User Session (Immediate Login)
if "user" in st.session_state:
    st.session_state.auth_status = "logged_in"

# 3. State Machine
# STATE: UNKNOWN (Default) -> Show Spinner, Check Cookie
if st.session_state.auth_status == "unknown":
    # Show loading spinner
    loading_placeholder = st.empty()
    loading_placeholder.markdown("""
    <div style="display: flex; justify-content: center; align-items: center; height: 80vh;">
        <div style="text-align: center; color: #6B7280;">
            <div style="font-size: 1.1rem; margin-bottom: 8px;">Loading Study.Smart...</div>
            <div style="width: 24px; height: 24px; border: 3px solid #e5e7eb; border-top: 3px solid #1f2937; border-radius: 50%; animation: spin 1s linear infinite; margin: 0 auto;"></div>
        </div>
    </div>
    <style>@keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }</style>
    """, unsafe_allow_html=True)
    
    # Check Cookie
    # NOTE: stx.CookieManager is ASYNC. It needs a moment to load from the frontend.
    # We use a retry mechanism to wait for the cookie to arrive.
    saved_token = cookie_manager.get("token")
    
    # Initialize retry counter
    if "cookie_retries" not in st.session_state:
        st.session_state.cookie_retries = 0

    if saved_token:
        # Token found! Reset retries and verify.
        try:
            from firebase_config import get_account_info
            account_info = get_account_info(saved_token)
            if account_info and "users" in account_info and len(account_info["users"]) > 0:
                user_data = account_info["users"][0]
                st.session_state["user"] = {
                    "localId": user_data.get("localId"),
                    "email": user_data.get("email"),
                    "displayName": user_data.get("displayName"),
                    "idToken": saved_token
                }
                st.session_state.auth_status = "logged_in"
                loading_placeholder.empty()
                st.rerun()
            else:
                 st.session_state.auth_status = "logged_out"
                 loading_placeholder.empty()
                 st.rerun()
        except:
            st.session_state.auth_status = "logged_out"
            loading_placeholder.empty()
            st.rerun()
    else:
        # No token found yet.
        # Check if we should wait (maybe it's loading?)
        if st.session_state.cookie_retries < 5:
            st.session_state.cookie_retries += 1
            import time
            time.sleep(0.2) # Wait for frontend to load cookies
            st.rerun()
        else:
            # We waited, still nothing. Assume truly logged out.
            st.session_state.auth_status = "logged_out"
            loading_placeholder.empty()
            st.rerun()

# STATE: LOGGED_OUT -> Show Login Form
elif st.session_state.auth_status == "logged_out":
    render_auth(cookie_manager=cookie_manager)
    st.stop()

# STATE: LOGGED_IN -> Fall through to App (Main)


def main():
    # --- QUERY PARAM SYNC (PERSISTENCE) ---
    # 2. Sync FROM Session State to URL (always, for URL bar consistency)
    # At this point, session state is the SOURCE OF TRUTH (set by hydration or user action)
    
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

