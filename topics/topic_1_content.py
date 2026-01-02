"""
Interactive Content for Topic 1: Grundlagen der Wahrscheinlichkeit
Brilliant.org-style learning experience with TechNoir theme
"""

import streamlit as st
import plotly.graph_objects as go
import numpy as np
from views.styles import render_icon, inject_equal_height_css
from utils.localization import t
from utils.ai_helper import render_ai_tutor
from utils.quiz_helper import render_mcq
from data.exam_questions import get_question
from data.exam_questions import get_question

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

def render_subtopic_1_1(model):
    """1.1 Ereignisse, Ereignisraum und Ereignismenge"""
    inject_equal_height_css()
    # Header
    st.header(t({"de": "1.1 Ereignisse, Ereignisraum und Ereignismenge", "en": "1.1 Events, Sample Space and Sets"}))
    
    # ===== NEW: FOUNDATIONAL DEFINITIONS FROM SLIDES =====
    st.markdown(f"### {t({'de': 'Grundlegende Definitionen', 'en': 'Fundamental Definitions'})}")
    
    # Zufallsexperiment Definition (from slides p.8)
    with st.container(border=True):
        st.markdown(f"**{t({'de': 'Was ist ein Zufallsexperiment?', 'en': 'What is a Random Experiment?'})}**")
        st.markdown(t({
            "de": """
Ein Experiment ist ein **Zufallsexperiment**, wenn es:

1. Nach einer **bestimmten Vorschrift** ausgeführt wird
2. Unter gleichen Bedingungen **beliebig oft wiederholbar** ist
3. Das Ergebnis **ungewiss** ist und nicht vorausgesagt werden kann

*Beispiele: Würfelwurf, Münzwurf, Lottoziehung*
            """,
            "en": """
An experiment is a **random experiment** if:

1. It follows a **specific procedure**
2. It can be **repeated indefinitely** under the same conditions
3. The outcome is **uncertain** and cannot be predicted

*Examples: dice roll, coin flip, lottery draw*
            """
        }))
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Special Events (sichere/unmögliches Ereignis from slides p.17)
    c_sicher, c_unmog = st.columns(2, gap="medium")
    
    with c_sicher:
        with st.container(border=True):
            st.markdown(f"**{t({'de': 'Sicheres Ereignis', 'en': 'Certain Event'})}**")
            st.latex(r"S")
            st.markdown(t({
                "de": "Der gesamte Ereignisraum. Tritt **immer** ein.",
                "en": "The entire sample space. **Always** occurs."
            }))
            st.caption(t({"de": "Beispiel: 'Es fällt eine Zahl 1-6' beim Würfel", "en": "Example: 'A number 1-6 appears' on a die"}))
    
    with c_unmog:
        with st.container(border=True):
            st.markdown(f"**{t({'de': 'Unmögliches Ereignis', 'en': 'Impossible Event'})}**")
            st.latex(r"\emptyset")
            st.markdown(t({
                "de": "Die leere Menge. Tritt **niemals** ein.",
                "en": "The empty set. **Never** occurs."
            }))
            st.caption(t({"de": "Beispiel: 'Es fällt eine 7' beim Würfel", "en": "Example: 'A 7 appears' on a die"}))
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Section header with Lucide icon
    st.markdown(f"### {t({'de': 'Theorie & Experimente', 'en': 'Theory & Experiments'})}")
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
                
                **Beispiel:**
                
                Beim Würfelwurf ist jede einzelne Zahl (1, 2, 3, 4, 5, 6) ein Elementarereignis.
                """,
                "en": """
                An **Elementary Event** is the smallest possible, indivisible outcome of a random experiment.
                
                **Example:**
                
                In a die roll, each single number (1, 2, 3, 4, 5, 6) is an elementary event.
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
            if st.session_state.dice_result:
                dice_svg = get_dice_svg(st.session_state.dice_result, 60)
                caption_text = t({"de": "Ein unteilbares Ergebnis.", "en": "An indivisible outcome."})
                
                # Use a text-align center block which is often more robust in Streamlit markdown
                st.markdown(f"""
                <div style="width: 100%; text-align: center; margin-top: 16px; margin-bottom: 12px;">
                    <div style="display: inline-block; margin: 0 auto;">
                        {dice_svg}
                    </div>
                    <h3 style="margin: 8px 0 4px 0; text-align: center; font-family: 'Source Sans Pro', sans-serif;">&omega; = {st.session_state.dice_result}</h3>
                    <div style="color: rgba(49, 51, 63, 0.6); font-size: 14px; text-align: center;">{caption_text}</div>
                </div>
                """, unsafe_allow_html=True)
            else:
                 # HIDE initial state as requested
                 pass
    
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
                st.success(t({"de": "Vollständig! $S = \{1,..,6\}$", "en": "Complete! $S = \{1,..,6\}$"}))
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
                    st.success(t({"de": "Korrekt $A = \{2, 4, 6\}$", "en": "Correct $A = \{2, 4, 6\}$"}))
            st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    # SUMMARY
    st.markdown(f"### {t({'de': 'Zusammenfassung', 'en': 'Summary'})}")
    
    with st.container(border=True):
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
    st.markdown(f"### {t({'de': 'Konzept-Check', 'en': 'Concept Check'})}")
    
    q_key = "q_1_1_stetig"
    q_data = get_question("1.1", q_key)

    if q_data:
        # Context
        current_lang_full = "German" if st.session_state.lang == 'de' else "English"
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
        
        Please answer in {current_lang_full}, concisely and clearly, relating back to the concepts above.
        """
        
        # Prepare options (localize)
        # In central repo, options are dicts: {"id": "A", "de":..., "en":...}
        # Render_mcq expects list of strings if options are strings.
        # But here options are dicts with 'de'/'en'.
        # Let's see get_question logic for 1.1 in Step 2830.
        # Options: [{"id": "A", "de": ..., "en": ...}]
        # I need to format them.
        
        formatted_options = []
        for opt in q_data["options"]:
            # Localize
            text = t(opt) 
            formatted_options.append(text)

        with st.container(border=True):
            render_mcq(
                key_suffix=q_key,
                question_text=t(q_data["question"]),
                options=formatted_options,
                correct_idx=q_data["correct_idx"],
                solution_text_dict=q_data["solution"],
                success_msg_dict={
                    "de": "**Richtig!** Stetige Räume beschreiben Messgrößen wie Zeit, Länge oder Temperatur.",
                    "en": "**Correct** Continuous spaces describe measurements like time, length, or temperature."
                },
                error_msg_dict={
                    "de": "**Nicht ganz.** Stetige Räume sind Intervalle (z.B. $[0, \\infty)$), keine diskreten Punkte.",
                    "en": "**Not quite.** Continuous spaces are intervals (e.g. $[0, \\infty)$), not discrete points."
                },
                client=model,
                ai_context=theory_context,
                allow_retry=False,
                course_id="vwl",
                topic_id="1",
                subtopic_id="1.1",
                question_id="q_1_1_stetig"
            )


# Main render function for Topic 1
def render_topic_1_content(model, subtopic_id=None):
    """Render content for Topic 1 based on selected subtopic"""
    
    if subtopic_id == "1.1" or subtopic_id is None:
        render_subtopic_1_1(model)
    elif subtopic_id == "1.2":
        from topics.topic_1_2_content import render_subtopic_1_2
        render_subtopic_1_2(model)
    elif subtopic_id == "1.3":
        from topics.topic_1_3_content import render_subtopic_1_3
        render_subtopic_1_3(model)
    elif subtopic_id == "1.4":
        from topics.topic_1_4_content import render_subtopic_1_4
        render_subtopic_1_4(model)
    elif subtopic_id == "1.5":
        from topics.topic_1_5_content import render_subtopic_1_5
        render_subtopic_1_5(model)
    elif subtopic_id == "1.6":
        from topics.topic_1_6_content import render_subtopic_1_6
        render_subtopic_1_6(model)
    elif subtopic_id == "1.7":
        from topics.topic_1_7_content import render_subtopic_1_7
        render_subtopic_1_7(model)
    elif subtopic_id == "1.8":
        from topics.topic_1_8_content import render_subtopic_1_8
        render_subtopic_1_8(model)
    elif subtopic_id == "1.9":
        from topics.topic_1_9_content import render_subtopic_1_9
        render_subtopic_1_9(model)
    elif subtopic_id == "1.10":
        from topics.topic_1_10_content import render_subtopic_1_10
        render_subtopic_1_10(model)
    elif subtopic_id == "1.11":
        from topics.topic_1_11_content import render_subtopic_1_11
        render_subtopic_1_11(model)
    else:
        st.info(f"Content for subtopic {subtopic_id} is under development.")
