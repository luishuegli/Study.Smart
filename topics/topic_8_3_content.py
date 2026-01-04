# Topic 8.3: Methods for Constructing Estimating Functions
import streamlit as st
from utils.localization import t
from utils.layouts.foundation import grey_info
from utils.quiz_helper import render_mcq
from data.exam_questions import get_question

def render_subtopic_8_3(model):
    """8.3 Methoden zur Konstruktion von Schätzfunktionen"""
    
    st.header(t({"de": "8.3 Methoden zur Konstruktion von Schätzfunktionen", "en": "8.3 Methods for Constructing Estimating Functions"}))
    st.markdown("---")
    
    # --- THEORY PLACEHOLDER ---
    with st.container(border=True):
        st.markdown(f"### {t({'de': 'Theorie', 'en': 'Theory'})}")
        grey_info(t({
            "de": "**Theorie-Inhalte kommen bald!**\n\nDieser Abschnitt wird theoretische Erklärungen enthalten:\n\n• Maximum-Likelihood-Methode\n• Likelihood-Funktion\n• Log-Likelihood",
            "en": "**Theory content coming soon!**\n\nThis section will contain theoretical explanations:\n\n• Maximum Likelihood Method\n• Likelihood Function\n• Log-Likelihood"
        }))
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- EXAM SECTION ---
    st.markdown(f"### {t({'de': 'Prüfungstraining', 'en': 'Exam Practice'})}")
    
    # MCQ 1: hs2022_mc8 (MLE for uniform distribution)
    q1 = get_question("8", "hs2022_mc8")
    if q1:
        with st.container(border=True):
            st.caption(q1.get("source", ""))
            opts = q1.get("options", [])
            if opts and isinstance(opts[0], dict):
                option_labels = [t(o) for o in opts]
            else:
                option_labels = opts
            
            render_mcq(
                key_suffix="8_3_mle",
                question_text=t(q1["question"]),
                options=option_labels,
                correct_idx=q1["correct_idx"],
                solution_text_dict=q1["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
                client=model,
                ai_context="Maximum Likelihood Estimator for uniform distribution",
                course_id="vwl",
                topic_id="8",
                subtopic_id="8.3",
                question_id="8_3_mle"
            )
