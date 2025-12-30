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
content_3_2 = {
    "title": {"de": "3.2 Diskrete Zufallsvariablen", "en": "3.2 Discrete Random Variables"},
    "anchor": {
        "header": {"de": "Die Intuition", "en": "The Intuition"},
        "text": {"de": "Stell dir Wahrscheinlichkeit als eine begrenzte Menge 'Knete' vor (insgesamt 1.0). Du verteilst diese Masse auf bestimmte Punkte (0, 1, 2...). Bei diskreten Variablen darfst du nichts verschütten - die Summe aller Häufchen muss exakt 1.0 sein.", "en": "Imagine probability as a limited amount of 'play-doh' (total 1.0). You distribute this mass onto specific points (0, 1, 2...). For discrete variables, you can't spill anything - the sum of all piles must be exactly 1.0."},
        "metaphor": {"de": "Der Massen-Bauer", "en": "The Mass Builder"}
    },
    "theory": {
        "pmf_title": {"de": "Wahrscheinlichkeitsfunktion (PMF)", "en": "Probability Mass Function (PMF)"},
        "pmf_text": {"de": "Ordnet jedem Wert x eine Wahrscheinlichkeit P(X=x) zu.", "en": "Assigns a probability P(X=x) to each value x."},
        "cdf_title": {"de": "Verteilungsfunktion (CDF)", "en": "Cumulative Distribution Function (CDF)"},
        "cdf_text": {"de": "Die Summe aller Wahrscheinlichkeiten bis x. Eine Treppenfunktion.", "en": "The sum of all probabilities up to x. A step function."},
        "norm_rule": r"\sum_{i} P(X=x_i) = 1"
    },
    "interactive": {
        "header": {"de": "Der Massen-Simulator", "en": "The Mass Simulator"},
        "desc": {"de": "Verteile die Wahrscheinlichkeit auf die Werte 1 bis 5. Die Summe muss 1.0 ergeben.", "en": "Distribute probability across values 1 to 5. The sum must equal 1.0."},
        "mission_title": {"de": "Mission: Der gezinkte Würfel", "en": "Mission: The Loaded Die"},
        "mission_desc": {"de": "Ein Casino beauftragt dich. Konstruiere einen Würfel, bei dem die **6** genau **3x so wahrscheinlich** ist wie jede andere Zahl. Die anderen Zahlen (1-5) sollen alle gleich wahrscheinlich sein.", "en": "A casino hires you. Construct a die where **6** is exactly **3x as likely** as any other number. The other numbers (1-5) should all be equally likely."}
    },
    "pro_tip": {
        "de": "Um P(a ≤ X ≤ b) zu berechnen, summiere einfach alle Balken in diesem Bereich. Oder nutze die CDF: F(b) - F(a-1) (Achtung auf die Grenzen!).",
        "en": "To calculate P(a ≤ X ≤ b), simply sum all bars in this range. Or use the CDF: F(b) - F(a-1) (Watch the boundaries!)."
    }
}

def render_subtopic_3_2(model):
    """3.2 Discrete Random Variables - High-Fidelity Dashboard"""
    
    # --- CSS INJECTION ---
    st.markdown("""
    <style>
    [data-testid="stHorizontalBlock"] { align-items: stretch !important; }
    [data-testid="column"] { display: flex !important; flex-direction: column !important; }
    [data-testid="column"] > div { flex: 1 !important; }
    </style>
    """, unsafe_allow_html=True)

    st.header(t(content_3_2["title"]))
    st.markdown(t({"de": "Wie modellieren wir Ereignisse, die man zählen kann?", "en": "How do we model events that can be counted?"}))
    
    # ROW 1: INTUITION
    st.markdown(f"### {t(content_3_2['anchor']['header'])}")
    st.markdown(t(content_3_2["anchor"]["text"]))
    st.markdown("<br>", unsafe_allow_html=True)

    # ROW 2: THEORY
    c1, c2 = st.columns(2, gap="medium")
    with c1:
        with st.container(border=True):
            st.markdown(f"**{t(content_3_2['theory']['pmf_title'])}**")
            st.caption(t(content_3_2['theory']['pmf_text']))
            st.latex(r"f(x) = P(X=x)")
            st.markdown(f"**Normierung:**")
            st.latex(content_3_2['theory']['norm_rule'])

    with c2:
        with st.container(border=True):
            st.markdown(f"**{t(content_3_2['theory']['cdf_title'])}**")
            st.caption(t(content_3_2['theory']['cdf_text']))
            st.latex(r"F(x) = \sum_{t \le x} f(t)")
            # Icon
            st.markdown(f"""
            <div style="text-align: center; margin-top: 10px;">
                {render_icon("bar-chart", size=48, color="#AF52DE")}
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ROW 3: SIMULATOR
    render_simulator_3_2()

    # EXAM SECTION
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"### {t({'de': 'Prüfungstraining', 'en': 'Exam Practice'})}")
    
    questions = ["uebung2_mc5", "test2_q4"]
    
    for q_key in questions:
        q_data = get_question("3.2", q_key)
        if q_data:
            with st.container(border=True):
                st.caption(q_data.get("source", ""))
                opts = q_data.get("options", [])
                if opts and isinstance(opts[0], dict):
                    option_labels = [t(o) for o in opts]
                else:
                    option_labels = opts

                render_mcq(
                    key_suffix=f"3_2_{q_key}",
                    question_text=t(q_data["question"]),
                    options=option_labels,
                    correct_idx=q_data["correct_idx"],
                    solution_text_dict=q_data["solution"],
                    success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                    error_msg_dict={"de": "Falsch.", "en": "Incorrect."},
                    client=model,
                    ai_context="Discrete Random Variables",
                    course_id="vwl",
                    topic_id="3",
                    subtopic_id="3.2",
                    question_id=f"3_2_{q_key}"
                )
            st.markdown("<br>", unsafe_allow_html=True)

def render_simulator_3_2():
    """
    Interactive Mass Builder (PMF).
    """
    # --- CSS SCOPED ---
    st.markdown("""
    <style>
    .stSlider:has([aria-label*="P(6)"]) div[data-baseweb="slider"] > div:first-child > div:first-child { background-color: #AF52DE !important; }
    .stSlider:has([aria-label*="P(6)"]) div[role="slider"] { background-color: #FFFFFF !important; border: 2px solid #AF52DE !important; }
    </style>
    """, unsafe_allow_html=True)

    st.markdown(f"### {t(content_3_2['interactive']['mission_title'])}")
    
    with st.container(border=True):
        st.markdown(t(content_3_2['interactive']['mission_desc']))
        st.markdown("---")

        # State
        if "miss_3_2_p_others" not in st.session_state: st.session_state.miss_3_2_p_others = 0.1
        if "miss_3_2_p6" not in st.session_state: st.session_state.miss_3_2_p6 = 0.1
        if "miss_3_2_done" not in st.session_state: st.session_state.miss_3_2_done = False

        # Logic: 5 * p_others + p6 = 1.0
        # Condition: p6 = 3 * p_others
        # Solution: 5p + 3p = 1 => 8p = 1 => p = 0.125. p6 = 0.375.

        # Controls
        c1, c2 = st.columns([1, 2], gap="large")

        with c1:
            st.markdown(f"**{t({'de': 'Einstellungen', 'en': 'Settings'})}**")
            
            p_others = st.slider(
                "P(1) = P(2) = ... = P(5)", 0.0, 0.3,
                st.session_state.miss_3_2_p_others, 0.005,
                key="miss_3_2_p_others",
                disabled=st.session_state.miss_3_2_done
            )
            
            p6 = st.slider(
                "P(6)", 0.0, 1.0,
                st.session_state.miss_3_2_p6, 0.005,
                key="miss_3_2_p6",
                disabled=st.session_state.miss_3_2_done
            )
            
            total_prob = 5 * p_others + p6

            # Validation
            is_sum_ok = abs(total_prob - 1.0) < 0.01
            is_ratio_ok = abs(p6 - 3 * p_others) < 0.01

            if is_sum_ok and is_ratio_ok:
                st.success(t({"de": "Mission erfüllt! Der Würfel ist bereit.", "en": "Mission Accomplished! The die is ready."}))
                if not st.session_state.miss_3_2_done:
                    st.balloons()
                    st.session_state.miss_3_2_done = True
                    # Track
                    from utils.progress_tracker import track_question_answer, update_local_progress
                    user = st.session_state.get("user")
                    if user:
                        track_question_answer(user["localId"], "vwl", "3", "3.2", "3_2_mission", True)
                        update_local_progress("3", "3.2", "3_2_mission", True)
                        st.rerun()

                if st.button("Reset Mission"):
                    st.session_state.miss_3_2_done = False
                    st.session_state.miss_3_2_p_others = 0.1
                    st.session_state.miss_3_2_p6 = 0.1
                    st.rerun()
            else:
                st.session_state.miss_3_2_done = False
                if not is_sum_ok:
                    if total_prob > 1:
                        st.error(f"Total Probability > 100% ({total_prob:.2f})")
                    else:
                        st.warning(f"Total Probability < 100% ({total_prob:.2f})")
                elif not is_ratio_ok:
                    st.info(f"Sum is correct (100%), but ratio is wrong. P(6) should be 3x others.")

        with c2:
            # Visualization
            x_vals = [1, 2, 3, 4, 5, 6]
            y_vals = [p_others]*5 + [p6]
            colors = ["#007AFF"]*5 + ["#AF52DE"]

            fig = go.Figure()

            # Theoretical
            fig.add_trace(go.Bar(
                x=x_vals, y=y_vals,
                marker_color=colors,
                text=[f"{v:.2f}" for v in y_vals],
                textposition='auto',
                name="Theoretical"
            ))

            # Empirical (if active)
            if "rolls_3_2" in st.session_state and st.session_state.total_rolls_3_2 > 0:
                counts = [st.session_state.rolls_3_2.get(i,0) for i in x_vals]
                freqs = [c / st.session_state.total_rolls_3_2 for c in counts]

                fig.add_trace(go.Scatter(
                    x=x_vals, y=freqs,
                    mode='markers', marker=dict(color='orange', size=10, symbol='diamond'),
                    name=f"Empirical (n={st.session_state.total_rolls_3_2})"
                ))

            fig.update_layout(
                title=dict(text=f"Total Mass: {total_prob:.2f}", x=0.5),
                xaxis=dict(tickmode='linear', dtick=1, title="Outcome (Die Face)"),
                yaxis=dict(range=[0, 1.0], title="Probability"),
                height=300,
                margin=dict(l=20, r=20, t=40, b=20),
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                showlegend=True,
                legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
            )
            st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

            # Simulation Controls (Below Chart)
            st.markdown("---")
            st.caption(t({"de": "Experiment: Würfle den gezinkten Würfel!", "en": "Experiment: Roll the loaded die!"}))

            # Init State if needed
            if "rolls_3_2" not in st.session_state: st.session_state.rolls_3_2 = {i:0 for i in range(1,7)}
            if "total_rolls_3_2" not in st.session_state: st.session_state.total_rolls_3_2 = 0

            sc1, sc2 = st.columns(2)
            with sc1:
                if st.button(t({"de": "100x Würfeln", "en": "Roll 100x"})):
                    # Normalize probs
                    s = sum(y_vals)
                    if s > 0:
                        probs = [y/s for y in y_vals]
                        new_rolls = np.random.choice(x_vals, size=100, p=probs)
                        for r in new_rolls:
                            st.session_state.rolls_3_2[r] += 1
                        st.session_state.total_rolls_3_2 += 100
                        st.rerun()
            with sc2:
                if st.button(t({"de": "Reset Daten", "en": "Reset Data"})):
                    st.session_state.rolls_3_2 = {i:0 for i in range(1,7)}
                    st.session_state.total_rolls_3_2 = 0
                    st.rerun()

    # PRO TIP
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"""
    <div style="background-color: #fef3c7; border-radius: 8px; padding: 12px; color: #92400e;">
        <strong>Pro Tip:</strong> {t(content_3_2['pro_tip'])}
    </div>
    """, unsafe_allow_html=True)
