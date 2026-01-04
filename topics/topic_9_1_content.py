# Topic 9.1: Concept of the Confidence Interval
import streamlit as st
from utils.localization import t
from utils.layouts.foundation import grey_info

def render_subtopic_9_1(model):
    """9.1 Konzept des Konfidenzintervalls"""
    
    st.header(t({"de": "9.1 Konzept des Konfidenzintervalls", "en": "9.1 Concept of the Confidence Interval"}))
    st.markdown("---")
    
    # --- THEORY PLACEHOLDER ---
    with st.container(border=True):
        st.markdown(f"### {t({'de': 'Theorie', 'en': 'Theory'})}")
        grey_info(t({
            "de": "**Theorie-Inhalte kommen bald!**\n\nDieser Abschnitt wird theoretische Erklärungen enthalten:\n\n• Definition des Konfidenzintervalls\n• Konfidenzniveau\n• Interpretation",
            "en": "**Theory content coming soon!**\n\nThis section will contain theoretical explanations:\n\n• Definition of confidence interval\n• Confidence level\n• Interpretation"
        }))
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- EXAM SECTION ---
    st.markdown(f"### {t({'de': 'Prüfungstraining', 'en': 'Exam Practice'})}")
    
    with st.container(border=True):
        grey_info(t({
            "de": "Für diesen Abschnitt gibt es derzeit keine MCQ-Fragen.",
            "en": "This section currently has no MCQ questions."
        }))
