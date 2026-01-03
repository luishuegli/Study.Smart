"""
Layout G: Definition Card
=========================
Use when: Simple term definition needed

Structure:
1. Term (bold)
2. Formal definition (italics)
3. Mathematical notation (LaTeX)
4. Plain English explanation

Examples: Independence, Mutual exclusivity, Random variable
"""

import streamlit as st
from utils.localization import t


def render_definition(
    term: dict,
    formal: dict = None,
    formula: str = None,
    plain: dict = None,
    show_border: bool = True
):
    """
    Render a definition card.
    
    Args:
        term: {"de": "Unabhängigkeit", "en": "Independence"} - The term
        formal: {"de": "...", "en": "..."} - Formal definition (italicized)
        formula: LaTeX string for mathematical notation
        plain: {"de": "...", "en": "..."} - Plain English explanation
    
    Example:
        render_definition(
            term={"de": "Unabhängigkeit", "en": "Independence"},
            formal={"de": "A und B sind unabhängig wenn...", "en": "A and B are independent if..."},
            formula=r"P(A \\cap B) = P(A) \\cdot P(B)",
            plain={"de": "Wissen über B sagt nichts über A.", "en": "Knowing B tells nothing about A."}
        )
    """
    wrapper = st.container(border=True) if show_border else st
    
    with wrapper:
        st.markdown(f"**{t(term)}**")
        
        if formal:
            st.markdown(f"*{t(formal)}*")
        
        if formula:
            st.latex(formula)
        
        if plain:
            st.markdown(f"{t({'de': 'Einfach gesagt', 'en': 'In plain English'})}: {t(plain)}")
