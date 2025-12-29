# Topic 6: Central Limit Theorem - Dispatcher
import streamlit as st

def render_topic_6_content(client, subtopic_id):
    """Dispatcher for Topic 6 subtopics."""
    
    if subtopic_id == "6.1":
        from topics.topic_6_1_content import render_subtopic_6_1
        render_subtopic_6_1(client)
    elif subtopic_id == "6.2":
        from topics.topic_6_2_content import render_subtopic_6_2
        render_subtopic_6_2(client)
    elif subtopic_id == "6.3":
        from topics.topic_6_3_content import render_subtopic_6_3
        render_subtopic_6_3(client)
    else:
        st.warning(f"Subtopic {subtopic_id} not found.")
