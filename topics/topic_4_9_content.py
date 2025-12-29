import streamlit as st
from utils.localization import t
from utils.quiz_helper import render_mcq
from data.exam_questions import get_question

def render_subtopic_4_9(model):
    """4.9 Additional Exam Questions"""
    
    st.header(t({"de": "4.9 Zusätzliche Prüfungsaufgaben", "en": "4.9 Additional Exam Questions"}))
    st.markdown("---")
    
    st.info(t({
        "de": "Aufgaben zu Verteilungsmodellen (Binomial, Poisson, Normal, etc.).",
        "en": "Problems on Distribution Models (Binomial, Poisson, Normal, etc.)."
    }))
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # List of Question IDs to render
    question_ids = [
        "hs2023_prob3",
        "uebung2_mc9", "uebung2_mc10", "uebung2_mc11", "uebung2_mc14", "uebung2_mc15",
        "hs2022_mc6",
        "test4_mc1", "test5_mc1"
    ]
    
    for q_id in question_ids:
        q = get_question("4.9", q_id)
        if q:
            # Handle Problems vs MC
            if q.get("type") == "problem":
                 # Simple rendering for problems that are not MC (if any)
                 # hs2023_prob3 is type "problem".
                 with st.container(border=True):
                    st.caption(q.get("source", ""))
                    st.markdown(f"**{t(q['question'])}**")
                    with st.expander(t({"de": "Lösung anzeigen", "en": "Show Solution"})):
                         st.markdown(t(q["solution"]))
            else:
                with st.container(border=True):
                    st.caption(q.get("source", ""))
                    opts = q.get("options", [])
                    if opts and isinstance(opts[0], dict):
                        option_labels = [t(o) for o in opts]
                    else:
                        option_labels = opts
                    
                    render_mcq(
                        key_suffix=f"4_9_{q_id}",
                        question_text=t(q["question"]),
                        options=option_labels,
                        correct_idx=q["correct_idx"],
                        solution_text_dict=q["solution"],
                        success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                        error_msg_dict={"de": "Falsch.", "en": "Incorrect."},
                        client=model,
                        ai_context=f"Distributions Drill: {q_id}",
                        course_id="vwl",
                        topic_id="4",
                        subtopic_id="4.9",
                        question_id=q_id
                    )
            st.markdown("<br>", unsafe_allow_html=True)
