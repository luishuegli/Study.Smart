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
content_3_3 = {
    "title": {"de": "3.3 Stetige Zufallsvariablen", "en": "3.3 Continuous Random Variables"},
    "anchor": {
        "header": {"de": "Die Intuition", "en": "The Intuition"},
        "text": {"de": "Stell dir eine Dartscheibe vor. Die Wahrscheinlichkeit, einen *exakten* mathematischen Punkt zu treffen (z.B. genau 12.000000... mm vom Zentrum), ist praktisch Null. Aber die Wahrscheinlichkeit, eine *Fläche* zu treffen (z.B. den inneren Ring), ist größer als Null. Bei stetigen Variablen ist Wahrscheinlichkeit = Fläche.", "en": "Imagine a dartboard. The probability of hitting an *exact* mathematical point (e.g., exactly 12.000000... mm from the center) is practically zero. But the probability of hitting an *area* (e.g., the inner ring) is greater than zero. For continuous variables, Probability = Area."},
        "metaphor": {"de": "Der Flächen-Maler", "en": "The Area Painter"}
    },
    "theory": {
        "pdf_title": {"de": "Dichtefunktion (PDF)", "en": "Probability Density Function (PDF)"},
        "pdf_text": {"de": "Die Kurve f(x). Wahrscheinlichkeit ist das Integral (die Fläche) unter dieser Kurve.", "en": "The curve f(x). Probability is the integral (area) under this curve."},
        "prop_title": {"de": "Eigenschaften", "en": "Properties"},
        "prop_text": {"de": "1. f(x) ≥ 0 (nie negativ)\n2. Gesamtfläche = 1\n3. P(X=x) = 0 (Einzelpunkte haben keine Wahrscheinlichkeit)", "en": "1. f(x) ≥ 0 (never negative)\n2. Total Area = 1\n3. P(X=x) = 0 (Single points have zero probability)"},
        "formula": r"P(a \le X \le b) = \int_a^b f(x) dx"
    },
    "interactive": {
        "header": {"de": "Der Flächen-Simulator", "en": "The Area Simulator"},
        "desc": {"de": "Markiere einen Bereich [a, b]. Die blaue Fläche entspricht der Wahrscheinlichkeit.", "en": "Select a range [a, b]. The blue area corresponds to the probability."},
        "mission_title": {"de": "Mission: Der Wartezeit-Guru", "en": "Mission: The Waiting Time Guru"},
        "mission_desc": {"de": "Ein Bus kommt zufällig zwischen 0 und 10 Minuten. Die Dichte ist aber nicht gleichmäßig! Sie steigt an: je länger du wartest, desto wahrscheinlicher kommt er. f(x) = x/50. Finde den Zeitraum, in dem der Bus mit 36% Wahrscheinlichkeit kommt.", "en": "A bus arrives randomly between 0 and 10 minutes. But the density is not uniform! It increases: the longer you wait, the more likely it comes. f(x) = x/50. Find the time window where the bus arrives with 36% probability."}
    },
    "pro_tip": {
        "de": "Vorsicht: f(x) kann größer als 1 sein! Nur die *Fläche* (Integral) muss ≤ 1 sein. Eine sehr schmale, hohe Spitze ist erlaubt.",
        "en": "Caution: f(x) can be greater than 1! Only the *area* (integral) must be ≤ 1. A very narrow, tall peak is allowed."
    }
}

def render_subtopic_3_3(model):
    """3.3 Continuous Random Variables"""
    
    # --- CSS ---
    st.markdown("""
    <style>
    [data-testid="stHorizontalBlock"] { align-items: stretch !important; }
    [data-testid="column"] { display: flex !important; flex-direction: column !important; }
    [data-testid="column"] > div { flex: 1 !important; }
    </style>
    """, unsafe_allow_html=True)

    st.header(t(content_3_3["title"]))
    
    # INTUITION
    st.markdown(f"### {t(content_3_3['anchor']['header'])}")
    st.markdown(t(content_3_3["anchor"]["text"]))
    st.markdown("<br>", unsafe_allow_html=True)

    # THEORY
    c1, c2 = st.columns(2, gap="medium")
    with c1:
        with st.container(border=True):
            st.markdown(f"**{t(content_3_3['theory']['pdf_title'])}**")
            st.caption(t(content_3_3['theory']['pdf_text']))
            st.latex(content_3_3['theory']['formula'])

    with c2:
        with st.container(border=True):
            st.markdown(f"**{t(content_3_3['theory']['prop_title'])}**")
            st.caption(t(content_3_3['theory']['prop_text']))
            st.markdown(f"""
            <div style="text-align: center; margin-top: 10px;">
                {render_icon("activity", size=48, color="#007AFF")}
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # SIMULATOR
    render_simulator_3_3()

    # EXAM
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"### {t({'de': 'Prüfungstraining', 'en': 'Exam Practice'})}")
    
    # List of questions to include
    # 1. test2_q3 (Calculus)
    # 2. hs2015_mc2 (Theory - False statement) - from 3.1 pool
    # 3. uebung2_mc2 (Definition Continuous) - from 3.5 pool
    # 4. uebung2_mc7 (Density Constant) - from 3.5 pool
    
    q_ids = [
        ("3.3", "test2_q3"),
        ("3.1", "hs2015_mc2"),
        ("3.5", "uebung2_mc2"),
        ("3.5", "uebung2_mc7")
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
                    key_suffix=f"3_3_{qid}",
                    question_text=t(q_data["question"]),
                    options=option_labels,
                    correct_idx=q_data["correct_idx"],
                    solution_text_dict=q_data["solution"],
                    success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                    error_msg_dict={"de": "Falsch.", "en": "Incorrect."},
                    client=model,
                    ai_context="Continuous Random Variables",
                    course_id="vwl",
                    topic_id="3",
                    subtopic_id="3.3",
                    question_id=f"3_3_{qid}"
                )
            st.markdown("<br>", unsafe_allow_html=True)

def render_simulator_3_3():
    """
    Interactive Area Painter.
    PDF: f(x) = x/50 on [0, 10].
    Triangle distribution.
    """
    st.markdown(f"### {t(content_3_3['interactive']['mission_title'])}")

    with st.container(border=True):
        st.markdown(t(content_3_3['interactive']['mission_desc']))
        st.markdown("---")

        # State
        if "miss_3_3_a" not in st.session_state: st.session_state.miss_3_3_a = 0.0
        if "miss_3_3_b" not in st.session_state: st.session_state.miss_3_3_b = 5.0
        if "miss_3_3_done" not in st.session_state: st.session_state.miss_3_3_done = False

        target_prob = 0.36 # 36%

        # Logic
        # f(x) = x/50.
        # F(x) = x^2 / 100.
        # P(a <= X <= b) = F(b) - F(a) = (b^2 - a^2) / 100.

        c1, c2 = st.columns([1, 2], gap="large")

        with c1:
            st.markdown(f"**{t({'de': 'Zeitraum wählen', 'en': 'Select Time Window'})}**")

            val_range = st.slider(
                "Range [a, b]", 0.0, 10.0,
                (st.session_state.miss_3_3_a, st.session_state.miss_3_3_b),
                0.5,
                key="miss_3_3_range",
                disabled=st.session_state.miss_3_3_done
            )

            # Sync
            st.session_state.miss_3_3_a = val_range[0]
            st.session_state.miss_3_3_b = val_range[1]

            a, b = val_range
            curr_prob = (b**2 - a**2) / 100.0

            if abs(curr_prob - target_prob) < 0.01:
                st.success(t({"de": "Treffer! Genau 36%.", "en": "Hit! Exactly 36%."}))
                if not st.session_state.miss_3_3_done:
                    st.balloons()
                    st.session_state.miss_3_3_done = True
                    from utils.progress_tracker import track_question_answer, update_local_progress
                    user = st.session_state.get("user")
                    if user:
                        track_question_answer(user["localId"], "vwl", "3", "3.3", "3_3_mission", True)
                        update_local_progress("3", "3.3", "3_3_mission", True)
                        st.rerun()

                if st.button("Reset"):
                    st.session_state.miss_3_3_done = False
                    st.rerun()
            else:
                st.session_state.miss_3_3_done = False
                st.metric("Probability (Area)", f"{curr_prob:.2%}", delta=f"{curr_prob-target_prob:.1%}")

        with c2:
            # Dual Visualization: PDF (Top) and CDF (Bottom)
            x = np.linspace(0, 10, 100)
            y_pdf = x / 50.0
            y_cdf = (x**2) / 100.0

            fig = go.Figure()

            # 1. PDF Trace (Left Axis)
            fig.add_trace(go.Scatter(
                x=x, y=y_pdf,
                mode='lines', line=dict(color='#E5E5EA', width=2),
                fill='tozeroy', fillcolor='rgba(0,0,0,0)',
                name="PDF f(x)"
            ))

            # Highlight Area
            x_fill = np.linspace(a, b, 50)
            y_fill = x_fill / 50.0
            x_poly = np.concatenate(([a], x_fill, [b]))
            y_poly = np.concatenate(([0], y_fill, [0]))

            fig.add_trace(go.Scatter(
                x=x_poly, y=y_poly,
                fill='toself', fillcolor='rgba(0, 122, 255, 0.3)',
                line=dict(color='#007AFF', width=0),
                showlegend=False, hoverinfo='skip'
            ))

            # 2. CDF Trace (Right Axis)
            fig.add_trace(go.Scatter(
                x=x, y=y_cdf,
                mode='lines', line=dict(color='#AF52DE', width=3),
                name="CDF F(x)",
                yaxis="y2"
            ))

            # CDF Markers
            fig.add_trace(go.Scatter(
                x=[a, b], y=[a**2/100, b**2/100],
                mode='markers', marker=dict(color='#AF52DE', size=10, symbol='circle'),
                showlegend=False, yaxis="y2"
            ))

            fig.update_layout(
                title=dict(text=f"Area = {curr_prob:.2f}", x=0.5),
                xaxis=dict(range=[0, 10], title="Time (min)", fixedrange=True),
                yaxis=dict(
                    range=[0, 0.25], title="Density f(x)",
                    fixedrange=True, showgrid=False
                ),
                yaxis2=dict(
                    range=[0, 1.1], 
                    title=dict(text="Cumul. Prob F(x)", font=dict(color="#AF52DE")),
                    overlaying="y", side="right",
                    fixedrange=True, showgrid=False,
                    tickfont=dict(color="#AF52DE")
                ),
                height=350,
                margin=dict(l=50, r=50, t=40, b=30),
                showlegend=True,
                legend=dict(x=0, y=1.1, orientation="h"),
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
            )

            # Add annotation for calculation
            fig.add_annotation(
                text=f"F({b:.1f}) - F({a:.1f})",
                xref="paper", yref="paper",
                x=0.5, y=-0.25, showarrow=False,
                font=dict(size=12, color="#555")
            )

            st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

    # PRO TIP
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"""
    <div style="background-color: #fef3c7; border-radius: 8px; padding: 12px; color: #92400e;">
        <strong>Pro Tip:</strong> {t(content_3_3['pro_tip'])}
    </div>
    """, unsafe_allow_html=True)
