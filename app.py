import streamlit as st
import course_config as config
from views.dashboard import dashboard_view
from views.course_overview import course_overview_view
from views.lesson import lesson_view
from views import dashboard, lesson
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

# --- AUTHENTICATION ---
# Cookie manager for session persistence (cannot be cached - it's a widget)
cookie_manager = stx.CookieManager(key="study_smart_auth")

# CRITICAL: Capture URL params BEFORE auth check to preserve deep links on refresh
# These get lost if we redirect to login then back to dashboard
_preserved_page = st.query_params.get("page")
_preserved_course = st.query_params.get("course")
_preserved_topic = st.query_params.get("topic")
_preserved_subtopic = st.query_params.get("subtopic")

# Check for existing session or restore from cookie
if "user" not in st.session_state:
    # Try to restore session from cookie
    saved_token = cookie_manager.get("token")
    
    if saved_token:
        # Show loading state while verifying token (prevents flash of login form)
        with st.spinner(loc.t({"de": "Session wird wiederhergestellt...", "en": "Restoring session..."})):
            from firebase_config import get_account_info
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
                    
                    # Restore preserved URL params to session state BEFORE rerun
                    if _preserved_page:
                        st.session_state.current_page = _preserved_page
                    if _preserved_course:
                        st.session_state.selected_course = _preserved_course
                    if _preserved_topic:
                        st.session_state.selected_topic = _preserved_topic
                    if _preserved_subtopic:
                        st.session_state.selected_subtopic = _preserved_subtopic
                    
                    st.rerun()  # Rerun to proceed with authenticated state
            except Exception as e:
                # Token invalid or expired, continue to login
                pass
    
    # No valid session, show login (only reached if no token or token invalid)
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

