# Topic 9.1: Concept of the Confidence Interval
# ULTRATHINK Implementation - Maximum pedagogical clarity

import streamlit as st
import numpy as np
import plotly.graph_objects as go
from utils.localization import t
from utils.quiz_helper import render_mcq
from utils.ask_yourself import render_ask_yourself
from utils.exam_essentials import render_exam_essentials
from utils.worked_example import render_worked_example
from utils.layouts import render_comparison, render_single_formula, render_definition
from utils.layouts.foundation import inject_equal_height_css
from data.exam_questions import QUESTIONS_9_4

# ============================================================================
# CONTENT DICTIONARY - All bilingual content
# ============================================================================

content_9_1 = {
    "title": {
        "de": "9.1 Konzept des Konfidenzintervalls",
        "en": "9.1 Concept of the Confidence Interval"
    },
    "subtitle": {
        "de": "Vom Punktschätzer zum Intervall — Unsicherheit quantifizieren",
        "en": "From Point Estimate to Interval — Quantifying Uncertainty"
    },
    
    # THE BIG PICTURE - Fishing with a Net
    "intuition": {
        "de": """Stell dir vor, du fischst in einem See, aber du <strong>kannst den Fisch nicht sehen</strong>. 
Du wirfst dein Netz dort, wo dein Sonar dir sagt, dass die Fische sind.

<strong>Das Problem:</strong> Jedes Mal, wenn du das Sonar benutzt (eine Stichprobe nimmst), 
zeigt es einen leicht anderen Standort. Dein Netz (Konfidenzintervall) ist der Bereich, den du basierend auf dieser Messung abdeckst.

<strong>Die 95%-Regel:</strong> Wenn du 100 Mal wirfst mit verschiedenen Sonar-Messungen, 
fängt dein Netz den Fisch in etwa <strong>95 Fällen</strong>.

<strong>Wichtig:</strong> Der Fisch (der wahre Parameter) bewegt sich nie — er ist FEST. 
Dein Netz (das Intervall) variiert mit jeder Messung — es ist ZUFÄLLIG.""",
        
        "en": """Imagine you're fishing in a lake, but you <strong>can't see the fish</strong>. 
You cast your net where your sonar tells you the fish might be.

<strong>The problem:</strong> Each time you use the sonar (take a sample), 
it shows a slightly different location. Your net (confidence interval) is the area you cover based on that reading.

<strong>The 95% rule:</strong> If you cast 100 times using different sonar readings, 
your net catches the fish in about <strong>95 cases</strong>.

<strong>Key point:</strong> The fish (true parameter) never moves — it's FIXED. 
Your net (the interval) varies with each reading — it's RANDOM."""
    },
    
    # COMPARISON: Point vs Interval
    "comparison": {
        "left": {
            "title": {"de": "Punktschätzung", "en": "Point Estimation"},
            "content": {
                "de": """<strong>Beispiel:</strong> θ̂ = 100

"Eine einzige Zahl als Schätzung"

<span style="color: #FF4B4B;"><strong>Riskant:</strong></span> Was, wenn wir daneben liegen?
Keine Information über Unsicherheit.""",
                "en": """<strong>Example:</strong> θ̂ = 100

"One single number as estimate"

<span style="color: #FF4B4B;"><strong>Risky:</strong></span> What if we're wrong?
No information about uncertainty."""
            }
        },
        "right": {
            "title": {"de": "Intervallschätzung", "en": "Interval Estimation"},
            "content": {
                "de": """<strong>Beispiel:</strong> θ ∈ [95, 105]

"Ein Bereich möglicher Werte"

<span style="color: #16a34a;"><strong>Sicher:</strong></span> Deckt den wahren Wert ab!
Zeigt genau, wie unsicher wir sind.""",
                "en": """<strong>Example:</strong> θ ∈ [95, 105]

"A range of possible values"

<span style="color: #16a34a;"><strong>Safe:</strong></span> Covers the true value!
Shows exactly how uncertain we are."""
            }
        }
    },
    
    # THE CI FORMULA
    "formula": {
        "title": {"de": "Das symmetrische Konfidenzintervall", "en": "The Symmetric Confidence Interval"},
        "intuition": {
            "de": "Ein Intervall um den Schätzer, das den wahren Parameter mit Wahrscheinlichkeit (1-α) enthält.",
            "en": "An interval around the estimator that contains the true parameter with probability (1-α)."
        },
        "formula": r"\text{KI}_{1-\alpha} = \left[\hat{\theta} - f_n \,;\, \hat{\theta} + f_n\right]",
        "variables": [
            {"symbol": r"\hat{\theta}", "name": {"de": "Punktschätzer", "en": "Point Estimate"}, 
             "desc": {"de": "Dein bester Einzelwert aus der Stichprobe", "en": "Your best single-value guess from the sample"}},
            {"symbol": r"f_n", "name": {"de": "Stichprobenfehler", "en": "Sampling Error"}, 
             "desc": {"de": "Wie weit du daneben liegen könntest (Margin of Error)", "en": "How far off you might be (margin of error)"}},
            {"symbol": r"1-\alpha", "name": {"de": "Konfidenzniveau", "en": "Confidence Level"}, 
             "desc": {"de": "Wie oft das Intervall θ enthält (z.B. 95% = 0.95)", "en": "How often the interval catches θ (e.g., 95% = 0.95)"}},
            {"symbol": r"\theta", "name": {"de": "Wahrer Parameter", "en": "True Parameter"}, 
             "desc": {"de": "Der unbekannte Wert, den wir schätzen wollen", "en": "The unknown value we want to estimate"}}
        ],
        "insight": {
            "de": "Der Schlüssel: Das Intervall ist <strong>zufällig</strong> (hängt von der Stichprobe ab). Der Parameter ist <strong>fest</strong> (ändert sich nie). Nicht umgekehrt!",
            "en": "The key: The interval is <strong>random</strong> (depends on the sample). The parameter is <strong>fixed</strong> (never changes). Not the other way around!"
        }
    },
    
    # FORMAL DEFINITION
    "definition": {
        "term": {"de": "Konfidenzintervall", "en": "Confidence Interval"},
        "definition": {
            "de": "Ein (1-α)-Konfidenzintervall ist ein Intervall [θ̂ - fₙ, θ̂ + fₙ], so dass der wahre Parameter θ mit Wahrscheinlichkeit (1-α) darin liegt.",
            "en": "A (1-α)-confidence interval is an interval [θ̂ - fₙ, θ̂ + fₙ] such that the true parameter θ lies within it with probability (1-α)."
        },
        "formula": r"P\left(\theta \in \text{KI}_{1-\alpha}\right) = 1 - \alpha",
        "examples": [
            {"de": "95%-Konfidenzniveau: 1-α = 0.95", "en": "95% confidence level: 1-α = 0.95"},
            {"de": "99%-Konfidenzniveau: 1-α = 0.99", "en": "99% confidence level: 1-α = 0.99"}
        ]
    },
    
    # WORKED EXAMPLE
    "worked_example": {
        "header": {"de": "Rechenbeispiel: 95%-Konfidenzintervall", "en": "Worked Example: 95% Confidence Interval"},
        "problem": {
            "de": "Eine Stichprobe von n=300 Messungen hat Mittelwert x̄=50. Die Standardabweichung ist σ=5. Berechne das 95%-Konfidenzintervall.",
            "en": "A sample of n=300 measurements has mean x̄=50. The standard deviation is σ=5. Calculate the 95% confidence interval."
        },
        "steps": [
            {
                "label": {"de": "Gegeben", "en": "Given"},
                "latex": r"n = {\color{#007AFF}300}, \quad {\color{#9B59B6}\bar{x} = 50}, \quad \sigma = 5, \quad z_{0.975} = 1.96",
                "note": {"de": "Stichprobendaten und kritischer Wert", "en": "Sample data and critical value"}
            },
            {
                "label": {"de": "Formel", "en": "Formula"},
                "latex": r"\text{KI} = \bar{x} \pm z \cdot \frac{\sigma}{\sqrt{n}}",
                "note": {"de": "Standardformel für KI bei bekanntem σ", "en": "Standard CI formula for known σ"}
            },
            {
                "label": {"de": "Berechnung", "en": "Calculate"},
                "latex": r"f_n = 1.96 \cdot \frac{5}{\sqrt{{\color{#007AFF}300}}} = 1.96 \cdot 0.289 = {\color{#FF4B4B}0.57}",
                "note": {"de": "Stichprobenfehler berechnen", "en": "Calculate sampling error"}
            },
            {
                "label": {"de": "Ergebnis", "en": "Result"},
                "latex": r"\text{KI}_{95\%} = [{\color{#9B59B6}50} - {\color{#FF4B4B}0.57} \,;\, {\color{#9B59B6}50} + {\color{#FF4B4B}0.57}] = {\color{#16a34a}[49.43 \,;\, 50.57]}",
                "note": {"de": "Mit 95% Sicherheit liegt μ in diesem Intervall", "en": "With 95% confidence, μ lies in this interval"}
            }
        ],
        "answer": {
            "de": "Das 95%-Konfidenzintervall ist [49.43; 50.57]",
            "en": "The 95% confidence interval is [49.43; 50.57]"
        }
    },
    
    # ASK YOURSELF
    "frag_dich": {
        "header": {"de": "Frag dich: Verstehst du Konfidenzintervalle?", "en": "Ask yourself: Do you understand confidence intervals?"},
        "questions": [
            {"de": "Was bedeutet '95% Konfidenzniveau' wirklich?", 
             "en": "What does '95% confidence level' really mean?"},
            {"de": "Was ist zufällig — das Intervall oder der Parameter?", 
             "en": "What is random — the interval or the parameter?"},
            {"de": "Wird das Intervall breiter oder schmaler bei mehr Stichproben?", 
             "en": "Does the interval get wider or narrower with more samples?"},
            {"de": "Was passiert, wenn du 99% statt 95% Konfidenz willst?", 
             "en": "What happens if you want 99% instead of 95% confidence?"}
        ],
        "conclusion": {
            "de": "Alle beantwortet? Dann verstehst du das Konzept!",
            "en": "All answered? Then you understand the concept!"
        }
    },
    
    # EXAM ESSENTIALS
    "exam_essentials": {
        "trap": {
            "de": "Falsche Interpretation: 'Es gibt eine 95% Chance, dass θ im Intervall liegt.'",
            "en": "Wrong interpretation: 'There's a 95% chance that θ is in the interval.'"
        },
        "trap_rule": {
            "de": "θ ist FEST — entweder es liegt drin oder nicht. Die 95% beziehen sich auf die METHODE: 95% aller möglichen Konfidenzintervalle würden θ enthalten.",
            "en": "θ is FIXED — it's either in or not. The 95% refers to the METHOD: 95% of all possible confidence intervals would contain θ."
        },
        "tips": [
            {
                "tip": {"de": "Mehr Sicherheit = breiteres Netz", "en": "More confidence = wider net"},
                "why": {"de": "99% KI ist breiter als 95% KI. Mehr Sicherheit braucht mehr Spielraum.", "en": "99% CI is wider than 95% CI. More confidence needs more margin."}
            },
            {
                "tip": {"de": "Mehr Stichproben = schmaleres Intervall", "en": "More samples = narrower interval"},
                "why": {"de": "Der Stichprobenfehler schrumpft mit der Wurzel von n.", "en": "The sampling error shrinks with the square root of n."},
                "why_formula": r"f_n \propto \frac{1}{\sqrt{n}}"
            },
            {
                "tip": {"de": "Intervall = Schätzer ± Fehler", "en": "Interval = Estimate ± Error"},
                "why": {"de": "Jedes KI hat dieselbe Struktur: Mitte plus/minus Rand.", "en": "Every CI has the same structure: center plus/minus margin."}
            }
        ]
    }
}


# ============================================================================
# INTERACTIVE: CI CATCHER (Catch the Fish with Your Net)
# ============================================================================

@st.fragment
def ci_catcher():
    """Interactive visualization of CI 'catching' the true parameter."""
    
    # Initialize state
    if "ci_samples" not in st.session_state:
        st.session_state.ci_samples = []
        st.session_state.ci_hits = 0
    
    true_mu = 20.0  # True temperature (fixed, unknown to "researcher")
    sigma = 4.0
    n = 25
    z = 1.96  # 95% CI
    
    # Scenario box - grey callout
    st.markdown(f"""
<div style="background: #f4f4f5; border-left: 4px solid #a1a1aa; 
            padding: 12px 16px; border-radius: 8px; color: #3f3f46;">
<strong>{t({"de": "Szenario", "en": "Scenario"})}:</strong> {t({"de": "Du misst die Wassertemperatur eines Sees. Die wahre Temperatur ist 20°C (du weisst es aber nicht). Jede Stichprobe gibt dir ein anderes Konfidenzintervall.", "en": "You're measuring a lake's water temperature. The true temp is 20°C (but you don't know). Each sample gives you a different confidence interval."})}
</div>
""", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown(f"**{t({'de': 'Mission', 'en': 'Mission'})}:** {t({'de': 'Nimm Stichproben und beobachte, wie oft dein 95%-Intervall den wahren Wert fängt.', 'en': 'Take samples and observe how often your 95% interval catches the true value.'})}")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Buttons
    b1, b2, b3 = st.columns(3)
    with b1:
        sample_btn = st.button(t({"de": "Stichprobe nehmen", "en": "Take Sample"}), key="ci_sample", use_container_width=True, type="primary")
    with b2:
        can_sim = len(st.session_state.ci_samples) >= 3
        sim_btn = st.button(t({"de": "20x Simulieren", "en": "Simulate 20x"}), key="ci_sim", use_container_width=True, disabled=not can_sim)
        if not can_sim and len(st.session_state.ci_samples) > 0:
            remaining = 3 - len(st.session_state.ci_samples)
            sample_word = "Stichprobe" if remaining == 1 else "Stichproben"
            sample_word_en = "sample" if remaining == 1 else "samples"
            st.caption(t({"de": f"Noch {remaining} {sample_word}", "en": f"{remaining} more {sample_word_en}"}))
    with b3:
        reset_btn = st.button(t({"de": "Reset", "en": "Reset"}), key="ci_reset", use_container_width=True)
    
    # Handle actions
    if reset_btn:
        st.session_state.ci_samples = []
        st.session_state.ci_hits = 0
        st.rerun(scope="fragment")
    
    if sample_btn:
        sample = np.random.normal(true_mu, sigma, n)
        x_bar = np.mean(sample)
        margin = z * (sigma / np.sqrt(n))
        lower, upper = x_bar - margin, x_bar + margin
        hit = lower <= true_mu <= upper
        st.session_state.ci_samples.append({"lower": lower, "upper": upper, "center": x_bar, "hit": hit})
        if hit:
            st.session_state.ci_hits += 1
        st.rerun(scope="fragment")
    
    if sim_btn and can_sim:
        for _ in range(20):
            sample = np.random.normal(true_mu, sigma, n)
            x_bar = np.mean(sample)
            margin = z * (sigma / np.sqrt(n))
            lower, upper = x_bar - margin, x_bar + margin
            hit = lower <= true_mu <= upper
            st.session_state.ci_samples.append({"lower": lower, "upper": upper, "center": x_bar, "hit": hit})
            if hit:
                st.session_state.ci_hits += 1
        st.rerun(scope="fragment")
    
    # Results display
    if len(st.session_state.ci_samples) > 0:
        total = len(st.session_state.ci_samples)
        hits = st.session_state.ci_hits
        
        # Metrics
        m1, m2, m3 = st.columns(3)
        with m1:
            st.metric(t({"de": "Stichproben", "en": "Samples"}), total)
        with m2:
            st.metric(t({"de": "Treffer", "en": "Hits"}), f"{hits} ({(hits/total)*100:.0f}%)")
        with m3:
            st.metric(t({"de": "Ziel", "en": "Target"}), "95%")
    
    # Chart - show CIs as horizontal lines
    fig = go.Figure()
    
    # Draw true parameter line (vertical)
    fig.add_shape(type="line", x0=true_mu, x1=true_mu, y0=0, y1=max(20, len(st.session_state.ci_samples) + 1),
                  line=dict(color="#6B7280", width=2, dash="dash"))
    fig.add_annotation(x=true_mu, y=-0.5, text=f"θ = {true_mu}°C", showarrow=False, font=dict(size=12, color="#6B7280"))
    
    # Draw each CI as a horizontal line
    for i, ci in enumerate(st.session_state.ci_samples[-20:]):  # Show last 20
        y_pos = i + 1
        color = "#007AFF" if ci["hit"] else "#FF4B4B"
        fig.add_shape(type="line", x0=ci["lower"], x1=ci["upper"], y0=y_pos, y1=y_pos,
                      line=dict(color=color, width=3))
        # Endpoints
        fig.add_trace(go.Scatter(x=[ci["lower"], ci["upper"]], y=[y_pos, y_pos],
                                 mode="markers", marker=dict(color=color, size=8),
                                 showlegend=False, hoverinfo="skip"))
    
    fig.update_layout(
        title=t({"de": "Konfidenzintervalle (Blau = Treffer, Rot = Daneben)", "en": "Confidence Intervals (Blue = Hit, Red = Miss)"}),
        xaxis_title=t({"de": "Temperatur (°C)", "en": "Temperature (°C)"}),
        yaxis_title=t({"de": "Stichprobe #", "en": "Sample #"}),
        xaxis=dict(range=[10, 30]),
        yaxis=dict(range=[0, max(21, len(st.session_state.ci_samples) + 1)]),
        height=300,
        margin=dict(l=40, r=20, t=40, b=40),
        hovermode=False
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Discovery insight
    if len(st.session_state.ci_samples) >= 10:
        hit_rate = (st.session_state.ci_hits / len(st.session_state.ci_samples)) * 100
        with st.container(border=True):
            st.markdown(f"**{t({'de': 'Entdeckung', 'en': 'Discovery'})}:** {t({'de': f'Nach {len(st.session_state.ci_samples)} Stichproben hast du eine Trefferquote von {hit_rate:.0f}%.', 'en': f'After {len(st.session_state.ci_samples)} samples, your hit rate is {hit_rate:.0f}%.'})}")
            st.markdown(t({
                "de": "**Aha-Moment:** Bei genügend Stichproben nähert sich die Trefferquote 95%! Das ist die Bedeutung von '95% Konfidenzniveau' — nicht die Wahrscheinlichkeit für DIESES Intervall, sondern für die METHODE.",
                "en": "**Aha moment:** With enough samples, the hit rate approaches 95%! That's what '95% confidence level' means — not the probability for THIS interval, but for the METHOD."
            }))


# ============================================================================
# MAIN RENDER FUNCTION
# ============================================================================

def render_subtopic_9_1(model):
    """Render Topic 9.1: Concept of the Confidence Interval"""
    
    # Title and subtitle
    st.header(t(content_9_1["title"]))
    st.markdown(f"*{t(content_9_1['subtitle'])}*")
    st.markdown("---")
    
    # Inject equal height CSS
    inject_equal_height_css()
    
    # =========================================================================
    # SECTION 1: INTUITION (Fishing with a Net)
    # =========================================================================
    st.markdown(f"### {t({'de': 'Intuition', 'en': 'Intuition'})}")
    
    with st.container(border=True):
        st.markdown(t(content_9_1["intuition"]), unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # =========================================================================
    # SECTION 2: POINT VS INTERVAL COMPARISON
    # =========================================================================
    st.markdown(f"### {t({'de': 'Punkt- vs. Intervallschätzung', 'en': 'Point vs. Interval Estimation'})}")
    
    # Inject equal height CSS
    inject_equal_height_css()
    
    # Side-by-side columns with containers inside
    col_left, col_right = st.columns(2, gap="medium")
    
    with col_left:
        with st.container(border=True):
            st.markdown(f"**{t(content_9_1['comparison']['left']['title'])}**")
            st.markdown(t(content_9_1['comparison']['left']['content']), unsafe_allow_html=True)
    
    with col_right:
        with st.container(border=True):
            st.markdown(f"**{t(content_9_1['comparison']['right']['title'])}**")
            st.markdown(t(content_9_1['comparison']['right']['content']), unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # =========================================================================
    # SECTION 3: THE CI FORMULA
    # =========================================================================
    st.markdown(f"### {t(content_9_1['formula']['title'])}")
    
    with st.container(border=True):
        # Intuition (italic)
        st.markdown(f"*{t(content_9_1['formula']['intuition'])}*")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Formula
        st.latex(content_9_1["formula"]["formula"])
        
        st.markdown("---")
        
        # Variable Decoder
        st.markdown(f"**{t({'de': 'Variablen-Decoder', 'en': 'Variable Decoder'})}:**")
        for v in content_9_1["formula"]["variables"]:
            st.markdown(f"${v['symbol']}$ = **{t(v['name'])}** — {t(v['desc'])}")
        
        st.markdown("---")
        
        # Key Insight
        st.markdown(f"*{t(content_9_1['formula']['insight'])}*", unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    st.markdown(f"### {t({'de': 'Definition', 'en': 'Definition'})}")
    
    with st.container(border=True):
        # Term (bold)
        st.markdown(f"**{t(content_9_1['definition']['term'])}**")
        
        # Formal definition (italic)
        st.markdown(f"*{t(content_9_1['definition']['definition'])}*")
        
        # Formula
        st.latex(content_9_1["definition"]["formula"])
        
        st.markdown("---")
        
        # Examples
        st.markdown(f"**{t({'de': 'Typische Konfidenzniveaus', 'en': 'Typical Confidence Levels'})}:**")
        for ex in content_9_1["definition"]["examples"]:
            st.markdown(f"- {t(ex)}")
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # =========================================================================
    # SECTION 5: WORKED EXAMPLE
    # =========================================================================
    render_worked_example(
        header=content_9_1["worked_example"]["header"],
        problem=content_9_1["worked_example"]["problem"],
        steps=content_9_1["worked_example"]["steps"],
        answer=content_9_1["worked_example"]["answer"]
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # =========================================================================
    # SECTION 6: INTERACTIVE - CI CATCHER
    # =========================================================================
    st.markdown(f"### {t({'de': 'Interaktiv: Konfidenzintervall-Fänger', 'en': 'Interactive: CI Catcher'})}")
    
    ci_catcher()
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # =========================================================================
    # SECTION 7: ASK YOURSELF
    # =========================================================================
    render_ask_yourself(
        header=content_9_1["frag_dich"]["header"],
        questions=content_9_1["frag_dich"]["questions"],
        conclusion=content_9_1["frag_dich"]["conclusion"]
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # =========================================================================
    # SECTION 8: EXAM ESSENTIALS
    # =========================================================================
    render_exam_essentials(
        trap=content_9_1["exam_essentials"]["trap"],
        trap_rule=content_9_1["exam_essentials"]["trap_rule"],
        tips=content_9_1["exam_essentials"]["tips"]
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # =========================================================================
    # SECTION 9: MCQs
    # =========================================================================
    st.markdown(f"### {t({'de': 'Prüfungstraining', 'en': 'Exam Practice'})}")
    
    # MCQ 1: Confidence level vs width
    q1 = QUESTIONS_9_4.get("uebung5_mc16")
    if q1:
        st.caption(f"Source: {q1.get('source', 'Unknown')}")
        
        options1 = q1.get("options", [])
        option_labels1 = [t({"de": o["de"], "en": o["en"]}) if isinstance(o, dict) else o for o in options1]
        
        render_mcq(
            key_suffix="9_1_mc1",
            question_text=t(q1["question"]),
            options=option_labels1,
            correct_idx=q1["correct_idx"],
            solution_text_dict=q1["solution"],
            success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
            error_msg_dict={"de": "Falsch.", "en": "Incorrect."},
            client=model,
            ai_context="Question about the relationship between confidence level and interval width.",
            course_id="vwl",
            topic_id="9",
            subtopic_id="9.1",
            question_id="9_1_mc1"
        )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # MCQ 2: CI boundaries are random
    q2 = QUESTIONS_9_4.get("uebung5_mc17")
    if q2:
        st.caption(f"Source: {q2.get('source', 'Unknown')}")
        
        options2 = q2.get("options", [])
        option_labels2 = [t({"de": o["de"], "en": o["en"]}) if isinstance(o, dict) else o for o in options2]
        
        render_mcq(
            key_suffix="9_1_mc2",
            question_text=t(q2["question"]),
            options=option_labels2,
            correct_idx=q2["correct_idx"],
            solution_text_dict=q2["solution"],
            success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
            error_msg_dict={"de": "Falsch.", "en": "Incorrect."},
            client=model,
            ai_context="Question about whether CI boundaries are random or fixed.",
            course_id="vwl",
            topic_id="9",
            subtopic_id="9.1",
            question_id="9_1_mc2"
        )
