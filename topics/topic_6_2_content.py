# Topic 6.2: Applications of the Central Limit Theorem
import streamlit as st
from utils.localization import t

def render_subtopic_6_2(model):
    """6.2 Anwendungen des CLT - Applications of the CLT"""
    
    st.header(t({"de": "6.2 Anwendungen des CLT", "en": "6.2 Applications of the CLT"}))
    st.markdown("---")
    
    # --- THEORY PLACEHOLDER ---
    with st.container(border=True):
        st.markdown(f"### {t({'de': 'Theorie', 'en': 'Theory'})}")
        st.info(t({
            "de": "**Theorie-Inhalte kommen bald!**\n\nDieser Abschnitt wird praktische Anwendungen des CLT behandeln:\n\n• Normalapproximation der Binomialverteilung\n• Approximation von Stichprobenmitteln\n• Konfidenzintervalle",
            "en": "**Theory content coming soon!**\n\nThis section will cover practical applications of the CLT:\n\n• Normal approximation of the binomial distribution\n• Approximation of sample means\n• Confidence intervals"
        }))
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- EXAM SECTION ---
    st.markdown(f"### {t({'de': 'Prüfungstraining', 'en': 'Exam Practice'})}")
    
    with st.container(border=True):
        st.info(t({
            "de": "Für diesen Abschnitt gibt es derzeit keine MCQ-Fragen. Diese werden in einem zukünftigen Update hinzugefügt.",
            "en": "This section currently has no MCQ questions. These will be added in a future update."
        }))
