import streamlit as st
from data import COURSES

def dashboard_view():
    st.title("Herzlich Willkommen im Kursbereich :)")
    st.subheader("Meine aktiven Kurse:")
    
    cols = st.columns(3)
    
    for i, (course_id, course_data) in enumerate(COURSES.items()):
        col = cols[i % 3]
        with col:
            # Custom Card Styling
            st.markdown(
                f"""
                <div style="
                    background-color: white;
                    padding: 20px;
                    border-radius: 12px;
                    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
                    border-top: 5px solid {course_data['color']};
                    margin-bottom: 20px;
                    color: black;
                ">
                    <h3 style="margin-top: 0; color: #1f2937;">{course_data['title']}</h3>
                    <p style="color: #6b7280; font-size: 0.9em;">{course_data['description']}</p>
                    <div style="margin-top: 15px;">
                        <span style="font-size: 0.8em; color: {course_data['color']}; font-weight: bold;">Fortschritt: {int(course_data['progress'] * 100)}%</span>
                        <div style="background-color: #e5e7eb; border-radius: 9999px; height: 8px; width: 100%; margin-top: 5px;">
                            <div style="background-color: {course_data['color']}; height: 8px; border-radius: 9999px; width: {course_data['progress'] * 100}%;"></div>
                        </div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
            
            if st.button(f"Kurs buchen / Starten", key=f"btn_{course_id}"):
                st.session_state.current_page = "course_overview"
                st.session_state.selected_course = course_id
                st.rerun()
