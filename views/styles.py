import streamlit as st

def render_icon(icon_name):
    """
    Render Lucide SVG icons for the TechNoir theme.
    
    Args:
        icon_name: Name of the Lucide icon to render
        
    Returns:
        HTML string with SVG icon
    """
    # Lucide Icons SVG library (stroke-width: 2px, size: 20x20)
    icons = {
        "book": """<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>""",
        "activity": """<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg>""",
        "check-circle": """<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>""",
        "file-text": """<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.5 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7.5L14.5 2z"/><polyline points="14 2 14 8 20 8"/><line x1="16" x2="8" y1="13" y2="13"/><line x1="16" x2="8" y1="17" y2="17"/><line x1="10" x2="8" y1="9" y2="9"/></svg>""",
        "bot": """<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 8V4H8"/><rect width="16" height="12" x="4" y="8" rx="2"/><path d="M2 14h2"/><path d="M20 14h2"/><path d="M15 13v2"/><path d="M9 13v2"/></svg>""",
        "square": """<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="18" x="3" y="3" rx="2" ry="2"/><path d="M12 12h.01"/></svg>""",
        "bar-chart": """<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 3v18h18"/><path d="M18 17V9"/><path d="M13 17V5"/><path d="M8 17v-3"/></svg>""",
        "filter": """<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="22 3 2 3 10 12.46 10 19 14 21 14 12.46 22 3"/></svg>""",
        "target": """<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/></svg>""",
        "beaker": """<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 2v17.5A2.5 2.5 0 0 1 6.5 22v0A2.5 2.5 0 0 1 4 19.5V2"/><path d="M20 2v17.5a2.5 2.5 0 0 1-2.5 2.5v0a2.5 2.5 0 0 1-2.5-2.5V2"/><path d="M3 2h18"/><path d="M9 22h6"/></svg>""",
        "menu": """<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="4" x2="20" y1="12" y2="12"/><line x1="4" x2="20" y1="6" y2="6"/><line x1="4" x2="20" y1="18" y2="18"/></svg>""",
        "arrow-left": """<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="19" x2="5" y1="12" y2="12"/><polyline points="12 19 5 12 12 5"/></svg>""",
        "slideshow": """<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="14" x="3" y="3" rx="2"/><path d="m9 10 2 2 4-4"/></svg>""",
    }
    
    return icons.get(icon_name, "")

def load_css():
    """Inject the Dual-Theme design system CSS (Technoir / Clean Apple)."""
    st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        /* ========== GLOBAL VARIABLES & RESET ========== */
        :root {
            --card-radius: 24px;
            --btn-radius: 50px;
            --border-width: 1px;
            --card-border: 1px solid rgba(128, 128, 128, 0.2);
            --shadow-light: 0 4px 20px rgba(0,0,0,0.1);
        }

        .stApp { 
            background-color: var(--background-color); 
            font-family: 'Inter', sans-serif; 
            color: var(--text-color);
        }
        
        /* ========== CARD CONTAINERS (BENTO GRID) ========== */
        /* Target Vertical Blocks that look like cards */
        div[data-testid="stVerticalBlock"] > div[style*="flex-direction: column;"] > div[data-testid="stVerticalBlock"] {
            background-color: var(--secondary-background-color);
            border: var(--card-border);
            border-radius: var(--card-radius);
            padding: 24px;
            box-shadow: var(--shadow-light);
        }

        /* ========== LATEX MATH FONT SIZE ========== */
        .katex { 
            font-size: 1.1em !important; 
            color: var(--text-color) !important; 
        }

        /* ========== CUSTOM BUTTONS (PILL SHAPE - INVERTED) ========== */
        .stButton > button {
            border-radius: var(--btn-radius);
            font-weight: 600;
            padding: 10px 24px;
            transition: all 0.2s ease;
            border: none;
        }
        
        /* Primary buttons: High Contrast Inverted */
        .stButton > button[kind="primary"] {
            background-color: var(--text-color);
            color: var(--background-color);
        }
        
        .stButton > button[kind="primary"]:hover {
            opacity: 0.8;
            box-shadow: 0 4px 12px rgba(0,0,0,0.2);
        }
        
        /* Secondary buttons: Subtle Outline */
        .stButton > button[kind="secondary"] {
            background-color: transparent;
            color: var(--text-color);
            border: 1px solid rgba(128, 128, 128, 0.3);
        }
        
        .stButton > button[kind="secondary"]:hover {
            background-color: var(--secondary-background-color);
            border-color: var(--text-color);
        }
        
        /* ========== INTERACTIVE INPUTS (SLIDERS/FIELDS) ========== */
        div[data-baseweb="slider"] { 
            opacity: 0.9; 
        }
        
        .stTextInput > div > div > input,
        .stTextArea > div > div > textarea {
            background-color: var(--secondary-background-color);
            color: var(--text-color);
            border: 1px solid rgba(128, 128, 128, 0.3);
            border-radius: 12px;
        }
        
        .stTextInput > div > div > input:focus,
        .stTextArea > div > div > textarea:focus {
            border-color: var(--primary-color);
            box-shadow: 0 0 0 1px var(--primary-color);
        }
        
        /* ========== THEORY BOXES ========== */
        .theory-box {
            background-color: var(--secondary-background-color);
            border: var(--card-border);
            border-radius: 16px;
            padding: 32px;
            margin: 24px 0;
            box-shadow: var(--shadow-light);
        }
        
        .theory-box-header {
            display: flex;
            align-items: center;
            gap: 16px;
            margin-bottom: 24px;
            padding-bottom: 16px;
            border-bottom: 1px solid rgba(128, 128, 128, 0.2);
        }
        
        .theory-icon {
            width: 48px;
            height: 48px;
            display: flex;
            align-items: center;
            justify-content: center;
            background-color: var(--text-color);
            border-radius: 12px;
            color: var(--background-color);
        }
        
        .theory-icon svg {
            width: 28px !important;
            height: 28px !important;
        }
        
        .theory-title {
            font-size: 20px;
            font-weight: 700;
            color: var(--text-color);
        }
        
        .theory-content {
            color: var(--text-color);
            line-height: 1.6;
            font-size: 16px;
            opacity: 0.9;
        }
        
        .experiment-badge {
            display: inline-flex;
            align-items: center;
            background-color: var(--background-color);
            color: var(--text-color);
            padding: 8px 16px;
            border-radius: 100px;
            font-size: 12px;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-top: 16px;
            border: 1px solid rgba(128, 128, 128, 0.3);
        }
        
        /* ========== RADIO BUTTONS ========== */
        div[class*="stRadio"] > div[role="radiogroup"] > label {
            background-color: var(--secondary-background-color);
            border: 1px solid rgba(128, 128, 128, 0.2);
            border-radius: 12px !important;
            padding: 16px !important;
            margin-bottom: 8px !important;
            transition: all 0.2s;
            color: var(--text-color);
        }
        
        div[class*="stRadio"] > div[role="radiogroup"] > label:hover {
            border-color: var(--text-color);
            background-color: var(--background-color);
        }
        
        div[class*="stRadio"] > div[role="radiogroup"] > label:has(input:checked) {
            border: 2px solid var(--text-color) !important;
            background-color: var(--background-color);
        }
        
        /* ========== TABS ========== */
        .stTabs [data-baseweb="tab-list"] {
            gap: 8px;
            background-color: transparent;
        }
        
        .stTabs [data-baseweb="tab"] {
            background-color: var(--secondary-background-color);
            border-radius: 12px;
            color: var(--text-color);
            padding: 12px 24px;
            border: 1px solid rgba(128, 128, 128, 0.1);
        }
        
        .stTabs [data-baseweb="tab"][aria-selected="true"] {
            background-color: var(--text-color);
            color: var(--background-color);
            font-weight: 600;
        }
        
        /* ========== SIDEBAR ========== */
        section[data-testid="stSidebar"] {
            background-color: var(--secondary-background-color);
            border-right: 1px solid rgba(128, 128, 128, 0.1);
        }
        
        section[data-testid="stSidebar"] .stButton > button {
            text-align: left;
            border: none;
            background: transparent;
        }
        
        section[data-testid="stSidebar"] .stButton > button:hover {
            background-color: var(--background-color);
        }
        
        /* ========== ALERTS & PROGRESS ========== */
        .stAlert {
            border-radius: 12px;
            background-color: var(--secondary-background-color);
            border: 1px solid rgba(128, 128, 128, 0.2);
        }
        
        .stProgress > div > div > div {
            background-color: var(--text-color);
        }
        
        /* ========== HEADINGS ========== */
        h1, h2, h3, h4, h5, h6 {
            color: var(--text-color);
            font-weight: 700;
        }
        
        /* ========== LINKS ========== */
        a {
            color: var(--text-color);
            font-weight: 600;
            text-decoration: none;
            opacity: 0.9;
        }
        
        a:hover {
            opacity: 1.0;
            text-decoration: underline;
        }
    </style>
    """, unsafe_allow_html=True)

# Legacy compatibility - keep icon() function for backward compatibility
def icon(name, size=24, color=None):
    """Legacy Material Icon function - redirects to Lucide icons."""
    # Map Material icon names to Lucide equivalents
    icon_map = {
        'menu_book': 'book',
        'school': 'book',
        'slideshow': 'slideshow',
    }
    
    lucide_name = icon_map.get(name, 'book')
    icon_svg = render_icon(lucide_name)
    
    # Apply size and color if specified
    if size != 20 or color:
        icon_svg = icon_svg.replace('width="20"', f'width="{size}"')
        icon_svg = icon_svg.replace('height="20"', f'height="{size}"')
        if color:
            icon_svg = icon_svg.replace('stroke="currentColor"', f'stroke="{color}"')
    
    return icon_svg
