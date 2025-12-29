# Topic 4.2: Bernoulli Distribution
import streamlit as st
from utils.localization import t

def render_subtopic_4_2(model):
    """4.2 Bernoulli-Verteilung - Bernoulli Distribution"""
    
    st.header(t({"de": "4.2 Bernoulli-Verteilung (diskret)", "en": "4.2 Bernoulli Distribution (Discrete)"}))
    st.markdown("---")
    
    # --- THEORY PLACEHOLDER ---
    with st.container(border=True):
        st.markdown(f"### {t({'de': 'Theorie', 'en': 'Theory'})}")
        st.info(t({
            "de": "**Theorie-Inhalte kommen bald!**\n\nDieser Abschnitt wird theoretische Erklärungen zur Bernoulli-Verteilung enthalten.",
            "en": "**Theory content coming soon!**\n\nThis section will contain theoretical explanations of the Bernoulli distribution."
        }))
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- EXAM SECTION ---
    st.markdown(f"### {t({'de': 'Prüfungstraining', 'en': 'Exam Practice'})}")
    
    with st.container(border=True):
        st.info(t({
            "de": "Für diesen Abschnitt gibt es derzeit nur Langform-Übungsaufgaben (keine MCQs). Diese werden in einem zukünftigen Update hinzugefügt.",
            "en": "This section currently only has long-form practice problems (no MCQs). These will be added in a future update."
        }))
