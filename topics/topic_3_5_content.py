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
content_3_5 = {
    "title": {"de": "3.5 Varianz & Standardabweichung", "en": "3.5 Variance & Standard Deviation"},
    "anchor": {
        "header": {"de": "Die Intuition", "en": "The Intuition"},
        "text": {"de": "Der Erwartungswert sagt dir, wo die Mitte ist. Die Varianz sagt dir, wie 'breit' oder 'flauschig' die Verteilung ist. Eine hohe Varianz bedeutet großes Risiko und große Unsicherheit.", "en": "The expected value tells you where the center is. The variance tells you how 'wide' or 'fluffy' the distribution is. High variance means high risk and high uncertainty."},
        "metaphor": {"de": "Der Streuungs-Messer", "en": "The Spread Gauge"}
    },
    "theory": {
        "def_title": {"de": "Definition Var(X)", "en": "Definition Var(X)"},
        "def_text": {"de": "Erwartete quadrierte Abweichung vom Mittelwert.", "en": "Expected squared deviation from the mean."},
        "shift_title": {"de": "Verschiebungssatz", "en": "Shift Formula"},
        "shift_text": {"de": "Var(X) = E[X²] - (E[X])². Das ist oft einfacher zu rechnen!", "en": "Var(X) = E[X²] - (E[X])². This is often easier to calculate!"},
        "formula": r"Var(X) = E[(X - \mu)^2]"
    },
    "interactive": {
        "header": {"de": "Der Varianz-Visualisierer", "en": "The Variance Visualizer"},
        "desc": {"de": "Verschiebe die Punkte. Die Quadrate zeigen die quadrierte Abweichung vom Mittelwert. Die Varianz ist die durchschnittliche Fläche dieser Quadrate.", "en": "Move the points. The squares show the squared deviation from the mean. The variance is the average area of these squares."},
        "mission_title": {"de": "Mission: Das Ziel-Risiko", "en": "Mission: The Target Risk"},
        "mission_desc": {"de": "Versuche, die Punkte so zu verteilen, dass die Varianz genau **4.0** beträgt.", "en": "Try to arrange the points so that the variance is exactly **4.0**."}
    },
    "pro_tip": {
        "de": "Achtung: Var(aX) = a² Var(X). Die Konstante kommt quadratisch raus! Aber Var(X + b) = Var(X) (Verschieben ändert die Breite nicht).",
        "en": "Watch out: Var(aX) = a² Var(X). The constant comes out squared! But Var(X + b) = Var(X) (Shifting doesn't change the width)."
    }
}

def render_subtopic_3_5(model):
    """3.5 Variance"""
    
    # --- CSS ---
    st.markdown("""
    <style>
    [data-testid="stHorizontalBlock"] { align-items: stretch !important; }
    [data-testid="column"] { display: flex !important; flex-direction: column !important; }
    [data-testid="column"] > div { flex: 1 !important; }
    </style>
    """, unsafe_allow_html=True)

    st.header(t(content_3_5["title"]))
    
    # INTUITION
    st.markdown(f"### {t(content_3_5['anchor']['header'])}")
    st.markdown(t(content_3_5["anchor"]["text"]))
    st.markdown("<br>", unsafe_allow_html=True)

    # THEORY
    c1, c2 = st.columns(2, gap="medium")
    with c1:
        with st.container(border=True):
            st.markdown(f"**{t(content_3_5['theory']['def_title'])}**")
            st.caption(t(content_3_5['theory']['def_text']))
            st.latex(content_3_5['theory']['formula'])

    with c2:
        with st.container(border=True):
            st.markdown(f"**{t(content_3_5['theory']['shift_title'])}**")
            st.caption(t(content_3_5['theory']['shift_text']))
            st.latex(r"Var(X) = E[X^2] - (E[X])^2")
            st.markdown(f"""
            <div style="text-align: center; margin-top: 10px;">
                {render_icon("activity", size=48, color="#AF52DE")}
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # SIMULATOR
    render_simulator_3_5()

    # EXAM
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"### {t({'de': 'Prüfungstraining', 'en': 'Exam Practice'})}")
    
    q_ids = [
        ("3.5", "uebung2_mc8"),
        ("3.5", "uebung2_mc4"),
        ("3.5", "hs2023_mc4"),
        ("3.5", "test3_mc2"), # Transformation Y = X/sigma
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
                    key_suffix=f"3_5_{qid}",
                    question_text=t(q_data["question"]),
                    options=option_labels,
                    correct_idx=q_data["correct_idx"],
                    solution_text_dict=q_data["solution"],
                    success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                    error_msg_dict={"de": "Falsch.", "en": "Incorrect."},
                    client=model,
                    ai_context="Variance",
                    course_id="vwl",
                    topic_id="3",
                    subtopic_id="3.5",
                    question_id=f"3_5_{qid}"
                )
            st.markdown("<br>", unsafe_allow_html=True)

def render_simulator_3_5():
    """
    Variance Simulator: The Squared Squares.
    Visualize deviation from mean as actual squares.
    """
    st.markdown(f"### {t(content_3_5['interactive']['mission_title'])}")
    
    with st.container(border=True):
        st.markdown(t(content_3_5['interactive']['mission_desc']))
        st.markdown("---")

        # State: 3 Points
        if "miss_3_5_pts" not in st.session_state:
            st.session_state.miss_3_5_pts = [-2.0, 0.0, 2.0]
        if "miss_3_5_done" not in st.session_state: st.session_state.miss_3_5_done = False

        # Controls
        cols = st.columns(3)
        pts = st.session_state.miss_3_5_pts

        new_pts = []
        for i, col in enumerate(cols):
            val = col.slider(f"Point {i+1}", -5.0, 5.0, pts[i], 0.5, key=f"p{i}_3_5", disabled=st.session_state.miss_3_5_done)
            new_pts.append(val)
            
        st.session_state.miss_3_5_pts = new_pts
        n = 3
        mean = sum(new_pts) / n
        sq_diffs = [(x - mean)**2 for x in new_pts]
        variance = sum(sq_diffs) / n

        target_var = 4.0

        # Visuals
        fig = go.Figure()

        # 1. The Line
        fig.add_shape(type="line", x0=-6, y0=0, x1=6, y1=0, line=dict(color="black", width=2))

        # 2. The Mean Line
        fig.add_shape(type="line", x0=mean, y0=-2, x1=mean, y1=5, line=dict(color="red", dash="dash"))
        fig.add_annotation(x=mean, y=5.2, text=f"Mean = {mean:.1f}", showarrow=False, font=dict(color="red"))

        # 3. The Squares
        for x, sq_area in zip(new_pts, sq_diffs):
            # Draw a square of area sq_area. Side = |x - mean|
            side = abs(x - mean)
            if side > 0.01:
                fig.add_shape(type="rect",
                    x0=min(x, mean), y0=0, x1=max(x, mean), y1=side,
                    line=dict(color="rgba(175, 82, 222, 0.5)"),
                    fillcolor="rgba(175, 82, 222, 0.2)"
                )

            # The Point
            fig.add_trace(go.Scatter(
                x=[x], y=[0],
                mode='markers', marker=dict(size=12, color='#007AFF'),
                hoverinfo='skip'
            ))

        fig.update_layout(
            title=dict(text=f"Variance = Sum of Areas / {n} = {sum(sq_diffs):.1f} / {n} = {variance:.2f}", x=0.5),
            xaxis=dict(range=[-6, 6], title="Value", fixedrange=True),
            yaxis=dict(range=[-0.5, 6], visible=False, fixedrange=True), # Space for squares
            height=300,
            margin=dict(l=20, r=20, t=40, b=20),
            showlegend=False,
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
        )
        st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

        # Win Condition
        if abs(variance - target_var) < 0.1:
            st.success(t({"de": "Perfekt! Varianz ≈ 4.0", "en": "Perfect! Variance ≈ 4.0"}))
            if not st.session_state.miss_3_5_done:
                st.balloons()
                st.session_state.miss_3_5_done = True
                from utils.progress_tracker import track_question_answer, update_local_progress
                user = st.session_state.get("user")
                if user:
                    track_question_answer(user["localId"], "vwl", "3", "3.5", "3_5_mission", True)
                    update_local_progress("3", "3.5", "3_5_mission", True)
                    st.rerun()
            if st.button("Reset 3.5"):
                st.session_state.miss_3_5_done = False
                st.session_state.miss_3_5_pts = [-2.0, 0.0, 2.0]
                st.rerun()
        else:
            st.session_state.miss_3_5_done = False
            # Hint
            if variance < target_var:
                st.info(t({"de": "Die Quadrate sind zu klein. Zieh die Punkte weiter auseinander!", "en": "Squares are too small. Pull points further apart!"}))
            else:
                st.info(t({"de": "Zu viel Streuung. Bring die Punkte näher zusammen.", "en": "Too much spread. Bring points closer together."}))

    # PRO TIP
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"""
    <div style="background-color: #fef3c7; border-radius: 8px; padding: 12px; color: #92400e;">
        <strong>Pro Tip:</strong> {t(content_3_5['pro_tip'])}
    </div>
    """, unsafe_allow_html=True)
