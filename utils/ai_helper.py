import streamlit as st
from utils.localization import t
# from views.styles import render_icon # (Assuming this is used elsewhere)

def render_ai_tutor(key_suffix, context_prompt, client):
    """
    Renders a standardized AI Tutor interface with Gemini-style input.
    """
    # Session state key for the response
    response_key = f"ai_response_{key_suffix}"
    input_key = f"ai_q_{key_suffix}"
    
    st.markdown("---")
    
    # 1. AI Response Area
    if response_key in st.session_state:
        st.markdown(f"**AI Tutor:**")
        st.info(st.session_state[response_key])
        st.markdown("<br>", unsafe_allow_html=True)

    # 2. Input Area - Gemini Style
    with st.form(key=f"ai_form_{key_suffix}", clear_on_submit=True, border=False):
        # We use columns inside the form for layout
        c_input, c_btn = st.columns([6, 1], gap="small", vertical_alignment="bottom")
        
        with c_input:
            ai_query = st.text_input(
                "AI Input",
                placeholder=t({"de": "Frag den AI Tutor...", "en": "Ask the AI Tutor..."}),
                label_visibility="collapsed",
                key=input_key
            )
            
        with c_btn:
            submitted = st.form_submit_button("Send", type="primary", use_container_width=True)

        if submitted:
            if not client:
                st.error("AI Model not available.")
            elif not ai_query:
                st.warning(t({"de": "Bitte gib eine Frage ein.", "en": "Please enter a question."}))
            else:
                try:
                    with st.spinner(t({"de": "AI denkt nach...", "en": "AI is thinking..."})):
                        full_prompt = f"{context_prompt}\n\n--- USER QUESTION ---\n{ai_query}"
                        response = client.models.generate_content(
                            model='gemini-2.0-flash',
                            contents=full_prompt
                        )
                        st.session_state[response_key] = response.text
                        st.rerun()
                except Exception as e:
                    st.error(f"AI Error: {str(e)}")

