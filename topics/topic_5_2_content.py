# Topic 5.2: Conditional Distributions and Stochastic Independence
import streamlit as st
from utils.localization import t
from utils.quiz_helper import render_mcq
from data.exam_questions import get_question

def render_subtopic_5_2(model):
    """5.2 Bedingte Verteilungen und stochastische Unabhängigkeit"""
    
    st.header(t({"de": "5.2 Bedingte Verteilungen und stochastische Unabhängigkeit", "en": "5.2 Conditional Distributions and Stochastic Independence"}))
    st.markdown("---")
    
    # --- THEORY PLACEHOLDER ---
    with st.container(border=True):
        st.markdown(f"### {t({'de': 'Theorie', 'en': 'Theory'})}")
        st.info(t({
            "de": "**Theorie-Inhalte kommen bald!**\n\nDieser Abschnitt wird theoretische Erklärungen zu bedingten Verteilungen enthalten.",
            "en": "**Theory content coming soon!**\n\nThis section will contain theoretical explanations of conditional distributions."
        }))
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- EXAM SECTION ---
    st.markdown(f"### {t({'de': 'Prüfungstraining', 'en': 'Exam Practice'})}")
    
    # MCQ 1: test3_q5 (Var(X - Y))
    q1 = get_question("5.2", "test3_q5")
    if q1:
        with st.container(border=True):
            st.caption(q1.get("source", ""))
            opts = q1.get("options", [])
            if opts and isinstance(opts[0], dict):
                option_labels = [t(o) for o in opts]
            else:
                option_labels = opts
            
            render_mcq(
                key_suffix="5_2_vardiff",
                question_text=t(q1["question"]),
                options=option_labels,
                correct_idx=q1["correct_idx"],
                solution_text_dict=q1["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
                client=model,
                ai_context="Variance of difference of independent variables",
                course_id="vwl",
                topic_id="5",
                subtopic_id="5.2",
                question_id="5_2_vardiff"
            )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # MCQ 2: uebung3_mc7 (Var(aX + b))
    q2 = get_question("5.2", "uebung3_mc7")
    if q2:
        with st.container(border=True):
            st.caption(q2.get("source", ""))
            opts = q2.get("options", [])
            if opts and isinstance(opts[0], dict):
                option_labels = [t(o) for o in opts]
            else:
                option_labels = opts
            
            render_mcq(
                key_suffix="5_2_varscale",
                question_text=t(q2["question"]),
                options=option_labels,
                correct_idx=q2["correct_idx"],
                solution_text_dict=q2["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
                client=model,
                ai_context="Variance of linear transformation",
                course_id="vwl",
                topic_id="5",
                subtopic_id="5.2",
                question_id="5_2_varscale"
            )
