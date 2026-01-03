"""
Layout H: Decision Tree / When-to-Use
=====================================
Use when: Choosing between approaches

Structure:
1. Section header
2. Container with IF → THEN rows

Examples: Distribution selection, Formula choice, Method selection
"""

import streamlit as st
from utils.localization import t


def render_decision_tree(
    title: dict,
    decisions: list,
    show_header: bool = True
):
    """
    Render a decision tree / when-to-use guide.
    
    Args:
        title: {"de": "Welche Verteilung?", "en": "Which Distribution?"}
        decisions: List of dicts with:
            - condition: {"de": "...", "en": "..."} - IF condition
            - result: {"de": "...", "en": "..."} - THEN result
            - highlight: bool (optional) - Highlight this row
    
    Example:
        render_decision_tree(
            title={"de": "Welche Verteilung?", "en": "Which Distribution?"},
            decisions=[
                {"condition": {"de": "Zähle Ereignisse pro Zeit", "en": "Counting events per time"}, "result": {"de": "Poisson", "en": "Poisson"}},
                {"condition": {"de": "Erfolge in n Versuchen", "en": "Successes in n trials"}, "result": {"de": "Binomial", "en": "Binomial"}},
            ]
        )
    """
    if show_header:
        st.markdown(f"### {t(title)}")
    
    with st.container(border=True):
        for i, decision in enumerate(decisions):
            if_text = t(decision.get("condition", {}))
            then_text = t(decision.get("result", {}))
            
            if decision.get("highlight"):
                st.markdown(f"**{t({'de': 'WENN', 'en': 'IF'})}** {if_text} → **{then_text}** ✓")
            else:
                st.markdown(f"**{t({'de': 'WENN', 'en': 'IF'})}** {if_text} → **{then_text}**")
            
            if i < len(decisions) - 1:
                st.markdown("---")
