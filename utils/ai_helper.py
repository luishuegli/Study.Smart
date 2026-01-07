import streamlit as st
import firebase_admin
from google import genai
from utils.localization import get_current_language, t

MAX_CHAT_HISTORY = 5

# --- FIRESTORE HELPERS ---

def get_ai_data(user_id, question_id):
    """Get AI usage count and history from Firestore."""
    try:
        db = firebase_admin.firestore.client()
        doc_ref = db.collection("ai_interactions").document(user_id).collection("questions").document(question_id)
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


def save_ai_interaction(user_id, question_id, question, answer):
    """Save AI interaction to Firestore."""
    try:
        db = firebase_admin.firestore.client()
        doc_ref = db.collection("ai_interactions").document(user_id).collection("questions").document(question_id)
        doc = doc_ref.get()
        
        if doc.exists:
            data = doc.to_dict()
            current_count = data.get("count", 0)
            history = data.get("history", [])
        else:
            current_count = 0
            history = []
        
        history.append({"q": question, "a": answer})
        
        doc_ref.set({
            "count": current_count + 1,
            "history": history
        })
    except Exception:
        pass


def get_max_ai_questions(user_id):
    """Get max questions allowed for user."""
    try:
        db = firebase_admin.firestore.client()
        doc_ref = db.collection("users").document(user_id)
        doc = doc_ref.get()
        if doc.exists:
            return doc.to_dict().get("max_ai_questions", MAX_CHAT_HISTORY)
        return MAX_CHAT_HISTORY
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
        background: #f4f4f5 !important;
        border-radius: 20px !important;
        padding: 16px 20px !important;
        border: none !important;
        box-shadow: none !important;
    }
    
    /* Chat message text */
    [data-testid="stChatMessage"] p {
        color: #1a1a1a !important;
    }
    
    /* Form styling */
    [data-testid="stForm"] {
        border: none !important;
        padding: 0 !important;
    }
    
    /* Text input styling */
    .gemini-input input {
        background: #f4f4f5 !important;
        border: none !important;
        border-radius: 24px !important;
        padding: 14px 20px !important;
        font-size: 15px !important;
        color: #1a1a1a !important;
    }
    
    .gemini-input input::placeholder {
        color: #6b7280 !important;
    }
    
    /* Send button: Circle - using grid for bulletproof centering */
    .gemini-send button {
        width: 44px !important;
        height: 44px !important;
        min-width: 44px !important;
        max-width: 44px !important;
        padding: 0 !important;
        border-radius: 50% !important;
        background: #000000 !important;
        color: #ffffff !important;
        font-size: 18px !important;
        border: none !important;
        display: grid !important;
        place-items: center !important;
        text-align: center !important;
    }
    
    /* Force all inner elements to center */
    .gemini-send button * {
        margin: 0 !important;
        padding: 0 !important;
        line-height: 1 !important;
        text-align: center !important;
        display: block !important;
        width: 100% !important;
    }
    
    .gemini-send button:hover {
        background: #333333 !important;
    }
    
    /* Questions remaining counter */
    .gemini-remaining {
        font-size: 13px;
        color: #6b7280;
        text-align: center;
        margin-top: 8px;
    }
    
    /* Shimmer animation for loading */
    @keyframes shimmer {
        0% { background-position: -200% 0; }
        100% { background-position: 200% 0; }
    }
    
    .shimmer-line {
        height: 16px;
        margin: 8px 0;
        border-radius: 8px;
        background: linear-gradient(90deg, #f0f0f0 25%, #e0e0e0 50%, #f0f0f0 75%);
        background-size: 200% 100%;
        animation: shimmer 1.5s infinite;
    }
    </style>
    """, unsafe_allow_html=True)

    # Get user info
    user = st.session_state.get("user", {})
    user_id = user.get("localId", "anonymous")
    
    # Session keys
    history_key = f"ai_history_{key_suffix}"
    pending_key = f"ai_pending_{key_suffix}"
    
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
    
    # --- HANDLE PENDING API CALL ---
    # This executes the API call AFTER the rerun, not during form submit
    if pending_key in st.session_state and st.session_state[pending_key]:
        pending_query = st.session_state[pending_key]
        st.session_state[pending_key] = None  # Clear pending state
        
        # Show shimmer while thinking
        thinking_placeholder = st.empty()
        thinking_placeholder.markdown("""
        <div style="min-height: 100px; padding: 16px 0;">
            <div class="shimmer-line" style="width: 75%;"></div>
            <div class="shimmer-line" style="width: 90%;"></div>
            <div class="shimmer-line" style="width: 60%;"></div>
        </div>
        """, unsafe_allow_html=True)
        
        try:
            # Build history context
            history_context = ""
            for qa in chat_history:
                history_context += f"\nUser: {qa['q']}\nAI: {qa['a']}\n"
            
            # Get current language (use already imported function)
            current_lang = get_current_language()
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
            
            full_prompt = f"{latex_instruction}\n\n{context_prompt}\n\n--- CHAT HISTORY ---{history_context}\n--- NEW QUESTION ---\n{pending_query}"
            
            response = client.models.generate_content(
                model='gemini-2.0-flash',
                contents=full_prompt
            )
            
            # Save to Firestore and session state
            save_ai_interaction(user_id, key_suffix, pending_query, response.text)
            st.session_state[history_key].append({
                "q": pending_query,
                "a": response.text
            })
            
            thinking_placeholder.empty()
            st.rerun()
            
        except Exception as e:
            thinking_placeholder.empty()
            st.error(f"AI Error: {str(e)}")
    
    # --- RENDER CHAT HISTORY ---
    if chat_history:
        chat_container = st.container(height=400, border=False)
        with chat_container:
            for qa in chat_history:
                # User bubble: TRUE BLACK, right-aligned
                st.markdown(f"""
                <div style="display: flex; justify-content: flex-end; margin-bottom: 12px;">
                    <div style="background: #000000; color: #ffffff; padding: 12px 18px; 
                                border-radius: 20px; max-width: 85%; width: fit-content;">
                        {qa.get("q", "")}
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                # AI response: native markdown for LaTeX
                with st.chat_message("assistant"):
                    st.markdown(qa.get("a", ""))
    
    # --- INPUT AREA ---
    if remaining > 0:
        # Use columns instead of form for better control
        c_input, c_btn = st.columns([12, 1], gap="small", vertical_alignment="bottom")
        
        with c_input:
            st.markdown('<div class="gemini-input">', unsafe_allow_html=True)
            ai_query = st.text_input(
                "AI Input",
                placeholder=t({"de": "Frag Gemini...", "en": "Ask Gemini..."}),
                label_visibility="collapsed",
                key=input_key
            )
            st.markdown('</div>', unsafe_allow_html=True)
        
        with c_btn:
            st.markdown('<div class="gemini-send">', unsafe_allow_html=True)
            if st.button("➤", key=f"ai_send_{key_suffix}_{len(chat_history)}", type="primary"):
                if not client:
                    st.error("AI Model not available.")
                elif not ai_query or ai_query.strip() == "":
                    st.warning(t({"de": "Bitte gib eine Frage ein.", "en": "Please enter a question."}))
                else:
                    # Check limit again
                    current_data = get_ai_data(user_id, key_suffix)
                    if current_data["count"] >= MAX_CHAT_HISTORY:
                        st.error(t({"de": "Fragenlimit erreicht.", "en": "Question limit reached."}))
                    else:
                        # Set pending state and rerun
                        st.session_state[pending_key] = ai_query
                        st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

        # Show remaining
        st.markdown(f'<div class="gemini-remaining">{remaining} {t({"de": "Fragen verbleibend", "en": "questions remaining"})}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="gemini-remaining">{t({"de": "Fragenlimit erreicht", "en": "Question limit reached"})}</div>', unsafe_allow_html=True)