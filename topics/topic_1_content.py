"""
Interactive Content for Topic 1: Grundlagen der Wahrscheinlichkeit
Brilliant.org-style learning experience with TechNoir theme
"""

import streamlit as st
import plotly.graph_objects as go
import numpy as np
from views.styles import render_icon
from utils.localization import t

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
    # Header
    st.header(t({"de": "1.1 Ereignisse, Ereignisraum und Ereignismenge", "en": "1.1 Events, Sample Space and Sets"}))
    
    # Section header with Lucide icon
    st.markdown(f'''<h3>{render_icon('book')} &nbsp; {t({"de": "Theorie & Experimente", "en": "Theory & Experiments"})}</h3>''', unsafe_allow_html=True)
    st.markdown(f"*{t({'de': 'Lerne jedes Konzept und wende es sofort interaktiv an!', 'en': 'Learn each concept and apply it interactively immediately!'})}*")
    
    # ===== CONCEPT 1: Elementarereignis (Unified Capsule) =====
    with st.container(border=True):
        st.markdown(f"#### 1. {t({'de': 'Elementarereignis', 'en': 'Elementary Event'})} ($\omega$)")
        
        col_c1_theory, col_c1_interact = st.columns([1, 1], gap="large")
        
        with col_c1_theory:
            # Header
            st.markdown(f"""<div style="display: flex; align-items: center; gap: 12px; margin-bottom: 2px;">
                <div class="theory-icon">{render_icon("square")}</div>
                <div class="theory-title" style="margin: 0;">{t({"de": "Was ist das?", "en": "What is this?"})}</div>
            </div>""", unsafe_allow_html=True)
            
            # Content
            st.markdown(t({
                "de": """
                Ein **Elementarereignis** ist das kleinstmögliche, unteilbare Ergebnis eines Zufallsexperiments.
                
                **Beispiel:** Beim Würfelwurf ist jede einzelne Zahl (1, 2, 3, 4, 5, 6) ein Elementarereignis.
                """,
                "en": """
                An **Elementary Event** is the smallest possible, indivisible outcome of a random experiment.
                
                **Example:** In a die roll, each single number (1, 2, 3, 4, 5, 6) is an elementary event.
                """
            }))

        with col_c1_interact:
            # Action Zone Wrapper removed to fix empty space layout bug
            st.markdown(f"**{t({'de': 'Experiment', 'en': 'Experiment'})}:** {t({'de': 'Würfel einmal.', 'en': 'Roll once.'})}", unsafe_allow_html=True)
            
            if 'dice_result' not in st.session_state:
                st.session_state.dice_result = None
                
            # Interactive Button
            if st.button(t({"de": "Würfel werfen", "en": "Roll Dice"}), key="dice_btn_interactive", type="primary", use_container_width=True):
                st.session_state.dice_result = np.random.randint(1, 7)
                st.rerun()

            # Result Display
            st.markdown("<div style='text-align: center; margin-top: 10px;'>", unsafe_allow_html=True)
            if st.session_state.dice_result:
                dice_svg_output = get_dice_svg(st.session_state.dice_result, 60)
                st.markdown(dice_svg_output, unsafe_allow_html=True)
                st.markdown(f"### $\omega = {st.session_state.dice_result}$")
                st.caption(t({"de": "Ein unteilbares Ergebnis.", "en": "An indivisible outcome."}))
            else:
                 st.markdown(get_dice_svg(6, 60), unsafe_allow_html=True)
                 st.caption(t({"de": "Warte auf Wurf...", "en": "Waiting for roll..."}))
            st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # ===== CONCEPT 2: Ereignisraum (Unified Capsule) =====
    with st.container(border=True):
        st.markdown(f"#### 2. {t({'de': 'Ereignisraum', 'en': 'Sample Space'})} ($S$)")
        
        col_c2_theory, col_c2_interact = st.columns([1, 1], gap="large")
        
        with col_c2_theory:
            st.markdown(f"""<div style="display: flex; align-items: center; gap: 12px; margin-bottom: 2px;">
                <div class="theory-icon">{render_icon("bar-chart")}</div>
                <div class="theory-title" style="margin: 0;">{t({"de": "Die Gesamtheit", "en": "The Totality"})}</div>
            </div>""", unsafe_allow_html=True)
            
            st.markdown(t({
                "de": """
                Der **Ereignisraum** ist die Menge aller möglichen Elementarereignisse.
                
                **Beispiel:** Beim Würfel ist $S = \{1, 2, 3, 4, 5, 6\}$.
                
                *Diskret* (abzählbar) vs. *Stetig* (Intervalle).
                """,
                "en": """
                The **Sample Space** is the set of all possible elementary events.
                
                **Example:** For a die, $S = \{1, 2, 3, 4, 5, 6\}$.
                
                *Discrete* (countable) vs. *Continuous* (intervals).
                """
            }))
         
        with col_c2_interact:
            # Action Zone Wrapper removed
            st.markdown(f"**Mission:** {t({'de': 'Baue den Raum $S$.', 'en': 'Build space $S$.'})}", unsafe_allow_html=True)
            
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
            st.markdown("<div style='margin-top: 10px;'>", unsafe_allow_html=True)
            count = len(st.session_state.selected_outcomes)
            if count == 6:
                st.success(t({"de": "✅ Vollständig! $S = \{1,..,6\}$", "en": "✅ Complete! $S = \{1,..,6\}$"}))
            elif count > 0:
                st.caption(f"{t({'de': 'Fortschritt', 'en': 'Progress'})}: {count}/6")
            st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ===== CONCEPT 3: Ereignis (Unified Capsule) =====
    with st.container(border=True):
        st.markdown(f"#### 3. {t({'de': 'Ereignis', 'en': 'Event'})} ($A$)")
        
        col_c3_theory, col_c3_interact = st.columns([1, 1], gap="large")
        
        with col_c3_theory:
            st.markdown(f"""<div style="display: flex; align-items: center; gap: 12px; margin-bottom: 2px;">
                <div class="theory-icon">{render_icon("filter")}</div>
                <div class="theory-title" style="margin: 0;">{t({"de": "Die Auswahl", "en": "The Selection"})}</div>
            </div>""", unsafe_allow_html=True)
            
            st.markdown(t({
                "de": """
                Ein **Ereignis** ist eine Teilmenge des Ereignisraums ($A \subseteq S$).
                
                **Beispiel:** "Gerade Zahl" ist $A = \{2, 4, 6\}$.
                """,
                "en": """
                An **Event** is a subset of the sample space ($A \subseteq S$).
                
                **Example:** "Even Number" is $A = \{2, 4, 6\}$.
                """
            }))
        
        with col_c3_interact:
            # Action Zone Wrapper removed
            st.markdown(f"**Mission:** {t({'de': 'Wähle Gerade Zahlen.', 'en': 'Select Even Numbers.'})}", unsafe_allow_html=True)
            
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
            st.markdown("<div style='margin-top: 10px;'>", unsafe_allow_html=True)
            if st.session_state.event_selection:
                sorted_sel = sorted(list(st.session_state.event_selection))
                st.markdown(f"##### $A = \\{{ {', '.join(map(str, sorted_sel))} \\}}$")
                
                if st.session_state.event_selection == {2, 4, 6}:
                    st.success(t({"de": "✅ Korrekt! $A = \{2, 4, 6\}$", "en": "✅ Correct! $A = \{2, 4, 6\}$"}))
            st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    # SUMMARY
    st.markdown(f'<h3>{render_icon("file-text")} &nbsp; {t({"de": "Zusammenfassung", "en": "Summary"})}</h3>', unsafe_allow_html=True)
    st.markdown(t({
        "de": """
        Du hast gelernt:
        
        - **Elementarereignis ($\omega$):** Ein einzelnes, unteilbares Ergebnis
        - **Ereignisraum ($S$):** Die Menge **aller** möglichen Elementarereignisse
        - **Ereignis ($A$):** Eine **Teilmenge** von $S$ ($A \subseteq S$)
        
        **Diskret vs. Stetig:**
        - **Diskret:** Abzählbare Ergebnisse (z.B. Würfel, Münze)
        - **Stetig:** Kontinuum, unendlich viele Punkte (z.B. Wartezeit, Temperatur)
        """,
        "en": """
        You have learned:
        
        - **Elementary Event ($\omega$):** A single, indivisible outcome
        - **Sample Space ($S$):** The set of **all** possible outcomes
        - **Event ($A$):** A **subset** of $S$ ($A \subseteq S$)
        
        **Discrete vs. Continuous:**
        - **Discrete:** Countable outcomes (e.g., dice, coin)
        - **Continuous:** Continuum, infinite points (e.g., waiting time, temperature)
        """
    }))
    
    # 3. PRACTICE QUESTION
    st.markdown(f'<h3>{render_icon("check-circle")} &nbsp; {t({"de": "Konzept-Check", "en": "Concept Check"})}</h3>', unsafe_allow_html=True)
    
    q_key = "q_1_1_stetig"
    if f"{q_key}_submitted" not in st.session_state:
        st.session_state[f"{q_key}_submitted"] = False
    
    st.markdown(f"**{t({'de': 'Frage', 'en': 'Question'})}:** {t({'de': 'Welcher der folgenden Ereignisräume $S$ ist stetig?', 'en': 'Which of the following sample spaces $S$ is continuous?'})}")
    
    options = {
        "A": {
            "de": "$S = \{1, 2, 3, 4, 5, 6\}$ (Würfelwurf)",
            "en": "$S = \{1, 2, 3, 4, 5, 6\}$ (Die Roll)"
        },
        "B": {
            "de": "$S = \{\\text{Kopf}, \\text{Zahl}\}$ (Münzwurf)",
            "en": "$S = \{\\text{Heads}, \\text{Tails}\}$ (Coin Toss)"
        },
        "C": {
            "de": "$S = [0, \\infty)$ (Wartezeit an der Haltestelle)",
            "en": "$S = [0, \\infty)$ (Waiting time at bus stop)"
        },
        "D": {
            "de": "$S = \{0, 1, 2, \\dots\}$ (Anzahl Kunden pro Tag)",
            "en": "$S = \{0, 1, 2, \\dots\}$ (Number of customers per day)"
        }
    }
    
    # Determine language-specific options for display
    current_options = {k: t(v) for k, v in options.items()}
    
    user_choice = st.radio(
        t({"de": "Wähle eine Antwort:", "en": "Choose an answer:"}),
        list(current_options.keys()),
        format_func=lambda x: f"**{x}**: {current_options[x]}",
        key=f"{q_key}_radio",
        disabled=st.session_state[f"{q_key}_submitted"],
        label_visibility="collapsed"
    )
    
    if not st.session_state[f"{q_key}_submitted"]:
        if st.button(t({"de": "Antwort überprüfen", "en": "Check Answer"}), key=f"{q_key}_btn", type="primary"):
            st.session_state[f"{q_key}_submitted"] = True
            st.session_state[f"{q_key}_correct"] = (user_choice == "C")
            st.rerun()
    else:
        if st.session_state[f"{q_key}_correct"]:
            st.success(t({
                "de": "✅ **Richtig!** Stetige Räume beschreiben Messgrößen wie Zeit, Länge oder Temperatur.",
                "en": "✅ **Correct!** Continuous spaces describe measurements like time, length, or temperature."
            }))
        else:
            st.error(t({
                "de": "❌ **Nicht ganz.** Stetige Räume sind Intervalle (z.B. $[0, \\infty)$), keine diskreten Punkte.",
                "en": "❌ **Not quite.** Continuous spaces are intervals (e.g. $[0, \\infty)$), not discrete points."
            }))
        
        with st.expander(t({"de": "🔓 Lösung anzeigen", "en": "🔓 Show Solution"}), expanded=True):
            st.markdown(t({
                "de": """
                **Antwort: (C)**
                
                Stetige Räume beschreiben **Messgrößen** wie:
                - Zeit (Wartezeit)
                - Länge
                - Temperatur
                
                Diskrete Räume beschreiben **Zählgrößen** oder Kategorien:
                - Würfelergebnisse (1, 2, 3...)
                - Anzahl Kunden (0, 1, 2...)
                - Münzwurf (Kopf/Zahl)
                """,
                "en": """
                **Answer: (C)**
                
                Continuous spaces describe **measurements** like:
                - Time (Waiting time)
                - Length
                - Temperature
                
                Discrete spaces describe **counts** or categories:
                - Die results (1, 2, 3...)
                - Number of customers (0, 1, 2...)
                - Coin toss (Heads/Tails)
                """
            }))
            
            # AI Q&A Feature (INSIDE the solution expander)
            st.markdown("---")
            st.markdown(f'<h3>{render_icon("bot")} &nbsp; Ask AI</h3>', unsafe_allow_html=True)
            
            ai_query = st.text_area(
                t({"de": "Deine Frage:", "en": "Your Question:"}),
                placeholder=t({
                    "de": "z.B. 'Warum ist Wartezeit stetig?' oder 'Was ist der Unterschied zwischen S und Omega?'",
                    "en": "e.g., 'Why is waiting time continuous?' or 'What is the difference between S and Omega?'"
                }),
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
                            
                            current_lang_full = "German" if st.session_state.lang == 'de' else "English"
                            
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
                            
                            Please answer in {current_lang_full}, concisely and clearly, relating back to the concepts above.
                            """
                            
                            response = model.generate_content(theory_context)
                            st.markdown("**🤖 AI Theory Agent:**")
                            st.info(response.text)
                        else:
                            st.warning(t({"de": "AI feature requires API key configuration.", "en": "AI feature requires API key."}))
                    except Exception as e:
                        st.error(f"AI Error: {str(e)}")
                else:
                    st.warning(t({"de": "Bitte gib eine Frage ein.", "en": "Please enter a question."}))
        
        if st.button(t({"de": "Frage zurücksetzen", "en": "Reset Question"}), key=f"{q_key}_retry", type="secondary"):
            st.session_state[f"{q_key}_submitted"] = False
            st.rerun()


# Main render function for Topic 1
def render_topic_1_content(subtopic_id=None):
    """Render content for Topic 1 based on selected subtopic"""
    
    if subtopic_id == "1.1" or subtopic_id is None:
        render_subtopic_1_1()
    else:
        st.info(f"Content for subtopic {subtopic_id} is under development.")
