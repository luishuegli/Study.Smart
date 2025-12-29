# Topic 3.5: Variance
import streamlit as st
from utils.localization import t
from utils.quiz_helper import render_mcq
from data.exam_questions import get_question

def render_subtopic_3_5(model):
    """3.5 Varianz - Variance"""
    
    st.header(t({"de": "3.5 Varianz", "en": "3.5 Variance"}))
    st.markdown("---")
    
    # --- THEORY PLACEHOLDER ---
    with st.container(border=True):
        st.markdown(f"### {t({'de': 'Theorie', 'en': 'Theory'})}")
        st.info(t({
            "de": "📚 **Theorie-Inhalte kommen bald!**\n\nDieser Abschnitt wird theoretische Erklärungen zur Varianz enthalten.",
            "en": "📚 **Theory content coming soon!**\n\nThis section will contain theoretical explanations of variance."
        }))
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- EXAM SECTION ---
    st.markdown(f"### {t({'de': 'Prüfungstraining', 'en': 'Exam Practice'})}")
    
    # MCQ 1: uebung2_mc8
    q_data = get_question("3.5", "uebung2_mc8")
    if q_data:
        with st.container(border=True):
            st.caption(q_data.get("source", ""))
            
            opts = q_data.get("options", [])
            if opts and isinstance(opts[0], dict) and ('de' in opts[0] or 'en' in opts[0]):
                option_labels = [t(o) for o in opts]
            else:
                option_labels = opts
            
            render_mcq(
                key_suffix="3_5_mc8",
                question_text=t(q_data["question"]),
                options=option_labels,
                correct_idx=q_data["correct_idx"],
                solution_text_dict=q_data["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
                client=model,
                ai_context="Variance calculation",
                course_id="vwl",
                topic_id="3",
                subtopic_id="3.5",
                question_id="3_5_mc8"
            )
