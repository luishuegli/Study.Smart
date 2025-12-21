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

def render_language_selector(container=None):
    """
    Renders the custom [DE] [EN] toggle.
    Args:
        container: Streamlit container to render in. Defaults to st.sidebar.
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
    
    if container is None:
        container = st.sidebar

    col1, col2 = container.columns(2)
    
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

def render_sidebar_footer():
    """
    Renders the sidebar footer with language selector and logout button.
    Should be called at the end of sidebar content in each view.
    """
    # CSS to force the sidebar content to fill the height and use flexbox
    st.markdown("""
    <style>
        /* Target the vertical block inside the sidebar user content */
        [data-testid="stSidebarUserContent"] > div:first-child {
            min-height: calc(100vh - 120px);
            display: flex;
            flex-direction: column;
        }
        
        /* Target the spacer container */
        div[data-testid="stElementContainer"]:has(.sidebar-spacer) {
            margin-top: auto;
        }
    </style>
    """, unsafe_allow_html=True)
    
    # Flexible spacer
    st.markdown('<div class="sidebar-spacer"></div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Account Info
    if "user" in st.session_state and isinstance(st.session_state["user"], dict):
        user = st.session_state["user"]
        # Prefer displayName (username), fallback to email
        display_text = user.get("displayName") or user.get("email", "User")
        
        st.markdown(f"""
        <div style="
            border: 1px solid rgba(49, 51, 63, 0.2);
            border-radius: 8px;
            padding: 8px 12px;
            margin-bottom: 12px;
            background-color: var(--secondary-background-color);
            text-align: center;
            font-size: 0.9em;
            color: var(--text-color);
        ">
            <span style="font-weight: 600;">{display_text}</span>
        </div>
        """, unsafe_allow_html=True)
    
    render_language_selector()
    
    if st.button(t({"de": "Abmelden", "en": "Sign Out"}), type="secondary", use_container_width=True):
        if "user" in st.session_state:
            del st.session_state["user"]
        st.rerun()
