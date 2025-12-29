import streamlit as st
from utils.localization import t
from utils.quiz_helper import render_mcq
from data.exam_questions import get_question

def render_subtopic_1_11(model):
    """1.11 Additional Exam Questions"""
    
    st.header(t({"de": "1.11 Zusätzliche Prüfungsaufgaben", "en": "1.11 Additional Exam Questions"}))
    st.markdown("---")
    
    st.info(t({
        "de": "Gemischte Aufgaben zu Wahrscheinlichkeiten, Bedingter W'keit und Unabhängigkeit.",
        "en": "Mixed problems on Probability, Conditional Prob, and Independence."
    }))
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # List of Question IDs to render
    question_ids = [
        "hs2024_mc10",
        "uebung1_mc3", "uebung1_mc16",
        "hub_mc1", "hub_mc2", "hub_mc3", "hub_mc4",
        "hs2022_prob3",
        "test1_mc1", "test1_mc2", "test3_mc1" 
    ]
    
    for q_id in question_ids:
        q = get_question("1.11", q_id)
        if q:
            # Handle Multi-Stage separately? No, currently get_question returns dict.
            # Assuming simple render for now.
            if q.get("type") == "multi_stage":
                # Fallback or specific renderer. For now, skip or basic dump?
                # hs2022_prob3 is multi-stage. It might fail `render_mcq`.
                # We need `render_multi_stage_problem`.
                # But that is not implemented in `quiz_helper` yet?
                # Implementation Plan said "NEW FILE utils/problem_renderer.py".
                # I haven't created that yet.
                # I should just render a placeholder or simple text for now.
                with st.container(border=True):
                    st.markdown(f"**{q_id}** (Multi-Stage Problem)")
                    st.caption("Rendering not fully implemented yet.")
                continue

            with st.container(border=True):
                st.caption(q.get("source", ""))
                opts = q.get("options", [])
                if opts and isinstance(opts[0], dict):
                    option_labels = [t(o) for o in opts]
                else:
                    option_labels = opts
                
                render_mcq(
                    key_suffix=f"1_11_{q_id}",
                    question_text=t(q["question"]),
                    options=option_labels,
                    correct_idx=q.get("correct_idx", 0),
                    solution_text_dict=q["solution"],
                    success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                    error_msg_dict={"de": "Falsch.", "en": "Incorrect."},
                    client=model,
                    ai_context=f"Prob Drill: {q_id}",
                    course_id="vwl",
                    topic_id="1",
                    subtopic_id="1.11",
                    question_id=q_id
                )
            st.markdown("<br>", unsafe_allow_html=True)
