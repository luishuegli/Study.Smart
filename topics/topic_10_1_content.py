# Topic 10.1: Types of Hypotheses
import streamlit as st
from utils.localization import t

def render_subtopic_10_1(model):
    """10.1 Arten von Hypothesen"""
    
    st.header(t({"de": "10.1 Arten von Hypothesen", "en": "10.1 Types of Hypotheses"}))
    st.markdown("---")
    
    # --- THEORY PLACEHOLDER ---
    with st.container(border=True):
        st.markdown(f"### {t({'de': 'Theorie', 'en': 'Theory'})}")
        st.info(t({
            "de": "**Theorie-Inhalte kommen bald!**\n\nDieser Abschnitt wird theoretische Erklärungen enthalten:\n\n• Nullhypothese $H_0$\n• Alternativhypothese $H_1$\n• Einseitige vs. zweiseitige Tests",
            "en": "**Theory content coming soon!**\n\nThis section will contain theoretical explanations:\n\n• Null hypothesis $H_0$\n• Alternative hypothesis $H_1$\n• One-sided vs. two-sided tests"
        }))
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- EXAM SECTION ---
    st.markdown(f"### {t({'de': 'Prüfungstraining', 'en': 'Exam Practice'})}")
    
    with st.container(border=True):
        st.info(t({
            "de": "Für diesen Abschnitt gibt es derzeit keine MCQ-Fragen.",
            "en": "This section currently has no MCQ questions."
        }))
