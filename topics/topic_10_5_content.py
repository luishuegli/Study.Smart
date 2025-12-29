import streamlit as st
from utils.localization import t
from utils.quiz_helper import render_mcq
from data.exam_questions import get_question

def render_subtopic_10_5(model):
    """10.5 Additional Exam Questions"""
    
    st.header(t({"de": "10.5 Zusätzliche Prüfungsaufgaben", "en": "10.5 Additional Exam Questions"}))
    st.markdown("---")
    
    st.info(t({
        "de": "Aufgaben zu Hypothesentests (Z-Test, p-Wert, Macht).",
        "en": "Problems on Hypothesis Testing (Z-Test, p-value, Power)."
    }))
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # List of Question IDs to render
    question_ids = [
        "uebung6_prob1", "uebung6_prob2", 
        "uebung6_prob3", "uebung6_prob4"
    ]
    
    for q_id in question_ids:
        q = get_question("10.5", q_id)
        if q:
            with st.container(border=True):
                st.caption(q.get("source", ""))
                opts = q.get("options", [])
                if opts and isinstance(opts[0], dict):
                    option_labels = [t(o) for o in opts]
                else:
                    option_labels = opts
                
                render_mcq(
                    key_suffix=f"10_5_{q_id}",
                    question_text=t(q["question"]),
                    options=option_labels,
                    correct_idx=q["correct_idx"],
                    solution_text_dict=q["solution"],
                    success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                    error_msg_dict={"de": "Falsch.", "en": "Incorrect."},
                    client=model,
                    ai_context=f"Hypothesis Test Drill: {q_id}",
                    course_id="vwl",
                    topic_id="10",
                    subtopic_id="10.5",
                    question_id=q_id
                )
            st.markdown("<br>", unsafe_allow_html=True)
