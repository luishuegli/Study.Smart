# Topic 5.4: Sum of Two or More Random Variables
import streamlit as st
from utils.localization import t
from utils.quiz_helper import render_mcq
from data.exam_questions import get_question

def render_subtopic_5_4(model):
    """5.4 Summe von zwei oder mehreren Zufallsvariablen"""
    
    st.header(t({"de": "5.4 Summe von zwei oder mehreren Zufallsvariablen", "en": "5.4 Sum of Two or More Random Variables"}))
    st.markdown("---")
    
    # --- THEORY PLACEHOLDER ---
    with st.container(border=True):
        st.markdown(f"### {t({'de': 'Theorie', 'en': 'Theory'})}")
        st.info(t({
            "de": "**Theorie-Inhalte kommen bald!**\n\nDieser Abschnitt wird theoretische Erklärungen zur Summe von Zufallsvariablen enthalten.",
            "en": "**Theory content coming soon!**\n\nThis section will contain theoretical explanations of sums of random variables."
        }))
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- EXAM SECTION ---
    st.markdown(f"### {t({'de': 'Prüfungstraining', 'en': 'Exam Practice'})}")
    
    # MCQ 1: uebung3_mc10 (Correlation range)
    q1 = get_question("5.4", "uebung3_mc10")
    if q1:
        with st.container(border=True):
            st.caption(q1.get("source", ""))
            opts = q1.get("options", [])
            if opts and isinstance(opts[0], dict):
                option_labels = [t(o) for o in opts]
            else:
                option_labels = opts
            
            render_mcq(
                key_suffix="5_4_range",
                question_text=t(q1["question"]),
                options=option_labels,
                correct_idx=q1["correct_idx"],
                solution_text_dict=q1["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
                client=model,
                ai_context="Range of correlation coefficient",
                course_id="vwl",
                topic_id="5",
                subtopic_id="5.4",
                question_id="5_4_range"
            )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # MCQ 2: uebung3_mc11 (Corr = 0.8 interpretation)
    q2 = get_question("5.4", "uebung3_mc11")
    if q2:
        with st.container(border=True):
            st.caption(q2.get("source", ""))
            opts = q2.get("options", [])
            if opts and isinstance(opts[0], dict):
                option_labels = [t(o) for o in opts]
            else:
                option_labels = opts
            
            render_mcq(
                key_suffix="5_4_interp",
                question_text=t(q2["question"]),
                options=option_labels,
                correct_idx=q2["correct_idx"],
                solution_text_dict=q2["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
                client=model,
                ai_context="Interpreting correlation values",
                course_id="vwl",
                topic_id="5",
                subtopic_id="5.4",
                question_id="5_4_interp"
            )
