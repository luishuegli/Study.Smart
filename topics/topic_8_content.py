# Topic 8: Point Estimation - Dispatcher
import streamlit as st

def render_topic_8_content(client, subtopic_id):
    """Dispatcher for Topic 8 subtopics."""
    
    if subtopic_id == "8.1":
        from topics.topic_8_1_content import render_subtopic_8_1
        render_subtopic_8_1(client)
    elif subtopic_id == "8.2":
        from topics.topic_8_2_content import render_subtopic_8_2
        render_subtopic_8_2(client)
    elif subtopic_id == "8.3":
        from topics.topic_8_3_content import render_subtopic_8_3
        render_subtopic_8_3(client)
    elif subtopic_id == "8.4":
        from topics.topic_8_4_content import render_subtopic_8_4
        render_subtopic_8_4(client)
    else:
        st.warning(f"Subtopic {subtopic_id} not found.")
