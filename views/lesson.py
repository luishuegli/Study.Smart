import streamlit as st
import plotly.graph_objects as go
import numpy as np
import course_config as config
from google import genai
import os
import utils.localization as loc
from data import COURSES
from exam_data import EXAM_QUESTIONS
from dotenv import load_dotenv
from views.styles import render_icon
from utils.progress_tracker import track_question_answer, get_user_progress

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    try:
        api_key = st.secrets.get("GEMINI_API_KEY")
    except (FileNotFoundError, KeyError):
        pass

if api_key:
    client = genai.Client(api_key=api_key)
else:
    client = None

def lesson_view():
    # --- GLOBAL UI RULES: EQUAL HEIGHT BOXES ---
    # --- GLOBAL UI RULES ---
    st.markdown("""
    <style>
    /* Make columns vertical flex containers */
    [data-testid="column"], [data-testid="stColumn"] {
        display: flex !important;
        flex-direction: column !important;
    }
    </style>
    """, unsafe_allow_html=True)

    # --- LOAD USER PROGRESS ---
    from utils.progress_tracker import get_user_progress
    user = st.session_state.get("user")
    course_id = st.session_state.get("selected_course", "vwl")
    
    if user and "localId" in user:
        # We store it in session state so it's accessible by components
        if "user_progress" not in st.session_state or st.session_state.get("last_progress_load") != course_id:
            st.session_state["user_progress"] = get_user_progress(user["localId"], course_id)
            st.session_state["last_progress_load"] = course_id

    # --- INITIALIZE NAVIGATION STATE (if not set) ---
    course = COURSES.get(course_id)
    if "selected_topic" not in st.session_state:
        if course and course["topics"]:
            st.session_state.selected_topic = course["topics"][0]["id"]
            
    if "selected_subtopic" not in st.session_state:
        current_topic_id = st.session_state.get("selected_topic")
        if course:
            topic = next((t for t in course["topics"] if t["id"] == current_topic_id), None)
            if topic and topic.get("subtopics"):
                first_sub = topic["subtopics"][0]
                st.session_state.selected_subtopic = first_sub["id"]
                st.session_state.current_slide_num = first_sub.get("slide_start", 0)
            else:
                st.session_state.selected_subtopic = None
    
    # --- NAVIGATION HANDLER ---
    def navigate_to_subtopic(topic_id, subtopic_id):
        """Centralized handler for all course navigation."""
        st.session_state.selected_topic = topic_id
        st.session_state.selected_subtopic = subtopic_id
        
        # Determine slide number
        c = COURSES.get(st.session_state.get("selected_course", "vwl"))
        t = next((x for x in c["topics"] if x["id"] == topic_id), None)
        if t:
            s = next((x for x in t["subtopics"] if x["id"] == subtopic_id), None)
            if s and "slide_start" in s:
                st.session_state.current_slide_num = s["slide_start"]
        
        # Clear radio state to prevent lag (forces radio to use 'index' based on new selection)
        radio_key = f"radio_{topic_id}"
        if radio_key in st.session_state:
            del st.session_state[radio_key]
            
        st.rerun()

    # --- SIDEBAR NAVIGATION ---
    with st.sidebar:
        # 1. Back Button at Field Top
        if st.button(f"← {loc.t({'de': 'Zurück zum Dashboard', 'en': 'Back to Dashboard'})}", use_container_width=True):
            st.session_state.current_page = "dashboard"
            st.session_state.selected_topic = None
            st.session_state.selected_subtopic = None
            st.rerun()
        
        # --- COURSE LEVEL PROGRESS ---
        overall_completed = st.session_state.get("overall_course_progress", 0.0)
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(f"**{loc.t({'de': 'Gesamtfortschritt', 'en': 'Total Progress'})}:** {int(overall_completed * 100)}%")
        st.progress(overall_completed)
        
        st.markdown("---")
        
        st.markdown(f"<h2>{render_icon('book')} &nbsp; {loc.t({'de': 'Kursnavigation', 'en': 'Course Navigation'})}</h2>", unsafe_allow_html=True)
        # Custom CSS to reduce padding and make radio buttons look like a list
        
        
        current_course_id = st.session_state.get("selected_course", "vwl")
        course = COURSES.get(current_course_id)
        
        if course:
            st.subheader(loc.t(course["title"]))
            
            # Define callback to handle selection
            def on_subtopic_change(topic_id, sub_map, key):
                selected_title = st.session_state[key]
                selected_id = sub_map[selected_title]
                # Use the centralized handler (but without rerun here as on_change already triggers it)
                # However, for consistency and to handle the 'lag', we'll just set the state
                st.session_state.selected_topic = topic_id
                st.session_state.selected_subtopic = selected_id
                
                # Retrieve course content to find slide
                c = COURSES.get(st.session_state.get("selected_course", "vwl"))
                t = next((x for x in c["topics"] if x["id"] == topic_id), None)
                if t:
                    s = next((x for x in t["subtopics"] if x["id"] == selected_id), None)
                    if s and "slide_start" in s:
                        st.session_state.current_slide_num = s["slide_start"]
                    # If it's a new topic, ensure subtopic is updated immediately for query param sync
                    st.session_state.selected_topic = topic_id
                    st.session_state.selected_subtopic = selected_id

            current_topic_id = st.session_state.get("selected_topic")
            current_sub_id = st.session_state.get("selected_subtopic")
            
            for topic in course["topics"]:
                # Logic: Expand if it contains the selected subtopic OR if it's the selected topic
                is_expanded = (topic["id"] == current_topic_id)
                
                with st.expander(loc.t(topic['title']), expanded=is_expanded):
                    subtopics = topic.get("subtopics", [])
                    if subtopics:
                        # Translate titles for the map
                        # --- PROGRESS LABELS ---
                        from views.course_overview import SUBTOPIC_QUESTION_COUNTS
                        user_progress = st.session_state.get("user_progress", {})
                        topic_data = user_progress.get("topics", {}).get(topic["id"].replace("topic_", ""), {})
                        subtopic_progress = topic_data.get("subtopics", {})
                        
                        dynamic_sub_titles = []
                        sub_map = {} # label -> id
                        
                        for s in subtopics:
                            s_id = s["id"]
                            base_title = loc.t(s["title"])
                            
                            # Calculate progress based on CORRECT answers
                            done_count = len(subtopic_progress.get(s_id, {}).get("correct_questions", []))
                            total_count = SUBTOPIC_QUESTION_COUNTS.get(s_id, 0)
                            
                            if total_count > 0:
                                if done_count >= total_count:
                                    # Base64 encoded version of a clean checkmark SVG
                                    checkmark_svg_b64 = "PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxOCIgaGVpZ2h0PSIxOCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9IiMzNEM3NTkiIHN0cm9rZS13aWR0aD0iMyIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48cG9seWxpbmUgcG9pbnRzPSIyMCA2IDkgMTcgNCAxMiI+PC9wb2x5bGluZT48L3N2Zz4="
                                    label = f"{base_title} ![check](data:image/svg+xml;base64,{checkmark_svg_b64})"
                                else:
                                    label = f"{base_title} ({done_count}/{total_count})"
                            else:
                                label = base_title
                            
                            dynamic_sub_titles.append(label)
                            sub_map[label] = s_id
                        
                        # Determine index based on dynamic labels
                        index = None
                        if topic["id"] == current_topic_id and current_sub_id:
                            active_title = next((k for k, v in sub_map.items() if v == current_sub_id), None)
                            if active_title in dynamic_sub_titles:
                                index = dynamic_sub_titles.index(active_title)
                        
                        # Radio Key
                        radio_key = f"radio_{topic['id']}"
                        
                        st.radio(
                            "Subtopics", 
                            dynamic_sub_titles, 
                            index=index,
                            key=radio_key, 
                            label_visibility="collapsed",
                            on_change=on_subtopic_change,
                            args=(topic["id"], sub_map, radio_key)
                        )
        
        
        # Render sidebar footer (language selector + logout)
        loc.render_sidebar_footer()

    # --- MAIN CONTENT ---
    topic_id = st.session_state.get("selected_topic", "topic_1") # Default to Topic 1
    subtopic_id = st.session_state.get("selected_subtopic")
    
    # Render Content
    render_topic_content(client, topic_id, subtopic_id)
    
    # Render Navigation
    render_navigation_buttons(current_course_id, topic_id, subtopic_id, navigate_to_subtopic)

def render_navigation_buttons(course_id, current_topic_id, current_subtopic_id, navigate_to_subtopic):
    """Renders 'Next Lesson' button at the bottom."""
    course = COURSES.get(course_id)
    if not course:
        return

    topics = course.get("topics", [])
    next_topic_id = None
    next_subtopic_id = None
    next_subtopic_title = None

    # Find current position
    for t_idx, topic in enumerate(topics):
        if topic["id"] == current_topic_id:
            subtopics = topic.get("subtopics", [])
            for s_idx, sub in enumerate(subtopics):
                if sub["id"] == current_subtopic_id:
                    # Found current subtopic. Is there a next one in this topic?
                    if s_idx + 1 < len(subtopics):
                        next_topic_id = current_topic_id
                        next_subtopic_id = subtopics[s_idx + 1]["id"]
                        next_subtopic_title = loc.t(subtopics[s_idx + 1]["title"])
                    # No more subtopics in this topic. Is there a next topic?
                    elif t_idx + 1 < len(topics):
                        next_topic = topics[t_idx + 1]
                        next_topic_id = next_topic["id"]
                        next_subs = next_topic.get("subtopics", [])
                        if next_subs:
                            next_subtopic_id = next_subs[0]["id"]
                            next_subtopic_title = loc.t(next_subs[0]["title"])
                    break
            break

    if next_topic_id and next_subtopic_id:
        st.markdown("<br><br>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            button_label = f"{loc.t({'de': 'Nächste Lektion', 'en': 'Next Lesson'})}: {next_subtopic_title} →"
            if st.button(button_label, use_container_width=True, type="primary"):
                navigate_to_subtopic(next_topic_id, next_subtopic_id)


def render_topic_content(client, topic_id, subtopic_id):
    # Retrieve Topic Data
    course = COURSES.get(st.session_state.get("selected_course", "vwl"))
    topic = next((t for t in course["topics"] if t["id"] == topic_id), None)
    
    if not topic:
        st.error(f"Topic not found: {topic_id}")
        return

    st.title(loc.t(topic["title"]))
    if subtopic_id:
        sub = next((s for s in topic["subtopics"] if s["id"] == subtopic_id), None)
        if sub:
            st.caption(f"{loc.t({'de': 'Abschnitt', 'en': 'Section'})}: {loc.t(sub['title'])}")

    # Check if this is Topic 1 or Topic 2 with interactive content
    if topic_id == "topic_1":
        # Import interactive content module
        try:
            from topics.topic_1_content import render_topic_1_content
            
            # Render content directly without tabs
            render_topic_1_content(client, subtopic_id)
                
        except ImportError as e:
            st.error(f"Interactive content not available: {str(e)}")
            
    elif topic_id == "topic_2":
        try:
            from topics.topic_2_content import render_topic_2_content
            render_topic_2_content(client, subtopic_id)
        except ImportError as e:
            st.error(f"Interactive content not available: {str(e)}")
    else:
        # Other topics: Show practice questions only
        st.subheader("Exam Questions")
        # Placeholder: Fetch questions for this topic specifically
        # For now, show "Descriptive Stats" questions if Topic 7, else generic
        questions = EXAM_QUESTIONS.get("descr_stats", []) if topic_id == "topic_7" else []
        
        if questions:
            for q in questions:
                render_exam_question(q, client)
        else:
            st.info("No practice questions added for this topic yet.")


def render_exam_question(q, client):
    st.markdown(f"**{ q['source'] }**")
    st.markdown(q['question_text'])
    
    qid = q['id']
    if f"{qid}_submitted" not in st.session_state:
        st.session_state[f"{qid}_submitted"] = False
        st.session_state[f"{qid}_correct"] = False

    opts = q['options']
    user_choice = st.radio("Choose:", list(opts.keys()), format_func=lambda x: f"{x}: {opts[x]}", key=f"{qid}_radio", disabled=st.session_state[f"{qid}_submitted"])

    if not st.session_state[f"{qid}_submitted"]:
        if st.button("Submit", key=f"{qid}_btn"):
            st.session_state[f"{qid}_submitted"] = True
            is_correct = (user_choice == q['correct_answer'])
            st.session_state[f"{qid}_correct"] = is_correct
            
            # Track progress
            user = st.session_state.get("user")
            course_id = st.session_state.get("selected_course", "vwl")
            topic_id = st.session_state.get("selected_topic", "topic_1").replace("topic_", "")
            subtopic_id = st.session_state.get("selected_subtopic", "unknown")
            
            if user and "localId" in user:
                track_question_answer(
                    user_id=user["localId"],
                    course_id=course_id,
                    topic_id=topic_id,
                    subtopic_id=subtopic_id,
                    question_id=qid,
                    is_correct=is_correct
                )
            st.rerun()
    else:
        if st.session_state[f"{qid}_correct"]:
            st.success(loc.t({"de": "Richtig!", "en": "Correct!"}))
        else:
            st.error(loc.t({"de": "Falsch.", "en": "Incorrect."}))
            if st.button("Retry", key=f"{qid}_retry"):
                 st.session_state[f"{qid}_submitted"] = False
                 st.rerun()
        
        with st.expander("Master Solution", expanded=True):
            st.markdown(q['solution_text'])
