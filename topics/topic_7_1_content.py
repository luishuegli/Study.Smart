# Topic 7.1: Frequency Distribution, Histogram and Distribution Function
# ULTRATHINK ENHANCED VERSION
import streamlit as st
import numpy as np
import plotly.graph_objects as go
from views.styles import inject_equal_height_css
from utils.localization import t
from utils.quiz_helper import render_mcq
from utils.ask_yourself import render_ask_yourself
from utils.exam_essentials import render_exam_essentials
from utils.worked_example import render_worked_example
from utils.layouts import (
    render_comparison,
    render_definition,
    render_single_formula,
)
from utils.layouts.foundation import intuition_box, grey_callout
from data.exam_questions import get_question

# ==========================================
# 1. CONTENT DICTIONARY - BILINGUAL (ULTRATHINK)
# ==========================================

content_7_1 = {
    "title": {"de": "7.1 Häufigkeitsverteilung, Histogramm und Verteilungsfunktion", 
              "en": "7.1 Frequency Distribution, Histogram and Distribution Function"},
    "subtitle": {
        "de": "Von theoretischen Verteilungen zu realen Daten",
        "en": "From theoretical distributions to real data"
    },
    
    # --- INTUITION ---
    "intuition": {
        "de": """In der Wahrscheinlichkeitsrechnung (Teil I) haben wir theoretische Verteilungen 
        wie die Normalverteilung studiert. Jetzt wechseln wir die Perspektive: Statt von 
        einem bekannten Modell auszugehen, <strong>haben wir Daten und suchen das passende Modell</strong>.
        <br><br>
        Stell dir vor, du arbeitest in einer Fabrik und misst die Gewichte von 1000 Produkten. 
        Wie fasst du diese 1000 Zahlen zusammen? Du gruppierst sie in Klassen und zählst, 
        wie viele Produkte in jede Klasse fallen. Das ist die <strong>Häufigkeitsverteilung</strong>.""",
        "en": """In probability theory (Part I), we studied theoretical distributions 
        like the normal distribution. Now we shift perspective: Instead of starting from 
        a known model, <strong>we have data and search for the right model</strong>.
        <br><br>
        Imagine you work in a factory and measure the weights of 1000 products. 
        How do you summarize these 1000 numbers? You group them into classes and count 
        how many products fall into each class. This is the <strong>frequency distribution</strong>."""
    },
    
    # --- FREQUENCY COMPARISON ---
    "frequency_comparison": {
        "header": {"de": "Absolute vs. Relative Häufigkeit", "en": "Absolute vs. Relative Frequency"},
        "left": {
            "title": {"de": "Absolute Häufigkeit", "en": "Absolute Frequency"},
            "notation": r"n_j",
            "formula": r"n_j = |\{i : y_i = j\}|",
            "intuition": {
                "de": "Wie viele Beobachtungen fallen in Klasse j?",
                "en": "How many observations fall into class j?"
            },
            "example": {"de": "Bei 50 Würfelwürfen: 8× die Sechs → n₆ = 8", 
                       "en": "In 50 die rolls: 8× the six → n₆ = 8"}
        },
        "right": {
            "title": {"de": "Relative Häufigkeit", "en": "Relative Frequency"},
            "notation": r"f_j",
            "formula": r"f_j = \frac{n_j}{n}",
            "intuition": {
                "de": "Welcher Anteil der Daten liegt in Klasse j?",
                "en": "What proportion of data is in class j?"
            },
            "example": {"de": "n₆ = 8 von n = 50 → f₆ = 8/50 = 0.16 = 16%", 
                       "en": "n₆ = 8 out of n = 50 → f₆ = 8/50 = 0.16 = 16%"}
        }
    },
    
    # --- HISTOGRAM DEFINITION ---
    "histogram_def": {
        "term": {"de": "Histogramm", "en": "Histogram"},
        "formal": {
            "de": "Ein Histogram ist eine grafische Darstellung der Häufigkeitsverteilung. Die Fläche jedes Balkens entspricht der relativen Häufigkeit der Klasse.",
            "en": "A histogram is a graphical representation of the frequency distribution. The area of each bar corresponds to the relative frequency of the class."
        },
        "plain": {
            "de": "Fläche = Häufigkeit (nicht die Höhe!)",
            "en": "Area = Frequency (not the height!)"
        }
    },
    
    # --- ECDF FORMULA ---
    "ecdf": {
        "header": {"de": "Die Empirische Verteilungsfunktion", "en": "The Empirical Distribution Function"},
        "intuition": {
            "de": "Wie viel Prozent der Daten sind kleiner oder gleich y?",
            "en": "What percentage of data is less than or equal to y?"
        },
        "formula": r"F_n(y) = \frac{1}{n} \sum_{i=1}^{n} \mathbf{1}_{y_i \le y} = \frac{\#(y_i \le y)}{n}",
        "variables": [
            {"symbol": r"F_n(y)", "name": {"de": "ECDF-Wert", "en": "ECDF value"}, 
             "description": {"de": "Anteil der Daten ≤ y", "en": "Proportion of data ≤ y"}},
            {"symbol": r"n", "name": {"de": "Stichprobengrösse", "en": "Sample size"}, 
             "description": {"de": "Gesamtzahl der Beobachtungen", "en": "Total number of observations"}},
            {"symbol": r"\mathbf{1}_{y_i \le y}", "name": {"de": "Indikatorfunktion", "en": "Indicator function"}, 
             "description": {"de": "= 1 wenn yᵢ ≤ y, sonst 0", "en": "= 1 if yᵢ ≤ y, else 0"}},
        ],
        "insight": {
            "de": "Die ECDF ist eine Treppenfunktion, die bei jedem Datenpunkt um 1/n springt.",
            "en": "The ECDF is a step function that jumps by 1/n at each data point."
        }
    },
    
    # --- WORKED EXAMPLE (Americium-241) ---
    "worked_example": {
        "header": {"de": "Beispiel: Radioaktiver Zerfall", "en": "Example: Radioactive Decay"},
        "problem": {
            "de": "Das radioaktive Element Americium-241 emittiert Teilchen. In einem Experiment wurden 1207 Intervalle von je 10 Sekunden beobachtet und die Anzahl der Emissionen gezählt. Gesamtzahl: 10'129 Emissionen.",
            "en": "The radioactive element Americium-241 emits particles. In an experiment, 1207 intervals of 10 seconds each were observed and the number of emissions counted. Total: 10,129 emissions."
        },
        "steps": [
            {
                "label": {"de": "Gegeben", "en": "Given"},
                "latex": r"n = {\color{#007AFF}1207}, \quad \Sigma = {\color{#FF4B4B}10129}",
                "note": {"de": "Blau = Stichprobengrösse, Rot = Summe", "en": "Blue = sample size, Red = total"}
            },
            {
                "label": {"de": "Mittlere Emissionen", "en": "Mean emissions"},
                "latex": r"\bar{y} = \frac{{\color{#FF4B4B}10129}}{{\color{#007AFF}1207}} \approx {\color{#16a34a}8.39}",
                "note": {"de": "Grün = Ergebnis", "en": "Green = result"}
            },
            {
                "label": {"de": "Klassenbildung", "en": "Class formation"},
                "latex": r"C_1 = [0, 2], \; C_2 = \{3\}, \; \ldots, \; C_{15} = \{16\}, \; C_{16} = [17, \infty)",
                "note": {"de": "Randklassen für extreme Werte", "en": "Edge classes for extreme values"}
            }
        ],
        "answer": {
            "de": "Mit den Klassenhäufigkeiten erstellt man ein Histogramm. Das Muster ähnelt einer Poisson-Verteilung mit λ ≈ 8.4.",
            "en": "Using class frequencies, we create a histogram. The pattern resembles a Poisson distribution with λ ≈ 8.4."
        }
    },
    
    # --- FRAG DICH ---
    "frag_dich": {
        "header": {"de": "Frag dich: Histogram oder ECDF?", "en": "Ask yourself: Histogram or ECDF?"},
        "questions": [
            {"de": "Willst du die <strong>Form der Verteilung</strong> sehen? → Histogram", 
             "en": "Do you want to see the <strong>shape of the distribution</strong>? → Histogram"},
            {"de": "Willst du <strong>Quantile ablesen</strong> (z.B. Median)? → ECDF", 
             "en": "Do you want to <strong>read quantiles</strong> (e.g., median)? → ECDF"},
            {"de": "Hast du <strong>wenige Daten</strong> (n < 30)? → ECDF (robuster)", 
             "en": "Do you have <strong>few data points</strong> (n < 30)? → ECDF (more robust)"},
            {"de": "Willst du mit einer <strong>theoretischen Verteilung</strong> vergleichen? → Beide möglich", 
             "en": "Do you want to compare with a <strong>theoretical distribution</strong>? → Both work"},
        ],
        "conclusion": {"de": "Histogram → Form | ECDF → Quantile", "en": "Histogram → Shape | ECDF → Quantiles"}
    },
    
    # --- EXAM ESSENTIALS ---
    "exam_essentials": {
        "trap": {
            "de": "<strong>Häufigkeit ≠ Wahrscheinlichkeit verwechseln:</strong> Relative Häufigkeit $f_j$ ist eine <em>Schätzung</em> für $P(X=j)$, nicht die wahre Wahrscheinlichkeit.",
            "en": "<strong>Confusing Frequency ≠ Probability:</strong> Relative frequency $f_j$ is an <em>estimate</em> for $P(X=j)$, not the true probability."
        },
        "trap_rule": {
            "de": "Immer sagen: 'geschätzte Wahrscheinlichkeit' oder 'beobachtete Häufigkeit'",
            "en": "Always say: 'estimated probability' or 'observed frequency'"
        },
        "tips": [
            {
                "tip": {"de": "Histogramm: Fläche = Häufigkeit", "en": "Histogram: Area = Frequency"},
                "why": {"de": "Bei ungleichen Klassenbreiten ist die Balkenhöhe NICHT die Häufigkeit!", 
                       "en": "With unequal class widths, bar height is NOT the frequency!"}
            },
            {
                "tip": {"de": "ECDF ablesen: $F_n(y)$ = Wert auf y-Achse", "en": "Reading ECDF: $F_n(y)$ = value on y-axis"},
                "why": {"de": "Median bei $F_n(y) = 0.5$, Quartile bei $0.25$ und $0.75$", 
                       "en": "Median at $F_n(y) = 0.5$, quartiles at $0.25$ and $0.75$"}
            },
            {
                "tip": {"de": "Summe aller $f_j = 1$", "en": "Sum of all $f_j = 1$"},
                "why": {"de": "Check für Rechenfehler – alle relativen Häufigkeiten müssen $1$ ergeben", 
                       "en": "Sanity check – all relative frequencies must sum to $1$"}
            }
        ]
    }
}


# ==========================================
# 2. INTERACTIVE: DISTRIBUTION MATCHER
# ==========================================

@st.fragment
def distribution_matcher():
    """Interactive: Match histogram shape to theoretical distribution."""
    
    # State initialization
    if "dm_attempts" not in st.session_state:
        st.session_state.dm_attempts = 0
    if "dm_correct" not in st.session_state:
        st.session_state.dm_correct = 0
    if "dm_current" not in st.session_state:
        st.session_state.dm_current = 0
    
    # Distribution scenarios (matching exam exercise HS2015)
    # Use fixed seed per scenario for consistent display during fragment reruns
    np.random.seed(42 + st.session_state.dm_current)
    scenarios = [
        {
            "data": np.random.normal(0, np.sqrt(3), 200),  # N(0, 3)
            "correct": "v1",
            "params": r"$N(\mu=0, \sigma^2=3)$"
        },
        {
            "data": np.random.exponential(1/3, 200),  # Exp(λ=3)
            "correct": "v2",
            "params": r"$\text{Exp}(\lambda=3)$"
        },
        {
            "data": np.random.normal(0, 1, 200),  # N(0, 1)
            "correct": "v3",
            "params": r"$N(\mu=0, \sigma^2=1)$"
        },
        {
            "data": np.random.uniform(-3, 3, 200),  # U[-3, 3]
            "correct": "v4",
            "params": r"$U[-3, 3]$"
        }
    ]
    
    current = scenarios[st.session_state.dm_current % len(scenarios)]
    
    # Scenario description
    st.markdown(f"""
<div style="background: #f4f4f5; border-left: 4px solid #a1a1aa; 
            padding: 12px 16px; border-radius: 8px; color: #3f3f46;">
<strong>{t({"de": "Szenario", "en": "Scenario"})}:</strong><br>
{t({"de": "Eine Stichprobe von 200 Beobachtungen wurde aus einer der folgenden Verteilungen gezogen. Welche passt?", 
    "en": "A sample of 200 observations was drawn from one of the following distributions. Which one fits?"})}
</div>
""", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"**{t({'de': 'Mission', 'en': 'Mission'})}:** {t({'de': 'Ordne das Histogramm der richtigen Verteilung zu!', 'en': 'Match the histogram to the correct distribution!'})}")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Create histogram
    fig = go.Figure()
    
    # Add histogram with semantic coloring
    fig.add_trace(go.Histogram(
        x=current["data"],
        nbinsx=15,
        marker_color="#007AFF",  # Blue for neutral/data
        opacity=0.8,
        name=t({"de": "Beobachtete Daten", "en": "Observed Data"})
    ))
    
    fig.update_layout(
        height=300,
        margin=dict(t=30, b=50, l=50, r=30),
        xaxis_title=t({"de": "Wert", "en": "Value"}),
        yaxis_title=t({"de": "Häufigkeit", "en": "Frequency"}),
        showlegend=False,
        clickmode='none',
        hovermode=False
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Answer options with mathematical notation (exam-style)
    options = {
        "v1": r"V1) $N(0, 3)$",
        "v2": r"V2) $\text{Exp}(\lambda=3)$",
        "v3": r"V3) $N(0, 1)$",
        "v4": r"V4) $U[-3, 3]$"
    }
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("V1) N(0, 3)", key="dm_v1", use_container_width=True):
            check_answer("v1", current["correct"])
        if st.button("V2) Exp(λ=3)", key="dm_v2", use_container_width=True):
            check_answer("v2", current["correct"])
    
    with col2:
        if st.button("V3) N(0, 1)", key="dm_v3", use_container_width=True):
            check_answer("v3", current["correct"])
        if st.button("V4) U[-3, 3]", key="dm_v4", use_container_width=True):
            check_answer("v4", current["correct"])
    
    # Progress display
    if st.session_state.dm_attempts > 0:
        st.markdown("<br>", unsafe_allow_html=True)
        progress = st.session_state.dm_correct / st.session_state.dm_attempts
        color = "#16a34a" if progress >= 0.75 else "#FF4B4B" if progress < 0.5 else "#6B7280"
        st.markdown(f"""
<div style="text-align: center; color: {color};">
<strong>{st.session_state.dm_correct}/{st.session_state.dm_attempts}</strong> {t({"de": "richtig", "en": "correct"})}
</div>
""", unsafe_allow_html=True)
    
    # Completion state
    if st.session_state.dm_attempts >= 4:
        st.markdown("<br>", unsafe_allow_html=True)
        st.success(t({
            "de": "Mission abgeschlossen! Du hast gelernt, Histogramme mit theoretischen Verteilungen zu verknüpfen.",
            "en": "Mission complete! You learned to connect histograms with theoretical distributions."
        }))
        
        # Discovery debrief
        st.markdown(f"""
<div style="background: #f4f4f5; border-left: 4px solid #a1a1aa; 
            padding: 12px 16px; border-radius: 8px; color: #3f3f46;">
<strong>{t({"de": "Was du entdeckt hast", "en": "What you discovered"})}:</strong><br>
{t({"de": "Die Form eines Histogramms verrät viel über die zugrunde liegende Verteilung. Symmetrie, Schiefe und Spannweite sind die Schlüsselmerkmale.", 
    "en": "The shape of a histogram reveals much about the underlying distribution. Symmetry, skewness, and spread are the key features."})}
</div>
""", unsafe_allow_html=True)


def check_answer(selected, correct):
    """Check answer and update state."""
    st.session_state.dm_attempts += 1
    if selected == correct:
        st.session_state.dm_correct += 1
        st.toast(t({"de": "Richtig!", "en": "Correct!"}))
    else:
        st.toast(t({"de": "Falsch. Schau dir die Form nochmal an.", "en": "Wrong. Look at the shape again."}))
    
    # Move to next scenario
    st.session_state.dm_current += 1
    st.rerun(scope="fragment")


# ==========================================
# 3. RENDER FUNCTION
# ==========================================

def render_subtopic_7_1(model):
    """7.1 Häufigkeitsverteilung, Histogramm und Verteilungsfunktion"""
    
    # Inject equal height CSS for comparison sections
    inject_equal_height_css()
    
    st.header(t(content_7_1["title"]))
    st.caption(t(content_7_1["subtitle"]))
    st.markdown("---")
    
    # === 1. INTUITION ===
    intuition_box(content_7_1["intuition"])
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # === 2. THEORY: Frequency Comparison ===
    st.markdown(f"### {t(content_7_1['frequency_comparison']['header'])}")
    
    c1, c2 = st.columns(2, gap="medium")
    
    with c1:
        with st.container(border=True):
            left = content_7_1["frequency_comparison"]["left"]
            st.markdown(f"**{t(left['title'])}**")
            st.markdown(f"*{t(left['intuition'])}*")
            st.latex(left["formula"])
            st.markdown("---")
            st.markdown(f"**{t({'de': 'Beispiel', 'en': 'Example'})}:** {t(left['example'])}")
    
    with c2:
        with st.container(border=True):
            right = content_7_1["frequency_comparison"]["right"]
            st.markdown(f"**{t(right['title'])}**")
            st.markdown(f"*{t(right['intuition'])}*")
            st.latex(right["formula"])
            st.markdown("---")
            st.markdown(f"**{t({'de': 'Beispiel', 'en': 'Example'})}:** {t(right['example'])}")
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # === 3. THEORY: Histogram Definition ===
    hist_def = content_7_1["histogram_def"]
    render_definition(
        term=hist_def["term"],
        formal=hist_def["formal"],
        plain=hist_def["plain"]
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # === 4. THEORY: ECDF ===
    ecdf = content_7_1["ecdf"]
    render_single_formula(
        title=ecdf["header"],
        intuition=ecdf["intuition"],
        formula=ecdf["formula"],
        variables=ecdf["variables"],
        insight=ecdf["insight"]
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # === 5. WORKED EXAMPLE ===
    we = content_7_1["worked_example"]
    render_worked_example(
        header=we["header"],
        problem=we["problem"],
        steps=we["steps"],
        answer=we["answer"]
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # === 6. INTERACTIVE: Distribution Matcher ===
    st.markdown(f"### {t({'de': 'Interaktiv: Verteilungs-Matcher', 'en': 'Interactive: Distribution Matcher'})}")
    with st.container(border=True):
        distribution_matcher()
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # === 7. FRAG DICH ===
    fd = content_7_1["frag_dich"]
    render_ask_yourself(
        header=fd["header"],
        questions=fd["questions"],
        conclusion=fd["conclusion"]
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # === 8. EXAM ESSENTIALS ===
    ee = content_7_1["exam_essentials"]
    render_exam_essentials(
        trap=ee["trap"],
        trap_rule=ee["trap_rule"],
        tips=ee["tips"]
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # === 9. MCQ PRACTICE ===
    st.markdown(f"### {t({'de': 'Prüfungstraining', 'en': 'Exam Practice'})}")
    
    # MCQ 1: hs2015_mc8
    st.caption("HS 2015, MC 8")
    q1 = get_question("7", "hs2015_mc8")
    if q1:
        with st.container(border=True):
            opts = q1.get("options", [])
            opt_labels = [t({"de": o["de"], "en": o["en"]}) for o in opts]
            render_mcq(
                key_suffix="7_1_mc8",
                question_text=t(q1["question"]),
                options=opt_labels,
                correct_idx=q1.get("correct_idx", 0),
                solution_text_dict=q1.get("solution", {}),
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Falsch.", "en": "Incorrect."},
                client=model,
                ai_context="Question about sample mean, variance, and median from 3 values",
                course_id="vwl",
                topic_id="7",
                subtopic_id="7.1",
                question_id="hs2015_mc8"
            )

