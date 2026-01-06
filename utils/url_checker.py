import streamlit as st
import urllib.parse

def sync_url_with_session():
    """
    Injects JavaScript to forcibly ensure the browser URL matches the server-side state.
    This bypasses potential st.query_params sync failures.
    """
    
    # 1. Build the desired query string from session state
    params = {
        "lang": st.session_state.get("lang", "en"),
        "page": st.session_state.get("current_page", "dashboard"),
        "course": st.session_state.get("selected_course", "vwl"),
    }
    
    if st.session_state.get("selected_topic"):
        params["topic"] = st.session_state.selected_topic
    
    if st.session_state.get("selected_subtopic"):
        params["subtopic"] = st.session_state.selected_subtopic
        
    # remove None values
    params = {k: v for k, v in params.items() if v is not None}
    
    # Preserve cache buster if present in current URL to avoid loops
    # Or strict mapping: we want exact state match.
    
    encoded_params = urllib.parse.urlencode(params)
    
    # 2. Inject JS to check and replace if necessary
    # We use st.html (or markdown) to execute the script
    # We use window.history.replaceState to modify URL without reloading
    
    script = f"""
    <script>
        const targetSearch = "?{encoded_params}";
        if (window.location.search !== targetSearch) {{
            console.log("Force-Syncing URL to:", targetSearch);
            window.history.replaceState(null, "", targetSearch);
        }}
    </script>
    """
    
    st.components.v1.html(script, height=0, width=0)
