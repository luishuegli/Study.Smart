
import streamlit as st

def load_css():
    """Injects global CSS for the application."""
    st.markdown("""<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
/* GLOBAL FONTS */
html, body, [class*="css"] {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
}

/* ROUNDED CORNERS GLOBAL */
.stButton > button {
    border-radius: 12px !important;
    border: 1px solid #e5e7eb !important;
    box-shadow: 0 1px 2px rgba(0,0,0,0.05) !important;
    transition: all 0.2s ease-in-out;
}

.stTextInput > div > div > input {
    border-radius: 10px !important;
}

div[data-baseweb="select"] > div {
    border-radius: 10px !important;
}

/* BUTTONS: White Secondary (Default) */
.stButton > button[kind="secondary"] {
    background-color: white !important;
    color: #1f2937 !important;
    transform: translateY(0);
}
.stButton > button[kind="secondary"]:hover {
    background-color: #f9fafb !important;
    border-color: #d1d5db !important;
    transform: translateY(-1px);
}

/* BUTTONS: Primary (Purple) */
.stButton > button[kind="primary"], 
.stButton > button[data-testid="baseButton-primary"] {
    background: linear-gradient(135deg, #6366f1 0%, #4f46e5 100%) !important;
    background-color: #6366f1 !important;
    color: white !important;
    border: none !important;
    box-shadow: 0 4px 6px -1px rgba(99, 102, 241, 0.3) !important;
}
.stButton > button[kind="primary"]:hover {
    opacity: 0.9 !important;
    transform: translateY(-1px);
    box-shadow: 0 6px 8px -1px rgba(99, 102, 241, 0.4) !important;
}

/* SUCCESS/INFO/WARNING BOXES ROUNDED */
.stAlert {
    border-radius: 12px !important;
}

/* THEORY BOX CUSTOM COMPONENT */
.theory-box {
    background: white;
    border: 2px solid #e5e7eb;
    border-radius: 16px;
    padding: 32px;
    margin: 24px 0;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
}
.theory-box-header {
    display: flex;
    align-items: center;
    gap: 16px;
    margin-bottom: 24px;
    padding-bottom: 16px;
    border-bottom: 2px solid #f3f4f6;
}
.theory-icon {
    width: 48px;
    height: 48px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: #ecfeff;
    border-radius: 12px;
    color: #0891b2;
}
.theory-title {
    font-size: 20px;
    font-weight: 700;
    color: #111827;
}
.theory-content {
    color: #4b5563;
    line-height: 1.6;
    font-size: 16px;
}
.experiment-badge {
    display: inline-block;
    background: #f0fdf4;
    color: #16a34a;
    padding: 6px 12px;
    border-radius: 100px;
    font-size: 12px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-top: 16px;
}

/* RADIO BUTTONS AS CARDS */
div[class*="stRadio"] > div[role="radiogroup"] > label {
    background-color: white;
    border: 1px solid #e5e7eb;
    border-radius: 12px !important;
    padding: 16px !important;
    margin-bottom: 8px !important;
    transition: all 0.2s;
}
div[class*="stRadio"] > div[role="radiogroup"] > label:hover {
    background-color: #f9fafb;
    border-color: #6366f1;
}

/* SIDEBAR NAVIGATION */
section[data-testid="stSidebar"] .stButton > button {
    width: 100%;
    justify-content: flex-start;
    text-align: left;
    border: none !important;
    background: transparent !important;
    box-shadow: none !important;
}
section[data-testid="stSidebar"] .stButton > button:hover {
    background: #f3f4f6 !important;
}

/* AUTH STYLES */
.auth-header {
    text-align: center;
    color: #0f172a;
    margin-bottom: 2rem;
}
</style>""", unsafe_allow_html=True)
