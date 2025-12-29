import streamlit as st
from utils.localization import t
from utils.quiz_helper import render_mcq
from data.exam_questions import get_question

def render_subtopic_3_7(model):
    """3.7 Additional Exam Questions"""
    
    st.header(t({"de": "3.7 Zusätzliche Prüfungsaufgaben", "en": "3.7 Additional Exam Questions"}))
    st.markdown("---")
    
    st.info(t({
        "de": "Gemischte Aufgaben zu Zufallsvariablen, Dichten, Verteilungen und Erwartungswerten.",
        "en": "Mixed problems on Random Variables, Densities, Distributions and Expectations."
    }))
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # List of Question IDs to render
    question_ids = [
        "hs2024_mc11", "hs2023_mc6",
        "uebung2_mc1", "uebung2_mc2", "uebung2_mc3", "uebung2_mc4", "uebung2_mc7",
        "test2_mc2", "test2_mc3", "test2_mc4", "test3_mc2"
    ]
    
    for q_id in question_ids:
        q = get_question("3.7", q_id)
        if q:
            with st.container(border=True):
                st.caption(q.get("source", ""))
                opts = q.get("options", [])
                if opts and isinstance(opts[0], dict):
                    option_labels = [t(o) for o in opts]
                else:
                    option_labels = opts
                
                render_mcq(
                    key_suffix=f"3_7_{q_id}",
                    question_text=t(q["question"]),
                    options=option_labels,
                    correct_idx=q["correct_idx"],
                    solution_text_dict=q["solution"],
                    success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                    error_msg_dict={"de": "Falsch.", "en": "Incorrect."},
                    client=model,
                    ai_context=f"RV Drill: {q_id}",
                    course_id="vwl",
                    topic_id="3",
                    subtopic_id="3.7",
                    question_id=q_id
                )
            st.markdown("<br>", unsafe_allow_html=True)
