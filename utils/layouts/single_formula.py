"""
Layout A: Single Formula Introduction
======================================
Use when: Introducing ONE new formula

Structure:
1. Section header (outside)
2. The Intuition (grey callout with real-world analogy)
3. The Formula (centered LaTeX)
4. Variable Decoder (grey callout explaining each symbol)
5. Key Insight (grey callout with "aha!" moment)

Follows Stupid Person Principle:
- WHAT: Formula itself
- WHY: Intuition explains purpose
- HOW: Variable decoder explains components
- WHEN: Implicit in the context
"""

import streamlit as st
from utils.localization import t
from utils.layouts.foundation import grey_callout, variable_decoder, key_insight


def render_single_formula(
    title: dict,
    intuition_label: dict = None,
    intuition: dict = None,
    formula: str = None,
    variables: list = None,
    insight: dict = None,
    show_header: bool = True
):
    """
    Render a complete single formula theory section.
    
    Args:
        title: {"de": "Die Binomialverteilung", "en": "The Binomial Distribution"}
        intuition_label: Label for intuition box (default: "The Intuition")
        intuition: {"de": "...", "en": "..."} - Real-world analogy
        formula: LaTeX string (without $$ delimiters)
        variables: List of variable dicts for decoder
            [{"symbol": "n", "name": {"de": "...", "en": "..."}, "description": {"de": "...", "en": "..."}}]
        insight: {"de": "...", "en": "..."} - Key insight/aha moment
        show_header: Whether to show the section header (default: True)
    
    Example:
        render_single_formula(
            title={"de": "Die Binomialformel", "en": "The Binomial Formula"},
            intuition={"de": "Stell dir vor...", "en": "Imagine..."},
            formula=r"P(X=k) = \\binom{n}{k} p^k (1-p)^{n-k}",
            variables=[
                {"symbol": "n", "name": {"de": "Stichprobe", "en": "Sample"}, "description": {"de": "Anzahl Versuche", "en": "Number of trials"}},
                {"symbol": "k", "name": {"de": "Erfolge", "en": "Successes"}, "description": {"de": "Was wir zählen", "en": "What we count"}},
            ],
            insight={"de": "Der Schlüssel ist...", "en": "The key is..."}
        )
    """
    # Section header (outside container)
    if show_header:
        st.markdown(f"### {t(title)}")
    
    # 1. The Intuition (OUTSIDE container - pedagogy rule)
    if intuition:
        from utils.layouts.foundation import intuition_box
        label = intuition_label or {"de": "Die Intuition", "en": "The Intuition"}
        intuition_box(intuition, label=label)
        st.markdown("<br>", unsafe_allow_html=True)
    
    with st.container(border=True):
        # 2. The Formula (PROMINENT)
        if formula:
            st.latex(formula)
        
        # 3. Variable Decoder (with line separator)
        if variables:
            st.markdown("---")
            variable_decoder(variables)
        
        # 4. Key Insight (with line separator)
        if insight:
            st.markdown("---")
            key_insight(insight)
