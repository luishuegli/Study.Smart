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
content_3_2 = {
    "title": {"de": "3.2 Diskrete Zufallsvariablen", "en": "3.2 Discrete Random Variables"},
    "anchor": {
        "header": {"de": "Die Intuition", "en": "The Intuition"},
        "text": {"de": "Stell dir eine digitale Währung vor. Du hast genau 1 Bitcoin (100% Wahrscheinlichkeit). Du musst diesen einen Coin auf verschiedene Wallets (Werte 1, 2, 3...) verteilen. Wenn du mehr in Wallet 1 steckst, MUSS in den anderen weniger sein. Das ist das 'Nullsummenspiel' der Wahrscheinlichkeit.", "en": "Imagine a digital currency. You have exactly 1 Bitcoin (100% probability). You must distribute this single coin across different wallets (Values 1, 2, 3...). If you put more into Wallet 1, there MUST be less in the others. This is the 'zero-sum game' of probability."},
    },
    "theory": {
        "pmf_title": {"de": "Wahrscheinlichkeitsfunktion (PMF)", "en": "Probability Mass Function (PMF)"},
        "pmf_text": {"de": "Ordnet jedem diskreten Wert x eine Wahrscheinlichkeit P(X=x) zu.", "en": "Assigns a probability P(X=x) to each discrete value x."},
        "prop_title": {"de": "Eigenschaften", "en": "Properties"},
        "props": {
            "p1": {"de": "Niemals negativ: $p_k \\geq 0$", "en": "Never negative: $p_k \\geq 0$"},
            "p2": {"de": "Alles muss da sein: $\\sum p_k = 1$", "en": "All accounted for: $\\sum p_k = 1$"}
        },
        "pmf_formula": r"f(x) = P(X=x)",
        "norm_formula": r"\sum_{i} P(X=x_i) = 1"
    },
    "mission1": {
        "title": {"de": "Mission 1: Die Aufwärmübung", "en": "Mission 1: The Warm-Up"},
        "desc": {"de": "Ein Casino beauftragt dich. Konstruiere einen Würfel, bei dem die **6 genau 50%** der Zeit fällt. Die anderen Zahlen (1-5) sollen gleich wahrscheinlich sein.", "en": "A casino hires you. Construct a die where **6 comes up exactly 50%** of the time. The other numbers (1-5) should be equally likely."},
        "target_p6": 0.50,
        "target_others": 0.10
    },
    "mission2": {
        "title": {"de": "Mission 2: Der gezinkte Würfel", "en": "Mission 2: The Loaded Die"},
        "desc": {"de": "Jetzt wird es schwieriger! Die **6** soll genau **40%** der Zeit erscheinen. Die anderen Zahlen teilen sich den Rest gleichmäßig.", "en": "Now it gets harder! **6** should come up exactly **40%** of the time. The other numbers share the rest equally."},
        "target_p6": 0.40,
        "target_others": 0.12
    },
    "pro_tip": {
        "de": "Der 'Kuchen-Trick': Fehlt in der Prüfung ein Wert? Der ganze Kuchen ist 1. Fehlender Wert = 1 - Summe(Rest). Wenn du n-1 Wahrscheinlichkeiten kennst, kennst du automatisch die letzte!",
        "en": "The 'Cake Trick': Missing a value in the exam? The whole cake is 1. Missing value = 1 - Sum(Rest). If you know n-1 probabilities, you automatically know the last one!"
    }
}

def render_subtopic_3_2(model):
    """3.2 Discrete Random Variables - High-Fidelity Dashboard"""
    
    # --- CSS INJECTION ---
    st.markdown("""
    <style>
    [data-testid="stHorizontalBlock"] { align-items: stretch !important; }
    [data-testid="column"] { display: flex !important; flex-direction: column !important; }
    [data-testid="column"] > div { flex: 1 !important; }
    </style>
    """, unsafe_allow_html=True)

    st.header(t(content_3_2["title"]))
    st.markdown(t({"de": "Wie modellieren wir Ereignisse, die man zählen kann?", "en": "How do we model events that can be counted?"}))
    st.markdown("---")
    
    # ROW 1: INTUITION
    with st.container(border=True):
        st.markdown(f"### {t(content_3_2['anchor']['header'])}")
        st.markdown(t(content_3_2["anchor"]["text"]))
    
    st.markdown("<br>", unsafe_allow_html=True)

    # ROW 2: THEORY
    c1, c2 = st.columns(2, gap="medium")
    with c1:
        with st.container(border=True):
            st.markdown(f"**{t(content_3_2['theory']['pmf_title'])}**")
            st.caption(t(content_3_2['theory']['pmf_text']))
            st.latex(content_3_2['theory']['pmf_formula'])
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown(f"**{t({'de': 'Normierung', 'en': 'Normalization'})}:**")
            st.latex(content_3_2['theory']['norm_formula'])

    with c2:
        with st.container(border=True):
            st.markdown(f"**{t(content_3_2['theory']['prop_title'])}**")
            st.markdown(f"""
            <div style="font-size: 14px; color: #333; line-height: 2.0; margin-top: 8px;">
            1. {t(content_3_2['theory']['props']['p1'])}<br>
            2. {t(content_3_2['theory']['props']['p2'])}
            </div>
            """, unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown(f"""
            <div style="text-align: center;">
                {render_icon("bar-chart", size=48, color="#AF52DE")}
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # ROW 3: MISSION TABS
    render_missions_3_2()

    # EXAM SECTION
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown(f"### {t({'de': 'Prüfungstraining', 'en': 'Exam Practice'})}")
    
    questions = ["uebung2_mc5", "test2_q4"]
    
    for q_key in questions:
        q_data = get_question("3.2", q_key)
        if q_data:
            with st.container(border=True):
                st.caption(q_data.get("source", ""))
                opts = q_data.get("options", [])
                if opts and isinstance(opts[0], dict):
                    option_labels = [t(o) for o in opts]
                else:
                    option_labels = opts

                render_mcq(
                    key_suffix=f"3_2_{q_key}",
                    question_text=t(q_data["question"]),
                    options=option_labels,
                    correct_idx=q_data["correct_idx"],
                    solution_text_dict=q_data["solution"],
                    success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                    error_msg_dict={"de": "Falsch.", "en": "Incorrect."},
                    client=model,
                    ai_context="Discrete Random Variables",
                    course_id="vwl",
                    topic_id="3",
                    subtopic_id="3.2",
                    question_id=f"3_2_{q_key}"
                )
            st.markdown("<br>", unsafe_allow_html=True)


def render_missions_3_2():
    """Two-mission structure: Easy (50%) and Advanced (3x)"""
    
    tab1, tab2 = st.tabs([
        t(content_3_2["mission1"]["title"]),
        t(content_3_2["mission2"]["title"])
    ])
    
    with tab1:
        render_die_mission(
            mission_key="m1",
            desc_dict=content_3_2["mission1"]["desc"],
            target_p6=0.50,
            target_others=0.10,
            tolerance=0.02  # Easy tolerance
        )
    
    with tab2:
        render_die_mission(
            mission_key="m2",
            desc_dict=content_3_2["mission2"]["desc"],
            target_p6=0.375,
            target_others=0.125,
            tolerance=0.015  # Tighter for advanced
        )
    
    # PRO TIP (Below missions)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"""
    <div style="background-color: #fef3c7; border-radius: 8px; padding: 12px; color: #92400e;">
        <strong>Pro Tip:</strong> {t(content_3_2['pro_tip'])}
    </div>
    """, unsafe_allow_html=True)


def render_die_mission(mission_key, desc_dict, target_p6, target_others, tolerance):
    """Reusable die-building mission component"""
    
    # Scoped CSS for slider colors
    st.markdown(f"""
    <style>
    /* Blue slider for P(1-5) */
    .stSlider:has([aria-label*="P(1)"]) div[data-baseweb="slider"] > div:first-child > div:first-child {{ background-color: #007AFF !important; }}
    .stSlider:has([aria-label*="P(1)"]) div[role="slider"] {{ background-color: #FFFFFF !important; border: 2px solid #007AFF !important; }}
    
    /* Purple slider for P(6) */
    .stSlider:has([aria-label="P(6)"]) div[data-baseweb="slider"] > div:first-child > div:first-child {{ background-color: #AF52DE !important; }}
    .stSlider:has([aria-label="P(6)"]) div[role="slider"] {{ background-color: #FFFFFF !important; border: 2px solid #AF52DE !important; }}
    </style>
    """, unsafe_allow_html=True)
    
    with st.container(border=True):
        st.markdown(t(desc_dict))
        st.markdown("---")

        # State keys
        p_others_key = f"miss_3_2_{mission_key}_p_others"
        p6_key = f"miss_3_2_{mission_key}_p6"
        done_key = f"miss_3_2_{mission_key}_done"

        # Initialize state
        if p_others_key not in st.session_state: st.session_state[p_others_key] = 0.10
        if p6_key not in st.session_state: st.session_state[p6_key] = 0.20
        if done_key not in st.session_state: st.session_state[done_key] = False

        # Controls
        c1, c2 = st.columns([1, 2], gap="large")

        with c1:
            st.markdown(f"**{t({'de': 'Einstellungen', 'en': 'Settings'})}**")
            
            p_others = st.slider(
                "P(1) = P(2) = ... = P(5)", 0.0, 0.30,
                st.session_state[p_others_key], 0.01,
                key=p_others_key,
                disabled=st.session_state[done_key]
            )
            
            p6 = st.slider(
                "P(6)", 0.0, 1.0,
                st.session_state[p6_key], 0.01,
                key=p6_key,
                disabled=st.session_state[done_key]
            )
            
            total_prob = 5 * p_others + p6

            # Validation
            is_sum_ok = abs(total_prob - 1.0) < 0.02
            is_p6_ok = abs(p6 - target_p6) < tolerance
            is_others_ok = abs(p_others - target_others) < tolerance

            if is_sum_ok and is_p6_ok and is_others_ok:
                st.success(t({"de": "Mission erfüllt!", "en": "Mission Accomplished!"}))
                if not st.session_state[done_key]:
                    st.balloons()
                    st.session_state[done_key] = True
                    # Track progress
                    from utils.progress_tracker import track_question_answer, update_local_progress
                    user = st.session_state.get("user")
                    if user:
                        track_question_answer(user["localId"], "vwl", "3", "3.2", f"3_2_{mission_key}", True)
                        update_local_progress("3", "3.2", f"3_2_{mission_key}", True)
                        st.rerun()

                if st.button(t({"de": "Mission zurücksetzen", "en": "Reset Mission"}), key=f"reset_{mission_key}"):
                    st.session_state[done_key] = False
                    st.session_state[p_others_key] = 0.10
                    st.session_state[p6_key] = 0.20
                    st.rerun()
            else:
                st.session_state[done_key] = False
                if not is_sum_ok:
                    if total_prob > 1:
                        st.error(f"{t({'de': 'Summe > 100%', 'en': 'Total > 100%'})} ({total_prob:.0%})")
                    else:
                        st.warning(f"{t({'de': 'Summe < 100%', 'en': 'Total < 100%'})} ({total_prob:.0%})")
                elif is_sum_ok:
                    st.info(t({"de": f"Summe stimmt! Aber überprüfe die Verhältnisse.", "en": f"Sum is correct! But check the ratios."}))

        with c2:
            # Visualization
            x_vals = [1, 2, 3, 4, 5, 6]
            y_vals = [p_others]*5 + [p6]
            colors = ["#007AFF"]*5 + ["#AF52DE"]

            fig = go.Figure()

            fig.add_trace(go.Bar(
                x=x_vals, y=y_vals,
                marker_color=colors,
                text=[f"{v:.0%}" for v in y_vals],
                textposition='auto',
                name="Theoretical"
            ))

            fig.update_layout(
                title=dict(text=f"Total Mass: {total_prob:.0%}", x=0.5),
                xaxis=dict(tickmode='linear', dtick=1, title="Outcome (Die Face)"),
                yaxis=dict(range=[0, 0.6], title="Probability"),
                height=300,
                margin=dict(l=20, r=20, t=40, b=20),
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                showlegend=False
            )
            st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False}, key=f"chart_{mission_key}")
