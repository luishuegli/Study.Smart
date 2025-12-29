import streamlit as st
from utils.localization import t
from utils.quiz_helper import render_mcq
from data.exam_questions import get_question

def render_subtopic_8_4(model):
    """8.4 Additional Exam Questions"""
    
    st.header(t({"de": "8.4 Zusätzliche Prüfungsaufgaben", "en": "8.4 Additional Exam Questions"}))
    st.markdown("---")
    
    st.info(t({
        "de": "Aufgaben zu Schätzfunktionen (Erwartungstreue, Konsistenz, Effizienz, MSE) und Methoden (MOM, MLE).",
        "en": "Problems on Estimators (Unbiasedness, Consistency, Efficiency, MSE) and Methods (MOM, MLE)."
    }))
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # List of Question IDs to render
    question_ids = [
        "uebung5_mc1", "uebung5_mc2", "uebung5_mc3", "uebung5_mc4", "uebung5_mc5",
        "uebung5_mc6", "uebung5_mc7", "uebung5_mc8", "uebung5_mc9",
        "uebung5_mc10", "uebung5_mc11", "uebung5_mc12", "uebung5_mc13", "uebung5_mc14", "uebung5_mc15",
        "uebung5_prob1", "uebung5_prob3", "uebung5_prob5", "uebung5_prob6", "uebung5_prob8",
        "test5_mc3"
    ]
    
    for q_id in question_ids:
        q = get_question("8.4", q_id)
        if q:
            with st.container(border=True):
                st.caption(q.get("source", ""))
                opts = q.get("options", [])
                if opts and isinstance(opts[0], dict):
                    option_labels = [t(o) for o in opts]
                else:
                    option_labels = opts
                
                render_mcq(
                    key_suffix=f"8_4_{q_id}",
                    question_text=t(q["question"]),
                    options=option_labels,
                    correct_idx=q["correct_idx"],
                    solution_text_dict=q["solution"],
                    success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                    error_msg_dict={"de": "Falsch.", "en": "Incorrect."},
                    client=model,
                    ai_context=f"Estimation Drill: {q_id}",
                    course_id="vwl",
                    topic_id="8",
                    subtopic_id="8.4",
                    question_id=q_id
                )
            st.markdown("<br>", unsafe_allow_html=True)
