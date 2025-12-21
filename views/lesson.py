import streamlit as st
import plotly.graph_objects as go
import numpy as np
import course_config as config
import google.generativeai as genai
import os
from data import COURSES
from exam_data import EXAM_QUESTIONS
from dotenv import load_dotenv
from views.styles import render_icon

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.0-flash')
else:
    model = None

def lesson_view():
    # --- SIDEBAR NAVIGATION ---
    with st.sidebar:
        st.markdown(f"<h2>{render_icon('book')} &nbsp; Course Navigation</h2>", unsafe_allow_html=True)
        # Custom CSS to reduce padding and make radio buttons look like a list
        
        
        current_course_id = st.session_state.get("selected_course", "vwl")
        course = COURSES.get(current_course_id)
        
        if course:
            st.subheader(course["title"])
            
            # Define callback to handle selection
            def on_subtopic_change(topic_id, sub_map, key):
                selected_title = st.session_state[key]
                selected_id = sub_map[selected_title]
                st.session_state.selected_topic = topic_id
                st.session_state.selected_subtopic = selected_id
                
                # Retrieve course content to find slide
                c = COURSES.get(st.session_state.get("selected_course", "vwl"))
                t = next((x for x in c["topics"] if x["id"] == topic_id), None)
                if t:
                    s = next((x for x in t["subtopics"] if x["id"] == selected_id), None)
                    if s and "slide_start" in s:
                        st.session_state.current_slide_num = s["slide_start"]

            current_topic_id = st.session_state.get("selected_topic")
            current_sub_id = st.session_state.get("selected_subtopic")
            
            for topic in course["topics"]:
                # Logic: Expand if it contains the selected subtopic OR if it's the selected topic
                is_expanded = (topic["id"] == current_topic_id)
                
                with st.expander(f"{topic['title']}", expanded=is_expanded):
                    subtopics = topic.get("subtopics", [])
                    if subtopics:
                        sub_map = {s["title"]: s["id"] for s in subtopics}
                        sub_titles = list(sub_map.keys())
                        
                        # Determine index. 
                        # If this topic is NOT active, index should be None (no selection).
                        # If active, find the index of the selected subtopic.
                        index = None
                        if topic["id"] == current_topic_id and current_sub_id:
                            # Find which title corresponds to active ID
                            active_title = next((k for k, v in sub_map.items() if v == current_sub_id), None)
                            if active_title in sub_titles:
                                index = sub_titles.index(active_title)
                        
                        # Radio Key
                        radio_key = f"radio_{topic['id']}"
                        
                        st.radio(
                            "Subtopics", 
                            sub_titles, 
                            index=index,
                            key=radio_key, 
                            label_visibility="collapsed",
                            on_change=on_subtopic_change,
                            args=(topic["id"], sub_map, radio_key)
                        )
        
        st.markdown("---")
        if st.button("← Back to Dashboard"):
            st.session_state.current_page = "dashboard"
            st.rerun()

    # --- MAIN CONTENT ---
    topic_id = st.session_state.get("selected_topic", "topic_1") # Default to Topic 1
    subtopic_id = st.session_state.get("selected_subtopic")
    
    # Render Content
    render_topic_content(model, topic_id, subtopic_id)


def render_topic_content(model, topic_id, subtopic_id):
    # Retrieve Topic Data
    course = COURSES.get(st.session_state.get("selected_course", "vwl"))
    topic = next((t for t in course["topics"] if t["id"] == topic_id), None)
    
    if not topic:
        st.error(f"Topic not found: {topic_id}")
        return

    st.title(topic["title"])
    if subtopic_id:
        sub = next((s for s in topic["subtopics"] if s["id"] == subtopic_id), None)
        if sub:
            st.caption(f"Section: {sub['title']}")

    # Check if this is Topic 1 (Grundlagen) with interactive content
    if topic_id == "topic_1":
        # Import interactive content module
        try:
            from topics.topic_1_content import render_topic_1_content
            
            # Single unified view with slides as a separate tab
            tab_learn, tab_slides = st.tabs([
                "Learn & Apply",
                "Lecture Slides (Reference)"
            ])
            
            # --- TAB: UNIFIED LEARN & APPLY ---
            with tab_learn:
                render_topic_1_content(subtopic_id)
                
        except ImportError as e:
            st.error(f"Interactive content not available: {str(e)}")
            # Fall back to slides only
            tab_slides = st.tabs(["Lecture Slides"])[0]
    else:
        # Other topics: Standard two-tab layout
        tab_slides, tab_practice = st.tabs(["Lecture Slides", "Practice Questions"])
    
    # --- TAB 1: SLIDES ---
    with tab_slides:
        if "slide_range" in topic:
            start, end = topic["slide_range"]
            
            # Sync state for slide navigation
            if "current_slide_num" not in st.session_state:
                st.session_state.current_slide_num = start
            
            # Ensure within bounds (in case we switched topics)
            if not (start <= st.session_state.current_slide_num <= end):
                st.session_state.current_slide_num = start

            col_nav_1, col_img, col_nav_2 = st.columns([0.1, 0.8, 0.1])
            
            with col_nav_1:
                if st.button("◀", key="prev_slide"):
                    st.session_state.current_slide_num = max(start, st.session_state.current_slide_num - 1)
                    st.rerun()
            
            with col_nav_2:
                if st.button("▶", key="next_slide"):
                    st.session_state.current_slide_num = min(end, st.session_state.current_slide_num + 1)
                    st.rerun()

            with col_img:
                current = st.session_state.current_slide_num
                slide_filename = f"Slides/Statistikskript_VWL_HS2025 (3)-{current:03d}.png"
                if os.path.exists(slide_filename):
                    st.image(slide_filename, caption=f"Slide {current} / {end}", use_container_width=True)
                else:
                    st.warning(f"Slide not found: {slide_filename}")
                    
                # Direct Jump Input
                new_slide = st.number_input("Go to Slide", min_value=start, max_value=end, value=current, key="slide_jump")
                if new_slide != current:
                    st.session_state.current_slide_num = new_slide
                    st.rerun()
        else:
            st.info("No slides available for this topic.")

    # --- TAB 2: QUESTIONS (only for non-topic_1) ---
    if topic_id != "topic_1":
        with tab_practice:
            st.subheader("Exam Questions")
            # Placeholder: Fetch questions for this topic specifically
            # For now, show "Descriptive Stats" questions if Topic 7, else generic
            questions = EXAM_QUESTIONS.get("descr_stats", []) if topic_id == "topic_7" else []
            
            if questions:
                for q in questions:
                    render_exam_question(q, model)
            else:
                st.info("No practice questions added for this topic yet.")

def render_exam_question(q, model):
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
            st.session_state[f"{qid}_correct"] = (user_choice == q['correct_answer'])
            st.rerun()
    else:
        if st.session_state[f"{qid}_correct"]:
            st.success("✅ Correct!")
        else:
            st.error("❌ Incorrect.")
            if st.button("Retry", key=f"{qid}_retry"):
                 st.session_state[f"{qid}_submitted"] = False
                 st.rerun()
        
        with st.expander("Master Solution", expanded=True):
            st.markdown(q['solution_text'])
