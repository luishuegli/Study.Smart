import streamlit as st
from utils.localization import t
from utils.quiz_helper import render_mcq
from utils.problem_renderer import render_multi_stage_problem, render_open_question
from data.exam_questions import get_all_questions_for_topic

# Config
TOPIC_ID = "topic_9"
SUBTOPIC_ID = "9.4"

def render_subtopic_9_4(model):
    st.header(t({"de": "9.4 Zusätzliche Prüfungsaufgaben", "en": "9.4 Additional Exam Questions"}))
    st.markdown("---")

    questions = get_all_questions_for_topic(SUBTOPIC_ID)
    
    if not questions:
        st.info(t({"de": "Noch keine Aufgaben verfügbar.", "en": "No exercises available yet."}))
        return

    for q_id, q in questions.items():
        q_type = q.get("type", "mc")
        
        if q_type == "multi_stage":
            render_multi_stage_problem(
                key_suffix=q_id,
                stem_text=q.get("stem", {}),
                parts=q.get("parts", []),
                source=q.get("source", ""),
                model=model,
                ai_context=q.get("ai_context", ""),
                course_id="vwl",
                topic_id=TOPIC_ID.replace("topic_", ""),
                subtopic_id=SUBTOPIC_ID,
                question_id=q_id
            )
            st.markdown("<br><br>", unsafe_allow_html=True)
            
        elif q_type == "open" or q_type == "problem":
            render_open_question(
                key_suffix=q_id,
                question_text=q.get("question", {}),
                solution_text_dict=q.get("solution", {}),
                source=q.get("source", ""),
                hints=q.get("hints", []),
                model=model,
                ai_context=q.get("ai_context", ""),
                course_id="vwl",
                topic_id=TOPIC_ID.replace("topic_", ""),
                subtopic_id=SUBTOPIC_ID,
                question_id=q_id
            )
            st.markdown("<br><br>", unsafe_allow_html=True)
            
        else:
            with st.container(border=True):
                 render_mcq(
                    key_suffix=q_id,
                    question_text=t(q["question"]),
                    options=q.get("options", []),
                    correct_idx=q.get("correct_idx", 0),
                    solution_text_dict=q["solution"],
                    success_msg_dict={"de": "Richtig!", "en": "Correct!"},
                    error_msg_dict={"de": "Falsch.", "en": "Incorrect."},
                    model=model,
                    ai_context=q.get("ai_context", ""),
                    course_id="vwl",
                    topic_id=TOPIC_ID.replace("topic_", ""),
                    subtopic_id=SUBTOPIC_ID,
                    question_id=q_id
                )
