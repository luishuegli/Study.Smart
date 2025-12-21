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

# Initialize Firebase
initialize_firebase_admin()

# Configure page settings
st.set_page_config(
    page_title="Study.Smart",
    page_icon="tao.png",
    layout="centered",
    initial_sidebar_state="expanded", # User requested sidebar back
)

# Initialize Language State
loc.init_lang()

# Inject Global Styles
load_design_system()

# Inject Firebase Analytics
st.markdown(get_firebase_analytics_script(), unsafe_allow_html=True)

# Authentication Flow with Persistence
import extra_streamlit_components as stx
cookie_manager = stx.CookieManager()

if "user" not in st.session_state:
    # Try to recover session from cookie
    try:
        cookies = cookie_manager.get_all()
        token = cookies.get("token")
        if token:
            from firebase_config import get_account_info
            user_info = get_account_info(token)
            if "users" in user_info:
                # Token valid
                user_data = user_info["users"][0]
                # Map Firebase user format to our session format
                st.session_state["user"] = {
                    "localId": user_data.get("localId"),
                    "email": user_data.get("email"),
                    "displayName": user_data.get("displayName"),
                    "idToken": token # Keep the token for future calls
                }
                st.rerun()
            else:
                # Token invalid/expired
                print("Token invalid or expired")
                # cookie_manager.delete("token") # deleting might require a key, safe to ignore for now
    except Exception as e:
        # If cookie manager fails or other error, fallback to auth
        print(f"Session recovery failed: {e}")

if "user" not in st.session_state:
    render_auth(cookie_manager=cookie_manager)
    st.stop()
    
# Load Env
load_dotenv()

def main():
    # Handle Query Params for Navigation (Clickable Cards)
    if "course" in st.query_params:
        course_id = st.query_params["course"]
        st.session_state.current_page = "course_overview"
        st.session_state.selected_course = course_id
        st.query_params.clear()
        st.rerun()

    # Initialize Session State
    if "current_page" not in st.session_state:
        st.session_state.current_page = "dashboard"
    
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
