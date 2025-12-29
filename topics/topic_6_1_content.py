# Topic 6.1: The Central Limit Theorem
import streamlit as st
from utils.localization import t

def render_subtopic_6_1(model):
    """6.1 Der zentrale Grenzwertsatz - The Central Limit Theorem"""
    
    st.header(t({"de": "6.1 Der zentrale Grenzwertsatz", "en": "6.1 The Central Limit Theorem"}))
    st.markdown("---")
    
    # --- THEORY PLACEHOLDER ---
    with st.container(border=True):
        st.markdown(f"### {t({'de': 'Theorie', 'en': 'Theory'})}")
        st.info(t({
            "de": "**Theorie-Inhalte kommen bald!**\n\nDieser Abschnitt wird theoretische Erklärungen zum zentralen Grenzwertsatz enthalten:\n\n• Definition und Voraussetzungen\n• Konvergenz der Summe von Zufallsvariablen\n• Die Standardnormalverteilung als Grenzverteilung",
            "en": "**Theory content coming soon!**\n\nThis section will contain theoretical explanations of the Central Limit Theorem:\n\n• Definition and prerequisites\n• Convergence of sums of random variables\n• The standard normal distribution as limiting distribution"
        }))
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- EXAM SECTION ---
    st.markdown(f"### {t({'de': 'Prüfungstraining', 'en': 'Exam Practice'})}")
    
    with st.container(border=True):
        st.info(t({
            "de": "Für diesen Abschnitt gibt es derzeit keine MCQ-Fragen. Diese werden in einem zukünftigen Update hinzugefügt.",
            "en": "This section currently has no MCQ questions. These will be added in a future update."
        }))
