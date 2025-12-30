import streamlit as st
import numpy as np
import plotly.graph_objects as go
from views.styles import render_icon
from utils.localization import t
from utils.quiz_helper import render_mcq
from data.exam_questions import get_question

# ==========================================
# 1. CONTENT DICTIONARY
# ==========================================
content_3_4 = {
    "title": {"de": "3.4 Erwartungswerte", "en": "3.4 Expected Values"},
    "anchor": {
        "header": {"de": "Die Intuition", "en": "The Intuition"},
        "text": {"de": "Der Erwartungswert ist nichts anderes als der physikalische Schwerpunkt. Wenn du die Wahrscheinlichkeitsverteilung aus Pappe ausschneiden würdest, ist der Erwartungswert genau der Punkt, an dem du sie auf einer Nadelspitze balancieren kannst.", "en": "The expected value is nothing more than the physical center of gravity. If you were to cut the probability distribution out of cardboard, the expected value is exactly the point where you could balance it on a pinhead."},
        "metaphor": {"de": "Die Balkenwaage", "en": "The Balance Scale"}
    },
    "theory": {
        "def_title": {"de": "Definition E[X]", "en": "Definition E[X]"},
        "def_text": {"de": "Gewichteter Durchschnitt aller möglichen Werte.", "en": "Weighted average of all possible values."},
        "lin_title": {"de": "Linearität", "en": "Linearity"},
        "lin_text": {"de": "E[aX + b] = aE[X] + b. Das ist extrem nützlich!", "en": "E[aX + b] = aE[X] + b. This is extremely useful!"},
        "formula": r"E[X] = \sum x_i P(X=x_i) \quad \text{oder} \quad \int x f(x) dx"
    },
    "interactive": {
        "header": {"de": "Der Balance-Simulator", "en": "The Balance Simulator"},
        "desc": {"de": "Platziere Gewichte (Wahrscheinlichkeiten) auf dem Balken. Der rote Punkt zeigt den Schwerpunkt (Erwartungswert).", "en": "Place weights (probabilities) on the beam. The red dot shows the center of gravity (expected value)."},
        "mission_title": {"de": "Mission: Das Gleichgewicht", "en": "Mission: The Equilibrium"},
        "mission_desc": {"de": "Wir haben eine 'Masse' bei Position -4. Wo musst du eine doppelt so schwere Masse platzieren, damit der Schwerpunkt genau bei 0 liegt?", "en": "We have a 'mass' at position -4. Where must you place a mass that is twice as heavy so that the center of gravity is exactly at 0?"}
    },
    "pro_tip": {
        "de": "Der Erwartungswert muss NICHT 'erwartet' werden! Bei einem Würfelwurf ist E[X] = 3.5, obwohl man niemals eine 3.5 würfeln kann.",
        "en": "The expected value does NOT have to be 'expected'! For a die roll, E[X] = 3.5, even though you can never roll a 3.5."
    }
}

def render_subtopic_3_4(model):
    """3.4 Expected Values"""
    
    # --- CSS ---
    st.markdown("""
    <style>
    [data-testid="stHorizontalBlock"] { align-items: stretch !important; }
    [data-testid="column"] { display: flex !important; flex-direction: column !important; }
    [data-testid="column"] > div { flex: 1 !important; }
    </style>
    """, unsafe_allow_html=True)

    st.header(t(content_3_4["title"]))
    
    # INTUITION
    st.markdown(f"### {t(content_3_4['anchor']['header'])}")
    st.markdown(t(content_3_4["anchor"]["text"]))
    st.markdown("<br>", unsafe_allow_html=True)

    # THEORY
    c1, c2 = st.columns(2, gap="medium")
    with c1:
        with st.container(border=True):
            st.markdown(f"**{t(content_3_4['theory']['def_title'])}**")
            st.caption(t(content_3_4['theory']['def_text']))
            st.latex(content_3_4['theory']['formula'])

    with c2:
        with st.container(border=True):
            st.markdown(f"**{t(content_3_4['theory']['lin_title'])}**")
            st.caption(t(content_3_4['theory']['lin_text']))
            st.markdown(f"""
            <div style="text-align: center; margin-top: 10px;">
                {render_icon("target", size=48, color="#007AFF")}
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # SIMULATOR
    render_simulator_3_4()

    # EXAM
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"### {t({'de': 'Prüfungstraining', 'en': 'Exam Practice'})}")
    
    q_ids = [
        ("3.4", "hs2024_mc7"),
        ("3.4", "hs2024_mc12"),
        ("3.4", "hs2023_mc11"),
        ("3.4", "uebung2_prob5"),
        ("3.4", "hs2022_mc11"),
        ("3.5", "uebung2_mc3") # From 3.5 pool
    ]
    
    for tid, qid in q_ids:
        q_data = get_question(tid, qid)
        if q_data:
            with st.container(border=True):
                st.caption(q_data.get("source", ""))
                opts = q_data.get("options", [])
                if opts and isinstance(opts[0], dict):
                    option_labels = [t(o) for o in opts]
                else:
                    option_labels = opts

                render_mcq(
                    key_suffix=f"3_4_{qid}",
                    question_text=t(q_data["question"]),
                    options=option_labels,
                    correct_idx=q_data["correct_idx"],
                    solution_text_dict=q_data["solution"],
                    success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                    error_msg_dict={"de": "Falsch.", "en": "Incorrect."},
                    client=model,
                    ai_context="Expected Value",
                    course_id="vwl",
                    topic_id="3",
                    subtopic_id="3.4",
                    question_id=f"3_4_{qid}"
                )
            st.markdown("<br>", unsafe_allow_html=True)

def render_simulator_3_4():
    """
    Balance Beam Simulator.
    """
    st.markdown(f"### {t(content_3_4['interactive']['mission_title'])}")
    
    with st.container(border=True):
        st.markdown(t(content_3_4['interactive']['mission_desc']))
        st.markdown("---")

        # State
        if "miss_3_4_pos" not in st.session_state: st.session_state.miss_3_4_pos = 0.0
        if "miss_3_4_done" not in st.session_state: st.session_state.miss_3_4_done = False

        # Logic:
        # m1 = 1 at x1 = -4.
        # m2 = 2 at x2 = ?
        # Mean = (1*-4 + 2*x2) / (1+2) = 0
        # -4 + 2x2 = 0 => 2x2 = 4 => x2 = 2.

        c1, c2 = st.columns([1, 2], gap="large")

        with c1:
            st.markdown(f"**{t({'de': 'Position wählen', 'en': 'Select Position'})}**")

            pos_x = st.slider(
                "Position (Mass 2)", -5.0, 5.0,
                st.session_state.miss_3_4_pos, 0.5,
                key="miss_3_4_pos",
                disabled=st.session_state.miss_3_4_done
            )
            
            # Calc Mean
            # Mass 1: weight 1, pos -4
            # Mass 2: weight 2, pos pos_x
            mean_val = (1 * (-4) + 2 * pos_x) / 3.0

            if abs(mean_val - 0.0) < 0.1:
                st.success(t({"de": "Im Gleichgewicht!", "en": "Balanced!"}))
                if not st.session_state.miss_3_4_done:
                    st.balloons()
                    st.session_state.miss_3_4_done = True
                    from utils.progress_tracker import track_question_answer, update_local_progress
                    user = st.session_state.get("user")
                    if user:
                        track_question_answer(user["localId"], "vwl", "3", "3.4", "3_4_mission", True)
                        update_local_progress("3", "3.4", "3_4_mission", True)
                        st.rerun()
                
                if st.button("Reset 3.4"):
                    st.session_state.miss_3_4_done = False
                    st.session_state.miss_3_4_pos = 0.0
                    st.rerun()
            else:
                st.session_state.miss_3_4_done = False
                st.metric("Center of Gravity", f"{mean_val:.2f}", delta=f"{mean_val:.2f}")

        with c2:
            fig = go.Figure()

            # Beam
            fig.add_shape(type="line", x0=-5, y0=0, x1=5, y1=0, line=dict(color="black", width=4))

            # Fulcrum (at 0? No, fulcrum is the mean, we want mean at 0)
            # Actually, standard visual is fulcrum at 0 and check if it balances.
            # Here we visualize the Mean as a red dot.

            # Mass 1 (Fixed)
            fig.add_trace(go.Scatter(
                x=[-4], y=[0.2],
                mode='markers+text', marker=dict(size=20, color='#007AFF'),
                text=["1kg"], textposition="top center",
                name="Mass 1"
            ))

            # Mass 2 (Movable)
            fig.add_trace(go.Scatter(
                x=[pos_x], y=[0.4], # Higher to show it's heavier? Or larger size
                mode='markers+text', marker=dict(size=30, color='#AF52DE'), # Bigger
                text=["2kg"], textposition="top center",
                name="Mass 2"
            ))

            # Mean Marker
            fig.add_trace(go.Scatter(
                x=[mean_val], y=[0],
                mode='markers', marker=dict(symbol='triangle-up', size=15, color='red'),
                name="Mean"
            ))

            fig.update_layout(
                xaxis=dict(range=[-6, 6], title="Position", fixedrange=True),
                yaxis=dict(range=[-0.5, 1], visible=False, fixedrange=True),
                height=250,
                margin=dict(l=20, r=20, t=20, b=20),
                showlegend=False,
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
            )
            st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

    # PRO TIP
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"""
    <div style="background-color: #fef3c7; border-radius: 8px; padding: 12px; color: #92400e;">
        <strong>Pro Tip:</strong> {t(content_3_4['pro_tip'])}
    </div>
    """, unsafe_allow_html=True)
