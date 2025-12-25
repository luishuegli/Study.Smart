
import streamlit as st
from utils.localization import t
from utils.ai_helper import render_ai_tutor
from utils.progress_tracker import track_question_answer

def render_tab_progress_css(tab_keys, key_prefix, topic_id=None, subtopic_id=None):
    """
    Generates CSS to show green indicators on answered tabs.
    Checks both session state and loaded Firestore progress.
    """
    answered_tabs = []
    user_progress = st.session_state.get("user_progress", {})
    topic_data = user_progress.get("topics", {}).get(str(topic_id), {})
    subtopic_data = topic_data.get("subtopics", {}).get(str(subtopic_id), {})
    correct_questions = subtopic_data.get("correct_questions", [])

    for tab_key in tab_keys:
        # Check current progress (handles both Firestore and immediate session updates)
            
        # Check Firestore progress
        question_id = f"{key_prefix}_{tab_key}"
        if question_id in correct_questions:
            answered_tabs.append(tab_key)
    
    # Check if all tabs are answered
    all_answered = len(answered_tabs) == len(tab_keys)
    
    # Generate CSS for green indicators
    css = """<style>
    /* Add padding to tab text for spacing, but keep borders continuous */
    button[data-baseweb="tab"] {
        padding-left: 16px !important;
        padding-right: 16px !important;
    }
    """
    
    if all_answered:
        css += """
        button[data-baseweb="tab"] {
            border-bottom: 2px solid #34C759 !important;
        }
        """
    else:
        css += """
        button[data-baseweb="tab"] {
            border-bottom: 2px solid transparent !important;
        }
        """
        for i, tab_key in enumerate(tab_keys):
            if tab_key in answered_tabs:
                css += f"""
                button[data-baseweb="tab"]:nth-child({i + 1}) {{
                    border-bottom: 2px solid #34C759 !important;
                }}
                """
    
    css += "</style>"
    return css

def render_mcq(
    key_suffix,
    question_text,
    options,
    correct_idx,
    solution_text_dict,
    success_msg_dict,
    error_msg_dict,
    model,
    ai_context,
    hint_text_dict=None,
    allow_retry=False,
    course_id=None,
    topic_id=None,
    subtopic_id=None,
    question_id=None
):
    """
    Renders a standardized Multiple Choice Question with persistence.
    """
    from utils.localization import t
    
    # 1. Question
    st.markdown(question_text)
    
    # 2. Hint (Always below question)
    if hint_text_dict:
        with st.expander(t({"de": "Hinweis anzeigen", "en": "Show Hint"})):
            st.markdown(t(hint_text_dict))
    
    # 2. Options (Radio)
    radio_key = f"mcq_radio_{key_suffix}"
    
    # --- PERSISTENCE: Check for saved answer ---
    initial_index = None
    if question_id:
        user_progress = st.session_state.get("user_progress", {})
        topic_data = user_progress.get("topics", {}).get(str(topic_id), {})
        subtopic_data = topic_data.get("subtopics", {}).get(str(subtopic_id), {})
        saved_index = subtopic_data.get("answers", {}).get(question_id)
        
        # If we have a saved index, use it. 
        # But if it's already in session state (meaning user just clicked it), session state wins.
        if radio_key not in st.session_state and saved_index is not None:
             initial_index = saved_index

    # --- CALLBACK FOR IMMEDIATE SYNC ---
    def on_mcq_change():
        selection = st.session_state[radio_key]
        if selection and all([course_id, topic_id, subtopic_id, question_id]):
            try:
                sel_idx = options.index(selection)
            except ValueError:
                sel_idx = -1
            
            is_correct = (sel_idx == correct_idx)
            user = st.session_state.get("user")
            if user and "localId" in user:
                user_id = user["localId"]
                # Track the answer in Firestore
                success = track_question_answer(
                    user_id=user_id,
                    course_id=course_id,
                    topic_id=topic_id,
                    subtopic_id=subtopic_id,
                    question_id=question_id,
                    is_correct=is_correct,
                    selected_index=sel_idx
                )
                
                # Update local session progress immediately
                if success:
                    from utils.progress_tracker import update_local_progress
                    update_local_progress(topic_id, subtopic_id, question_id, is_correct, sel_idx)

    user_selection = st.radio(
        "Select Answer:",
        options,
        index=initial_index,
        key=radio_key,
        label_visibility="collapsed",
        on_change=on_mcq_change
    )
    
    # 3. Check Answer & Feedback
    if user_selection:
        # Find index of selection
        try:
            sel_idx = options.index(user_selection)
        except ValueError:
            sel_idx = -1
            
        is_correct = (sel_idx == correct_idx)
        
        if is_correct:
            st.success(t(success_msg_dict))
        else:
            st.error(t(error_msg_dict))
            
    # Spacer removed for tighter layout
    
    # 4. Solution Toggle
    sol_btn_key = f"mcq_sol_btn_{key_suffix}"
    if sol_btn_key not in st.session_state:
        st.session_state[sol_btn_key] = False
    
    # Styled like the other topics
    if st.button(t({"de": "Lösung zeigen", "en": "Show Solution"}), key=f"toggle_{key_suffix}"):
        st.session_state[sol_btn_key] = not st.session_state[sol_btn_key]
        
    if st.session_state[sol_btn_key]:
        with st.container(border=True):
            # Render solution
            sol_content = t(solution_text_dict)
            st.markdown(sol_content, unsafe_allow_html=True)
            
            # 5. AI Tutor
            # We append the user's view of the question to the context if not present
            full_context = f"{ai_context}\n\nProblem: {question_text}\nCorrect Answer Index: {correct_idx}"
            render_ai_tutor(f"mcq_ai_{key_suffix}", full_context, model)
            
    # Retry logic if requested (optional)
    if allow_retry:
        if st.button(t({"de": "Frage zurücksetzen", "en": "Reset Question"}), key=f"retry_{key_suffix}", type="secondary"):
            st.session_state[radio_key] = None
            st.rerun()
