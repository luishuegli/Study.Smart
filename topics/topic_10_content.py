# Topic 10: Hypothesis Tests - Dispatcher
import streamlit as st

def render_topic_10_content(client, subtopic_id):
    """Dispatcher for Topic 10 subtopics."""
    
    if subtopic_id == "10.1":
        from topics.topic_10_1_content import render_subtopic_10_1
        render_subtopic_10_1(client)
    elif subtopic_id == "10.2":
        from topics.topic_10_2_content import render_subtopic_10_2
        render_subtopic_10_2(client)
    elif subtopic_id == "10.3":
        from topics.topic_10_3_content import render_subtopic_10_3
        render_subtopic_10_3(client)
    elif subtopic_id == "10.4":
        from topics.topic_10_4_content import render_subtopic_10_4
        render_subtopic_10_4(client)
    elif subtopic_id == "10.5":
        from topics.topic_10_5_content import render_subtopic_10_5
        render_subtopic_10_5(client)
    else:
        st.warning(f"Subtopic {subtopic_id} not found.")
