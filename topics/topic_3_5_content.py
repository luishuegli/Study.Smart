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
        "header": {"de": "Der Risiko-Simulator", "en": "The Risk Simulator"},
        "desc": {"de": "Verändere die Streuung (Standardabweichung). Beobachte, wie die Kurve flacher und breiter wird.", "en": "Change the spread (Standard Deviation). Watch how the curve gets flatter and wider."},
        "mission_title": {"de": "Mission: Das Ziel-Risiko", "en": "Mission: The Target Risk"},
        "mission_desc": {"de": "Wir suchen eine Verteilung mit einer Varianz von genau **4.0**. Stelle die Standardabweichung (Sigma) so ein, dass dies erreicht wird.", "en": "We are looking for a distribution with a variance of exactly **4.0**. Adjust the Standard Deviation (Sigma) to achieve this."}
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
    Variance Simulator.
    """
    st.markdown(f"### {t(content_3_5['interactive']['mission_title'])}")
    
    with st.container(border=True):
        st.markdown(t(content_3_5['interactive']['mission_desc']))
        st.markdown("---")

        # State
        if "miss_3_5_sigma" not in st.session_state: st.session_state.miss_3_5_sigma = 1.0
        if "miss_3_5_done" not in st.session_state: st.session_state.miss_3_5_done = False

        # Logic: Var = sigma^2. Target Var = 4 => Sigma = 2.

        c1, c2 = st.columns([1, 2], gap="large")

        with c1:
            st.markdown(f"**{t({'de': 'Streuung einstellen', 'en': 'Adjust Spread'})}**")

            sigma = st.slider(
                "Standard Deviation (Sigma)", 0.5, 3.0,
                st.session_state.miss_3_5_sigma, 0.1,
                key="miss_3_5_sigma",
                disabled=st.session_state.miss_3_5_done
            )

            var_val = sigma ** 2
            
            if abs(var_val - 4.0) < 0.1:
                st.success(t({"de": "Ziel erreicht! Var = 4.", "en": "Target Reached! Var = 4."}))
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
                    st.session_state.miss_3_5_sigma = 1.0
                    st.rerun()
            else:
                st.session_state.miss_3_5_done = False
                st.metric("Variance (Sigma²)", f"{var_val:.2f}", delta=f"{var_val-4.0:.2f}")

        with c2:
            x = np.linspace(-10, 10, 200)
            # Normal PDF
            y = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * (x / sigma)**2)

            fig = go.Figure()

            fig.add_trace(go.Scatter(
                x=x, y=y,
                mode='lines', line=dict(color='#AF52DE', width=2),
                fill='tozeroy', fillcolor='rgba(175, 82, 222, 0.2)',
            ))
            
            # Show inflection points or width?
            # 1 SD lines
            fig.add_shape(type="line", x0=-sigma, y0=0, x1=-sigma, y1=max(y), line=dict(color="gray", dash="dot"))
            fig.add_shape(type="line", x0=sigma, y0=0, x1=sigma, y1=max(y), line=dict(color="gray", dash="dot"))

            fig.update_layout(
                title=dict(text=f"Normal Distribution (σ={sigma:.1f})", x=0.5),
                xaxis=dict(range=[-8, 8], title="x", fixedrange=True),
                yaxis=dict(range=[0, 0.8], visible=False, fixedrange=True),
                height=250,
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
        <strong>Pro Tip:</strong> {t(content_3_5['pro_tip'])}
    </div>
    """, unsafe_allow_html=True)
