import streamlit as st
import plotly.graph_objects as go
import numpy as np
from utils.localization import t
from utils.quiz_helper import render_mcq
from data.exam_questions import get_question

# --- CONTENT DICTIONARY ---
content_3_2 = {
    "title": {
        "de": "3.2 Diskrete Zufallsvariablen",
        "en": "3.2 Discrete Random Variables"
    },
    "intuition": {
        "title": {"de": "Die Intuition", "en": "The Intuition"},
        "text": {
            "de": "Stell dir eine digitale Währung vor. Du hast genau 1 Bitcoin (100% Wahrscheinlichkeit). Du musst diesen einen Coin auf verschiedene Wallets (Werte 1, 2, 3) verteilen. Wenn du mehr in Wallet 1 steckst, MUSS in den anderen weniger sein. Das ist das 'Nullsummenspiel' der Wahrscheinlichkeit.",
            "en": "Imagine a digital currency. You have exactly 1 Bitcoin (100% probability). You must distribute this single coin across different wallets (Values 1, 2, 3). If you put more into Wallet 1, there MUST be less in the others. This is the 'zero-sum game' of probability."
        }
    },
    "interactive": {
        "title": {"de": "Der Wahrscheinlichkeits-Balancer", "en": "The Probability Balancer"},
        "instruction": {
            "de": "Verändere P(X=1) oder P(X=2). Beobachte, wie sich der Rest automatisch anpasst (Elastizität).",
            "en": "Change P(X=1) or P(X=2). Watch how the rest automatically adjusts (Elasticity)."
        },
        "metric": {"de": "Summe", "en": "Sum"}
    },
    "definition": {
        "title": {"de": "Die Wahrscheinlichkeitsfunktion (PMF)", "en": "The Probability Mass Function (PMF)"},
        "text": {
            "de": "Für diskrete Variablen ordnet die PMF (Wahrscheinlichkeitsfunktion) jedem möglichen Wert $x$ eine Wahrscheinlichkeit $P(X=x)$ zu. Die Summe aller Balken ist immer **exakt 1**.",
            "en": "For discrete variables, the PMF assigns a probability $P(X=x)$ to each possible value $x$. The sum of all bars is always **exactly 1**."
        },
        "formula": r"\sum_{i} P(X=x_i) = 1"
    },
    "pro_tip": {
        "title": {"de": "Profi-Tipp", "en": "Pro Tip"},
        "text": {
            "de": "Fehlt in der Prüfung ein Wert $k$? Nutze den 'Kuchen-Trick': Der ganze Kuchen ist 1. $k = 1 - (\text{Rest})$.",
            "en": "Missing a value $k$ in the exam? Use the 'Cake Trick': The whole cake is 1. $k = 1 - (\text{Rest})$."
        }
    },
    "mission": {
        "title": {"de": "Mission: Der fehlende Baustein", "en": "Mission: The Missing Block"},
        "task": {
            "de": "Eine Variable $X$ kann die Werte 1, 2 oder 3 annehmen. Gegeben ist: $P(X=1) = 0.2$ und $P(X=2) = 0.5$. Berechne $P(X=3)$.",
            "en": "A variable $X$ can take values 1, 2, or 3. Given: $P(X=1) = 0.2$ and $P(X=2) = 0.5$. Calculate $P(X=3)$."
        },
        "options": [
            {"id": "a", "de": "0.7", "en": "0.7"},
            {"id": "b", "de": "0.3", "en": "0.3"},
            {"id": "c", "de": "0.2", "en": "0.2"}
        ],
        "correct_id": "b",
        "solution": {
            "de": "Richtig! $1.0 - (0.2 + 0.5) = 0.3$.",
            "en": "Correct! $1.0 - (0.2 + 0.5) = 0.3$."
        }
    }
}

def normalize_others(changed_idx, new_val, current_probs):
    """
    Adjusts other probabilities proportionally to maintain sum = 1.
    changed_idx: 0, 1, or 2
    new_val: float (0 to 1)
    current_probs: list of 3 floats
    Returns: new list of 3 floats
    """
    probs = list(current_probs)
    old_val = probs[changed_idx]
    probs[changed_idx] = new_val

    # If the new value takes up everything (or more), zero others
    if new_val >= 1.0:
        return [new_val if i == changed_idx else 0.0 for i in range(3)]

    # Calculate remaining pot
    remaining = 1.0 - new_val

    # Calculate sum of others
    sum_others = sum([p for i, p in enumerate(current_probs) if i != changed_idx])

    if sum_others == 0:
        # If others were 0, distribute remaining equally
        # Or, just give it to the "next" available slot?
        # Equal distribution is fairest for "creation"
        count_others = 2
        split = remaining / count_others
        for i in range(3):
            if i != changed_idx:
                probs[i] = split
    else:
        # Scale proportionally
        ratio = remaining / sum_others
        for i in range(3):
            if i != changed_idx:
                probs[i] = current_probs[i] * ratio

    return probs

def render_interactive_pmf():
    """Renders the Elastic PMF builder."""

    # Initialize state
    if "pmf_probs" not in st.session_state:
        st.session_state.pmf_probs = [0.2, 0.5, 0.3]

    # Callback handlers
    def update_p1():
        new_v = st.session_state.s1_val
        st.session_state.pmf_probs = normalize_others(0, new_v, st.session_state.pmf_probs)

    def update_p2():
        new_v = st.session_state.s2_val
        st.session_state.pmf_probs = normalize_others(1, new_v, st.session_state.pmf_probs)

    def update_p3():
        new_v = st.session_state.s3_val
        st.session_state.pmf_probs = normalize_others(2, new_v, st.session_state.pmf_probs)

    col_ctrl, col_viz = st.columns([1, 1.5])

    probs = st.session_state.pmf_probs

    with col_ctrl:
        st.markdown(f"**{t(content_3_2['interactive']['instruction'])}**")

        # We use a custom style for sliders to match bar colors
        # Red
        st.markdown("""
        <style>
        div[data-testid="stVerticalBlock"] > div > div > div > div[data-baseweb="slider"] > div > div > div[role="slider"] {
            border-width: 2px !important;
        }
        </style>
        """, unsafe_allow_html=True)

        # P1 Slider (Red)
        st.slider(
            f"P(X=1) - {probs[0]:.2f}",
            0.0, 1.0, probs[0],
            step=0.01,
            key="s1_val",
            on_change=update_p1
        )

        # P2 Slider (Green)
        st.slider(
            f"P(X=2) - {probs[1]:.2f}",
            0.0, 1.0, probs[1],
            step=0.01,
            key="s2_val",
            on_change=update_p2
        )

        # P3 Slider (Blue)
        st.slider(
            f"P(X=3) - {probs[2]:.2f}",
            0.0, 1.0, probs[2],
            step=0.01,
            key="s3_val",
            on_change=update_p3
        )

        st.markdown(f"""
        <div style="margin-top: 10px; font-size: 0.9em; color: #6B7280; text-align: right;">
            {t(content_3_2['interactive']['metric'])}: <b>{sum(probs):.2f}</b>
        </div>
        """, unsafe_allow_html=True)

    with col_viz:
        x = [1, 2, 3]
        y = probs
        colors = ['#EF4444', '#10B981', '#3B82F6'] # Red, Green, Blue

        fig = go.Figure(data=[go.Bar(
            x=x, y=y,
            marker_color=colors,
            text=[f"{v:.2f}" for v in y],
            textposition='auto',
            width=0.6
        )])

        fig.update_layout(
            yaxis=dict(range=[0, 1.05], visible=False, fixedrange=True),
            xaxis=dict(
                tickmode='array',
                tickvals=[1, 2, 3],
                ticktext=["X=1", "X=2", "X=3"],
                fixedrange=True,
                showgrid=False
            ),
            margin=dict(l=10, r=10, t=10, b=10),
            height=280,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            barcornerradius=4,
            showlegend=False
        )

        st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

def render_subtopic_3_2(model):
    """3.2 Diskrete Zufallsvariablen"""
    
    # --- HEADER ---
    st.header(t(content_3_2["title"]))
    st.markdown("---")
    
    # --- INTUITION SECTION ---
    st.markdown(f"### {t(content_3_2['intuition']['title'])}")

    # CSS for Equal Height
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
            st.markdown(t(content_3_2["intuition"]["text"]))
            st.markdown("<br>", unsafe_allow_html=True)
            st.info(t({"de": "Denk an digitalen Kuchen!", "en": "Think of digital cake!"}))

    with col_play:
        with st.container(border=True):
            render_interactive_pmf()

    st.markdown("<br><br>", unsafe_allow_html=True)

    # --- DEFINITION & PRO TIP ---
    col_def, col_pro = st.columns([1, 1], gap="medium")

    with col_def:
        with st.container(border=True):
            st.markdown(f"**{t(content_3_2['definition']['title'])}**")
            st.markdown(t(content_3_2["definition"]["text"]))
            st.latex(content_3_2["definition"]["formula"])

    with col_pro:
        with st.container(border=True):
            st.markdown(f"**{t(content_3_2['pro_tip']['title'])}**")
            st.warning(t(content_3_2["pro_tip"]["text"]))

    st.markdown("<br><br>", unsafe_allow_html=True)

    # --- MISSION ---
    st.markdown(f"### {t(content_3_2['mission']['title'])}")
    with st.container(border=True):
        render_mcq(
            key_suffix="3_2_mission",
            question_text=t(content_3_2["mission"]["task"]),
            options=[t(o) for o in content_3_2["mission"]["options"]],
            correct_idx=1,
            solution_text_dict=content_3_2["mission"]["solution"],
            success_msg_dict={"de": "Exzellent!", "en": "Excellent!"},
            error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
            client=model,
            ai_context="Discrete PMF normalization mission",
            course_id="vwl",
            topic_id="3",
            subtopic_id="3.2",
            question_id="3_2_mission"
        )

    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- EXAM SECTION ---
    st.markdown(f"### {t({'de': 'Prüfungstraining', 'en': 'Exam Practice'})}")
    
    # MCQ 1
    q1_data = get_question("3.2", "uebung2_mc5")
    if q1_data:
        with st.container(border=True):
            st.caption(q1_data.get("source", ""))
            opts = q1_data.get("options", [])
            option_labels = [t(o) for o in opts] if opts and isinstance(opts[0], dict) else opts
            
            render_mcq(
                key_suffix="3_2_mc5",
                question_text=t(q1_data["question"]),
                options=option_labels,
                correct_idx=q1_data["correct_idx"],
                solution_text_dict=q1_data["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Leider falsch.", "en": "Incorrect."},
                client=model,
                ai_context="Discrete RV Exam Q1",
                course_id="vwl",
                topic_id="3",
                subtopic_id="3.2",
                question_id="3_2_mc5"
            )

    st.markdown("<br>", unsafe_allow_html=True)

    # MCQ 2
    q2_data = get_question("3.2", "test2_q4")
    if q2_data:
        with st.container(border=True):
            st.caption(q2_data.get("source", ""))
            opts = q2_data.get("options", [])
            option_labels = [t(o) for o in opts] if opts and isinstance(opts[0], dict) else opts
            
            render_mcq(
                key_suffix="3_2_q4",
                question_text=t(q2_data["question"]),
                options=option_labels,
                correct_idx=q2_data["correct_idx"],
                solution_text_dict=q2_data["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Leider falsch.", "en": "Incorrect."},
                client=model,
                ai_context="Discrete RV Exam Q2",
                course_id="vwl",
                topic_id="3",
                subtopic_id="3.2",
                question_id="3_2_q4"
            )
