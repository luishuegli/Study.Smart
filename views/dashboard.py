import streamlit as st
from data import COURSES

def dashboard_view():
    # Sidebar with footer
    import utils.localization as loc
    with st.sidebar:
        loc.render_language_selector(st.sidebar)
        # Fallback: use displayName, then email prefix, then "Student"
        user = st.session_state.get('user', {})
        display_name = user.get('displayName') or (user.get('email', '').split('@')[0]) or 'Student'
        st.sidebar.markdown(f"### {loc.t({'de': 'Hallo', 'en': 'Hello'})}, **{display_name}**!")
    
    # Load Progress from Firebase
    try:
        from firebase_config import load_progress
        user_id = st.session_state["user"]["localId"]
        user_progress = load_progress(user_id) # Returns dict like {'vwl': 0.5}
    except Exception as e:
        st.error(f"Error loading progress: {e}")
        user_progress = {}
    
    # Update local course data with loaded progress
    # We work on a copy to avoid mutating the global constant if we have multiple users in same runtime (unlikely in Streamlit but good practice)
    import copy
    
    # Dashboard Content
    st.title(loc.t({"de": "Herzlich Willkommen im Kursbereich", "en": "Welcome to the Course Area"}))
    st.subheader(loc.t({"de": "Meine aktiven Kurse:", "en": "My Active Courses:"}))
    
    cols = st.columns(3)
    
    for i, (course_id, course_data) in enumerate(COURSES.items()):
        # Apply progress if found in DB
        current_progress = user_progress.get(course_id, course_data.get("progress", 0.0))
        
        col = cols[i % 3]
        with col:
            # Display the card visually (non-clickable HTML)
            st.markdown(
                f"""
                <div style="
                    background-color: var(--background-color);
                    border: 1px solid rgba(128, 128, 128, 0.2);
                    border-radius: 15px;
                    padding: 20px;
                    min-height: 320px;
                    display: flex;
                    flex-direction: column;
                    justify-content: space-between;
                    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
                    margin-bottom: 8px;
                ">
                    <div>
                        <div style="height: 8px; width: 50%; background-color: {course_data['color']}; border-radius: 4px; margin-bottom: 20px;"></div>
                        <h3 style="margin-top: 0; color: var(--text-color); font-weight: 700;">{loc.t(course_data['title'])}</h3>
                        <p style="color: var(--text-color); opacity: 0.8; font-size: 0.9em; line-height: 1.6;">{loc.t(course_data['description'])}</p>
                        <div style="margin-top: 20px;">
                            <span style="font-size: 0.85em; color: {course_data['color']}; font-weight: 600;">{loc.t({'de': 'Fortschritt', 'en': 'Progress'})}: {int(current_progress * 100)}%</span>
                            <div style="
                                width: 100%;
                                background-color: rgba(128, 128, 128, 0.1);
                                border-radius: 4px;
                                height: 8px;
                                margin-top: 8px;
                            ">
                                <div style="
                                    width: {int(current_progress * 100)}%;
                                    background-color: {course_data['color']};
                                    height: 100%;
                                    border-radius: 4px;
                                "></div>
                            </div>
                        </div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
            
            # Native Streamlit button (prevents full page reload)
            if st.button(
                loc.t({"de": "Kurs öffnen", "en": "Open Course"}),
                key=f"open_course_{course_id}",
                use_container_width=True
            ):
                st.session_state.current_page = "course_overview"
                st.session_state.selected_course = course_id
                st.query_params.update({"page": "course_overview", "course": course_id})
                st.rerun()
