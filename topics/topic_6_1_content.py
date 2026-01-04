# Topic 6.1: Der zentrale Grenzwertsatz (Central Limit Theorem)
# ULTRATHINK ENHANCED VERSION
import streamlit as st
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from utils.localization import t
from utils.layouts.foundation import grey_info
from utils.quiz_helper import render_mcq
from utils.ask_yourself import render_ask_yourself
from utils.exam_essentials import render_exam_essentials
from utils.worked_example import render_worked_example
from utils.layouts import render_comparison, render_steps
from utils.layouts.foundation import inject_equal_height_css, grey_callout, key_insight
from data.exam_questions import get_question

# ==========================================
# 1. CONTENT DICTIONARY - BILINGUAL (ULTRATHINK)
# ==========================================
content_6_1 = {
    "title": {"de": "6.1 Der zentrale Grenzwertsatz", "en": "6.1 The Central Limit Theorem"},
    "subtitle": {
        "de": "Die Brücke von 'irgendeine Verteilung' zur Normalverteilung",
        "en": "The bridge from 'any distribution' to the Normal distribution"
    },
    
    # --- INTUITION HOOK ---
    "intuition": {
        "header": {"de": "Die grosse Idee", "en": "The Big Idea"},
        "text": {
            "de": "Stell dir vor, du misst die Körpergrösse von 50 zufälligen Personen und berechnest den Durchschnitt. Dann wiederholst du das Ganze 1000 Mal — jedes Mal mit 50 neuen Personen. Was passiert mit all diesen Durchschnittswerten? Sie formen eine **Glockenkurve** — egal wie die ursprüngliche Verteilung der Körpergrössen aussah! Das ist die Magie des zentralen Grenzwertsatzes.",
            "en": "Imagine measuring the height of 50 random people and calculating the average. Then you repeat this 1000 times — each time with 50 new people. What happens to all these averages? They form a **bell curve** — regardless of what the original height distribution looked like! This is the magic of the Central Limit Theorem."
        },
        "punchline": {
            "de": "Das ist, was der ZGS sagt: Mittelwerte von Stichproben sind immer normalverteilt — wenn n gross genug ist!",
            "en": "This is what the CLT says: Sample means are always normally distributed — if n is large enough!"
        }
    },
    
    # --- i.i.d. DEFINITION ---
    # --- i.i.d. DEFINITION (ULTRATHINK: Stupid Person Rule) ---
    "iid_definition": {
        "term": {"de": "i.i.d. (unabhängig und identisch verteilt)", "en": "i.i.d. (independent and identically distributed)"},
        
        # THE ANALOGY (A 12-year-old must understand this)
        "analogy": {
            "de": "Stell dir vor, du hast einen Beutel mit 100 nummerierten Bällen. Du ziehst einen Ball, notierst die Nummer, und <strong>legst ihn zurück</strong>. Dann schüttelst du und ziehst wieder. Jeder Zug ist gleich (identisch) und der vorherige Zug beeinflusst den nächsten nicht (unabhängig). Das ist i.i.d.!",
            "en": "Imagine you have a bag with 100 numbered balls. You draw a ball, write down the number, and <strong>put it back</strong>. Then you shake and draw again. Each draw is the same (identical) and the previous draw doesn't affect the next (independent). That's i.i.d.!"
        },
        
        # THE TWO CONDITIONS (Broken down simply)
        "conditions": {
            "independent": {
                "title": {"de": "Unabhängig", "en": "Independent"},
                "simple": {
                    "de": "Wissen über eine Variable sagt NICHTS über die anderen aus.",
                    "en": "Knowing one variable tells you NOTHING about the others."
                },
                "example": {
                    "de": "Wenn der 1. Würfelwurf eine 6 ist, ändert das die Chance für den 2. Wurf nicht.",
                    "en": "If the 1st die roll is a 6, it doesn't change the odds for the 2nd roll."
                }
            },
            "identical": {
                "title": {"de": "Identisch verteilt", "en": "Identically distributed"},
                "simple": {
                    "de": "Alle Variablen kommen aus der GLEICHEN 'Maschine' (gleiche Verteilung, μ, σ).",
                    "en": "All variables come from the SAME 'machine' (same distribution, μ, σ)."
                },
                "example": {
                    "de": "Alle Würfelwürfe haben dieselbe Verteilung: 1/6 für jede Zahl.",
                    "en": "All die rolls have the same distribution: 1/6 for each number."
                }
            }
        },
        
        # WHY IT MATTERS (The "So what?")
        "why_matters": {
            "de": "Der ZGS funktioniert nur, wenn deine Daten i.i.d. sind! Ohne diese Bedingung kannst du die Normalverteilung nicht anwenden.",
            "en": "The CLT only works if your data is i.i.d.! Without this condition, you can't apply the Normal distribution."
        },
        
        # RECOGNITION SIGNALS (When to spot it)
        "signals": {
            "iid_yes": [
                {"de": "Mit Zurücklegen", "en": "With replacement"},
                {"de": "Unabhängige Wiederholungen", "en": "Independent repetitions"},
                {"de": "Gleiche Bedingungen bei jedem Versuch", "en": "Same conditions for each trial"}
            ],
            "iid_no": [
                {"de": "Ohne Zurücklegen (dann Hypergeometrisch!)", "en": "Without replacement (then Hypergeometric!)"},
                {"de": "Zeitreihen mit Trend", "en": "Time series with trends"},
                {"de": "Abhängige Messungen (z.B. Familienmitglieder)", "en": "Dependent measurements (e.g., family members)"}
            ]
        },
        
        # CONCRETE EXAMPLES
        "examples": [
            {"de": "Stichprobe mit Zurücklegen aus einer Urne", "en": "Sample with replacement from an urn"},
            {"de": "Wiederholte Würfelwürfe (gleicher Würfel, gleiche Bedingungen)", "en": "Repeated dice rolls (same die, same conditions)"},
            {"de": "Gewichte von zufällig ausgewählten Produkten (aus grosser Produktion)", "en": "Weights of randomly selected products (from large production)"}
        ]
    },
    
    # --- SUM VS MEAN COMPARISON ---
    "comparison": {
        "left": {
            "title": {"de": "Die Summe $S_n$", "en": "The Sum $S_n$"},
            "formula": r"S_n = \sum_{i=1}^{n} X_i",
            "expectation": r"E[S_n] = n \cdot \mu",
            "variance": r"\text{Var}(S_n) = n \cdot \sigma^2",
            "insight": {
                "de": "Die Streuung **wächst** mit n. Je mehr du addierst, desto unsicherer die Summe.",
                "en": "The spread **grows** with n. The more you add, the more uncertain the sum."
            }
        },
        "right": {
            "title": {"de": "Der Mittelwert $\\bar{X}_n$", "en": "The Mean $\\bar{X}_n$"},
            "formula": r"\bar{X}_n = \frac{1}{n} \sum_{i=1}^{n} X_i = \frac{S_n}{n}",
            "expectation": r"E[\bar{X}] = \mu",
            "variance": r"\text{Var}(\bar{X}) = \frac{\sigma^2}{n}",
            "insight": {
                "de": "Die Streuung **schrumpft** mit n ($\\sqrt{n}$-Gesetz). Grössere Stichproben = präzisere Schätzung!",
                "en": "The spread **shrinks** with n ($\\sqrt{n}$-law). Larger samples = more precise estimate!"
            }
        }
    },
    
    # --- THE CLT THEOREM ---
    "theorem": {
        "header": {"de": "Der zentrale Grenzwertsatz (ZGS)", "en": "The Central Limit Theorem (CLT)"},
        "statement": {
            "de": "Seien $X_1, X_2, \\ldots, X_n$ i.i.d. Zufallsvariablen mit $E[X_i] = \\mu$ und $\\text{Var}(X_i) = \\sigma^2$. Für grosses n gilt:",
            "en": "Let $X_1, X_2, \\ldots, X_n$ be i.i.d. random variables with $E[X_i] = \\mu$ and $\\text{Var}(X_i) = \\sigma^2$. For large n:"
        },
        "formula_sum": r"Z_n = \frac{S_n - n\mu}{\sigma\sqrt{n}} \xrightarrow{d} N(0,1)",
        "formula_mean": r"Z_n = \frac{\bar{X} - \mu}{\sigma / \sqrt{n}} \xrightarrow{d} N(0,1)",
        
        # INLINE MINI-DECODER (so user understands without scrolling)
        "inline_decoder": {
            "header": {"de": "Was steht hier?", "en": "What does this say?"},
            "items": [
                {"symbol": "$X_i$", "meaning": {"de": "Eine einzelne Messung (z.B. Gewicht einer Person)", "en": "A single measurement (e.g., weight of one person)"}},
                {"symbol": "$n$", "meaning": {"de": "Anzahl Messungen", "en": "Number of measurements"}},
                {"symbol": "$\\mu$", "meaning": {"de": "Der Durchschnitt aller möglichen Messungen ('wahrer Mittelwert')", "en": "The average of all possible measurements ('true mean')"}},
                {"symbol": "$\\sigma$", "meaning": {"de": "Wie stark einzelne Messungen streuen", "en": "How much individual measurements vary"}},
                {"symbol": "$S_n$", "meaning": {"de": "Summe aller n Messungen", "en": "Sum of all n measurements"}},
                {"symbol": "$\\bar{X}$", "meaning": {"de": "Durchschnitt der n Messungen", "en": "Average of the n measurements"}},
                {"symbol": "$Z_n$", "meaning": {"de": "Die standardisierte Grösse (hat immer Mittelwert 0, Streuung 1)", "en": "The standardized statistic (always has mean 0, spread 1)"}},
                {"symbol": "$N(0,1)$", "meaning": {"de": "Die Standard-Normalverteilung (die berühmte Glockenkurve)", "en": "The Standard Normal distribution (the famous bell curve)"}}
            ]
        },
        
        # PRACTICAL MEANING - use separate LaTeX elements to render properly
        "practical_intro": {
            "de": "Das heisst praktisch:",
            "en": "This means in practice:"
        },
        "practical_formulas": [
            {"label": {"de": "Summe", "en": "Sum"}, "formula": r"S_n \approx N(n\mu, n\sigma^2)"},
            {"label": {"de": "Mittelwert", "en": "Mean"}, "formula": r"\bar{X} \approx N\left(\mu, \frac{\sigma^2}{n}\right)"}
        ]
    },
    
    # --- VARIABLE DECODER ---
    "variables": {
        "header": {"de": "Was bedeutet jede Variable?", "en": "What does each variable mean?"},
        "items": [
            {
                "symbol": r"X_i",
                "name": {"de": "Einzelne Beobachtung", "en": "Individual observation"},
                "meaning": {"de": "Eine einzelne Messung (z.B. Gewicht einer Person)", "en": "A single measurement (e.g., weight of one person)"}
            },
            {
                "symbol": r"n",
                "name": {"de": "Stichprobengrösse", "en": "Sample size"},
                "meaning": {"de": "Anzahl Beobachtungen. Faustregel: n ≥ 30 für gute Approximation", "en": "Number of observations. Rule of thumb: n ≥ 30 for good approximation"}
            },
            {
                "symbol": r"\mu",
                "name": {"de": "Erwartungswert der Grundgesamtheit", "en": "Population mean"},
                "meaning": {"de": "Der 'wahre' Mittelwert — oft unbekannt!", "en": "The 'true' mean — often unknown!"}
            },
            {
                "symbol": r"\sigma^2",
                "name": {"de": "Varianz der Grundgesamtheit", "en": "Population variance"},
                "meaning": {"de": "Die Streuung einer einzelnen Beobachtung", "en": "The spread of a single observation"}
            },
            {
                "symbol": r"S_n",
                "name": {"de": "Summe aller Beobachtungen", "en": "Sum of all observations"},
                "meaning": {"de": "Var(Summe) wächst mit n", "en": "Var(Sum) grows with n"}
            },
            {
                "symbol": r"\bar{X}",
                "name": {"de": "Stichprobenmittelwert", "en": "Sample mean"},
                "meaning": {"de": "Var(Mittelwert) schrumpft mit n", "en": "Var(Mean) shrinks with n"}
            },
            {
                "symbol": r"Z_n",
                "name": {"de": "Standardisierte Grösse", "en": "Standardized statistic"},
                "meaning": {"de": "Diese konvergiert gegen N(0,1) — das ist der ZGS!", "en": "This converges to N(0,1) — this is the CLT!"}
            }
        ]
    },
    
    # --- 5-STEP PROCEDURE ---
    "steps": {
        "header": {"de": "5-Schritte-Rezept: ZGS anwenden", "en": "5-Step Recipe: Apply the CLT"},
        "items": [
            {
                "title": {"de": "Identifiziere die i.i.d. Variablen", "en": "Identify the i.i.d. variables"},
                "content": {"de": "z.B. 'Gewicht einer Person'", "en": "e.g., 'weight of one person'"},
                "formula": r"X_i = \text{?}"
            },
            {
                "title": {"de": "Finde Erwartungswert und Varianz für EINE Variable", "en": "Find mean and variance for ONE variable"},
                "content": {"de": "Die Parameter der Grundgesamtheit", "en": "The population parameters"},
                "formula": {"de": r"E[X_i] = \mu \quad \text{und} \quad \text{Var}(X_i) = \sigma^2", "en": r"E[X_i] = \mu \quad \text{and} \quad \text{Var}(X_i) = \sigma^2"}
            },
            {
                "title": {"de": "Summe oder Mittelwert?", "en": "Sum or Mean?"},
                "content": {"de": "Geht es um das Total oder den Durchschnitt?", "en": "Is it about the total or the average?"},
                "formula": {"de": r"S_n = \sum X_i \quad \text{oder} \quad \bar{X} = \frac{S_n}{n}", "en": r"S_n = \sum X_i \quad \text{or} \quad \bar{X} = \frac{S_n}{n}"}
            },
            {
                "title": {"de": "Berechne E und Var für deine Grösse", "en": "Calculate E and Var for your quantity"},
                "content": None,
                "formula": {"de": r"\text{Summe: } E = n\mu, \, \text{Var} = n\sigma^2 \quad | \quad \text{Mittelwert: } E = \mu, \, \text{Var} = \frac{\sigma^2}{n}", "en": r"\text{Sum: } E = n\mu, \, \text{Var} = n\sigma^2 \quad | \quad \text{Mean: } E = \mu, \, \text{Var} = \frac{\sigma^2}{n}"}
            },
            {
                "title": {"de": "Standardisiere und nutze Z-Tabelle", "en": "Standardize and use Z-table"},
                "content": None,
                "formula": {"de": r"Z = \frac{\text{Wert} - \text{Erwartungswert}}{\text{Standardabweichung}}", "en": r"Z = \frac{\text{Value} - \text{Expected Value}}{\text{Standard Deviation}}"}
            }
        ]
    },
    
    # --- WORKED EXAMPLE ---
    "worked_example": {
        "header": {"de": "Beispiel: Seilbahn-Sicherheit", "en": "Example: Cable Car Safety"},
        "problem": {
            "de": "Eine Seilbahn hat eine maximale Tragkraft von <strong style='color:#FF4B4B'>4200 kg</strong>. Es sind <strong style='color:#007AFF'>n = 50</strong> Passagiere an Bord. Das Gewicht pro Person hat Erwartungswert <strong style='color:#007AFF'>μ = 80 kg</strong> und Standardabweichung <strong style='color:#6B7280'>σ = 10 kg</strong>. Wie gross ist die Wahrscheinlichkeit einer Überlastung?",
            "en": "A cable car has a maximum capacity of <strong style='color:#FF4B4B'>4200 kg</strong>. There are <strong style='color:#007AFF'>n = 50</strong> passengers on board. Weight per person has mean <strong style='color:#007AFF'>μ = 80 kg</strong> and standard deviation <strong style='color:#6B7280'>σ = 10 kg</strong>. What is the probability of overloading?"
        },
        "steps": [
            {
                "label": {"de": "Gegeben", "en": "Given"},
                "latex": r"{\color{#007AFF}n = 50}, \quad {\color{#007AFF}\mu = 80}, \quad {\color{#6B7280}\sigma = 10}, \quad \text{Limit} = {\color{#FF4B4B}4200}",
                "note": None
            },
            {
                "label": {"de": "Summen-Parameter", "en": "Sum Parameters"},
                "latex": r"E[S_{50}] = {\color{#007AFF}50} \cdot {\color{#007AFF}80} = {\color{#9B59B6}4000}, \quad \sigma_{S} = \sqrt{{\color{#007AFF}50}} \cdot {\color{#6B7280}10} \approx {\color{#9B59B6}70.7}",
                "note": {"de": "Erwartetes Gesamtgewicht und dessen Streuung", "en": "Expected total weight and its spread"}
            },
            {
                "label": {"de": "Gesucht", "en": "Find"},
                "latex": r"P(S_{50} > {\color{#FF4B4B}4200}) = P\left(Z > \frac{{\color{#FF4B4B}4200} - {\color{#9B59B6}4000}}{{\color{#9B59B6}70.7}}\right)",
                "note": None
            },
            {
                "label": {"de": "Rechnung", "en": "Calculation"},
                "latex": r"Z = \frac{200}{70.7} \approx 2.83",
                "note": None
            },
            {
                "label": {"de": "Z-Tabelle", "en": "Z-Table"},
                "latex": r"P(Z > 2.83) = 1 - \Phi(2.83) \approx 1 - 0.9977 = {\color{#16a34a}\mathbf{0.0023}}",
                "note": None
            }
        ],
        "answer": {
            "de": "Die Wahrscheinlichkeit einer Überlastung beträgt etwa **0.23%** — ein sehr kleines Risiko!",
            "en": "The probability of overloading is approximately **0.23%** — a very small risk!"
        }
    },
    
    # --- FRAG DICH ---
    "frag_dich": {
        "header": {"de": "Frag dich: Kann ich den ZGS anwenden?", "en": "Ask yourself: Can I apply the CLT?"},
        "questions": [
            {"de": "Sind die X<sub>i</sub> <strong>unabhängig</strong> voneinander?", "en": "Are the X<sub>i</sub> <strong>independent</strong> of each other?"},
            {"de": "Haben alle X<sub>i</sub> die <strong>gleiche Verteilung</strong> (gleiche μ und σ)?", "en": "Do all X<sub>i</sub> have the <strong>same distribution</strong> (same μ and σ)?"},
            {"de": "Ist <strong>n gross genug</strong> (≥ 30)?", "en": "Is <strong>n large enough</strong> (≥ 30)?"},
            {"de": "Suche ich P für eine <strong>Summe oder einen Mittelwert</strong>?", "en": "Am I looking for P for a <strong>sum or a mean</strong>?"}
        ],
        "conclusion": {"de": "4× Ja → ZGS anwenden!", "en": "4× Yes → Apply the CLT!"}
    },
    
    # --- EXAM ESSENTIALS ---
    "exam_essentials": {
        "trap": {
            "de": "<strong>Mean vs Sum verwechseln:</strong> Bei der Summe $S_n$ <em>wächst</em> die Varianz mit n (= nσ²). Beim Mittelwert $\\bar{X}$ <em>schrumpft</em> sie (= σ²/n).",
            "en": "<strong>Confusing Mean vs Sum:</strong> For the sum $S_n$, variance <em>grows</em> with n (= nσ²). For the mean $\\bar{X}$, it <em>shrinks</em> (= σ²/n)."
        },
        "trap_rule": {
            "de": "Immer zuerst klären: Suche ich die Summe oder den Mittelwert?",
            "en": "Always clarify first: Am I looking for the sum or the mean?"
        },
        "tips": [
            {
                "tip": {"de": "Standardisierung nicht vergessen!", "en": "Don't forget to standardize!"},
                "why": {"de": "Der ZGS gilt für die standardisierte Grösse $Z$, nicht direkt für $S_n$ oder $\\bar{X}$.", "en": "The CLT applies to the standardized statistic $Z$, not directly to $S_n$ or $\\bar{X}$."}
            },
            {
                "tip": {"de": "n ≥ 30 ist die Faustregel", "en": "n ≥ 30 is the rule of thumb"},
                "why": {"de": "Bei kleinerem n ist die Approximation ungenau — ausser wenn $X$ bereits normalverteilt ist.", "en": "With smaller n, the approximation is inaccurate — unless $X$ is already normally distributed."}
            },
            {
                "tip": {"de": "Stetigkeitskorrektur bei diskreten Verteilungen", "en": "Continuity correction for discrete distributions"},
                "why": {"de": "Bei Binomial → Normal: ±0.5 Korrektur für bessere Approximation (z.B. P(X ≥ 60) → P(X > 59.5)).", "en": "For Binomial → Normal: ±0.5 correction for better approximation (e.g., P(X ≥ 60) → P(X > 59.5))."},
                "tip_formula": r"P(X \geq k) \approx P\left(Z > \frac{k - 0.5 - np}{\sqrt{np(1-p)}}\right)"
            }
        ]
    },
    
    # --- INTERACTIVE MISSION ---
    "mission": {
        "scenario": {
            "de": "Du bist Qualitätsingenieur in einer Batteriefabrik. Jede Batterie hat eine zufällige Lebensdauer. Du nimmst Stichproben von n Batterien und berechnest den Durchschnitt.",
            "en": "You're a quality engineer in a battery factory. Each battery has a random lifetime. You take samples of n batteries and calculate the average."
        },
        "goal": {
            "de": "Entdecke: Was passiert mit der Verteilung der Mittelwerte, wenn du n vergrösserst?",
            "en": "Discover: What happens to the distribution of means as you increase n?"
        },
        "debrief": {
            "de": "Das hast du entdeckt: Egal wie die ursprüngliche Verteilung aussieht — bei grossem n werden die Mittelwerte immer normalverteilt! Das ist der zentrale Grenzwertsatz in Aktion.",
            "en": "What you discovered: No matter what the original distribution looks like — with large n, the means always become normally distributed! This is the Central Limit Theorem in action."
        }
    }
}


# ==========================================
# 2. INTERACTIVE CLT VISUALIZER
# ==========================================
@st.fragment
def clt_visualizer():
    """Interactive CLT visualization - shows any distribution becoming normal"""
    
    # State initialization
    if "clt_n" not in st.session_state:
        st.session_state.clt_n = 5
    if "clt_dist" not in st.session_state:
        st.session_state.clt_dist = "uniform"
    if "clt_completed" not in st.session_state:
        st.session_state.clt_completed = {"n1": False, "n10": False, "n50": False}
    
    # Scenario
    st.markdown(f"""
<div style="background: #f4f4f5; border-left: 4px solid #a1a1aa; 
            padding: 12px 16px; border-radius: 8px; color: #3f3f46;">
<strong>{t({"de": "Szenario", "en": "Scenario"})}:</strong><br>
{t(content_6_1["mission"]["scenario"])}
</div>
""", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"**{t({'de': 'Mission', 'en': 'Mission'})}:** {t(content_6_1['mission']['goal'])}")
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Controls
    col_ctrl1, col_ctrl2 = st.columns([1, 1])
    
    with col_ctrl1:
        dist_options = {
            "uniform": t({"de": "Gleichverteilung", "en": "Uniform Distribution"}),
            "exponential": t({"de": "Exponentialverteilung (schief)", "en": "Exponential Distribution (skewed)"}),
            "bimodal": t({"de": "Bimodal (zwei Gipfel)", "en": "Bimodal (two peaks)"})
        }
        selected_dist = st.radio(
            t({"de": "Wähle Original-Verteilung:", "en": "Choose Original Distribution:"}),
            options=list(dist_options.keys()),
            format_func=lambda x: dist_options[x],
            key="clt_dist_radio",
            horizontal=True
        )
        st.session_state.clt_dist = selected_dist
    
    with col_ctrl2:
        # Just use key - Streamlit manages the state automatically
        # Don't set value AND key simultaneously (causes 'ping-pong' on reruns)
        n_value = st.slider(
            t({"de": "Stichprobengrösse n:", "en": "Sample size n:"}),
            min_value=1,
            max_value=100,
            value=5,  # Initial value only (ignored after first render when key exists)
            key="clt_n_slider"
        )
        # Read from widget directly, no manual sync needed
        
        # Track completion
        if n_value == 1:
            st.session_state.clt_completed["n1"] = True
        elif n_value >= 10 and n_value < 30:
            st.session_state.clt_completed["n10"] = True
        elif n_value >= 50:
            st.session_state.clt_completed["n50"] = True
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Generate data
    np.random.seed(42)
    n_simulations = 1000
    n = n_value  # Use slider value directly
    dist = selected_dist  # Use radio value directly
    
    # Original distribution
    if dist == "uniform":
        original_data = np.random.uniform(0, 10, 10000)
        samples = np.random.uniform(0, 10, (n_simulations, n))
    elif dist == "exponential":
        original_data = np.random.exponential(5, 10000)
        samples = np.random.exponential(5, (n_simulations, n))
    else:  # bimodal
        original_data = np.concatenate([
            np.random.normal(3, 0.8, 5000),
            np.random.normal(7, 0.8, 5000)
        ])
        samples = np.concatenate([
            np.random.normal(3, 0.8, (n_simulations, n // 2 + n % 2)),
            np.random.normal(7, 0.8, (n_simulations, n // 2))
        ], axis=1)
    
    # Calculate means
    sample_means = np.mean(samples, axis=1)
    
    # Create subplots
    fig = make_subplots(
        rows=1, cols=2,
        subplot_titles=(
            t({"de": "Originalverteilung", "en": "Original Distribution"}),
            t({"de": f"Verteilung der Mittelwerte (n={n})", "en": f"Distribution of Means (n={n})"})
        ),
        horizontal_spacing=0.12
    )
    
    # Left: Original distribution
    fig.add_trace(
        go.Histogram(
            x=original_data,
            nbinsx=50,
            marker_color="#6B7280",
            opacity=0.7,
            name=t({"de": "Original", "en": "Original"})
        ),
        row=1, col=1
    )
    
    # Right: Sample means - color based on how normal it looks
    if n >= 30:
        mean_color = "#16a34a"  # Green - success
    elif n >= 10:
        mean_color = "#9B59B6"  # Purple - getting there
    else:
        mean_color = "#FF4B4B"  # Red - not yet normal
    
    fig.add_trace(
        go.Histogram(
            x=sample_means,
            nbinsx=40,
            marker_color=mean_color,
            opacity=0.8,
            name=t({"de": "Mittelwerte", "en": "Means"})
        ),
        row=1, col=2
    )
    
    fig.update_layout(
        height=350,
        showlegend=False,
        margin=dict(l=40, r=40, t=50, b=40),
        plot_bgcolor="white",
        paper_bgcolor="white"
    )
    
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='#f0f0f0')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#f0f0f0')
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Color legend
    col_leg1, col_leg2, col_leg3 = st.columns(3)
    with col_leg1:
        st.markdown(f"<span style='color:#FF4B4B'>●</span> n < 10: {t({'de': 'ZGS schwach', 'en': 'CLT weak'})}", unsafe_allow_html=True)
    with col_leg2:
        st.markdown(f"<span style='color:#9B59B6'>●</span> 10 ≤ n < 30: {t({'de': 'Besser', 'en': 'Better'})}", unsafe_allow_html=True)
    with col_leg3:
        st.markdown(f"<span style='color:#16a34a'>●</span> n ≥ 30: {t({'de': 'ZGS gültig', 'en': 'CLT valid'})}", unsafe_allow_html=True)
    
    # Feedback based on n
    if n < 5:
        st.warning(t({"de": "n ist sehr klein — die Mittelwerte sind noch nicht normalverteilt!", 
                      "en": "n is very small — the means are not yet normally distributed!"}))
    elif n < 30:
        grey_info(t({"de": "Besser! Die Verteilung wird glockenkurvenartiger...", 
                   "en": "Better! The distribution is becoming more bell-shaped..."}))
    else:
        st.success(t({"de": "Glockenkurve! Bei n ≥ 30 ist der ZGS wirksam!", 
                      "en": "Bell curve! At n ≥ 30, the CLT is in effect!"}))
    
    # Completion check
    all_completed = all(st.session_state.clt_completed.values())
    if all_completed:
        st.markdown("<br>", unsafe_allow_html=True)
        st.success(t({"de": "Mission abgeschlossen!", "en": "Mission Complete!"}))
        st.markdown(f"""
<div style="background: #f4f4f5; border-left: 4px solid #16a34a; 
            padding: 12px 16px; border-radius: 8px; color: #3f3f46;">
<strong>{t({"de": "Was du entdeckt hast", "en": "What You Discovered"})}:</strong><br>
{t(content_6_1["mission"]["debrief"])}
</div>
""", unsafe_allow_html=True)


# ==========================================
# 3. MAIN RENDER FUNCTION
# ==========================================
def render_subtopic_6_1(model):
    """6.1 Der zentrale Grenzwertsatz - ULTRATHINK Enhanced"""
    inject_equal_height_css()
    
    # --- HEADER ---
    st.header(t(content_6_1["title"]))
    st.caption(t(content_6_1["subtitle"]))
    st.markdown("---")
    
    # --- 1. INTUITION HOOK ---
    st.markdown(f"### {t(content_6_1['intuition']['header'])}")
    with st.container(border=True):
        st.markdown(t(content_6_1["intuition"]["text"]))
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(f"""
<div style="background: #f4f4f5; border-left: 4px solid #007AFF; 
            padding: 12px 16px; border-radius: 8px; color: #3f3f46;">
<strong>{t({"de": "Die Kernaussage", "en": "The Core Message"})}:</strong><br>
{t(content_6_1["intuition"]["punchline"])}
</div>
""", unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- 2. i.i.d DEFINITION (ULTRATHINK: Stupid Person Rule) ---
    st.markdown(f"### {t({'de': 'Was bedeutet i.i.d.?', 'en': 'What does i.i.d. mean?'})}")
    
    iid = content_6_1['iid_definition']
    
    with st.container(border=True):
        # Term
        st.markdown(f"**{t(iid['term'])}**")
        st.markdown("<br>", unsafe_allow_html=True)
        
        # THE ANALOGY (Grey callout)
        st.markdown(f"""
<div style="background: #f4f4f5; border-left: 4px solid #007AFF; 
            padding: 12px 16px; border-radius: 8px; color: #3f3f46;">
<strong>{t({"de": "Einfache Vorstellung", "en": "Simple Picture"})}:</strong><br>
{t(iid['analogy'])}
</div>
""", unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # THE TWO CONDITIONS - Side by side
        st.markdown(f"**{t({'de': 'Die zwei Bedingungen:', 'en': 'The Two Conditions:'})}**")
        st.markdown("<br>", unsafe_allow_html=True)
        
        col_ind, col_ident = st.columns(2, gap="medium")
        
        with col_ind:
            cond = iid['conditions']['independent']
            st.markdown(f"**1. {t(cond['title'])}**")
            st.markdown(t(cond['simple']))
            st.caption(t(cond['example']))
        
        with col_ident:
            cond = iid['conditions']['identical']
            st.markdown(f"**2. {t(cond['title'])}**")
            st.markdown(t(cond['simple']))
            st.caption(t(cond['example']))
        
        st.markdown("---")
        
        # WHY IT MATTERS (Grey callout)
        st.markdown(f"""
<div style="background: #f4f4f5; border-left: 4px solid #FF4B4B; 
            padding: 12px 16px; border-radius: 8px; color: #3f3f46;">
<strong>{t({"de": "Warum ist das wichtig?", "en": "Why Does This Matter?"})}:</strong><br>
{t(iid['why_matters'])}
</div>
""", unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # RECOGNITION SIGNALS
        st.markdown(f"**{t({'de': 'Erkennungssignale', 'en': 'Recognition Signals'})}:**")
        
        col_yes, col_no = st.columns(2)
        with col_yes:
            st.markdown(f"<span style='color:#16a34a; font-weight:600'>{t({'de': 'i.i.d. JA', 'en': 'i.i.d. YES'})}</span>", unsafe_allow_html=True)
            for sig in iid['signals']['iid_yes']:
                st.markdown(f"<span style='color:#16a34a'>+</span> {t(sig)}", unsafe_allow_html=True)
        
        with col_no:
            st.markdown(f"<span style='color:#FF4B4B; font-weight:600'>{t({'de': 'i.i.d. NEIN', 'en': 'i.i.d. NO'})}</span>", unsafe_allow_html=True)
            for sig in iid['signals']['iid_no']:
                st.markdown(f"<span style='color:#FF4B4B'>-</span> {t(sig)}", unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- 3. SUM VS MEAN COMPARISON ---
    st.markdown(f"### {t({'de': 'Summe vs. Mittelwert: Der entscheidende Unterschied', 'en': 'Sum vs. Mean: The Crucial Difference'})}")
    
    # Build comparison data
    left = content_6_1["comparison"]["left"]
    right = content_6_1["comparison"]["right"]
    
    col1, col2 = st.columns(2, gap="medium")
    
    with col1:
        with st.container(border=True):
            st.markdown(f"**{t(left['title'])}**")
            st.latex(left["formula"])
            st.markdown("---")
            st.latex(left["expectation"])
            st.latex(left["variance"])
            st.markdown("---")
            st.markdown(f"*{t(left['insight'])}*")
    
    with col2:
        with st.container(border=True):
            st.markdown(f"**{t(right['title'])}**")
            st.latex(right["formula"])
            st.markdown("---")
            st.latex(right["expectation"])
            st.latex(right["variance"])
            st.markdown("---")
            st.markdown(f"*{t(right['insight'])}*")
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- 4. THE CLT THEOREM ---
    st.markdown(f"### {t(content_6_1['theorem']['header'])}")
    with st.container(border=True):
        st.markdown(t(content_6_1["theorem"]["statement"]))
        st.markdown("<br>", unsafe_allow_html=True)
        
        col_sum, col_mean = st.columns(2)
        with col_sum:
            st.markdown(f"**{t({'de': 'Für die Summe:', 'en': 'For the Sum:'})}**")
            st.latex(content_6_1["theorem"]["formula_sum"])
        with col_mean:
            st.markdown(f"**{t({'de': 'Für den Mittelwert:', 'en': 'For the Mean:'})}**")
            st.latex(content_6_1["theorem"]["formula_mean"])
        
        st.markdown("---")
        
        # INLINE SYMBOL DECODER (consolidated from separate section)
        with st.expander(t(content_6_1['variables']['header']), expanded=False):
            for var in content_6_1["variables"]["items"]:
                st.markdown(f"${var['symbol']}$ = **{t(var['name'])}** — {t(var['meaning'])}")
        
        st.markdown("---")
        
        # PRACTICAL MEANING - using proper st.latex for rendering
        st.markdown(f"**{t(content_6_1['theorem']['practical_intro'])}**")
        col_prac1, col_prac2 = st.columns(2)
        for i, item in enumerate(content_6_1['theorem']['practical_formulas']):
            with (col_prac1 if i == 0 else col_prac2):
                st.caption(t(item['label']))
                st.latex(item['formula'])
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- 5. 5-STEP PROCEDURE (Custom for LaTeX support) ---
    st.markdown(f"### {t(content_6_1['steps']['header'])}")
    
    with st.container(border=True):
        steps = content_6_1["steps"]["items"]
        for i, step in enumerate(steps, 1):
            st.markdown(f"**{t({'de': 'Schritt', 'en': 'Step'})} {i}:** {t(step['title'])}")
            
            if step.get("content"):
                st.markdown(t(step["content"]))
            
            if step.get("formula"):
                formula = step["formula"]
                # Handle bilingual formula (dict) or raw string
                if isinstance(formula, dict):
                    st.latex(t(formula))
                else:
                    st.latex(formula)
            
            if i < len(steps):
                st.markdown("---")
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- 6. INTERACTIVE MISSION ---
    st.markdown(f"### {t({'de': 'Interaktive Entdeckung: Der ZGS in Aktion', 'en': 'Interactive Discovery: The CLT in Action'})}")
    clt_visualizer()
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- 7. WORKED EXAMPLE ---
    we = content_6_1["worked_example"]
    render_worked_example(
        header=we["header"],
        problem=we["problem"],
        steps=we["steps"],
        answer=we["answer"]
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- 8. FRAG DICH ---
    render_ask_yourself(
        header=content_6_1["frag_dich"]["header"],
        questions=content_6_1["frag_dich"]["questions"],
        conclusion=content_6_1["frag_dich"]["conclusion"]
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- 9. EXAM ESSENTIALS ---
    ee = content_6_1["exam_essentials"]
    render_exam_essentials(
        trap=ee["trap"],
        trap_rule=ee["trap_rule"],
        tips=ee["tips"]
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- 10. MCQ SECTION ---
    st.markdown(f"### {t({'de': 'Prüfungstraining', 'en': 'Exam Practice'})}")
    
    # MCQ 1: uebung4_mc1 - What does CLT say?
    q1 = get_question("6.3", "uebung4_mc1")
    if q1:
        st.caption(q1.get("source", ""))
        with st.container(border=True):
            opts = q1.get("options", [])
            option_labels = [t(o) for o in opts] if opts and isinstance(opts[0], dict) else opts
            
            render_mcq(
                key_suffix="6_1_clt_def",
                question_text=t(q1["question"]),
                options=option_labels,
                correct_idx=q1["correct_idx"],
                solution_text_dict=q1["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
                client=model,
                ai_context="Central Limit Theorem - definition",
                course_id="vwl",
                topic_id="6",
                subtopic_id="6.1",
                question_id="6_1_clt_def"
            )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # MCQ 2: uebung4_mc2 - Conditions for CLT
    q2 = get_question("6.3", "uebung4_mc2")
    if q2:
        st.caption(q2.get("source", ""))
        with st.container(border=True):
            opts = q2.get("options", [])
            option_labels = [t(o) for o in opts] if opts and isinstance(opts[0], dict) else opts
            
            render_mcq(
                key_suffix="6_1_clt_cond",
                question_text=t(q2["question"]),
                options=option_labels,
                correct_idx=q2["correct_idx"],
                solution_text_dict=q2["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
                client=model,
                ai_context="Central Limit Theorem - conditions",
                course_id="vwl",
                topic_id="6",
                subtopic_id="6.1",
                question_id="6_1_clt_cond"
            )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # MCQ 3: uebung4_prob7 - Cable car
    q3 = get_question("6.3", "uebung4_prob7")
    if q3:
        st.caption(q3.get("source", ""))
        with st.container(border=True):
            opts = q3.get("options", [])
            option_labels = [t(o) for o in opts] if opts and isinstance(opts[0], dict) else opts
            
            render_mcq(
                key_suffix="6_1_cablecar",
                question_text=t(q3["question"]),
                options=option_labels,
                correct_idx=q3["correct_idx"],
                solution_text_dict=q3["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
                client=model,
                ai_context="Central Limit Theorem - cable car overload",
                course_id="vwl",
                topic_id="6",
                subtopic_id="6.1",
                question_id="6_1_cablecar"
            )
