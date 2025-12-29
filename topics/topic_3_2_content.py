# Topic 3.2: Discrete Random Variables
import streamlit as st
from utils.localization import t
from utils.quiz_helper import render_mcq
from data.exam_questions import get_question

def render_subtopic_3_2(model):
    """3.2 Diskrete Zufallsvariablen - Discrete Random Variables"""
    
    st.header(t({"de": "3.2 Diskrete Zufallsvariablen", "en": "3.2 Discrete Random Variables"}))
    st.markdown("---")
    
    # --- THEORY PLACEHOLDER ---
    with st.container(border=True):
        st.markdown(f"### {t({'de': 'Theorie', 'en': 'Theory'})}")
        st.info(t({
            "de": "**Theorie-Inhalte kommen bald!**\n\nDieser Abschnitt wird theoretische Erklärungen zu diskreten Zufallsvariablen enthalten.",
            "en": "**Theory content coming soon!**\n\nThis section will contain theoretical explanations of discrete random variables."
        }))
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- EXAM SECTION ---
    st.markdown(f"### {t({'de': 'Prüfungstraining', 'en': 'Exam Practice'})}")
    
    # MCQ 1: uebung2_mc5
    q1_data = get_question("3.2", "uebung2_mc5")
    if q1_data:
        with st.container(border=True):
            st.caption(q1_data.get("source", ""))
            
            opts = q1_data.get("options", [])
            if opts and isinstance(opts[0], dict) and ('de' in opts[0] or 'en' in opts[0]):
                option_labels = [t(o) for o in opts]
            else:
                option_labels = opts
            
            render_mcq(
                key_suffix="3_2_mc5",
                question_text=t(q1_data["question"]),
                options=option_labels,
                correct_idx=q1_data["correct_idx"],
                solution_text_dict=q1_data["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
                client=model,
                ai_context="Discrete random variables - CDF calculation",
                course_id="vwl",
                topic_id="3",
                subtopic_id="3.2",
                question_id="3_2_mc5"
            )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # MCQ 2: test2_q4
    q2_data = get_question("3.2", "test2_q4")
    if q2_data:
        with st.container(border=True):
            st.caption(q2_data.get("source", ""))
            
            opts = q2_data.get("options", [])
            if opts and isinstance(opts[0], dict) and ('de' in opts[0] or 'en' in opts[0]):
                option_labels = [t(o) for o in opts]
            else:
                option_labels = opts
            
            render_mcq(
                key_suffix="3_2_q4",
                question_text=t(q2_data["question"]),
                options=option_labels,
                correct_idx=q2_data["correct_idx"],
                solution_text_dict=q2_data["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
                client=model,
                ai_context="Discrete PMF normalization constant",
                course_id="vwl",
                topic_id="3",
                subtopic_id="3.2",
                question_id="3_2_q4"
            )
