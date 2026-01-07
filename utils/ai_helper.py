import streamlit as st
import re
from utils.localization import t
import firebase_admin.firestore
import time

MAX_CHAT_HISTORY = 5  # Limit to 5 questions per MCQ

def get_ai_data(user_id: str, question_key: str) -> dict:
    """Get current AI usage count AND history from Firestore."""
    try:
        db = firebase_admin.firestore.client()
        doc_ref = db.collection("users").document(user_id).collection("ai_usage").document(question_key)
        doc = doc_ref.get()
        if doc.exists:
            data = doc.to_dict()
            return {
                "count": data.get("count", 0),
                "history": data.get("history", [])
            }
        return {"count": 0, "history": []}
    except Exception:
        return {"count": 0, "history": []}


def save_ai_interaction(user_id: str, question_key: str, query: str, response: str) -> int:
    """Save AI interaction to Firestore and increment count. Returns new count."""
    try:
        db = firebase_admin.firestore.client()
        doc_ref = db.collection("users").document(user_id).collection("ai_usage").document(question_key)
        
        doc = doc_ref.get()
        
        current_data = doc.to_dict() if doc.exists else {}
        current_count = current_data.get("count", 0)
        current_history = current_data.get("history", [])
        
        new_count = current_count + 1
        
        import datetime
        timestamp = datetime.datetime.now().isoformat()
        current_history.append({
            "q": query,
            "a": response,
            "ts": timestamp
        })
        
        doc_ref.set({
            "count": new_count, 
            "max": MAX_CHAT_HISTORY,
            "history": current_history
        })
        return new_count
    except Exception:
        return MAX_CHAT_HISTORY


def render_ai_tutor(key_suffix, context_prompt, client):
    """Gemini-style AI Tutor: User=Right/Black, AI=Left/Light, No icons."""
    
    # CSS: Gemini Dark Mode Style
    st.markdown("""
    <style>
    /* HIDE ALL CHAT ICONS */
    [data-testid="stChatMessage"] > div:first-child {
        display: none !important;
    }
    
    /* Base chat message */
    [data-testid="stChatMessage"] {
        padding: 12px 16px !important;
        border-radius: 20px !important;
        margin-bottom: 12px !important;
    }
    
    /* User Message: TRUE BLACK, RIGHT aligned, width fits text */
    [data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) {
        background: #000000 !important;
        color: #ffffff !important;
        border: none !important;
        width: fit-content !important;
        max-width: 85% !important;
        margin-left: auto !important;
        margin-right: 0 !important;
    }
    
    [data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) p {
        color: #ffffff !important;
    }
    
    /* AI Message: Light, full width left */
    [data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-assistant"]) {
        background: #ffffff !important;
        border: 1px solid #e0e0e0 !important;
        color: #202124 !important;
    }
    
    /* Hide input instructions */
    .stForm [data-testid="InputInstructions"] { display: none !important; }
    
    /* GLOBAL FIX: Submit button - TRUE BLACK with white icon */
    [data-testid="stFormSubmitButton"] > button {
        background-color: #000000 !important;
        border: none !important;
        border-radius: 50% !important;
        height: 42px !important;
        width: 42px !important;
        min-width: 42px !important;
        padding: 0 !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }
    
    [data-testid="stFormSubmitButton"] > button:hover {
        background-color: #333333 !important;
    }
    
    [data-testid="stFormSubmitButton"] > button p {
        color: #ffffff !important;
        font-size: 18px !important;
        margin: 0 !important;
    }
    
    /* Shimmer */
    .shimmer-line {
        height: 14px;
        margin-bottom: 10px;
        border-radius: 8px;
        background: linear-gradient(to right, #f0f0f0 0%, #e0e0e0 20%, #f0f0f0 40%);
        background-size: 800px 100%;
        animation: shimmer 1.5s infinite linear;
    }
    @keyframes shimmer {
        0% { background-position: -400px 0; }
        100% { background-position: 400px 0; }
    }
    
    .gemini-remaining {
        text-align: center;
        color: #888;
        font-size: 0.85em;
        margin-top: 8px;
    }
    </style>
    """, unsafe_allow_html=True)

    # Get user info
    user = st.session_state.get("user", {})
    user_id = user.get("localId", "anonymous")
    
    # Session keys
    history_key = f"ai_history_{key_suffix}"
    
    # Get usage & history from Firestore
    ai_data = get_ai_data(user_id, key_suffix)
    usage_count = ai_data["count"]
    persisted_history = ai_data["history"]
    remaining = MAX_CHAT_HISTORY - usage_count
    
    # Initialize local chat history
    if history_key not in st.session_state:
        st.session_state[history_key] = persisted_history
    else:
        if len(persisted_history) > len(st.session_state[history_key]):
            st.session_state[history_key] = persisted_history

    st.markdown("---")
    
    chat_history = st.session_state[history_key]
    
    # Dynamic Input Key logic
    input_key = f"ai_q_{key_suffix}_{len(chat_history)}"
    form_key = f"ai_form_{key_suffix}_{len(chat_history)}"
    
    # --- RENDER CHAT HISTORY (Custom HTML for full control) ---
    if chat_history:
        chat_container = st.container(height=400)
        with chat_container:
            for qa in chat_history:
                # User bubble: TRUE BLACK, right-aligned, width fits text
                st.markdown(f"""
                <div style="display: flex; justify-content: flex-end; margin-bottom: 12px;">
                    <div style="background: #000000; color: #ffffff; padding: 12px 18px; 
                                border-radius: 20px; max-width: 85%; width: fit-content;">
                        {qa.get("q", "")}
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                # AI response: use native markdown for LaTeX support
                with st.chat_message("assistant"):
                    st.markdown(qa.get("a", ""))
    
    # --- INPUT AREA ---
    if remaining > 0:
        with st.form(key=form_key, clear_on_submit=True, border=False):
            # Full width: text input extends left, button on right
            c_input, c_btn = st.columns([12, 1], gap="small", vertical_alignment="bottom")
            
            with c_input:
                ai_query = st.text_input(
                    "AI Input",
                    placeholder=t({"de": "Frag Gemini...", "en": "Ask Gemini..."}),
                    label_visibility="collapsed",
                    key=input_key
                )
            
            with c_btn:
                submitted = st.form_submit_button("➤", type="primary")

            if submitted:
                if not client:
                    st.error("AI Model not available.")
                elif not ai_query:
                    st.warning(t({"de": "Bitte gib eine Frage ein.", "en": "Please enter a question."}))
                else:
                    # Double-check limit
                    current_data_check = get_ai_data(user_id, key_suffix)
                    if current_data_check["count"] >= MAX_CHAT_HISTORY:
                        st.error(t({"de": "Fragenlimit erreicht.", "en": "Question limit reached."}))
                    else:
                        # --- STEP 1: IMMEDIATE VISUAL FEEDBACK ---
                        
                        # A. Show User's Question (Custom HTML - same as history)
                        st.markdown(f"""
                        <div style="display: flex; justify-content: flex-end; margin-bottom: 12px;">
                            <div style="background: #000000; color: #ffffff; padding: 12px 18px; 
                                        border-radius: 20px; max-width: 85%; width: fit-content;">
                                {ai_query}
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        # B. Show Shimmer with Reserved Space (Gemini-style)
                        thinking_placeholder = st.empty()
                        thinking_placeholder.markdown("""
                        <div style="min-height: 150px; padding: 16px 0;">
                            <div class="shimmer-line" style="width: 75%;"></div>
                            <div class="shimmer-line" style="width: 90%;"></div>
                            <div class="shimmer-line" style="width: 60%;"></div>
                            <div class="shimmer-line" style="width: 80%;"></div>
                        </div>
                        <script>
                            // Scroll container to bottom
                            setTimeout(() => {
                                const containers = window.parent.document.querySelectorAll('[data-testid="stVerticalBlock"]');
                                containers.forEach(c => c.scrollTop = c.scrollHeight);
                            }, 100);
                        </script>
                        """, unsafe_allow_html=True)

                        # --- STEP 2: API CALL ---
                        try:
                            history_context = ""
                            for qa in chat_history:
                                history_context += f"\nUser: {qa['q']}\nAI: {qa['a']}\n"
                            
                            # Get current language for response
                            import utils.localization as loc
                            current_lang = loc.get_language()
                            lang_instruction = "RESPOND IN GERMAN (Deutsch)." if current_lang == "de" else "RESPOND IN ENGLISH."
                            
                            latex_instruction = f"""
                            LANGUAGE: {lang_instruction}
                            
                            TEACHING STYLE (Feynman Method):
                            - Explain like teaching a smart friend who's new to the topic.
                            - Show the relevant formula using LaTeX: $$formula$$.
                            - Break down what each variable/symbol means in plain words.
                            - Give the intuition: WHY does this work? What's the "aha" moment?
                            - Use simple analogies when helpful.
                            - Use inline math $x$ for variables in sentences.
                            """
                            
                            full_prompt = f"{latex_instruction}\n\n{context_prompt}\n\n--- CHAT HISTORY ---{history_context}\n--- NEW QUESTION ---\n{ai_query}"
                            
                            response = client.models.generate_content(
                                model='gemini-2.0-flash',
                                contents=full_prompt
                            )
                            
                            # --- STEP 3: SAVE & RERUN ---
                            save_ai_interaction(user_id, key_suffix, ai_query, response.text)
                            st.session_state[history_key].append({
                                "q": ai_query,
                                "a": response.text
                            })
                            
                            thinking_placeholder.empty()
                            st.rerun(scope="fragment")
                            
                        except Exception as e:
                            thinking_placeholder.empty()
                            st.error(f"AI Error: {str(e)}")

        # Show remaining
        st.markdown(f'<div class="gemini-remaining">{remaining} {t({"de": "Fragen verbleibend", "en": "questions remaining"})}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="gemini-remaining">{t({"de": "Fragenlimit erreicht", "en": "Question limit reached"})}</div>', unsafe_allow_html=True)