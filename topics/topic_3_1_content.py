import streamlit as st
import plotly.graph_objects as go
import numpy as np
import scipy.stats as stats
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
            "de": "Stell dir vor, du läufst einen Zahlenstrahl entlang und sammelst Wahrscheinlichkeit wie Regenwasser in einem Tank. $F(x)$ zeigt dir den aktuellen Füllstand an. Wenn du ganz links startest ($-\infty$), ist der Tank leer (0). Wenn du ganz rechts ankommst ($+\infty$), ist er voll (1).",
            "en": "Imagine walking along a number line collecting probability like rainwater in a tank. $F(x)$ shows you the current fill level. When you start at the far left ($-\infty$), the tank is empty (0). When you reach the far right ($+\infty$), it is full (1)."
        }
    },
    "interactive": {
        "title": {"de": "Der Wahrscheinlichkeits-Tank", "en": "The Probability Tank"},
        "instruction": {
            "de": "Ziehe den Regler. Beobachte, wie die Fläche volläuft.",
            "en": "Drag the slider. Watch the area fill up."
        }
    },
    "definition": {
        "title": {"de": "Die Definition", "en": "The Definition"},
        "text": {
            "de": "Die Verteilungsfunktion $F(x)$ ist die **Summe aller Wahrscheinlichkeiten** links von $x$ (inklusive $x$).",
            "en": "The distribution function $F(x)$ is the **sum of all probabilities** to the left of $x$ (including $x$)."
        },
        "formula": r"F(x) = P(X \leq x)"
    },
    "pro_tip": {
        "title": {"de": "Profi-Tipp", "en": "Pro Tip"},
        "text": {
            "de": "Intervall-Wahrscheinlichkeit $P(a < X \leq b)$? Einfach 'Groß minus Klein': $F(b) - F(a)$. Denke an deinen Stromzähler: Zählerstand Ende minus Zählerstand Anfang = Verbrauch.",
            "en": "Interval probability $P(a < X \leq b)$? Simply 'Big minus Small': $F(b) - F(a)$. Think of your electric meter: Reading End minus Reading Start = Consumption."
        }
    },
    "mission": {
        "title": {"de": "Mission: Der Qualitäts-Check", "en": "Mission: Quality Check"},
        "task": {
            "de": "Ein Bauteil hält höchstens $x$ Stunden. Gegeben ist $F(100) = 0.8$. Was bedeutet das exakt?",
            "en": "A component lasts at most $x$ hours. Given $F(100) = 0.8$. What does this mean exactly?"
        },
        "options": [
            {"id": "a", "de": "80% der Bauteile halten genau 100 Stunden.", "en": "80% of components last exactly 100 hours."},
            {"id": "b", "de": "80% der Bauteile halten höchstens 100 Stunden.", "en": "80% of components last at most 100 hours."},
            {"id": "c", "de": "20% der Bauteile halten höchstens 100 Stunden.", "en": "20% of components last at most 100 hours."}
        ],
        "correct_id": "b",
        "solution": {
            "de": "Richtig! $F(100)$ ist die kumulierte Wahrscheinlichkeit bis 100.",
            "en": "Correct! $F(100)$ is the cumulative probability up to 100."
        }
    }
}

def render_interactive_cdf():
    """Renders the high-fidelity CDF visualization."""

    # 1. Controls (Left Side)
    col_ctrl, col_viz = st.columns([1, 2.5])

    with col_ctrl:
        st.markdown(f"**{t(content_3_1['interactive']['instruction'])}**")

        # Custom CSS for the slider to make it look "integrated"
        st.markdown("""
        <style>
        div[data-baseweb="slider"] > div > div > div[role="slider"] {
            background-color: #EF4444 !important; /* Red thumb */
            border-color: #EF4444 !important;
        }
        </style>
        """, unsafe_allow_html=True)

        x_val = st.slider(
            "x",
            min_value=-3.0,
            max_value=3.0,
            value=0.0,
            step=0.1,
            label_visibility="collapsed"
        )

        # Calculate Normal CDF
        p_val = stats.norm.cdf(x_val)

        # "Big Number" Display
        st.markdown(f"""
        <div style="text-align: center; margin-top: 20px; padding: 15px; background: #F9FAFB; border-radius: 12px; border: 1px solid #E5E7EB;">
            <div style="color: #6B7280; font-size: 0.9em; font-weight: 500; margin-bottom: 5px;">F(x) = P(X ≤ {x_val})</div>
            <div style="color: #111827; font-size: 2.5em; font-weight: 700; line-height: 1.0;">{p_val:.2f}</div>
            <div style="color: #EF4444; font-size: 0.8em; font-weight: 600; margin-top: 5px;">{int(p_val*100)}% {t({'de': 'Gefüllt', 'en': 'Filled'})}</div>
        </div>
        """, unsafe_allow_html=True)

    with col_viz:
        # Generate data for PDF (Normal Distribution)
        x = np.linspace(-3.5, 3.5, 300)
        y = stats.norm.pdf(x)

        # Mask for filled area
        mask = x <= x_val
        x_fill = x[mask]
        y_fill = y[mask]

        # Add zero points to close the polygon for filling
        # We need to ensure the polygon closes nicely at the bottom
        x_fill_poly = np.concatenate(([-3.5], x_fill, [x_val]))
        y_fill_poly = np.concatenate(([0], y_fill, [0]))

        fig = go.Figure()

        # 1. The Full Curve (Background Ghost)
        fig.add_trace(go.Scatter(
            x=x, y=y,
            mode='lines',
            line=dict(color='#E5E7EB', width=2), # Gray-200
            hoverinfo='skip'
        ))

        # 2. The Filled Area (Accumulated Probability - Liquid Red)
        fig.add_trace(go.Scatter(
            x=x_fill_poly,
            y=y_fill_poly,
            fill='toself',
            fillcolor='rgba(239, 68, 68, 0.6)', # Red-500 with opacity
            line=dict(color='rgba(239, 68, 68, 1)', width=0),
            name=f'P(X ≤ {x_val})',
            hoverinfo='skip'
        ))

        # 3. The Vertical Line at x (Needle)
        fig.add_trace(go.Scatter(
            x=[x_val, x_val],
            y=[0, stats.norm.pdf(x_val)],
            mode='lines',
            line=dict(color='#DC2626', width=3), # Red-600
            name='x'
        ))

        # Layout Polish
        fig.update_layout(
            margin=dict(l=0, r=0, t=10, b=20),
            height=280,
            xaxis=dict(
                range=[-3.5, 3.5],
                fixedrange=True,
                title="x",
                showgrid=False,
                zeroline=False,
                tickfont=dict(color='#9CA3AF')
            ),
            yaxis=dict(
                range=[0, 0.45],
                fixedrange=True,
                visible=False
            ),
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
    
    # CSS Injection for Equal Height
    st.markdown("""
    <style>
    [data-testid="stHorizontalBlock"] { align-items: stretch !important; }
    [data-testid="column"] { display: flex !important; flex-direction: column !important; }
    [data-testid="column"] > div { flex: 1 !important; }
    </style>
    """, unsafe_allow_html=True)

    col_intuition, col_interactive = st.columns([1, 1.8], gap="medium")

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
        render_mcq(
            key_suffix="3_1_mission",
            question_text=t(content_3_1["mission"]["task"]),
            options=[t(o) for o in content_3_1["mission"]["options"]],
            correct_idx=1,
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
            option_labels = [t(o) for o in opts] if opts and isinstance(opts[0], dict) else opts
            
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
