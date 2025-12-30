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
            "de": "Stell dir eine Treppe vor. Du kannst auf der ersten Stufe stehen oder auf der zweiten, aber nicht 'zwischen' den Stufen. Diskrete Variablen sind wie 'Klumpen' von Daten – man kann sie abzählen (1, 2, 3...).",
            "en": "Imagine a staircase. You can stand on the first step or the second, but not 'between' steps. Discrete variables are like 'chunks' of data—you can count them (1, 2, 3...)."
        }
    },
    "interactive": {
        "title": {"de": "Der Wahrscheinlichkeits-Macher", "en": "The Probability Maker"},
        "instruction": {
            "de": "Baue deine eigene Verteilung. Aber Achtung: Die Summe muss immer genau 100% (1.0) ergeben!",
            "en": "Build your own distribution. But beware: The sum must always equal exactly 100% (1.0)!"
        },
        "metric": {"de": "Summe", "en": "Sum"}
    },
    "definition": {
        "title": {"de": "Die Wahrscheinlichkeitsfunktion (PMF)", "en": "The Probability Mass Function (PMF)"},
        "text": {
            "de": "Für diskrete Variablen ordnet die PMF (Wahrscheinlichkeitsfunktion) jedem möglichen Wert $x$ eine Wahrscheinlichkeit $P(X=x)$ zu. Die Summe aller Balken muss 1 sein.",
            "en": "For discrete variables, the PMF assigns a probability $P(X=x)$ to each possible value $x$. The sum of all bars must be 1."
        },
        "formula": r"\sum_{i} P(X=x_i) = 1"
    },
    "pro_tip": {
        "title": {"de": "Profi-Tipp", "en": "Pro Tip"},
        "text": {
            "de": "In Prüfungen fehlt oft ein Wert 'k'. Nutze die Regel: 'Alles zusammen muss 1 ergeben'. Addiere den Rest und ziehe ihn von 1 ab. Das ist dein k.",
            "en": "In exams, a value 'k' is often missing. Use the rule: 'Everything together must be 1'. Sum the rest and subtract from 1. That's your k."
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

def render_interactive_pmf():
    """Renders the interactive PMF builder."""

    # Initialize state for sliders if not set
    if "pmf_p1" not in st.session_state: st.session_state.pmf_p1 = 0.2
    if "pmf_p2" not in st.session_state: st.session_state.pmf_p2 = 0.3

    col_ctrl, col_viz = st.columns([1, 2])

    with col_ctrl:
        st.markdown(f"**{t(content_3_2['interactive']['instruction'])}**")

        # Slider 1
        p1 = st.slider("P(X=1)", 0.0, 1.0, st.session_state.pmf_p1, key="pmf_s1")
        # Slider 2 (constrained max)
        max_p2 = max(0.0, 1.0 - p1)
        # If stored p2 is now too high, clip it visually (and in calculation)
        curr_p2 = min(st.session_state.pmf_p2, max_p2)

        p2 = st.slider("P(X=2)", 0.0, 1.0, curr_p2, key="pmf_s2")

        # Calculate P3 automatically
        p3 = max(0.0, 1.0 - p1 - p2)

        # Display sum check
        total = p1 + p2 + p3

        # If user tries to set p2 > allowed, warn
        if p1 + p2 > 1.0:
             st.warning(t({"de": "Summe > 1! Reduziere P(X=1) oder P(X=2).", "en": "Sum > 1! Reduce P(X=1) or P(X=2)."}))
             # Visual fix for chart
             scale = 1.0 / (p1 + p2)
             p1_c, p2_c, p3_c = p1*scale, p2*scale, 0
        else:
             p1_c, p2_c, p3_c = p1, p2, p3

        st.markdown(f"""
        <div style="background-color: #F3F4F6; padding: 10px; border-radius: 5px; margin-top: 20px;">
            <b>P(X=1):</b> {p1_c:.2f}<br>
            <b>P(X=2):</b> {p2_c:.2f}<br>
            <b>P(X=3):</b> <span style="color: #007AFF; font-weight: bold;">{p3_c:.2f}</span> (Auto)<br>
            <hr style="margin: 5px 0;">
            <b>{t(content_3_2['interactive']['metric'])}:</b> {p1_c+p2_c+p3_c:.2f}
        </div>
        """, unsafe_allow_html=True)

    with col_viz:
        x = [1, 2, 3]
        y = [p1_c, p2_c, p3_c]
        colors = ['#EF4444', '#10B981', '#007AFF'] # Red, Green, Blue

        fig = go.Figure(data=[go.Bar(
            x=x, y=y,
            marker_color=colors,
            text=[f"{v:.2f}" for v in y],
            textposition='auto',
        )])

        fig.update_layout(
            yaxis=dict(range=[0, 1.1], title="P(X=x)", fixedrange=True),
            xaxis=dict(tickmode='linear', tick0=1, dtick=1, title="x", fixedrange=True),
            margin=dict(l=20, r=20, t=20, b=20),
            height=300,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            barcornerradius=5
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
            st.info(t({"de": "Denk an Treppenstufen!", "en": "Think of stairs!"}))

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
