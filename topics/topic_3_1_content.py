import streamlit as st
import plotly.graph_objects as go
import numpy as np
from math import erf, sqrt
from views.styles import render_icon
from utils.localization import t
from utils.quiz_helper import render_mcq
from data.exam_questions import get_question
from utils.progress_tracker import track_question_answer, update_local_progress

# --- CONTENT DICTIONARY ---
content_3_1 = {
    "title": {"de": "3.1 Die Verteilungsfunktion", "en": "3.1 Distribution Function (CDF)"},
    "anchor": {"de": "Wie viel Wahrscheinlichkeit liegt links von mir?", "en": "How much probability is to my left?"},
    "intro": {
        "text": {
            "de": "Stell dir vor, du läufst auf einem Zahlenstrahl von links nach rechts. Du hast einen 'Schneeschieber' dabei, der alle Wahrscheinlichkeit auf deinem Weg aufsammelt. Die Verteilungsfunktion $F(x)$ ist dein Tacho: Sie zeigt an, **wie viel Prozent** der gesamten Wahrscheinlichkeit du bis zum Punkt $x$ bereits eingesammelt hast.",
            "en": "Imagine walking along a number line from left to right. You are pushing a 'snow shovel' that collects all probability in your path. The Distribution Function $F(x)$ is your gauge: It shows **what percentage** of the total probability you have collected up to point $x$."
        }
    },
    "playground": {
        "title": {"de": "Der Akkumulator", "en": "The Accumulator"},
        "desc": {
            "de": "Ziehe den Schieber nach rechts. Oben siehst du die 'Dichte' (den Schnee), unten die 'Verteilungsfunktion' (den gesammelten Haufen).",
            "en": "Drag the slider to the right. Top shows the 'Density' (the snow), bottom shows the 'Distribution Function' (the collected pile)."
        },
        "slider_label": {"de": "Position x", "en": "Position x"}
    },
    "theory": {
        "def_title": {"de": "Definition", "en": "Definition"},
        "def_text": {
            "de": "Die Verteilungsfunktion $F(x)$ gibt die Wahrscheinlichkeit an, dass die Zufallsvariable $X$ einen Wert kleiner oder gleich $x$ annimmt.",
            "en": "The distribution function $F(x)$ gives the probability that the random variable $X$ takes a value less than or equal to $x$."
        },
        "prop_title": {"de": "Eigenschaften", "en": "Properties"},
        "prop_text": {
            "de": "1. Startet bei 0 (links) und endet bei 1 (rechts).\n2. Geht niemals nach unten (monoton steigend).",
            "en": "1. Starts at 0 (left) and ends at 1 (right).\n2. Never goes down (monotonically increasing)."
        }
    },
    "mission": {
        "title": {"de": "Mission: Der Staudamm-Operator", "en": "Mission: The Dam Operator"},
        "briefing": {
            "de": "Ein Staudamm ist fast voll. Du musst das Wehr öffnen, um Wasser abzulassen. Die Sicherheitsvorschrift sagt: Lasse exakt **80%** der Wassermenge ab.",
            "en": "A dam is nearly full. You must open the gate to release water. Safety regulations state: Release exactly **80%** of the water volume."
        },
        "task": {
            "de": "Finde den Wasserstand $x$, bei dem $F(x) = 0.80$ ist.",
            "en": "Find the water level $x$ where $F(x) = 0.80$."
        },
        "success": {
            "de": "Perfekt! Der Druck ist stabilisiert.",
            "en": "Perfect! Pressure stabilized."
        }
    },
    "pro_tip": {
        "text": {
            "de": r"Um die Wahrscheinlichkeit für ein Intervall zu finden, musst du nicht integrieren! Subtrahiere einfach: $P(a < X \le b) = F(b) - F(a)$. Wie beim Bankkonto: Kontostand Ende - Kontostand Anfang = Umsatz.",
            "en": r"To find the probability of an interval, you don't need to integrate! Just subtract: $P(a < X \le b) = F(b) - F(a)$. Like a bank account: Ending Balance - Starting Balance = Transaction Amount."
        }
    }
}

def render_subtopic_3_1(model):
    """3.1 Distribution Function (CDF) - High-Fidelity Implementation"""

    # --- CSS INJECTION (Equal Height & Styling) ---
    st.markdown("""
    <style>
    [data-testid="stHorizontalBlock"] { align-items: stretch !important; }
    [data-testid="column"] { display: flex !important; flex-direction: column !important; }
    [data-testid="column"] > div { flex: 1 !important; }
    
    /* Mission Slider Styling */
    .stSlider:has([aria-label*="Dam"]) div[data-baseweb="slider"] > div:first-child > div:first-child { background-color: #007AFF !important; }
    .stSlider:has([aria-label*="Dam"]) div[role="slider"] { background-color: #FFFFFF !important; border: 2px solid #007AFF !important; }
    </style>
    """, unsafe_allow_html=True)

    # --- HEADER ---
    st.header(t(content_3_1["title"]))
    st.markdown(f"**{t(content_3_1['anchor'])}**")
    st.markdown("---")

    # --- INTUITION SECTION ---
    with st.container(border=True):
        st.markdown(f"### {render_icon('lightbulb', '#F59E0B')} {t({'de': 'Die Intuition', 'en': 'The Intuition'})}", unsafe_allow_html=True)
        st.markdown(t(content_3_1["intro"]["text"]))
    
    st.markdown("<br>", unsafe_allow_html=True)

    # --- INTERACTIVE PLAYGROUND (The Accumulator) ---
    st.markdown(f"### {t(content_3_1['playground']['title'])}")
    with st.container(border=True):
        st.caption(t(content_3_1["playground"]["desc"]))

        # Controls
        col_ctrl, col_vis = st.columns([1, 2], gap="large")

        with col_ctrl:
            x_val = st.slider(t(content_3_1["playground"]["slider_label"]), -3.0, 3.0, 0.0, 0.1)

            # Calculate values (Standard Normal)
            pdf_val = (1 / sqrt(2 * np.pi)) * np.exp(-0.5 * x_val**2)
            cdf_val = 0.5 * (1 + erf(x_val / sqrt(2)))

            st.metric(t({"de": "Position x", "en": "Position x"}), f"{x_val:.1f}")
            st.metric(f"F(x) = P(X ≤ {x_val:.1f})", f"{cdf_val:.1%}")

            accum_text = t({
                "de": f"Wir gehen bis <b>{x_val}</b>.<br>Wir haben <b>{cdf_val:.1%}</b> der gesamten Fläche eingesammelt.",
                "en": f"We move to <b>{x_val}</b>.<br>We have collected <b>{cdf_val:.1%}</b> of the total area."
            })
            st.markdown(f"""
            <div style="margin-top: 20px; font-size: 0.9em; color: #666;">
            {accum_text}
            </div>
            """, unsafe_allow_html=True)

        with col_vis:
            fig = get_cdf_plot(x_val)
            st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

    st.markdown("<br>", unsafe_allow_html=True)

    # --- THEORY CARDS ---
    c1, c2 = st.columns(2, gap="medium")
    
    with c1:
        with st.container(border=True):
            st.markdown(f"**{t(content_3_1['theory']['def_title'])}**")
            st.markdown(t(content_3_1["theory"]["def_text"]))
            st.latex(r"F(x) = P(X \le x) = \int_{-\infty}^{x} f(t) \, dt")

    with c2:
        with st.container(border=True):
            st.markdown(f"**{t(content_3_1['theory']['prop_title'])}**")
            st.markdown(t(content_3_1["theory"]["prop_text"]))
            st.latex(r"\lim_{x \to -\infty} F(x) = 0, \quad \lim_{x \to \infty} F(x) = 1")

    st.markdown("<br>", unsafe_allow_html=True)

    # --- MISSION: THE DAM OPERATOR ---
    st.markdown(f"### {t(content_3_1['mission']['title'])}")

    with st.container(border=True):
        # State Init
        if "dam_x" not in st.session_state: st.session_state.dam_x = -1.0
        if "dam_solved" not in st.session_state: st.session_state.dam_solved = False

        st.markdown(t(content_3_1["mission"]["briefing"]))
        st.markdown(f"**{t(content_3_1['mission']['task'])}**")

        # Interactive Part
        target_prob = 0.80

        dam_x = st.slider(
            t({"de": "Wehröffnung (x)", "en": "Gate Opening (x)"}),
            -2.0, 2.0,
            value=st.session_state.dam_x,
            key="dam_x_slider",
            disabled=st.session_state.dam_solved,
            help="Adjust x to find F(x) = 0.80"
        )

        # Sync state
        st.session_state.dam_x = dam_x

        # Calculate
        current_prob = 0.5 * (1 + erf(dam_x / sqrt(2)))

        # Feedback
        col_m1, col_m2 = st.columns([1, 1])

        with col_m1:
            st.metric(t({"de": "Ziel-Pegel", "en": "Target Level"}), "80.0%")
        with col_m2:
            delta = current_prob - target_prob
            color = "normal"
            if abs(delta) < 0.02: color = "normal" # Metric handles color usually, but we'll use conditional formatting below
            st.metric(t({"de": "Aktueller Pegel", "en": "Current Level"}), f"{current_prob:.1%}", delta=f"{delta*100:.1f}%", delta_color="inverse")

        # Visual Feedback Bar
        st.progress(current_prob)

        # Check Win Condition
        if abs(current_prob - target_prob) < 0.01:
            if not st.session_state.dam_solved:
                st.balloons()
                st.session_state.dam_solved = True

                # Tracking
                user = st.session_state.get("user")
                if user:
                    track_question_answer(user["localId"], "vwl", "3", "3.1", "3_1_mission", True)
                    update_local_progress("3", "3.1", "3_1_mission", True)
                    st.rerun()

            st.success(f"{t(content_3_1['mission']['success'])} (x ≈ {dam_x:.2f})")

            if st.button(t({"de": "Mission neu starten", "en": "Restart Mission"})):
                st.session_state.dam_solved = False
                st.session_state.dam_x = -1.0
                st.rerun()
        else:
            st.session_state.dam_solved = False # Unlock if moved away
            if current_prob < target_prob:
                st.warning(t({"de": "Zu wenig Wasser! Öffne das Wehr weiter (x erhöhen).", "en": "Too little water! Open the gate more (increase x)."}))
            else:
                st.warning(t({"de": "Zu viel Wasser! Schließe das Wehr etwas (x verringern).", "en": "Too much water! Close the gate (decrease x)."}))

    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- PRO TIP ---
    st.markdown(f"""
    <div style="background-color: #fef3c7; border-radius: 8px; padding: 12px; color: #92400e;">
        <strong>Pro Tip:</strong> {t(content_3_1['pro_tip']['text'])}
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # --- EXAM SECTION ---
    st.markdown(f"### {t({'de': 'Prüfungstraining', 'en': 'Exam Practice'})}")
    
    q_data = get_question("3.1", "uebung2_mc6")
    if q_data:
        with st.container(border=True):
            st.caption(q_data.get("source", ""))
            
            # Handle bilingual options
            opts = q_data.get("options", [])
            if opts and isinstance(opts[0], dict) and ('de' in opts[0] or 'en' in opts[0]):
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
                ai_context="Distribution function definition",
                course_id="vwl",
                topic_id="3",
                subtopic_id="3.1",
                question_id="3_1_mc6"
            )

def get_cdf_plot(x_highlight):
    """Generates the split view PDF/CDF plot."""
    x = np.linspace(-3.5, 3.5, 200)
    pdf = (1 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * x**2)
    # Fix: Ensure list comprehension results in a numpy array for vector math
    erf_vals = np.array([erf(val / np.sqrt(2)) for val in x])
    cdf = 0.5 * (1 + erf_vals)

    fig = go.Figure()

    # --- TOP SUBPLOT: PDF ---
    # We can't easily use subplots with different shapes in one go.Figure without make_subplots,
    # but we can use domains. Let's stack them vertically.

    # PDF Curve
    fig.add_trace(go.Scatter(x=x, y=pdf, mode='lines', line=dict(color='black', width=1), name='f(x)', xaxis='x', yaxis='y2'))

    # Shaded Area (Left of x_highlight)
    mask = x <= x_highlight
    fig.add_trace(go.Scatter(
        x=np.concatenate(([x[0]], x[mask], [x_highlight])),
        y=np.concatenate(([0], pdf[mask], [0])),
        fill='toself',
        fillcolor='rgba(0, 122, 255, 0.3)',
        line=dict(width=0),
        name='P(X ≤ x)',
        xaxis='x', yaxis='y2',
        hoverinfo='skip'
    ))

    # --- BOTTOM SUBPLOT: CDF ---
    # CDF Curve
    fig.add_trace(go.Scatter(x=x, y=cdf, mode='lines', line=dict(color='#007AFF', width=3), name='F(x)', xaxis='x', yaxis='y'))

    # Highlight Point
    y_val = 0.5 * (1 + erf(x_highlight / sqrt(2)))
    fig.add_trace(go.Scatter(
        x=[x_highlight], y=[y_val],
        mode='markers',
        marker=dict(color='red', size=10, line=dict(color='white', width=2)),
        name='Current F(x)',
        xaxis='x', yaxis='y'
    ))

    # Dashed line connecting them
    fig.add_shape(type="line", x0=x_highlight, y0=0, x1=x_highlight, y1=1, xref="x", yref="paper", line=dict(color="gray", dash="dash", width=1))

    # Layout
    fig.update_layout(
        grid=dict(rows=2, columns=1, pattern='independent'),
        xaxis=dict(domain=[0, 1], range=[-3.5, 3.5], showgrid=False, title="x"),
        yaxis=dict(domain=[0, 0.45], range=[-0.1, 1.1], showgrid=True, title="F(x)"), # Bottom
        yaxis2=dict(domain=[0.55, 1], range=[0, 0.5], showgrid=False, title="f(x)"), # Top
        showlegend=False,
        height=400,
        margin=dict(l=40, r=20, t=20, b=40),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )

    return fig
