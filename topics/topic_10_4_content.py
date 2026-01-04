# Topic 10.4: The p-Value
import streamlit as st
from utils.localization import t
from utils.layouts.foundation import grey_info

def render_subtopic_10_4(model):
    """10.4 Der p-Wert"""
    
    st.header(t({"de": "10.4 Der p-Wert", "en": "10.4 The p-Value"}))
    st.markdown("---")
    
    # --- THEORY PLACEHOLDER ---
    with st.container(border=True):
        st.markdown(f"### {t({'de': 'Theorie', 'en': 'Theory'})}")
        grey_info(t({
            "de": "**Theorie-Inhalte kommen bald!**\n\nDieser Abschnitt wird theoretische Erklärungen enthalten:\n\n• Definition des p-Werts\n• Interpretation\n• Entscheidungsregel",
            "en": "**Theory content coming soon!**\n\nThis section will contain theoretical explanations:\n\n• Definition of p-value\n• Interpretation\n• Decision rule"
        }))
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- EXAM SECTION ---
    st.markdown(f"### {t({'de': 'Prüfungstraining', 'en': 'Exam Practice'})}")
    
    with st.container(border=True):
        grey_info(t({
            "de": "Für diesen Abschnitt gibt es derzeit keine MCQ-Fragen.",
            "en": "This section currently has no MCQ questions."
        }))
