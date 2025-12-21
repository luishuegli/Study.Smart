import streamlit as st
from data import COURSES

def dashboard_view():
    # Hide sidebar on dashboard as it provides no value here
    st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            display: none;
        }
    </style>
    """, unsafe_allow_html=True)
    
    st.title("Herzlich Willkommen im Kursbereich")
    st.subheader("Meine aktiven Kurse:")
    
    cols = st.columns(3)
    
    for i, (course_id, course_data) in enumerate(COURSES.items()):
        col = cols[i % 3]
        with col:
            # TechNoir Card Styling (Clickable Link)
            st.markdown(
                f"""
                <a href="/?course={course_id}" target="_self" style="text-decoration: none; color: inherit; display: block;">
                    <div style="
                        background-color: var(--secondary-background-color);
                        padding: 24px;
                        border-radius: 20px;
                        box-shadow: 0 4px 20px rgba(0,0,0,0.1);
                        border: 1px solid rgba(128, 128, 128, 0.2);
                        border-top: 5px solid {course_data['color']};
                        margin-bottom: 20px;
                        transition: all 0.3s ease;
                    " onmouseover="this.style.transform='translateY(-8px)'; this.style.boxShadow='0 8px 30px rgba(0,0,0,0.15)';" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 4px 20px rgba(0,0,0,0.1)';">
                        <h3 style="margin-top: 0; color: var(--text-color); font-weight: 700;">{course_data['title']}</h3>
                        <p style="color: var(--text-color); opacity: 0.8; font-size: 0.9em; line-height: 1.6;">{course_data['description']}</p>
                        <div style="margin-top: 20px;">
                            <span style="font-size: 0.85em; color: {course_data['color']}; font-weight: 600;">Fortschritt: {int(course_data['progress'] * 100)}%</span>
                            <div style="background-color: rgba(128,128,128,0.2); border-radius: 9999px; height: 8px; width: 100%; margin-top: 8px; overflow: hidden;">
                                <div style="background: linear-gradient(90deg, {course_data['color']} 0%, {course_data['color']}dd 100%); height: 8px; border-radius: 9999px; width: {course_data['progress'] * 100}%; transition: width 0.5s ease;"></div>
                            </div>
                        </div>
                    </div>
                </a>
                """,
                unsafe_allow_html=True
            )
