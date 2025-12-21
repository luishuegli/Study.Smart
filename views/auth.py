
import streamlit as st
import firebase_config as firebase
from views.styles import icon
import utils.localization as loc

def render_auth():
    """Renders the authentication view (Login/Signup)."""
    
    # Custom CSS for the auth card
    

    # Initialize language
    loc.init_lang()

    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        # Language Selector top right of the card
        loc.render_language_selector(container=st)
        
        st.markdown(f"<div class='auth-header'><h1>{icon('menu_book', 32)} VWL Statistik</h1><p>{loc.t({'de': 'Bitte melden Sie sich an.', 'en': 'Please sign in.'})}</p></div>", unsafe_allow_html=True)
        
        tab1, tab2 = st.tabs([loc.t({"de": "Anmelden", "en": "Sign In"}), loc.t({"de": "Registrieren", "en": "Sign Up"})])
        
        with tab1:
            with st.form("login_form"):
                email = st.text_input("Email", key="login_email")
                password = st.text_input(loc.t({"de": "Passwort", "en": "Password"}), type="password", key="login_password")
                submit = st.form_submit_button(loc.t({"de": "Anmelden", "en": "Sign In"}))
                
                if submit:
                    if not email or not password:
                        st.error(loc.t({"de": "Bitte Email und Passwort eintragen.", "en": "Please enter email and password."}))
                    else:
                        with st.spinner(loc.t({"de": "Anmeldung läuft...", "en": "Signing in..."})):
                            user = firebase.sign_in_user(email, password)
                            if "error" in user:
                                st.error(f"{loc.t({'de': 'Fehler', 'en': 'Error'})}: {user['error']}")
                            else:
                                st.success(loc.t({"de": "Erfolgreich angemeldet!", "en": "Successfully signed in!"}))
                                st.session_state["user"] = user
                                st.rerun()

        with tab2:
            with st.form("signup_form"):
                new_email = st.text_input("Email", key="signup_email")
                new_username = st.text_input(loc.t({"de": "Benutzername", "en": "Username"}), key="signup_username")
                new_password = st.text_input(loc.t({"de": "Passwort", "en": "Password"}), type="password", key="signup_password")
                confirm_password = st.text_input(loc.t({"de": "Passwort bestätigen", "en": "Confirm Password"}), type="password", key="signup_confirm")
                submit_signup = st.form_submit_button(loc.t({"de": "Registrieren", "en": "Sign Up"}))
                
                if submit_signup:
                    if new_password != confirm_password:
                        st.error(loc.t({"de": "Passwörter stimmen nicht überein.", "en": "Passwords do not match."}))
                    elif not new_email or not new_password or not new_username:
                        st.error(loc.t({"de": "Bitte alle Felder ausfüllen.", "en": "Please fill in all fields."}))
                    else:
                        with st.spinner(loc.t({"de": "Konto wird erstellt...", "en": "Creating account..."})):
                            user = firebase.sign_up_user(new_email, new_password)
                            if "error" in user:
                                st.error(f"{loc.t({'de': 'Fehler', 'en': 'Error'})}: {user['error']}")
                            else:
                                # Update profile with username
                                updated_user = firebase.update_user_profile(user["idToken"], display_name=new_username)
                                if "error" in updated_user:
                                    st.warning(f"{loc.t({'de': 'Konto erstellt, aber Benutzername konnte nicht gesetzt werden', 'en': 'Account created, but username could not be set'})}: {updated_user['error']}")
                                else:
                                    # Merge the update info back into user object for session state if we were to auto-login
                                    pass
                                    
                                st.success(loc.t({"de": "Konto erstellt! Sie können sich jetzt anmelden.", "en": "Account created! You can now sign in."}))
