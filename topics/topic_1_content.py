"""
Interactive Content for Topic 1: Grundlagen der Wahrscheinlichkeit
Brilliant.org-style learning experience
"""

import streamlit as st
import plotly.graph_objects as go
import numpy as np


def render_subtopic_1_1():
    """1.1 Ereignisse, Ereignisraum und Ereignismenge"""
    st.header("1.1 Ereignisse, Ereignisraum und Ereignismenge")
    
    # Inject custom CSS - uses st.markdown with unsafe_allow_html
    st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
* {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
}

/* White buttons by default */
.stButton > button {
    background-color: white !important;
    background: white !important;
    color: #1f2937 !important;
    border: 2px solid #d1d5db !important;
    border-radius: 20px !important;
    font-weight: 500 !important;
    box-shadow: 0 1px 3px rgba(0,0,0,0.1) !important;
}

.stButton > button:hover {
    background-color: #f3f4f6 !important;
    border-color: #9ca3af !important;
}

/* Purple/indigo for primary buttons (selected dice) */
.stButton > button[data-testid="baseButton-primary"],
.stButton > button[kind="primary"] {
    background-color: #6366f1 !important;
    background: #6366f1 !important;
    color: white !important;
    border-color: #6366f1 !important;
}

.stButton > button[data-testid="baseButton-primary"]:hover {
    background-color: #4f46e5 !important;
}

/* Theory boxes */
.theory-box {
    background: white;
    border: 2px solid #e5e7eb;
    border-radius: 12px;
    padding: 28px 32px;
    margin: 24px 0;
    box-shadow: 0 1px 3px rgba(0,0,0,0.08);
}

.theory-box-header {
    display: flex;
    align-items: center;
    gap: 16px;
    margin-bottom: 20px;
    padding-bottom: 16px;
    border-bottom: 2px solid #f3f4f6;
}

.theory-icon {
    width: 56px;
    height: 56px;
    min-width: 56px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: #ecfeff;
    border-radius: 10px;
}

.theory-title {
    font-size: 22px;
    font-weight: 700;
    color: #0f172a;
}

.theory-content {
    color: #475569;
    line-height: 1.7;
    font-size: 15px;
    margin-bottom: 20px;
}

.experiment-badge {
    display: inline-block;
    background: #ecfeff;
    color: #0891b2;
    padding: 8px 16px;
    border-radius: 6px;
    font-size: 13px;
    font-weight: 600;
    margin-bottom: 16px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}
</style>
    """, unsafe_allow_html=True)
    
    st.subheader("📚 Theorie & Experimente")
    st.markdown("*Lerne jedes Konzept und wende es sofort interaktiv an!*")
    
    # ===== CONCEPT 1: Elementarereignis =====
    st.markdown("""
    <div class="theory-box">
        <div class="theory-box-header">
            <div class="theory-icon">
                <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="#14b8a6" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="18" x="3" y="3" rx="2" ry="2"/><path d="M12 12h.01"/></svg>
            </div>
            <div class="theory-title">Elementarereignis (ω)</div>
        </div>
        <div class="theory-content">
            Ein <strong>Elementarereignis</strong> ist das kleinstmögliche, unteilbare Ergebnis eines Zufallsexperiments.
            <br><br>
            <strong>Beispiel:</strong> Beim Würfelwurf ist jede einzelne Zahl (1, 2, 3, 4, 5, 6) ein Elementarereignis.
        </div>
        <div class="experiment-badge">🎲 Jetzt ausprobieren</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Experiment 1
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        if 'dice_result' not in st.session_state:
            st.session_state.dice_result = None
        
        if st.button("🎲 Würfel werfen", type="primary", use_container_width=True, key="dice_btn"):
            st.session_state.dice_result = np.random.randint(1, 7)
            st.rerun()
        
        if st.session_state.dice_result:
            dice_symbols = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]
            st.markdown(f"""
            <div style='background: linear-gradient(135deg, #14b8a6 0%, #0891b2 100%); 
                        padding: 32px; border-radius: 12px; text-align: center;
                        box-shadow: 0 8px 20px rgba(20, 184, 166, 0.2); margin: 20px 0;'>
                <div style='font-size: 80px; margin-bottom: 16px;'>{dice_symbols[st.session_state.dice_result - 1]}</div>
                <div style='color: white; font-size: 22px; font-weight: 600;'>
                    Elementarereignis: ω = {st.session_state.dice_result}
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            st.success(f"**Erkenntnis:** Die Zahl **{st.session_state.dice_result}** ist ein einzelnes, unteilbares Ergebnis.")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # ===== CONCEPT 2: Ereignisraum =====
    st.markdown("""
    <div class="theory-box">
        <div class="theory-box-header">
            <div class="theory-icon">
                <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="#14b8a6" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 3v18h18"/><path d="M18 17V9"/><path d="M13 17V5"/><path d="M8 17v-3"/></svg>
            </div>
            <div class="theory-title">Ereignisraum (S oder Ω)</div>
        </div>
        <div class="theory-content">
            Der <strong>Ereignisraum</strong> ist die Menge aller möglichen Elementarereignisse eines Experiments.
            <br><br>
            <strong>Beispiel:</strong> Beim Würfel ist <em>S = {1, 2, 3, 4, 5, 6}</em> – alle möglichen Ergebnisse.
            <br><br>
            <strong>Wichtig:</strong> Der Ereignisraum kann <em>diskret</em> (abzählbar, wie beim Würfel) oder <em>stetig</em> (unendlich viele Punkte, wie Wartezeit) sein.
        </div>
        <div class="experiment-badge">🧪 Baue den Ereignisraum</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Experiment 2
    if 'selected_outcomes' not in st.session_state:
        st.session_state.selected_outcomes = set()
    
    st.markdown("**Aufgabe:** Welche Ergebnisse sind beim Würfelwurf möglich? Klicke alle an!")
    
    cols = st.columns(6)
    dice_faces = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]
    
    for i, col in enumerate(cols):
        with col:
            outcome = i + 1
            is_selected = outcome in st.session_state.selected_outcomes
            
            if st.button(
                f"{dice_faces[i]}\n\n{outcome}",
                key=f"outcome_{outcome}",
                type="primary" if is_selected else "secondary",
                use_container_width=True
            ):
                if is_selected:
                    st.session_state.selected_outcomes.discard(outcome)
                else:
                    st.session_state.selected_outcomes.add(outcome)
                st.rerun()
    
    if len(st.session_state.selected_outcomes) == 6:
        st.success("✅ **Perfekt!** Du hast den vollständigen Ereignisraum **S = {1, 2, 3, 4, 5, 6}** gebaut!")
        st.info("**Erkenntnis:** Der Ereignisraum ist die **Gesamtheit** aller möglichen Ergebnisse. Hier: **diskret** und **abzählbar**.")
    elif len(st.session_state.selected_outcomes) > 0:
        st.warning(f"Du hast {len(st.session_state.selected_outcomes)} von 6 ausgewählt. Fehlt noch etwas?")
    
    if st.button("🔄 Zurücksetzen", key="reset_space"):
        st.session_state.selected_outcomes = set()
        st.rerun()
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # ===== CONCEPT 3: Ereignis =====
    st.markdown("""
    <div class="theory-box">
        <div class="theory-box-header">
            <div class="theory-icon">
                <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="#14b8a6" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="22 3 2 3 10 12.46 10 19 14 21 14 12.46 22 3"/></svg>
            </div>
            <div class="theory-title">Ereignis (A)</div>
        </div>
        <div class="theory-content">
            Ein <strong>Ereignis</strong> ist eine Teilmenge des Ereignisraums – eine Auswahl von Ergebnissen, die uns interessieren.
            <br><br>
            <strong>Beispiel:</strong> "Gerade Zahl würfeln" ist das Ereignis <em>A = {2, 4, 6}</em> (eine Teilmenge von S).
            <br><br>
            <strong>Notation:</strong> A ⊆ S (A ist Teilmenge von S)
        </div>
        <div class="experiment-badge">🎯 Definiere ein Ereignis</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Experiment 3
    st.markdown("**Aufgabe:** Wähle alle **geraden Zahlen** aus!")
    
    if 'event_selection' not in st.session_state:
        st.session_state.event_selection = set()
    
    dice_faces = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]
    event_cols = st.columns(6)
    for i, col in enumerate(event_cols):
        with col:
            outcome = i + 1
            is_in_event = outcome in st.session_state.event_selection
            
            if st.button(
                f"{dice_faces[i]}\n\n{outcome}",
                key=f"event_{outcome}",
                type="primary" if is_in_event else "secondary",
                use_container_width=True
            ):
                if is_in_event:
                    st.session_state.event_selection.discard(outcome)
                else:
                    st.session_state.event_selection.add(outcome)
                st.rerun()
    
    if st.session_state.event_selection:
        selected_list = sorted(list(st.session_state.event_selection))
        st.markdown(f"""
        <div style='background: #f0f9ff; border: 2px solid #0891b2; border-radius: 12px; 
                    padding: 24px; margin: 20px 0; text-align: center;'>
            <div style='font-size: 16px; color: #0891b2; font-weight: 600; margin-bottom: 12px;'>
                Dein Ereignis A:
            </div>
            <div style='font-size: 28px; font-weight: 700; color: #0f172a;'>
                A = {{{", ".join(map(str, selected_list))}}}
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        if st.session_state.event_selection == {2, 4, 6}:
            st.success("✅ **Richtig!** Das Ereignis 'Gerade Zahl' ist **A = {2, 4, 6}**.")
            st.info("**Erkenntnis:** Ereignisse sind **Teilmengen** des Ereignisraums (A ⊆ S). Wir können beliebige Kombinationen wählen!")
        elif st.session_state.event_selection:
            st.info("💡 Sind das wirklich **alle** geraden Zahlen?")
    
    if st.button("🔄 Zurücksetzen", key="reset_event"):
        st.session_state.event_selection = set()
        st.rerun()
    
    st.markdown("---")
    
    # SUMMARY
    st.subheader("📝 Zusammenfassung")
    st.markdown("""
    Du hast gelernt:
    
    - **Elementarereignis (ω):** Ein einzelnes, unteilbares Ergebnis
    - **Ereignisraum (S):** Die Menge **aller** möglichen Elementarereignisse
    - **Ereignis (A):** Eine **Teilmenge** von S (A ⊆ S)
    
    **Diskret vs. Stetig:**
    - **Diskret:** Abzählbare Ergebnisse (z.B. Würfel, Münze)
    - **Stetig:** Kontinuum, unendlich viele Punkte (z.B. Wartezeit, Temperatur)
    """)
    
    # 3. PRACTICE QUESTION
    st.subheader("📝 Konzept-Check")
    
    # Custom CSS for boxed answer choices with selection indication
    st.markdown("""
    <style>
    /* Style radio buttons as boxes */
    div[data-testid="stRadio"] > div {
        gap: 10px;
    }
    div[data-testid="stRadio"] > div > label {
        background-color: #f8f9fa;
        border: 2px solid #dee2e6;
        border-radius: 8px;
        padding: 12px 16px;
        cursor: pointer;
        transition: all 0.2s ease;
        display: block;
        width: 100%;
    }
    div[data-testid="stRadio"] > div > label:hover {
        border-color: #6366f1;
        background-color: #f0f0ff;
    }
    /* Selected state - highlight with color */
    div[data-testid="stRadio"] > div > label[data-baseweb="radio"] > div:first-child[aria-checked="true"] {
        background-color: #6366f1 !important;
    }
    div[data-testid="stRadio"] > div > label:has(input:checked) {
        border-color: #6366f1;
        background-color: #eef2ff;
        font-weight: 600;
    }
    </style>
    """, unsafe_allow_html=True)
    
    q_key = "q_1_1_stetig"
    if f"{q_key}_submitted" not in st.session_state:
        st.session_state[f"{q_key}_submitted"] = False
    
    st.markdown("**Frage:** Welcher der folgenden Ereignisräume $S$ ist stetig?")
    
    options = {
        "A": "$S = \\{1, 2, 3, 4, 5, 6\\}$ (Würfelwurf)",
        "B": "$S = \\{\\text{Kopf}, \\text{Zahl}\\}$ (Münzwurf)",
        "C": "$S = [0, \\infty)$ (Wartezeit an der Haltestelle)",
        "D": "$S = \\{0, 1, 2, \\dots\\}$ (Anzahl Kunden pro Tag)"
    }
    
    user_choice = st.radio(
        "Wähle eine Antwort:",
        list(options.keys()),
        format_func=lambda x: f"{x}: {options[x]}",
        key=f"{q_key}_radio",
        disabled=st.session_state[f"{q_key}_submitted"],
        label_visibility="collapsed"
    )
    
    if not st.session_state[f"{q_key}_submitted"]:
        if st.button("Antwort überprüfen", key=f"{q_key}_btn", type="primary"):
            st.session_state[f"{q_key}_submitted"] = True
            st.session_state[f"{q_key}_correct"] = (user_choice == "C")
            st.rerun()
    else:
        if st.session_state[f"{q_key}_correct"]:
            st.success("✅ **Richtig!** Stetige Räume beschreiben Messgrößen wie Zeit, Länge oder Temperatur.")
        else:
            st.error("❌ **Nicht ganz.** Stetige Räume sind Intervalle (z.B. $[0, \\infty)$), keine diskreten Punkte.")
        
        with st.expander("🔓 Lösung anzeigen", expanded=True):
            st.markdown("""
            **Antwort: (C)**
            
            Stetige Räume beschreiben **Messgrößen** wie:
            - Zeit (Wartezeit)
            - Länge
            - Temperatur
            
            Diskrete Räume beschreiben **Zählgrößen** oder Kategorien:
            - Würfelergebnisse (1, 2, 3...)
            - Anzahl Kunden (0, 1, 2...)
            - Münzwurf (Kopf/Zahl)
            """)
            
            # AI Q&A Feature (INSIDE the solution expander)
            st.markdown("---")
            st.markdown("### 🤖 Ask AI")
            
            ai_query = st.text_area(
                "Deine Frage:",
                placeholder="z.B. 'Warum ist Wartezeit stetig?' oder 'Was ist der Unterschied zwischen S und Omega?'",
                key=f"{q_key}_ai_input"
            )
            
            if st.button("Ask Theory Agent", key=f"{q_key}_ai_btn"):
                if ai_query:
                    # Import AI model
                    try:
                        import google.generativeai as genai
                        import os
                        from dotenv import load_dotenv
                        
                        load_dotenv()
                        api_key = os.getenv("GEMINI_API_KEY")
                        if api_key:
                            genai.configure(api_key=api_key)
                            model = genai.GenerativeModel('gemini-2.0-flash')
                            
                            # Build context-aware prompt
                            theory_context = f"""
                            You are a helpful statistics tutor.

                            --- STUDENT IS LEARNING THIS THEORY ---
                            Topic: Ereignisse, Ereignisraum und Ereignismenge (Events, Event Space, Event Sets)
                            
                            Key Concepts:
                            - Elementarereignis (ω): The smallest possible outcome (e.g., rolling a "3")
                            - Ereignisraum (S or Ω): The set of all possible outcomes
                            - Ereignis (A): A subset of the event space (collection of outcomes we care about)
                            
                            Types of Event Spaces:
                            - **Discrete**: Countable points (coin flip, dice roll)
                            - **Continuous**: Intervals, uncountable (waiting time, temperature)
                            
                            --- QUESTION FROM THE EXERCISE ---
                            "Which of the following event spaces S is continuous?"
                            Correct Answer: S = [0, ∞) (Waiting time at bus stop)
                            
                            --- USER QUESTION ---
                            "{ai_query}"
                            
                            Please answer in German, concisely and clearly, relating back to the concepts above.
                            """
                            
                            response = model.generate_content(theory_context)
                            st.markdown("**🤖 AI Theory Agent:**")
                            st.info(response.text)
                        else:
                            st.warning("AI feature requires API key configuration.")
                    except Exception as e:
                        st.error(f"AI Error: {str(e)}")
                else:
                    st.warning("Bitte gib eine Frage ein.")
        
        if st.button("Frage zurücksetzen", key=f"{q_key}_retry"):
            st.session_state[f"{q_key}_submitted"] = False
            st.rerun()


# Main render function for Topic 1
def render_topic_1_content(subtopic_id=None):
    """Render content for Topic 1 based on selected subtopic"""
    
    if subtopic_id == "1.1" or subtopic_id is None:
        render_subtopic_1_1()
    else:
        st.info(f"Content for subtopic {subtopic_id} is under development.")
