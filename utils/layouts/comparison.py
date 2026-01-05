"""
Layout B: Side-by-Side Comparison
=================================
Use when: Comparing/contrasting TWO related concepts

FOLLOWS PEDAGOGY RULES:
1. Intuition (NO math, 12-year-old understands) - white bg, standard border
2. Formula (prominent, clean)
3. Variable Decoder (line-separated)
4. Key Insight (line-separated)

Examples: Discrete vs Continuous, Permutation vs Combination, Independence
"""

import streamlit as st
from utils.localization import t
from utils.layouts.foundation import inject_equal_height_css, grey_callout, intuition_box


def render_comparison(
    title: dict = None,
    intuition: dict = None,
    left: dict = None,
    right: dict = None,
    key_difference: dict = None,
    key_difference_formula: str = None,
    show_header: bool = True
):
    """
    Render a side-by-side comparison following pedagogy rules.
    
    Args:
        title: {"de": "...", "en": "..."} - Section header
        intuition: {"de": "...", "en": "..."} - Intro WITHOUT math symbols (12-year-old understands)
        left/right: Dict with keys:
            - title: Concept name
            - intuition: Simple explanation (NO math)
            - formula: LaTeX string
            - variables: List of variable dicts for decoder (optional)
            - insight: Key insight for this concept (optional)
        key_difference: {"de": "...", "en": "..."} - Summary of key difference
    """
    inject_equal_height_css()
    
    # Section header
    if show_header and title:
        st.markdown(f"### {t(title)}")
    
    # Overview intuition - uses centralized intuition_box utility
    if intuition:
        intuition_box(intuition)
        st.markdown("<br>", unsafe_allow_html=True)
    
    # Side-by-side cards
    col1, col2 = st.columns(2, gap="medium")
    
    with col1:
        if left:
            _render_concept_card(left)
    
    with col2:
        if right:
            _render_concept_card(right)
    
    # Key difference callout
    if key_difference:
        st.markdown("<br>", unsafe_allow_html=True)
        # Label outside box (as ### for consistency)
        st.markdown(f"### {t({'de': 'Der Kernunterschied', 'en': 'The Key Difference'})}")
        # Use container so LaTeX renders inside
        with st.container(border=True):
            st.markdown(t(key_difference), unsafe_allow_html=True)
            if key_difference_formula:
                st.latex(key_difference_formula)


def _render_concept_card(concept: dict):
    """Render a single concept card following pedagogy order with line separators."""
    with st.container(border=True):
        # 1. Title
        st.markdown(f"**{t(concept.get('title', {}))}**")
        
        # 2. Intuition (NO MATH - simple explanation)
        if concept.get("intuition"):
            st.markdown(f"*{t(concept['intuition'])}*")
        
        # 3. Formula (PROMINENT)
        if concept.get("formula"):
            st.latex(concept["formula"])
        
        # 4. Variable Decoder (with line separator)
        if concept.get("variables"):
            st.markdown("---")
            st.markdown(f"**{t({'de': 'Variablen', 'en': 'Variables'})}:**")
            for v in concept["variables"]:
                name = t(v["name"])
                desc = t(v.get("description", {"de": "", "en": ""}))
                desc_part = f" — {desc}" if desc else ""
                st.markdown(f"• ${v['symbol']}$ = **{name}**{desc_part}")
        
        # 5. Key Insight (with line separator, NO emoji)
        if concept.get("insight"):
            st.markdown("---")
            st.markdown(f"*{t(concept['insight'])}*")


