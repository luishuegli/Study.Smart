import streamlit as st
import numpy as np
import math
import plotly.graph_objects as go
from views.styles import render_icon
from utils.localization import t
from utils.quiz_helper import render_mcq
from data.exam_questions import get_question

# ==========================================
# 1. CONTENT DICTIONARY (Bilingual)
# ==========================================
content_3_1 = {
    "title": {"de": "3.1 Die Verteilungsfunktion (CDF)", "en": "3.1 Distribution Function (CDF)"},
    "anchor": {
        "header": {"de": "Die Intuition", "en": "The Intuition"},
        "text": {"de": "Stell dir vor, du läufst einen Zahlenstrahl entlang und sammelst Wahrscheinlichkeit wie Regenwasser in einem Tank. Die Funktion F(x) zeigt dir den aktuellen Füllstand an. Ganz links (-∞) ist der Tank leer (0). Ganz rechts (+∞) ist er voll (1). Du kannst niemals Wasser verlieren – der Tank wird nur voller!", "en": "Imagine walking along a number line collecting probability like rainwater in a tank. The function F(x) shows you the current fill level. At the far left (-∞), the tank is empty (0). At the far right (+∞), it is full (1). You can never lose water – the tank only gets fuller!"},
        "metaphor": {"de": "Der Wahrscheinlichkeits-Scanner", "en": "The Probability Scanner"}
    },
    "theory": {
        "def_title": {"de": "Definition", "en": "Definition"},
        "def_text": {"de": "Die Verteilungsfunktion F(x) gibt die Wahrscheinlichkeit an, dass die Zufallsvariable X einen Wert kleiner oder gleich x annimmt.", "en": "The distribution function F(x) gives the probability that the random variable X takes a value less than or equal to x."},
        "formula": r"F(x) = P(X \leq x) = \int_{-\infty}^{x} f(t) \, dt",
        "prop_title": {"de": "Eigenschaften", "en": "Properties"},
        "props": {
            "p1": {"de": "Startet bei 0 (links) und endet bei 1 (rechts).", "en": "Starts at 0 (left) and ends at 1 (right)."},
            "p2": {"de": "Geht niemals nach unten (monoton steigend).", "en": "Never goes down (monotonically increasing)."}
        },
        "limits_formula": r"\lim_{x \to -\infty} F(x) = 0, \quad \lim_{x \to +\infty} F(x) = 1"
    },
    "interactive": {
        "header": {"de": "Der Wahrscheinlichkeits-Scanner", "en": "The Probability Scanner"},
        "desc": {"de": "Bewege den Scanner nach rechts. Beobachte, wie sich die Wahrscheinlichkeit (blaue Fläche) ansammelt.", "en": "Move the scanner to the right. Watch how the probability (blue area) accumulates."},
        "mission_title": {"de": "Mission: Qualitäts-Check", "en": "Mission: Quality Check"},
        "mission_desc": {"de": "Eine Maschine hat eine normalverteilte Lebensdauer (Mittelwert 0, Standardabweichung 1). Wir betrachten dies als Standard-Einheiten. Deine Aufgabe ist es, Grenzwerte für die Qualitätskontrolle zu finden.", "en": "A machine has a normally distributed lifespan (Mean 0, Std Dev 1). We view this as standard units. Your task is to find thresholds for quality control."}
    },
    "pro_tip": {
        "de": "Um die Wahrscheinlichkeit für ein Intervall zu finden, subtrahiere einfach: P(a < X ≤ b) = F(b) - F(a). Denk an deinen Stromzähler: Zählerstand Ende minus Zählerstand Anfang = Verbrauch!",
        "en": "To find the probability for an interval, simply subtract: P(a < X ≤ b) = F(b) - F(a). Think of your electric meter: Reading End minus Reading Start = Consumption!"
    }
}

def render_subtopic_3_1(model):
    """3.1 Distribution Function (CDF) - High-Fidelity Dashboard"""
    
    # --- STEP 0: THE ULTRA-ROBUST EQUAL HEIGHT PROTOCOL ---
    st.markdown("""
    <style>
    [data-testid="stHorizontalBlock"] { align-items: stretch !important; }
    [data-testid="column"] { display: flex !important; flex-direction: column !important; }
    [data-testid="column"] > div { flex: 1 !important; display: flex !important; flex-direction: column !important; }
    </style>
    """, unsafe_allow_html=True)

    st.header(t(content_3_1["title"]))
    st.markdown(t({"de": "Wie sammeln wir Wahrscheinlichkeiten?", "en": "How do we accumulate probabilities?"}))
    
    # ROW 1: THE INTUITION (Full Width)
    st.markdown(f"### {t(content_3_1['anchor']['header'])}")
    st.markdown(t(content_3_1["anchor"]["text"]))
    st.markdown("<br>", unsafe_allow_html=True)

    # ROW 2: THE THEORY (Side-by-Side)
    c1, c2 = st.columns(2, gap="medium")
    
    with c1:
        with st.container(border=True):
            st.markdown(f"**{t(content_3_1['theory']['def_title'])}**")
            st.caption(t(content_3_1['theory']['def_text']))
            st.latex(content_3_1['theory']['formula'])

            st.markdown(f"""
            <div style="font-size: 13px; color: #555; line-height: 1.5; margin-top: 10px;">
            • {t(content_3_1['theory']['props']['p1'])}<br>
            • {t(content_3_1['theory']['props']['p2'])}
            </div>
            """, unsafe_allow_html=True)

    with c2:
        with st.container(border=True):
            st.markdown(f"**{t(content_3_1['theory']['prop_title'])}**")
            st.markdown(f"""
            <div style="font-size: 14px; color: #333; line-height: 1.8; margin-bottom: 12px;">
            1. {t(content_3_1['theory']['props']['p1'])}<br>
            2. {t(content_3_1['theory']['props']['p2'])}
            </div>
            """, unsafe_allow_html=True)
            st.latex(content_3_1['theory']['limits_formula'])

    st.markdown("<br>", unsafe_allow_html=True)

    # ROW 3: THE SIMULATOR
    render_simulator_3_1()

    # EXAM SECTION
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"### {t({'de': 'Prüfungstraining', 'en': 'Exam Practice'})}")
    
    # MCQ 1: uebung2_mc6
    q_data = get_question("3.1", "uebung2_mc6")
    if q_data:
        with st.container(border=True):
            st.caption(q_data.get("source", ""))
            
            # Handle bilingual options if dict
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

def render_simulator_3_1():
    """
    Interactive Probability Scanner (PDF vs CDF).
    Standard Normal Distribution.
    """

    # --- CSS: SCOPED SLIDER ---
    st.markdown("""
    <style>
    .stSlider:has([aria-label*="Scanner"]) div[data-baseweb="slider"] > div:first-child > div:first-child { background-color: #007AFF !important; }
    .stSlider:has([aria-label*="Scanner"]) div[role="slider"] { background-color: #FFFFFF !important; border: 2px solid #007AFF !important; }
    </style>
    """, unsafe_allow_html=True)

    # ==========================================
    # SECTION 1: PLAYGROUND
    # ==========================================
    st.markdown(f"### {t(content_3_1['interactive']['header'])}")
    with st.container(border=True):
        st.caption(t(content_3_1['interactive']['desc']))

        # Controls
        x_val = st.slider("Scanner Position (x)", -3.0, 3.0, 0.0, 0.1, key="play_x_3_1")

        # Calculate Math
        cdf_val = get_normal_cdf(x_val)

        # Visuals
        fig = get_cdf_pdf_plot(x_val)
        st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

        # Live Formula
        st.latex(rf"F({x_val:.1f}) = P(X \leq {x_val:.1f}) = \mathbf{{{cdf_val:.4f}}} \quad ({cdf_val*100:.1f}\%)")

    st.markdown("<br>", unsafe_allow_html=True)

    # ==========================================
    # SECTION 2: THE MISSION
    # ==========================================
    st.markdown(f"### {t(content_3_1['interactive']['mission_title'])}")
    with st.container(border=True):
        st.markdown(t(content_3_1['interactive']['mission_desc']))
        st.markdown("---")

        # State
        if "miss_3_1_x" not in st.session_state: st.session_state.miss_3_1_x = -1.0
        if "miss_3_1_done" not in st.session_state: st.session_state.miss_3_1_done = False

        target_prob = 0.8413 # Approx 1 SD
        target_x = 1.0

        # Logic
        def is_close(val, target): return abs(val - target) < 0.15

        # Controls
        col_ctrl, col_vis = st.columns([1, 1.5], gap="large")

        with col_ctrl:
            st.markdown(f"""
            <div style="background-color: #f4f4f5; border-radius: 8px; padding: 12px; color: #3f3f46; margin-bottom: 16px;">
                <strong>{t({'de': 'Aufgabe:', 'en': 'Task:'})}</strong> {t({'de': 'Finde den Wert x, bei dem 84% der Maschinen ausgefallen sind.', 'en': 'Find the value x where 84% of machines have failed.'})}
            </div>
            """, unsafe_allow_html=True)

            val_x = st.slider(
                "Adjust Threshold (x)", -3.0, 3.0,
                value=st.session_state.miss_3_1_x,
                step=0.1,
                key="miss_3_1_x",
                disabled=st.session_state.miss_3_1_done
            )

            curr_prob = get_normal_cdf(val_x)

            if is_close(val_x, target_x):
                st.success(t({"de": "Perfekt! Das ist bei ca. +1 Standardabweichung.", "en": "Perfect! That's at approx +1 Standard Deviation."}))
                if not st.session_state.miss_3_1_done:
                    st.balloons()
                    st.session_state.miss_3_1_done = True
                    # Track Progress
                    from utils.progress_tracker import track_question_answer, update_local_progress
                    user = st.session_state.get("user")
                    if user:
                        track_question_answer(user["localId"], "vwl", "3", "3.1", "3_1_mission", True)
                        update_local_progress("3", "3.1", "3_1_mission", True)
                        # Note: We do NOT call st.rerun() here so the user can see the balloons

                if st.button(t({"de": "Neustart", "en": "Restart"})):
                    st.session_state.miss_3_1_done = False
                    st.session_state.miss_3_1_x = -1.0
                    st.rerun()
            else:
                st.session_state.miss_3_1_done = False
                diff = curr_prob - target_prob
                if diff > 0:
                    st.info(t({"de": "Zu viel! (Mehr als 84%)", "en": "Too high! (More than 84%)"}))
                else:
                    st.info(t({"de": "Zu wenig! (Weniger als 84%)", "en": "Too low! (Less than 84%)"}))

        with col_vis:
            st.metric("Accumulated Probability", f"{curr_prob:.1%}", delta=f"{curr_prob-target_prob:.1%}")
            # Simplified Visual for Mission
            fig_m = get_cdf_pdf_plot(val_x, show_pdf=False) # Only CDF for variety? Or both. Let's show both.
            st.plotly_chart(fig_m, use_container_width=True, config={'displayModeBar': False}, key="fig_miss_3_1")

    # ROW 4: PRO TIP
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"""
    <div style="background-color: #f4f4f5; border-radius: 8px; padding: 12px; color: #3f3f46;">
        <strong>Pro Tip:</strong> {t(content_3_1['pro_tip'])}
    </div>
    """, unsafe_allow_html=True)

# --- HELPER FUNCTIONS ---

def get_normal_pdf(x, mu=0, sigma=1):
    return (1 / (sigma * math.sqrt(2 * math.pi))) * math.exp(-0.5 * ((x - mu) / sigma) ** 2)

def get_normal_cdf(x, mu=0, sigma=1):
    return 0.5 * (1 + math.erf((x - mu) / (sigma * math.sqrt(2))))

def get_cdf_pdf_plot(x_highlight, show_pdf=True):
    """
    Generates a dual plot: PDF on top (filled), CDF on bottom (trace).
    Uses Standard Normal.
    """
    x_range = np.linspace(-3.5, 3.5, 200)
    pdf_vals = [get_normal_pdf(x) for x in x_range]
    cdf_vals = [get_normal_cdf(x) for x in x_range]

    fig = go.Figure()

    # 1. PDF (Top Area)
    if show_pdf:
        # Full Curve Line
        fig.add_trace(go.Scatter(
            x=x_range, y=pdf_vals,
            mode='lines', line=dict(color='#E5E5EA', width=2),
            hoverinfo='skip', showlegend=False
        ))

        # Filled Area up to x_highlight
        x_fill = [x for x in x_range if x <= x_highlight]
        y_fill = [get_normal_pdf(x) for x in x_fill]
        # Add endpoints for clean fill
        x_fill.append(x_highlight)
        y_fill.append(0)
        x_fill.insert(0, -3.5)
        y_fill.insert(0, 0)

        fig.add_trace(go.Scatter(
            x=x_fill, y=y_fill,
            fill='toself', fillcolor='rgba(0, 122, 255, 0.2)',
            line=dict(color='#007AFF', width=2),
            name='Density', hoverinfo='skip'
        ))

        # Annotation "PDF" (Blue to match slider)
        fig.add_annotation(x=-2.5, y=0.3, text="PDF (Density)", showarrow=False, font=dict(size=12, color="#007AFF"))

    # 2. CDF (Bottom Line)
    # To show it on the same chart, we might need secondary y-axis or separate plots.
    # But usually PDF and CDF have different scales (PDF can be > 1, CDF max 1).
    # For Standard Normal, max PDF is ~0.4. CDF is 1.0.
    # Let's use a single plot but clear distinction or secondary axis.
    # Actually, stacking them vertically is better in Plotly via subplots,
    # but Streamlit column layout is easier to manage than Plotly subplots for responsiveness.
    # However, let's try to put them on one chart with secondary axis to save space.

    fig.add_trace(go.Scatter(
        x=x_range, y=cdf_vals,
        mode='lines', line=dict(color='#AF52DE', width=3),
        name='CDF', yaxis='y2'
    ))

    # Dot on CDF
    curr_cdf = get_normal_cdf(x_highlight)
    fig.add_trace(go.Scatter(
        x=[x_highlight], y=[curr_cdf],
        mode='markers', marker=dict(color='#AF52DE', size=10, line=dict(color='white', width=2)),
        showlegend=False, yaxis='y2', hovertemplate="F(%{x:.1f}) = %{y:.2f}"
    ))

    # Vertical Line connecting x
    fig.add_shape(
        type="line", xref="x", yref="paper",
        x0=x_highlight, y0=0, x1=x_highlight, y1=1,
        line=dict(color="rgba(0,0,0,0.2)", width=1, dash="dash")
    )

    fig.update_layout(
        xaxis=dict(range=[-3.5, 3.5], fixedrange=True, showgrid=False),
        yaxis=dict(range=[0, 0.45], visible=False, fixedrange=True),
        yaxis2=dict(range=[0, 1.1], overlaying='y', side='right', showgrid=False, visible=False, fixedrange=True),
        margin=dict(l=0, r=0, t=10, b=20),
        height=250,
        showlegend=False,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        dragmode=False
    )

    # Annotation "CDF"
    fig.add_annotation(xref="x", yref="y2", x=2.5, y=0.9, text="CDF (Sum)", showarrow=False, font=dict(size=12, color="#AF52DE"))

    return fig
