# Topic 7.5: Scatter Plot
import streamlit as st
from utils.localization import t

def render_subtopic_7_5(model):
    """7.5 Streudiagramm"""
    
    st.header(t({"de": "7.5 Streudiagramm", "en": "7.5 Scatter Plot"}))
    st.markdown("---")
    
    # --- THEORY PLACEHOLDER ---
    with st.container(border=True):
        st.markdown(f"### {t({'de': 'Theorie', 'en': 'Theory'})}")
        st.info(t({
            "de": "**Theorie-Inhalte kommen bald!**\n\nDieser Abschnitt wird theoretische Erklärungen enthalten:\n\n• Darstellung von Zusammenhängen\n• Korrelation visualisieren\n• Lineare Regression",
            "en": "**Theory content coming soon!**\n\nThis section will contain theoretical explanations:\n\n• Representing relationships\n• Visualizing correlation\n• Linear regression"
        }))
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- EXAM SECTION ---
    st.markdown(f"### {t({'de': 'Prüfungstraining', 'en': 'Exam Practice'})}")
    
    with st.container(border=True):
        st.info(t({
            "de": "Für diesen Abschnitt gibt es derzeit keine MCQ-Fragen.",
            "en": "This section currently has no MCQ questions."
        }))
