# Topic 4.7: Normal Distribution
import streamlit as st
from utils.localization import t
from utils.quiz_helper import render_mcq
from data.exam_questions import get_question

def render_subtopic_4_7(model):
    """4.7 Normalverteilung (stetig) - Normal Distribution"""
    
    st.header(t({"de": "4.7 Normalverteilung (stetig)", "en": "4.7 Normal Distribution (Continuous)"}))
    st.markdown("---")
    
    # --- THEORY PLACEHOLDER ---
    with st.container(border=True):
        st.markdown(f"### {t({'de': 'Theorie', 'en': 'Theory'})}")
        st.info(t({
            "de": "**Theorie-Inhalte kommen bald!**\n\nDieser Abschnitt wird theoretische Erklärungen zur Normalverteilung enthalten.",
            "en": "**Theory content coming soon!**\n\nThis section will contain theoretical explanations of the normal distribution."
        }))
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- EXAM SECTION ---
    st.markdown(f"### {t({'de': 'Prüfungstraining', 'en': 'Exam Practice'})}")
    
    # MCQ 1: uebung2_mc13 (N(30,9))
    q1 = get_question("4.7", "uebung2_mc13")
    if q1:
        with st.container(border=True):
            st.caption(q1.get("source", ""))
            opts = q1.get("options", [])
            if opts and isinstance(opts[0], dict):
                option_labels = [t(o) for o in opts]
            else:
                option_labels = opts
            
            render_mcq(
                key_suffix="4_7_normal1",
                question_text=t(q1["question"]),
                options=option_labels,
                correct_idx=q1["correct_idx"],
                solution_text_dict=q1["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
                client=model,
                ai_context="Normal distribution - Z-score calculation",
                course_id="vwl",
                topic_id="4",
                subtopic_id="4.7",
                question_id="4_7_normal1"
            )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # MCQ 2: hs2023_mc7 (Exam scores)
    q2 = get_question("4.7", "hs2023_mc7")
    if q2:
        with st.container(border=True):
            st.caption(q2.get("source", ""))
            opts = q2.get("options", [])
            if opts and isinstance(opts[0], dict):
                option_labels = [t(o) for o in opts]
            else:
                option_labels = opts
            
            render_mcq(
                key_suffix="4_7_exam",
                question_text=t(q2["question"]),
                options=option_labels,
                correct_idx=q2["correct_idx"],
                solution_text_dict=q2["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
                client=model,
                ai_context="Normal distribution - exam score probability",
                course_id="vwl",
                topic_id="4",
                subtopic_id="4.7",
                question_id="4_7_exam"
            )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # MCQ 3: hs2022_mc3 (CLT - sample mean)
    q3 = get_question("4.7", "hs2022_mc3")
    if q3:
        with st.container(border=True):
            st.caption(q3.get("source", ""))
            opts = q3.get("options", [])
            if opts and isinstance(opts[0], dict):
                option_labels = [t(o) for o in opts]
            else:
                option_labels = opts
            
            render_mcq(
                key_suffix="4_7_clt",
                question_text=t(q3["question"]),
                options=option_labels,
                correct_idx=q3["correct_idx"],
                solution_text_dict=q3["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
                client=model,
                ai_context="Central Limit Theorem - sample mean probability",
                course_id="vwl",
                topic_id="4",
                subtopic_id="4.7",
                question_id="4_7_clt"
            )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # MCQ 4: hs2024_mc3_tanker (CLT - variance estimation)
    q4 = get_question("4.7", "hs2024_mc3_tanker")
    if q4:
        with st.container(border=True):
            st.caption(q4.get("source", ""))
            opts = q4.get("options", [])
            if opts and isinstance(opts[0], dict):
                option_labels = [t(o) for o in opts]
            else:
                option_labels = opts
            
            render_mcq(
                key_suffix="4_7_tanker",
                question_text=t(q4["question"]),
                options=option_labels,
                correct_idx=q4["correct_idx"],
                solution_text_dict=q4["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
                client=model,
                ai_context="CLT - reverse engineering variance from probability",
                course_id="vwl",
                topic_id="4",
                subtopic_id="4.7",
                question_id="4_7_tanker"
            )
