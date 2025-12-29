# Topic 7.1: Frequency Distribution, Histogram and Distribution Function
import streamlit as st
from utils.localization import t
from utils.quiz_helper import render_mcq
from data.exam_questions import get_question

def render_subtopic_7_1(model):
    """7.1 Häufigkeitsverteilung, Histogramm und Verteilungsfunktion"""
    
    st.header(t({"de": "7.1 Häufigkeitsverteilung, Histogramm und Verteilungsfunktion", "en": "7.1 Frequency Distribution, Histogram and Distribution Function"}))
    st.markdown("---")
    
    # --- THEORY PLACEHOLDER ---
    with st.container(border=True):
        st.markdown(f"### {t({'de': 'Theorie', 'en': 'Theory'})}")
        st.info(t({
            "de": "**Theorie-Inhalte kommen bald!**\n\nDieser Abschnitt wird theoretische Erklärungen enthalten:\n\n• Absolute und relative Häufigkeit\n• Histogramme\n• Empirische Verteilungsfunktion",
            "en": "**Theory content coming soon!**\n\nThis section will contain theoretical explanations:\n\n• Absolute and relative frequency\n• Histograms\n• Empirical distribution function"
        }))
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- EXAM SECTION ---
    st.markdown(f"### {t({'de': 'Prüfungstraining', 'en': 'Exam Practice'})}")
    
    with st.container(border=True):
        st.info(t({
            "de": "Für diesen Abschnitt gibt es derzeit keine MCQ-Fragen.",
            "en": "This section currently has no MCQ questions."
        }))
