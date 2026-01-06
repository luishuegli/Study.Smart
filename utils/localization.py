import streamlit as st

def init_lang():
    """Initialize language state from URL or default to 'en'."""
    if 'lang' not in st.session_state:
        # Check URL query param first for persistence across refresh
        url_lang = st.query_params.get('lang', 'en')
        st.session_state.lang = url_lang if url_lang in ('de', 'en') else 'en'
    
    # Always sync to URL for persistence
    st.query_params.lang = st.session_state.lang

def get_current_language():
    """Return current language code ('de' or 'en')."""
    return st.session_state.get('lang', 'de')

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
    
    # Given the constraint of "simple toggle", standard Streamlit buttons in columns work best.
    
    if container is None:
        container = st.sidebar

    col1, col2 = container.columns(2)
    
    # Helper to determine button type based on state
    def get_type(target_lang):
        return "primary" if st.session_state.lang == target_lang else "secondary"
    
    # CSS to make secondary buttons white (unselected state)
    container.markdown("""
    <style>
    /* Language toggle: unselected (secondary) = white background */
    [data-testid="stHorizontalBlock"]:has([data-testid="stButton"]) button[kind="secondary"] {
        background-color: #FFFFFF !important;
        color: #1D1D1F !important;
        border: 1px solid rgba(0,0,0,0.20) !important;
    }
    [data-testid="stHorizontalBlock"]:has([data-testid="stButton"]) button[kind="secondary"]:hover {
        background-color: #F5F5F7 !important;
    }
    </style>
    """, unsafe_allow_html=True)

    with col1:
        if st.button("EN", key="lang_en", type=get_type("en"), use_container_width=True):
            st.session_state.lang = "en"
            st.query_params.lang = "en"  # Persist to URL
            st.rerun()
            
    with col2:
        if st.button("DE", key="lang_de", type=get_type("de"), use_container_width=True):
            st.session_state.lang = "de"
            st.query_params.lang = "de"  # Persist to URL
            st.rerun()

def reset_user_progress(user_id: str, course_id: str) -> bool:
    """
    Resets all progress for a user in a specific course.
    Clears Firestore data and session state.
    
    Returns:
        True if successful, False otherwise
    """
    try:
        import firebase_admin.firestore
        db = firebase_admin.firestore.client()
        
        # Delete progress document from Firestore
        progress_ref = db.collection("users").document(user_id).collection("progress").document(course_id)
        progress_ref.delete()
        
        # Also reset the dashboard progress summary
        user_ref = db.collection("users").document(user_id)
        user_ref.set({
            "progress": {
                course_id: 0.0
            }
        }, merge=True)
        
        return True
    except Exception as e:
        print(f"Error resetting progress: {e}")
        return False


def render_sidebar_footer():
    """
    Renders the sidebar footer with settings, language selector, and logout button.
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
    
    # --- SETTINGS ---
    with st.expander(t({"de": "Einstellungen", "en": "Settings"}), expanded=False):
        # Reset Progress inside Settings
        st.markdown(f"**{t({'de': 'Fortschritt zurücksetzen', 'en': 'Reset Progress'})}**")
        st.caption(t({
            "de": "Löscht deinen gesamten Lernfortschritt für diesen Kurs.",
            "en": "Deletes all your learning progress for this course."
        }))
        
        if st.button(
            t({"de": "Fortschritt löschen", "en": "Delete Progress"}),
            type="secondary",
            use_container_width=True,
            key="reset_progress_btn"
        ):
            user = st.session_state.get("user")
            course_id = st.session_state.get("selected_course", "vwl")
            
            if user and "localId" in user:
                success = reset_user_progress(user["localId"], course_id)
                
                if success:
                    # Clear local session state
                    if "user_progress" in st.session_state:
                        del st.session_state["user_progress"]
                    if "overall_course_progress" in st.session_state:
                        del st.session_state["overall_course_progress"]
                    if "last_progress_load" in st.session_state:
                        del st.session_state["last_progress_load"]
                    
                    st.success(t({"de": "Fortschritt zurückgesetzt!", "en": "Progress reset!"}))
                    st.rerun()
                else:
                    st.error(t({"de": "Fehler beim Zurücksetzen.", "en": "Error resetting progress."}))
            else:
                st.warning(t({"de": "Nicht angemeldet.", "en": "Not logged in."}))
        
        st.markdown("---")
        
        # Sign Out inside Settings
        if st.button(t({"de": "Abmelden", "en": "Sign Out"}), type="primary", use_container_width=True, key="signout_btn"):
            # Clear cookie to prevent auto-restore on refresh
            try:
                import extra_streamlit_components as stx
                cookie_manager = stx.CookieManager(key="study_smart_auth_logout")
                cookie_manager.delete("token")
            except Exception:
                pass  # Cookie clearing failed, but continue with logout
            
            if "user" in st.session_state:
                del st.session_state["user"]
            st.rerun()
    
    # Language selector at the bottom
    render_language_selector()
