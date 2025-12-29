# Topic 7.3: Box Plot
import streamlit as st
from utils.localization import t

def render_subtopic_7_3(model):
    """7.3 Boxplot"""
    
    st.header(t({"de": "7.3 Boxplot", "en": "7.3 Box Plot"}))
    st.markdown("---")
    
    # --- THEORY PLACEHOLDER ---
    with st.container(border=True):
        st.markdown(f"### {t({'de': 'Theorie', 'en': 'Theory'})}")
        st.info(t({
            "de": "**Theorie-Inhalte kommen bald!**\n\nDieser Abschnitt wird theoretische Erklärungen enthalten:\n\n• Quartile und Interquartilsabstand\n• Whisker und Ausreisser\n• Interpretation von Boxplots",
            "en": "**Theory content coming soon!**\n\nThis section will contain theoretical explanations:\n\n• Quartiles and interquartile range\n• Whiskers and outliers\n• Interpreting box plots"
        }))
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- EXAM SECTION ---
    st.markdown(f"### {t({'de': 'Prüfungstraining', 'en': 'Exam Practice'})}")
    
    with st.container(border=True):
        st.info(t({
            "de": "Für diesen Abschnitt gibt es derzeit keine MCQ-Fragen.",
            "en": "This section currently has no MCQ questions."
        }))
