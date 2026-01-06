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
    # Label OUTSIDE the box (no colon)
    st.markdown(f"**{t(label)}**")
    st.markdown(f'''<div style="background: #f4f4f5; border-left: 4px solid #a1a1aa; padding: 12px 16px; border-radius: 8px; color: #3f3f46;">
{t(content)}
</div>''', unsafe_allow_html=True)


def intuition_box(content: dict, label: dict = None):
    """
    Render The Intuition box - white background, standard border.
    Use for opening context (NO math symbols, 12-year-old understands).
    
    Args:
        content: {"de": "...", "en": "..."} - The intuition text (HTML allowed)
        label: {"de": "...", "en": "..."} - Optional custom label (default: "The Intuition")
    """
    label_text = label or {"de": "Die Intuition", "en": "The Intuition"}
    # Heading OUTSIDE the box (as ### for proper size)
    st.markdown(f"### {t(label_text)}")
    # Content in styled box (standard border-radius)
    with st.container(border=True):
        st.markdown(t(content), unsafe_allow_html=True)


def variable_decoder(variables: list):
    """
    Render a variable decoder section (clean, no grey box).
    Uses st.markdown for each variable to ensure proper formatting.
    """
    st.markdown(f"**{t({'de': 'Variablen-Decoder', 'en': 'Variable Decoder'})}:**")
    
    for v in variables:
        symbol = v["symbol"]
        name = t(v["name"])
        desc = t(v.get("description", {"de": "", "en": ""}))
        desc_part = f" — {desc}" if desc else ""
        
        # Use markdown with LaTeX inline
        st.markdown(f"• ${symbol}$ = **{name}**{desc_part}")


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


def grey_info(content):
    """
    Drop-in replacement for st.info() that uses grey callout styling.
    Accepts either a string or a dict (for bilingual content via t()).
    """
    if isinstance(content, dict):
        text = t(content)
    else:
        text = content
    
    st.markdown(f'''<div style="background: #f4f4f5; border-left: 4px solid #a1a1aa; padding: 12px 16px; border-radius: 8px; color: #3f3f46;">
{text}
</div>''', unsafe_allow_html=True)


def inject_slider_css(slider_configs: list = None):
    """
    Inject CSS for semantic slider colors (overrides global black default).
    
    ARCHITECTURE:
    - Global CSS in styles.py: ALL sliders are BLACK by default (via mix-blend-mode:hue)
    - This utility: Adds higher-specificity CSS to override with semantic colors
    - Only use this when a slider controls a colored visual element (e.g., blue chart line)
    - Uses mix-blend-mode:hue on a ::before pseudo-element to tint the filled portion
    
    Usage:
        # Only call this if sliders control colored elements in visualizations
        inject_slider_css([
            {"label_contains": "Alpha", "color": "#007AFF"},  # Blue (matches blue element)
            {"label_contains": "Beta", "color": "#16a34a"},   # Green (matches green element)
            {"label_contains": "Outlier", "color": "#FF4B4B"},  # Red (matches red element)
        ])
    """
    if not slider_configs:
        return  # No semantic colors, use global black default
    
    css_parts = []
    
    for config in slider_configs:
        label = config.get("label_contains", "")
        color = config.get("color", "#1f1f1f")
        
        css_parts.append(f"""
/* Semantic slider: {label} */
/* Reset grayscale, setup for overlay */
.stSlider:has([aria-label*="{label}"]) div[data-baseweb="slider"] > div:first-child > div:first-child {{
    filter: none !important;
    position: relative !important;
}}
/* Color overlay with mix-blend-mode:hue */
.stSlider:has([aria-label*="{label}"]) div[data-baseweb="slider"] > div:first-child > div:first-child::before {{
    content: "";
    position: absolute;
    inset: 0;
    background-color: {color} !important;
    mix-blend-mode: hue !important;
    pointer-events: none;
    z-index: 1;
    border-radius: inherit;
}}
/* Thumb - semantic color, above overlay */
.stSlider:has([aria-label*="{label}"]) div[role="slider"] {{
    background-color: {color} !important;
    border: none !important;
    z-index: 2 !important;
}}
""")
    
    st.markdown(f"<style>{''.join(css_parts)}</style>", unsafe_allow_html=True)
