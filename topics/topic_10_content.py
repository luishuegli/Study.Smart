import streamlit as st
from utils.localization import t
from utils.layouts.foundation import grey_info

def render_topic_10_content(model, subtopic_id):
    """Topic 10: Hypothesis Testing (Hypothesentests) — Router"""
    
    # Import subtopic renderers
    from topics.topic_10_1_content import render_subtopic_10_1
    from topics.topic_10_2_content import render_subtopic_10_2
    from topics.topic_10_3_content import render_subtopic_10_3
    from topics.topic_10_4_content import render_subtopic_10_4
    from topics.topic_10_5_content import render_subtopic_10_5
    
    # Route to subtopic
    subtopic_map = {
        "10.1": render_subtopic_10_1,
        "10.2": render_subtopic_10_2,
        "10.3": render_subtopic_10_3,
        "10.4": render_subtopic_10_4,
        "10.5": render_subtopic_10_5,
    }
    
    if subtopic_id in subtopic_map:
        subtopic_map[subtopic_id](model)
    else:
        # Default: Show topic overview
        st.header(t({"de": "10. Hypothesentests", "en": "10. Hypothesis Testing"}))
        st.markdown("---")
        
        grey_info(t({
            "de": "In diesem Kapitel lernen wir, wie man statistische Entscheidungen trifft. Wir behandeln Z-Tests, p-Werte und die Macht (Power) eines Tests.",
            "en": "In this chapter, we learn how to make statistical decisions. We cover Z-Tests, p-values, and the Power of a test."
        }))
        
        st.info(t({
            "de": "Bitte wähle einen Abschnitt aus dem Menü links.",
            "en": "Please select a section from the menu on the left."
        }))


# Legacy function name for backward compatibility
def render_topic_10(model):
    """Legacy entry point - render overview when no subtopic selected."""
    render_topic_10_content(model, None)
