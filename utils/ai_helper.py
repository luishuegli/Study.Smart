import streamlit as st
import re
from utils.localization import t
import firebase_admin.firestore

MAX_CHAT_HISTORY = 5  # Limit to 5 questions per MCQ

# MathJax script for LaTeX rendering (injected once)
MATHJAX_SCRIPT = '''
<script>
if (!window.MathJax) {
    window.MathJax = {
        tex: {inlineMath: [['$', '$']], displayMath: [['$$', '$$']]},
        svg: {fontCache: 'global'},
        startup: {typeset: true}
    };
    var script = document.createElement('script');
    script.src = 'https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js';
    script.async = true;
    document.head.appendChild(script);
}
</script>
'''


def markdown_to_html(text):
    """Convert markdown to HTML with LaTeX support."""
    # Protect LaTeX from markdown processing
    # Store display math ($$...$$) 
    display_math = []
    def save_display(m):
        display_math.append(m.group(1))
        return f'%%DISPLAY_MATH_{len(display_math)-1}%%'
    text = re.sub(r'\$\$(.+?)\$\$', save_display, text, flags=re.DOTALL)
    
    # Store inline math ($...$)
    inline_math = []
    def save_inline(m):
        inline_math.append(m.group(1))
        return f'%%INLINE_MATH_{len(inline_math)-1}%%'
    text = re.sub(r'\$(.+?)\$', save_inline, text)
    
    # Convert markdown
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    text = text.replace('\n', '<br>')
    
    # Restore inline math
    for i, m in enumerate(inline_math):
        text = text.replace(f'%%INLINE_MATH_{i}%%', f'\\({m}\\)')
    
    # Restore display math (centered)
    for i, m in enumerate(display_math):
        text = text.replace(f'%%DISPLAY_MATH_{i}%%', f'<div style="text-align:center; margin: 16px 0;">\\[{m}\\]</div>')
    
    return text


def get_ai_usage(user_id: str, question_key: str) -> int:
    """Get current AI usage count from Firestore."""
    try:
        db = firebase_admin.firestore.client()
        doc_ref = db.collection("users").document(user_id).collection("ai_usage").document(question_key)
        doc = doc_ref.get()
        if doc.exists:
            return doc.to_dict().get("count", 0)
        return 0
    except Exception:
        return 0


def increment_ai_usage(user_id: str, question_key: str) -> int:
    """Increment AI usage count in Firestore. Returns new count."""
    try:
        db = firebase_admin.firestore.client()
        doc_ref = db.collection("users").document(user_id).collection("ai_usage").document(question_key)
        doc = doc_ref.get()
        
        if doc.exists:
            new_count = doc.to_dict().get("count", 0) + 1
        else:
            new_count = 1
        
        doc_ref.set({"count": new_count, "max": MAX_CHAT_HISTORY})
        return new_count
    except Exception:
        return MAX_CHAT_HISTORY  # Fail safe: block on error


def render_ai_tutor(key_suffix, context_prompt, client):
    """
    Renders a Gemini-style AI Tutor interface with Firestore-persisted limits.
    """
    # Gemini-style CSS
    st.markdown("""
    <style>
    .gemini-chat-container {
        max-height: 300px;
        overflow-y: auto;
        padding: 16px 0;
        margin-bottom: 8px;
    }
    .gemini-user-wrapper {
        display: flex;
        justify-content: flex-end;
        margin-bottom: 12px;
    }
    .gemini-user-msg {
        background: #303134;
        color: #e8eaed;
        padding: 10px 16px;
        border-radius: 20px;
        display: inline-block;
        max-width: 80%;
        text-align: left;
    }
    .gemini-ai-text {
        background: #f8f9fa;
        border: 1px solid #e8eaed;
        padding: 12px 16px;
        border-radius: 20px;
        color: #202124;
        line-height: 1.5;
        margin-bottom: 16px;
    }
    .gemini-remaining {
        text-align: center;
        color: #9aa0a6;
        font-size: 0.85em;
        margin-top: 8px;
    }
    .stForm [data-testid="InputInstructions"],
    .stTextInput [data-testid="InputInstructions"] {
        display: none !important;
    }
    [data-testid="stFormSubmitButton"] > button {
        background-color: #1e1e1e !important;
        border-color: #1e1e1e !important;
        color: #FFFFFF !important;
        border-radius: 20px !important;
    }
    [data-testid="stFormSubmitButton"] > button:hover {
        background-color: #333333 !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Get user info
    user = st.session_state.get("user", {})
    user_id = user.get("localId", "anonymous")
    
    # Session keys
    history_key = f"ai_history_{key_suffix}"
    input_key = f"ai_q_{key_suffix}"
    
    # Get usage from Firestore (persisted)
    usage_count = get_ai_usage(user_id, key_suffix)
    remaining = MAX_CHAT_HISTORY - usage_count
    
    # Initialize local chat history (for display only)
    if history_key not in st.session_state:
        st.session_state[history_key] = []
    
    st.markdown("---")
    
    chat_history = st.session_state[history_key]
    
    # 1. Chat History (display only)
    if chat_history:
        # Inject MathJax for LaTeX rendering
        st.markdown(MATHJAX_SCRIPT, unsafe_allow_html=True)
        
        chat_html = '<div class="gemini-chat-container">'
        for qa in chat_history:
            q = qa.get("q", "")
            a = markdown_to_html(qa.get("a", ""))
            chat_html += f'<div class="gemini-user-wrapper"><div class="gemini-user-msg">{q}</div></div>'
            chat_html += f'<div class="gemini-ai-text">{a}</div>'
        chat_html += '</div>'
        # Trigger MathJax typeset after content loads
        chat_html += '<script>if(window.MathJax && window.MathJax.typeset) { window.MathJax.typeset(); }</script>'
        st.markdown(chat_html, unsafe_allow_html=True)
    
    # 2. Input Area (only if under limit)
    if remaining > 0:
        with st.form(key=f"ai_form_{key_suffix}", clear_on_submit=True, border=False):
            c_input, c_btn = st.columns([6, 1], gap="small", vertical_alignment="bottom")
            
            with c_input:
                ai_query = st.text_input(
                    "AI Input",
                    placeholder=t({"de": "Frag Gemini...", "en": "Ask Gemini..."}),
                    label_visibility="collapsed",
                    key=input_key
                )
                
            with c_btn:
                submitted = st.form_submit_button("→", type="primary", use_container_width=True)

            if submitted:
                if not client:
                    st.error("AI Model not available.")
                elif not ai_query:
                    st.warning(t({"de": "Bitte gib eine Frage ein.", "en": "Please enter a question."}))
                else:
                    # Double-check limit (race condition protection)
                    current_usage = get_ai_usage(user_id, key_suffix)
                    if current_usage >= MAX_CHAT_HISTORY:
                        st.error(t({"de": "Fragenlimit erreicht.", "en": "Question limit reached."}))
                    else:
                        try:
                            with st.spinner(t({"de": "Gemini denkt nach...", "en": "Gemini is thinking..."})):
                                history_context = ""
                                for qa in chat_history:
                                    history_context += f"\nUser: {qa['q']}\nAI: {qa['a']}\n"
                                
                                full_prompt = f"{context_prompt}\n\n--- CHAT HISTORY ---{history_context}\n--- NEW QUESTION ---\n{ai_query}"
                                response = client.models.generate_content(
                                    model='gemini-2.0-flash',
                                    contents=full_prompt
                                )
                                
                                # Increment usage in Firestore BEFORE adding to history
                                increment_ai_usage(user_id, key_suffix)
                                
                                st.session_state[history_key].append({
                                    "q": ai_query,
                                    "a": response.text
                                })
                                st.rerun()
                        except Exception as e:
                            st.error(f"AI Error: {str(e)}")
        
        # Show remaining (from Firestore)
        st.markdown(f'<div class="gemini-remaining">{remaining} {t({"de": "Fragen verbleibend", "en": "questions remaining"})}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="gemini-remaining">{t({"de": "Fragenlimit erreicht", "en": "Question limit reached"})}</div>', unsafe_allow_html=True)
