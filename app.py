import streamlit as st
import course_config as config
from views.dashboard import dashboard_view
from views.course_overview import course_overview_view
from views.lesson import lesson_view
from views import dashboard, lesson
from firebase_config import initialize_firebase_admin, get_firebase_analytics_script
from dotenv import load_dotenv
import os

# Initialize Firebase
initialize_firebase_admin()

# Configure page settings
st.set_page_config(
    page_title="VWL Statistik",
    page_icon="tao.png",
    layout="wide",
    initial_sidebar_state="expanded", # User requested sidebar back
)

# Inject Firebase Analytics
st.markdown(get_firebase_analytics_script(), unsafe_allow_html=True)

# Load Env
load_dotenv()

# Custom CSS
st.markdown("""
<style>
    /* Global Theme Overrides */
    .stApp {
        background-color: #f7f9fc;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }
    
    /* Text Colors */
    h1, h2, h3 {
        color: #0f172a;
        font-weight: 700;
    }
    p, li, .stMarkdown {
        color: #475569;
    }
    
    /* "Brilliant" Button Styling */
    div.stButton > button {
        background: linear-gradient(135deg, #6366f1 0%, #4f46e5 100%);
        color: white;
        border: none;
        padding: 0.5rem 1.5rem;
        border-radius: 9999px;
        font-weight: 600;
        box-shadow: 0 4px 6px -1px rgba(79, 70, 229, 0.3);
        transition: all 0.2s ease;
    }
    div.stButton > button:hover {
        transform: scale(1.05);
        box-shadow: 0 10px 15px -3px rgba(79, 70, 229, 0.4);
        background: linear-gradient(135deg, #4f46e5 0%, #4338ca 100%);
        color: white;
        border: none;
    }
    
    /* Metric Styling */
    div[data-testid="stMetricValue"] {
        color: #0f172a;
        font-weight: 700;
    }
    
    /* Remove top padding */
    .block-container {
        padding-top: 2rem;
    }
</style>
""", unsafe_allow_html=True)

def main():
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
