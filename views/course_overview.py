import streamlit as st
import utils.localization as loc
from data import COURSES

def course_overview_view():
    # Sidebar should remain visible for language toggle
    # Removed the 'display: none' CSS block
    
    course_id = st.query_params.get("course", st.session_state.get("selected_course", "vwl"))
    course = COURSES.get(course_id)
    
    if not course:
        st.error(loc.t({"de": "Kurs nicht gefunden.", "en": "Course not found."}))
        if st.button(loc.t({"de": "Zurück zum Dashboard", "en": "Back to Dashboard"})):
            st.session_state.current_page = "dashboard"
            st.rerun()
        return

    # Back Navigation
    if st.button(f"← {loc.t({'de': 'Zurück zum Dashboard', 'en': 'Back to Dashboard'})}", type="secondary"):
        st.session_state.current_page = "dashboard"
        st.rerun()

    st.title(course["title"])
    
    # Global Progress
    st.markdown(f"**{loc.t({'de': 'Mein Gesamtfortschritt', 'en': 'My Total Progress'})}:** {int(course['progress'] * 100)}%")
    st.progress(course["progress"])
    
    st.markdown("---")
    
    st.subheader(loc.t({"de": "Themen", "en": "Topics"}))
    
    # List Topics
    for topic in course["topics"]:
        with st.expander(f"{loc.t(topic['title'])} ({topic['status']})", expanded=True):
            col1, col2 = st.columns([3, 1])
            with col1:
                st.markdown(loc.t({
                    "de": "Hier finden Sie Vorlesungen, Übungen und Prüfungen zu diesem Thema.",
                    "en": "Here you will find lectures, exercises, and exams related to this topic."
                }))
                # Fake progress sliders for visual effect
                st.caption(loc.t({"de": "Bearbeitet:", "en": "Completed:"}))
                st.progress(0.1 if topic['status'] == 'in_progress' else 0.0)
                st.caption(loc.t({"de": "Verstanden:", "en": "Understood:"}))
                st.progress(0.0)
                
            with col2:
                if topic['status'] == 'locked':
                    st.button(loc.t({"de": "Gesperrt", "en": "Locked"}), key=topic['id'], disabled=True)
                else:
                    if st.button(loc.t({"de": "Lernen starten", "en": "Start Learning"}), key=topic['id'], type="primary"):
                        st.session_state.current_page = "lesson"
                        st.session_state.selected_topic = topic['id']
                        st.rerun()
