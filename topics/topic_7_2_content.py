# Topic 7.2: Measures for Describing Statistical Distributions
import streamlit as st
from utils.localization import t
from utils.quiz_helper import render_mcq
from data.exam_questions import get_question

def render_subtopic_7_2(model):
    """7.2 Messzahlen zur Beschreibung statistischer Verteilungen"""
    
    st.header(t({"de": "7.2 Messzahlen zur Beschreibung statistischer Verteilungen", "en": "7.2 Measures for Describing Statistical Distributions"}))
    st.markdown("---")
    
    # --- THEORY PLACEHOLDER ---
    with st.container(border=True):
        st.markdown(f"### {t({'de': 'Theorie', 'en': 'Theory'})}")
        st.info(t({
            "de": "**Theorie-Inhalte kommen bald!**\n\nDieser Abschnitt wird theoretische Erklärungen enthalten:\n\n• Lagemaße (Mean, Median, Mode)\n• Streuungsmaße (Varianz, Standardabweichung)\n• Schiefe und Wölbung",
            "en": "**Theory content coming soon!**\n\nThis section will contain theoretical explanations:\n\n• Location measures (Mean, Median, Mode)\n• Dispersion measures (Variance, Standard Deviation)\n• Skewness and Kurtosis"
        }))
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- EXAM SECTION ---
    st.markdown(f"### {t({'de': 'Prüfungstraining', 'en': 'Exam Practice'})}")
    
    # MCQ 1: test4_q3 (Mean, Median, Mode)
    q1 = get_question("7", "test4_q3")
    if q1:
        with st.container(border=True):
            st.caption(q1.get("source", ""))
            opts = q1.get("options", [])
            if opts and isinstance(opts[0], dict):
                option_labels = [t(o) for o in opts]
            else:
                option_labels = opts
            
            render_mcq(
                key_suffix="7_2_measures",
                question_text=t(q1["question"]),
                options=option_labels,
                correct_idx=q1["correct_idx"],
                solution_text_dict=q1["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
                client=model,
                ai_context="Mean, Median, Mode identification",
                course_id="vwl",
                topic_id="7",
                subtopic_id="7.2",
                question_id="7_2_measures"
            )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # MCQ 2: hs2015_mc9 (Variance from normal distribution)
    q2 = get_question("7", "hs2015_mc9")
    if q2:
        with st.container(border=True):
            st.caption(q2.get("source", ""))
            opts = q2.get("options", [])
            if opts and isinstance(opts[0], dict):
                option_labels = [t(o) for o in opts]
            else:
                option_labels = opts
            
            render_mcq(
                key_suffix="7_2_variance",
                question_text=t(q2["question"]),
                options=option_labels,
                correct_idx=q2["correct_idx"],
                solution_text_dict=q2["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
                client=model,
                ai_context="Calculating variance from normal distribution percentiles",
                course_id="vwl",
                topic_id="7",
                subtopic_id="7.2",
                question_id="7_2_variance"
            )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # MCQ 3: hs2023_mc4 (Variance from PDF)
    q3 = get_question("7", "hs2023_mc4")
    if q3:
        with st.container(border=True):
            st.caption(q3.get("source", ""))
            opts = q3.get("options", [])
            if opts and isinstance(opts[0], dict):
                option_labels = [t(o) for o in opts]
            else:
                option_labels = opts
            
            render_mcq(
                key_suffix="7_2_pdf_var",
                question_text=t(q3["question"]),
                options=option_labels,
                correct_idx=q3["correct_idx"],
                solution_text_dict=q3["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
                client=model,
                ai_context="Calculating variance from probability density function",
                course_id="vwl",
                topic_id="7",
                subtopic_id="7.2",
                question_id="7_2_pdf_var"
            )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # MCQ 4: test3_q3 (Variance of linear combination)
    q4 = get_question("7", "test3_q3")
    if q4:
        with st.container(border=True):
            st.caption(q4.get("source", ""))
            opts = q4.get("options", [])
            if opts and isinstance(opts[0], dict):
                option_labels = [t(o) for o in opts]
            else:
                option_labels = opts
            
            render_mcq(
                key_suffix="7_2_var_combo",
                question_text=t(q4["question"]),
                options=option_labels,
                correct_idx=q4["correct_idx"],
                solution_text_dict=q4["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
                client=model,
                ai_context="Variance of linear combination with correlation",
                course_id="vwl",
                topic_id="7",
                subtopic_id="7.2",
                question_id="7_2_var_combo"
            )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # MCQ 5: hs2023_mc9 (Covariance calculation)
    q5 = get_question("7", "hs2023_mc9")
    if q5:
        with st.container(border=True):
            st.caption(q5.get("source", ""))
            opts = q5.get("options", [])
            if opts and isinstance(opts[0], dict):
                option_labels = [t(o) for o in opts]
            else:
                option_labels = opts
            
            render_mcq(
                key_suffix="7_2_cov",
                question_text=t(q5["question"]),
                options=option_labels,
                correct_idx=q5["correct_idx"],
                solution_text_dict=q5["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
                client=model,
                ai_context="Covariance calculation with linear transformation",
                course_id="vwl",
                topic_id="7",
                subtopic_id="7.2",
                question_id="7_2_cov"
            )
