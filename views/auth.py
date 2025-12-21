
import streamlit as st
import firebase_config as firebase
from views.styles import icon

def render_auth():
    """Renders the authentication view (Login/Signup)."""
    
    # Custom CSS for the auth card
    

    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown(f"<div class='auth-header'><h1>{icon('menu_book', 32)} VWL Statistik</h1><p>Bitte melden Sie sich an.</p></div>", unsafe_allow_html=True)
        
        tab1, tab2 = st.tabs(["Anmelden", "Registrieren"])
        
        with tab1:
            with st.form("login_form"):
                email = st.text_input("Email", key="login_email")
                password = st.text_input("Passwort", type="password", key="login_password")
                submit = st.form_submit_button("Anmelden")
                
                if submit:
                    if not email or not password:
                        st.error("Bitte Email und Passwort eintragen.")
                    else:
                        with st.spinner("Anmeldung läuft..."):
                            user = firebase.sign_in_user(email, password)
                            if "error" in user:
                                st.error(f"Fehler: {user['error']}")
                            else:
                                st.success("Erfolgreich angemeldet!")
                                st.session_state["user"] = user
                                st.rerun()

        with tab2:
            with st.form("signup_form"):
                new_email = st.text_input("Email", key="signup_email")
                new_password = st.text_input("Passwort", type="password", key="signup_password")
                confirm_password = st.text_input("Passwort bestätigen", type="password", key="signup_confirm")
                submit_signup = st.form_submit_button("Registrieren")
                
                if submit_signup:
                    if new_password != confirm_password:
                        st.error("Passwörter stimmen nicht überein.")
                    elif not new_email or not new_password:
                        st.error("Bitte alle Felder ausfüllen.")
                    else:
                        with st.spinner("Konto wird erstellt..."):
                            user = firebase.sign_up_user(new_email, new_password)
                            if "error" in user:
                                st.error(f"Fehler: {user['error']}")
                            else:
                                st.success("Konto erstellt! Sie können sich jetzt anmelden.")
