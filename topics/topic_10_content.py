import streamlit as st
from utils.localization import t
from topics.topic_10_5_content import render_subtopic_10_5

def render_topic_10(model):
    """Topic 10: Hypothesis Testing (Hypothesentests)"""
    
    st.header(t({"de": "10. Hypothesentests", "en": "10. Hypothesis Testing"}))
    st.markdown("---")
    
    st.info(t({
        "de": "In diesem Kapitel lernen wir, wie man statistische Entscheidungen trifft. Wir behandeln Z-Tests, p-Werte und die Macht (Power) eines Tests.",
        "en": "In this chapter, we learn how to make statistical decisions. We cover Z-Tests, p-values, and the Power of a test."
    }))
    
    # Subtopic Selection Tabs
    tab1, = st.tabs([
        t({"de": "10.5 Übungsaufgaben", "en": "10.5 Exercises"})
    ])
    
    with tab1:
        render_subtopic_10_5(model)
