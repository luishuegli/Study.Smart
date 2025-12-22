
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
    completed_questions = subtopic_data.get("completed_questions", [])

    for tab_key in tab_keys:
        # Check session state first (immediate feedback)
        radio_key = f"mcq_radio_{key_prefix}_{tab_key}"
        if radio_key in st.session_state and st.session_state[radio_key] is not None:
            answered_tabs.append(tab_key)
            continue
            
        # Check Firestore progress
        question_id = f"{key_prefix}_{tab_key}"
        if question_id in completed_questions:
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
    allow_retry=False,
    course_id=None,
    topic_id=None,
    subtopic_id=None,
    question_id=None
):
    """
    Renders a standardized Multiple Choice Question with persistence.
    """
    
    # 1. Question
    st.markdown(f"**{question_text}**")
    
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

    user_selection = st.radio(
        "Select Answer:",
        options,
        index=initial_index,
        key=radio_key,
        label_visibility="collapsed"
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
        
        # Track progress if all tracking parameters are provided
        if all([course_id, topic_id, subtopic_id, question_id]):
            # Check if user is logged in - get user ID from auth system
            user = st.session_state.get("user")
            if user and "localId" in user:
                user_id = user["localId"]
                # Track the answer
                success = track_question_answer(
                    user_id=user_id,
                    course_id=course_id,
                    topic_id=topic_id,
                    subtopic_id=subtopic_id,
                    question_id=question_id,
                    is_correct=is_correct,
                    selected_index=sel_idx
                )
                
                # Update local session progress immediately so UI (like tab bars) updates
                if success:
                    if "user_progress" not in st.session_state:
                        st.session_state["user_progress"] = {"topics": {}}
                    
                    prog = st.session_state["user_progress"]
                    t_id = str(topic_id)
                    s_id = str(subtopic_id)
                    
                    if "topics" not in prog: prog["topics"] = {}
                    if t_id not in prog["topics"]: prog["topics"][t_id] = {"subtopics": {}}
                    if s_id not in prog["topics"][t_id]["subtopics"]:
                        prog["topics"][t_id]["subtopics"][s_id] = {"completed_questions": [], "correct_questions": [], "answers": {}}
                    
                    sub_data = prog["topics"][t_id]["subtopics"][s_id]
                    
                    # Ensure structure exists
                    if "completed_questions" not in sub_data: sub_data["completed_questions"] = []
                    if "correct_questions" not in sub_data: sub_data["correct_questions"] = []
                    if "answers" not in sub_data: sub_data["answers"] = {}
                    
                    # Sync question ID
                    if question_id not in sub_data["completed_questions"]:
                        sub_data["completed_questions"].append(question_id)
                    
                    # Sync correctness
                    if is_correct and question_id not in sub_data["correct_questions"]:
                        sub_data["correct_questions"].append(question_id)
                    elif not is_correct and question_id in sub_data["correct_questions"]:
                        sub_data["correct_questions"].remove(question_id)
                    
                    # Sync selected index
                    sub_data["answers"][question_id] = sel_idx
            
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
