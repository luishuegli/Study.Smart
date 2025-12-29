import streamlit as st
from utils.localization import t
from utils.quiz_helper import render_mcq
from data.exam_questions import get_question

def render_subtopic_7_6(model):
    """7.6 Additional Exam Questions"""
    
    st.header(t({"de": "7.6 Zusätzliche Prüfungsaufgaben", "en": "7.6 Additional Exam Questions"}))
    st.markdown("---")
    
    st.info(t({
        "de": "Zusätzliche Aufgaben zur Beschreibenden Statistik.",
        "en": "Additional problems on Descriptive Statistics."
    }))
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # List of Question IDs to render
    question_ids = [
        "test4_mc3"
    ]
    
    for q_id in question_ids:
        q = get_question("7.6", q_id)
        if q:
            with st.container(border=True):
                st.caption(q.get("source", ""))
                opts = q.get("options", [])
                if opts and isinstance(opts[0], dict):
                    option_labels = [t(o) for o in opts]
                else:
                    option_labels = opts
                
                render_mcq(
                    key_suffix=f"7_6_{q_id}",
                    question_text=t(q["question"]),
                    options=option_labels,
                    correct_idx=q["correct_idx"],
                    solution_text_dict=q["solution"],
                    success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                    error_msg_dict={"de": "Falsch.", "en": "Incorrect."},
                    client=model,
                    ai_context=f"Descriptive Drill: {q_id}",
                    course_id="vwl",
                    topic_id="7",
                    subtopic_id="7.6",
                    question_id=q_id
                )
            st.markdown("<br>", unsafe_allow_html=True)
