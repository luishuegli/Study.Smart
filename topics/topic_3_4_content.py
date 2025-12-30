import streamlit as st
import plotly.graph_objects as go
import numpy as np
from views.styles import render_icon
from utils.localization import t
from utils.quiz_helper import render_mcq
from data.exam_questions import get_question
from utils.progress_tracker import track_question_answer, update_local_progress

# --- CONTENT DICTIONARY ---
content_3_4 = {
    "title": {"de": "3.4 Erwartungswerte", "en": "3.4 Expected Values"},
    "anchor": {"de": "Wo ist der Schwerpunkt?", "en": "Where is the center of mass?"},
    "intro": {
        "text": {
            "de": "Stell dir eine Wippe vor. Auf den Zahlen 1, 2, 3... liegen Gewichte (die Wahrscheinlichkeiten). Der Erwartungswert $E(X)$ ist genau der Punkt, an dem du die Wippe stützen musst, damit sie perfekt balanciert.",
            "en": "Imagine a seesaw. Weights (probabilities) are placed on numbers 1, 2, 3... The Expected Value $E(X)$ is exactly the point where you must support the seesaw so it balances perfectly."
        }
    },
    "playground": {
        "title": {"de": "Die Wahrscheinlichkeits-Wippe", "en": "The Probability Seesaw"},
        "desc": {
            "de": "Bewege das Dreieck (den Stützpunkt), bis die Wippe im Gleichgewicht ist. Die 'Hebelkraft' (Drehmoment) links und rechts muss gleich sein.",
            "en": "Move the triangle (fulcrum) until the seesaw is balanced. The 'leverage' (torque) on the left and right must be equal."
        },
        "metric_torque": {"de": "Netto-Drehmoment", "en": "Net Torque"}
    },
    "theory": {
        "def_title": {"de": "Definition", "en": "Definition"},
        "def_text": {
            "de": "Der Erwartungswert ist der gewichtete Durchschnitt aller möglichen Werte. Er ist der 'Schwerpunkt' der Verteilung.",
            "en": "The Expected Value is the weighted average of all possible values. It is the 'center of mass' of the distribution."
        },
        "formula_disc": r"E(X) = \sum_{i} x_i \cdot P(X=x_i)",
        "formula_cont": r"E(X) = \int_{-\infty}^{\infty} x \cdot f(x) \, dx"
    },
    "mission": {
        "title": {"de": "Mission: Der Portfolio-Manager", "en": "Mission: The Portfolio Manager"},
        "briefing": {
            "de": "Du hast zwei Aktien. Aktie A: 50% Chance auf +20%, 50% auf -10%. Aktie B: 90% Chance auf +5%, 10% auf -50%.",
            "en": "You have two stocks. Stock A: 50% chance of +20%, 50% of -10%. Stock B: 90% chance of +5%, 10% of -50%."
        },
        "task": {
            "de": "Welche Aktie hat den höheren Erwartungswert? Berechne ihn und wähle die richtige Strategie.",
            "en": "Which stock has the higher expected value? Calculate it and choose the correct strategy."
        },
        "success": {
            "de": "Richtig analysiert! Langfristig gewinnt Mathe.",
            "en": "Correctly analyzed! In the long run, math wins."
        }
    },
    "pro_tip": {
        "text": {
            "de": "Der Erwartungswert muss NICHT einer der möglichen Werte sein! Beim Würfeln ist der Durchschnitt 3.5, obwohl du nie eine 3.5 würfeln kannst.",
            "en": "The Expected Value does NOT have to be one of the possible values! When rolling a die, the average is 3.5, even though you can never roll a 3.5."
        }
    }
}

def render_subtopic_3_4(model):
    """3.4 Expected Values - The Seesaw Metaphor"""
    
    # --- CSS INJECTION ---
    st.markdown("""
    <style>
    [data-testid="stHorizontalBlock"] { align-items: stretch !important; }
    
    /* Slider Colors for Seesaw */
    .stSlider:has([aria-label*="Fulcrum"]) div[data-baseweb="slider"] > div:first-child > div:first-child { background-color: #FF9500 !important; }
    .stSlider:has([aria-label*="Fulcrum"]) div[role="slider"] { border: 2px solid #FF9500 !important; }
    </style>
    """, unsafe_allow_html=True)

    st.header(t(content_3_4["title"]))
    st.markdown(f"**{t(content_3_4['anchor'])}**")
    st.markdown("---")

    # --- INTUITION ---
    with st.container(border=True):
        st.markdown(f"### {render_icon('lightbulb', '#F59E0B')} {t({'de': 'Die Intuition', 'en': 'The Intuition'})}", unsafe_allow_html=True)
        st.markdown(t(content_3_4["intro"]["text"]))
    
    st.markdown("<br>", unsafe_allow_html=True)

    # --- PLAYGROUND: SEESAW ---
    st.markdown(f"### {t(content_3_4['playground']['title'])}")
    with st.container(border=True):
        st.caption(t(content_3_4["playground"]["desc"]))

        # Setup Weights (Fixed scenario for simplicity)
        # Weights at x=2 (Mass 4), x=5 (Mass 1), x=8 (Mass 3)
        # Expected Value = (2*4 + 5*1 + 8*3) / (4+1+3) = (8+5+24)/8 = 37/8 = 4.625
        masses = [(2, 4), (5, 1), (8, 3)]
        true_ev = 4.625

        # State
        if "fulcrum_pos" not in st.session_state: st.session_state.fulcrum_pos = 2.0

        c_ctrl, c_vis = st.columns([1, 2], gap="large")

        with c_ctrl:
            fulcrum = st.slider(
                t({"de": "Stützpunkt verschieben", "en": "Move Fulcrum"}),
                0.0, 10.0, st.session_state.fulcrum_pos, 0.1,
                key="fulcrum_slider"
            )
            st.session_state.fulcrum_pos = fulcrum

            # Calculate Torque
            net_torque = sum([m * (x - fulcrum) for x, m in masses])

            # Display
            st.metric(t(content_3_4["playground"]["metric_torque"]), f"{net_torque:.2f}")
            
            if abs(net_torque) < 0.5:
                st.success(t({"de": "Im Gleichgewicht!", "en": "Balanced!"}))
            elif net_torque > 0:
                st.warning(t({"de": "Kippt nach rechts!", "en": "Tilting right!"}))
            else:
                st.warning(t({"de": "Kippt nach links!", "en": "Tilting left!"}))

        with c_vis:
            fig = get_seesaw_chart(masses, fulcrum)
            st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

    st.markdown("<br>", unsafe_allow_html=True)

    # --- THEORY ---
    c1, c2 = st.columns(2, gap="medium")
    with c1:
        with st.container(border=True):
            st.markdown(f"**{t(content_3_4['theory']['def_title'])}**")
            st.markdown(t(content_3_4["theory"]["def_text"]))
    with c2:
        with st.container(border=True):
            st.markdown("**Formel (Diskret & Stetig)**")
            st.latex(content_3_4["theory"]["formula_disc"])
            st.latex(content_3_4["theory"]["formula_cont"])

    st.markdown("<br>", unsafe_allow_html=True)

    # --- MISSION: PORTFOLIO MANAGER ---
    st.markdown(f"### {t(content_3_4['mission']['title'])}")
    with st.container(border=True):
        st.markdown(t(content_3_4["mission"]["briefing"]))

        # Calculate EV
        ev_a = 0.5 * 20 + 0.5 * (-10) # 10 - 5 = 5
        ev_b = 0.9 * 5 + 0.1 * (-50)  # 4.5 - 5 = -0.5

        # User Choice
        choice = st.radio(
            t(content_3_4["mission"]["task"]),
            ["Aktie A (Stock A)", "Aktie B (Stock B)"],
            horizontal=True
        )

        if st.button(t({"de": "Entscheidung prüfen", "en": "Check Decision"})):
            if "Aktie A" in choice: # Correct
                st.success(f"{t(content_3_4['mission']['success'])} E(A) = +5%, E(B) = -0.5%")
                st.balloons()
                
                # Track
                user = st.session_state.get("user")
                if user:
                    track_question_answer(user["localId"], "vwl", "3", "3.4", "3_4_mission", True)
                    update_local_progress("3", "3.4", "3_4_mission", True)
                    st.rerun()
            else:
                st.error(t({"de": "Vorsicht! Rechne nochmal nach.", "en": "Careful! Calculate again."}))
                st.markdown(f"E(B) = $0.9 \\cdot 5 + 0.1 \\cdot (-50)$ ...")

    st.markdown("<br>", unsafe_allow_html=True)

    # --- PRO TIP ---
    st.markdown(f"""
    <div style="background-color: #fef3c7; border-radius: 8px; padding: 12px; color: #92400e;">
        <strong>Pro Tip:</strong> {t(content_3_4['pro_tip']['text'])}
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # --- EXAM PRACTICE ---
    st.markdown(f"### {t({'de': 'Prüfungstraining', 'en': 'Exam Practice'})}")

    questions = ["hs2024_mc7", "hs2024_mc12"]
    for q_id in questions:
        q_data = get_question("3.4", q_id)
        if q_data:
            with st.container(border=True):
                st.caption(q_data.get("source", ""))
                opts = q_data.get("options", [])
                if opts and isinstance(opts[0], dict):
                    option_labels = [t(o) for o in opts]
                else:
                    option_labels = opts

                render_mcq(
                    key_suffix=f"3_4_{q_id}",
                    question_text=t(q_data["question"]),
                    options=option_labels,
                    correct_idx=q_data["correct_idx"],
                    solution_text_dict=q_data["solution"],
                    success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                    error_msg_dict={"de": "Falsch.", "en": "Incorrect."},
                    client=model,
                    ai_context=f"Expected Value Question {q_id}",
                    course_id="vwl", topic_id="3", subtopic_id="3.4", question_id=f"3_4_{q_id}"
                )
            st.markdown("<br>", unsafe_allow_html=True)

def get_seesaw_chart(masses, fulcrum):
    """Seesaw Visualization."""
    fig = go.Figure()

    # 1. The Beam (Plank)
    beam_len = 10
    # Rotation Angle (proportional to torque, clamped)
    net_torque = sum([m * (x - fulcrum) for x, m in masses])
    angle = np.clip(net_torque * -2, -20, 20) # Degrees. neg torque -> left down (pos angle) ?
    # Actually: Positive torque (right heavy) -> Clockwise (negative angle)
    # If torque > 0 (right heavy), beam should dip right (y < 0 on right).
    angle = np.clip(net_torque * -2, -20, 20)

    # Coordinate Transform
    rad = np.radians(angle)
    c, s = np.cos(rad), np.sin(rad)

    # Beam Coords relative to fulcrum (0,0 locally)
    # Beam goes from 0 to 10 in global coords.
    # Local coords: x_local = x_global - fulcrum

    x_left = 0 - fulcrum
    x_right = 10 - fulcrum

    # Rotate
    x0_rot = x_left * c
    y0_rot = x_left * s
    x1_rot = x_right * c
    y1_rot = x_right * s

    # Shift back to fulcrum plot position
    # Plot origin (0,0) is fulcrum bottom? Let's say fulcrum tip is at (fulcrum, 1)
    tip_x, tip_y = fulcrum, 1.0

    fig.add_trace(go.Scatter(
        x=[tip_x + x0_rot, tip_x + x1_rot],
        y=[tip_y + y0_rot, tip_y + y1_rot],
        mode='lines',
        line=dict(color='#8E8E93', width=5)
    ))

    # 2. The Weights (Masses)
    for x_pos, mass in masses:
        # Distance from fulcrum
        dist = x_pos - fulcrum

        # Rotated position
        mx = dist * c
        my = dist * s

        # Final Plot Position
        px = tip_x + mx
        py = tip_y + my

        # Draw Circle
        r = mass * 0.1 # Size prop to mass
        fig.add_trace(go.Scatter(
            x=[px], y=[py + r], # Sit on top of beam
            mode='markers+text',
            marker=dict(size=mass*10, color='#007AFF'),
            text=str(mass),
            textposition="middle center",
            textfont=dict(color='white')
        ))

    # 3. The Fulcrum (Triangle)
    fig.add_trace(go.Scatter(
        x=[fulcrum - 0.5, fulcrum + 0.5, fulcrum, fulcrum - 0.5],
        y=[0, 0, 1, 0],
        fill="toself",
        fillcolor="#FF9500",
        line=dict(color="#FF9500"),
        mode='lines'
    ))

    fig.update_layout(
        xaxis=dict(range=[-1, 11], visible=False, fixedrange=True),
        yaxis=dict(range=[-2, 4], visible=False, fixedrange=True),
        margin=dict(l=0, r=0, t=0, b=0),
        height=250,
        showlegend=False,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )
    return fig
