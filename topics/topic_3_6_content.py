# Topic 3.6: Standardization (Z-Transformation)
import streamlit as st
import numpy as np
import plotly.graph_objects as go
from math import sqrt, erf
from utils.localization import t
from utils.quiz_helper import render_mcq
from utils.ask_yourself import render_ask_yourself
from utils.exam_essentials import render_exam_essentials
from views.styles import inject_equal_height_css
from data.exam_questions import get_question
from utils.progress_tracker import track_question_answer, update_local_progress

# ==========================================
# 1. CONTENT DICTIONARY
# ==========================================
content_3_6 = {
    "title": {"de": "3.6 Standardisieren", "en": "3.6 Standardization"},
    "subtitle": {"de": "Die universelle Sprache der Statistik", "en": "The Universal Language of Statistics"},
    "intuition": {
        "header": {"de": "Die Intuition", "en": "The Intuition"},
        "text": {
            "de": "Stell dir vor, du vergleichst Prüfungsnoten aus zwei verschiedenen Ländern. Land A benotet von 0-100 (Durchschnitt 65). Land B benotet von 1-6 (Durchschnitt 4.2). Rohwerte sind nutzlos für Vergleiche. **Standardisierung** ist wie das Umrechnen aller Währungen in Dollar — sie schafft eine universelle Sprache, in der '1.5 Standardabweichungen über dem Durchschnitt' überall dasselbe bedeutet.",
            "en": "Imagine comparing exam scores from two different countries. Country A grades 0-100 (average 65). Country B grades 1-6 (average 4.2). Raw values are useless for comparison. **Standardization** is like converting all currencies to dollars — it creates a universal language where '1.5 standard deviations above average' means the same thing everywhere."
        }
    },
    "variable_decoder": {
        "de": "$Z$ = <strong>Standardisierter Wert</strong> — Wie viele Standardabweichungen vom Mittelwert entfernt?<br>$X$ = <strong>Originalwert</strong> — Der Rohwert in der ursprünglichen Skala<br>$\\mu$ = <strong>Mittelwert</strong> — Das Zentrum der Verteilung<br>$\\sigma$ = <strong>Standardabweichung</strong> — Die Streuung der Verteilung",
        "en": "$Z$ = <strong>Standardized Value</strong> — How many standard deviations from the mean?<br>$X$ = <strong>Original Value</strong> — The raw value in the original scale<br>$\\mu$ = <strong>Mean</strong> — The center of the distribution<br>$\\sigma$ = <strong>Standard Deviation</strong> — The spread of the distribution"
    },
    "key_insight": {
        "de": "Der Z-Score ist die <strong>universelle Währung</strong> der Statistik. Egal ob Prüfungsnoten (0-100), IQ-Werte (100 ± 15), oder Körpergrössen — ein Z von +1.5 bedeutet überall dasselbe: 'deutlich überdurchschnittlich'. Das macht Vergleiche zwischen komplett unterschiedlichen Skalen möglich!",
        "en": "The Z-score is the <strong>universal currency</strong> of statistics. Whether exam scores (0-100), IQ values (100 ± 15), or heights — a Z of +1.5 means the same everywhere: 'significantly above average'. This makes comparisons between completely different scales possible!"
    },
    "theory": {
        "forward_title": {"de": "Standardisierung", "en": "Standardization"},
        "forward_text": {"de": "Subtrahiere das Zentrum, teile durch die Streuung.", "en": "Subtract the center, divide by the spread."},
        "reverse_title": {"de": "De-Standardisierung", "en": "De-Standardization"},
        "reverse_text": {"de": "Aus Z zurück zu X: Multipliziere mit σ, addiere μ.", "en": "From Z back to X: Multiply by σ, add μ."}
    },
    "frag_dich": {
        "header": {"de": "Frag dich: Brauche ich Standardisierung?", "en": "Ask yourself: Do I need standardization?"},
        "questions": [
            {"de": "Muss ich Werte aus verschiedenen Skalen vergleichen?", "en": "Do I need to compare values from different scales?"},
            {"de": "Suche ich einen Wert in der Z-Tabelle (Standardnormalverteilung)?", "en": "Am I looking up a value in the Z-table (standard normal)?"},
            {"de": "Sehe ich Φ(z) oder 'N(0,1)' in der Aufgabe?", "en": "Do I see Φ(z) or 'N(0,1)' in the problem?"},
            {"de": "Muss ich von Z zurück zum Originalwert rechnen?", "en": "Do I need to convert from Z back to the original value?"}
        ],
        "conclusion": {"de": "Mindestens 1× JA? → Standardisierung ist der Schlüssel!", "en": "At least 1 YES? → Standardization is the key!"}
    },
    "exam_essentials": {
        "trap": {
            "de": "Nach dem Nachschlagen von Z in der Tabelle vergessen, zurück zur Original-Skala zu rechnen. Du findest z.B. Z = 1.645 für das 95%-Perzentil, aber die Aufgabe fragt nach dem Wert in der Originalverteilung!",
            "en": "After looking up Z in the table, forgetting to convert back to the original scale. You find Z = 1.645 for the 95th percentile, but the question asks for the value in the original distribution!"
        },
        "trap_rule": {
            "de": "Immer prüfen: Fragt die Aufgabe nach Z oder nach X? Wenn X: X = μ + Z·σ nicht vergessen!",
            "en": "Always check: Does the question ask for Z or X? If X: Don't forget X = μ + Z·σ!"
        },
        "tips": [
            {
                "tip": {"de": "Standardisieren: Z = (X - μ) / σ", "en": "Standardize: Z = (X - μ) / σ"},
                "why": {"de": "Wandelt jeden Wert in 'Anzahl Standardabweichungen vom Mittelwert' um.", "en": "Converts any value to 'number of standard deviations from the mean'."}
            },
            {
                "tip": {"de": "De-Standardisieren: X = μ + Z·σ", "en": "De-standardize: X = μ + Z·σ"},
                "why": {"de": "Wandelt Z zurück in die Originalskala — unverzichtbar für Perzentil-Aufgaben!", "en": "Converts Z back to the original scale — essential for percentile problems!"}
            },
            {
                "tip": {"de": "Symmetrie-Shortcut: Φ(-z) = 1 - Φ(z)", "en": "Symmetry shortcut: Φ(-z) = 1 - Φ(z)"},
                "why": {"de": "Spart Nachschlagen für negative Z-Werte. Die Standardnormalverteilung ist symmetrisch um 0!", "en": "Saves lookup for negative Z values. The standard normal is symmetric around 0!"}
            }
        ]
    },
    "playground": {
        "title": {"de": "Z-Tabellen Explorer", "en": "Z-Table Explorer"},
        "desc": {"de": "Bewege den Slider und beobachte, wie sich Z-Wert und Wahrscheinlichkeit zueinander verhalten.", "en": "Move the slider and observe how Z-value and probability relate to each other."}
    },
    "mission": {
        "title": {"de": "Mission: Der Noten-Übersetzer", "en": "Mission: The Grade Translator"},
        "desc": {
            "de": "Ein Student hat **85 Punkte** in einem Kurs erzielt, wo $\\mu = 70$ und $\\sigma = 10$. Was ist die **äquivalente Punktzahl** in einem Kurs mit $\\mu = 500$ und $\\sigma = 100$?",
            "en": "A student scored **85 points** in a class where $\\mu = 70$ and $\\sigma = 10$. What is the **equivalent score** in a class where $\\mu = 500$ and $\\sigma = 100$?"
        },
        "target": 650,
        "tolerance": 10
    }
}


def render_subtopic_3_6(model):
    """3.6 Standardization - The Universal Translator"""
    
    inject_equal_height_css()
    
    # Slider styling
    st.markdown("""
    <style>
    /* Blue slider for Z */
    .stSlider:has([aria-label*="Z"]) div[data-baseweb="slider"] > div:first-child > div:first-child { background-color: #007AFF !important; }
    .stSlider:has([aria-label*="Z"]) div[role="slider"] { background-color: #FFFFFF !important; border: 2px solid #007AFF !important; }
    
    /* Purple slider for equivalent */
    .stSlider:has([aria-label*="Equivalent"]) div[data-baseweb="slider"] > div:first-child > div:first-child { background-color: #AF52DE !important; }
    .stSlider:has([aria-label*="Equivalent"]) div[role="slider"] { background-color: #FFFFFF !important; border: 2px solid #AF52DE !important; }
    </style>
    """, unsafe_allow_html=True)

    st.header(t(content_3_6["title"]))
    st.markdown(t(content_3_6["subtitle"]))
    st.markdown("---")
    
    # --- INTUITION (Header OUTSIDE per header-out protocol) ---
    st.markdown(f"### {t(content_3_6['intuition']['header'])}")
    with st.container(border=True):
        st.markdown(t(content_3_6["intuition"]["text"]))
    
    st.markdown("<br>", unsafe_allow_html=True)

    # --- THEORY SECTION: Using Layout B (Comparison) - Gold Standard from Topic 1.6 ---
    from utils.layouts import render_comparison
    render_comparison(
        title={"de": "Die zwei Richtungen der Standardisierung", "en": "The Two Directions of Standardization"},
        intuition=None,  # Already have intuition above
        left={
            "title": {"de": "Standardisierung", "en": "Standardization"},
            "intuition": {"de": "Subtrahiere das Zentrum, teile durch die Streuung.", "en": "Subtract the center, divide by the spread."},
            "formula": r"Z = \frac{X - \mu}{\sigma}",
            "variables": [
                {"symbol": "Z", "name": {"de": "Z-Score", "en": "Z-Score"}, "description": {"de": "Wie viele σ vom μ entfernt?", "en": "How many σ from μ?"}},
                {"symbol": "X", "name": {"de": "Originalwert", "en": "Original value"}, "description": {"de": "Der Rohwert", "en": "The raw value"}},
                {"symbol": r"\mu", "name": {"de": "Mittelwert", "en": "Mean"}, "description": {"de": "Das Zentrum", "en": "The center"}},
                {"symbol": r"\sigma", "name": {"de": "Standardabweichung", "en": "Std Dev"}, "description": {"de": "Die Streuung", "en": "The spread"}}
            ],
            "insight": {"de": "Ergebnis: Z ~ N(0, 1) — universell vergleichbar!", "en": "Result: Z ~ N(0, 1) — universally comparable!"}
        },
        right={
            "title": {"de": "De-Standardisierung", "en": "De-Standardization"},
            "intuition": {"de": "Von Z zurück zu X: Multipliziere mit σ, addiere μ.", "en": "From Z back to X: Multiply by σ, add μ."},
            "formula": r"X = \mu + Z \cdot \sigma",
            "variables": [
                {"symbol": "X", "name": {"de": "Gesuchter Wert", "en": "Target value"}, "description": {"de": "In Originalskala", "en": "In original scale"}},
                {"symbol": "Z", "name": {"de": "Z-Score", "en": "Z-Score"}, "description": {"de": "Aus Tabelle", "en": "From table"}},
                {"symbol": r"\mu", "name": {"de": "Mittelwert", "en": "Mean"}, "description": {"de": "Zentrum der Zielskala", "en": "Center of target scale"}},
                {"symbol": r"\sigma", "name": {"de": "Standardabweichung", "en": "Std Dev"}, "description": {"de": "Streuung der Zielskala", "en": "Spread of target scale"}}
            ],
            "insight": {"de": "Anwendung: Perzentile finden (z.B. 'Top 5%' in Punkten)", "en": "Use: Finding percentiles (e.g., 'Top 5%' in points)"}
        },
        key_difference={
            "de": "<strong>Der Z-Score ist die universelle Währung der Statistik.</strong> Egal ob Prüfungsnoten, IQ-Werte oder Körpergrössen — ein Z von +1.5 bedeutet überall dasselbe.",
            "en": "<strong>The Z-score is the universal currency of statistics.</strong> Whether exam scores, IQ values, or heights — a Z of +1.5 means the same everywhere."
        },
        show_header=True
    )

    st.markdown("<br><br>", unsafe_allow_html=True)

    # --- SECTION 1: Z-TABLE EXPLORER (Playground) ---
    render_z_table_explorer()

    st.markdown("<br><br>", unsafe_allow_html=True)

    # --- SECTION 2: GRADE TRANSLATOR (Mission) ---
    render_grade_translator_mission()

    st.markdown("<br><br>", unsafe_allow_html=True)

    # --- FRAG DICH (Ask Yourself) ---
    render_ask_yourself(
        header=content_3_6["frag_dich"]["header"],
        questions=content_3_6["frag_dich"]["questions"],
        conclusion=content_3_6["frag_dich"]["conclusion"]
    )

    st.markdown("<br><br>", unsafe_allow_html=True)

    # --- EXAM ESSENTIALS ---
    render_exam_essentials(
        trap=content_3_6["exam_essentials"]["trap"],
        trap_rule=content_3_6["exam_essentials"]["trap_rule"],
        tips=content_3_6["exam_essentials"]["tips"]
    )

    st.markdown("<br><br>", unsafe_allow_html=True)

    # --- EXAM PRACTICE ---
    st.markdown(f"### {t({'de': 'Prüfungstraining', 'en': 'Exam Practice'})}")
    
    # MCQ from test3_mc2 (currently in 3.5, should be moved to 3.6)
    q_data = get_question("3.6", "test3_mc2")
    if q_data:
        with st.container(border=True):
            st.caption(q_data.get("source", ""))
            opts = q_data.get("options", [])
            if opts and isinstance(opts[0], dict):
                option_labels = [t(o) for o in opts]
            else:
                option_labels = opts
            
            render_mcq(
                key_suffix="3_6_mc2",
                question_text=t(q_data["question"]),
                options=option_labels,
                correct_idx=q_data["correct_idx"],
                solution_text_dict=q_data["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
                client=model,
                ai_context="Standardization of random variables, E[Y^2] calculation",
                course_id="vwl",
                topic_id="3",
                subtopic_id="3.6",
                question_id="3_6_mc2"
            )


@st.fragment
def render_z_table_explorer():
    """Interactive Z-Table: See the relationship between Z and Φ(Z)"""
    
    st.markdown(f"### {t(content_3_6['playground']['title'])}")
    st.caption(t(content_3_6["playground"]["desc"]))
    
    # Controls and visualization side by side
    col_ctrl, col_vis = st.columns([1, 2], gap="large")
    
    with col_ctrl:
        z_val = st.slider(
            t({"de": "Z-Wert", "en": "Z-Value"}),
            -3.0, 3.0, 0.0, 0.05,
            key="z_explorer_slider"
        )
        
        # Calculate probability
        prob = get_normal_cdf(z_val)
        
        st.metric(t({"de": "Wahrscheinlichkeit Φ(Z)", "en": "Probability Φ(Z)"}), f"{prob:.4f}")
        st.metric(t({"de": "Als Prozent", "en": "As Percent"}), f"{prob:.1%}")
        
        # Quick reference
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(f"**{t({'de': 'Schnellreferenz', 'en': 'Quick Reference'})}**")
        st.caption("Φ(-1.96) = 2.5%  |  Φ(0) = 50%  |  Φ(1.96) = 97.5%")
        
    with col_vis:
        fig = create_z_distribution_plot(z_val, prob)
        st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
    
    # Live formula with semantic colors (Blue = Z, Purple = Probability)
    st.latex(rf"\Phi({{\color{{blue}}{z_val:.2f}}}) = P(Z \leq {{\color{{blue}}{z_val:.2f}}}) = {{\color{{purple}}\mathbf{{{prob:.4f}}}}}")


@st.fragment
def render_grade_translator_mission():
    """Mission: Translate grades between different scales using Z-scores"""
    
    st.markdown(f"### {t(content_3_6['mission']['title'])}")
    st.markdown(t(content_3_6["mission"]["desc"]))
    st.markdown("---")
    
    # State
    if "mission_3_6_done" not in st.session_state:
        st.session_state.mission_3_6_done = False
    if "user_answer_3_6" not in st.session_state:
        st.session_state.user_answer_3_6 = 500
    
    # Fixed parameters for mission
    score_a = 85
    mu_a, sigma_a = 70, 10
    mu_b, sigma_b = 500, 100
    
    # Calculate correct answer
    z_score = (score_a - mu_a) / sigma_a  # = 1.5
    correct_score_b = mu_b + z_score * sigma_b  # = 650
    
    # Two-column layout for the two "schools"
    col_a, col_b = st.columns(2, gap="large")
    
    with col_a:
        st.markdown(f"""
        <div style="background-color: rgba(0, 122, 255, 0.08); border: 2px solid #007AFF; border-radius: 8px; padding: 16px;">
            <div style="font-weight: 600; color: #007AFF; margin-bottom: 8px;">
                {t({'de': 'Kurs A (Gegeben)', 'en': 'Class A (Given)'})}
            </div>
            <div style="font-size: 14px; color: #333;">
                μ = {mu_a}, σ = {sigma_a}<br>
                <strong>{t({'de': 'Punktzahl', 'en': 'Score'})}: {score_a}</strong>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col_b:
        st.markdown(f"""
        <div style="background-color: rgba(175, 82, 222, 0.08); border: 2px solid #AF52DE; border-radius: 8px; padding: 16px;">
            <div style="font-weight: 600; color: #AF52DE; margin-bottom: 8px;">
                {t({'de': 'Kurs B (Ziel)', 'en': 'Class B (Target)'})}
            </div>
            <div style="font-size: 14px; color: #333;">
                μ = {mu_b}, σ = {sigma_b}<br>
                <strong>{t({'de': 'Äquivalente Punktzahl', 'en': 'Equivalent Score'})}: ?</strong>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # User input
    user_answer = st.slider(
        t({"de": "Deine Antwort: Equivalent Score in Kurs B", "en": "Your Answer: Equivalent Score in Class B"}),
        300, 700, st.session_state.user_answer_3_6, 5,
        key="user_answer_3_6",
        disabled=st.session_state.mission_3_6_done
    )
    
    # Z-score display (always show)
    st.markdown(f"**Z-Score = (85 - 70) / 10 = {z_score:.1f}**")
    
    # Feedback
    tolerance = content_3_6["mission"]["tolerance"]
    is_correct = abs(user_answer - correct_score_b) <= tolerance
    
    if is_correct:
        if not st.session_state.mission_3_6_done:
            st.balloons()
            st.session_state.mission_3_6_done = True
            user = st.session_state.get("user")
            if user:
                track_question_answer(user["localId"], "vwl", "3", "3.6", "3_6_mission", True)
                update_local_progress("3", "3.6", "3_6_mission", True)
        
        st.success(t({
            "de": f"Perfekt! {score_a} in Kurs A entspricht {int(correct_score_b)} in Kurs B (beide sind Z = +1.5).",
            "en": f"Perfect! {score_a} in Class A equals {int(correct_score_b)} in Class B (both are Z = +1.5)."
        }))
        
        if st.button(t({"de": "Nochmal spielen", "en": "Play again"}), key="reset_3_6"):
            st.session_state.mission_3_6_done = False
            st.session_state.user_answer_3_6 = 500
            st.rerun()
    else:
        st.session_state.mission_3_6_done = False
        diff = user_answer - correct_score_b
        if diff > 0:
            st.info(t({"de": "Zu hoch! Denk an die Formel: X = μ + Z·σ", "en": "Too high! Think about the formula: X = μ + Z·σ"}))
        else:
            st.info(t({"de": "Zu niedrig! Denk an die Formel: X = μ + Z·σ", "en": "Too low! Think about the formula: X = μ + Z·σ"}))


# --- HELPER FUNCTIONS ---

def get_normal_cdf(x, mu=0, sigma=1):
    """Standard normal CDF using error function"""
    return 0.5 * (1 + erf((x - mu) / (sigma * sqrt(2))))


def create_z_distribution_plot(z_highlight, prob):
    """Creates a standard normal distribution with shaded area up to z_highlight"""
    
    x_range = np.linspace(-3.5, 3.5, 200)
    pdf_vals = (1 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * x_range**2)
    
    fig = go.Figure()
    
    # Full curve (gray outline)
    fig.add_trace(go.Scatter(
        x=x_range, y=pdf_vals,
        mode='lines', line=dict(color='#E5E5EA', width=2),
        hoverinfo='skip', showlegend=False
    ))
    
    # Filled area up to z_highlight (blue)
    x_fill = x_range[x_range <= z_highlight]
    y_fill = (1 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * x_fill**2)
    
    # Add endpoints for clean fill
    x_fill_list = list(x_fill) + [z_highlight, x_fill[0]]
    y_fill_list = list(y_fill) + [0, 0]
    
    fig.add_trace(go.Scatter(
        x=x_fill_list, y=y_fill_list,
        fill='toself', fillcolor='rgba(0, 122, 255, 0.3)',
        line=dict(color='#007AFF', width=2),
        hoverinfo='skip', showlegend=False
    ))
    
    # Vertical line at z_highlight
    fig.add_shape(
        type="line", x0=z_highlight, x1=z_highlight, y0=0, y1=0.45,
        line=dict(color="#007AFF", width=2, dash="dash")
    )
    
    # Annotation for probability
    fig.add_annotation(
        x=z_highlight, y=0.42,
        text=f"Z = {z_highlight:.2f}",
        showarrow=False, font=dict(size=12, color="#007AFF")
    )
    
    fig.update_layout(
        xaxis=dict(
            title="Z", range=[-3.5, 3.5], 
            tickmode='array', tickvals=[-3, -2, -1, 0, 1, 2, 3],
            fixedrange=True, showgrid=False
        ),
        yaxis=dict(visible=False, range=[0, 0.45], fixedrange=True),
        margin=dict(l=20, r=20, t=20, b=40),
        height=250,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        showlegend=False
    )
    
    return fig
