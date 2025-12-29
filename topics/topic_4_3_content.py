# Topic 4.3: Binomial Distribution
import streamlit as st
from utils.localization import t
from utils.quiz_helper import render_mcq
from data.exam_questions import get_question

def render_subtopic_4_3(model):
    """4.3 Binomialverteilung - Binomial Distribution"""
    
    st.header(t({"de": "4.3 Binomialverteilung (diskret)", "en": "4.3 Binomial Distribution (Discrete)"}))
    st.markdown("---")
    
    # --- THEORY PLACEHOLDER ---
    with st.container(border=True):
        st.markdown(f"### {t({'de': 'Theorie', 'en': 'Theory'})}")
        st.info(t({
            "de": "**Theorie-Inhalte kommen bald!**\n\nDieser Abschnitt wird theoretische Erklärungen zur Binomialverteilung enthalten.",
            "en": "**Theory content coming soon!**\n\nThis section will contain theoretical explanations of the binomial distribution."
        }))
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- EXAM SECTION ---
    st.markdown(f"### {t({'de': 'Prüfungstraining', 'en': 'Exam Practice'})}")
    
    # MCQ 1: uebung2_giro
    q1 = get_question("4.3", "uebung2_giro")
    if q1:
        with st.container(border=True):
            st.caption(q1.get("source", ""))
            opts = q1.get("options", [])
            if opts and isinstance(opts[0], dict):
                option_labels = [t(o) for o in opts]
            else:
                option_labels = opts
            
            render_mcq(
                key_suffix="4_3_giro",
                question_text=t(q1["question"]),
                options=option_labels,
                correct_idx=q1["correct_idx"],
                solution_text_dict=q1["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
                client=model,
                ai_context="Binomial distribution - at least k successes",
                course_id="vwl",
                topic_id="4",
                subtopic_id="4.3",
                question_id="4_3_giro"
            )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # MCQ 2: hs2022_mc7 (Rain probability)
    q2 = get_question("4.3", "hs2022_mc7")
    if q2:
        with st.container(border=True):
            st.caption(q2.get("source", ""))
            opts = q2.get("options", [])
            if opts and isinstance(opts[0], dict):
                option_labels = [t(o) for o in opts]
            else:
                option_labels = opts
            
            render_mcq(
                key_suffix="4_3_rain",
                question_text=t(q2["question"]),
                options=option_labels,
                correct_idx=q2["correct_idx"],
                solution_text_dict=q2["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
                client=model,
                ai_context="Binomial distribution - weather probability",
                course_id="vwl",
                topic_id="4",
                subtopic_id="4.3",
                question_id="4_3_rain"
            )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # MCQ 3: hs2023_mc12 (Casino slots)
    q3 = get_question("4.3", "hs2023_mc12")
    if q3:
        with st.container(border=True):
            st.caption(q3.get("source", ""))
            opts = q3.get("options", [])
            if opts and isinstance(opts[0], dict):
                option_labels = [t(o) for o in opts]
            else:
                option_labels = opts
            
            render_mcq(
                key_suffix="4_3_casino",
                question_text=t(q3["question"]),
                options=option_labels,
                correct_idx=q3["correct_idx"],
                solution_text_dict=q3["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
                client=model,
                ai_context="Binomial distribution - two-stage problem",
                course_id="vwl",
                topic_id="4",
                subtopic_id="4.3",
                question_id="4_3_casino"
            )
