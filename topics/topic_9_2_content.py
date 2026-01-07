# Topic 9.2: Derivation of Confidence Intervals (Large Samples)
# ULTRATHINK Implementation - Maximum pedagogical clarity
# "From CLT to Formula — The Complete Recipe"

import streamlit as st
import numpy as np
import plotly.graph_objects as go
from utils.localization import t
from utils.quiz_helper import render_mcq
from utils.ask_yourself import render_ask_yourself
from utils.exam_essentials import render_exam_essentials
from utils.layouts import render_comparison, render_steps
from utils.layouts.foundation import inject_equal_height_css, grey_callout
from data.exam_questions import QUESTIONS_9

# ============================================================================
# CONTENT DICTIONARY - All bilingual content
# ============================================================================

content_9_2 = {
    "title": {
        "de": "9.2 Ableitung von Konfidenzintervallen",
        "en": "9.2 Derivation of Confidence Intervals"
    },
    "subtitle": {
        "de": "Vom ZGS zur Formel — Das komplette Rezept",
        "en": "From CLT to Formula — The Complete Recipe"
    },
    
    # THE RECIPE INTUITION
    "intuition": {
        "de": """Ein Wetterfrosch sagt: <strong>„30°C ± 2°C"</strong>. Aber woher kommt das <strong>± 2</strong>?

Es wird <strong>abgeleitet</strong> aus drei Zutaten:

<strong>1.</strong> Wie genau dein Thermometer ist (σ — Standardabweichung)
<strong>2.</strong> Wie viele Messungen du gemacht hast (n — Stichprobenumfang)
<strong>3.</strong> Wie sicher du sein willst (1-α — Konfidenzniveau)

Das Konfidenzintervall ist ein <strong>Rezept</strong>: Zutaten rein, Formel anwenden, Intervall raus!""",
        
        "en": """A weather forecaster says: <strong>"30°C ± 2°C"</strong>. But where does the <strong>± 2</strong> come from?

It's <strong>derived</strong> from three ingredients:

<strong>1.</strong> How accurate your thermometer is (σ — standard deviation)
<strong>2.</strong> How many readings you took (n — sample size)
<strong>3.</strong> How confident you want to be (1-α — confidence level)

The confidence interval is a <strong>recipe</strong>: ingredients in, formula applied, interval out!"""
    },
    
    # DERIVATION STEPS (using render_steps)
    "derivation_steps": {
        "title": {"de": "Die Herleitung in 4 Schritten", "en": "The Derivation in 4 Steps"},
        "steps": [
            {
                "action": {"de": "Starte mit dem ZGS", "en": "Start with the CLT"},
                "explanation": {
                    "de": "Das Stichprobenmittel ist approximativ normalverteilt. Die standardisierte Version folgt der Standardnormalverteilung.",
                    "en": "The sample mean is approximately normally distributed. The standardized version follows the standard normal distribution."
                },
                "formula": r"Z = \frac{\bar{X} - \mu}{\sigma / \sqrt{n}} \sim N(0,1)"
            },
            {
                "action": {"de": "Nutze die Quantilschranken", "en": "Use the quantile bounds"},
                "explanation": {
                    "de": "Mit Wahrscheinlichkeit (1-α) liegt Z zwischen den kritischen Werten.",
                    "en": "With probability (1-α), Z lies between the critical values."
                },
                "formula": r"P\left( -z_{1-\alpha/2} \leq Z \leq z_{1-\alpha/2} \right) = 1 - \alpha"
            },
            {
                "action": {"de": "Ersetze Z und löse nach μ", "en": "Substitute Z and solve for μ"},
                "explanation": {
                    "de": "Setze die Definition von Z ein und isoliere μ in der Mitte.",
                    "en": "Insert the definition of Z and isolate μ in the middle."
                },
                "formula": r"P\left( \bar{X} - z_{1-\alpha/2} \cdot \frac{\sigma}{\sqrt{n}} \leq \mu \leq \bar{X} + z_{1-\alpha/2} \cdot \frac{\sigma}{\sqrt{n}} \right) = 1-\alpha"
            },
            {
                "action": {"de": "DIE FORMEL!", "en": "THE FORMULA!"},
                "explanation": {
                    "de": "Das (1-α)-Konfidenzintervall für den Erwartungswert μ lautet:",
                    "en": "The (1-α)-confidence interval for the expected value μ is:"
                },
                "formula": r"\boxed{ \text{KI}_{1-\alpha} = \left[ \bar{X} - z_{1-\alpha/2} \cdot \frac{\sigma}{\sqrt{n}} \,;\, \bar{X} + z_{1-\alpha/2} \cdot \frac{\sigma}{\sqrt{n}} \right] }"
            }
        ]
    },
    
    # TWO CASES COMPARISON
    "comparison": {
        "title": {"de": "Zwei Fälle: σ bekannt vs. σ unbekannt", "en": "Two Cases: σ Known vs. σ Unknown"},
        "left": {
            "title": {"de": "Fall A: σ bekannt", "en": "Case A: σ Known"},
            "insight": {
                "de": """Verwende die <strong>wahre</strong> Standardabweichung σ.

<strong>Wann:</strong> σ ist in der Aufgabe gegeben.

<strong>Formel:</strong>""",
                "en": """Use the <strong>true</strong> standard deviation σ.

<strong>When:</strong> σ is given in the problem.

<strong>Formula:</strong>"""
            },
            "formula": r"\bar{X} \pm z_{1-\alpha/2} \cdot \frac{\sigma}{\sqrt{n}}"
        },
        "right": {
            "title": {"de": "Fall B: σ unbekannt", "en": "Case B: σ Unknown"},
            "insight": {
                "de": """Verwende die <strong>Stichproben</strong>-Standardabweichung Sₙ.

<strong>Wann:</strong> Nur Sₙ gegeben UND n ≥ 50 (grosse Stichprobe).

<strong>Formel:</strong>""",
                "en": """Use the <strong>sample</strong> standard deviation Sₙ.

<strong>When:</strong> Only Sₙ given AND n ≥ 50 (large sample).

<strong>Formula:</strong>"""
            },
            "formula": r"\bar{X} \pm z_{1-\alpha/2} \cdot \frac{S_n}{\sqrt{n}}"
        }
    },
    
    # KEY INSIGHT
    "key_insight": {
        "de": """<strong>Merke:</strong> Der einzige Unterschied ist σ vs. Sₙ. 
Bei <strong>grossen Stichproben</strong> (n ≥ 50) funktioniert Sₙ als gute Näherung für σ.""",
        "en": """<strong>Remember:</strong> The only difference is σ vs. Sₙ. 
For <strong>large samples</strong> (n ≥ 50), Sₙ works as a good approximation for σ."""
    },
    
    # INTERACTIVE SCENARIO
    "interactive": {
        "scenario": {
            "de": "Eine Gemeindeverwaltung befragt 50 Haushalte nach der Kaltmiete pro m². Ergebnis: Mittelwert = 8.30 CHF, Standardabweichung Sₙ = 2.07 CHF.",
            "en": "A municipality surveys 50 households about rent per m². Result: Mean = 8.30 CHF, Standard deviation Sₙ = 2.07 CHF."
        },
        "mission": {
            "de": "Berechne das Konfidenzintervall für verschiedene Konfidenzniveaus. Beobachte: Mehr Sicherheit = breiteres Intervall!",
            "en": "Calculate the confidence interval for different confidence levels. Observe: More confidence = wider interval!"
        }
    },
    
    # ASK YOURSELF
    "frag_dich": {
        "header": {"de": "Frag dich: Kannst du die Formeln anwenden?", "en": "Ask yourself: Can you apply the formulas?"},
        "questions": [
            {"de": "σ = 5 ist in der Aufgabe gegeben. Welchen Fall verwendest du?", 
             "en": "σ = 5 is given in the problem. Which case do you use?"},
            {"de": "Du hast n = 200 und nur Sₙ. Welche Formel?", 
             "en": "You have n = 200 and only Sₙ. Which formula?"},
            {"de": "z-Wert für 95% Konfidenz?", 
             "en": "z-value for 95% confidence?"},
            {"de": "Mehr Konfidenz (99% statt 95%) → breiteres oder schmaleres KI?", 
             "en": "More confidence (99% instead of 95%) → wider or narrower CI?"}
        ],
        "conclusion": {
            "de": "Antworten: Fall A (σ bekannt), Fall B (n ≥ 50), z = 1.96, Breiter!",
            "en": "Answers: Case A (σ known), Case B (n ≥ 50), z = 1.96, Wider!"
        }
    },
    
    # EXAM ESSENTIALS
    "exam_essentials": {
        "trap": {
            "de": "Vergessen von √n: Studierende berechnen x̄ ± z·σ und vergessen dabei √n im Nenner!",
            "en": "Forgetting √n: Students calculate x̄ ± z·σ and forget √n in the denominator!"
        },
        "trap_rule": {
            "de": "IMMER durch √n teilen! Das ist der Standardfehler. Ohne √n ist das Intervall viel zu breit.",
            "en": "ALWAYS divide by √n! That's the standard error. Without √n the interval is way too wide."
        },
        "tips": [
            {
                "tip": {"de": "Prüfe zuerst σ — es bestimmt die Formel!", "en": "Check σ first — it determines the formula!"},
                "why": {"de": "Sₙ verwenden wenn σ gegeben ist = falsche Formel!", "en": "Using Sₙ when σ is given = wrong formula!"}
            },
            {
                "tip": {"de": "z-Werte auswendig kennen", "en": "Memorize z-values"},
                "why": {"de": "Keine Zeit zum Nachschlagen in der Prüfung.", "en": "No time to look them up during exams."},
                "why_formula": r"90\%: z = 1.645, \quad 95\%: z = 1.96, \quad 99\%: z = 2.576"
            },
            {
                "tip": {"de": "Intervallbreite = 2·Fehler", "en": "Interval width = 2·error"},
                "why": {"de": "Das Intervall ist symmetrisch um x̄.", "en": "The interval is symmetric around x̄."},
                "why_formula": r"\text{Breite} = 2 \cdot z_{1-\alpha/2} \cdot \frac{\sigma}{\sqrt{n}}"
            }
        ]
    },
    
    # Z-VALUES TABLE
    "z_table": {
        "title": {"de": "Kritische z-Werte", "en": "Critical z-Values"},
        "values": [
            {"level": "90%", "alpha": "0.10", "z": "1.645"},
            {"level": "95%", "alpha": "0.05", "z": "1.960"},
            {"level": "99%", "alpha": "0.01", "z": "2.576"}
        ]
    }
}


# ============================================================================
# INTERACTIVE: CI Builder — Compact design with pill buttons
# ============================================================================

@st.fragment
def ci_builder():
    """Compact CI calculator with pill button selection."""
    
    # Fixed data (rent example from course)
    n = 50
    x_bar = 8.30
    s_n = 2.07
    
    # State for exploration tracking
    if "ci_explored_levels" not in st.session_state:
        st.session_state.ci_explored_levels = set()
    if "ci_selected_level" not in st.session_state:
        st.session_state.ci_selected_level = 95
    
    # Compact scenario + mission in one line
    st.markdown(f"""
<div style="background: #f4f4f5; border-left: 4px solid #a1a1aa; 
            padding: 10px 14px; border-radius: 8px; color: #3f3f46; font-size: 0.9em;">
<strong>{t({"de": "Szenario", "en": "Scenario"})}:</strong> 
{t({"de": "50 Haushalte befragt → Mittelwert = 8.30 CHF/m², Sₙ = 2.07 CHF", 
    "en": "50 households surveyed → Mean = 8.30 CHF/m², Sₙ = 2.07 CHF"})}
</div>
""", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Pill button CSS
    st.markdown("""
<style>
.ci-pill-container { display: flex; gap: 8px; margin-bottom: 16px; }
.ci-pill { 
    padding: 8px 20px; 
    border-radius: 20px; 
    border: 2px solid #007AFF; 
    background: white; 
    color: #007AFF; 
    font-weight: 600; 
    cursor: pointer;
    transition: all 0.2s ease;
}
.ci-pill:hover { background: rgba(0, 122, 255, 0.1); }
.ci-pill.active { background: #007AFF; color: white; }
</style>
""", unsafe_allow_html=True)
    
    # Pill buttons for confidence level
    st.markdown(f"**{t({'de': 'Konfidenzniveau wählen', 'en': 'Select Confidence Level'})}:**")
    
    conf_options = {90: 1.645, 95: 1.960, 99: 2.576}
    
    cols = st.columns(3)
    for i, (level, z) in enumerate(conf_options.items()):
        with cols[i]:
            btn_type = "primary" if st.session_state.ci_selected_level == level else "secondary"
            if st.button(f"{level}%", key=f"ci_btn_{level}", use_container_width=True, type=btn_type):
                st.session_state.ci_selected_level = level
                st.session_state.ci_explored_levels.add(level)
                st.rerun(scope="fragment")
    
    # Track current selection
    conf_level = st.session_state.ci_selected_level
    st.session_state.ci_explored_levels.add(conf_level)
    z_val = conf_options[conf_level]
    
    # Calculate CI
    std_error = s_n / np.sqrt(n)
    margin = z_val * std_error
    lower = x_bar - margin
    upper = x_bar + margin
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # COMPACT: Single container with calculation + visual
    with st.container(border=True):
        # Row 1: Formula + Result side by side
        c1, c2 = st.columns([1.5, 1])
        
        with c1:
            st.markdown(f"**{t({'de': 'Berechnung', 'en': 'Calculation'})}:**")
            st.latex(fr"z = {z_val:.3f}, \quad SE = \frac{{{s_n}}}{{\sqrt{{{n}}}}} = {std_error:.3f}")
        
        with c2:
            st.markdown(f"**{t({'de': 'Ergebnis', 'en': 'Result'})}:**")
            st.latex(fr"\boxed{{[{lower:.2f} \,;\, {upper:.2f}]}}")
        
        st.markdown("---")
        
        # Row 2: Compact number line visualization
        fig = go.Figure()
        
        # CI bar
        fig.add_shape(type="rect", x0=lower, x1=upper, y0=0.3, y1=0.7,
                      fillcolor="rgba(0, 122, 255, 0.3)", line=dict(color="#007AFF", width=2))
        
        # Center point
        fig.add_trace(go.Scatter(x=[x_bar], y=[0.5], mode="markers",
                                 marker=dict(color="#9B59B6", size=12, symbol="diamond"),
                                 hovertemplate=f"x̄ = {x_bar:.2f}<extra></extra>", showlegend=False))
        
        # Endpoints
        fig.add_trace(go.Scatter(x=[lower, upper], y=[0.5, 0.5], mode="markers",
                                 marker=dict(color="#007AFF", size=8),
                                 hovertemplate="%{x:.2f}<extra></extra>", showlegend=False))
        
        # Labels
        fig.add_annotation(x=lower, y=0.15, text=f"{lower:.2f}", showarrow=False, font=dict(size=11, color="#007AFF"))
        fig.add_annotation(x=x_bar, y=0.85, text=f"x̄={x_bar}", showarrow=False, font=dict(size=11, color="#9B59B6"))
        fig.add_annotation(x=upper, y=0.15, text=f"{upper:.2f}", showarrow=False, font=dict(size=11, color="#007AFF"))
        
        fig.update_layout(
            xaxis=dict(range=[6.5, 10.5], title=t({"de": "CHF/m²", "en": "CHF/m²"})),
            yaxis=dict(range=[0, 1], visible=False),
            height=120,
            margin=dict(l=10, r=10, t=10, b=30),
            hovermode=False
        )
        
        st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})
    
    # Compact discovery message
    if len(st.session_state.ci_explored_levels) >= 3:
        st.success(t({
            "de": "Mehr Konfidenz = breiteres Intervall. Präzision vs. Sicherheit!",
            "en": "More confidence = wider interval. Precision vs. confidence!"
        }))
    else:
        remaining = 3 - len(st.session_state.ci_explored_levels)
        st.caption(t({"de": f"Probiere noch {remaining} Niveau(s)!", "en": f"Try {remaining} more level(s)!"}))




# ============================================================================
# MAIN RENDER FUNCTION
# ============================================================================

def render_subtopic_9_2(model):
    """Render Topic 9.2: Derivation of Confidence Intervals for Large Samples"""
    
    # Title and subtitle
    st.header(t(content_9_2["title"]))
    st.markdown(f"*{t(content_9_2['subtitle'])}*")
    st.markdown("---")
    
    # Inject equal height CSS for later side-by-side containers
    inject_equal_height_css()
    
    # =========================================================================
    # SECTION 1: INTUITION (The Recipe Metaphor)
    # =========================================================================
    st.markdown(f"### {t({'de': 'Intuition', 'en': 'Intuition'})}")
    
    with st.container(border=True):
        st.markdown(t(content_9_2["intuition"]), unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # =========================================================================
    # SECTION 2: THE DERIVATION (4 Visual Steps)
    # =========================================================================
    st.markdown(f"### {t(content_9_2['derivation_steps']['title'])}")
    
    with st.container(border=True):
        for i, step in enumerate(content_9_2["derivation_steps"]["steps"]):
            if i > 0:
                st.markdown("---")
            
            step_num = i + 1
            st.markdown(f"**{t({'de': f'Schritt {step_num}', 'en': f'Step {step_num}'})}:** {t(step['action'])}")
            st.markdown(f"*{t(step['explanation'])}*")
            st.latex(step["formula"])
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # =========================================================================
    # SECTION 3: TWO CASES COMPARISON
    # =========================================================================
    st.markdown(f"### {t(content_9_2['comparison']['title'])}")
    
    col_left, col_right = st.columns(2, gap="medium")
    
    with col_left:
        with st.container(border=True):
            st.markdown(f"**{t(content_9_2['comparison']['left']['title'])}**")
            st.markdown(t(content_9_2['comparison']['left']['insight']), unsafe_allow_html=True)
            st.latex(content_9_2['comparison']['left']['formula'])
    
    with col_right:
        with st.container(border=True):
            st.markdown(f"**{t(content_9_2['comparison']['right']['title'])}**")
            st.markdown(t(content_9_2['comparison']['right']['insight']), unsafe_allow_html=True)
            st.latex(content_9_2['comparison']['right']['formula'])
    
    # Key insight below comparison
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"""
<div style="background: #f4f4f5; border-left: 4px solid #a1a1aa; 
            padding: 12px 16px; border-radius: 8px; color: #3f3f46;">
{t(content_9_2["key_insight"])}
</div>
""", unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # =========================================================================
    # SECTION 4: Z-VALUES REFERENCE TABLE
    # =========================================================================
    st.markdown(f"### {t(content_9_2['z_table']['title'])}")
    
    with st.container(border=True):
        # Create simple table
        st.markdown(f"""
| {t({"de": "Konfidenzniveau", "en": "Confidence Level"})} | α | z |
|:---:|:---:|:---:|
| 90% | 0.10 | **1.645** |
| 95% | 0.05 | **1.960** |
| 99% | 0.01 | **2.576** |
""")
        st.markdown("")  # Spacer to prevent cutoff
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # =========================================================================
    # SECTION 5: INTERACTIVE CI BUILDER
    # =========================================================================
    st.markdown(f"### {t({'de': 'Interaktiv: KI-Rechner', 'en': 'Interactive: CI Calculator'})}")
    
    ci_builder()
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # =========================================================================
    # SECTION 6: ASK YOURSELF
    # =========================================================================
    render_ask_yourself(
        header=content_9_2["frag_dich"]["header"],
        questions=content_9_2["frag_dich"]["questions"],
        conclusion=content_9_2["frag_dich"]["conclusion"]
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # =========================================================================
    # SECTION 7: EXAM ESSENTIALS
    # =========================================================================
    render_exam_essentials(
        trap=content_9_2["exam_essentials"]["trap"],
        trap_rule=content_9_2["exam_essentials"]["trap_rule"],
        tips=content_9_2["exam_essentials"]["tips"]
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # =========================================================================
    # SECTION 8: MCQ (hs2023_mc5)
    # =========================================================================
    st.markdown(f"### {t({'de': 'Prüfungstraining', 'en': 'Exam Practice'})}")
    
    q1 = QUESTIONS_9.get("hs2023_mc5")
    if q1:
        st.caption(q1.get("source", ""))
        
        opts = q1.get("options", [])
        option_labels = []
        for o in opts:
            if isinstance(o, dict):
                option_labels.append(t({"de": o.get("de", ""), "en": o.get("en", "")}))
            else:
                option_labels.append(o)
        
        render_mcq(
            key_suffix="9_2_ci_calc",
            question_text=t(q1["question"]),
            options=option_labels,
            correct_idx=q1["correct_idx"],
            solution_text_dict=q1["solution"],
            success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
            error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
            client=model,
            ai_context="Confidence interval calculation for mean fill amount with known variance. Tests application of the CI formula derived in this section.",
            course_id="vwl",
            topic_id="9",
            subtopic_id="9.2",
            question_id="9_2_ci_calc"
        )
