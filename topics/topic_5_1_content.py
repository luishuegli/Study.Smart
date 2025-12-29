# Topic 5.1: Joint Distribution and Marginal Distributions
import streamlit as st
from utils.localization import t
from utils.quiz_helper import render_mcq
from data.exam_questions import get_question

def render_subtopic_5_1(model):
    """5.1 Gemeinsame Verteilung und Randverteilungen"""
    
    st.header(t({"de": "5.1 Gemeinsame Verteilung und Randverteilungen", "en": "5.1 Joint Distribution and Marginal Distributions"}))
    st.markdown("---")
    
    # --- THEORY PLACEHOLDER ---
    with st.container(border=True):
        st.markdown(f"### {t({'de': 'Theorie', 'en': 'Theory'})}")
        st.info(t({
            "de": "**Theorie-Inhalte kommen bald!**\n\nDieser Abschnitt wird theoretische Erklärungen zu gemeinsamen Verteilungen und Randverteilungen enthalten.",
            "en": "**Theory content coming soon!**\n\nThis section will contain theoretical explanations of joint distributions and marginal distributions."
        }))
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- EXAM SECTION ---
    st.markdown(f"### {t({'de': 'Prüfungstraining', 'en': 'Exam Practice'})}")
    
    # MCQ 1: test3_q4 (E[X+Y])
    q1 = get_question("5.1", "test3_q4")
    if q1:
        with st.container(border=True):
            st.caption(q1.get("source", ""))
            opts = q1.get("options", [])
            if opts and isinstance(opts[0], dict):
                option_labels = [t(o) for o in opts]
            else:
                option_labels = opts
            
            render_mcq(
                key_suffix="5_1_sum",
                question_text=t(q1["question"]),
                options=option_labels,
                correct_idx=q1["correct_idx"],
                solution_text_dict=q1["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
                client=model,
                ai_context="Linearity of expectation",
                course_id="vwl",
                topic_id="5",
                subtopic_id="5.1",
                question_id="5_1_sum"
            )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # MCQ 2: uebung3_mc5 (Expectation operator)
    q2 = get_question("5.1", "uebung3_mc5")
    if q2:
        with st.container(border=True):
            st.caption(q2.get("source", ""))
            opts = q2.get("options", [])
            if opts and isinstance(opts[0], dict):
                option_labels = [t(o) for o in opts]
            else:
                option_labels = opts
            
            render_mcq(
                key_suffix="5_1_linear",
                question_text=t(q2["question"]),
                options=option_labels,
                correct_idx=q2["correct_idx"],
                solution_text_dict=q2["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
                client=model,
                ai_context="Properties of expectation operator",
                course_id="vwl",
                topic_id="5",
                subtopic_id="5.1",
                question_id="5_1_linear"
            )
