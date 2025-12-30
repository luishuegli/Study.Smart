import streamlit as st
import plotly.graph_objects as go
import numpy as np
import time
from views.styles import render_icon
from utils.localization import t
from utils.quiz_helper import render_mcq
from data.exam_questions import get_question
from utils.progress_tracker import track_question_answer, update_local_progress

# --- CONTENT DICTIONARY ---
content_3_2 = {
    "title": {"de": "3.2 Diskrete Zufallsvariablen", "en": "3.2 Discrete Random Variables"},
    "anchor": {"de": "Wie verteilt man Glück auf einem Teller?", "en": "How to distribute luck on a plate?"},
    "intro": {
        "text": {
            "de": "Stell dir vor, du hast 1kg Knete (die gesamte Wahrscheinlichkeit). Eine diskrete Zufallsvariable bedeutet: Du reißt Stücke ab und legst sie auf bestimmte Zahlen. Du kannst 200g auf die '1' legen und 800g auf die '6'. Aber du kannst nichts *zwischen* die Zahlen schmieren.",
            "en": "Imagine you have 1kg of clay (the total probability). A discrete random variable means: You tear off chunks and place them on specific numbers. You can put 200g on '1' and 800g on '6'. But you cannot smear anything *between* the numbers."
        }
    },
    "playground": {
        "title": {"de": "Der Wahrscheinlichkeits-Equalizer", "en": "The Probability Equalizer"},
        "desc": {
            "de": "Verteile die Wahrscheinlichkeit auf die Ergebnisse 1 bis 5. Die Summe muss immer 100% ergeben.",
            "en": "Distribute probability across outcomes 1 to 5. The sum must always equal 100%."
        },
        "metric_sum": {"de": "Summe (Muss 1.0 sein)", "en": "Sum (Must be 1.0)"}
    },
    "theory": {
        "def_title": {"de": "Wahrscheinlichkeitsfunktion (PMF)", "en": "Probability Mass Function (PMF)"},
        "def_text": {
            "de": "Die PMF $p_X(x)$ gibt an, wie viel 'Masse' (Wahrscheinlichkeit) auf einem genauen Wert liegt.",
            "en": "The PMF $p_X(x)$ tells you how much 'mass' (probability) sits on a specific value."
        },
        "prop_title": {"de": "Gesetze der Schwerkraft", "en": "Laws of Gravity"},
        "prop_text": {
            "de": r"1. Niemals negativ: $p_k \ge 0$" + "\n" + r"2. Alles muss da sein: $\sum p_k = 1$",
            "en": r"1. Never negative: $p_k \ge 0$" + "\n" + r"2. All accounted for: $\sum p_k = 1$"
        }
    },
    "mission": {
        "title": {"de": "Mission: Der Casino-Boss", "en": "Mission: The Casino Boss"},
        "briefing": {
            "de": "Du designst ein Würfelspiel. Der Spieler gewinnt bei einer **6** groß, verliert aber bei **1-5** klein. Dein Ziel: Der Würfel soll so gezinkt sein, dass die **6** genau **40%** der Zeit fällt (um Spieler anzulocken), aber die Summe muss stimmen.",
            "en": "You are designing a dice game. The player wins big on a **6**, but loses small on **1-5**. Your goal: Load the die so **6** comes up exactly **40%** of the time (to lure players), but the probability sum must be valid."
        },
        "sim_btn": {"de": "100 Spiele simulieren", "en": "Simulate 100 Games"},
        "success": {
            "de": "Perfekt kalibriert! Das Casino gewinnt langfristig, aber die Spieler bleiben motiviert.",
            "en": "Perfectly calibrated! The casino wins long-term, but players stay motivated."
        }
    },
    "pro_tip": {
        "text": {
            "de": "Wenn du die Wahrscheinlichkeiten von $n-1$ Ergebnissen kennst, kennst du automatisch das letzte! Subtrahiere einfach die Summe der anderen von 1. Das ist das 'Residuum'.",
            "en": "If you know the probabilities of $n-1$ outcomes, you automatically know the last one! Just subtract the sum of the others from 1. That's the 'residual'."
        }
    }
}

def render_subtopic_3_2(model):
    """3.2 Discrete Random Variables - Interactive Equalizer & Casino Sim"""
    
    # --- CSS INJECTION ---
    st.markdown("""
    <style>
    [data-testid="stHorizontalBlock"] { align-items: stretch !important; }
    
    /* Custom Slider Colors */
    .stSlider:has([aria-label*="P(X=6)"]) div[data-baseweb="slider"] > div:first-child > div:first-child { background-color: #FF4B4B !important; }
    .stSlider:has([aria-label*="P(X=6)"]) div[role="slider"] { border: 2px solid #FF4B4B !important; }
    </style>
    """, unsafe_allow_html=True)

    st.header(t(content_3_2["title"]))
    st.markdown(f"**{t(content_3_2['anchor'])}**")
    st.markdown("---")

    # --- INTUITION ---
    with st.container(border=True):
        st.markdown(f"### {render_icon('lightbulb', '#F59E0B')} {t({'de': 'Die Intuition', 'en': 'The Intuition'})}", unsafe_allow_html=True)
        st.markdown(t(content_3_2["intro"]["text"]))
    
    st.markdown("<br>", unsafe_allow_html=True)

    # --- PLAYGROUND: EQUALIZER ---
    st.markdown(f"### {t(content_3_2['playground']['title'])}")
    with st.container(border=True):
        st.caption(t(content_3_2["playground"]["desc"]))

        c_plot, c_ctrl = st.columns([2, 1], gap="medium")

        # State for sliders
        defaults = [0.2] * 5
        for i in range(1, 6):
            if f"pmf_{i}" not in st.session_state: st.session_state[f"pmf_{i}"] = defaults[i-1]

        with c_ctrl:
            p_vals = []
            for i in range(1, 6):
                p = st.slider(f"P(X={i})", 0.0, 1.0, st.session_state[f"pmf_{i}"], 0.05, key=f"pmf_{i}")
                p_vals.append(p)
            
            total_sum = sum(p_vals)

            delta_color = "normal"
            if abs(total_sum - 1.0) < 0.001:
                delta_color = "normal"
            else:
                delta_color = "inverse"

            st.metric(t(content_3_2["playground"]["metric_sum"]), f"{total_sum:.2f}", delta=f"{1.0-total_sum:.2f}", delta_color=delta_color)

        with c_plot:
            fig = get_pmf_chart([1,2,3,4,5], p_vals)
            st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
            
            if abs(total_sum - 1.0) < 0.001:
                st.success(t({"de": "Gültige Verteilung! Summe = 1.0", "en": "Valid Distribution! Sum = 1.0"}))
            elif total_sum > 1.0:
                st.error(t({"de": "Zu viel Wahrscheinlichkeit! (> 100%)", "en": "Too much probability! (> 100%)"}))
            else:
                st.warning(t({"de": "Da fehlt noch was! (< 100%)", "en": "Something is missing! (< 100%)"}))

    st.markdown("<br>", unsafe_allow_html=True)

    # --- THEORY ---
    c1, c2 = st.columns(2, gap="medium")
    with c1:
        with st.container(border=True):
            st.markdown(f"**{t(content_3_2['theory']['def_title'])}**")
            st.markdown(t(content_3_2["theory"]["def_text"]))
            st.latex(r"p_k = P(X = x_k)")
    with c2:
        with st.container(border=True):
            st.markdown(f"**{t(content_3_2['theory']['prop_title'])}**")
            st.markdown(t(content_3_2["theory"]["prop_text"]))
            st.latex(r"\sum_{k} p_k = 1")

    st.markdown("<br>", unsafe_allow_html=True)

    # --- MISSION: CASINO BOSS ---
    st.markdown(f"### {t(content_3_2['mission']['title'])}")
    with st.container(border=True):
        st.markdown(t(content_3_2["mission"]["briefing"]))

        if "load_6" not in st.session_state: st.session_state.load_6 = 0.0
        if "load_others" not in st.session_state: st.session_state.load_others = 0.2
        if "mission_3_2_done" not in st.session_state: st.session_state.mission_3_2_done = False
        if "sim_results" not in st.session_state: st.session_state.sim_results = []

        c_m_ctrl, c_m_vis = st.columns([1, 1.5], gap="large")

        with c_m_ctrl:
            val_6 = st.slider("P(X=6) [Jackpot]", 0.0, 1.0, st.session_state.load_6, 0.05, key="load_6_slider")
            val_others = st.slider("P(X=1-5) [Each]", 0.0, 0.2, st.session_state.load_others, 0.01, key="load_others_slider")
            
            st.session_state.load_6 = val_6
            st.session_state.load_others = val_others

            total_mission = val_6 + val_others * 5
            st.metric(t({"de": "Summe", "en": "Total Sum"}), f"{total_mission:.2f}")

        with c_m_vis:
            outcomes = [1, 2, 3, 4, 5, 6]
            probs = [val_others]*5 + [val_6]
            colors = ["#AF52DE"]*5 + ["#FF4B4B"]
            
            fig_m = go.Figure(data=[go.Bar(
                x=outcomes, y=probs,
                marker_color=colors,
                text=[f"{p:.2f}" for p in probs],
                textposition='auto'
            )])
            fig_m.update_layout(yaxis=dict(range=[0, 1.1], title="P(X=x)"), margin=dict(t=20, b=20), height=200)
            st.plotly_chart(fig_m, use_container_width=True, config={'displayModeBar': False})

        # Simulation Button
        if st.button(t(content_3_2["mission"]["sim_btn"])):
            if abs(total_mission - 1.0) > 0.01:
                st.error("Sum != 1.0. Cannot simulate.")
            else:
                # Run Simulation
                rng = np.random.default_rng()
                sim_outcomes = rng.choice(outcomes, size=100, p=[p/total_mission for p in probs])
                st.session_state.sim_results = sim_outcomes

        # Show Simulation Results (Histogram)
        if len(st.session_state.sim_results) > 0:
            counts = np.bincount(st.session_state.sim_results, minlength=7)[1:]
            st.caption(t({"de": "Simulations-Ergebnis (100 Spiele)", "en": "Simulation Results (100 Games)"}))
            st.bar_chart(counts, height=150)

        # Win Condition
        is_success = (abs(val_6 - 0.40) < 0.01) and (abs(val_others - 0.12) < 0.01) # 0.6 / 5 = 0.12

        if is_success and abs(total_mission - 1.0) < 0.01:
            if not st.session_state.mission_3_2_done:
                st.balloons()
                st.session_state.mission_3_2_done = True
                user = st.session_state.get("user")
                if user:
                    track_question_answer(user["localId"], "vwl", "3", "3.2", "3_2_mission", True)
                    update_local_progress("3", "3.2", "3_2_mission", True)
                    st.rerun()
            st.success(t(content_3_2["mission"]["success"]))
        elif total_mission == 1.0:
            if val_6 < 0.40:
                st.info(t({"de": "Mehr Action! Erhöhe P(6).", "en": "More action! Increase P(6)."}))
            elif val_6 > 0.40:
                st.info(t({"de": "Zu teuer für das Casino! Verringere P(6).", "en": "Too expensive! Decrease P(6)."}))

    st.markdown("<br>", unsafe_allow_html=True)

    # --- PRO TIP ---
    st.markdown(f"""
    <div style="background-color: #fef3c7; border-radius: 8px; padding: 12px; color: #92400e;">
        <strong>Pro Tip:</strong> {t(content_3_2['pro_tip']['text'])}
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # --- EXAM PRACTICE ---
    st.markdown(f"### {t({'de': 'Prüfungstraining', 'en': 'Exam Practice'})}")
    questions = ["uebung2_mc5", "test2_q4", "hs2015_mc5"]
    for q_id in questions:
        q_data = get_question("3.2", q_id)
        if q_data:
            with st.container(border=True):
                st.caption(q_data.get("source", ""))
                opts = q_data.get("options", [])
                if opts and isinstance(opts[0], dict) and ('de' in opts[0] or 'en' in opts[0]):
                    option_labels = [t(o) for o in opts]
                else:
                    option_labels = opts
                render_mcq(
                    key_suffix=f"3_2_{q_id}",
                    question_text=t(q_data["question"]),
                    options=option_labels,
                    correct_idx=q_data["correct_idx"],
                    solution_text_dict=q_data["solution"],
                    success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                    error_msg_dict={"de": "Falsch.", "en": "Incorrect."},
                    client=model,
                    ai_context=f"Question {q_id}",
                    course_id="vwl", topic_id="3", subtopic_id="3.2", question_id=f"3_2_{q_id}"
                )
            st.markdown("<br>", unsafe_allow_html=True)

def get_pmf_chart(x, y):
    fig = go.Figure([go.Bar(x=x, y=y, marker_color="#5856D6", opacity=0.8)])
    fig.update_layout(
        xaxis=dict(title="x", tickmode='linear'),
        yaxis=dict(title="P(X=x)", range=[0, 1.1]),
        margin=dict(l=20, r=20, t=20, b=20),
        height=300,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )
    return fig
