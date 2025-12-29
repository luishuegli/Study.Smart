# Topic 7: Descriptive Statistics - Dispatcher
import streamlit as st

def render_topic_7_content(client, subtopic_id):
    """Dispatcher for Topic 7 subtopics."""
    
    if subtopic_id == "7.1":
        from topics.topic_7_1_content import render_subtopic_7_1
        render_subtopic_7_1(client)
    elif subtopic_id == "7.2":
        from topics.topic_7_2_content import render_subtopic_7_2
        render_subtopic_7_2(client)
    elif subtopic_id == "7.3":
        from topics.topic_7_3_content import render_subtopic_7_3
        render_subtopic_7_3(client)
    elif subtopic_id == "7.4":
        from topics.topic_7_4_content import render_subtopic_7_4
        render_subtopic_7_4(client)
    elif subtopic_id == "7.5":
        from topics.topic_7_5_content import render_subtopic_7_5
        render_subtopic_7_5(client)
    elif subtopic_id == "7.6":
        from topics.topic_7_6_content import render_subtopic_7_6
        render_subtopic_7_6(client)
    else:
        st.warning(f"Subtopic {subtopic_id} not found.")
