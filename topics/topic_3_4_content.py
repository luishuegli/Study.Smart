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
        "title": {"de": "Mission: Der Hedge-Fonds-Manager", "en": "Mission: The Hedge Fund Manager"},
        "briefing": {
            "de": "Du verwaltest ein Portfolio. **Staatsanleihen (Safe)** bringen sichere **2%**. **Tech-Aktien (Risk)** haben eine 50/50 Chance auf **+20%** oder **-10%**.",
            "en": "You manage a portfolio. **Bonds (Safe)** yield a sure **2%**. **Tech Stocks (Risk)** have a 50/50 chance of **+20%** or **-10%**."
        },
        "task": {
            "de": "Mische das Portfolio so, dass du einen **Erwartungswert von exakt 5.0%** Rendite erzielst. Wie viel Prozent investierst du in Tech-Aktien?",
            "en": "Mix the portfolio to achieve an **Expected Return of exactly 5.0%**. What percentage do you invest in Tech Stocks?"
        },
        "success": {
            "de": "Ziel erreicht! Dein Portfolio ist perfekt ausbalanciert.",
            "en": "Target achieved! Your portfolio is perfectly balanced."
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
        masses = [(2, 4), (5, 1), (8, 3)]

        if "fulcrum_pos" not in st.session_state: st.session_state.fulcrum_pos = 2.0

        c_ctrl, c_vis = st.columns([1, 2], gap="large")

        with c_ctrl:
            fulcrum = st.slider(t({"de": "Stützpunkt verschieben", "en": "Move Fulcrum"}), 0.0, 10.0, st.session_state.fulcrum_pos, 0.1, key="fulcrum_slider")
            st.session_state.fulcrum_pos = fulcrum

            net_torque = sum([m * (x - fulcrum) for x, m in masses])
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

    # --- MISSION: HEDGE FUND MANAGER ---
    st.markdown(f"### {t(content_3_4['mission']['title'])}")
    with st.container(border=True):
        st.markdown(t(content_3_4["mission"]["briefing"]))

        # Safe Asset (Bonds): Return = 2%
        # Risky Asset (Tech): E(R) = 0.5*20 + 0.5*(-10) = 5%
        # Portfolio E(R) = w * E(Risk) + (1-w) * E(Safe)
        # Target = 5%? Wait. E(Risk) IS 5%. So to get 5% you need 100% Tech.
        # Let's make Target 3.5%.
        # 3.5 = w * 5 + (1-w) * 2 = 5w + 2 - 2w = 3w + 2 => 1.5 = 3w => w = 0.5 (50%)

        # Dynamic Text update based on calculation
        e_safe = 2.0
        e_risk = 0.5 * 20.0 + 0.5 * (-10.0) # 5.0

        target_return = 3.5

        if "mission_3_4_done" not in st.session_state: st.session_state.mission_3_4_done = False
        if "alloc_tech" not in st.session_state: st.session_state.alloc_tech = 0.0

        st.markdown(t({
            "de": "Ziel: Erreiche einen **Erwartungswert von 3.5%**.",
            "en": "Goal: Achieve an **Expected Return of 3.5%**."
        }))

        c_m_ctrl, c_m_res = st.columns([1, 1], gap="large")

        with c_m_ctrl:
            w_tech = st.slider(
                t({"de": "Anteil Tech-Aktien (%)", "en": "Tech Allocation (%)"}),
                0, 100, int(st.session_state.alloc_tech * 100), 5,
                key="alloc_slider"
            ) / 100.0
            st.session_state.alloc_tech = w_tech

        with c_m_res:
            port_ev = w_tech * e_risk + (1 - w_tech) * e_safe
            st.metric("Portfolio Expected Return", f"{port_ev:.1f}%", delta=f"{port_ev - target_return:.1f}%")

        # Win Condition
        if abs(port_ev - target_return) < 0.1:
            if not st.session_state.mission_3_4_done:
                st.balloons()
                st.session_state.mission_3_4_done = True
                user = st.session_state.get("user")
                if user:
                    track_question_answer(user["localId"], "vwl", "3", "3.4", "3_4_mission", True)
                    update_local_progress("3", "3.4", "3_4_mission", True)
                    st.rerun()
            st.success(t(content_3_4["mission"]["success"]))
        else:
            st.session_state.mission_3_4_done = False
            if port_ev < target_return:
                st.info(t({"de": "Zu wenig Rendite. Mehr Risiko wagen!", "en": "Return too low. Take more risk!"}))
            else:
                st.info(t({"de": "Zu viel Risiko. Mehr Staatsanleihen!", "en": "Too much risk. Buy more bonds!"}))

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
    fig = go.Figure()
    net_torque = sum([m * (x - fulcrum) for x, m in masses])
    angle = np.clip(net_torque * -2, -20, 20)
    rad = np.radians(angle)
    c, s = np.cos(rad), np.sin(rad)

    tip_x, tip_y = fulcrum, 1.0
    x_left, x_right = 0 - fulcrum, 10 - fulcrum

    fig.add_trace(go.Scatter(
        x=[tip_x + x_left * c, tip_x + x_right * c],
        y=[tip_y + x_left * s, tip_y + x_right * s],
        mode='lines', line=dict(color='#8E8E93', width=5)
    ))

    for x_pos, mass in masses:
        dist = x_pos - fulcrum
        px = tip_x + dist * c
        py = tip_y + dist * s
        r = mass * 0.1
        fig.add_trace(go.Scatter(
            x=[px], y=[py + r], mode='markers+text',
            marker=dict(size=mass*10, color='#007AFF'),
            text=str(mass), textposition="middle center", textfont=dict(color='white')
        ))

    fig.add_trace(go.Scatter(
        x=[fulcrum - 0.5, fulcrum + 0.5, fulcrum, fulcrum - 0.5],
        y=[0, 0, 1, 0], fill="toself", fillcolor="#FF9500", line=dict(color="#FF9500"), mode='lines'
    ))

    fig.update_layout(xaxis=dict(range=[-1, 11], visible=False, fixedrange=True), yaxis=dict(range=[-2, 4], visible=False, fixedrange=True), margin=dict(t=0, b=0), height=250, showlegend=False, paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
    return fig
