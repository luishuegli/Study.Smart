# Topic 9: Confidence Intervals - Dispatcher
import streamlit as st

def render_topic_9_content(client, subtopic_id):
    """Dispatcher for Topic 9 subtopics."""
    
    if subtopic_id == "9.1":
        from topics.topic_9_1_content import render_subtopic_9_1
        render_subtopic_9_1(client)
    elif subtopic_id == "9.2":
        from topics.topic_9_2_content import render_subtopic_9_2
        render_subtopic_9_2(client)
    elif subtopic_id == "9.3":
        from topics.topic_9_3_content import render_subtopic_9_3
        render_subtopic_9_3(client)
    else:
        st.warning(f"Subtopic {subtopic_id} not found.")
