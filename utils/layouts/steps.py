"""
Layout D: Step-by-Step Process
==============================
Use when: Explaining a procedure/algorithm

Structure:
1. Section header
2. Steps in a single container, each with:
   - Step number + action (bold)
   - Explanation + formula if needed

Examples: How to apply Bayes, Hypothesis testing steps
"""

import streamlit as st
from utils.localization import t


def render_steps(
    title: dict,
    steps: list,
    show_header: bool = True
):
    """
    Render a step-by-step process.
    
    Args:
        title: {"de": "...", "en": "..."} - Section header
        steps: List of dicts with:
            - action: {"de": "...", "en": "..."} - What to do
            - explanation: {"de": "...", "en": "..."} - Why/how (optional)
            - formula: LaTeX string (optional)
    
    Example:
        render_steps(
            title={"de": "Bayes anwenden", "en": "Applying Bayes"},
            steps=[
                {"action": {"de": "Identifiziere Prior", "en": "Identify Prior"}, "formula": r"P(H)"},
                {"action": {"de": "Berechne Likelihood", "en": "Calculate Likelihood"}, "explanation": {"de": "...", "en": "..."}},
            ]
        )
    """
    if show_header:
        st.markdown(f"### {t(title)}")
    
    with st.container(border=True):
        for i, step in enumerate(steps, 1):
            st.markdown(f"**{t({'de': 'Schritt', 'en': 'Step'})} {i}:** {t(step.get('action', {}))}")
            
            if step.get("explanation"):
                st.markdown(t(step["explanation"]))
            
            if step.get("formula"):
                st.latex(step["formula"])
            
            if i < len(steps):
                st.markdown("---")
