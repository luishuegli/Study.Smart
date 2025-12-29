# Topic 9.2: Derivation of Confidence Intervals
import streamlit as st
from utils.localization import t
from utils.quiz_helper import render_mcq
from data.exam_questions import get_question

def render_subtopic_9_2(model):
    """9.2 Ableitung von Konfidenzintervallen (bei grossen Stichproben)"""
    
    st.header(t({"de": "9.2 Ableitung von Konfidenzintervallen", "en": "9.2 Derivation of Confidence Intervals"}))
    st.markdown("---")
    
    # --- THEORY PLACEHOLDER ---
    with st.container(border=True):
        st.markdown(f"### {t({'de': 'Theorie', 'en': 'Theory'})}")
        st.info(t({
            "de": "**Theorie-Inhalte kommen bald!**\n\nDieser Abschnitt wird theoretische Erklärungen enthalten:\n\n• KI für Erwartungswert (σ bekannt)\n• KI für Erwartungswert (σ unbekannt)\n• KI für Proportionen",
            "en": "**Theory content coming soon!**\n\nThis section will contain theoretical explanations:\n\n• CI for mean (σ known)\n• CI for mean (σ unknown)\n• CI for proportions"
        }))
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- EXAM SECTION ---
    st.markdown(f"### {t({'de': 'Prüfungstraining', 'en': 'Exam Practice'})}")
    
    # MCQ: hs2023_mc5 (Confidence interval calculation)
    q1 = get_question("8", "hs2023_mc5")
    if q1:
        with st.container(border=True):
            st.caption(q1.get("source", ""))
            opts = q1.get("options", [])
            if opts and isinstance(opts[0], dict):
                option_labels = [t(o) for o in opts]
            else:
                option_labels = opts
            
            render_mcq(
                key_suffix="9_2_ci",
                question_text=t(q1["question"]),
                options=option_labels,
                correct_idx=q1["correct_idx"],
                solution_text_dict=q1["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
                client=model,
                ai_context="Confidence interval calculation for mean with known variance",
                course_id="vwl",
                topic_id="9",
                subtopic_id="9.2",
                question_id="9_2_ci"
            )

