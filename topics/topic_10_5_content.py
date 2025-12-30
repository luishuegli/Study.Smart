import streamlit as st
from utils.localization import t
from utils.quiz_helper import render_mcq
from data.exam_questions import get_question

def render_subtopic_10_5(model):
    """10.5 Practice Problems"""
    
    st.header(t({"de": "10.5 Übungsaufgaben", "en": "10.5 Practice Problems"}))
    st.markdown("---")
    
    st.markdown(t({
        "de": "Berechnungsaufgaben zu Z-Tests, p-Wert und Power.",
        "en": "Calculation problems on Z-Tests, p-value, and Power."
    }))
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Question Identifiers
    questions = [
        "uebung6_prob1", 
        "uebung6_prob2", 
        "uebung6_prob3", 
        "uebung6_prob4"
    ]
    
    for q_id in questions:
        q = get_question("10.5", q_id)
        if q:
            with st.container(border=True):
                st.markdown(f"**{t(q.get('question'))}**")
                
                # Render Solution (using special render_mcq logic or custom expander for 'problem' type)
                # Since get_question returns raw dict, we need to handle rendering.
                # However, our design system prefers `render_mcq` even for open problems 
                # OR detailed solution blocks.
                # Let's use a simple Solution Expander as used in other "Problem" sections.
                
                with st.expander(t({"de": "Lösung anzeigen", "en": "Show Solution"})):
                    st.markdown(t(q.get("solution")))
                    
            st.markdown("<br>", unsafe_allow_html=True)
