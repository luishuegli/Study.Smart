# Topic 3.4: Expected Values
import streamlit as st
from utils.localization import t

def render_subtopic_3_4(model):
    """3.4 Erwartungswerte - Expected Values"""
    
    st.header(t({"de": "3.4 Erwartungswerte von Zufallsvariablen", "en": "3.4 Expected Values of Random Variables"}))
    st.markdown("---")
    
    # --- THEORY PLACEHOLDER ---
    with st.container(border=True):
        st.markdown(f"### {t({'de': 'Theorie', 'en': 'Theory'})}")
        st.info(t({
            "de": "**Theorie-Inhalte kommen bald!**\n\nDieser Abschnitt wird theoretische Erklärungen zu Erwartungswerten enthalten.",
            "en": "**Theory content coming soon!**\n\nThis section will contain theoretical explanations of expected values."
        }))
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- EXAM SECTION ---
    st.markdown(f"### {t({'de': 'Prüfungstraining', 'en': 'Exam Practice'})}")
    
    with st.container(border=True):
        st.caption("HS 2024 Januar, MC #7")
        q1 = get_question("3.4", "hs2024_mc7")
        # Handle options
        if q1:
            opts = q1.get("options", [])
            if opts and isinstance(opts[0], dict):
                option_labels = [t(o) for o in opts]
            else:
                option_labels = opts
                
            render_mcq(
                key_suffix="3_4_mc7",
                question_text=t(q1["question"]),
                options=option_labels,
                correct_idx=q1["correct_idx"],
                solution_text_dict=q1["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Falsch.", "en": "Incorrect."},
                client=model,
                ai_context="Expected value of symmetrical PDF",
                course_id="vwl", topic_id="3", subtopic_id="3.4", question_id="3_4_mc7"
            )
            
    st.markdown("<br>", unsafe_allow_html=True)
    
    with st.container(border=True):
        st.caption("HS 2024 Januar, MC #12")
        q2 = get_question("3.4", "hs2024_mc12")
        if q2:
            opts = q2.get("options", [])
            if opts and isinstance(opts[0], dict):
                option_labels = [t(o) for o in opts]
            else:
                option_labels = opts
                
            render_mcq(
                key_suffix="3_4_mc12",
                question_text=t(q2["question"]),
                options=option_labels,
                correct_idx=q2["correct_idx"],
                solution_text_dict=q2["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Falsch.", "en": "Incorrect."},
                client=model,
                ai_context="Expected value, Wald's identity",
                course_id="vwl", topic_id="3", subtopic_id="3.4", question_id="3_4_mc12"
            )
