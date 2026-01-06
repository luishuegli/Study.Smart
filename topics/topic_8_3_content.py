# Topic 8.3: Methods for Constructing Estimating Functions
# "Two Detectives, Two Methods — Same Mystery"
# Maximum clarity approach with semantic color connections

import streamlit as st
import numpy as np
from utils.localization import t
from utils.quiz_helper import render_mcq
from utils.ask_yourself import render_ask_yourself
from utils.exam_essentials import render_exam_essentials
from utils.worked_example import render_worked_example
from utils.layouts import (
    render_comparison,
    render_steps,
    render_formula_breakdown,
    render_decision_tree,
)
from utils.layouts.foundation import (
    grey_callout,
    key_insight,
    inject_equal_height_css,
)
from data.exam_questions import QUESTIONS_8

# =============================================================================
# CONTENT DICTIONARY (Bilingual)
# =============================================================================

content_8_3 = {
    "title": {
        "de": "8.3 Methoden zur Konstruktion von Schätzfunktionen",
        "en": "8.3 Methods for Constructing Estimators"
    },
    "subtitle": {
        "de": "Zwei Methoden, ein Ziel — den Parameter finden",
        "en": "Two Methods, One Goal — Find the Parameter"
    },
    
    # INTUITION
    "intuition": {
        "de": """Du möchtest die <strong>Temperatur eines Sees</strong> schätzen. Du hast gemessen — aber <em>wie</em> verwandelst du diese Messungen in eine Schätzung?

Es gibt <strong>Rezepte</strong> dafür! Genau wie es verschiedene Wege gibt, einen Kuchen zu backen, gibt es verschiedene Methoden, einen Schätzer zu konstruieren.

<strong>Die zwei wichtigsten Methoden:</strong>
<br>• <strong>Momentenmethode (MOM)</strong> — Setze Stichprobenmittel = theoretisches Mittel
<br>• <strong>Maximum-Likelihood (MLE)</strong> — Finde den Wert, der deine Daten am wahrscheinlichsten macht""",
        "en": """You want to estimate the <strong>temperature of a lake</strong>. You've measured — but <em>how</em> do you turn those measurements into an estimate?

There are <strong>recipes</strong> for this! Just like there are different ways to bake a cake, there are different methods to construct an estimator.

<strong>The two key methods:</strong>
<br>• <strong>Method of Moments (MOM)</strong> — Set sample mean = theoretical mean
<br>• <strong>Maximum Likelihood (MLE)</strong> — Find the value that makes your data most likely"""
    },
    
    # COMPARISON DATA
    "comparison": {
        "header": {"de": "Die zwei Methoden im Vergleich", "en": "The Two Methods Compared"},
        "left": {
            "title": {"de": "Momentenmethode (MOM)", "en": "Method of Moments (MOM)"},
            "insight": {
                "de": "Setze das, was du siehst, gleich dem, was du erwartest. Löse nach dem Parameter auf.",
                "en": "Set what you observe equal to what you expect. Solve for the parameter."
            }
        },
        "right": {
            "title": {"de": "Maximum-Likelihood (MLE)", "en": "Maximum Likelihood (MLE)"},
            "insight": {
                "de": "Finde den Parameterwert, der deine beobachteten Daten am wahrscheinlichsten macht.",
                "en": "Find the parameter value that makes your observed data most probable."
            }
        }
    },
    
    # MOM STEPS
    "mom_steps": {
        "header": {"de": "Momentenmethode — Schritt für Schritt", "en": "Method of Moments — Step by Step"},
        "steps": [
            {
                "action": {"de": "Erwartungswert aufschreiben", "en": "Write the expected value"},
                "explanation": {"de": "Schreibe E[X] als Funktion des Parameters θ", "en": "Write E[X] as a function of parameter θ"},
                "formula": r"E[X] = g(\theta)"
            },
            {
                "action": {"de": "Mit Stichprobenmittel gleichsetzen", "en": "Set equal to sample mean"},
                "explanation": {"de": "Ersetze E[X] durch das Stichprobenmittel", "en": "Replace E[X] with the sample mean"},
                "formula": r"\bar{X} = g(\theta)"
            },
            {
                "action": {"de": "Nach θ auflösen", "en": "Solve for θ"},
                "explanation": {"de": "Löse die Gleichung nach θ auf", "en": "Solve the equation for θ"},
                "formula": r"\hat{\theta}_{MOM} = g^{-1}(\bar{X})"
            }
        ]
    },
    
    # MOM WORKED EXAMPLE
    "mom_example": {
        "header": {"de": "Beispiel: Poisson-Verteilung", "en": "Example: Poisson Distribution"},
        "problem": {
            "de": "Stichprobe aus Poisson(λ): Werte 2, 1, 4, 3, 5. Schätze λ mit der Momentenmethode.",
            "en": "Sample from Poisson(λ): Values 2, 1, 4, 3, 5. Estimate λ using Method of Moments."
        },
        "steps": [
            {
                "label": {"de": "Gegeben", "en": "Given"},
                "latex": r"X \sim \text{Poisson}({\color{#6B7280}\lambda}), \quad n = {\color{#007AFF}5}",
                "note": {"de": "Parameter λ unbekannt", "en": "Parameter λ unknown"}
            },
            {
                "label": {"de": "Erwartungswert", "en": "Expected value"},
                "latex": r"E[X] = {\color{#6B7280}\lambda}",
                "note": {"de": "Aus der Poisson-Formel", "en": "From Poisson formula"}
            },
            {
                "label": {"de": "Stichprobenmittel berechnen", "en": "Calculate sample mean"},
                "latex": r"\bar{X} = \frac{2+1+4+3+5}{{\color{#007AFF}5}} = {\color{#9B59B6}3}",
                "note": {"de": "Summe durch n", "en": "Sum divided by n"}
            },
            {
                "label": {"de": "Gleichsetzen und lösen", "en": "Set equal and solve"},
                "latex": r"\bar{X} = \lambda \implies \hat{\lambda}_{MOM} = {\color{#16a34a}3}",
                "note": None
            }
        ],
        "answer": {
            "de": "Der Momentenschätzer für λ ist 3",
            "en": "The MOM estimator for λ is 3"
        }
    },
    
    # MLE INTUITION
    "mle_intuition": {
        "de": """Stell dir vor, du hast eine Münze 10 Mal geworfen und 7 Mal Kopf bekommen. 

<strong>Welcher Wert für p (Kopf-Wahrscheinlichkeit) macht dieses Ergebnis am wahrscheinlichsten?</strong>

Intuitiv: p = 0.7! Denn bei p = 0.5 wäre 7/10 unwahrscheinlicher.

<strong>Das ist die Idee der Maximum-Likelihood:</strong> Finde den Parameter, der deine beobachteten Daten am plausibelsten macht.""",
        "en": """Imagine you flipped a coin 10 times and got 7 heads.

<strong>Which value of p (probability of heads) makes this result most likely?</strong>

Intuitively: p = 0.7! Because at p = 0.5, getting 7/10 would be less probable.

<strong>This is the Maximum Likelihood idea:</strong> Find the parameter that makes your observed data most plausible."""
    },
    
    # MLE FORMULA BREAKDOWN
    "mle_breakdown": {
        "header": {"de": "Die Likelihood-Funktion", "en": "The Likelihood Function"},
        "intuition": {
            "de": "Die Likelihood misst, wie plausibel ein Parameterwert ist, gegeben die Daten.",
            "en": "The likelihood measures how plausible a parameter value is, given the data."
        },
        "formula": r"L(\theta) = \prod_{i=1}^{n} f(x_i; \theta) = f(x_1; \theta) \cdot f(x_2; \theta) \cdot \ldots \cdot f(x_n; \theta)",
        "parts": [
            {
                "formula": r"L(\theta)",
                "name": {"de": "Likelihood-Funktion", "en": "Likelihood function"},
                "explanation": {"de": "Wie plausibel ist θ, wenn wir diese Daten sehen?", "en": "How plausible is θ given this data?"}
            },
            {
                "formula": r"f(x_i; \theta)",
                "name": {"de": "Wahrscheinlichkeit", "en": "Probability"},
                "explanation": {"de": "P(Wert xᵢ beobachten | Parameter = θ)", "en": "P(observing value xᵢ | parameter = θ)"}
            },
            {
                "formula": r"\theta",
                "name": {"de": "Parameter", "en": "Parameter"},
                "explanation": {"de": "Der unbekannte Wert, den wir finden wollen", "en": "The unknown value we want to find"}
            }
        ],
        "key_insight": {
            "de": "Produkte sind schwer zu maximieren! Deshalb nehmen wir den <strong>Logarithmus</strong>: Die Log-Likelihood log L(θ) ist einfacher zu differenzieren.",
            "en": "Products are hard to maximize! That's why we take the <strong>logarithm</strong>: The log-likelihood log L(θ) is easier to differentiate."
        }
    },
    
    # MLE STEPS
    "mle_steps": {
        "header": {"de": "Maximum-Likelihood — Schritt für Schritt", "en": "Maximum Likelihood — Step by Step"},
        "steps": [
            {
                "action": {"de": "Likelihood aufschreiben", "en": "Write the likelihood"},
                "explanation": {"de": "Produkt aller Wahrscheinlichkeiten", "en": "Product of all probabilities"},
                "formula": r"L(\theta) = \prod_{i=1}^{n} f(x_i; \theta)"
            },
            {
                "action": {"de": "Log-Likelihood bilden", "en": "Take the log"},
                "explanation": {"de": "Logarithmus verwandelt Produkt in Summe", "en": "Log transforms product into sum"},
                "formula": r"\ell(\theta) = \log L(\theta) = \sum_{i=1}^{n} \log f(x_i; \theta)"
            },
            {
                "action": {"de": "Ableitung = 0 setzen", "en": "Set derivative = 0"},
                "explanation": {"de": "Notwendige Bedingung für Maximum", "en": "Necessary condition for maximum"},
                "formula": r"\frac{d\ell}{d\theta} = 0 \implies \hat{\theta}_{MLE}"
            }
        ]
    },
    
    # THE SURPRISING DIFFERENCE
    "surprise": {
        "header": {"de": "Wenn die Methoden unterschiedliche Ergebnisse liefern", "en": "When Methods Give Different Results"},
        "intro": {
            "de": "Für viele Verteilungen (Poisson, Normal) liefern MOM und MLE dasselbe Ergebnis. Aber nicht immer!",
            "en": "For many distributions (Poisson, Normal), MOM and MLE give the same result. But not always!"
        },
        "example_title": {"de": "Beispiel: Gleichverteilung U[0, b]", "en": "Example: Uniform U[0, b]"},
        "example_data": {"de": "Daten: 1, 3, 5", "en": "Data: 1, 3, 5"},
        "mom_result": {
            "de": "MOM: E[X] = b/2, also b = 2·X̄ = 2·3 = 6",
            "en": "MOM: E[X] = b/2, so b = 2·X̄ = 2·3 = 6"
        },
        "mle_result": {
            "de": "MLE: b muss mindestens max(xᵢ) sein → b = 5",
            "en": "MLE: b must be at least max(xᵢ) → b = 5"
        },
        "insight": {
            "de": "MLE ist hier besser: b kann nicht kleiner als das grösste beobachtete x sein!",
            "en": "MLE is better here: b cannot be smaller than the largest observed x!"
        }
    },
    
    # DECISION TREE - converted to IF/THEN decisions format
    "decision_tree": {
        "header": {"de": "Welche Methode wählen?", "en": "Which Method to Choose?"},
        "decisions": [
            {
                "condition": {"de": "E[X] ist einfach als Funktion von θ auszudrücken", "en": "E[X] is easy to express as function of θ"},
                "result": {"de": "MOM (schnell und einfach)", "en": "MOM (quick and simple)"}
            },
            {
                "condition": {"de": "Ich brauche den optimalen Schätzer", "en": "I need the optimal estimator"},
                "result": {"de": "MLE (mehr Arbeit, besseres Ergebnis)", "en": "MLE (more work, better result)"}
            },
            {
                "condition": {"de": "Ich bin unsicher, welche Methode besser ist", "en": "I'm unsure which method is better"},
                "result": {"de": "Beide berechnen und vergleichen", "en": "Calculate both and compare"}
            },
            {
                "condition": {"de": "Die Frage gibt die Methode explizit vor", "en": "The question explicitly specifies the method"},
                "result": {"de": "Die vorgegebene Methode verwenden!", "en": "Use the specified method!"},
                "highlight": True
            }
        ]
    },
    
    # FRAG DICH
    "frag_dich": {
        "header": {"de": "Frag dich: Erkennst du die Methode?", "en": "Ask yourself: Can you recognize the method?"},
        "questions": [
            {"de": "Wenn ich X̄ = μ setze und nach θ auflöse — welche Methode?", 
             "en": "If I set X̄ = μ and solve for θ — which method?"},
            {"de": "Wenn ich L(θ) maximiere — welche Methode?",
             "en": "If I maximize L(θ) — which method?"},
            {"de": "Für Poisson: Sind MOM und MLE gleich?",
             "en": "For Poisson: Are MOM and MLE the same?"},
            {"de": "Für Gleichverteilung U[0,b]: Sind MOM und MLE gleich?",
             "en": "For Uniform U[0,b]: Are MOM and MLE the same?"}
        ],
        "conclusion": {
            "de": "Wenn du alle 4 beantworten kannst, hast du die Methoden gemeistert!",
            "en": "If you can answer all 4, you've mastered the methods!"
        }
    },
    
    # EXAM ESSENTIALS
    "exam_essentials": {
        "trap": {
            "de": "MOM-Logik in einem MLE-Problem anwenden (oder umgekehrt)! <strong>LIES DIE FRAGE:</strong> Steht dort 'Maximum Likelihood' oder 'Momentenmethode'?",
            "en": "Using MOM logic in an MLE problem (or vice versa)! <strong>READ THE QUESTION:</strong> Does it say 'Maximum Likelihood' or 'Method of Moments'?"
        },
        "trap_rule": {
            "de": "Bei 'Maximum Likelihood' → Likelihood aufstellen, log nehmen, ableiten, = 0 setzen",
            "en": "For 'Maximum Likelihood' → Write likelihood, take log, differentiate, set = 0"
        },
        "tips": [
            {
                "tip": {"de": "MLE für Gleichverteilung U[0,b]", "en": "MLE for Uniform U[0,b]"},
                "why": {"de": "Der MLE ist das Maximum der Stichprobe, NICHT das Doppelte des Mittels!", "en": "The MLE is the sample maximum, NOT twice the mean!"},
                "why_formula": r"\hat{b}_{MLE} = \max(x_1, \ldots, x_n) \neq 2\bar{X}"
            },
            {
                "tip": {"de": "Log-Likelihood vor dem Ableiten", "en": "Log-Likelihood before differentiating"},
                "why": {"de": "Der Logarithmus verwandelt das Produkt in eine Summe — viel einfacher abzuleiten!", "en": "The logarithm turns the product into a sum — much easier to differentiate!"},
                "why_formula": r"\log \prod f_i = \sum \log f_i"
            },
            {
                "tip": {"de": "MOM und MLE sind oft gleich — aber nicht immer!", "en": "MOM and MLE are often equal — but not always!"},
                "why": {"de": "Bei Normalverteilung und Poisson: gleich. Bei Gleichverteilung: verschieden.", "en": "For Normal and Poisson: equal. For Uniform: different."}
            }
        ]
    }
}

# =============================================================================
# INTERACTIVE: METHOD DETECTIVE QUIZ
# =============================================================================

@st.fragment
def method_detective_quiz():
    """Interactive quiz: identify which method is being used."""
    
    # Pill button styling - ULTRATHINK FIX - Always white text, fixed size
    st.markdown("""
<style>
/* ULTRATHINK: Force ALL buttons to FIXED size and WHITE text */
.stButton > button,
.stButton > button[kind="secondary"],
.stButton > button[kind="primary"],
div[data-testid="stButton"] > button,
[data-testid="stHorizontalBlock"] .stButton > button {
    border-radius: 20px !important;
    padding: 10px 24px !important;
    font-weight: 500 !important;
    height: 44px !important;
    min-height: 44px !important;
    max-height: 44px !important;
    background: #000 !important;
    background-color: #000 !important;
    color: #fff !important;
    border: 1px solid #000 !important;
    box-sizing: border-box !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
}
.stButton > button:hover,
div[data-testid="stButton"] > button:hover {
    background: #333 !important;
    background-color: #333 !important;
    border-color: #333 !important;
}
/* CRITICAL: Force ALL nested elements to white text */
.stButton > button *,
div[data-testid="stButton"] > button * {
    color: #fff !important;
    margin: 0 !important;
    padding: 0 !important;
}
</style>
""", unsafe_allow_html=True)
    
    # Quiz questions - each shows a calculation snippet with LaTeX
    quiz_questions = [
        {
            "text": {
                "de": "Gegeben:",
                "en": "Given:"
            },
            "latex": r"E[X] = \frac{1}{\lambda}, \quad \bar{X} = 0.5 \implies \hat{\lambda} = 2",
            "context": {
                "de": "Setze Stichprobenmittel = Erwartungswert",
                "en": "Set sample mean = expected value"
            },
            "answer": "MOM",
            "explanation": {
                "de": "Das Gleichsetzen von",
                "en": "Setting"
            },
            "explanation_latex": r"\bar{X} = E[X]",
            "explanation_suffix": {
                "de": "ist die Momentenmethode!",
                "en": "is the Method of Moments!"
            }
        },
        {
            "text": {
                "de": "Gesucht:",
                "en": "Find:"
            },
            "latex": r"\frac{d \log L(\theta)}{d\theta} = 0",
            "context": {
                "de": "Ableitung der Log-Likelihood null setzen",
                "en": "Set derivative of log-likelihood to zero"
            },
            "answer": "MLE",
            "explanation": {
                "de": "Das Ableiten der Log-Likelihood ist Maximum-Likelihood!",
                "en": "Differentiating the log-likelihood is Maximum Likelihood!"
            }
        },
        {
            "text": {
                "de": "Gegeben:",
                "en": "Given:"
            },
            "latex": r"L(p) = p^3(1-p)^2 \implies \hat{p} = \frac{3}{5}",
            "context": {
                "de": "Maximiere die Likelihood-Funktion",
                "en": "Maximize the likelihood function"
            },
            "answer": "MLE",
            "explanation": {
                "de": "Das Maximieren von",
                "en": "Maximizing"
            },
            "explanation_latex": r"L(p)",
            "explanation_suffix": {
                "de": "ist Maximum-Likelihood!",
                "en": "is Maximum Likelihood!"
            }
        },
        {
            "text": {
                "de": "Für",
                "en": "For"
            },
            "text_latex": r"\text{Poisson}(\lambda)",
            "latex": r"E[X] = \lambda \implies \hat{\lambda} = \bar{X} = 4.2",
            "context": {
                "de": "Erwartungswert gleich Parameter",
                "en": "Expected value equals parameter"
            },
            "answer": "BOTH",
            "explanation": {
                "de": "Bei Poisson sind MOM und MLE identisch: beide ergeben",
                "en": "For Poisson, MOM and MLE are identical: both give"
            },
            "explanation_latex": r"\bar{X}"
        },
        {
            "text": {
                "de": "Für",
                "en": "For"
            },
            "text_latex": r"U[0, b]",
            "latex": r"\hat{b} = \max(x_1, \ldots, x_n) = 7.3",
            "context": {
                "de": "Schätzer = Maximum der Stichprobe",
                "en": "Estimator = sample maximum"
            },
            "answer": "MLE",
            "explanation": {
                "de": "Das Maximum der Stichprobe ist der MLE für die Obergrenze!",
                "en": "The sample maximum is the MLE for the upper bound!"
            }
        }
    ]
    
    # Initialize state
    if "md_current" not in st.session_state:
        st.session_state.md_current = 0
        st.session_state.md_correct = 0
        st.session_state.md_answered = False
        st.session_state.md_last_answer = None
    
    max_rounds = 5
    current = st.session_state.md_current
    
    # Check if completed
    if current >= max_rounds:
        score = st.session_state.md_correct
        if score >= 4:
            st.success(t({"de": f"Ausgezeichnet! {score}/{max_rounds} richtig — Du erkennst die Methoden sofort!", 
                          "en": f"Excellent! {score}/{max_rounds} correct — You can spot the methods instantly!"}))
        else:
            st.warning(t({"de": f"{score}/{max_rounds} richtig. Wiederhole die Theorie oben und versuche es nochmal!", 
                          "en": f"{score}/{max_rounds} correct. Review the theory above and try again!"}))
        
        if st.button(t({"de": "Nochmal spielen", "en": "Play again"}), key="md_restart", type="primary"):
            st.session_state.md_current = 0
            st.session_state.md_correct = 0
            st.session_state.md_answered = False
            st.session_state.md_last_answer = None
            st.rerun(scope="fragment")
        return
    
    q = quiz_questions[current]
    
    # Progress
    st.markdown(f"**{t({'de': 'Runde', 'en': 'Round'})} {current + 1}/{max_rounds}**")
    
    # Progress bar
    progress_html = "".join(["●" if i < st.session_state.md_correct else "○" for i in range(max_rounds)])
    st.caption(f"{t({'de': 'Punkte', 'en': 'Score'})}: {progress_html}")
    
    # Question snippet with proper LaTeX
    with st.container(border=True):
        # Handle text with optional inline LaTeX
        if "text_latex" in q:
            c1, c2 = st.columns([0.15, 0.85])
            with c1:
                st.markdown(f"*{t(q['text'])}*")
            with c2:
                st.latex(q["text_latex"])
        else:
            st.markdown(f"*{t(q['text'])}*")
        
        st.latex(q["latex"])
        st.caption(t(q["context"]))
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Answer buttons as pill buttons
    btn_cols = st.columns(3)
    options = [("MOM", "#007AFF"), ("MLE", "#FF4B4B"), ("BOTH", "#6B7280")]
    
    for col, (opt, color) in zip(btn_cols, options):
        with col:
            if st.session_state.md_answered:
                # Show result styling as pills
                if opt == q["answer"]:
                    st.markdown(f"""<div style="background: {color}; color: white; padding: 10px 24px; 
                        border-radius: 20px; text-align: center; font-weight: bold;">{opt}</div>""", 
                        unsafe_allow_html=True)
                elif opt == st.session_state.md_last_answer and opt != q["answer"]:
                    st.markdown(f"""<div style="background: #fee2e2; color: #991b1b; padding: 10px 24px; 
                        border-radius: 20px; text-align: center; text-decoration: line-through;">{opt}</div>""", 
                        unsafe_allow_html=True)
                else:
                    st.markdown(f"""<div style="background: #f4f4f5; padding: 10px 24px; 
                        border-radius: 20px; text-align: center; color: #6B7280;">{opt}</div>""", 
                        unsafe_allow_html=True)
            else:
                if st.button(opt, key=f"md_btn_{opt}_{current}", use_container_width=True):
                    st.session_state.md_answered = True
                    st.session_state.md_last_answer = opt
                    if opt == q["answer"]:
                        st.session_state.md_correct += 1
                    st.rerun(scope="fragment")
    
    # Show feedback with LaTeX support
    if st.session_state.md_answered:
        st.markdown("<br>", unsafe_allow_html=True)
        is_correct = st.session_state.md_last_answer == q["answer"]
        
        # Build the full explanation text
        explanation_text = t(q["explanation"])
        if "explanation_suffix" in q:
            explanation_text += " ... " + t(q["explanation_suffix"])
        
        # Show feedback
        if is_correct:
            st.success(explanation_text)
        else:
            st.error(t({"de": f"Falsch! Richtig wäre: {q['answer']}. ", "en": f"Wrong! Correct answer: {q['answer']}. "}) + explanation_text)
        
        # Show LaTeX formula if present (centered, below the message)
        if "explanation_latex" in q:
            st.latex(q["explanation_latex"])
        
        if st.button(t({"de": "Weiter", "en": "Next"}), key="md_next", type="primary"):
            st.session_state.md_current += 1
            st.session_state.md_answered = False
            st.session_state.md_last_answer = None
            st.rerun(scope="fragment")


# =============================================================================
# MAIN RENDER FUNCTION
# =============================================================================

def render_subtopic_8_3(model):
    """8.3 Methoden zur Konstruktion von Schätzfunktionen"""
    
    # Title and subtitle
    st.header(t(content_8_3["title"]))
    st.markdown(f"*{t(content_8_3['subtitle'])}*")
    st.markdown("---")
    
    # Inject equal height CSS
    inject_equal_height_css()
    
    # =========================================================================
    # SECTION 1: INTUITION
    # =========================================================================
    st.markdown(f"### {t({'de': 'Das grosse Bild', 'en': 'The Big Picture'})}")
    
    with st.container(border=True):
        st.markdown(t(content_8_3["intuition"]), unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # =========================================================================
    # SECTION 2: SIDE-BY-SIDE COMPARISON
    # =========================================================================
    # Build comparison data with formulas included
    left_data = {
        "title": content_8_3["comparison"]["left"]["title"],
        "insight": content_8_3["comparison"]["left"]["insight"],
        "formula": r"\bar{X} = E[X] \implies \text{solve for } \theta"
    }
    right_data = {
        "title": content_8_3["comparison"]["right"]["title"],
        "insight": content_8_3["comparison"]["right"]["insight"],
        "formula": r"\max_\theta L(\theta) \implies \hat{\theta}_{MLE}"
    }
    
    render_comparison(
        title=content_8_3["comparison"]["header"],
        left=left_data,
        right=right_data
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # =========================================================================
    # SECTION 3: MOMENTENMETHODE DEEP DIVE
    # =========================================================================
    st.markdown(f"### {t({'de': 'Methode A: Momentenmethode (MOM)', 'en': 'Method A: Method of Moments (MOM)'})}")
    
    # Intuition box
    with st.container(border=True):
        st.markdown(t({
            "de": """<strong>Die Kernidee:</strong> Dein Stichprobenmittel sollte dem theoretischen Erwartungswert entsprechen. Setze sie gleich und löse nach dem unbekannten Parameter auf.""",
            "en": """<strong>The key idea:</strong> Your sample mean should equal the theoretical expected value. Set them equal and solve for the unknown parameter."""
        }), unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Steps
    render_steps(
        title=content_8_3["mom_steps"]["header"],
        steps=content_8_3["mom_steps"]["steps"]
    )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Worked example
    render_worked_example(
        header=content_8_3["mom_example"]["header"],
        problem=content_8_3["mom_example"]["problem"],
        steps=content_8_3["mom_example"]["steps"],
        answer=content_8_3["mom_example"]["answer"]
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # =========================================================================
    # SECTION 4: MAXIMUM LIKELIHOOD DEEP DIVE
    # =========================================================================
    st.markdown(f"### {t({'de': 'Methode B: Maximum-Likelihood (MLE)', 'en': 'Method B: Maximum Likelihood (MLE)'})}")
    
    # Intuition box
    with st.container(border=True):
        st.markdown(t(content_8_3["mle_intuition"]), unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Likelihood formula breakdown
    render_formula_breakdown(
        title=content_8_3["mle_breakdown"]["header"],
        story=content_8_3["mle_breakdown"]["intuition"],
        formula=content_8_3["mle_breakdown"]["formula"],
        parts=content_8_3["mle_breakdown"]["parts"]
    )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Key insight about log
    st.markdown(f"### {t({'de': 'Warum Log-Likelihood?', 'en': 'Why Log-Likelihood?'})}")
    with st.container(border=True):
        st.markdown(t(content_8_3["mle_breakdown"]["key_insight"]), unsafe_allow_html=True)
        st.markdown("---")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"**{t({'de': 'Vorher (schwer)', 'en': 'Before (hard)'})}:**")
            st.latex(r"L(\theta) = f_1 \cdot f_2 \cdot \ldots \cdot f_n")
        with col2:
            st.markdown(f"**{t({'de': 'Nachher (einfach)', 'en': 'After (easy)'})}:**")
            st.latex(r"\log L(\theta) = \log f_1 + \log f_2 + \ldots + \log f_n")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # MLE steps
    render_steps(
        title=content_8_3["mle_steps"]["header"],
        steps=content_8_3["mle_steps"]["steps"]
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # =========================================================================
    # SECTION 5: WHEN METHODS DIFFER
    # =========================================================================
    st.markdown(f"### {t(content_8_3['surprise']['header'])}")
    
    st.markdown(t(content_8_3["surprise"]["intro"]))
    st.markdown("<br>", unsafe_allow_html=True)
    
    with st.container(border=True):
        st.markdown(f"**{t(content_8_3['surprise']['example_title'])}**")
        st.markdown(t(content_8_3["surprise"]["example_data"]))
        st.markdown("---")
        
        col_mom, col_mle = st.columns(2)
        with col_mom:
            st.markdown(f"<span style='color: #007AFF; font-weight: bold;'>MOM:</span>", unsafe_allow_html=True)
            st.latex(r"E[X] = \frac{b}{2} \implies b = 2\bar{X} = 2 \cdot 3 = {\color{#007AFF}6}")
        with col_mle:
            st.markdown(f"<span style='color: #FF4B4B; font-weight: bold;'>MLE:</span>", unsafe_allow_html=True)
            st.latex(r"\hat{b}_{MLE} = \max(x_i) = {\color{#FF4B4B}5}")
        
        st.markdown("---")
        st.markdown(f"""
<div style="background: #f4f4f5; border-left: 4px solid #a1a1aa; 
            padding: 12px 16px; border-radius: 8px; color: #3f3f46;">
<strong>{t({"de": "Fazit", "en": "Conclusion"})}:</strong> {t(content_8_3["surprise"]["insight"])}
</div>
""", unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # =========================================================================
    # SECTION 6: INTERACTIVE QUIZ
    # =========================================================================
    st.markdown(f"### {t({'de': 'Interaktiv: Methoden-Detektiv', 'en': 'Interactive: Method Detective'})}")
    
    st.markdown(t({
        "de": "Erkenne anhand der Beschreibung, welche Methode verwendet wird!",
        "en": "Identify from the description which method is being used!"
    }))
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    method_detective_quiz()
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # =========================================================================
    # SECTION 7: DECISION TREE
    # =========================================================================
    render_decision_tree(
        title=content_8_3["decision_tree"]["header"],
        decisions=content_8_3["decision_tree"]["decisions"]
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # =========================================================================
    # SECTION 8: FRAG DICH
    # =========================================================================
    render_ask_yourself(
        header=content_8_3["frag_dich"]["header"],
        questions=content_8_3["frag_dich"]["questions"],
        conclusion=content_8_3["frag_dich"]["conclusion"]
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # =========================================================================
    # SECTION 9: EXAM ESSENTIALS
    # =========================================================================
    render_exam_essentials(
        trap=content_8_3["exam_essentials"]["trap"],
        trap_rule=content_8_3["exam_essentials"]["trap_rule"],
        tips=content_8_3["exam_essentials"]["tips"]
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # =========================================================================
    # SECTION 10: MCQ
    # =========================================================================
    st.markdown(f"### {t({'de': 'Prüfungstraining', 'en': 'Exam Practice'})}")
    
    # MCQ 1: MLE for uniform
    q1 = QUESTIONS_8.get("hs2022_mc8")
    if q1:
        st.caption(q1.get("source", ""))
        opts = q1.get("options", [])
        option_labels = [t({"de": o["de"], "en": o["en"]}) for o in opts] if opts else []
        
        with st.container(border=True):
            render_mcq(
                key_suffix="8_3_mle_uniform",
                question_text=t(q1["question"]),
                options=option_labels,
                correct_idx=q1["correct_idx"],
                solution_text_dict=q1["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
                client=model,
                ai_context="Maximum Likelihood Estimator for uniform distribution U[0,b]. MLE = max of sample.",
                course_id="vwl",
                topic_id="8",
                subtopic_id="8.3",
                question_id="8_3_mle_uniform"
            )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # MCQ 2: MOM vs MLE comparison - from QUESTIONS_8_4
    from data.exam_questions import QUESTIONS_8_4
    q2 = QUESTIONS_8_4.get("uebung5_mc12")
    if q2:
        st.caption(q2.get("source", ""))
        opts2 = q2.get("options", [])
        option_labels2 = [t({"de": o["de"], "en": o["en"]}) for o in opts2] if opts2 else []
        
        with st.container(border=True):
            render_mcq(
                key_suffix="8_3_mom_mle_compare",
                question_text=t(q2["question"]),
                options=option_labels2,
                correct_idx=q2["correct_idx"],
                solution_text_dict=q2["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
                client=model,
                ai_context="Comparison of Method of Moments vs Maximum Likelihood - they don't always give same results.",
                course_id="vwl",
                topic_id="8",
                subtopic_id="8.3",
                question_id="8_3_mom_mle_compare"
            )
