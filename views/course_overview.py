import streamlit as st
import utils.localization as loc
from utils.localization import t
from data import COURSES
from utils.progress_tracker import get_user_progress

# Define total questions per subtopic for progress calculation
SUBTOPIC_QUESTION_COUNTS = {
    "1.1": 1,  # q_1_1_stetig
    "1.2": 5,  # 1_2_A, 1_2_B, 1_2_C, 1_2_D (test1_q2), 1_2_E (test3_q1)
    "1.3": 1,  # 1_3_exam
    "1.4": 1,  # 1_4_exam
    "1.5": 2,  # 1_5_exam + Market Analyst Mission
    "1.6": 2,  # p_single_point, 1_6_dart_mission
    "1.7": 12, # Integrated HS2024 MC3, MC5
    "1.8": 4,  # 1_8_factory, 1_8_mission, 1_8_bayes_coins, 1_8_game_theory
    "1.9": 4,  # + hs2024_mc6
    "1.10": 6, # exam_l1 to exam_l6
    "1.11": 11, # hs2024_mc10 + 10 uebung1_mc
    "2.1": 1,  # q_2_1_scenario_mastery
    "2.2": 1,  # q_2_2_club
    "2.3": 3,  # q_2_3_dvd, 2_3_test1_q3, 2_3_hs2015_mc4
    "2.4": 2,  # q_2_4_lottery, 2_4_test2_q1
    "2.5": 1,  # q_2_5_coin
    "2.6": 3,  # Additional Questions
    # Topic 3: Random Variables
    "3.1": 1,  # uebung2_mc6
    "3.2": 4,  # m1 (50%), m2 (3x), uebung2_mc5, test2_q4
    "3.3": 2,  # test2_q3, 3_3_mission (Factory Tycoon)
    "3.4": 7,  # 3_4_casino + hs2024_mc7, mc12, +4 more
    "3.5": 2,  # 3_5_sharpshooter + uebung2_mc8
    "3.6": 2,  # 3_6_mission + test3_mc2
    "3.7": 2,  # 3_7_symmetry_mission + hs2024_mc11
    # Topic 4: Stochastic Models and Distributions
    "4.1": 0,  # No MCQs
    "4.2": 0,  # Problems only
    "4.3": 4,  # uebung2_giro, hs2022_mc7, hs2023_mc12, hs2022_mc6
    "4.4": 1,  # test4_q1
    "4.5": 1,  # test2_q2
    "4.6": 3,  # uebung2_mc12, hs2015_prob3, hs2022_mc4
    "4.7": 6,  # + hs2024_mc9
    "4.8": 1,  # hypergeom_10_5_3
    "4.9": 9,  # hs2023_prob3 + 4 uebung2 + 2 Test + 2 Audit (uebung2_mc11, hs2022_mc6)
    # Topic 5: Multidimensional Random Variables
    "5.1": 3,  # test3_q4, uebung3_mc5, hs2015_prob4
    "5.2": 4,  # 5_2_coin_mission, 5_2_cov, 5_2_vardiff, 5_2_varscale
    "5.3": 7,  # + hs2024_mc2
    "5.4": 3,  # uebung3_mc10, uebung3_mc11, hs2025_mc6
    "5.5": 14,  # 3 Quick Checks + 11 official exam questions
    # Topic 6: Central Limit Theorem
    "6.1": 3,  # uebung4_mc1, uebung4_mc2, uebung4_prob7
    "6.2": 3,  # uebung4_prob3, hs2022_mc10, hs2023_mc3 (De Moivre-Laplace)
    "6.3": 9,  # 4 Quick Checks + 5 official exam questions (uebung4_mc1,2,3, prob3, prob7)
    # Topic 7: Descriptive Statistics
    "7.1": 1,  # hs2015_mc8 + Distribution Matcher interactive
    "7.2": 6,  # test4_q3, hs2015_mc9, hs2023_mc4, test3_q3, hs2023_mc9, hs2015_mc8
    "7.3": 1,  # hs2015_prob1 (Boxplot)
    "7.4": 2,  # 7_4_mcq1, 7_4_mcq2
    "7.5": 2,  # 7_5_mcq1, 7_5_mcq2 (Correlation Explorer + MCQs)
    "7.6": 6,  # 4 Quick Checks (visual, center, dispersion, boxplot) + 2 official exam questions
    # Topic 8: Point Estimation
    "8.1": 1,  # hs2023_mc10
    "8.2": 2,  # hs2023_mc10, hs2015_mc10
    "8.3": 3,  # hs2022_mc8, hs2015_prob5, +1
    "8.4": 22,  # uebung5_mc1-15 + prob3,5,6,8 + test5_mc3 + hs2023_prob5 + hs2022_prob5
    # Topic 9: Confidence Intervals
    "9.1": 2,  # uebung5_mc16, uebung5_mc17
    "9.2": 1,  # hs2023_mc5
    "9.3": 1,  # 9_3_duality (CI-Test connection)
    "9.4": 8,  # 3 Quick Checks (concept, formulas, duality) + 5 exam questions
    # Topic 10: Hypothesis Tests
    "10.1": 1,  # 10_1_types (Hypothesis classification MCQ)
    "10.2": 0,  # No MCQs
    "10.3": 0,  # No MCQs
    "10.4": 0,  # No MCQs
    "10.5": 4,  # uebung6_prob1-4 (Implemented)
    # Topic 11: Interdisciplinary
    "11.1": 4,  # hs2023_full_prob1,2,3 + hs2022_full_prob3
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
        if st.button(f"← {loc.t({'de': 'Zurück zum Dashboard', 'en': 'Back to Dashboard'})}", use_container_width=True, type="primary"):
            st.session_state.current_page = "dashboard"
            st.session_state.selected_topic = None
            st.session_state.selected_subtopic = None
            st.rerun()
            
        loc.render_sidebar_footer()

    course_id = st.session_state.get("selected_course", "vwl")
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

    st.title(t(course["title"]))
    
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
        
        # Prepare Header Label (title already includes numbers like "1. Basics of Probability")
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
