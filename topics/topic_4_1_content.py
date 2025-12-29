# Topic 4.1: Uniform Distribution (Discrete)
import streamlit as st
from utils.localization import t

def render_subtopic_4_1(model):
    """4.1 Gleichförmige Verteilung (diskret) - Uniform Distribution (discrete)"""
    
    st.header(t({"de": "4.1 Gleichförmige Verteilung (diskret)", "en": "4.1 Uniform Distribution (Discrete)"}))
    st.markdown("---")
    
    # --- THEORY PLACEHOLDER ---
    with st.container(border=True):
        st.markdown(f"### {t({'de': 'Theorie', 'en': 'Theory'})}")
        st.info(t({
            "de": "**Theorie-Inhalte kommen bald!**\n\nDieser Abschnitt wird theoretische Erklärungen zur diskreten Gleichverteilung enthalten.",
            "en": "**Theory content coming soon!**\n\nThis section will contain theoretical explanations of the discrete uniform distribution."
        }))
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- EXAM SECTION ---
    st.markdown(f"### {t({'de': 'Prüfungstraining', 'en': 'Exam Practice'})}")
    
    with st.container(border=True):
        st.info(t({
            "de": "Für diesen Abschnitt gibt es derzeit keine MCQ-Fragen. Diese werden in einem zukünftigen Update hinzugefügt.",
            "en": "This section currently has no MCQ questions. These will be added in a future update."
        }))
