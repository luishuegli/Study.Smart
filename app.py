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

# --- Theme Toggle ---
# Check if the theme is already set in the session state, default to 'light'
if "theme" not in st.session_state:
    st.session_state.theme = "light"

# Create a toggle button in the sidebar. The value is determined by the current theme.
# The label changes based on the theme to be more descriptive.
toggle_label = "Switch to Dark Mode" if st.session_state.theme == "light" else "Switch to Light Mode"
is_dark_mode = st.sidebar.toggle(toggle_label, value=(st.session_state.theme == "dark"))

# Update the theme in the session state based on the toggle's status
new_theme = "dark" if is_dark_mode else "light"

# If the theme has changed, update the session state and rerun the app to apply the new theme
if st.session_state.theme != new_theme:
    st.session_state.theme = new_theme
    st.rerun()

# Inject Global Styles
load_design_system()

# Inject Firebase Analytics
st.markdown(get_firebase_analytics_script(), unsafe_allow_html=True)

# Authentication Flow with Persistence
# import extra_streamlit_components as stx
# cookie_manager = stx.CookieManager(key="main_auth_cookies")

if "user" not in st.session_state:
    # Bypass Auth for testing
    st.session_state["user"] = {
        "localId": "test_user_id",
        "email": "test@example.com",
        "displayName": "Test User",
        "idToken": "dummy_token"
    }

# if "user" not in st.session_state:
#     render_auth(cookie_manager=cookie_manager)
#     st.stop()
    
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
