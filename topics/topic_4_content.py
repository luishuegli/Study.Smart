# Topic 4: Stochastic Models and Special Distributions - Dispatcher
import streamlit as st

def render_topic_4_content(client, subtopic_id):
    """Dispatcher for Topic 4 subtopics."""
    
    if subtopic_id == "4.1":
        from topics.topic_4_1_content import render_subtopic_4_1
        render_subtopic_4_1(client)
    elif subtopic_id == "4.2":
        from topics.topic_4_2_content import render_subtopic_4_2
        render_subtopic_4_2(client)
    elif subtopic_id == "4.3":
        from topics.topic_4_3_content import render_subtopic_4_3
        render_subtopic_4_3(client)
    elif subtopic_id == "4.4":
        from topics.topic_4_4_content import render_subtopic_4_4
        render_subtopic_4_4(client)
    elif subtopic_id == "4.5":
        from topics.topic_4_5_content import render_subtopic_4_5
        render_subtopic_4_5(client)
    elif subtopic_id == "4.6":
        from topics.topic_4_6_content import render_subtopic_4_6
        render_subtopic_4_6(client)
    elif subtopic_id == "4.7":
        from topics.topic_4_7_content import render_subtopic_4_7
        render_subtopic_4_7(client)
    elif subtopic_id == "4.8":
        from topics.topic_4_8_content import render_subtopic_4_8
        render_subtopic_4_8(client)
    else:
        st.warning(f"Subtopic {subtopic_id} not found.")

