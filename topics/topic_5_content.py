# Topic 5: Multidimensional Random Variables - Dispatcher
import streamlit as st

def render_topic_5_content(client, subtopic_id):
    """Dispatcher for Topic 5 subtopics."""
    
    if subtopic_id == "5.1":
        from topics.topic_5_1_content import render_subtopic_5_1
        render_subtopic_5_1(client)
    elif subtopic_id == "5.2":
        from topics.topic_5_2_content import render_subtopic_5_2
        render_subtopic_5_2(client)
    elif subtopic_id == "5.3":
        from topics.topic_5_3_content import render_subtopic_5_3
        render_subtopic_5_3(client)
    elif subtopic_id == "5.4":
        from topics.topic_5_4_content import render_subtopic_5_4
        render_subtopic_5_4(client)
    elif subtopic_id == "5.5":
        from topics.topic_5_5_content import render_subtopic_5_5
        render_subtopic_5_5(client)
    else:
        st.warning(f"Subtopic {subtopic_id} not found.")
