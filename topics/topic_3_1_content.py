import streamlit as st
import plotly.graph_objects as go
import numpy as np
from utils.localization import t
from utils.quiz_helper import render_mcq
from data.exam_questions import get_question

# --- CONTENT DICTIONARY ---
content_3_1 = {
    "title": {
        "de": "3.1 Die Verteilungsfunktion",
        "en": "3.1 The Distribution Function"
    },
    "intuition": {
        "title": {"de": "Die Intuition", "en": "The Intuition"},
        "text": {
            "de": "Stell dir vor, du läufst einen Zahlenstrahl entlang. Dein 'Rucksack' füllt sich mit Wahrscheinlichkeit. Die Verteilungsfunktion $F(x)$ zeigt dir jederzeit an: Wie viel Prozent der gesamten Wahrscheinlichkeit liegen **hinter dir** (oder genau hier)?",
            "en": "Imagine walking along a number line. Your 'backpack' fills up with probability. The distribution function $F(x)$ tells you at any moment: What percentage of the total probability is **behind you** (or exactly here)?"
        }
    },
    "interactive": {
        "title": {"de": "Der Wahrscheinlichkeits-Tank", "en": "The Probability Tank"},
        "instruction": {
            "de": "Ziehe den roten Punkt nach rechts. Beobachte, wie sich der 'Tank' füllt.",
            "en": "Drag the red dot to the right. Watch how the 'tank' fills up."
        }
    },
    "definition": {
        "title": {"de": "Die Definition", "en": "The Definition"},
        "text": {
            "de": "Die Verteilungsfunktion $F(x)$ ist einfach die **kumulierte** Wahrscheinlichkeit bis zum Punkt $x$.",
            "en": "The distribution function $F(x)$ is simply the **cumulative** probability up to point $x$."
        },
        "formula": r"F(x) = P(X \leq x)"
    },
    "pro_tip": {
        "title": {"de": "Profi-Tipp", "en": "Pro Tip"},
        "text": {
            "de": "Willst du die Wahrscheinlichkeit für ein Intervall $P(a < X \leq b)$? Subtrahiere einfach: $F(b) - F(a)$. Das ist wie der Kontostand-Check: Kontostand Ende - Kontostand Anfang = Gewinn.",
            "en": "Want the probability for an interval $P(a < X \leq b)$? Just subtract: $F(b) - F(a)$. It's like checking your bank balance: Balance End - Balance Start = Profit."
        }
    },
    "mission": {
        "title": {"de": "Mission: Der Qualitäts-Check", "en": "Mission: Quality Check"},
        "task": {
            "de": "Ein Bauteil hält höchstens $x$ Stunden. Gegeben ist $F(100) = 0.8$. Was bedeutet das?",
            "en": "A component lasts at most $x$ hours. Given $F(100) = 0.8$. What does this mean?"
        },
        "options": [
            {"id": "a", "de": "80% der Bauteile halten genau 100 Stunden.", "en": "80% of components last exactly 100 hours."},
            {"id": "b", "de": "80% der Bauteile halten höchstens 100 Stunden.", "en": "80% of components last at most 100 hours."},
            {"id": "c", "de": "20% der Bauteile halten höchstens 100 Stunden.", "en": "20% of components last at most 100 hours."}
        ],
        "correct_id": "b",
        "solution": {
            "de": "Richtig! $F(100)$ summiert alle Wahrscheinlichkeiten von 0 bis 100.",
            "en": "Correct! $F(100)$ sums up all probabilities from 0 to 100."
        }
    }
}

def render_interactive_cdf():
    """Renders the interactive CDF visualization."""

    # 1. Controls
    col_ctrl, col_viz = st.columns([1, 2])

    with col_ctrl:
        st.markdown(f"**{t(content_3_1['interactive']['instruction'])}**")
        x_val = st.slider(
            "x",
            min_value=-4.0,
            max_value=4.0,
            value=0.0,
            step=0.1,
            label_visibility="collapsed"
        )

        # Calculate Normal CDF for demo
        import scipy.stats as stats
        p_val = stats.norm.cdf(x_val)

        # Live Indicator (The "Thermometer")
        st.markdown(f"<h3 style='text-align: center; color: #4B5563;'>F(x) = {p_val:.2f}</h3>", unsafe_allow_html=True)
        st.progress(p_val)
        st.caption(t({"de": "Gefüllte Wahrscheinlichkeit", "en": "Accumulated Probability"}))

    with col_viz:
        # Generate data for PDF (Normal Distribution)
        x = np.linspace(-4, 4, 200)
        y = stats.norm.pdf(x)

        # Mask for filled area
        mask = x <= x_val
        x_fill = x[mask]
        y_fill = y[mask]

        # Add zero points to close the polygon for filling
        x_fill_poly = np.concatenate(([-4], x_fill, [x_val]))
        y_fill_poly = np.concatenate(([0], y_fill, [0]))

        fig = go.Figure()

        # 1. The Full Curve (Outline)
        fig.add_trace(go.Scatter(
            x=x, y=y,
            mode='lines',
            line=dict(color='lightgray', width=2),
            hoverinfo='skip'
        ))

        # 2. The Filled Area (Accumulated Probability)
        fig.add_trace(go.Scatter(
            x=x_fill_poly,
            y=y_fill_poly,
            fill='toself',
            fillcolor='rgba(239, 68, 68, 0.3)', # Red with opacity
            line=dict(color='rgba(239, 68, 68, 1)', width=0),
            name=f'P(X ≤ {x_val})',
            hoverinfo='skip'
        ))

        # 3. The Vertical Line at x
        fig.add_trace(go.Scatter(
            x=[x_val, x_val],
            y=[0, stats.norm.pdf(x_val)],
            mode='lines',
            line=dict(color='#DC2626', width=3, dash='solid'), # Red-600
            name='x'
        ))

        # Layout
        fig.update_layout(
            margin=dict(l=20, r=20, t=20, b=20),
            height=300,
            xaxis=dict(range=[-4.2, 4.2], fixedrange=True, title="x"),
            yaxis=dict(range=[0, 0.45], fixedrange=True, visible=False),
            showlegend=False,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
        )

        st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

def render_subtopic_3_1(model):
    """3.1 Die Verteilungsfunktion - Distribution Function"""
    
    # --- HEADER ---
    st.header(t(content_3_1["title"]))
    st.markdown("---")
    
    # --- INTUITION SECTION ---
    st.markdown(f"### {t(content_3_1['intuition']['title'])}")

    # Split Row Protocol: Text | Interactive
    # We want "Equal Height" for these two boxes
    
    # CSS Injection for Equal Height
    st.markdown("""
    <style>
    [data-testid="stHorizontalBlock"] { align-items: stretch !important; }
    [data-testid="column"] { display: flex !important; flex-direction: column !important; }
    [data-testid="column"] > div { flex: 1 !important; }
    </style>
    """, unsafe_allow_html=True)

    col_intuition, col_interactive = st.columns([1, 1.6], gap="medium")

    with col_intuition:
        with st.container(border=True):
            st.markdown(t(content_3_1["intuition"]["text"]))
            st.markdown("<br>", unsafe_allow_html=True)
            st.info(t({"de": "Denk an ein Thermometer!", "en": "Think of a thermometer!"}))

    with col_interactive:
        with st.container(border=True):
            render_interactive_cdf()

    st.markdown("<br><br>", unsafe_allow_html=True)

    # --- DEFINITION & PRO TIP ---
    col_def, col_pro = st.columns([1, 1], gap="medium")

    with col_def:
        with st.container(border=True):
            st.markdown(f"**{t(content_3_1['definition']['title'])}**")
            st.markdown(t(content_3_1["definition"]["text"]))
            st.latex(content_3_1["definition"]["formula"])

    with col_pro:
        with st.container(border=True):
            st.markdown(f"**{t(content_3_1['pro_tip']['title'])}**")
            st.warning(t(content_3_1["pro_tip"]["text"]))

    st.markdown("<br><br>", unsafe_allow_html=True)

    # --- MISSION SECTION ---
    st.markdown(f"### {t(content_3_1['mission']['title'])}")

    with st.container(border=True):
        # We implement this as a simple MCQ but inline
        render_mcq(
            key_suffix="3_1_mission",
            question_text=t(content_3_1["mission"]["task"]),
            options=[t(o) for o in content_3_1["mission"]["options"]],
            correct_idx=1, # Option B is correct (0-based index)
            solution_text_dict=content_3_1["mission"]["solution"],
            success_msg_dict={"de": "Exzellent!", "en": "Excellent!"},
            error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
            client=model,
            ai_context="CDF interpretation mission",
            course_id="vwl",
            topic_id="3",
            subtopic_id="3.1",
            question_id="3_1_mission"
        )

    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- EXAM SECTION ---
    st.markdown(f"### {t({'de': 'Prüfungstraining', 'en': 'Exam Practice'})}")
    
    q_data = get_question("3.1", "uebung2_mc6")
    if q_data:
        with st.container(border=True):
            st.caption(q_data.get("source", ""))
            
            opts = q_data.get("options", [])
            if opts and isinstance(opts[0], dict):
                option_labels = [t(o) for o in opts]
            else:
                option_labels = opts
            
            render_mcq(
                key_suffix="3_1_mc6",
                question_text=t(q_data["question"]),
                options=option_labels,
                correct_idx=q_data["correct_idx"],
                solution_text_dict=q_data["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
                client=model,
                ai_context="CDF exam question",
                course_id="vwl",
                topic_id="3",
                subtopic_id="3.1",
                question_id="3_1_mc6"
            )
