# Topic 3.4: Expected Values
import streamlit as st
from utils.localization import t

def render_subtopic_3_4(model):
    """3.4 Erwartungswerte - Expected Values"""
    
    st.header(t({"de": "3.4 Erwartungswerte von Zufallsvariablen", "en": "3.4 Expected Values of Random Variables"}))
    st.markdown("---")
    
    # --- THEORY PLACEHOLDER ---
    with st.container(border=True):
        st.markdown(f"### {t({'de': 'Theorie', 'en': 'Theory'})}")
        st.info(t({
            "de": "**Theorie-Inhalte kommen bald!**\n\nDieser Abschnitt wird theoretische Erklärungen zu Erwartungswerten enthalten.",
            "en": "**Theory content coming soon!**\n\nThis section will contain theoretical explanations of expected values."
        }))
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- EXAM SECTION ---
    st.markdown(f"### {t({'de': 'Prüfungstraining', 'en': 'Exam Practice'})}")
    
    with st.container(border=True):
        st.info(t({
            "de": "Für diesen Abschnitt gibt es derzeit nur Langform-Übungsaufgaben (keine MCQs). Diese werden in einem zukünftigen Update hinzugefügt.",
            "en": "This section currently only has long-form practice problems (no MCQs). These will be added in a future update."
        }))
