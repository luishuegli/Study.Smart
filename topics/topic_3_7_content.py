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
content_3_7 = {
    "title": {"de": "3.7 Formparameter (Schiefe & Wölbung)", "en": "3.7 Shape Parameters (Skewness & Kurtosis)"},
    "anchor": {
        "header": {"de": "Die Intuition", "en": "The Intuition"},
        "text": {"de": "Nicht alle Glockenkurven sind symmetrisch. Manche sind 'schief' (wie Einkommensverteilungen: viele Arme, wenige Superreiche -> langer Schwanz nach rechts). Andere sind 'spitz' oder 'flach'. Die Schiefe misst die Asymmetrie, die Wölbung (Kurtosis) misst die 'Dicke der Enden'.", "en": "Not all bell curves are symmetric. Some are 'skewed' (like income distributions: many poor, few super-rich -> long tail to the right). Others are 'pointy' or 'flat'. Skewness measures asymmetry, Kurtosis measures the 'thickness of tails'."},
        "metaphor": {"de": "Die Töpfer-Werkstatt", "en": "The Pottery Studio"}
    },
    "theory": {
        "skew_title": {"de": "Schiefe (Skewness)", "en": "Skewness"},
        "skew_text": {"de": "3. Moment. > 0: Rechts-Schief (Linker Berg). < 0: Links-Schief (Rechter Berg).", "en": "3rd Moment. > 0: Right-Skewed (Left Peak). < 0: Left-Skewed (Right Peak)."},
        "kurt_title": {"de": "Wölbung (Kurtosis)", "en": "Kurtosis"},
        "kurt_text": {"de": "4. Moment. Hohe Kurtosis = Dicke Enden (Fat Tails) = Mehr Ausreißer.", "en": "4th Moment. High Kurtosis = Fat Tails = More Outliers."},
        "formula": r"\gamma_1 = E[(\frac{X-\mu}{\sigma})^3]"
    },
    "interactive": {
        "header": {"de": "Der Form-Wandler", "en": "The Shape Shifter"},
        "desc": {"de": "Verschiebe die Spitze des Dreiecks, um Schiefe zu erzeugen.", "en": "Move the peak of the triangle to create skewness."},
        "mission_title": {"de": "Mission: Der Einkommens-Analyst", "en": "Mission: The Income Analyst"},
        "mission_desc": {"de": "Einkommensverteilungen sind typischerweise **rechts-schief** (positiver Skew). Das heißt, die Masse ist links (viele Leute mit normalem Einkommen), aber es gibt einen langen Schwanz nach rechts (wenige Milliardäre). Stelle die Verteilung so ein, dass sie **rechts-schief** ist.", "en": "Income distributions are typically **right-skewed** (positive skew). This means the mass is on the left (many people with normal income), but there is a long tail to the right (few billionaires). Adjust the distribution to be **right-skewed**."}
    },
    "pro_tip": {
        "de": "Merksatz: 'The Tail tells the Tale'. Wo der Schwanz ist, da ist die Schiefe. Schwanz rechts = Rechts-Schief = Positive Schiefe.",
        "en": "Rule of thumb: 'The Tail tells the Tale'. Where the tail is, there is the skew. Tail right = Right-Skewed = Positive Skew."
    }
}

def render_subtopic_3_7(model):
    """3.7 Shape Parameters"""
    
    # --- CSS ---
    st.markdown("""
    <style>
    [data-testid="stHorizontalBlock"] { align-items: stretch !important; }
    [data-testid="column"] { display: flex !important; flex-direction: column !important; }
    [data-testid="column"] > div { flex: 1 !important; }
    </style>
    """, unsafe_allow_html=True)

    st.header(t(content_3_7["title"]))
    
    # INTUITION
    st.markdown(f"### {t(content_3_7['anchor']['header'])}")
    st.markdown(t(content_3_7["anchor"]["text"]))
    st.markdown("<br>", unsafe_allow_html=True)

    # THEORY
    c1, c2 = st.columns(2, gap="medium")
    with c1:
        with st.container(border=True):
            st.markdown(f"**{t(content_3_7['theory']['skew_title'])}**")
            st.caption(t(content_3_7['theory']['skew_text']))
            st.latex(content_3_7['theory']['formula'])

    with c2:
        with st.container(border=True):
            st.markdown(f"**{t(content_3_7['theory']['kurt_title'])}**")
            st.caption(t(content_3_7['theory']['kurt_text']))
            st.markdown(f"""
            <div style="text-align: center; margin-top: 10px;">
                {render_icon("shapes", size=48, color="#AF52DE")}
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # SIMULATOR
    render_simulator_3_7()

    # EXAM
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"### {t({'de': 'Prüfungstraining', 'en': 'Exam Practice'})}")
    
    # MCQ: hs2024_mc11 (Symmetry)
    q_data = get_question("3.7", "hs2024_mc11")
    if q_data:
        with st.container(border=True):
            st.caption(q_data.get("source", ""))
            opts = q_data.get("options", [])
            if opts and isinstance(opts[0], dict):
                option_labels = [t(o) for o in opts]
            else:
                option_labels = opts

            render_mcq(
                key_suffix="3_7_mc11",
                question_text=t(q_data["question"]),
                options=option_labels,
                correct_idx=q_data["correct_idx"],
                solution_text_dict=q_data["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Falsch.", "en": "Incorrect."},
                client=model,
                ai_context="Distribution Symmetry",
                course_id="vwl",
                topic_id="3",
                subtopic_id="3.7",
                question_id="hs2024_mc11"
            )

def render_simulator_3_7():
    """
    Shape Shifter (Triangle Distribution).
    """
    st.markdown(f"### {t(content_3_7['interactive']['mission_title'])}")
    
    with st.container(border=True):
        st.markdown(t(content_3_7['interactive']['mission_desc']))
        st.markdown("---")

        # State
        if "miss_3_7_peak" not in st.session_state: st.session_state.miss_3_7_peak = 0.5
        if "miss_3_7_done" not in st.session_state: st.session_state.miss_3_7_done = False

        # Logic: Right Skew -> Peak on Left (< 0.5).

        c1, c2 = st.columns([1, 2], gap="large")

        with c1:
            st.markdown(f"**{t({'de': 'Spitze verschieben', 'en': 'Move Peak'})}**")

            peak = st.slider(
                "Peak Position (c)", 0.0, 1.0,
                st.session_state.miss_3_7_peak, 0.05,
                key="miss_3_7_peak",
                disabled=st.session_state.miss_3_7_done
            )

            # Determine skew description
            if peak < 0.4:
                skew_desc = t({"de": "Rechts-Schief (Positiv)", "en": "Right-Skewed (Positive)"})
                color = "#34C759" # Green for match
                is_correct = True
            elif peak > 0.6:
                skew_desc = t({"de": "Links-Schief (Negativ)", "en": "Left-Skewed (Negative)"})
                color = "#FF3B30"
                is_correct = False
            else:
                skew_desc = t({"de": "Symmetrisch", "en": "Symmetric"})
                color = "#007AFF"
                is_correct = False

            st.markdown(f"**Status:** <span style='color:{color}'>{skew_desc}</span>", unsafe_allow_html=True)

            if is_correct:
                if not st.session_state.miss_3_7_done:
                    st.balloons()
                    st.session_state.miss_3_7_done = True
                    from utils.progress_tracker import track_question_answer, update_local_progress
                    user = st.session_state.get("user")
                    if user:
                        track_question_answer(user["localId"], "vwl", "3", "3.7", "3_7_mission", True)
                        update_local_progress("3", "3.7", "3_7_mission", True)
                        st.rerun()
                
                if st.button("Reset 3.7"):
                    st.session_state.miss_3_7_done = False
                    st.session_state.miss_3_7_peak = 0.5
                    st.rerun()

        with c2:
            # Triangle PDF
            x = np.linspace(0, 1, 100)
            y = []
            c = peak
            for val in x:
                if val < c:
                    y.append(2*val/c if c > 0 else 0)
                else:
                    y.append(2*(1-val)/(1-c) if c < 1 else 0)

            fig = go.Figure()

            fig.add_trace(go.Scatter(
                x=x, y=y,
                mode='lines', line=dict(color=color, width=3),
                fill='tozeroy', fillcolor=f"{color}33", # Hex opacity
            ))

            # Annotation
            fig.add_annotation(x=c, y=2.1, text="Peak", showarrow=True, arrowhead=2)

            fig.update_layout(
                title=dict(text="Triangle Distribution", x=0.5),
                xaxis=dict(range=[0, 1], title="x", fixedrange=True),
                yaxis=dict(range=[0, 2.5], visible=False, fixedrange=True),
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
        <strong>Pro Tip:</strong> {t(content_3_7['pro_tip'])}
    </div>
    """, unsafe_allow_html=True)
