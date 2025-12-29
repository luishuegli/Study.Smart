# Topic 8.2: Properties of Point Estimations
import streamlit as st
from utils.localization import t
from utils.quiz_helper import render_mcq
from data.exam_questions import get_question

def render_subtopic_8_2(model):
    """8.2 Eigenschaften von Punktschätzungen"""
    
    st.header(t({"de": "8.2 Eigenschaften von Punktschätzungen", "en": "8.2 Properties of Point Estimations"}))
    st.markdown("---")
    
    # --- THEORY PLACEHOLDER ---
    with st.container(border=True):
        st.markdown(f"### {t({'de': 'Theorie', 'en': 'Theory'})}")
        st.info(t({
            "de": "**Theorie-Inhalte kommen bald!**\n\nDieser Abschnitt wird theoretische Erklärungen enthalten:\n\n• Erwartungstreue (Unbiasedness)\n• Effizienz\n• Konsistenz",
            "en": "**Theory content coming soon!**\n\nThis section will contain theoretical explanations:\n\n• Unbiasedness\n• Efficiency\n• Consistency"
        }))
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- EXAM SECTION ---
    st.markdown(f"### {t({'de': 'Prüfungstraining', 'en': 'Exam Practice'})}")
    
    # MCQ 1: hs2023_mc10 (Unbiased estimator)
    q1 = get_question("8", "hs2023_mc10")
    if q1:
        with st.container(border=True):
            st.caption(q1.get("source", ""))
            opts = q1.get("options", [])
            if opts and isinstance(opts[0], dict):
                option_labels = [t(o) for o in opts]
            else:
                option_labels = opts
            
            render_mcq(
                key_suffix="8_2_unbiased",
                question_text=t(q1["question"]),
                options=option_labels,
                correct_idx=q1["correct_idx"],
                solution_text_dict=q1["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
                client=model,
                ai_context="Identifying unbiased estimators",
                course_id="vwl",
                topic_id="8",
                subtopic_id="8.2",
                question_id="8_2_unbiased"
            )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # MCQ 2: hs2015_mc10 (Consistency vs unbiasedness)
    q2 = get_question("8", "hs2015_mc10")
    if q2:
        with st.container(border=True):
            st.caption(q2.get("source", ""))
            opts = q2.get("options", [])
            if opts and isinstance(opts[0], dict):
                option_labels = [t(o) for o in opts]
            else:
                option_labels = opts
            
            render_mcq(
                key_suffix="8_2_consistency",
                question_text=t(q2["question"]),
                options=option_labels,
                correct_idx=q2["correct_idx"],
                solution_text_dict=q2["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
                client=model,
                ai_context="Distinguishing between unbiasedness and consistency",
                course_id="vwl",
                topic_id="8",
                subtopic_id="8.2",
                question_id="8_2_consistency"
            )
