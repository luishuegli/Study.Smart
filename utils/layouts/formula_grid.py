"""
Layout C: Multi-Formula Grid (2x2 or 3x2)
=========================================
Use when: Multiple related rules/formulas

Structure:
1. Section header
2. Overview intuition (optional)
3. Grid of cards (2 columns), each with:
   - Number + Name (bold)
   - 1-line description
   - Formula (LaTeX)

Examples: Probability rules, Expectation properties, Variance formulas
"""

import streamlit as st
from utils.localization import t
from utils.layouts.foundation import inject_equal_height_css, grey_callout


def render_formula_grid(
    title: dict = None,
    overview: dict = None,
    formulas: list = None,
    key_takeaway: dict = None,
    show_header: bool = True
):
    """
    Render a grid of related formulas.
    
    Args:
        title: {"de": "...", "en": "..."} - Section header
        overview: {"de": "...", "en": "..."} - Intro/context text
        formulas: List of dicts with:
            - name: {"de": "...", "en": "..."} - Rule/formula name
            - description: {"de": "...", "en": "..."} - 1-line explanation
            - formula: LaTeX string
        key_takeaway: {"de": "...", "en": "..."} - Summary insight (optional)
    
    Example:
        render_formula_grid(
            title={"de": "Die Wahrscheinlichkeitsregeln", "en": "Probability Rules"},
            formulas=[
                {
                    "name": {"de": "Komplement", "en": "Complement"},
                    "description": {"de": "Gegenwahrscheinlichkeit", "en": "Opposite probability"},
                    "formula": r"P(\\bar{A}) = 1 - P(A)"
                },
                {
                    "name": {"de": "Additionssatz", "en": "Addition Rule"},
                    "description": {"de": "Vereinigung zweier Ereignisse", "en": "Union of two events"},
                    "formula": r"P(A \\cup B) = P(A) + P(B) - P(A \\cap B)"
                },
            ]
        )
    """
    inject_equal_height_css()
    
    # Section header
    if show_header and title:
        st.markdown(f"### {t(title)}")
    
    # Overview
    if overview:
        st.markdown(t(overview))
        st.markdown("<br>", unsafe_allow_html=True)
    
    # Grid of formulas
    if formulas:
        num_formulas = len(formulas)
        for i in range(0, num_formulas, 2):
            cols = st.columns(2, gap="medium")
            
            for j, col in enumerate(cols):
                idx = i + j
                if idx < num_formulas:
                    f = formulas[idx]
                    with col:
                        with st.container(border=True):
                            st.markdown(f"**{idx + 1}. {t(f.get('name', {}))}**")
                            if f.get("description"):
                                st.caption(t(f["description"]))
                            if f.get("formula"):
                                st.latex(f["formula"])
    
    # Key takeaway
    if key_takeaway:
        st.markdown("<br>", unsafe_allow_html=True)
        grey_callout(
            {"de": "Zusammenfassung", "en": "Key Takeaway"},
            key_takeaway
        )
