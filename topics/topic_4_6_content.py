# Topic 4.6: Exponential Distribution
import streamlit as st
from utils.localization import t
from utils.quiz_helper import render_mcq
from data.exam_questions import get_question

def render_subtopic_4_6(model):
    """4.6 Exponentialverteilung (stetig) - Exponential Distribution"""
    
    st.header(t({"de": "4.6 Exponentialverteilung (stetig)", "en": "4.6 Exponential Distribution (Continuous)"}))
    st.markdown("---")
    
    # --- THEORY PLACEHOLDER ---
    with st.container(border=True):
        st.markdown(f"### {t({'de': 'Theorie', 'en': 'Theory'})}")
        st.info(t({
            "de": "**Theorie-Inhalte kommen bald!**\n\nDieser Abschnitt wird theoretische Erklärungen zur Exponentialverteilung enthalten.",
            "en": "**Theory content coming soon!**\n\nThis section will contain theoretical explanations of the exponential distribution."
        }))
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- EXAM SECTION ---
    st.markdown(f"### {t({'de': 'Prüfungstraining', 'en': 'Exam Practice'})}")
    
    # MCQ 1: uebung2_mc12 (Battery lifetime)
    q1 = get_question("4.6", "uebung2_mc12")
    if q1:
        with st.container(border=True):
            st.caption(q1.get("source", ""))
            opts = q1.get("options", [])
            if opts and isinstance(opts[0], dict):
                option_labels = [t(o) for o in opts]
            else:
                option_labels = opts
            
            render_mcq(
                key_suffix="4_6_exp",
                question_text=t(q1["question"]),
                options=option_labels,
                correct_idx=q1["correct_idx"],
                solution_text_dict=q1["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
                client=model,
                ai_context="Exponential distribution - survival probability",
                course_id="vwl",
                topic_id="4",
                subtopic_id="4.6",
                question_id="4_6_exp"
            )
