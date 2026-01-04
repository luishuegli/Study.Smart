"""
Exam Essentials Utility
=======================
Standardized component for Exam Essentials sections.
REFERENCE: See image 4 from user feedback - this is the gold standard.

Layout (UPDATED ORDER):
1. "Pro Tip: Exam essentials:" header
2. Numbered tips: bold title on one line, "Why?" explanation below
3. Divider
4. "The Most Common Trap" header (LAST for emphasis)
5. Trap description + Rule statement
"""

import streamlit as st
from utils.localization import t


def render_exam_essentials(
    trap: dict = None,
    trap_formula: str = None,
    trap_rule: dict = None,
    tips: list = None,
    items: list = None,
    header: dict = None
):
    """
    Renders standardized Exam Essentials section matching reference image.
    
    ORDER: Pro Tips FIRST, then Trap LAST (for emphasis)
    
    For Topic 4.x (items format): Uses items list with type=warning/tip
    For Topic 5.x (simple format): Uses trap + trap_rule + tips
    """
    # Main header outside container
    main_header = header or {"de": "Prüfungs-Essentials", "en": "Exam Essentials"}
    st.markdown(f"### {t(main_header)}")
    
    with st.container(border=True):
        
        # ========================
        # ITEMS FORMAT (Topic 4.x)
        # ========================
        if items:
            trap_items = [item for item in items if item.get("type") == "warning" or item.get("label", {}).get("en") == "Trap"]
            tip_items = [item for item in items if item not in trap_items]
            
            # PRO TIPS FIRST
            if tip_items:
                st.markdown(f"**Pro Tip: {t({'de': 'Exam essentials', 'en': 'Exam essentials'})}:**")
                st.markdown("")
                
                for i, item in enumerate(tip_items, 1):
                    # Bold title
                    if "title_formula" in item:
                        st.markdown(f"**({i})**")
                        st.latex(item["title_formula"])
                    elif "title" in item:
                        st.markdown(f"**({i}) {t(item['title'])}**")
                    
                    # Why? explanation
                    if "content" in item:
                        st.markdown(f"*{t({'de': 'Warum', 'en': 'Why'})}?* {t(item['content'])}", unsafe_allow_html=True)
                    
                    st.markdown("")
            
            # TRAP LAST (with divider)
            if trap_items:
                st.markdown("---")  # Divider before trap
                for item in trap_items:
                    st.markdown(f"**{t({'de': 'Die häufigste Falle', 'en': 'The Most Common Trap'})}**")
                    
                    if "title" in item:
                        st.markdown(f"**{t(item['title'])}**")
                    if "formula" in item:
                        st.latex(item["formula"])
                    if "content" in item:
                        st.markdown(t(item["content"]), unsafe_allow_html=True)
                    if "shortcut_label" in item:
                        st.markdown(f"**{t(item['shortcut_label'])}:** {t(item.get('shortcut_text', {}))}")
                    if "shortcut_formula" in item:
                        st.latex(item["shortcut_formula"])
            
            return
        
        # ========================
        # SIMPLE FORMAT (Topic 5.x)
        # ========================
        
        # === PRO TIP + TIPS SECTION FIRST ===
        if tips:
            st.markdown(f"**Pro Tip: {t({'de': 'Exam essentials', 'en': 'Exam essentials'})}:**")
            st.markdown("")
            
            for i, tip_data in enumerate(tips, 1):
                # Bold title with optional LaTeX
                if "tip_formula" in tip_data:
                    st.markdown(f"**({i}) {t(tip_data['tip'])}**")
                    st.latex(tip_data["tip_formula"])
                else:
                    st.markdown(f"**({i}) {t(tip_data['tip'])}**")
                
                # Why? explanation with optional LaTeX
                if "why_formula" in tip_data:
                    st.markdown(f"*{t({'de': 'Warum', 'en': 'Why'})}?* {t(tip_data['why'])}")
                    st.latex(tip_data["why_formula"])
                else:
                    st.markdown(f"*{t({'de': 'Warum', 'en': 'Why'})}?* {t(tip_data['why'])}")
                st.markdown("")
        
        # === TRAP SECTION LAST ===
        if trap:
            if tips:  # Only add divider if there were tips before
                st.markdown("---")  # Divider before trap
            st.markdown(f"**{t({'de': 'Die häufigste Falle', 'en': 'The Most Common Trap'})}**")
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown(t(trap), unsafe_allow_html=True)
            
            if trap_formula:
                # Support both string and bilingual dict
                formula = t(trap_formula) if isinstance(trap_formula, dict) else trap_formula
                st.latex(formula)
            
            if trap_rule:
                st.markdown("<br>", unsafe_allow_html=True)
                st.markdown(f"**{t({'de': 'Regel', 'en': 'Rule'})}:** {t(trap_rule)}", unsafe_allow_html=True)

