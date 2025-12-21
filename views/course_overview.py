import streamlit as st
from data import COURSES

def course_overview_view():
    # Hide sidebar on course overview as it's empty and provides no value
    st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            display: none;
        }
    </style>
    """, unsafe_allow_html=True)
    
    course_id = st.query_params.get("course", st.session_state.get("selected_course", "vwl"))
    course = COURSES.get(course_id)
    
    if not course:
        st.error("Course not found.")
        if st.button("Back to Dashboard"):
            st.session_state.current_page = "dashboard"
            st.rerun()
        return

    # Back Navigation
    if st.button("← Back to Dashboard", type="secondary"):
        st.session_state.current_page = "dashboard"
        st.rerun()

    st.title(course["title"])
    
    # Global Progress
    st.markdown(f"**Mein Gesamtfortschritt:** {int(course['progress'] * 100)}%")
    st.progress(course["progress"])
    
    st.markdown("---")
    
    st.subheader("Themen / Topics")
    
    # List Topics
    for topic in course["topics"]:
        with st.expander(f"{topic['title']} ({topic['status']})", expanded=True):
            col1, col2 = st.columns([3, 1])
            with col1:
                st.markdown("Here you will find lectures, exercises, and exams related to this topic.")
                # Fake progress sliders for visual effect
                st.caption("Bearbeitet:")
                st.progress(0.1 if topic['status'] == 'in_progress' else 0.0)
                st.caption("Verstanden:")
                st.progress(0.0)
                
            with col2:
                if topic['status'] == 'locked':
                    st.button("Locked", key=topic['id'], disabled=True)
                else:
                    if st.button("Start Learning", key=topic['id'], type="primary"):
                        st.session_state.current_page = "lesson"
                        st.session_state.selected_topic = topic['id']
                        st.rerun()
