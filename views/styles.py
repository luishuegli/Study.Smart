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
        "settings-2": f"""<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 7h-9"/><path d="M14 17H5"/><circle cx="17" cy="17" r="3"/><circle cx="7" cy="7" r="3"/></svg>""",
        "calculator": f"""<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="16" height="20" x="4" y="2" rx="2"/><line x1="8" x2="16" y1="6" y2="6"/><line x1="16" x2="16" y1="14" y2="18"/><path d="M16 10h.01"/><path d="M12 10h.01"/><path d="M8 10h.01"/><path d="M12 14h.01"/><path d="M8 14h.01"/><path d="M12 18h.01"/><path d="M8 18h.01"/></svg>""",
        "layout-grid": f"""<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="7" height="7" x="3" y="3" rx="1"/><rect width="7" height="7" x="14" y="3" rx="1"/><rect width="7" height="7" x="14" y="14" rx="1"/><rect width="7" height="7" x="3" y="14" rx="1"/></svg>""",
        "award": f"""<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="7"/><polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"/></svg>""",
        "arrow-down-0-9": f"""<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m3 16 4 4 4-4"/><path d="M7 20V4"/><rect x="15" y="4" width="4" height="6" ry="2"/><path d="M15 20h3a2 2 0 0 0 2-2v-2a2 2 0 0 0-2-2h-3"/><path d="M15 14h3a2 2 0 0 0 2-2V10a2 2 0 0 0-2-2h-3"/></svg>""",
        "users": f"""<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>""",
        "shapes": f"""<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M8.3 10a.7.7 0 0 1-.626-1.079l1.7-2.798a.7.7 0 0 1 1.252 0l1.7 2.798A.7.7 0 0 1 11.7 10Z"/><rect x="14" y="14" width="7" height="7" rx="1"/><circle cx="4" cy="18" r="3"/><path d="M7 21h10"/></svg>""",
        "trophy": f"""<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 9H4.5a2.5 2.5 0 0 1 0-5H6"/><path d="M18 9h1.5a2.5 2.5 0 0 0 0-5H18"/><path d="M4 22h16"/><path d="M10 14.66V17c0 .55-.47.98-.97 1.21C7.85 18.75 7 20.24 7 22"/><path d="M14 14.66V17c0 .55.47.98.97 1.21C16.15 18.75 17 20.24 17 22"/><path d="M18 2H6v7a6 6 0 0 0 12 0V2Z"/></svg>""",
        "ticket": f"""<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 9a3 3 0 0 1 0 6v2a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2v-2a3 3 0 0 1 0-6V7a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2Z"/><path d="M13 5v2"/><path d="M13 17v2"/><path d="M13 11v2"/></svg>""",
        "lightbulb": f"""<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 14c.2-1 .7-1.7 1.5-2.5 1-1 1.5-2.4 1.5-3.8 0-3.2-2.8-5.7-6-5.7S6 4.7 6 7.9c0 1.4.5 2.8 1.5 3.8.8.8 1.3 1.5 1.5 2.5"/><path d="M9 18h6"/><path d="M10 22h4"/></svg>""",
        "shirt": f"""<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.38 3.46 16 2a4 4 0 0 1-8 0L3.62 3.46a2 2 0 0 0-1.34 2.23l.58 3.47a1 1 0 0 0 .99.84H6v10c0 1.1.9 2 2 2h8a2 2 0 0 0 2-2V10h2.15a1 1 0 0 0 .99-.84l.58-3.47a2 2 0 0 0-1.34-2.23z"/></svg>""",
        "ghost": f"""<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 10h.01"/><path d="M15 10h.01"/><path d="M12 2a8 8 0 0 0-8 8v12l3-3 2.5 2.5L12 19l2.5 2.5L17 19l3 3V10a8 8 0 0 0-8-8z"/></svg>""",
        "x": f"""<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 6 6 18"/><path d="m6 6 12 12"/></svg>""",
        "ship": f"""<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 21c.6.5 1.2 1 2.5 1 2.5 0 2.5-2 5-2 1.3 0 1.9.5 2.5 1 .6.5 1.2 1 2.5 1 2.5 0 2.5-2 5-2 1.3 0 1.9.5 2.5 1"/><path d="M19.38 20A11.6 11.6 0 0 0 21 14l-9-4-9 4c0 2.9.9 5.8 2.5 8"/><path d="M10 10V4a2 2 0 0 1 2-2a2 2 0 0 1 2 2v6"/><polyline points="14 7 8 7"/></svg>""",
        "help-circle": f"""<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><path d="M12 17h.01"/></svg>""",
        "car": f"""<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 17h2c.6 0 1-.4 1-1v-3c0-.9-.7-1.7-1.5-1.9C18.7 10.6 16 10 16 10s-1.3-1.4-2.2-2.3c-.5-.4-1.1-.7-1.8-.7H5c-.6 0-1.1.4-1.4.9l-1.4 2.9A3.7 3.7 0 0 0 2 12v4c0 .6.4 1 1 1h2"/><circle cx="7" cy="17" r="2"/><path d="M9 17h6"/><circle cx="17" cy="17" r="2"/></svg>""",
        "lock": f"""<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="11" x="3" y="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>""",
        "refresh-cw": f"""<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 12a9 9 0 0 1 9-9 9.75 9.75 0 0 1 6.74 2.74L21 8"/><path d="M21 3v5h-5"/><path d="M21 12a9 9 0 0 1-9 9 9.75 9.75 0 0 1-6.74-2.74L3 16"/><path d="M8 16H3v5"/></svg>""",
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
        /* === NUCLEAR OPTION: Force Streamlit's CSS variables to LIGHT MODE === */
        /* This overrides localStorage/system dark mode preferences */
        :root, [data-theme="dark"], [data-theme="light"], html, body {
            --primary-color: #000000 !important;
            --background-color: #FFFFFF !important;
            --secondary-background-color: #F5F5F7 !important;
            --text-color: #1D1D1F !important;
        }
        
        /* --- 1. VARIABLES (The Purge: Strict Light Mode) --- */
        :root {
            /* === COLORS === */
            --bg-void: #FFFFFF;           /* Page background */
            --bg-card: #FFFFFF;           /* Container background */
            --text-primary: #1D1D1F;      /* Main text */
            --text-secondary: #86868b;    /* Secondary text */
            --accent-fill: #000000;       /* Primary button fill */
            --accent-text: #FFFFFF;       /* Button text */
            --highlight: rgba(0,0,0,0.04);
            
            /* === BORDERS === */
            --border-color: rgba(0,0,0,0.20);
            --border-width: 1px;
            --shadow-card: 0 1px 2px rgba(0,0,0,0.12);
            
            /* === 8PT SPACING SCALE === */
            --space-xs: 8px;    /* Tight gaps */
            --space-sm: 16px;   /* Small elements */
            --space-md: 24px;   /* Medium spacing */
            --space-lg: 32px;   /* Standard card padding */
            --space-xl: 32px;   /* Generous padding */
            --space-2xl: 48px;  /* Extra spacious */
            
            /* === RADIUS === */
            --radius-sm: 8px;   /* Buttons, inputs */
            --radius-md: 12px;  /* Cards, modals */
            --radius-lg: 20px;  /* Large containers */
        }

        /* --- 2. GLOBAL RESET --- */
        .stApp { 
            background-color: var(--bg-void) !important; 
            font-family: 'Inter', sans-serif;
            color: var(--text-primary);
        }
        
        /* --- 3. THE BENTO CARD & NATIVE CONTAINERS --- */
        /* Target bordered containers via stLayoutWrapper (Streamlit's actual structure) */
        div[data-testid="stVerticalBlock"] > div[style*="flex-direction: column;"] > div[data-testid="stVerticalBlock"],
        div[data-testid="stVerticalBlockBorderWrapper"],
        div[data-testid="stLayoutWrapper"] > div[data-testid="stVerticalBlock"] {
            background-color: var(--bg-card) !important;
            border: var(--border-width) solid var(--border-color) !important;
            border-radius: var(--radius-lg) !important;
            padding: var(--space-xl) !important; /* Breathing Room */
            box-shadow: var(--shadow-card) !important;
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
        
        /* --- 3c. EQUAL HEIGHT COLUMNS (Force side-by-side containers to match height) --- */
        /* Turn columns into stretch flex containers */
        [data-testid="stHorizontalBlock"] {
            align-items: stretch !important;
        }
        [data-testid="column"], [data-testid="stColumn"] {
            display: flex !important;
            flex-direction: column !important;
        }
        /* Make inner wrappers grow to fill space */
        [data-testid="column"] > div, [data-testid="stColumn"] > div {
            flex: 1 !important;
        }
        /* CRITICAL: stVerticalBlock inside columns must also flex */
        [data-testid="column"] [data-testid="stVerticalBlock"],
        [data-testid="stColumn"] [data-testid="stVerticalBlock"] {
            display: flex !important;
            flex-direction: column !important;
            flex: 1 !important;
        }
        /* CRITICAL FIX: stLayoutWrapper breaks the chain with flex-grow: 0 by default */
        [data-testid="stLayoutWrapper"] {
            flex: 1 !important;
            display: flex !important;
            flex-direction: column !important;
        }
        /* Force border containers to take full height */
        [data-testid="stVerticalBlockBorderWrapper"] {
            height: 100% !important;
            flex: 1 !important;
            display: flex !important;
            flex-direction: column !important;
            justify-content: space-between !important;
        }
        
        /* --- 4. BUTTONS (The 'Ghost' Fix) --- */
        .stButton > button {
            width: 100%;
            background-color: var(--accent-fill) !important; /* Pure Black */
            color: #FFFFFF !important; /* Force Pure White for Icon */
            border: var(--border-width) solid var(--border-color) !important;
            border-radius: var(--space-md) !important; /* Pill shape */
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
            box-shadow: var(--shadow-card);
            color: #FFFFFF !important;
        }
        
        /* Secondary Buttons (Outlined) */
        .stButton > button[kind="secondary"] {
            background-color: transparent !important;
            color: var(--text-primary) !important;
            border: var(--border-width) solid var(--border-color) !important;
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
        
        /* --- 5b. SLIDERS (Global Defaults) --- */
        /* Remove red gradient from filled track */
        div[data-baseweb="slider"] > div:first-child > div:first-child {
            background-image: none !important;
        }
        
        /* Force ALL slider value text to black - comprehensive selectors */
        div[data-baseweb="slider"] > div > div > div[role="slider"] + div {
            background-color: transparent !important;
            color: #1D1D1F !important;
            font-weight: bold !important;
        }
        
        .stSlider [data-testid="stMarkdownContainer"] p,
        .stSlider p,
        .stSlider span,
        div[data-baseweb="slider"] span,
        div[data-baseweb="slider"] div[data-testid] {
            color: #1D1D1F !important;
        }
        
        /* Target the thumb value tooltip/label specifically */
        div[data-baseweb="slider"] [aria-valuetext],
        div[data-baseweb="slider"] [data-baseweb="tooltip"] {
            color: #1D1D1F !important;
        }
        
        /* --- 6. EXPANDERS --- */
        .streamlit-expanderHeader {
            background-color: transparent !important;
            color: var(--text-primary) !important;
            font-weight: 600;
        }
        
        /* Target the actual details element inside the expander wrapper */
        div[data-testid="stExpander"] details {
            border: var(--border-width) solid var(--border-color) !important;
            border-radius: var(--radius-md) !important;
            background-color: var(--bg-card) !important;
        }
        
        div[data-testid="stExpander"] details summary {
            padding: 12px 16px !important;
            border-bottom: none !important;
        }
        
        /* --- 7a. PILLS (Black Selection - CENTRALIZED) --- */
        /* Streamlit uses stButtonGroup container with stBaseButton-pills and stBaseButton-pillsActive */
        
        /* Unselected pills */
        button[data-testid="stBaseButton-pills"] {
            background-color: #FFFFFF !important;
            border: 1px solid var(--border-color) !important;
            border-radius: 20px !important;
            color: var(--text-primary) !important;
            font-weight: 500 !important;
            padding: 6px 16px !important;
            transition: all 0.15s ease !important;
        }
        
        button[data-testid="stBaseButton-pills"]:hover {
            border-color: #1D1D1F !important;
            background-color: #FAFAFA !important;
        }
        
        /* Selected pill - BLACK (override Streamlit's hardcoded red #FF4B4B) */
        button[data-testid="stBaseButton-pillsActive"] {
            background-color: #1D1D1F !important;
            border: 1px solid #1D1D1F !important;
            color: #FFFFFF !important;
            font-weight: 600 !important;
        }
        
        button[data-testid="stBaseButton-pillsActive"] p,
        button[data-testid="stBaseButton-pillsActive"] span,
        button[data-testid="stBaseButton-pillsActive"] div {
            color: #FFFFFF !important;
        }
        
        /* --- 7a-ii. TABS (Black Underline - override Streamlit's red) --- */
        /* Active tab - black underline */
        button[data-baseweb="tab"][aria-selected="true"] {
            color: #1D1D1F !important;
            border-bottom-color: #1D1D1F !important;
        }
        
        /* The underline indicator itself */
        div[data-baseweb="tab-highlight"] {
            background-color: #1D1D1F !important;
        }
        
        /* Alternative selector for tab underline */
        .stTabs [data-baseweb="tab-list"] button[aria-selected="true"]::after {
            background-color: #1D1D1F !important;
        }
        
        /* Force black border on active tab */
        .stTabs [data-baseweb="tab-list"] [aria-selected="true"] {
            border-bottom: 2px solid #1D1D1F !important;
        }
        
        /* --- 7b. RADIO BUTTONS (Border Selection Logic) --- */
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
            background-color: #FFFFFF !important; /* Explicit white */
            border: 1px solid rgba(0,0,0,0.20) !important;
            border-radius: 12px !important; /* Explicit value, not variable */
            padding: 12px 16px !important;
            margin-bottom: 8px !important;
            transition: all 0.1s ease-in-out;
            color: #1D1D1F !important;
            cursor: pointer;
            display: block !important;
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
        
        /* Selected State: Designer's Choice (Clean & Bold) */
        div[class*="stRadio"] > div[role="radiogroup"] > label:has(input:checked) {
            border: 2px solid #000000 !important; /* Explicit black border */
            background-color: #F8F9FA !important;
            color: #1D1D1F !important;
            font-weight: 700 !important;
            transform: scale(1.005);
            box-shadow: 0 1px 2px rgba(0,0,0,0.12) !important;
            border-radius: 12px !important; /* Maintain radius on selected */
        }
        
        /* Reset text color to standard black */
        div[class*="stRadio"] > div[role="radiogroup"] > label:has(input:checked) p,
        div[class*="stRadio"] > div[role="radiogroup"] > label:has(input:checked) div,
        div[class*="stRadio"] > div[role="radiogroup"] > label:has(input:checked) span {
            color: #1D1D1F !important;
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
        
        /* LaTeX/KaTeX Font Size Harmonization */
        /* Reduce default LaTeX size (1.21em) to match body text */
        .katex {
            font-size: 1.0em !important;
        }
        /* Inline math should match surrounding text */
        .katex-display {
            font-size: 1.1em !important;
        }
        
        /* === FIX KATEX FORMULA CLIPPING === */
        /* Formulas get cut off at top due to overflow:hidden on parent containers */
        /* This ensures the full formula (especially fractions) renders completely */
        .katex,
        .katex-display,
        .katex-display > .katex {
            overflow: visible !important;
        }
        /* Add breathing room at top for tall elements like fractions */
        .katex-display {
            padding-top: 4px !important;
            padding-bottom: 2px !important;
            text-align: center !important; /* Center display math */
        }
        /* Ensure the Streamlit container holding st.latex doesn't clip */
        [data-testid="stMarkdownContainer"] .katex-display,
        [data-testid="stVerticalBlock"] .katex-display {
            overflow: visible !important;
            margin-top: 4px !important;
            text-align: center !important; /* Center display math */
        }
        /* Center $$...$$ display blocks in markdown */
        [data-testid="stMarkdownContainer"] {
            text-align: left; /* Default left for text */
        }
        [data-testid="stMarkdownContainer"] .katex-display {
            margin-left: auto !important;
            margin-right: auto !important;
        }
        
        /* === COMPACT DIVIDERS WITHIN CONTAINERS === */
        /* CRITICAL: Streamlit's st.container(border=True) no longer uses stVerticalBlockBorderWrapper */
        /* The bordered container uses stVerticalBlock with emotion-cache classes for border */
        /* We target ALL hr elements with high specificity to override Streamlit's 2em margins */
        
        /* Global compact hr - override Streamlit's .st-emotion-cache-* 2em margins */
        .stApp hr,
        [data-testid="stVerticalBlock"] hr,
        [data-testid="stMarkdownContainer"] hr {
            margin-top: 4px !important;
            margin-bottom: 4px !important;
        }
        
        /* Keep page-level dividers (after header) with normal spacing */
        .stApp > [data-testid="stVerticalBlock"] > [data-testid="stVerticalBlock"] > [data-testid="stElementContainer"]:first-child ~ [data-testid="stElementContainer"]:nth-child(3) hr {
            margin-top: 16px !important;
            margin-bottom: 16px !important;
        }
        
        /* Reduce vertical gaps between markdown elements */
        [data-testid="stVerticalBlock"] [data-testid="stMarkdownContainer"] p {
            margin-bottom: 4px !important;
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
        /* FORCE WHITE BACKGROUND */
        section[data-testid="stSidebar"] {
            background-color: #FFFFFF !important;
            border-right: var(--border-width) solid var(--border-color) !important;
        }

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
        
        /* --- 11. HIDE FORM SUBMIT HELPER TEXT --- */
        /* Hides "Press Enter to submit form" text from st.form */
        div[data-testid="stFormSubmitButton"] + div,
        .stForm [data-testid="stMarkdownContainer"]:has(p:empty),
        .stForm > div:last-child > div:last-child > small,
        div[data-testid="stForm"] > div > div:last-of-type:not(:has(button)) {
            display: none !important;
        }
        
        /* --- 12. HIDE FRAGMENT BORDERS --- */
        /* Fragments should be invisible wrappers, not bordered containers */
        div[data-testid="stVerticalBlockBorderWrapper"]:has(> div > div > button[data-testid="stBaseButton-primary"]:only-child),
        div[data-testid="stVerticalBlockBorderWrapper"]:has(> div > div > div[data-testid="stVerticalBlockBorderWrapper"]) {
            border: none !important;
            padding: 0 !important;
            background: transparent !important;
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

def inject_equal_height_css():
    """
    Inject CSS to force side-by-side containers to have equal height.
    Call this once at the start of any render function that uses st.columns with bordered containers.
    """
    st.markdown("""
    <style>
    /* Turn the column into a flex container that stretches its children */
    [data-testid="column"], [data-testid="stColumn"] {
        display: flex;
        flex-direction: column;
    }
    
    /* Make the inner wrapper grow to fill available space */
    [data-testid="column"] > div, [data-testid="stColumn"] > div {
        flex: 1;
    }
    
    /* Force the actual border container to take up 100% height */
    [data-testid="stVerticalBlockBorderWrapper"] {
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    </style>
    """, unsafe_allow_html=True)

# LaTeX phantom for equalizing formula heights
LATEX_PHANTOM = r"\vphantom{\int_{-\infty}^{x} \frac{A^2}{B^2}}"
