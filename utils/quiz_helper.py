
import streamlit as st
import random
from utils.localization import t
from utils.ai_helper import render_ai_tutor
from utils.progress_tracker import track_question_answer

def shuffle_options(options, correct_idx, seed):
    """
    Shuffles options deterministically based on seed.
    Returns shuffled options and the new correct index.
    """
    random.seed(seed)
    indices = list(range(len(options)))
    random.shuffle(indices)
    shuffled = [options[i] for i in indices]
    # Find where the original correct index ended up
    new_correct = indices.index(correct_idx)
    return shuffled, new_correct

def render_tab_progress_css(tab_keys, key_prefix, topic_id=None, subtopic_id=None):
    """
    Returns tab labels with checkmarks for completed tabs (Option A).
    Also returns minimal CSS to remove any default styling.
    
    Returns: (tab_labels, css_string)
    - tab_labels: List of strings like ["Event A ✓", "Event B ✓", "Event C"]
    - css_string: Minimal CSS to inject
    """
    answered_tabs = []
    user_progress = st.session_state.get("user_progress", {})
    topic_data = user_progress.get("topics", {}).get(str(topic_id), {})
    subtopic_data = topic_data.get("subtopics", {}).get(str(subtopic_id), {})
    correct_questions = subtopic_data.get("correct_questions", [])

    for tab_key in tab_keys:
        question_id = f"{key_prefix}_{tab_key}"
        if question_id in correct_questions:
            answered_tabs.append(tab_key)
    
    # Generate tab labels with checkmarks for completed
    tab_labels = []
    for tab_key in tab_keys:
        if tab_key in answered_tabs:
            tab_labels.append(f"{tab_key} ✓")
        else:
            tab_labels.append(tab_key)
    
    # Minimal CSS (remove borders from previous implementation)
    css = """<style>
    button[data-baseweb="tab"] {
        border-left: none !important;
        border-bottom: none !important;
    }
    </style>"""
    
    return tab_labels, css


def get_tab_labels_with_progress(tab_keys, key_prefix, topic_id=None, subtopic_id=None):
    """
    Convenience function that returns just the tab labels with checkmarks.
    Use this when you only need labels, not CSS.
    """
    labels, _ = render_tab_progress_css(tab_keys, key_prefix, topic_id, subtopic_id)
    return labels

def render_mcq(
    key_suffix,
    question_text,
    options,
    correct_idx,
    solution_text_dict,
    success_msg_dict,
    error_msg_dict,
    client,
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
    Supports Single Choice (Radio) if correct_idx is int.
    Supports Multiple Choice (Checkbox) if correct_idx is list[int].
    
    Uses @st.fragment internally to prevent tab resets when interacting with expanders.
    """
    
    # Create fragment-wrapped MCQ to isolate reruns from parent tabs
    @st.fragment
    def _mcq_fragment():
        from utils.localization import t
        
        # 1. Question (Allow HTML for <br>)
        st.markdown(question_text, unsafe_allow_html=True)
        
        # 2. Hint (Always below question)
        if hint_text_dict:
            with st.expander(t({"de": "Hinweis anzeigen", "en": "Show Hint"})):
                st.markdown(t(hint_text_dict))
        
        # --- DETERMINE TYPE: Single vs Multi ---
        is_multi_select = isinstance(correct_idx, list)
        
        # --- PERSISTENCE KEYS ---
        radio_key = f"mcq_radio_{key_suffix}"
        checkbox_prefix = f"mcq_check_{key_suffix}"
        check_btn_key = f"mcq_check_btn_{key_suffix}"
        show_sol_key = f"mcq_show_sol_{key_suffix}"
        
        # Initialize Solution State
        if show_sol_key not in st.session_state:
            st.session_state[show_sol_key] = False

        # --- RESTORE SAVED STATE (if new session) ---
        initial_value = None
        if question_id:
            user_progress = st.session_state.get("user_progress", {})
            topic_data = user_progress.get("topics", {}).get(str(topic_id), {})
            subtopic_data = topic_data.get("subtopics", {}).get(str(subtopic_id), {})
            saved_answer = subtopic_data.get("answers", {}).get(question_id)
            
            if saved_answer is not None:
                # Only restore if not already interacted with in this session
                if is_multi_select:
                    # Expect list of ints
                    if isinstance(saved_answer, list):
                        for i in range(len(options)):
                            k = f"{checkbox_prefix}_{i}"
                            if k not in st.session_state:
                                st.session_state[k] = (i in saved_answer)
                else:
                    # specific radio logic handled below or via key default
                    if radio_key not in st.session_state:
                        if isinstance(saved_answer, int) and 0 <= saved_answer < len(options):
                             initial_value = saved_answer
                        else:
                             initial_value = 0

        # =================================================================
        # RENDERING LOGIC
        # =================================================================

        user_submitted = False
        is_correct = False
        
        # --- CASE A: MULTIPLE SELECT (Custom Button Bars) ---
        if is_multi_select:
            selected_indices = []
            
            # Initialize state for each option
            for i in range(len(options)):
                k = f"{checkbox_prefix}_{i}"
                if k not in st.session_state:
                    st.session_state[k] = False
            
            # Render custom option bars (matching radio button styling)
            for i, opt in enumerate(options):
                k = f"{checkbox_prefix}_{i}"
                is_selected = st.session_state.get(k, False)
                
                # Style: selected = black border + gray background, unselected = light border
                if is_selected:
                    selected_indices.append(i)
                    border_style = "border: 2px solid #1f2937; background: #f3f4f6;"
                else:
                    border_style = "border: 1px solid #e5e7eb; background: white;"
                
                # Render as a clickable button
                if st.button(
                    opt,
                    key=f"{checkbox_prefix}_btn_{i}",
                    use_container_width=True,
                    type="secondary"
                ):
                    # Toggle selection
                    st.session_state[k] = not st.session_state[k]
                    st.rerun(scope="fragment")
            
            # Collect current selection
            selected_indices = [i for i in range(len(options)) if st.session_state.get(f"{checkbox_prefix}_{i}", False)]
            
            # Check Answer Button (Combined Submit + Show Solution)
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button(t({"de": "Antwort prüfen", "en": "Check Answer"}), key=check_btn_key, type="primary"):
                user_submitted = True
                # Sort for comparison
                selected_indices.sort()
                correct_set = sorted(correct_idx)
                is_correct = (selected_indices == correct_set)
                
                # Reveal solution immediately on check
                st.session_state[show_sol_key] = True
                
                # Persist Result
                if all([course_id, topic_id, subtopic_id, question_id]):
                    user = st.session_state.get("user")
                    if user and "localId" in user:
                        track_question_answer(
                            user_id=user["localId"],
                            course_id=course_id,
                            topic_id=topic_id,
                            subtopic_id=subtopic_id,
                            question_id=question_id,
                            is_correct=is_correct,
                            selected_index=selected_indices # Store list
                        )
                        from utils.progress_tracker import update_local_progress
                        update_local_progress(topic_id, subtopic_id, question_id, is_correct, selected_indices)

            # Feedback Display (Only if button clicked or solution visible)
            if st.session_state[show_sol_key]:
                 # Re-calc correctness for display in case user changed boxes after clicking 
                 curr_selection = [i for i in range(len(options)) if st.session_state.get(f"{checkbox_prefix}_{i}", False)]
                 curr_selection.sort()
                 curr_correct = (curr_selection == sorted(correct_idx))
                 
                 if curr_correct:
                     st.success(t(success_msg_dict))
                 else:
                     st.error(t(error_msg_dict))


        # --- CASE B: SINGLE SELECT (Radio - Instant) ---
        else:
            # Callback for immediate sync
            def on_radio_change():
                selection = st.session_state[radio_key]
                if selection and all([course_id, topic_id, subtopic_id, question_id]):
                    try:
                        sel_idx = options.index(selection)
                    except ValueError:
                        sel_idx = -1
                    
                    is_correct = (sel_idx == correct_idx)
                    user = st.session_state.get("user")
                    if user and "localId" in user:
                        track_question_answer(
                            user_id=user["localId"],
                            course_id=course_id,
                            topic_id=topic_id,
                            subtopic_id=subtopic_id,
                            question_id=question_id,
                            is_correct=is_correct,
                            selected_index=sel_idx
                        )
                        from utils.progress_tracker import update_local_progress
                        update_local_progress(topic_id, subtopic_id, question_id, is_correct, sel_idx)

            user_selection = st.radio(
                "Select Answer:",
                options,
                index=initial_value,
                key=radio_key,
                label_visibility="collapsed",
                on_change=on_radio_change
            )
            
            if user_selection:
                try:
                    sel_idx = options.index(user_selection)
                except ValueError:
                    sel_idx = -1
                
                is_correct = (sel_idx == correct_idx)
                if is_correct:
                    st.success(t(success_msg_dict))
                else:
                    st.error(t(error_msg_dict))


        # 4. Solution Display Logic
        # Multi-select: Shows after Check Answer button
        # Single-select: Uses expander (inside fragment = no tab reset)
        
        if is_multi_select:
            # Multi-select: Show solution if Check Answer was clicked
            if st.session_state.get(show_sol_key, False):
                with st.container(border=True):
                    sol_content = t(solution_text_dict)
                    st.markdown(sol_content, unsafe_allow_html=True)
                    full_context = f"{ai_context}\n\nProblem: {question_text}\nCorrect Indices: {correct_idx}"
                    render_ai_tutor(f"mcq_ai_{key_suffix}", full_context, client)
        else:
            # Single-select: Use expander (inside fragment = no tab reset)
            with st.expander(t({"de": "Lösung zeigen", "en": "Show Solution"}), expanded=False):
                sol_content = t(solution_text_dict)
                st.markdown(sol_content, unsafe_allow_html=True)
                full_context = f"{ai_context}\n\nProblem: {question_text}\nCorrect Answer Index: {correct_idx}"
                render_ai_tutor(f"mcq_ai_{key_suffix}", full_context, client)

        # Retry/Reset
        if allow_retry:
            if st.button(t({"de": "Frage zurücksetzen", "en": "Reset Question"}), key=f"retry_{key_suffix}", type="secondary"):
                if is_multi_select:
                     for i in range(len(options)):
                         st.session_state[f"{checkbox_prefix}_{i}"] = False
                     st.session_state[show_sol_key] = False
                else:
                    st.session_state[radio_key] = None
                    st.session_state[show_sol_key] = False
                st.rerun(scope="fragment")
    
    # Execute the fragment
    _mcq_fragment()
