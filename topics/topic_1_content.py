"""
Interactive Content for Topic 1: Grundlagen der Wahrscheinlichkeit
Brilliant.org-style learning experience with TechNoir theme
"""

import streamlit as st
import plotly.graph_objects as go
import numpy as np
from views.styles import render_icon

def get_dice_svg(number, size=48):
    """Generate SVG for dice faces 1-6 with dark mode support"""
    dots = {
        1: [(50, 50)],
        2: [(30, 30), (70, 70)],
        3: [(30, 30), (50, 50), (70, 70)],
        4: [(30, 30), (70, 30), (30, 70), (70, 70)],
        5: [(30, 30), (70, 30), (50, 50), (30, 70), (70, 70)],
        6: [(30, 30), (70, 30), (30, 50), (70, 50), (30, 70), (70, 70)]
    }
    
    svg = f'''<svg width="{size}" height="{size}" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg" class="dice-svg">
    <style>
        .dice-svg rect {{ fill: #f8fafc; stroke: #334155; }}
        .dice-svg circle {{ fill: #334155; }}
    </style>
    <rect width="100" height="100" rx="15" stroke-width="3"/>'''
    
    for x, y in dots[number]:
        svg += f'<circle cx="{x}" cy="{y}" r="8"/>'
    
    svg += '</svg>'
    return svg

def render_subtopic_1_1():
    """1.1 Ereignisse, Ereignisraum und Ereignismenge"""
    st.header("1.1 Ereignisse, Ereignisraum und Ereignismenge")
    
    # Section header with Lucide icon
    st.markdown(f'''<h3>{render_icon('book')} &nbsp; Theorie & Experimente</h3>''', unsafe_allow_html=True)
    st.markdown("*Lerne jedes Konzept und wende es sofort interaktiv an!*")
    
    # ===== CONCEPT 1: Elementarereignis =====
    st.markdown('<div class="theory-box">', unsafe_allow_html=True)
    col_icon, col_title = st.columns([0.1, 0.9])
    with col_icon:
        st.markdown(f'<div class="theory-icon">{render_icon("square")}</div>', unsafe_allow_html=True)
    with col_title:
        st.markdown('<div class="theory-title">Elementarereignis ($\omega$)</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="theory-content">
    Ein <strong>Elementarereignis</strong> ist das kleinstmögliche, unteilbare Ergebnis eines Zufallsexperiments.
    <br><br>
    <strong>Beispiel:</strong> Beim Würfelwurf ist jede einzelne Zahl (1, 2, 3, 4, 5, 6) ein Elementarereignis.
    </div>
    """, unsafe_allow_html=True)
    st.markdown(f'<div class="experiment-badge">{render_icon("beaker")} Jetzt ausprobieren</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Experiment 1
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        if 'dice_result' not in st.session_state:
            st.session_state.dice_result = None
        if 'dice_click_count' not in st.session_state:
            st.session_state.dice_click_count = 0
        
        # Create custom button with larger dice SVG
        dice_icon_svg = get_dice_svg(5, 40)
        
        st.markdown(f"""
        <div style="text-align: center; margin: 20px 0;">
            <div id="dice-button" style="
                display: inline-block;
                background: var(--secondary-background-color);
                border: 1px solid rgba(128, 128, 128, 0.2);
                border-radius: 12px;
                padding: 16px 32px;
                cursor: pointer;
                transition: all 0.2s;
                font-size: 16px;
                font-weight: 600;
                color: var(--text-color);
            " onmouseover="this.style.boxShadow='0 4px 12px rgba(0,0,0,0.1)'; this.style.transform='scale(1.05)';" onmouseout="this.style.boxShadow='none'; this.style.transform='scale(1)';">
                {dice_icon_svg} &nbsp; Würfel werfen
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Hidden button for actual functionality
        if st.button("Roll Dice", key="dice_btn_hidden", type="secondary", use_container_width=True):
            st.session_state.dice_result = np.random.randint(1, 7)
            st.session_state.dice_click_count += 1
            st.rerun()
        
        if st.session_state.dice_result:
            dice_svg_output = get_dice_svg(st.session_state.dice_result, 80)
            st.markdown(f"""
            <div style='background: var(--background-color); border: 1px solid rgba(128, 128, 128, 0.2);
                        padding: 32px; border-radius: 12px; text-align: center;
                        box-shadow: 0 8px 20px rgba(0,0,0,0.1); margin: 20px 0;'>
                <div style='margin-bottom: 16px;'>{dice_svg_output}</div>
                <div style='color: var(--text-color); font-size: 22px; font-weight: 600;'>
                    Elementarereignis: $\omega = {st.session_state.dice_result}$
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            st.success(f"**Erkenntnis:** Die Zahl **{st.session_state.dice_result}** ist ein einzelnes, unteilbares Ergebnis.")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # ===== CONCEPT 2: Ereignisraum =====
    st.markdown('<div class="theory-box">', unsafe_allow_html=True)
    col_icon, col_title = st.columns([0.1, 0.9])
    with col_icon:
        st.markdown(f'<div class="theory-icon">{render_icon("bar-chart")}</div>', unsafe_allow_html=True)
    with col_title:
        st.markdown('<div class="theory-title">Ereignisraum ($S$ oder $\Omega$)</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="theory-content">
    Der <strong>Ereignisraum</strong> ist die Menge aller möglichen Elementarereignisse eines Experiments.
    <br><br>
    <strong>Beispiel:</strong> Beim Würfel ist $S = \{1, 2, 3, 4, 5, 6\}$ – alle möglichen Ergebnisse.
    <br><br>
    <strong>Wichtig:</strong> Der Ereignisraum kann <em>diskret</em> (abzählbar, wie beim Würfel) oder <em>stetig</em> (unendlich viele Punkte, wie Wartezeit) sein.
    </div>
    """, unsafe_allow_html=True)
    st.markdown(f'<div class="experiment-badge">{render_icon("beaker")} Baue den Ereignisraum</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Experiment 2
    if 'selected_outcomes' not in st.session_state:
        st.session_state.selected_outcomes = set()
    
    st.markdown("**Aufgabe:** Welche Ergebnisse sind beim Würfelwurf möglich? Klicke alle an!")
    
    cols = st.columns(6)
    
    for i, col in enumerate(cols):
        with col:
            outcome = i + 1
            is_selected = outcome in st.session_state.selected_outcomes
            
            # Display dice SVG and number
            dice_svg = get_dice_svg(outcome, 48)
            st.markdown(f"""
            <div style="text-align: center; margin-bottom: 8px;">
                {dice_svg}
                <div style="margin-top: 8px; font-size: 18px; font-weight: 600;">{outcome}</div>
            </div>
            """, unsafe_allow_html=True)
            
            # Button for interaction
            if st.button(
                f"⠀",  # Invisible character
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
        st.success("✅ **Perfekt!** Du hast den vollständigen Ereignisraum $S = \{1, 2, 3, 4, 5, 6\}$ gebaut!")
        st.info("**Erkenntnis:** Der Ereignisraum ist die **Gesamtheit** aller möglichen Ergebnisse. Hier: **diskret** und **abzählbar**.")
    elif len(st.session_state.selected_outcomes) > 0:
        st.warning(f"Du hast {len(st.session_state.selected_outcomes)} von 6 ausgewählt. Fehlt noch etwas?")
    
    if st.button("↻ Zurücksetzen", key="reset_space"):
        st.session_state.selected_outcomes = set()
        st.rerun()
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # ===== CONCEPT 3: Ereignis =====
    st.markdown('<div class="theory-box">', unsafe_allow_html=True)
    col_icon, col_title = st.columns([0.1, 0.9])
    with col_icon:
        st.markdown(f'<div class="theory-icon">{render_icon("filter")}</div>', unsafe_allow_html=True)
    with col_title:
        st.markdown('<div class="theory-title">Ereignis ($A$)</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="theory-content">
    Ein <strong>Ereignis</strong> ist eine Teilmenge des Ereignisraums – eine Auswahl von Ergebnissen, die uns interessieren.
    <br><br>
    <strong>Beispiel:</strong> "Gerade Zahl würfeln" ist das Ereignis $A = \{2, 4, 6\}$ (eine Teilmenge von $S$).
    <br><br>
    <strong>Notation:</strong> $A \subseteq S$ ($A$ ist Teilmenge von $S$)
    </div>
    """, unsafe_allow_html=True)
    st.markdown(f'<div class="experiment-badge">{render_icon("target")} Definiere ein Ereignis</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Experiment 3
    if 'event_selection' not in st.session_state:
        st.session_state.event_selection = set()
    
    st.markdown("**Aufgabe:** Wähle alle geraden Zahlen aus!")
    
    cols = st.columns(6)
    
    for i, col in enumerate(cols):
        with col:
            outcome = i + 1
            is_in_event = outcome in st.session_state.event_selection
            
            # Display dice SVG and number
            dice_svg = get_dice_svg(outcome, 48)
            st.markdown(f"""
            <div style="text-align: center; margin-bottom: 8px;">
                {dice_svg}
                <div style="margin-top: 8px; font-size: 18px; font-weight: 600;">{outcome}</div>
            </div>
            """, unsafe_allow_html=True)
            
            # Button for interaction
            if st.button(
                f"⠀",  # Invisible character
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
        <div style='background: rgba(255, 255, 255, 0.05); border: 2px solid white; border-radius: 12px; 
                    padding: 24px; margin: 20px 0; text-align: center;'>
            <div style='font-size: 16px; color: #a5b4fc; font-weight: 600; margin-bottom: 12px;'>
                Dein Ereignis $A$:
            </div>
            <div style='font-size: 28px; font-weight: 700; color: #E0E0E0;'>
                $A = \{{ {", ".join(map(str, selected_list))} \}}$
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        if st.session_state.event_selection == {2, 4, 6}:
            st.success("✅ **Richtig!** Das Ereignis 'Gerade Zahl' ist $A = \{2, 4, 6\}$.")
            st.info("**Erkenntnis:** Ereignisse sind **Teilmengen** des Ereignisraums ($A \subseteq S$). Wir können beliebige Kombinationen wählen!")
        elif st.session_state.event_selection:
            st.info("💡 Sind das wirklich **alle** geraden Zahlen?")
    
    if st.button("↻ Zurücksetzen", key="reset_event"):
        st.session_state.event_selection = set()
        st.rerun()
    
    st.markdown("---")
    
    # SUMMARY
    st.markdown(f'<h3>{render_icon("file-text")} &nbsp; Zusammenfassung</h3>', unsafe_allow_html=True)
    st.markdown("""
    Du hast gelernt:
    
    - **Elementarereignis ($\omega$):** Ein einzelnes, unteilbares Ergebnis
    - **Ereignisraum ($S$):** Die Menge **aller** möglichen Elementarereignisse
    - **Ereignis ($A$):** Eine **Teilmenge** von $S$ ($A \subseteq S$)
    
    **Diskret vs. Stetig:**
    - **Diskret:** Abzählbare Ergebnisse (z.B. Würfel, Münze)
    - **Stetig:** Kontinuum, unendlich viele Punkte (z.B. Wartezeit, Temperatur)
    """)
    
    # 3. PRACTICE QUESTION
    st.markdown(f'<h3>{render_icon("check-circle")} &nbsp; Konzept-Check</h3>', unsafe_allow_html=True)
    
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
            st.markdown(f'<h3>{render_icon("bot")} &nbsp; Ask AI</h3>', unsafe_allow_html=True)
            
            ai_query = st.text_area(
                "Deine Frage:",
                placeholder="z.B. 'Warum ist Wartezeit stetig?' oder 'Was ist der Unterschied zwischen S und Omega?'",
                key=f"{q_key}_ai_input"
            )
            
            if st.button("Ask Theory Agent", key=f"{q_key}_ai_btn", type="primary"):
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
        
        if st.button("Frage zurücksetzen", key=f"{q_key}_retry", type="secondary"):
            st.session_state[f"{q_key}_submitted"] = False
            st.rerun()


# Main render function for Topic 1
def render_topic_1_content(subtopic_id=None):
    """Render content for Topic 1 based on selected subtopic"""
    
    if subtopic_id == "1.1" or subtopic_id is None:
        render_subtopic_1_1()
    else:
        st.info(f"Content for subtopic {subtopic_id} is under development.")
