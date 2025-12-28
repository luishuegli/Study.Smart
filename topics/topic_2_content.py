import streamlit as st
from utils.localization import t

# --- CONTENT DICTIONARY ---
content_2 = {
    "title": {"de": "2. Elementare Kombinatorik", "en": "2. Elementary Combinatorics"}
}

# --- MAIN DISPATCHER ---
def render_topic_2_content(client, subtopic_id=None):
    if subtopic_id == "2.1":
        from topics.topic_2_1_content import render_subtopic_2_1
        render_subtopic_2_1(client)
    elif subtopic_id == "2.2":
        from topics.topic_2_2_content import render_subtopic_2_2
        render_subtopic_2_2(client)
    elif subtopic_id == "2.3":
        from topics.topic_2_3_content import render_subtopic_2_3
        render_subtopic_2_3(client)
    else:
        st.info(t({
            "de": "🚀 Dieser Abschnitt ist noch in Entwicklung. Schau bald wieder vorbei!",
            "en": "🚀 This section is still in development. Check back soon!"
        }))
