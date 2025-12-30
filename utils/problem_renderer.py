
import streamlit as st
from utils.localization import t
from utils.progress_tracker import track_question_answer

def render_multi_stage_problem(
    key_suffix: str,
    stem_text: dict, 
    parts: list,
    source: str,
    model,
    ai_context: str,
    course_id: str,
    topic_id: str,
    subtopic_id: str,
    question_id: str
):
    """
    Renders a multi-stage problem with an accordion-style value reveal.
    
    Args:
        parts: List of dicts, each containing:
               {'id': 'a', 'points': 3, 'question': {...}, 'solution': {...}}
    """
    
    # --- RENDER HEADER ---
    st.markdown(f"**{source}**")
    
    with st.container(border=True):
        # Stem / Context
        st.markdown(t(stem_text))
        
        st.markdown("---")
        
        # Calculate Progress Dots
        # Check which parts are completed
        completed_parts = []
        for p in parts:
            part_qid = f"{question_id}_{p['id']}"
            if st.session_state.get(f"{part_qid}_submitted", False):
                completed_parts.append(p['id'])
        
        total_parts = len(parts)
        done_count = len(completed_parts)
        progress_dots = " ".join(["●" if i < done_count else "○" for i in range(total_parts)])
        
        st.caption(f"{t({'de': 'Fortschritt', 'en': 'Progress'})}: {progress_dots}")
        st.markdown("<br>", unsafe_allow_html=True)
        
        # --- RENDER PARTS ---
        for i, part in enumerate(parts):
            p_id = part['id']
            full_qid = f"{question_id}_{p_id}"
            points = part.get('points', 0)
            
            # Accordion Label
            label = f"{t({'de': 'Teil', 'en': 'Part'})} ({p_id}) — {points} {t({'de': 'Punkte', 'en': 'Points'})}"
            if p_id in completed_parts:
                # Clean checkmark SVG
                checkmark = "![check](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9IiMxMGI5ODEiIHN0cm9rZS13aWR0aD0iMyIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48cG9seWxpbmUgcG9pbnRzPSIyMCA2IDkgMTcgNCAxMiI+PC9wb2x5bGluZT48L3N2Zz4=)"
                label = f"{label}  {checkmark}"
            
            # Determine if expanded:
            # Expand if it's the first one, OR if the previous one is done, OR if this one is already done/active
            is_expanded = False
            if i == 0:
                is_expanded = True
            elif parts[i-1]['id'] in completed_parts:
                is_expanded = True
            elif p_id in completed_parts:
                is_expanded = False # Collapse completed ones to save space? Or keep open? Let's keep open if active.
            
            # Override: User interaction state handling
            # Simple rule: Expand if not done, or if it was just interacted with.
            # Using Streamlit default behavior for expanders unless manually controlled.
            # Let's just default to expanded=True for visibility.
            
            with st.expander(label, expanded=True):
                st.markdown(t(part['question']))
                
                # Check state
                is_submitted = st.session_state.get(f"{full_qid}_submitted", False)
                
                if not is_submitted:
                    if st.button(t({'de': 'Lösung anzeigen', 'en': 'Show Solution'}), key=f"btn_{full_qid}", type="primary"):
                        st.session_state[f"{full_qid}_submitted"] = True
                        
                        # Track progress (always correct for open format reveal)
                        track_question_answer(
                            user_id=st.session_state.get("user", {}).get("localId", "guest"),
                            course_id=course_id,
                            topic_id=topic_id,
                            subtopic_id=subtopic_id,
                            question_id=full_qid,
                            is_correct=True
                        )
                        st.rerun()
                else:
                    # Show Solution
                    st.markdown("---")
                    sol = part['solution']
                    # Dual Mode Display
                    st.markdown(t(sol))
                    
                    # Optional: "Hide" button to reset? (Maybe later)


def render_open_question(
    key_suffix: str,
    question_text: dict, 
    solution_text_dict: dict,
    source: str,
    hints: list = None,
    model = None,
    ai_context: str = "",
    course_id: str = "vwl",
    topic_id: str = "1",
    subtopic_id: str = "1.1",
    question_id: str = "q1"
):
    """
    Renders a single open-ended question with solution reveal.
    """
    st.markdown(f"**{source}**")
    
    with st.container(border=True):
        st.markdown(t(question_text))
        
        # Hints
        if hints:
            for h_idx, hint in enumerate(hints):
                with st.expander(f"💡 {t({'de': 'Hinweis', 'en': 'Hint'})} {h_idx+1}"):
                    # Warm background for hints
                    st.markdown(
                        f"""
                        <div style="background-color: #fef3c7; color: #92400e; padding: 12px; border-radius: 8px; border: 1px solid #f59e0b;">
                            {t(hint)}
                        </div>
                        """, 
                        unsafe_allow_html=True
                    )
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Interaction
        is_submitted = st.session_state.get(f"{question_id}_submitted", False)
        
        if not is_submitted:
            if st.button(t({'de': 'Lösung anzeigen', 'en': 'Show Solution'}), key=f"btn_{question_id}", type="primary"):
                st.session_state[f"{question_id}_submitted"] = True
                
                # Track
                track_question_answer(
                    user_id=st.session_state.get("user", {}).get("localId", "guest"),
                    course_id=course_id,
                    topic_id=topic_id,
                    subtopic_id=subtopic_id,
                    question_id=question_id,
                    is_correct=True
                )
                st.rerun()
        else:
            st.markdown("---")
            st.markdown(t(solution_text_dict))
            
            # Reset button for practice
            if st.button(t({'de': 'Zurücksetzen', 'en': 'Reset'}), key=f"reset_{question_id}", type="secondary"):
                st.session_state[f"{question_id}_submitted"] = False
                st.rerun()
