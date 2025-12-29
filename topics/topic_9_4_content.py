import streamlit as st
from utils.localization import t
from utils.quiz_helper import render_mcq
from data.exam_questions import get_question

def render_subtopic_9_4(model):
    """9.4 Additional Exam Questions"""
    
    st.header(t({"de": "9.4 Zusätzliche Prüfungsaufgaben", "en": "9.4 Additional Exam Questions"}))
    st.markdown("---")
    
    st.info(t({
        "de": "Aufgaben zu Konfidenzintervallen.",
        "en": "Problems on Confidence Intervals."
    }))
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # List of Question IDs to render
    question_ids = [
        "uebung5_mc16", "uebung5_mc17", "uebung5_mc18",
        "uebung5_prob9",
        "test5_mc4"
    ]
    
    for q_id in question_ids:
        q = get_question("9.4", q_id)
        if q:
            with st.container(border=True):
                st.caption(q.get("source", ""))
                opts = q.get("options", [])
                if opts and isinstance(opts[0], dict):
                    option_labels = [t(o) for o in opts]
                else:
                    option_labels = opts
                
                render_mcq(
                    key_suffix=f"9_4_{q_id}",
                    question_text=t(q["question"]),
                    options=option_labels,
                    correct_idx=q["correct_idx"],
                    solution_text_dict=q["solution"],
                    success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                    error_msg_dict={"de": "Falsch.", "en": "Incorrect."},
                    client=model,
                    ai_context=f"CI Drill: {q_id}",
                    course_id="vwl",
                    topic_id="9",
                    subtopic_id="9.4",
                    question_id=q_id
                )
            st.markdown("<br>", unsafe_allow_html=True)
