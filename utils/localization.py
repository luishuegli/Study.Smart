import streamlit as st

def init_lang():
    """Initialize language state if not present."""
    if 'lang' not in st.session_state:
        st.session_state.lang = 'de'

def t(content_dict):
    """
    Translate content based on current session state language.
    
    Args:
        content_dict (dict or str): Dictionary with 'de'/'en' keys, or a string (returned as-is).
        
    Returns:
        str: The translated string.
    """
    if isinstance(content_dict, str):
        return content_dict
        
    lang = st.session_state.get('lang', 'de')
    return content_dict.get(lang, content_dict.get('de', ''))

def render_language_selector():
    """
    Renders the custom [DE] [EN] toggle in the sidebar.
    """
    init_lang()
    
    # Custom CSS for the toggle
    st.markdown("""
    <style>
    .lang-btn-container {
        display: flex;
        gap: 8px;
        margin-bottom: 20px;
    }
    .lang-btn {
        flex: 1;
        border: 1px solid rgba(0,0,0,0.1);
        border-radius: 20px;
        padding: 4px 12px;
        text-align: center;
        font-size: 14px;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.2s;
        text-decoration: none;
    }
    .lang-btn-active {
        background-color: #000000;
        color: #FFFFFF !important;
        border-color: #000000;
    }
    .lang-btn-inactive {
        background-color: transparent;
        color: #1D1D1F !important;
    }
    .lang-btn-inactive:hover {
        background-color: rgba(0,0,0,0.05);
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Using columns for the "pill" layout interaction
    # Note: Since we can't easily style native buttons to look exactly like pills side-by-side 
    # without gaps, we'll use native columns with buttons and custom class styling or just native buttons.
    # Given the constraint of "simple toggle", standard Streamlit buttons in columns work best.
    
    col1, col2 = st.sidebar.columns(2)
    
    # Helper to determine button type based on state
    def get_type(target_lang):
        return "primary" if st.session_state.lang == target_lang else "secondary"

    with col1:
        if st.button("DE", key="lang_de", type=get_type("de"), use_container_width=True):
            st.session_state.lang = "de"
            st.rerun()
            
    with col2:
        if st.button("EN", key="lang_en", type=get_type("en"), use_container_width=True):
            st.session_state.lang = "en"
            st.rerun()
