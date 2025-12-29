# Topic 3: Random Variables - Dispatcher
# Routes to specific subtopic renderers

import streamlit as st

def render_topic_3_content(client, subtopic_id):
    """Dispatcher for Topic 3 subtopics."""
    
    if subtopic_id == "3.1":
        from topics.topic_3_1_content import render_subtopic_3_1
        render_subtopic_3_1(client)
    elif subtopic_id == "3.2":
        from topics.topic_3_2_content import render_subtopic_3_2
        render_subtopic_3_2(client)
    elif subtopic_id == "3.3":
        from topics.topic_3_3_content import render_subtopic_3_3
        render_subtopic_3_3(client)
    elif subtopic_id == "3.4":
        from topics.topic_3_4_content import render_subtopic_3_4
        render_subtopic_3_4(client)
    elif subtopic_id == "3.5":
        from topics.topic_3_5_content import render_subtopic_3_5
        render_subtopic_3_5(client)
    elif subtopic_id == "3.6":
        from topics.topic_3_6_content import render_subtopic_3_6
        render_subtopic_3_6(client)
    elif subtopic_id == "3.7":
        from topics.topic_3_7_content import render_subtopic_3_7
        render_subtopic_3_7(client)
    else:
        st.warning(f"Subtopic {subtopic_id} not found.")
