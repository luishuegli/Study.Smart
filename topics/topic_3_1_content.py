# Topic 3.1: Distribution Function
import streamlit as st
from utils.localization import t
from utils.quiz_helper import render_mcq
from data.exam_questions import get_question

def render_subtopic_3_1(model):
    """3.1 Die Verteilungsfunktion - Distribution Function"""
    
    st.header(t({"de": "3.1 Die Verteilungsfunktion", "en": "3.1 Distribution Function"}))
    st.markdown("---")
    
    # --- THEORY PLACEHOLDER ---
    with st.container(border=True):
        st.markdown(f"### {t({'de': 'Theorie', 'en': 'Theory'})}")
        st.info(t({
            "de": "📚 **Theorie-Inhalte kommen bald!**\n\nDieser Abschnitt wird theoretische Erklärungen zur Verteilungsfunktion enthalten.",
            "en": "📚 **Theory content coming soon!**\n\nThis section will contain theoretical explanations of distribution functions."
        }))
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- EXAM SECTION ---
    st.markdown(f"### {t({'de': 'Prüfungstraining', 'en': 'Exam Practice'})}")
    
    # MCQ 1: uebung2_mc6
    q_data = get_question("3.1", "uebung2_mc6")
    if q_data:
        with st.container(border=True):
            st.caption(q_data.get("source", ""))
            
            # Handle bilingual options
            opts = q_data.get("options", [])
            if opts and isinstance(opts[0], dict) and ('de' in opts[0] or 'en' in opts[0]):
                option_labels = [t(o) for o in opts]
            else:
                option_labels = opts
            
            render_mcq(
                key_suffix="3_1_mc6",
                question_text=t(q_data["question"]),
                options=option_labels,
                correct_idx=q_data["correct_idx"],
                solution_text_dict=q_data["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
                client=model,
                ai_context="Distribution function definition",
                course_id="vwl",
                topic_id="3",
                subtopic_id="3.1",
                question_id="3_1_mc6"
            )
