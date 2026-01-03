"""
Worked Example Utility
======================
Standardized component for step-by-step problem solutions.
Based on Topic 4 pattern. Use for all future worked examples.

COLOR ROLES (not variables):
| Color   | Hex     | Role                           |
|---------|---------|--------------------------------|
| Blue    | #007AFF | Known parameters ("The Given") |
| Red     | #FF4B4B | Query values ("The Target")    |
| Green   | #16a34a | Probability/uncertainty (p, σ) |
| Purple  | #9B59B6 | Transformed values (z, t)      |
| Gray    | #6B7280 | Complement ("The Rest")        |

USAGE:
    from utils.worked_example import render_worked_example
    
    render_worked_example(
        header={"de": "Schritt-für-Schritt", "en": "Step-by-Step"},
        problem={"de": "...", "en": "..."},
        steps=[
            {
                "label": {"de": "Gegeben", "en": "Given"},
                "latex": r"{\\color{#007AFF}\\lambda = 4}",
                "note": {"de": "Rate", "en": "Rate"}  # optional
            },
            ...
        ],
        answer={"de": "...", "en": "..."},  # optional
        check={"de": "...", "en": "..."}    # optional, grey callout
    )
"""

import streamlit as st
from utils.localization import t


def render_worked_example(
    header: dict,
    problem: dict,
    steps: list,
    answer: dict = None,
    check: dict = None
):
    """
    Renders a standardized step-by-step worked example.
    
    Args:
        header: Bilingual title {"de": "...", "en": "..."}
        problem: Bilingual problem statement (HTML allowed)
        steps: List of step dicts with 'label', 'latex', optional 'latex_en', 'note'
        answer: Optional bilingual final answer (bold text)
        check: Optional bilingual plausibility check (grey callout)
    """
    # Header outside container (Header-Out Protocol)
    st.markdown(f"### {t(header)}")
    
    with st.container(border=True):
        # Problem statement
        st.markdown(t(problem), unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Steps with dividers between
        for i, step in enumerate(steps):
            if i > 0:
                st.markdown("---")
            
            # Bold label
            st.markdown(f"**{t(step['label'])}:**")
            
            # LaTeX (with optional bilingual support)
            if "latex_en" in step and t({"de": "x", "en": "y"}) == "y":
                st.latex(step["latex_en"])
            else:
                st.latex(step["latex"])
            
            # Optional note/caption
            if step.get("note"):
                st.caption(t(step["note"]))
        
        st.markdown("---")
        
        # Answer OR Check (not both typically)
        if answer:
            st.markdown(f"**{t(answer)}**")
        
        if check:
            st.markdown(f"""
<div style="background-color: #f4f4f5; border-radius: 8px; padding: 12px; border-left: 4px solid #a1a1aa; color: #3f3f46;">
{t(check)}
</div>""", unsafe_allow_html=True)
