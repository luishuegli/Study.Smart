"""
Layout E: Formula Breakdown (Deep Dive)
=======================================
Use when: Complex formula needs detailed part-by-part explanation

Structure:
1. Section header
2. The Story (grey callout - real scenario this solves)
3. The Formula (centered LaTeX)
4. Breaking it down: (sub-section)
   - Grid of formula parts, each explained
5. Key Insight (optional)

Examples: Binomial PMF, Hypergeometric, Variance formula
"""

import streamlit as st
from utils.localization import t
from utils.layouts.foundation import grey_callout, key_insight, inject_equal_height_css


def render_formula_breakdown(
    title: dict,
    story: dict = None,
    formula: str = None,
    parts: list = None,
    insight: dict = None,
    show_header: bool = True
):
    """
    Render a detailed formula breakdown section.
    
    Args:
        title: {"de": "...", "en": "..."} - Section header
        story: {"de": "...", "en": "..."} - Real-world scenario this formula solves
        formula: LaTeX string for main formula
        parts: List of dicts, each with:
            - formula: LaTeX for this part
            - name: {"de": "...", "en": "..."} - What this part represents
            - explanation: {"de": "...", "en": "..."} - Why it's there
        insight: {"de": "...", "en": "..."} - Key insight/aha moment
    
    Example:
        render_formula_breakdown(
            title={"de": "Die Binomialformel verstehen", "en": "Understanding the Binomial Formula"},
            story={"de": "Du fragst: Wie wahrscheinlich...", "en": "You ask: How likely..."},
            formula=r"P(X=k) = \\binom{n}{k} p^k (1-p)^{n-k}",
            parts=[
                {
                    "formula": r"\\binom{n}{k}",
                    "name": {"de": "Wähle k aus n", "en": "Choose k from n"},
                    "explanation": {"de": "Wie viele Wege gibt es?", "en": "How many ways?"}
                },
                {
                    "formula": r"p^k",
                    "name": {"de": "k Erfolge", "en": "k successes"},
                    "explanation": {"de": "Jeder Erfolg hat Wsk p", "en": "Each success has prob p"}
                },
            ]
        )
    """
    inject_equal_height_css()
    
    # Section header
    if show_header:
        st.markdown(f"### {t(title)}")
    
    # 1. The Story (OUTSIDE container - pedagogy rule)
    if story:
        from utils.layouts.foundation import intuition_box
        intuition_box(story, label={"de": "Die Geschichte", "en": "The Story"})
        st.markdown("<br>", unsafe_allow_html=True)
    
    with st.container(border=True):
        # 2. The Main Formula (PROMINENT)
        if formula:
            st.latex(formula)
        
        # 3. Breaking it down
        if parts:
            st.markdown("---")
            st.markdown(f"**{t({'de': 'Aufgeschlüsselt', 'en': 'Breaking it down'})}:**")
            st.markdown("<br>", unsafe_allow_html=True)
            
            # Render parts in 2-column grid
            num_parts = len(parts)
            for i in range(0, num_parts, 2):
                cols = st.columns(2, gap="medium")
                
                for j, col in enumerate(cols):
                    idx = i + j
                    if idx < num_parts:
                        part = parts[idx]
                        with col:
                            with st.container(border=True):
                                st.markdown(f"**{t(part.get('name', {}))}**")
                                if part.get("formula"):
                                    st.latex(part["formula"])
                                if part.get("explanation"):
                                    st.caption(t(part["explanation"]))
        
        # 4. Key Insight (with line separator)
        if insight:
            st.markdown("---")
            key_insight(insight)
