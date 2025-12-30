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
            "de": "Stell dir eine Zielscheibe vor. Du versuchst, exakt den Punkt 0.50000... zu treffen. Aber egal wie sehr du reinzoomst, du kannst immer noch weiter reinzoomen. Ein einzelner Punkt ist 'unendlich dünn'. Die Chance, ihn zu treffen, ist daher **Null**.",
            "en": "Imagine a target. You are trying to hit exactly the point 0.50000... But no matter how much you zoom in, you can always zoom in further. A single point is 'infinitely thin'. The chance of hitting it is therefore **zero**."
        }
    },
    "interactive": {
        "title": {"de": "Das Mikroskop", "en": "The Microscope"},
        "instruction": {
            "de": "Erhöhe die Vergrößerung. Versuche, die Nadel auf dem Ziel zu halten.",
            "en": "Increase magnification. Try to keep the needle on the target."
        },
        "feedback_miss": {"de": "Abweichung: {val:.6f}", "en": "Deviation: {val:.6f}"},
        "feedback_hit": {"de": "Perfekt! (Theoretisch unmöglich)", "en": "Perfect! (Theoretically impossible)"}
    },
    "definition": {
        "title": {"de": "Die Dichtefunktion (PDF)", "en": "The Density Function (PDF)"},
        "text": {
            "de": "Bei stetigen Variablen messen wir keine Punkte, sondern **Flächen**. Die Wahrscheinlichkeit ist das Integral unter der Kurve.",
            "en": "For continuous variables, we don't measure points, but **areas**. Probability is the integral under the curve."
        },
        "formula": r"P(a \leq X \leq b) = \int_a^b f(x) dx"
    },
    "pro_tip": {
        "title": {"de": "Profi-Tipp", "en": "Pro Tip"},
        "text": {
            "de": r"Ein einzelner Punkt hat Wahrscheinlichkeit 0 ($P(X=x)=0$). Daher ist es egal, ob wir $\le$ oder $<$ schreiben. $P(X \le 5)$ ist dasselbe wie $P(X < 5)$.",
            "en": r"A single point has probability 0 ($P(X=x)=0$). Therefore, it doesn't matter if we write $\le$ or $<$. $P(X \le 5)$ is the same as $P(X < 5)$."
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
            "de": "Richtig! Ein Punkt hat keine Breite, also keine Fläche.",
            "en": "Correct! A point has no width, so no area."
        }
    }
}

def render_interactive_pdf_zoom():
    """Renders the Microscope visualization."""

    col_ctrl, col_viz = st.columns([1, 1.5])

    # State for Magnification (Log Scale)
    # 0 = 1x, 1 = 10x, 2 = 100x, 3 = 1000x
    if "mag_level" not in st.session_state: st.session_state.mag_level = 0.0

    with col_ctrl:
        st.markdown(f"**{t(content_3_3['interactive']['instruction'])}**")

        mag = st.slider(
            "Magnification (Log Scale)",
            0.0, 4.0,
            value=st.session_state.mag_level,
            step=0.1
        )
        st.session_state.mag_level = mag

        # Calculate range based on magnification
        # range_width shrinks from 1.0 to 0.0001
        width = 1.0 / (10 ** mag)
        center = 0.5
        min_v = center - width/2
        max_v = center + width/2

        # User tries to pick center
        # The slider step needs to be finer than the view width to allow precision
        step_size = width / 100.0

        user_val = st.slider(
            f"Needle Position (Range: {width:.5f})",
            min_v, max_v,
            center + (width * 0.2), # Start off-center
            step=step_size,
            format="%.6f"
        )

        deviation = abs(user_val - center)

        st.markdown(f"""
        <div style="margin-top: 20px; padding: 15px; background: #F3F4F6; border-radius: 8px;">
            <div style="color: #6B7280; font-size: 0.8em; font-weight: bold; text-transform: uppercase; letter-spacing: 1px;">
                {t({'de': 'Abstand zum Ziel', 'en': 'Distance to Target'})}
            </div>
            <div style="font-family: monospace; font-size: 1.5em; font-weight: bold; color: {'#EF4444' if deviation > 0 else '#10B981'};">
                {deviation:.8f}
            </div>
        </div>
        """, unsafe_allow_html=True)

        if deviation == 0:
            st.success(t(content_3_3['interactive']['feedback_hit']))
        elif mag > 3.0:
            st.info(t({"de": "Bei 1000x Zoom siehst du: Du triffst nie exakt.", "en": "At 1000x zoom you see: You never hit exactly."}))

    with col_viz:
        # Visualize the "View"
        x = np.linspace(min_v, max_v, 100)
        y = np.ones_like(x) * 1.0

        fig = go.Figure()

        # 1. Background (The "Matter")
        fig.add_trace(go.Scatter(
            x=x, y=y,
            fill='tozeroy',
            fillcolor='rgba(59, 130, 246, 0.1)',
            line=dict(color='rgba(59, 130, 246, 0.0)'),
            hoverinfo='skip'
        ))

        # 2. The Target Line (Green) - "Infinitely Thin" but drawn with fixed pixel width
        fig.add_trace(go.Scatter(
            x=[center, center],
            y=[0, 1.5],
            mode='lines',
            line=dict(color='#10B981', width=2, dash='dash'),
            name='Target'
        ))

        # 3. The User Needle (Red)
        fig.add_trace(go.Scatter(
            x=[user_val, user_val],
            y=[0, 1.5],
            mode='lines',
            line=dict(color='#EF4444', width=3),
            name='Needle'
        ))

        # Layout
        fig.update_layout(
            yaxis=dict(range=[0, 1.6], visible=False, fixedrange=True),
            xaxis=dict(
                range=[min_v, max_v],
                title=dict(text="x (Zoomed)", font=dict(size=10, color="#9CA3AF")),
                fixedrange=True,
                showgrid=True,
                gridcolor='#E5E7EB',
                zeroline=False
            ),
            margin=dict(l=10, r=10, t=10, b=10),
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
            st.info(t({"de": "Die Nadel hat Breite 0!", "en": "The needle has width 0!"}))

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
