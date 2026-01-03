"""
Layout K: Foundation Utilities
==============================
Common helper functions used by all layouts.
Provides: Grey callouts, equal-height CSS, semantic colors.

BORDER CONSISTENCY: Uses rgba(0,0,0,0.20) to match styles.py centralized settings.
"""

import streamlit as st
from utils.localization import t


# Centralized border settings (match views/styles.py)
STANDARD_BORDER = "1px solid rgba(0,0,0,0.20)"
STANDARD_RADIUS = "8px"


def inject_equal_height_css():
    """Inject CSS for equal-height side-by-side containers."""
    st.markdown("""<style>
[data-testid="stHorizontalBlock"] { align-items: stretch !important; }
[data-testid="column"], [data-testid="stColumn"] { display: flex !important; flex-direction: column !important; }
[data-testid="column"] > div, [data-testid="stColumn"] > div { flex: 1 !important; display: flex !important; flex-direction: column !important; height: 100% !important; }
div[data-testid="stVerticalBlock"], div[data-testid="stVerticalBlockBorderWrapper"] { flex: 1 !important; display: flex !important; flex-direction: column !important; }
</style>""", unsafe_allow_html=True)


def grey_callout(label: dict, content: dict):
    """
    Render a grey callout box with label and content.
    Uses 4px left border accent style.
    """
    st.markdown(f'''<div style="background: #f4f4f5; border-left: 4px solid #a1a1aa; padding: 12px 16px; border-radius: 8px; color: #3f3f46;">
<strong>{t(label)}:</strong><br>{t(content)}
</div>''', unsafe_allow_html=True)


def intuition_box(content: dict, label: dict = None):
    """
    Render The Intuition box - white background, standard border.
    Use for opening context (NO math symbols, 12-year-old understands).
    
    Args:
        content: {"de": "...", "en": "..."} - The intuition text
        label: {"de": "...", "en": "..."} - Optional custom label (default: "The Intuition")
    """
    label_text = label or {"de": "Die Intuition", "en": "The Intuition"}
    st.markdown(f'''<div style="background: #ffffff; border: {STANDARD_BORDER}; padding: 16px 20px; border-radius: {STANDARD_RADIUS}; color: #374151;">
<strong>{t(label_text)}:</strong><br>
{t(content)}
</div>''', unsafe_allow_html=True)


def variable_decoder(variables: list):
    """
    Render a variable decoder grey callout.
    """
    items_html = ""
    for v in variables:
        name = t(v["name"])
        desc = t(v.get("description", {"de": "", "en": ""}))
        desc_part = f" — {desc}" if desc else ""
        items_html += f"• ${v['symbol']}$ = <strong>{name}</strong>{desc_part}<br>"
    
    st.markdown(f'''<div style="background: #f4f4f5; border-left: 4px solid #a1a1aa; padding: 12px 16px; border-radius: 8px; color: #3f3f46;">
<strong>{t({"de": "Variablen-Decoder", "en": "Variable Decoder"})}:</strong><br>{items_html}
</div>''', unsafe_allow_html=True)


def key_insight(content: dict):
    """Render a key insight grey callout."""
    st.markdown(f'''<div style="background: #f4f4f5; border-left: 4px solid #a1a1aa; padding: 12px 16px; border-radius: 8px; color: #3f3f46;">
<strong>{t({"de": "Aha-Moment", "en": "Key Insight"})}:</strong><br>{t(content)}
</div>''', unsafe_allow_html=True)


# Semantic colors (match views/styles.py)
COLORS = {
    "blue": "#007AFF",      # Pool, Set A, n
    "red": "#FF4B4B",       # Selection, Event, k
    "purple": "#9B59B6",    # Intersection
    "gray": "#6B7280",      # Neutral
    "callout_bg": "#f4f4f5",
    "callout_border": "#a1a1aa",
    "callout_text": "#3f3f46",
    "border": "rgba(0,0,0,0.20)"  # Standard border color
}

