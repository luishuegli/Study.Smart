import streamlit as st
import utils.localization as loc
from data import COURSES
from utils.progress_tracker import get_user_progress

# Define total questions per subtopic for progress calculation
SUBTOPIC_QUESTION_COUNTS = {
    "1.1": 1,  # q_1_1_stetig
    "1.2": 3,  # 1_2_A, 1_2_B, 1_2_C (Mission removed)
    "1.3": 1,  # 1_3_exam
    "1.4": 1,  # 1_4_exam
    "1.5": 2,  # 1_5_exam + Market Analyst Mission
    "1.6": 2,  # p_single_point, 1_6_dart_mission
    "1.7": 4,  # 1_7_q1_narrative, 1_7_q2_narrative, 1_7_narrative_mission, 1_7_balance_mission
    "1.8": 2,  # 1_8_factory, 1_8_mission
    "1.9": 3,  # 1_9_prisoners, 1_9_medical_mission, 1_9_search_mission
    "1.10": 6, # exam_l1 to exam_l6
    "2.1": 1,  # q_2_1_scenario_mastery
    "2.2": 1,  # q_2_2_club
}

def calculate_topic_progress(topic_data, subtopic_ids):
    """Calculate overall topic completion percentage from all its subtopics."""
    total_completed = 0
    total_questions = 0
    
    for subtopic_id in subtopic_ids:
        question_count = SUBTOPIC_QUESTION_COUNTS.get(subtopic_id, 0)
        if question_count == 0:
            continue
            
        total_questions += question_count
        
        subtopics = topic_data.get("subtopics", {})
        if subtopic_id in subtopics:
            subtopic = subtopics[subtopic_id]
            total_completed += len(subtopic.get("correct_questions", []))
    
    if total_questions == 0:
        return 0.0
    
    # Clamp to 1.0 incase of ghost data (e.g., renamed ids)
    return min(1.0, total_completed / total_questions)

def course_overview_view():
    # Add sidebar footer

    # Sidebar: Back Button + Spacer + Footer
    with st.sidebar:
        if st.button(f"← {loc.t({'de': 'Zurück zum Dashboard', 'en': 'Back to Dashboard'})}", use_container_width=True):
            st.session_state.current_page = "dashboard"
            st.rerun()
            
        loc.render_sidebar_footer()

    course_id = st.query_params.get("course", st.session_state.get("selected_course", "vwl"))
    course = COURSES.get(course_id)
    
    if not course:
        st.error(loc.t({"de": "Kurs nicht gefunden.", "en": "Course not found."}))
        if st.button(loc.t({"de": "Zurück zum Dashboard", "en": "Back to Dashboard"}), key="co_back_error"):
            st.session_state.current_page = "dashboard"
            st.rerun()
        return

    # Load user progress from Firestore
    user = st.session_state.get("user")
    user_progress = {}
    if user and "localId" in user:
        user_id = user["localId"]
        user_progress = get_user_progress(user_id, course_id)

    st.title(course["title"])
    
    # Calculate overall course progress
    overall_completed = 0.0
    topic_count = 0
    
    for topic in course["topics"]:
        topic_id = topic["id"].replace("topic_", "")  # "topic_1" -> "1"
        subtopic_ids = [st["id"] for st in topic.get("subtopics", [])]
        
        # Get topic data from progress
        topics_data = user_progress.get("topics", {})
        topic_data = topics_data.get(topic_id, {})
        
        # Calculate progress for this topic
        completed_pct = calculate_topic_progress(topic_data, subtopic_ids)
        overall_completed += completed_pct
        topic_count += 1
    
    # Average across all topics
    if topic_count > 0:
        overall_completed /= topic_count
    
    # Store in session state for sidebar/dashboard sync
    st.session_state["overall_course_progress"] = overall_completed
    
    # Global Progress
    st.markdown(f"**{loc.t({'de': 'Mein Gesamtfortschritt', 'en': 'My Total Progress'})}:** {int(overall_completed * 100)}%")
    st.progress(overall_completed)
    
    st.markdown("---")
    
    st.subheader(loc.t({"de": "Themen", "en": "Topics"}))
    
    # List Topics
    for topic in course["topics"]:
        topic_id = topic["id"].replace("topic_", "")
        subtopic_ids = [st["id"] for st in topic.get("subtopics", [])]
        
        # Get topic data from progress
        topics_data = user_progress.get("topics", {})
        topic_data = topics_data.get(topic_id, {})
        
        # Calculate progress
        completed_pct = calculate_topic_progress(topic_data, subtopic_ids)
        
        # Determine status based on progress
        if completed_pct >= 1.0:
            status = "completed"
        elif completed_pct > 0:
            status = "in_progress"
        else:
            status = topic.get("status", "open")
        
        # Prepare Header Label
        base_title = loc.t(topic['title'])
        header_label = base_title
        
        if status == "completed":
            # Clean SVG checkmark (same as sidebar)
            checkmark_svg_b64 = "PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxOCIgaGVpZ2h0PSIxOCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9IiMzNEM3NTkiIHN0cm9rZS13aWR0aD0iMyIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48cG9seWxpbmUgcG9pbnRzPSIyMCA2IDkgMTcgNCAxMiI+PC9wb2x5bGluZT48L3N2Zz4="
            header_label = f"{base_title} ![check](data:image/svg+xml;base64,{checkmark_svg_b64})"
        elif status == "in_progress":
            header_label = f"{base_title} ({int(completed_pct * 100)}%)"
        
        with st.expander(header_label, expanded=True):
            col1, col2 = st.columns([3, 1])
            with col1:
                st.markdown(loc.t({
                    "de": "Hier finden Sie Vorlesungen, Übungen und Prüfungen zu diesem Thema.",
                    "en": "Here you will find lectures, exercises, and exams related to this topic."
                }))
                # Progress bar
                st.caption(loc.t({"de": "Fortschritt:", "en": "Progress:"}))
                st.progress(completed_pct)
                
            with col2:
                if status == 'locked':
                    st.button(loc.t({"de": "Gesperrt", "en": "Locked"}), key=topic['id'], disabled=True)
                else:
                    if st.button(loc.t({"de": "Lernen starten", "en": "Start Learning"}), key=topic['id'], type="primary"):
                        st.session_state.current_page = "lesson"
                        st.session_state.selected_topic = topic['id']
                        st.rerun()
