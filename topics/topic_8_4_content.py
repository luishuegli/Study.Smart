import streamlit as st
from utils.localization import t
from utils.quiz_helper import render_mcq
from utils.problem_renderer import render_open_question, render_multi_stage_problem
from data.exam_questions import get_all_questions_for_topic

def render_subtopic_8_4(model):
    """8.4 Additional Exam Questions"""
    
    st.header(t({"de": "8.4 Zusätzliche Prüfungsaufgaben", "en": "8.4 Additional Exam Questions"}))
    st.markdown("---")
    
    st.info(t({
        "de": "Aufgaben zu Schätzfunktionen (Erwartungstreue, Konsistenz, Effizienz, MSE) und Methoden (MOM, MLE).",
        "en": "Problems on Estimators (Unbiasedness, Consistency, Efficiency, MSE) and Methods (MOM, MLE)."
    }))
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Get all questions for this subtopic
    questions = get_all_questions_for_topic("8.4")
    
    for q_id, q in questions.items():
        q_type = q.get("type", "mc")
        
        if q_type == "multi_stage":
            render_multi_stage_problem(
                key_suffix=f"8_4_{q_id}",
                stem_text=q.get("stem", {}),
                parts=q.get("parts", []),
                source=q.get("source", ""),
                model=model,
                ai_context=f"Estimation Problem: {q_id}",
                course_id="vwl",
                topic_id="8",
                subtopic_id="8.4",
                question_id=q_id
            )
        elif q_type == "problem" or q_type == "open":
            render_open_question(
                key_suffix=f"8_4_{q_id}",
                question_text=q["question"],
                solution_text_dict=q["solution"],
                source=q.get("source", ""),
                hints=q.get("hints", []),
                model=model,
                ai_context=f"Estimation Problem: {q_id}",
                course_id="vwl",
                topic_id="8",
                subtopic_id="8.4",
                question_id=q_id
            )
        else:
            # MC type
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
