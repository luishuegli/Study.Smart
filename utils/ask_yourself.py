"""
Ask Yourself (Frag Dich) Utility
================================
Standardized component for self-assessment decision guides.
REFERENCE: Topic 4.3's blue-themed decision guide.

Purpose:
- Help students self-check if a concept applies
- Provide quick decision checklist
- Reinforce recognition patterns

Layout:
1. Blue-themed header with question
2. Numbered checklist of criteria
3. Optional conclusion badge (blue filled)
"""

import streamlit as st
from utils.localization import t


def render_ask_yourself(
    header: dict,
    questions: list,
    conclusion: dict = None,
    numbered: bool = True
):
    """
    Renders standardized 'Ask Yourself' / 'Frag Dich' section.
    
    Args:
        header: {"de": "Frag dich: Ist es X?", "en": "Ask yourself: Is it X?"}
        questions: List of question dicts [{"de": "...", "en": "..."}, ...]
        conclusion: Optional badge text {"de": "Alle JA? → X!", "en": "All YES? → X!"}
        numbered: If True, renders as <ol>, else as <ul>
    
    Design:
        - Blue theme: #007AFF border and accent
        - Light blue background: rgba(0, 122, 255, 0.08)
        - White conclusion badge with blue fill
    """
    # Build questions HTML
    list_tag = "ol" if numbered else "ul"
    questions_html = "".join([f"<li>{t(q)}</li>" for q in questions])
    
    # Build conclusion badge HTML (optional)
    conclusion_html = ""
    if conclusion:
        conclusion_html = f'<div style="margin-top: 16px; padding: 10px; background: #007AFF; color: white; border-radius: 8px; text-align: center; font-weight: 600;">{t(conclusion)}</div>'
    
    # Render full component - ALL STYLES MUST BE SINGLE LINE
    st.markdown(f'''<div style="background-color: rgba(0, 122, 255, 0.08); border-radius: 12px; padding: 20px; border: 2px solid #007AFF;">
<div style="font-weight: 700; color: #007AFF; margin-bottom: 16px; font-size: 1.1em;">{t(header)}</div>
<div style="color: #1c1c1e;">
<{list_tag} style="margin: 0; padding-left: 20px; line-height: 2;">{questions_html}</{list_tag}>
</div>
{conclusion_html}
</div>''', unsafe_allow_html=True)

