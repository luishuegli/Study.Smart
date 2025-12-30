import streamlit as st
import plotly.graph_objects as go
import numpy as np
from utils.localization import t
from utils.quiz_helper import render_mcq
from data.exam_questions import get_question

# --- CONTENT DICTIONARY ---
content_3_3 = {
    "title": {
        "de": "3.3 Stetige Zufallsvariablen",
        "en": "3.3 Continuous Random Variables"
    },
    "intuition": {
        "title": {"de": "Die Intuition", "en": "The Intuition"},
        "text": {
            "de": "Stell dir eine Dartscheibe vor. Wie wahrscheinlich ist es, dass du EXAKT den Mittelpunkt triffst? Nicht 'ungefähr', sondern auf das Atom genau? Die Wahrscheinlichkeit ist Null. Du brauchst eine Fläche (den Bullseye-Ring), um eine Trefferchance zu haben.",
            "en": "Imagine a dartboard. What is the probability of hitting EXACTLY the center point? Not 'roughly', but to the precise atom? The probability is zero. You need an area (the Bullseye ring) to have a chance of hitting."
        }
    },
    "interactive": {
        "title": {"de": "Das Präzisions-Paradoxon", "en": "The Precision Paradox"},
        "instruction": {
            "de": "Versuche, exakt den Wert 0.5000 zu treffen. Zoome hinein.",
            "en": "Try to hit exactly 0.5000. Zoom in."
        },
        "feedback_miss": {"de": "Knapp daneben! Du hast {val} getroffen.", "en": "Missed! You hit {val}."},
        "feedback_hit": {"de": "Perfekt! (Theoretisch unmöglich, aber gut gemacht)", "en": "Perfect! (Theoretically impossible, but well done)"}
    },
    "definition": {
        "title": {"de": "Die Dichtefunktion (PDF)", "en": "The Density Function (PDF)"},
        "text": {
            "de": "Bei stetigen Variablen ist die Wahrscheinlichkeit für einen einzelnen Punkt immer 0. Wir messen stattdessen die **Fläche** unter der Kurve in einem Intervall.",
            "en": "For continuous variables, the probability of a single point is always 0. Instead, we measure the **area** under the curve within an interval."
        },
        "formula": r"P(a \leq X \leq b) = \int_a^b f(x) dx"
    },
    "pro_tip": {
        "title": {"de": "Profi-Tipp", "en": "Pro Tip"},
        "text": {
            "de": r"Verwechsle nie $f(x)$ mit Wahrscheinlichkeit! $f(x)$ kann größer als 1 sein. Nur die **Fläche** (Integral) muss $\le 1$ sein. $P(X=x) = 0$ gilt immer.",
            "en": r"Never confuse $f(x)$ with probability! $f(x)$ can be greater than 1. Only the **area** (integral) must be $\le 1$. $P(X=x) = 0$ always holds."
        }
    },
    "mission": {
        "title": {"de": "Mission: Der Flächen-Scanner", "en": "Mission: The Area Scanner"},
        "task": {
            "de": "Gegeben ist eine Gleichverteilung (Rechteck) von 0 bis 2. Die Höhe ist $0.5$. Wie groß ist die Wahrscheinlichkeit $P(X=1.5)$?",
            "en": "Given a uniform distribution (rectangle) from 0 to 2. The height is $0.5$. What is the probability $P(X=1.5)$?"
        },
        "options": [
            {"id": "a", "de": "0.5", "en": "0.5"},
            {"id": "b", "de": "0.0", "en": "0.0"},
            {"id": "c", "de": "0.25", "en": "0.25"}
        ],
        "correct_id": "b",
        "solution": {
            "de": "Richtig! Bei stetigen Variablen ist die Wahrscheinlichkeit für einen *einzelnen Punkt* immer 0. Nur Intervalle haben Wahrscheinlichkeit.",
            "en": "Correct! For continuous variables, the probability of a *single point* is always 0. Only intervals have probability."
        }
    }
}

def render_interactive_pdf_zoom():
    """Renders a visualization of 'zooming in' to a point."""

    col_ctrl, col_viz = st.columns([1, 2])

    with col_ctrl:
        st.markdown(f"**{t(content_3_3['interactive']['instruction'])}**")

        # A slider that simulates "infinite precision" difficulty
        # We start with range 0-1.
        zoom_level = st.radio("Zoom Level", ["1x (0-1)", "10x (0.4-0.6)", "100x (0.49-0.51)"], horizontal=False)

        min_v, max_v = 0.0, 1.0
        step = 0.01

        if "10x" in zoom_level:
            min_v, max_v = 0.4, 0.6
            step = 0.001
        elif "100x" in zoom_level:
            min_v, max_v = 0.49, 0.51
            step = 0.0001

        user_val = st.slider("Select 0.5", min_v, max_v, (min_v+max_v)/2, step=step, format="%.4f")

        is_hit = abs(user_val - 0.5) < 0.0000001

        if is_hit:
            st.success(t(content_3_3['interactive']['feedback_hit']))
        else:
            st.caption(f"{t({'de': 'Aktueller Wert', 'en': 'Current Value'})}: {user_val:.4f}")
            if "100x" in zoom_level:
                st.info(t({"de": "Siehst du? Selbst hier ist es schwer, genau 0.5000... zu treffen.", "en": "See? Even here it's hard to hit exactly 0.5000..."}))

    with col_viz:
        # Visualize the PDF (Uniform) and the point
        x = np.linspace(min_v, max_v, 100)
        y = np.ones_like(x) * 1.0 # Uniform density f(x)=1

        fig = go.Figure()

        # The PDF area
        fig.add_trace(go.Scatter(
            x=x, y=y,
            fill='tozeroy',
            fillcolor='rgba(59, 130, 246, 0.2)', # Blue
            line=dict(color='#3B82F6'),
            name='f(x)'
        ))

        # The user's point (Needle)
        fig.add_trace(go.Scatter(
            x=[user_val, user_val],
            y=[0, 1.5],
            mode='lines',
            line=dict(color='#EF4444', width=2), # Red
            name='You'
        ))

        # The Target
        fig.add_trace(go.Scatter(
            x=[0.5, 0.5],
            y=[0, 1.2],
            mode='lines',
            line=dict(color='#10B981', width=2, dash='dot'), # Green
            name='Target (0.5)'
        ))

        fig.update_layout(
            yaxis=dict(range=[0, 1.6], visible=False, fixedrange=True),
            xaxis=dict(range=[min_v, max_v], title="x", fixedrange=True),
            margin=dict(l=20, r=20, t=20, b=20),
            height=300,
            showlegend=False,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)'
        )
        st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

def render_subtopic_3_3(model):
    """3.3 Stetige Zufallsvariablen"""
    
    st.header(t(content_3_3["title"]))
    st.markdown("---")
    
    # --- INTUITION ---
    st.markdown(f"### {t(content_3_3['intuition']['title'])}")

    # CSS Equal Height
    st.markdown("""
    <style>
    [data-testid="stHorizontalBlock"] { align-items: stretch !important; }
    [data-testid="column"] { display: flex !important; flex-direction: column !important; }
    [data-testid="column"] > div { flex: 1 !important; }
    </style>
    """, unsafe_allow_html=True)

    col_int, col_play = st.columns([1, 1.6], gap="medium")

    with col_int:
        with st.container(border=True):
            st.markdown(t(content_3_3["intuition"]["text"]))
            st.markdown("<br>", unsafe_allow_html=True)
            st.info(t({"de": "Ein Punkt hat keine Breite!", "en": "A point has no width!"}))

    with col_play:
        with st.container(border=True):
            render_interactive_pdf_zoom()

    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- DEFINITION & PRO TIP ---
    col_def, col_pro = st.columns([1, 1], gap="medium")

    with col_def:
        with st.container(border=True):
            st.markdown(f"**{t(content_3_3['definition']['title'])}**")
            st.markdown(t(content_3_3["definition"]["text"]))
            st.latex(content_3_3["definition"]["formula"])

    with col_pro:
        with st.container(border=True):
            st.markdown(f"**{t(content_3_3['pro_tip']['title'])}**")
            st.warning(t(content_3_3["pro_tip"]["text"]))

    st.markdown("<br><br>", unsafe_allow_html=True)

    # --- MISSION ---
    st.markdown(f"### {t(content_3_3['mission']['title'])}")
    with st.container(border=True):
        render_mcq(
            key_suffix="3_3_mission",
            question_text=t(content_3_3["mission"]["task"]),
            options=[t(o) for o in content_3_3["mission"]["options"]],
            correct_idx=1,
            solution_text_dict=content_3_3["mission"]["solution"],
            success_msg_dict={"de": "Exzellent!", "en": "Excellent!"},
            error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
            client=model,
            ai_context="Continuous PDF zero probability",
            course_id="vwl",
            topic_id="3",
            subtopic_id="3.3",
            question_id="3_3_mission"
        )

    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- EXAM SECTION ---
    st.markdown(f"### {t({'de': 'Prüfungstraining', 'en': 'Exam Practice'})}")
    
    q_data = get_question("3.3", "test2_q3")
    if q_data:
        with st.container(border=True):
            st.caption(q_data.get("source", ""))
            opts = q_data.get("options", [])
            option_labels = [t(o) for o in opts] if opts and isinstance(opts[0], dict) else opts
            
            render_mcq(
                key_suffix="3_3_q3",
                question_text=t(q_data["question"]),
                options=option_labels,
                correct_idx=q_data["correct_idx"],
                solution_text_dict=q_data["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Leider falsch.", "en": "Incorrect."},
                client=model,
                ai_context="Continuous PDF Exam Q1",
                course_id="vwl",
                topic_id="3",
                subtopic_id="3.3",
                question_id="3_3_q3"
            )
