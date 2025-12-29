# Topic 11: Interdisciplinary Problems - Dispatcher
import streamlit as st
from utils.localization import t

def render_topic_11_content(client, subtopic_id):
    """Dispatcher for Topic 11 subtopics."""
    
    if subtopic_id == "11.1" or subtopic_id is None:
        from topics.topic_11_1_content import render_subtopic_11_1
        render_subtopic_11_1(client)
    else:
        st.warning(f"Subtopic {subtopic_id} not found.")
