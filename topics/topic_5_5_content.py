import streamlit as st
from utils.localization import t
from utils.quiz_helper import render_mcq
from data.exam_questions import get_question

def render_subtopic_5_5(model):
    """5.5 Additional Exam Questions"""
    
    st.header(t({"de": "5.5 Zusätzliche Prüfungsaufgaben", "en": "5.5 Additional Exam Questions"}))
    st.markdown("---")
    
    st.info(t({
        "de": "Aufgaben zu mehrdimensionalen Zufallsvariablen (Kovarianz, Korrelation, Summen).",
        "en": "Problems on multidimensional random variables (Covariance, Correlation, Sums)."
    }))
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # List of Question IDs to render
    question_ids = [
        "uebung3_mc2", "uebung3_mc3", "uebung3_mc4", 
        "uebung3_mc6", "uebung3_mc8", "uebung3_mc12", "uebung3_mc13",
        "test3_mc3", "test3_mc4", "test4_mc2", "test5_mc2",
        "uebung3_prob1", "uebung3_prob2", "uebung3_prob3", 
        "uebung3_prob4", "uebung3_prob5", "uebung3_prob6", "uebung3_prob7"
    ]
    
    for q_id in question_ids:
        q = get_question("5.5", q_id)
        if q:
            with st.container(border=True):
                st.caption(q.get("source", ""))
                opts = q.get("options", [])
                if opts and isinstance(opts[0], dict):
                    option_labels = [t(o) for o in opts]
                else:
                    option_labels = opts
                
                render_mcq(
                    key_suffix=f"5_5_{q_id}",
                    question_text=t(q["question"]),
                    options=option_labels,
                    correct_idx=q["correct_idx"],
                    solution_text_dict=q["solution"],
                    success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                    error_msg_dict={"de": "Falsch.", "en": "Incorrect."},
                    client=model,
                    ai_context=f"MultiVariate Drill: {q_id}",
                    course_id="vwl",
                    topic_id="5",
                    subtopic_id="5.5",
                    question_id=q_id
                )
            st.markdown("<br>", unsafe_allow_html=True)
