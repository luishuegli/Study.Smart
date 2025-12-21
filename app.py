import streamlit as st
import course_config as config
from views.dashboard import dashboard_view
from views.course_overview import course_overview_view
from views.lesson import lesson_view
from views import dashboard, lesson
from views.auth import render_auth
from views.styles import load_css
from firebase_config import initialize_firebase_admin, get_firebase_analytics_script
from dotenv import load_dotenv
import os

# Initialize Firebase
initialize_firebase_admin()

# Configure page settings
st.set_page_config(
    page_title="VWL Statistik",
    page_icon="tao.png",
    layout="centered",
    initial_sidebar_state="expanded", # User requested sidebar back
)

# Inject Global Styles
load_css()

# Inject Firebase Analytics
st.markdown(get_firebase_analytics_script(), unsafe_allow_html=True)

# Authentication Flow
# Authentication Flow (DISABLED FOR DEV)
if "user" not in st.session_state:
    # render_auth()
    # st.stop()
    st.session_state["user"] = {"email": "dev@example.com", "localId": "dev_user"}

# Logout Button (Sidebar)
with st.sidebar:
    if st.button("Abmelden", type="secondary"):
        del st.session_state["user"]
        st.rerun()

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
