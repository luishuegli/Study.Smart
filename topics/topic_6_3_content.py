import streamlit as st
from utils.localization import t
from utils.quiz_helper import render_mcq
from utils.problem_renderer import render_open_question
from data.exam_questions import get_all_questions_for_topic

def render_subtopic_6_3(model):
    """6.3 Additional Exam Questions"""
    
    st.header(t({"de": "6.3 Zusätzliche Prüfungsaufgaben", "en": "6.3 Additional Exam Questions"}))
    st.markdown("---")
    
    st.info(t({
        "de": "Aufgaben zum Zentralen Grenzwertsatz (CLT) und Normalapproximation.",
        "en": "Problems on Central Limit Theorem (CLT) and Normal Approximation."
    }))
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Get all questions for this subtopic
    questions = get_all_questions_for_topic("6.3")
    
    for q_id, q in questions.items():
        q_type = q.get("type", "mc")
        
        if q_type == "problem" or q_type == "open":
            # Use problem renderer for open-ended questions
            render_open_question(
                key_suffix=f"6_3_{q_id}",
                question_text=q["question"],
                solution_text_dict=q["solution"],
                source=q.get("source", ""),
                hints=q.get("hints", []),
                model=model,
                ai_context=f"CLT Problem: {q_id}",
                course_id="vwl",
                topic_id="6",
                subtopic_id="6.3",
                question_id=q_id
            )
        else:
            # Use MCQ renderer for multiple choice
            with st.container(border=True):
                st.caption(q.get("source", ""))
                opts = q.get("options", [])
                if opts and isinstance(opts[0], dict):
                    option_labels = [t(o) for o in opts]
                else:
                    option_labels = opts
                
                render_mcq(
                    key_suffix=f"6_3_{q_id}",
                    question_text=t(q["question"]),
                    options=option_labels,
                    correct_idx=q["correct_idx"],
                    solution_text_dict=q["solution"],
                    success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                    error_msg_dict={"de": "Falsch.", "en": "Incorrect."},
                    client=model,
                    ai_context=f"CLT Drill: {q_id}",
                    course_id="vwl",
                    topic_id="6",
                    subtopic_id="6.3",
                    question_id=q_id
                )
        st.markdown("<br>", unsafe_allow_html=True)
