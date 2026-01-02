import streamlit as st
import numpy as np
import plotly.graph_objects as go
from views.styles import render_icon, inject_equal_height_css
from utils.localization import t
from utils.quiz_helper import render_mcq
from data.exam_questions import get_question
from utils.progress_tracker import track_question_answer, update_local_progress

# ==========================================
# 1. CONTENT DICTIONARY
# ==========================================
content_3_4 = {
    "title": {"de": "3.4 Erwartungswerte", "en": "3.4 Expected Values"},
    "anchor": {
        "header": {"de": "Die Intuition", "en": "The Intuition"},
        "text": {"de": "Stell dir vor, du schneidest deine Wahrscheinlichkeitsverteilung aus Pappe aus. Der Erwartungswert E(X) ist genau der Punkt, an dem du sie auf einer Nadelspitze balancieren könntest – der physikalische Schwerpunkt.", "en": "Imagine cutting your probability distribution out of cardboard. The expected value E(X) is exactly the point where you could balance it on a needle tip – the physical center of mass."},
    },
    "theory": {
        "def_title": {"de": "Definition", "en": "Definition"},
        "def_text": {"de": "Der gewichtete Durchschnitt aller möglichen Werte.", "en": "The weighted average of all possible values."},
        "discrete_formula": r"E[X] = \sum_{i} x_i \cdot P(X=x_i)",
        "continuous_formula": r"E[X] = \int_{-\infty}^{\infty} x \cdot f(x) \, dx",
        "lin_title": {"de": "Der Shortcut", "en": "The Shortcut"},
        "lin_text": {"de": "Die Linearitätseigenschaft ist extrem nützlich in Prüfungen!", "en": "The linearity property is extremely useful in exams!"},
        "lin_formula": r"E[aX + b] = a \cdot E[X] + b",
        "lin_formula2": r"E[X + Y] = E[X] + E[Y]",
        "lin_formula2_note": {"de": "(immer!)", "en": "(always!)"}
    },
    "interactive": {
        "header": {"de": "Der Balance-Simulator", "en": "The Balance Simulator"},
        "desc": {"de": "Platziere Wahrscheinlichkeiten auf dem Balken. Beobachte, wie sich der Schwerpunkt (E[X]) verschiebt.", "en": "Place probabilities on the beam. Watch how the center of mass (E[X]) shifts."},
    },
    "mission": {
        "title": {"de": "Mission: Der Casino-Berater", "en": "Mission: The Casino Consultant"},
        "desc": {"de": "Ein Casino bietet ein Würfelspiel an: Bei einer **6** gewinnt der Spieler **60€**. Bei jeder anderen Zahl gewinnt er **0€**. Deine Aufgabe: Finde den fairen Eintrittspreis, bei dem E[Gewinn] = 0.", "en": "A casino offers a dice game: On a **6**, the player wins **€60**. On any other number, they win **€0**. Your task: Find the fair entry price where E[Profit] = 0."},
        "target": 10.0,
        "hint": {"de": "Tipp: E[Gewinn] = (1/6)×60 + (5/6)×0 = ?", "en": "Hint: E[Win] = (1/6)×60 + (5/6)×0 = ?"}
    },
    "pro_tip": {
        "de": "E[X] muss KEIN möglicher Wert sein! Beim Würfeln ist E[X] = 3.5, obwohl man niemals eine 3.5 würfeln kann. Es ist der Langzeit-Durchschnitt, keine Vorhersage für einen Wurf.",
        "en": "E[X] does NOT have to be a possible value! When rolling a die, E[X] = 3.5, even though you can never roll 3.5. It's the long-run average, not a single-roll prediction."
    }
}

def render_subtopic_3_4(model):
    """3.4 Expected Values - Premium Implementation"""
    
    inject_equal_height_css()

    st.header(t(content_3_4["title"]))
    st.markdown(t({"de": "Wo liegt der Schwerpunkt?", "en": "Where is the balance point?"}))
    st.markdown("---")
    
    # --- INTUITION ---
    with st.container(border=True):
        st.markdown(f"### {t(content_3_4['anchor']['header'])}")
        st.markdown(t(content_3_4["anchor"]["text"]))
    
    st.markdown("<br>", unsafe_allow_html=True)

    # --- THEORY CARDS ---
    c1, c2 = st.columns(2, gap="medium")
    with c1:
        with st.container(border=True):
            st.markdown(f"**{t(content_3_4['theory']['def_title'])}**")
            st.caption(t(content_3_4['theory']['def_text']))
            st.markdown(f"**{t({'de': 'Diskret', 'en': 'Discrete'})}:**")
            st.latex(content_3_4['theory']['discrete_formula'])
            st.markdown(f"**{t({'de': 'Stetig', 'en': 'Continuous'})}:**")
            st.latex(content_3_4['theory']['continuous_formula'])

    with c2:
        with st.container(border=True):
            st.markdown(f"**{t(content_3_4['theory']['lin_title'])}**")
            st.caption(t(content_3_4['theory']['lin_text']))
            st.latex(content_3_4['theory']['lin_formula'])
            st.markdown("<br>", unsafe_allow_html=True)
            st.latex(content_3_4['theory']['lin_formula2'])
            st.caption(t(content_3_4['theory']['lin_formula2_note']))

    st.markdown("<br><br>", unsafe_allow_html=True)

    # --- BALANCE SIMULATOR ---
    render_balance_simulator()

    st.markdown("<br><br>", unsafe_allow_html=True)

    # --- MISSION: CASINO CONSULTANT ---
    render_casino_mission()

    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- PRO TIP ---
    st.markdown(f"""
    <div style="background-color: #f4f4f5; border-radius: 8px; padding: 12px; color: #3f3f46;">
        <strong>Pro Tip:</strong> {t(content_3_4['pro_tip'])}
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # --- EXAM PRACTICE ---
    st.markdown(f"### {t({'de': 'Prüfungstraining', 'en': 'Exam Practice'})}")
    
    questions = ["hs2024_mc7", "hs2024_mc12"]
    for q_key in questions:
        q_data = get_question("3.4", q_key)
        if q_data:
            with st.container(border=True):
                st.caption(q_data.get("source", ""))
                opts = q_data.get("options", [])
                if opts and isinstance(opts[0], dict):
                    option_labels = [t(o) for o in opts]
                else:
                    option_labels = opts
                
                render_mcq(
                    key_suffix=f"3_4_{q_key}",
                    question_text=t(q_data["question"]),
                    options=option_labels,
                    correct_idx=q_data["correct_idx"],
                    solution_text_dict=q_data["solution"],
                    success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                    error_msg_dict={"de": "Falsch.", "en": "Incorrect."},
                    client=model,
                    ai_context="Expected Value calculation",
                    course_id="vwl", topic_id="3", subtopic_id="3.4", question_id=f"3_4_{q_key}"
                )
            st.markdown("<br>", unsafe_allow_html=True)


def render_balance_simulator():
    """Interactive tilting balance beam - Find the target E[X]!"""
    
    st.markdown(f"### {t({'de': 'Mission: Der Balanceakt', 'en': 'Mission: The Balancing Act'})}")
    
    with st.container(border=True):
        st.markdown(t({
            "de": "Platziere Gewichte auf dem Balken, sodass **E[X] = 3.0** (perfekte Mitte)! Der Balken kippt je nach Schwerpunkt.",
            "en": "Place weights on the beam so that **E[X] = 3.0** (perfect center)! The beam tilts based on center of mass."
        }))
        st.markdown("---")
        
        # State initialization
        if "bal_mission_done" not in st.session_state: st.session_state.bal_mission_done = False
        
        # Handle reset - use default values for sliders
        reset_mode = st.session_state.get("bal_needs_reset", False)
        if reset_mode:
            st.session_state.bal_needs_reset = False
        
        # ASYMMETRIC starting values to ensure E[X] != 3.0 (the target)
        # These give E[X] ≈ 3.45, forcing the user to rebalance
        default_vals = [0.05, 0.10, 0.10, 0.25, 0.50]
        
        target_ex = 3.0
        
        # VISUALIZATION FIRST (Full Width)
        values = [1, 2, 3, 4, 5]
        
        # Use pills for quick weight selection (more gamified)
        st.markdown(f"**{t({'de': 'Klicke um Gewichte zu setzen:', 'en': 'Click to place weights:'})}**")
        
        cols = st.columns(5)
        probs = []
        for i, col in enumerate(cols):
            with col:
                # Use fresh key on reset to avoid session state conflict
                key_suffix = "_r" if reset_mode else ""
                p = st.slider(
                    f"X={i+1}", 0.0, 0.50, default_vals[i], 0.05,
                    key=f"bal_game_{i}{key_suffix}",
                    disabled=st.session_state.bal_mission_done
                )
                probs.append(p)
        
        
        total = sum(probs)
        
        # Calculate E[X] (normalized if needed)
        if total > 0:
            e_x = sum(x * p for x, p in zip(values, probs)) / total
        else:
            e_x = 3.0
        
        # Calculate tilt angle (max ±15 degrees)
        tilt_factor = (e_x - 3.0) * 10  # -20 to +20
        tilt_angle = max(-15, min(15, tilt_factor))
        
        # Create tilting beam visualization
        fig = go.Figure()
        
        # Calculate beam endpoints with tilt
        beam_length = 4
        y_center = 0.5
        rad = np.radians(tilt_angle)
        
        # Beam endpoints (rotated around center at x=3)
        x_left = 1 - (np.sin(rad) * 0.1)
        y_left = y_center - np.sin(rad) * beam_length / 2
        x_right = 5 + (np.sin(rad) * 0.1)
        y_right = y_center + np.sin(rad) * beam_length / 2
        
        # Draw the tilted beam
        fig.add_shape(
            type="line", x0=0.5, x1=5.5, y0=y_left, y1=y_right,
            line=dict(color="#333", width=6)
        )
        
        # Fulcrum (triangle at center)
        fig.add_trace(go.Scatter(
            x=[3], y=[0.2],
            mode='markers',
            marker=dict(size=30, symbol='triangle-up', color='#007AFF'),
            hoverinfo='skip',
            showlegend=False
        ))
        
        # Weights on the beam (positioned based on tilt)
        for i, (x, p) in enumerate(zip(values, probs)):
            y_offset = y_center + (x - 3) * np.sin(rad) * 0.5
            size = max(15, p * 100)
            fig.add_trace(go.Scatter(
                x=[x], y=[y_offset + 0.1],
                mode='markers+text',
                marker=dict(size=size, color='#FF9500' if p > 0.3 else '#34C759'),
                text=[f"{p:.0%}"] if p > 0 else [""],
                textposition='top center',
                textfont=dict(size=11, weight='bold'),
                hoverinfo='skip',
                showlegend=False
            ))
        
        # E[X] indicator
        e_x_y = y_center + (e_x - 3) * np.sin(rad) * 0.5
        fig.add_trace(go.Scatter(
            x=[e_x], y=[e_x_y - 0.15],
            mode='markers',
            marker=dict(size=16, symbol='triangle-down', color='#FF3B30'),
            hoverinfo='skip',
            showlegend=False
        ))
        
        fig.update_layout(
            xaxis=dict(range=[0, 6], tickmode='array', tickvals=[1,2,3,4,5], 
                      title="X", fixedrange=True, showgrid=False),
            yaxis=dict(range=[-0.2, 1.2], visible=False, fixedrange=True),
            height=220,
            margin=dict(l=20, r=20, t=10, b=40),
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)"
        )
        
        st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False}, key="tilt_beam")
        
        # Status display
        c_stat1, c_stat2, c_stat3 = st.columns(3)
        
        with c_stat1:
            delta_color = "normal" if abs(total - 1.0) < 0.02 else "inverse"
            st.metric(t({"de": "Summe", "en": "Sum"}), f"{total:.0%}", 
                     delta=f"{1.0-total:+.0%}" if abs(total-1.0) > 0.01 else None,
                     delta_color=delta_color)
        
        with c_stat2:
            st.metric("E[X]", f"{e_x:.2f}", 
                     delta=f"{e_x - target_ex:+.2f} vs {target_ex}",
                     delta_color="normal" if abs(e_x - target_ex) < 0.1 else "inverse")
        
        with c_stat3:
            if abs(e_x - target_ex) < 0.1 and abs(total - 1.0) < 0.02:
                if not st.session_state.bal_mission_done:
                    st.balloons()
                    st.session_state.bal_mission_done = True
                    user = st.session_state.get("user")
                    if user:
                        track_question_answer(user["localId"], "vwl", "3", "3.4", "3_4_balance", True)
                        update_local_progress("3", "3.4", "3_4_balance", True)
                        st.rerun()
                st.success(t({"de": "Perfekt balanciert!", "en": "Perfectly balanced!"}))
            else:
                if e_x < target_ex:
                    st.info(t({"de": "Kippt nach links!", "en": "Tilting left!"}))
                elif e_x > target_ex:
                    st.info(t({"de": "Kippt nach rechts!", "en": "Tilting right!"}))
        
        if st.session_state.bal_mission_done:
            if st.button(t({"de": "Nochmal spielen", "en": "Play again"}), key="reset_balance"):
                st.session_state.bal_mission_done = False
                st.session_state.bal_needs_reset = True
                st.rerun()


def render_casino_mission():
    """Casino Consultant mission - find fair entry price"""
    
    st.markdown(f"### {t(content_3_4['mission']['title'])}")
    
    with st.container(border=True):
        st.markdown(t(content_3_4['mission']['desc']))
        
        # State
        if "casino_fee" not in st.session_state: st.session_state.casino_fee = 5.0
        if "casino_done" not in st.session_state: st.session_state.casino_done = False
        
        c1, c2 = st.columns([1, 1], gap="large")
        
        with c1:
            st.markdown(f"**{t({'de': 'Eintrittspreis', 'en': 'Entry Fee'})}**")
            
            fee = st.slider(
                t({"de": "Preis in €", "en": "Price in €"}),
                0.0, 20.0, st.session_state.casino_fee, 1.0,
                key="casino_fee",
                disabled=st.session_state.casino_done
            )
            
            # E[Win] = (1/6) * 60 = 10
            # E[Profit] = E[Win] - Fee = 10 - Fee
            expected_win = 60 * (1/6)
            expected_profit = expected_win - fee
            
            st.metric(t({"de": "E[Gewinn] für Spieler", "en": "E[Profit] for player"}), f"€{expected_profit:.2f}")
        
        with c2:
            st.markdown("<br>", unsafe_allow_html=True)
            
            # Check win condition
            if abs(fee - 10.0) < 0.5:
                if not st.session_state.casino_done:
                    st.balloons()
                    st.session_state.casino_done = True
                    user = st.session_state.get("user")
                    if user:
                        track_question_answer(user["localId"], "vwl", "3", "3.4", "3_4_casino", True)
                        update_local_progress("3", "3.4", "3_4_casino", True)
                        st.rerun()
                st.success(t({"de": "Perfekt! Bei 10€ ist das Spiel fair.", "en": "Perfect! At €10, the game is fair."}))
                
                if st.button(t({"de": "Mission zurücksetzen", "en": "Reset Mission"}), key="reset_casino"):
                    st.session_state.casino_done = False
                    st.session_state.casino_fee = 5.0
                    st.rerun()
            else:
                st.session_state.casino_done = False
                if expected_profit > 0:
                    st.info(t({"de": "Zu billig! Der Spieler gewinnt durchschnittlich.", "en": "Too cheap! The player wins on average."}))
                else:
                    st.info(t({"de": "Zu teuer! Der Spieler verliert durchschnittlich.", "en": "Too expensive! The player loses on average."}))
        
        # Hint expander
        with st.expander(t({"de": "Hinweis anzeigen", "en": "Show hint"})):
            st.markdown(t(content_3_4['mission']['hint']))
