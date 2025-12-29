# Topic 5.3: Covariance and Correlation Coefficient
import streamlit as st
from utils.localization import t
from utils.quiz_helper import render_mcq
from data.exam_questions import get_question

def render_subtopic_5_3(model):
    """5.3 Kovarianz und Korrelationskoeffizient"""
    
    st.header(t({"de": "5.3 Kovarianz und Korrelationskoeffizient", "en": "5.3 Covariance and Correlation Coefficient"}))
    st.markdown("---")
    
    # --- THEORY PLACEHOLDER ---
    with st.container(border=True):
        st.markdown(f"### {t({'de': 'Theorie', 'en': 'Theory'})}")
        st.info(t({
            "de": "**Theorie-Inhalte kommen bald!**\n\nDieser Abschnitt wird theoretische Erklärungen zur Kovarianz und Korrelation enthalten.",
            "en": "**Theory content coming soon!**\n\nThis section will contain theoretical explanations of covariance and correlation."
        }))
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- EXAM SECTION ---
    st.markdown(f"### {t({'de': 'Prüfungstraining', 'en': 'Exam Practice'})}")
    
    # MCQ 1: uebung3_mc1 (Covariance measures)
    q1 = get_question("5.3", "uebung3_mc1")
    if q1:
        with st.container(border=True):
            st.caption(q1.get("source", ""))
            opts = q1.get("options", [])
            if opts and isinstance(opts[0], dict):
                option_labels = [t(o) for o in opts]
            else:
                option_labels = opts
            
            render_mcq(
                key_suffix="5_3_cov_def",
                question_text=t(q1["question"]),
                options=option_labels,
                correct_idx=q1["correct_idx"],
                solution_text_dict=q1["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
                client=model,
                ai_context="What covariance measures",
                course_id="vwl",
                topic_id="5",
                subtopic_id="5.3",
                question_id="5_3_cov_def"
            )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # MCQ 2: uebung3_mc9 (Urn correlation)
    q2 = get_question("5.3", "uebung3_mc9")
    if q2:
        with st.container(border=True):
            st.caption(q2.get("source", ""))
            opts = q2.get("options", [])
            if opts and isinstance(opts[0], dict):
                option_labels = [t(o) for o in opts]
            else:
                option_labels = opts
            
            render_mcq(
                key_suffix="5_3_urn",
                question_text=t(q2["question"]),
                options=option_labels,
                correct_idx=q2["correct_idx"],
                solution_text_dict=q2["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
                client=model,
                ai_context="Correlation in sampling without replacement",
                course_id="vwl",
                topic_id="5",
                subtopic_id="5.3",
                question_id="5_3_urn"
            )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # MCQ 3: test4_q2 (Correlation calculation)
    q3 = get_question("5.3", "test4_q2")
    if q3:
        with st.container(border=True):
            st.caption(q3.get("source", ""))
            opts = q3.get("options", [])
            if opts and isinstance(opts[0], dict):
                option_labels = [t(o) for o in opts]
            else:
                option_labels = opts
            
            render_mcq(
                key_suffix="5_3_calc",
                question_text=t(q3["question"]),
                options=option_labels,
                correct_idx=q3["correct_idx"],
                solution_text_dict=q3["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
                client=model,
                ai_context="Calculating correlation from covariance and variances",
                course_id="vwl",
                topic_id="5",
                subtopic_id="5.3",
                question_id="5_3_calc"
            )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # MCQ 4: test4_q4 (Independence → Covariance = 0)
    q4 = get_question("5.3", "test4_q4")
    if q4:
        with st.container(border=True):
            st.caption(q4.get("source", ""))
            opts = q4.get("options", [])
            if opts and isinstance(opts[0], dict):
                option_labels = [t(o) for o in opts]
            else:
                option_labels = opts
            
            render_mcq(
                key_suffix="5_3_indep",
                question_text=t(q4["question"]),
                options=option_labels,
                correct_idx=q4["correct_idx"],
                solution_text_dict=q4["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
                client=model,
                ai_context="Independence implies zero covariance",
                course_id="vwl",
                topic_id="5",
                subtopic_id="5.3",
                question_id="5_3_indep"
            )
            
    st.markdown("<br>", unsafe_allow_html=True)
    
    # MCQ 5: hs2024_mc2 (Correlation properties)
    q5 = get_question("5.3", "hs2024_mc2")
    if q5:
        with st.container(border=True):
            st.caption(q5.get("source", ""))
            opts = q5.get("options", [])
            if opts and isinstance(opts[0], dict):
                option_labels = [t(o) for o in opts]
            else:
                option_labels = opts
            
            render_mcq(
                key_suffix="5_3_corr_props",
                question_text=t(q5["question"]),
                options=option_labels,
                correct_idx=q5["correct_idx"],
                solution_text_dict=q5["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
                client=model,
                ai_context="Correlation vs Independence properties",
                course_id="vwl",
                topic_id="5",
                subtopic_id="5.3",
                question_id="5_3_corr_props"
            )
            
    st.markdown("<br>", unsafe_allow_html=True)
    

