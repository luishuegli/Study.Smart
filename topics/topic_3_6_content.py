import streamlit as st
import numpy as np
import plotly.graph_objects as go
from views.styles import render_icon
from utils.localization import t
from utils.quiz_helper import render_mcq
from data.exam_questions import get_question
from statistics import NormalDist

# ==========================================
# 1. CONTENT DICTIONARY
# ==========================================
content_3_6 = {
    "title": {"de": "3.6 Quantile", "en": "3.6 Quantiles"},
    "anchor": {
        "header": {"de": "Die Intuition", "en": "The Intuition"},
        "text": {"de": "Stell dir vor, alle Menschen stellen sich der Größe nach auf. Wo musst du die Leine ziehen, damit genau 90% der Leute links davon stehen? Das ist das 90%-Quantil. Es ist der Umkehrschluss: Statt zu fragen 'Wie wahrscheinlich ist Wert X?', fragen wir 'Welcher Wert X trennt p% ab?'.", "en": "Imagine everyone lining up by height. Where do you draw the line so that exactly 90% of people are to the left? That is the 90% quantile. It's the reverse logic: Instead of asking 'How likely is value X?', we ask 'Which value X separates p%?'."},
        "metaphor": {"de": "Die VIP-Absperrung", "en": "The Velvet Rope"}
    },
    "theory": {
        "def_title": {"de": "Definition", "en": "Definition"},
        "def_text": {"de": "Das p-Quantil (oder Perzentil) $x_p$ ist der Wert, für den gilt: $F(x_p) = p$.", "en": "The p-quantile (or percentile) $x_p$ is the value such that $F(x_p) = p$."},
        "inv_title": {"de": "Inverse Funktion", "en": "Inverse Function"},
        "inv_text": {"de": "Es ist die Umkehrfunktion der Verteilungsfunktion: $x_p = F^{-1}(p)$.", "en": "It is the inverse of the cumulative distribution function: $x_p = F^{-1}(p)$."},
        "formula": r"x_p = F^{-1}(p)"
    },
    "interactive": {
        "header": {"de": "Der Perzentil-Picker", "en": "The Percentile Picker"},
        "desc": {"de": "Wähle einen Prozentsatz p. Der Simulator findet den 'Cut-Off'-Wert x, der genau p% der Fläche abschneidet.", "en": "Choose a percentage p. The simulator finds the 'cut-off' value x that cuts off exactly p% of the area."},
        "mission_title": {"de": "Mission: Der Hochbegabten-Club", "en": "Mission: The High IQ Club"},
        "mission_desc": {"de": r"IQ-Werte sind normalverteilt mit $\mu=100$ und $\sigma=15$. Um dem Club beizutreten, musst du zu den Top 2% gehören (also besser sein als 98%). Welchen IQ brauchst du?", "en": r"IQ scores are normally distributed with $\mu=100$ and $\sigma=15$. To join the club, you must be in the top 2% (better than 98%). What IQ do you need?"}
    },
    "pro_tip": {
        "de": "Median = 50%-Quantil. 1. Quartil = 25%-Quantil. 3. Quartil = 75%-Quantil. Der Interquartilsabstand (IQR) ist der Bereich zwischen den Quartilen.",
        "en": "Median = 50% quantile. 1st Quartile = 25% quantile. 3rd Quartile = 75% quantile. The Interquartile Range (IQR) is the distance between the quartiles."
    }
}

def render_subtopic_3_6(model):
    """3.6 Quantiles"""
    
    # --- CSS ---
    st.markdown("""
    <style>
    [data-testid="stHorizontalBlock"] { align-items: stretch !important; }
    [data-testid="column"] { display: flex !important; flex-direction: column !important; }
    [data-testid="column"] > div { flex: 1 !important; }
    </style>
    """, unsafe_allow_html=True)

    st.header(t(content_3_6["title"]))
    
    # INTUITION
    st.markdown(f"### {t(content_3_6['anchor']['header'])}")
    st.markdown(t(content_3_6["anchor"]["text"]))
    st.markdown("<br>", unsafe_allow_html=True)

    # THEORY
    c1, c2 = st.columns(2, gap="medium")
    with c1:
        with st.container(border=True):
            st.markdown(f"**{t(content_3_6['theory']['def_title'])}**")
            st.caption(t(content_3_6['theory']['def_text']))
            st.latex(content_3_6['theory']['formula'])

    with c2:
        with st.container(border=True):
            st.markdown(f"**{t(content_3_6['theory']['inv_title'])}**")
            st.caption(t(content_3_6['theory']['inv_text']))
            st.markdown(f"""
            <div style="text-align: center; margin-top: 10px;">
                {render_icon("git-pull-request", size=48, color="#007AFF")}
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # SIMULATOR
    render_simulator_3_6()

    # EXAM
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"### {t({'de': 'Prüfungstraining', 'en': 'Exam Practice'})}")
    
    # uebung2_mc14 and mc15 from 4.9 pool
    q_ids = [
        ("4.9", "uebung2_mc14"),
        ("4.9", "uebung2_mc15")
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
                    key_suffix=f"3_6_{qid}",
                    question_text=t(q_data["question"]),
                    options=option_labels,
                    correct_idx=q_data["correct_idx"],
                    solution_text_dict=q_data["solution"],
                    success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                    error_msg_dict={"de": "Falsch.", "en": "Incorrect."},
                    client=model,
                    ai_context="Quantiles",
                    course_id="vwl",
                    topic_id="3",
                    subtopic_id="3.6",
                    question_id=f"3_6_{qid}"
                )
            st.markdown("<br>", unsafe_allow_html=True)

def render_simulator_3_6():
    """
    Percentile Picker.
    """
    st.markdown(f"### {t(content_3_6['interactive']['mission_title'])}")
    
    with st.container(border=True):
        st.markdown(t(content_3_6['interactive']['mission_desc']))
        st.markdown("---")

        # State
        if "miss_3_6_p" not in st.session_state: st.session_state.miss_3_6_p = 50
        if "miss_3_6_done" not in st.session_state: st.session_state.miss_3_6_done = False

        # Logic: 98th percentile of N(100, 15).
        dist = NormalDist(mu=100, sigma=15)
        target_x = dist.inv_cdf(0.98) # approx 130.8

        c1, c2 = st.columns([1, 2], gap="large")

        with c1:
            st.markdown(f"**{t({'de': 'Perzentil wählen', 'en': 'Select Percentile'})}**")

            pct = st.slider(
                "Percentile (%)", 1, 99,
                st.session_state.miss_3_6_p, 1,
                key="miss_3_6_p",
                disabled=st.session_state.miss_3_6_done
            )
            
            p_val = pct / 100.0
            x_val = dist.inv_cdf(p_val)

            # Check win condition: Needs to be >= 98% (so >= 130.8)
            # Actually mission asks "What IQ do you need?".
            # If user sets slider to 98%, x_val is correct.

            if pct == 98:
                st.success(t({"de": f"Richtig! IQ > {x_val:.1f}.", "en": f"Correct! IQ > {x_val:.1f}."}))
                if not st.session_state.miss_3_6_done:
                    st.balloons()
                    st.session_state.miss_3_6_done = True
                    from utils.progress_tracker import track_question_answer, update_local_progress
                    user = st.session_state.get("user")
                    if user:
                        track_question_answer(user["localId"], "vwl", "3", "3.6", "3_6_mission", True)
                        update_local_progress("3", "3.6", "3_6_mission", True)
                        st.rerun()
                if st.button("Reset 3.6"):
                    st.session_state.miss_3_6_done = False
                    st.session_state.miss_3_6_p = 50
                    st.rerun()
            else:
                st.session_state.miss_3_6_done = False
                st.metric("IQ Score (Cut-Off)", f"{x_val:.1f}", delta=None)
                if pct < 98:
                    st.info(t({"de": "Zu niedrig. Du brauchst die Top 2%.", "en": "Too low. You need top 2%."}))
                else:
                    st.info(t({"de": "Zu hoch (Top 1% ist auch okay, aber wir suchen die Grenze 98%).", "en": "Too high (Top 1% is also okay, but we look for the 98% bound)."}))

        with c2:
            # Plot
            x = np.linspace(55, 145, 200)
            y = [dist.pdf(v) for v in x]
            
            fig = go.Figure()

            # Full PDF
            fig.add_trace(go.Scatter(
                x=x, y=y,
                mode='lines', line=dict(color='#E5E5EA', width=2),
                hoverinfo='skip'
            ))

            # Filled Area (Left of x_val)
            x_fill = [v for v in x if v <= x_val]
            y_fill = [dist.pdf(v) for v in x_fill]
            x_fill.append(x_val)
            y_fill.append(0)
            x_fill.insert(0, 55)
            y_fill.insert(0, 0)

            fig.add_trace(go.Scatter(
                x=x_fill, y=y_fill,
                fill='toself', fillcolor='rgba(0, 122, 255, 0.3)',
                line=dict(color='#007AFF', width=0),
                name=f"Bottom {pct}%"
            ))

            # Vertical Line
            fig.add_shape(type="line", x0=x_val, y0=0, x1=x_val, y1=max(y), line=dict(color="#007AFF", width=2))

            fig.update_layout(
                title=dict(text=f"IQ Distribution (Top {100-pct}%)", x=0.5),
                xaxis=dict(title="IQ Score", fixedrange=True),
                yaxis=dict(visible=False, fixedrange=True),
                height=300,
                margin=dict(l=20, r=20, t=40, b=20),
                showlegend=False,
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
            )
            st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

    # PRO TIP
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"""
    <div style="background-color: #fef3c7; border-radius: 8px; padding: 12px; color: #92400e;">
        <strong>Pro Tip:</strong> {t(content_3_6['pro_tip'])}
    </div>
    """, unsafe_allow_html=True)
