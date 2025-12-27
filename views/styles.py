import streamlit as st

def render_icon(icon_name, size=20, color=None):
    """
    Render Lucide SVG icons for the 'Apple Pro' Light theme.
    """
    icons = {
        "book": f"""<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>""",
        "book-open": f"""<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg>""",
        "activity": f"""<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg>""",
        "layers": f"""<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/></svg>""",
        "clipboard-list": f"""<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><rect x="8" y="2" width="8" height="4" rx="1" ry="1"/><path d="M9 12h6"/><path d="M9 16h6"/><path d="M9 8h6"/></svg>""",
        "check-circle": f"""<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>""",
        "file-text": f"""<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.5 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7.5L14.5 2z"/><polyline points="14 2 14 8 20 8"/><line x1="16" x2="8" y1="13" y2="13"/><line x1="16" x2="8" y1="17" y2="17"/><line x1="10" x2="8" y1="9" y2="9"/></svg>""",
        "bot": f"""<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 8V4H8"/><rect width="16" height="12" x="4" y="8" rx="2"/><path d="M2 14h2"/><path d="M20 14h2"/><path d="M15 13v2"/><path d="M9 13v2"/></svg>""",
        "square": f"""<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="18" x="3" y="3" rx="2" ry="2"/><path d="M12 12h.01"/></svg>""",
        "bar-chart": f"""<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 3v18h18"/><path d="M18 17V9"/><path d="M13 17V5"/><path d="M8 17v-3"/></svg>""",
        "filter": f"""<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="22 3 2 3 10 12.46 10 19 14 21 14 12.46 22 3"/></svg>""",
        "target": f"""<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/></svg>""",
        "beaker": f"""<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 2v17.5A2.5 2.5 0 0 1 6.5 22v0A2.5 2.5 0 0 1 4 19.5V2"/><path d="M20 2v17.5a2.5 2.5 0 0 1-2.5 2.5v0a2.5 2.5 0 0 1-2.5-2.5V2"/><path d="M3 2h18"/><path d="M9 22h6"/></svg>""",
        "menu": f"""<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="4" x2="20" y1="12" y2="12"/><line x1="4" x2="20" y1="6" y2="6"/><line x1="4" x2="20" y1="18" y2="18"/></svg>""",
        "arrow-left": f"""<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="19" x2="5" y1="12" y2="12"/><polyline points="12 19 5 12 12 5"/></svg>""",
        "arrow-right": f"""<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>""",
        "slideshow": f"""<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="14" x="3" y="3" rx="2"/><path d="m9 10 2 2 4-4"/></svg>""",
        "send": f"""<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="22" x2="11" y1="2" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/></svg>""",
        "info": f"""<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/></svg>""",
        "circle": f"""<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/></svg>""",
        "rotate-ccw": f"""<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 12a9 9 0 1 0 9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"/><path d="M3 3v5h5"/></svg>""",
        "factory": f"""<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 20a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V8l-7 5V8l-7 5V4a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2Z"/><path d="M17 18h1"/><path d="M12 18h1"/><path d="M7 18h1"/></svg>""",
        "microscope": f"""<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 18h8"/><path d="M3 22h18"/><path d="M14 22a7 7 0 1 0 0-14h-1"/><path d="M9 14h2"/><path d="M9 12a2 2 0 0 1-2-2V6h6v4a2 2 0 0 1-2 2Z"/><path d="M12 6V3a1 1 0 0 0-1-1H9a1 1 0 0 0-1 1v3"/></svg>""",
        "door-open": f"""<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M13 4h3a2 2 0 0 1 2 2v14"/><path d="M2 20h3"/><path d="M13 20h9"/><path d="M10 12v.01"/><path d="M13 4.562v16.157a1 1 0 0 1-1.242.97L5 20V5.562a2 2 0 0 1 1.515-1.94l4-1A2 2 0 0 1 13 4.561Z"/></svg>""",
        "combine": f"""<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/><circle cx="18" cy="19" r="3"/><line x1="8.59" x2="15.42" y1="13.51" y2="17.49"/><line x1="15.41" x2="8.59" y1="6.51" y2="10.49"/></svg>""",
    }
    
    icon_svg = icons.get(icon_name, "")
    
    if color:
        icon_svg = icon_svg.replace('stroke="currentColor"', f'stroke="{color}"')
        
    return icon_svg

def load_design_system():
    """Inject the Strict 'Apple Pro' Light Mode CSS."""
    st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        /* --- 1. VARIABLES (The Purge: Strict Light Mode) --- */
        :root {
            /* Apple Pro Palette */
            --bg-void: #FFFFFF;           /* The Pure White Void */
            --bg-card: #F5F5F7;           /* The 'Surface' (Soft Grey) */
            --text-primary: #1D1D1F;      /* Near Black for Text */
            --text-secondary: #86868b;
            --border-color: rgba(0,0,0,0.08);
            --accent-fill: #000000;       /* Pure Black for Action */
            --accent-text: #FFFFFF;       /* White Text on Black */
            --highlight: rgba(0,0,0,0.04);
        }

        /* --- 2. GLOBAL RESET --- */
        .stApp { 
            background-color: var(--bg-void) !important; 
            font-family: 'Inter', sans-serif;
            color: var(--text-primary);
        }
        
        /* --- 3. THE BENTO CARD & NATIVE CONTAINERS --- */
        /* Target the main vertical blocks & Native Containers */
        div[data-testid="stVerticalBlock"] > div[style*="flex-direction: column;"] > div[data-testid="stVerticalBlock"],
        div[data-testid="stVerticalBlockBorderWrapper"] {
            background-color: var(--bg-card) !important;
            border: 1px solid var(--border-color) !important;
            border-radius: 20px !important;
            padding: 40px !important; /* Increased from 24px for more breathability */
            box-shadow: 0 4px 12px rgba(0,0,0,0.05) !important; /* Subtle shadow */
            gap: 24px;
        }

        /* --- 3b. CONTAINER WIDTH (Widen the central column) --- */
        .block-container {
            max-width: 56rem !important; /* Sweet spot between default 46rem and 66rem */
            padding-left: 2rem !important;
            padding-right: 2rem !important;
            padding-top: 12px !important; /* Aggressively reduced to 12px */
            padding-bottom: 2rem !important;
        }
        
        /* Remove default margin from top headers to avoid double spacing */
        h1, h2, h3 {
             margin-top: 0 !important;
        }
        
        div[data-testid="stVerticalBlockBorderWrapper"] > div {
             gap: 16px;
        }
        
        /* --- 4. BUTTONS (The 'Ghost' Fix) --- */
        .stButton > button {
            width: 100%;
            background-color: var(--accent-fill) !important; /* Pure Black */
            color: #FFFFFF !important; /* Force Pure White for Icon */
            border: 1px solid var(--border-color) !important;
            border-radius: 24px !important; /* MATCH INPUT ROUNDEDNESS */
            font-weight: 600 !important;
            padding: 8px 24px !important; /* Reduced padding to match input height */
            line-height: normal !important; /* Use normal line height for button */
            transition: all 0.2s ease;
            display: flex !important;
            align-items: center !important;
            justify-content: center !important;
        }
        
        /* FIX: Force internal text to White and remove margins */
        .stButton > button p, 
        .stButton > button div,
        .stButton > button span,
        div[data-testid="stFormSubmitButton"] > button p,
        div[data-testid="stFormSubmitButton"] > button div,
        div[data-testid="stFormSubmitButton"] > button span {
            color: #FFFFFF !important; /* Force Pure White */
            margin: 0 !important;
            line-height: 1 !important;
            padding: 0 !important;
        }
        
        .stButton > button:hover {
            opacity: 0.85;
            transform: scale(0.99);
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            color: #FFFFFF !important;
        }
        
        /* Secondary Buttons (Outlined) */
        .stButton > button[kind="secondary"] {
            background-color: transparent !important;
            color: var(--text-primary) !important;
            border: 1px solid var(--border-color) !important;
        }
         .stButton > button[kind="secondary"]:hover {
            background-color: rgba(0,0,0,0.05) !important;
        }
        /* Fix secondary button text */
        .stButton > button[kind="secondary"] p {
             color: var(--text-primary) !important;
        }
        

        /* AI Chat Input Styling - REMOVED TO FIX BORDER ISSUES */
        /* See ai_helper.py for local override or use default Streamlit style */

        /* --- 5. PROGRESS BARS (Force Black) --- */
        .stProgress > div > div > div > div {
            background-color: var(--accent-fill) !important; /* Black Bar */
        }
        .stProgress > div > div > div {
             background-color: #E5E5E5 !important; /* Light Grey Track */
        }
        
        /* --- 6. EXPANDERS --- */
        .streamlit-expanderHeader {
            background-color: transparent !important;
            color: var(--text-primary) !important;
            font-weight: 600;
            border-bottom: 1px solid var(--border-color);
        }
        
        /* --- 7. RADIO BUTTONS (Border Selection Logic) --- */
        /* Force the element container wrapper to full width */
        div.stElementContainer:has(div.stRadio) {
            width: 100% !important;
        }
        
        /* Force the entire radio widget to full width */
        div[class*="stRadio"] {
            width: 100% !important;
        }
        
        /* Hide Dot */
        div[class*="stRadio"] > div[role="radiogroup"] > label > div:first-child {
            display: none !important;
        }
        
        /* Force radiogroup to full width */
        div[class*="stRadio"] > div[role="radiogroup"] {
            display: flex !important;
            flex-direction: column !important;
            width: 100% !important;
            gap: 0 !important;
        }
        
        /* Container Style - Force full width */
        div[class*="stRadio"] > div[role="radiogroup"] > label {
            background-color: var(--bg-void); /* White background for options */
            border: 1px solid var(--border-color) !important;
            border-radius: 12px !important;
            padding: 12px 16px !important;
            margin-bottom: 8px !important;
            transition: all 0.1s ease-in-out;
            color: var(--text-primary);
            cursor: pointer;
            display: block !important; /* Changed to block */
            width: 100% !important;
            max-width: 100% !important;
            box-sizing: border-box !important;
        }
        
        /* Force the inner div to also be full width */
        div[class*="stRadio"] > div[role="radiogroup"] > label > div {
            width: 100% !important;
            max-width: 100% !important;
        }
        
        div[class*="stRadio"] > div[role="radiogroup"] > label:hover {
            border-color: var(--text-primary) !important;
            background-color: #FAFAFA;
        }
        
        /* Selected State: Thick Black Border */
        div[class*="stRadio"] > div[role="radiogroup"] > label:has(input:checked) {
            border: 2px solid var(--text-primary) !important; /* Black Border */
            background-color: var(--bg-void) !important;
            font-weight: 600;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        }
        
        /* Fix text alignment */
        div[class*="stRadio"] > div[role="radiogroup"] > label > div[data-testid="stMarkdownContainer"] {
            margin-left: 0 !important;
        }

        /* --- 8. TYPOGRAPHY --- */
        h1, h2, h3, h4, h5, h6 {
            color: var(--text-primary);
            font-weight: 700;
            letter-spacing: -0.02em; /* Tight "Pro" tracking */
        }
        p, div, label, li {
            color: var(--text-primary);
        }
        
        .theory-content {
             font-size: 1.05rem;
             line-height: 1.6;
             color: #333;
        }

        /* --- 9. LINKS --- */
        a {
            color: var(--text-primary);
            opacity: 0.7;
            text-decoration: none;
        }
        a:hover {
            opacity: 1.0;
            text-decoration: underline;
        }

        /* --- 10. SIDEBAR TWEAKS --- */
        /* HELL BANNED RE-SIZE HANDLE */
        /* Target the resizing div that typically appears after the section */
        div[data-testid="stSidebar"] > div {
             overflow: hidden !important; 
        }
        
        /* The resize handle is often a div with a specific class or style in Streamlit */
        /* SAFE REVERT: These selectors were likely hiding the main content div */
        /* 
        div[data-testid="stSidebar"] + div,
        section[data-testid="stSidebar"] + div {
            display: none !important;
            width: 0 !important;
            pointer-events: none !important;
        }
        */

        /* Fix unnecessary scrollbar in sidebar - HIDE UI but allow scroll */
        /* We target the user content part specifically */
        section[data-testid="stSidebar"] [data-testid="stSidebarUserContent"] {
             padding-bottom: 20px;
        }

        section[data-testid="stSidebar"] > div { 
            overflow-y: auto !important; 
            overflow-x: hidden !important;
        }
        
        section[data-testid="stSidebar"] ::-webkit-scrollbar {
            display: none !important;
            width: 0 !important;
            height: 0 !important;
        }
        
        /* Ensure specific elements in sidebar don't trigger wide width */
        section[data-testid="stSidebar"] .stElementContainer {
            width: 100% !important;
        }

    </style>
    """, unsafe_allow_html=True)

# Legacy compatibility
def icon(name, size=24, color=None):
    """Legacy Material Icon function - redirects to Lucide icons."""
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
