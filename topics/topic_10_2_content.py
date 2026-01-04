# Topic 10.2: Critical Region and Test Statistics
import streamlit as st
from utils.localization import t
from utils.layouts.foundation import grey_info

def render_subtopic_10_2(model):
    """10.2 Kritischer Bereich und Teststatistik"""
    
    st.header(t({"de": "10.2 Kritischer Bereich und Teststatistik", "en": "10.2 Critical Region and Test Statistics"}))
    st.markdown("---")
    
    # --- THEORY PLACEHOLDER ---
    with st.container(border=True):
        st.markdown(f"### {t({'de': 'Theorie', 'en': 'Theory'})}")
        grey_info(t({
            "de": "**Theorie-Inhalte kommen bald!**\n\nDieser Abschnitt wird theoretische Erklärungen enthalten:\n\n• Teststatistik\n• Kritischer Bereich\n• Ablehnungsbereich",
            "en": "**Theory content coming soon!**\n\nThis section will contain theoretical explanations:\n\n• Test statistic\n• Critical region\n• Rejection region"
        }))
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- EXAM SECTION ---
    st.markdown(f"### {t({'de': 'Prüfungstraining', 'en': 'Exam Practice'})}")
    
    with st.container(border=True):
        grey_info(t({
            "de": "Für diesen Abschnitt gibt es derzeit keine MCQ-Fragen.",
            "en": "This section currently has no MCQ questions."
        }))
