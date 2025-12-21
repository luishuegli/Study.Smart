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
    
    # ===== CONCEPT 1: Elementarereignis (Interactive Canvas) =====
    st.markdown("#### 1. Elementarereignis ($\omega$)")
    
    # Create a 2-column layout: Left=Theory, Right=Interaction
    col_c1_theory, col_c1_interact = st.columns([1, 1], gap="large")
    
    with col_c1_theory:
        with st.container(border=True):
            # Header
            st.markdown(f"""<div style="display: flex; align-items: center; gap: 12px; margin-bottom: 2px;">
                <div class="theory-icon">{render_icon("square")}</div>
                <div class="theory-title" style="margin: 0;">Was ist das?</div>
            </div>""", unsafe_allow_html=True)
            
            # Content (Native Markdown for LaTeX)
            st.markdown("""
            Ein **Elementarereignis** ist das kleinstmögliche, unteilbare Ergebnis eines Zufallsexperiments.
            
            **Beispiel:** Beim Würfelwurf ist jede einzelne Zahl (1, 2, 3, 4, 5, 6) ein Elementarereignis.
            """)

    with col_c1_interact:
        with st.container(border=True):
            st.markdown("**Experiment:** Würfel einmal.", unsafe_allow_html=True)
            
            if 'dice_result' not in st.session_state:
                st.session_state.dice_result = None
                
            # Interactive Button
            if st.button("Würfel werfen", key="dice_btn_interactive", type="primary", use_container_width=True):
                st.session_state.dice_result = np.random.randint(1, 7)
                st.rerun()

            # Result Display
            st.markdown("<div style='text-align: center; margin-top: 10px;'>", unsafe_allow_html=True)
            if st.session_state.dice_result:
                dice_svg_output = get_dice_svg(st.session_state.dice_result, 60)
                st.markdown(dice_svg_output, unsafe_allow_html=True)
                # LaTeX Result
                st.markdown(f"### $\omega = {st.session_state.dice_result}$")
                st.caption("Ein unteilbares Ergebnis.")
            else:
                 st.markdown(get_dice_svg(6, 60), unsafe_allow_html=True)
                 st.caption("Warte auf Wurf...")
            st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # ===== CONCEPT 2: Ereignisraum (Interactive Canvas) =====
    st.markdown("#### 2. Ereignisraum ($S$)")
    
    col_c2_theory, col_c2_interact = st.columns([1, 1], gap="large")
    
    with col_c2_theory:
         with st.container(border=True):
            st.markdown(f"""<div style="display: flex; align-items: center; gap: 12px; margin-bottom: 2px;">
                <div class="theory-icon">{render_icon("bar-chart")}</div>
                <div class="theory-title" style="margin: 0;">Die Gesamtheit</div>
            </div>""", unsafe_allow_html=True)
            
            st.markdown("""
            Der **Ereignisraum** ist die Menge aller möglichen Elementarereignisse.
            
            **Beispiel:** Beim Würfel ist $S = \{1, 2, 3, 4, 5, 6\}$.
            
            *Diskret* (abzählbar) vs. *Stetig* (Intervalle).
            """)
         
    with col_c2_interact:
        with st.container(border=True):
            st.markdown("**Mission:** Baue den Raum $S$. Klicke alle möglichen Ergebnisse an.")
            
            if 'selected_outcomes' not in st.session_state:
                st.session_state.selected_outcomes = set()

            # Grid of Buttons
            grid_cols = st.columns(3)
            for i in range(1, 7):
                col_idx = (i-1) % 3
                with grid_cols[col_idx]:
                     is_selected = i in st.session_state.selected_outcomes
                     if st.button(f"{i}", key=f"s_btn_{i}", type="primary" if is_selected else "secondary", use_container_width=True):
                         if is_selected: st.session_state.selected_outcomes.discard(i)
                         else: st.session_state.selected_outcomes.add(i)
                         st.rerun()

            # Feedback
            count = len(st.session_state.selected_outcomes)
            if count == 6:
                st.success("✅ Vollständig! $S = \{1,..,6\}$")
            elif count > 0:
                st.caption(f"Fortschritt: {count}/6 ausgewählt")
            
            # Reset visual spacing
            st.markdown("")

    st.markdown("<br>", unsafe_allow_html=True)

    # ===== CONCEPT 3: Ereignis (Interactive Canvas) =====
    st.markdown("#### 3. Ereignis ($A$)")
    
    col_c3_theory, col_c3_interact = st.columns([1, 1], gap="large")
    
    with col_c3_theory:
        with st.container(border=True):
            st.markdown(f"""<div style="display: flex; align-items: center; gap: 12px; margin-bottom: 2px;">
                <div class="theory-icon">{render_icon("filter")}</div>
                <div class="theory-title" style="margin: 0;">Die Auswahl</div>
            </div>""", unsafe_allow_html=True)
            
            st.markdown("""
            Ein **Ereignis** ist eine Teilmenge des Ereignisraums ($A \subseteq S$).
            
            **Beispiel:** "Gerade Zahl" ist $A = \{2, 4, 6\}$.
            """)
        
    with col_c3_interact:
        with st.container(border=True):
            st.markdown("**Mission:** Wähle das Ereignis 'Gerade Zahlen'.")
            
            if 'event_selection' not in st.session_state:
                st.session_state.event_selection = set()

            # Grid of Buttons
            grid_cols_e = st.columns(3)
            for i in range(1, 7):
                col_idx_e = (i-1) % 3
                with grid_cols_e[col_idx_e]:
                     is_in_event = i in st.session_state.event_selection
                     if st.button(f"{i}", key=f"e_btn_{i}", type="primary" if is_in_event else "secondary", use_container_width=True):
                         if is_in_event: st.session_state.event_selection.discard(i)
                         else: st.session_state.event_selection.add(i)
                         st.rerun()
                         
            # Dynamic Equation Display
            if st.session_state.event_selection:
                sorted_sel = sorted(list(st.session_state.event_selection))
                # Using standard markdown for equation
                st.markdown(f"##### $A = \\{{ {', '.join(map(str, sorted_sel))} \\}}$")
                
                if st.session_state.event_selection == {2, 4, 6}:
                    st.success("✅ Korrekt! $A = \{2, 4, 6\}$")
    
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
