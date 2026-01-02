# Topic 4.3: Binomial Distribution - Binomialverteilung
# ULTRATHINK ENHANCED VERSION
import streamlit as st
from views.styles import inject_equal_height_css
from utils.localization import t
from utils.quiz_helper import render_mcq
from data.exam_questions import get_question

# ==========================================
# 1. CONTENT DICTIONARY - BILINGUAL (ULTRATHINK)
# ==========================================
content_4_3 = {
    "title": {"de": "4.3 Binomialverteilung (diskret)", "en": "4.3 Binomial Distribution (Discrete)"},
    "subtitle": {
        "de": "Anzahl der Erfolge bei n unabhängigen Versuchen",
        "en": "Number of Successes in n Independent Trials"
    },
    
    # --- INTUITION HOOK ---
    "intuition": {
        "header": {"de": "Die Intuition", "en": "The Intuition"},
        "text": {
            "de": "Stell dir vor, du wirfst eine Münze **10-mal** und zählst, wie oft **Kopf** erscheint. Oder du fragst 50 Kunden, ob sie dein Produkt kaufen würden. In beiden Fällen: Du **zählst Erfolge** bei einer **festen Anzahl** unabhängiger Versuche, bei denen jeder Versuch dieselbe Erfolgswahrscheinlichkeit hat.",
            "en": "Imagine flipping a coin **10 times** and counting how often **heads** appears. Or asking 50 customers if they would buy your product. In both cases: You're **counting successes** in a **fixed number** of independent trials, where each trial has the same success probability."
        }
    },
    
    # --- FRAG DICH (Decision Guide) ---
    "frag_dich": {
        "header": {"de": "Frag dich: Ist es Binomial?", "en": "Ask yourself: Is it Binomial?"},
        "questions": [
            {"de": "Zähle ich die Anzahl der <strong>Erfolge</strong>?", "en": "Am I counting the number of <strong>successes</strong>?"},
            {"de": "Habe ich eine <strong>feste Anzahl</strong> n von Versuchen?", "en": "Do I have a <strong>fixed number</strong> n of trials?"},
            {"de": "Sind die Versuche <strong>unabhängig</strong> voneinander?", "en": "Are the trials <strong>independent</strong> of each other?"},
            {"de": "Ist p bei jedem Versuch <strong>gleich</strong>?", "en": "Is p the <strong>same</strong> for each trial?"}
        ],
        "conclusion": {
            "de": "4× Ja → Binomialverteilung anwenden!",
            "en": "4× Yes → Apply Binomial Distribution!"
        }
    },
    
    # --- DEFINITION ---
    "definition": {
        "header": {"de": "Definition & Herleitung", "en": "Definition & Derivation"},
        "text": {
            "de": "Seien $Y_1, Y_2, \\ldots, Y_n$ unabhängige Bernoulli-Zufallsvariablen mit Parameter $p$. Dann ist die Summe $X = \\sum_{i=1}^{n} Y_i$ **binomialverteilt** mit Parametern $n$ und $p$.",
            "en": "Let $Y_1, Y_2, \\ldots, Y_n$ be independent Bernoulli random variables with parameter $p$. Then the sum $X = \\sum_{i=1}^{n} Y_i$ is **binomially distributed** with parameters $n$ and $p$."
        },
        "notation": r"X \sim \text{Bin}(n, p)",
        # VARIABLE DECODER - "Stupid Person Rule" applied
        "variable_decoder": {
            "header": {"de": "Was bedeutet jedes Symbol?", "en": "What does each symbol mean?"},
            "variables": [
                {
                    "symbol": "X",
                    "name": {"de": "Die Zufallsvariable", "en": "The Random Variable"},
                    "meaning": {
                        "de": "Die <strong>Anzahl der Erfolge</strong> in deinen n Versuchen. X kann Werte von <strong>0 bis n</strong> annehmen — nie mehr als n!",
                        "en": "The <strong>number of successes</strong> in your n trials. X can take values from <strong>0 to n</strong> — never more than n!"
                    },
                    "example": {"de": "10 Münzwürfe: X = 'Wie viele Köpfe?' (0, 1, 2, ... oder 10)", "en": "10 coin flips: X = 'How many heads?' (0, 1, 2, ... or 10)"}
                },
                {
                    "symbol": r"\sim",
                    "name": {"de": "'folgt' oder 'ist verteilt nach'", "en": "'follows' or 'is distributed as'"},
                    "meaning": {
                        "de": "Dieses Symbol verbindet die Zufallsvariable mit ihrer Verteilung. Lies es als: <strong>'X folgt einer...'</strong>",
                        "en": "This symbol connects the random variable to its distribution. Read it as: <strong>'X follows a...'</strong>"
                    },
                    "example": {"de": "Wie ein Etikett: sagt dir, welches 'Modell' die Daten beschreibt", "en": "Like a label: tells you which 'model' describes the data"}
                },
                {
                    "symbol": r"\text{Bin}",
                    "name": {"de": "Binomialverteilung", "en": "Binomial Distribution"},
                    "meaning": {
                        "de": "Der <strong>Name</strong> der Verteilung. 'Bi' = zwei Ausgänge (Erfolg/Misserfolg). Zählt Erfolge bei n Versuchen.",
                        "en": "The <strong>name</strong> of the distribution. 'Bi' = two outcomes (success/failure). Counts successes in n trials."
                    },
                    "example": {"de": "Wie 'Poisson' oder 'Normal' — ein Markenname für ein Wahrscheinlichkeitsmodell", "en": "Like 'Poisson' or 'Normal' — a brand name for a probability model"}
                },
                {
                    "symbol": "n",
                    "name": {"de": "Anzahl Versuche", "en": "Number of Trials"},
                    "meaning": {
                        "de": "<strong>Wie oft</strong> du das Experiment wiederholst. Eine <strong>feste ganze Zahl</strong> (1, 2, 3, ...). Muss VOR dem Experiment feststehen!",
                        "en": "<strong>How many times</strong> you repeat the experiment. A <strong>fixed whole number</strong> (1, 2, 3, ...). Must be fixed BEFORE the experiment!"
                    },
                    "example": {"de": "n = 10 Münzwürfe | n = 50 Kunden befragt | n = 20 Produkte geprüft", "en": "n = 10 coin flips | n = 50 customers surveyed | n = 20 products tested"}
                },
                {
                    "symbol": "p",
                    "name": {"de": "Erfolgswahrscheinlichkeit", "en": "Success Probability"},
                    "meaning": {
                        "de": "Die <strong>Chance</strong> für Erfolg bei <strong>EINEM</strong> einzelnen Versuch. Zahl zwischen 0 und 1. <strong>Bleibt konstant</strong> bei jedem Versuch!",
                        "en": "The <strong>chance</strong> of success in <strong>ONE</strong> single trial. Number between 0 and 1. <strong>Stays constant</strong> for every trial!"
                    },
                    "example": {"de": "Faire Münze: p = 0.5 | Würfel 6: p = 1/6 | Defektrate: p = 0.02", "en": "Fair coin: p = 0.5 | Die roll 6: p = 1/6 | Defect rate: p = 0.02"}
                }
            ],
            "full_reading": {
                "de": "<strong>Lies die ganze Notation so:</strong><br>'Die Zufallsvariable X (= Anzahl Erfolge) folgt einer Binomialverteilung mit n Versuchen und Erfolgswahrscheinlichkeit p.'",
                "en": "<strong>Read the full notation as:</strong><br>'The random variable X (= number of successes) follows a Binomial distribution with n trials and success probability p.'"
            }
        }
    },
    
    # --- THE FORMULA (With Breakdown) ---
    "formula": {
        "header": {"de": "Die Massenfunktion", "en": "The Mass Function"},
        "pmf": r"f_{\text{Bi}}(x; n, p) = \binom{n}{x} p^x (1-p)^{n-x}",
        "range": {"de": "x = 0, 1, 2, ..., n (kann nie mehr als n Erfolge haben)", "en": "x = 0, 1, 2, ..., n (can never have more than n successes)"},
        "breakdown": {
            "header": {"de": "Was bedeutet jeder Teil? (Intuition!)", "en": "What does each part mean? (Intuition!)"},
            "parts": [
                {
                    "symbol": r"\binom{n}{x}",
                    "meaning_de": "<strong>Warum C(n,x)?</strong> Du wirfst 10-mal. 3 Erfolge können Wurf 1,2,3 sein ODER Wurf 1,4,7 ODER Wurf 2,5,8... Es gibt viele 'Muster', die alle 3 Erfolge ergeben! C(10,3) = 120 solche Muster. Jedes Muster ist gleichwahrscheinlich.",
                    "meaning_en": "<strong>Why C(n,x)?</strong> You flip 10 times. 3 successes could be flips 1,2,3 OR flips 1,4,7 OR flips 2,5,8... There are many 'patterns' that all give 3 successes! C(10,3) = 120 such patterns. Each pattern is equally likely."
                },
                {
                    "symbol": r"p^x",
                    "meaning_de": "<strong>Warum p hoch x?</strong> Jeder Erfolg hat Wahrscheinlichkeit p. Bei x Erfolgen: p × p × ... × p = p<sup>x</sup>. Beispiel: p = 0.5, x = 3 → 0.5³ = 0.125.",
                    "meaning_en": "<strong>Why p to the x?</strong> Each success has probability p. For x successes: p × p × ... × p = p<sup>x</sup>. Example: p = 0.5, x = 3 → 0.5³ = 0.125."
                },
                {
                    "symbol": r"(1-p)^{n-x}",
                    "meaning_de": "<strong>Warum (1-p) hoch (n-x)?</strong> Von n Versuchen sind (n-x) Misserfolge. Jeder Misserfolg hat Wahrscheinlichkeit (1-p). Beispiel: n=10, x=3 → 7 Misserfolge, jeder mit Prob. 0.5 → 0.5⁷.",
                    "meaning_en": "<strong>Why (1-p) to the (n-x)?</strong> Of n trials, (n-x) are failures. Each failure has probability (1-p). Example: n=10, x=3 → 7 failures, each with prob. 0.5 → 0.5⁷."
                }
            ],
            "example": {
                "de": "<strong>Zusammen:</strong> P(3 Köpfe bei 10 Würfen, p=0.5) = C(10,3) × 0.5³ × 0.5⁷ = 120 × 0.125 × 0.0078 ≈ 0.117",
                "en": "<strong>Together:</strong> P(3 heads in 10 flips, p=0.5) = C(10,3) × 0.5³ × 0.5⁷ = 120 × 0.125 × 0.0078 ≈ 0.117"
            }
        }
    },
    
    # --- PARAMETERS WITH MEANING ---
    "parameters": {
        "header": {"de": "Die Parameter", "en": "The Parameters"},
        "n": {
            "symbol": r"n \in \{1, 2, 3, \ldots\}",
            "name_de": "Anzahl Versuche",
            "name_en": "Number of Trials",
            "meaning_de": "Wie oft wird das Experiment durchgeführt?",
            "meaning_en": "How many times is the experiment performed?"
        },
        "p": {
            "symbol": r"p \in [0, 1]",
            "name_de": "Erfolgswahrscheinlichkeit",
            "name_en": "Success Probability",
            "meaning_de": "Wie wahrscheinlich ist 'Erfolg' bei EINEM Versuch?",
            "meaning_en": "How likely is 'success' in ONE trial?"
        }
    },
    
    # --- MOMENTS WITH INTERPRETATION ---
    "moments": {
        "header": {"de": "Erwartungswert & Varianz", "en": "Expected Value & Variance"},
        "expectation": {
            "title_de": "Erwartungswert",
            "title_en": "Expected Value",
            "formula": r"E[X] = n \cdot p",
            "interpretation_de": "Bei 100 Würfen mit p=0.3 erwarte ich im Schnitt 30 Erfolge. NICHT 'genau 30', sondern 'der langfristige Durchschnitt ist 30'.",
            "interpretation_en": "With 100 throws at p=0.3, I expect 30 successes on average. NOT 'exactly 30', but 'the long-run average is 30'."
        },
        "variance": {
            "title_de": "Varianz",
            "title_en": "Variance",
            "formula": r"V(X) = n \cdot p \cdot (1-p)",
            "interpretation_de": "Die Streuung ist maximal wenn $p = 0.5$ (maximale Unsicherheit). Bei $p$ nahe 0 oder 1 ist die Varianz klein (fast sicherer Ausgang).",
            "interpretation_en": "The spread is maximum when $p = 0.5$ (maximum uncertainty). When $p$ is near 0 or 1, variance is small (almost certain outcome)."
        },
        "std_dev": {
            "title_de": "Standardabweichung",
            "title_en": "Standard Deviation",
            "formula": r"\sigma = \sqrt{n \cdot p \cdot (1-p)}",
            "interpretation_de": "Hat dieselbe Einheit wie X (Anzahl Erfolge).",
            "interpretation_en": "Has the same unit as X (number of successes)."
        }
    },
    
    # --- RECOGNITION SIGNALS ---
    "signals": {
        "header": {"de": "Signalwörter erkennen", "en": "Recognize Signal Words"},
        "keywords": {
            "trigger_de": ["Anzahl der Erfolge", "wie viele von n", "mindestens k mal", "genau k von n", "mit Zurücklegen", "unabhängige Versuche", "Trefferquote"],
            "trigger_en": ["number of successes", "how many out of n", "at least k times", "exactly k of n", "with replacement", "independent trials", "hit rate"]
        },
        "anti_signals": {
            "header": {"de": "NICHT Binomial wenn:", "en": "NOT Binomial if:"},
            "items": [
                {"de": "'ohne Zurücklegen' → Hypergeometrisch", "en": "'without replacement' → Hypergeometric"},
                {"de": "Keine feste Anzahl n → evtl. Poisson", "en": "No fixed number n → possibly Poisson"},
                {"de": "Versuche abhängig voneinander → anderes Modell", "en": "Trials dependent on each other → different model"}
            ]
        }
    },
    
    # --- WORKED EXAMPLE (Step-by-Step) ---
    "example_worked": {
        "header": {"de": "Schritt-für-Schritt Beispiel", "en": "Step-by-Step Example"},
        "problem": {
            "de": "Bei einer Umfrage antworten **35%** der Leute mit 'Ja'. Du befragst **12 Personen**. Wie wahrscheinlich ist es, dass **genau 5** mit 'Ja' antworten?",
            "en": "In a survey, **35%** of people say 'Yes'. You ask **12 people**. What is the probability that **exactly 5** say 'Yes'?"
        },
        "steps": [
            {
                "label_de": "Gegeben",
                "label_en": "Given",
                "content_de": "$n = 12$ (Anzahl Befragte), $p = 0.35$ (Erfolgswahrscheinlichkeit)",
                "content_en": "$n = 12$ (number surveyed), $p = 0.35$ (success probability)",
                "is_latex": False
            },
            {
                "label_de": "Gesucht",
                "label_en": "Find",
                "latex": r"P(X = 5) \text{ wobei } X \sim \text{Bin}(12, 0.35)",
                "latex_en": r"P(X = 5) \text{ where } X \sim \text{Bin}(12, 0.35)",
                "is_latex": True
            },
            {
                "label_de": "Signal",
                "label_en": "Signal",
                "content_de": "'genau 5 von 12' + unabhängige Befragungen → Binomial",
                "content_en": "'exactly 5 of 12' + independent surveys → Binomial",
                "is_latex": False
            },
            {
                "label_de": "Formel",
                "label_en": "Formula",
                "latex": r"P(X = 5) = \binom{12}{5} \times 0.35^5 \times 0.65^7",
                "is_latex": True
            },
            {
                "label_de": "Rechnung",
                "label_en": "Calculation",
                "latex": r"= 792 \times 0.00525 \times 0.0490 \approx 0.204",
                "is_latex": True
            }
        ],
        "answer": {
            "de": "Die Wahrscheinlichkeit beträgt etwa **20.4%**.",
            "en": "The probability is approximately **20.4%**."
        }
    },
    
    # --- EXAM ESSENTIALS (Merged Trap + Pro Tip) ---
    "exam_essentials": {
        "header": {"de": "Prüfungs-Essentials", "en": "Exam Essentials"},
        "items": [
            {
                "label": {"de": "Falle", "en": "Trap"},
                "title": {"de": "'Mindestens k' ≠ 'genau k'", "en": "'At least k' ≠ 'exactly k'"},
                "formula": r"P(X \geq k) = 1 - P(X < k)",
                "content": {
                    "de": "Oft ist der Umweg über das Komplement schneller!",
                    "en": "Often the detour via complement is faster!"
                },
                "shortcut_label": {"de": "Shortcut", "en": "Shortcut"},
                "shortcut_text": {"de": "Für 'mindestens 1':", "en": "For 'at least 1':"},
                "shortcut_formula": r"P(X \geq 1) = 1 - (1-p)^n",
                "type": "warning"
            },
            {
                "label": {"de": "Regel", "en": "Rule"},
                "title": {"de": "'mit Zurücklegen' = Binomial", "en": "'with replacement' = Binomial"},
                "content": {
                    "de": "Mit Zurücklegen → $p$ bleibt konstant → Binomial.<br>Ohne Zurücklegen → $p$ ändert sich → Hypergeometrisch.",
                    "en": "With replacement → $p$ stays constant → Binomial.<br>Without replacement → $p$ changes → Hypergeometric."
                },
                "type": "tip"
            },
            {
                "label": {"de": "Check", "en": "Check"},
                "title_formula": r"E[X] = n \cdot p",
                "content": {
                    "de": "Schneller Plausibilitäts-Check! $n=100$, $p=0.3$ → erwarte ~30 Erfolge.",
                    "en": "Quick plausibility check! $n=100$, $p=0.3$ → expect ~30 successes."
                },
                "type": "tip"
            }
        ]
    }
}


def render_subtopic_4_3(model):
    """4.3 Binomialverteilung - ULTRATHINK Enhanced"""
    inject_equal_height_css()
    
    # --- CSS INJECTION FOR EQUAL HEIGHT (AGGRESSIVE) ---
    st.markdown("""
    <style>
    /* Force horizontal blocks to stretch children */
    [data-testid="stHorizontalBlock"] {
        align-items: stretch !important;
        display: flex !important;
    }
    
    /* Make columns flex containers that fill height */
    [data-testid="column"], [data-testid="stColumn"] {
        display: flex !important;
        flex-direction: column !important;
        flex: 1 !important;
    }
    
    /* All direct children should expand */
    [data-testid="column"] > div,
    [data-testid="stColumn"] > div {
        flex: 1 !important; 
        display: flex !important;
        flex-direction: column !important;
        height: 100% !important;
        min-height: 100% !important;
    }
    
    /* Target the vertical block inside columns */
    [data-testid="column"] [data-testid="stVerticalBlock"],
    [data-testid="stColumn"] [data-testid="stVerticalBlock"] {
        flex: 1 !important;
        display: flex !important;
        flex-direction: column !important;
        height: 100% !important;
    }
    
    /* Target the border wrapper specifically */
    [data-testid="column"] [data-testid="stVerticalBlockBorderWrapper"],
    [data-testid="stColumn"] [data-testid="stVerticalBlockBorderWrapper"] {
        flex: 1 !important;
        height: 100% !important;
        min-height: 100% !important;
        display: flex !important;
        flex-direction: column !important;
    }
    
    /* And its child */
    [data-testid="stVerticalBlockBorderWrapper"] > div {
        flex: 1 !important;
        height: 100% !important;
    }
    
    /* Also target any container with border=True */
    .stContainer, [data-testid="stContainer"] {
        height: 100% !important;
        flex: 1 !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # --- HEADER ---
    st.header(t(content_4_3["title"]))
    st.caption(t(content_4_3["subtitle"]))
    st.markdown("---")
    
    # --- INTUITION HOOK ---
    st.markdown(f"### {t(content_4_3['intuition']['header'])}")
    with st.container(border=True):
        st.markdown(t(content_4_3["intuition"]["text"]))
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- FRAG DICH: DECISION GUIDE ---
    st.markdown(f"""
    <div style="background-color: rgba(0, 122, 255, 0.08); border-radius: 12px; padding: 20px; border: 2px solid #007AFF;">
        <div style="font-weight: 700; color: #007AFF; margin-bottom: 16px; font-size: 1.1em;">
            {t(content_4_3['frag_dich']['header'])}
        </div>
        <div style="color: #1c1c1e;">
            <ol style="margin: 0; padding-left: 20px; line-height: 2;">
                {"".join([f"<li>{t({'de': q['de'], 'en': q['en']})}</li>" for q in content_4_3['frag_dich']['questions']])}
            </ol>
        </div>
        <div style="margin-top: 16px; padding: 10px; background: #007AFF; color: white; border-radius: 8px; text-align: center; font-weight: 600;">
            {t(content_4_3['frag_dich']['conclusion'])}
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- DEFINITION (With integrated Symbol Ledger - like 4.2) ---
    st.markdown(f"### {t(content_4_3['definition']['header'])}")
    with st.container(border=True):
        st.markdown(t(content_4_3["definition"]["text"]))
        st.markdown("<br>", unsafe_allow_html=True)
        st.latex(content_4_3["definition"]["notation"])
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # --- INTEGRATED SYMBOL LEDGER (inside same container) ---
        decoder = content_4_3["definition"]["variable_decoder"]
        st.markdown(f"**{t(decoder['header'])}**")
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Render each variable using native Streamlit layout for proper LaTeX
        for i, var in enumerate(decoder["variables"]):
            col_sym, col_content = st.columns([1, 4])
            with col_sym:
                st.latex(var['symbol'])
            with col_content:
                st.markdown(f"**{t(var['name'])}**")
                st.markdown(t(var['meaning']), unsafe_allow_html=True)
                st.caption(t(var['example']))
            st.markdown("---")
        
        # Full reading summary at the bottom
        st.markdown(f"""
<div style="background: #f4f4f5; border-radius: 8px; padding: 14px;">
    <div style="color: #3f3f46; line-height: 1.5;">{t(decoder['full_reading'])}</div>
</div>
        """, unsafe_allow_html=True)

    
    # --- THE FORMULA WITH BREAKDOWN ---
    st.markdown(f"### {t(content_4_3['formula']['header'])}")
    with st.container(border=True):
        st.latex(content_4_3["formula"]["pmf"])
        st.caption(t(content_4_3["formula"]["range"]))
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(f"**{t(content_4_3['formula']['breakdown']['header'])}**")
        
        for part in content_4_3["formula"]["breakdown"]["parts"]:
            col_sym, col_mean = st.columns([1, 3])
            with col_sym:
                st.latex(part["symbol"])
            with col_mean:
                st.markdown(t({"de": part["meaning_de"], "en": part["meaning_en"]}), unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        example_text = t(content_4_3["formula"]["breakdown"]["example"])
        st.markdown(f"""
        <div style="background-color: #f4f4f5; border-radius: 8px; padding: 12px; border-left: 4px solid #a1a1aa; color: #3f3f46;">
            {example_text}
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- PARAMETERS WITH MEANING ---
    st.markdown(f"### {t(content_4_3['parameters']['header'])}")
    
    col_n, col_p = st.columns(2, gap="medium")
    
    with col_n:
        with st.container(border=True):
            st.latex(content_4_3["parameters"]["n"]["symbol"])
            st.markdown(f"**{t({'de': content_4_3['parameters']['n']['name_de'], 'en': content_4_3['parameters']['n']['name_en']})}**")
            st.caption(t({"de": content_4_3["parameters"]["n"]["meaning_de"], "en": content_4_3["parameters"]["n"]["meaning_en"]}))
    
    with col_p:
        with st.container(border=True):
            st.latex(content_4_3["parameters"]["p"]["symbol"])
            st.markdown(f"**{t({'de': content_4_3['parameters']['p']['name_de'], 'en': content_4_3['parameters']['p']['name_en']})}**")
            st.caption(t({"de": content_4_3["parameters"]["p"]["meaning_de"], "en": content_4_3["parameters"]["p"]["meaning_en"]}))
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- MOMENTS WITH INTERPRETATION ---
    st.markdown(f"### {t(content_4_3['moments']['header'])}")
    
    col_e, col_v = st.columns(2, gap="medium")
    
    with col_e:
        with st.container(border=True):
            st.markdown(f"**{t({'de': content_4_3['moments']['expectation']['title_de'], 'en': content_4_3['moments']['expectation']['title_en']})}**")
            st.latex(content_4_3["moments"]["expectation"]["formula"])
            st.markdown("---")
            st.markdown(t({"de": content_4_3["moments"]["expectation"]["interpretation_de"], "en": content_4_3["moments"]["expectation"]["interpretation_en"]}))
    
    with col_v:
        with st.container(border=True):
            st.markdown(f"**{t({'de': content_4_3['moments']['variance']['title_de'], 'en': content_4_3['moments']['variance']['title_en']})}**")
            st.latex(content_4_3["moments"]["variance"]["formula"])
            st.markdown("---")
            st.markdown(t({"de": content_4_3["moments"]["variance"]["interpretation_de"], "en": content_4_3["moments"]["variance"]["interpretation_en"]}))
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Standard deviation
    with st.container(border=True):
        col_std_f, col_std_i = st.columns([1, 2])
        with col_std_f:
            st.markdown(f"**{t({'de': content_4_3['moments']['std_dev']['title_de'], 'en': content_4_3['moments']['std_dev']['title_en']})}**")
            st.latex(content_4_3["moments"]["std_dev"]["formula"])
        with col_std_i:
            st.markdown(t({"de": content_4_3["moments"]["std_dev"]["interpretation_de"], "en": content_4_3["moments"]["std_dev"]["interpretation_en"]}))
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- RECOGNITION SIGNALS (UNIFIED CARD) ---
    st.markdown(f"### {t({'de': 'Schnellübersicht: Binomial-Signale', 'en': 'Quick Reference: Binomial Signals'})}")
    
    # Build keywords HTML
    keywords = content_4_3["signals"]["keywords"]["trigger_de"] if t({"de": "x", "en": "y"}) == "x" else content_4_3["signals"]["keywords"]["trigger_en"]
    keywords_html = "".join([f"<span style='background:#dcfce7; padding:5px 12px; border-radius:6px; color:#16a34a; margin:4px; display:inline-block; font-weight:500;'>{kw}</span>" for kw in keywords])
    
    # Build anti-signals HTML
    anti_items_html = "".join([f"<li style='margin-bottom:8px;'>{t({'de': item['de'], 'en': item['en']})}</li>" for item in content_4_3["signals"]["anti_signals"]["items"]])
    
    st.markdown(f"""
    <div style="display: flex; gap: 24px; align-items: stretch;">
        <div style="flex: 1; background: #f9fafb; border-radius: 12px; padding: 20px; border: 1px solid #e5e7eb;">
            <div style="font-weight: 600; color: #16a34a; margin-bottom: 16px; font-size: 0.95em;">
                {t({'de': 'Binomial-Signale', 'en': 'Binomial Signals'})}
            </div>
            <div style="line-height: 2.2;">
                {keywords_html}
            </div>
        </div>
        <div style="flex: 1; background: #f9fafb; border-radius: 12px; padding: 20px; border: 1px solid #e5e7eb;">
            <div style="font-weight: 600; color: #6b7280; margin-bottom: 12px; font-size: 0.95em;">
                {t(content_4_3['signals']['anti_signals']['header'])}
            </div>
            <ul style="margin: 0; padding-left: 20px; color: #374151; line-height: 1.8;">
                {anti_items_html}
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- WORKED EXAMPLE ---
    st.markdown(f"### {t(content_4_3['example_worked']['header'])}")
    with st.container(border=True):
        
        # Problem statement
        st.markdown(f"""
        <div style="background:#fafafa; border-radius:8px; padding:12px; margin-bottom:16px;">
            {t(content_4_3['example_worked']['problem'])}
        </div>
        """, unsafe_allow_html=True)
        
        # Steps with color coding
        for step in content_4_3["example_worked"]["steps"]:
            label = t({"de": step["label_de"], "en": step["label_en"]})
            is_latex = step.get("is_latex", False)
            
            # Color based on step type
            if "Gegeben" in label or "Given" in label:
                bg = "#dbeafe"; color = "#1d4ed8"
            elif "Gesucht" in label or "Find" in label:
                bg = "#fee2e2"; color = "#dc2626"
            elif "Signal" in label:
                bg = "#dcfce7"; color = "#16a34a"
            else:
                bg = "#f4f4f5"; color = "#3f3f46"
            
            # Render the step
            col_label, col_content = st.columns([1, 4])
            with col_label:
                st.markdown(f"""
                <div style="background:{bg}; padding:6px 12px; border-radius:6px; color:{color}; font-weight:600; text-align:center; margin-top:8px;">
                    {label}
                </div>
                """, unsafe_allow_html=True)
            
            with col_content:
                if is_latex:
                    # Use latex_en if available and language is English
                    if "latex_en" in step and t({"de": "x", "en": "y"}) == "y":
                        st.latex(step["latex_en"])
                    else:
                        st.latex(step["latex"])
                else:
                    content = t({"de": step["content_de"], "en": step["content_en"]})
                    st.markdown(content)
        
        st.markdown("---")
        st.markdown(f"**{t(content_4_3['example_worked']['answer'])}**")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- EXAM ESSENTIALS (With LaTeX) ---
    st.markdown(f"### {t(content_4_3['exam_essentials']['header'])}")
    with st.container(border=True):
        for item in content_4_3["exam_essentials"]["items"]:
            st.markdown("---")
            
            # Title - either text or LaTeX formula
            if "title_formula" in item:
                st.latex(item["title_formula"])
            elif "title" in item:
                st.markdown(f"**{t(item['title'])}**")
            
            # Main formula (if present)
            if "formula" in item:
                st.latex(item["formula"])
            
            # Content text
            st.markdown(t(item['content']), unsafe_allow_html=True)
            
            # Shortcut section (if present)
            if "shortcut_formula" in item:
                st.markdown(f"*{t(item['shortcut_label'])}: {t(item['shortcut_text'])}*")
                st.latex(item["shortcut_formula"])
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- EXAM SECTION ---
    st.markdown(f"### {t({'de': 'Prüfungstraining', 'en': 'Exam Practice'})}")
    
    # MCQ 1: uebung2_giro
    q1 = get_question("4.3", "uebung2_giro")
    if q1:
        with st.container(border=True):
            st.caption(q1.get("source", ""))
            opts = q1.get("options", [])
            if opts and isinstance(opts[0], dict):
                option_labels = [t(o) for o in opts]
            else:
                option_labels = opts
            
            render_mcq(
                key_suffix="4_3_giro",
                question_text=t(q1["question"]),
                options=option_labels,
                correct_idx=q1["correct_idx"],
                solution_text_dict=q1["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
                client=model,
                ai_context="Binomial distribution - at least k successes",
                course_id="vwl",
                topic_id="4",
                subtopic_id="4.3",
                question_id="4_3_giro"
            )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # MCQ 2: hs2022_mc7
    q2 = get_question("4.3", "hs2022_mc7")
    if q2:
        with st.container(border=True):
            st.caption(q2.get("source", ""))
            opts = q2.get("options", [])
            if opts and isinstance(opts[0], dict):
                option_labels = [t(o) for o in opts]
            else:
                option_labels = opts
            
            render_mcq(
                key_suffix="4_3_rain",
                question_text=t(q2["question"]),
                options=option_labels,
                correct_idx=q2["correct_idx"],
                solution_text_dict=q2["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
                client=model,
                ai_context="Binomial distribution - weather probability",
                course_id="vwl",
                topic_id="4",
                subtopic_id="4.3",
                question_id="4_3_rain"
            )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # MCQ 3: hs2023_mc12
    q3 = get_question("4.3", "hs2023_mc12")
    if q3:
        with st.container(border=True):
            st.caption(q3.get("source", ""))
            opts = q3.get("options", [])
            if opts and isinstance(opts[0], dict):
                option_labels = [t(o) for o in opts]
            else:
                option_labels = opts
            
            render_mcq(
                key_suffix="4_3_casino",
                question_text=t(q3["question"]),
                options=option_labels,
                correct_idx=q3["correct_idx"],
                solution_text_dict=q3["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
                client=model,
                ai_context="Binomial distribution - two-stage problem",
                course_id="vwl",
                topic_id="4",
                subtopic_id="4.3",
                question_id="4_3_casino"
            )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # MCQ 4: hs2022_mc6
    q4 = get_question("4.3", "hs2022_mc6")
    if q4:
        with st.container(border=True):
            st.caption(q4.get("source", ""))
            opts = q4.get("options", [])
            if opts and isinstance(opts[0], dict):
                option_labels = [t(o) for o in opts]
            else:
                option_labels = opts
            
            render_mcq(
                key_suffix="4_3_rain_2",
                question_text=t(q4["question"]),
                options=option_labels,
                correct_idx=q4["correct_idx"],
                solution_text_dict=q4["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
                client=model,
                ai_context="Binomial probability",
                course_id="vwl",
                topic_id="4",
                subtopic_id="4.3",
                question_id="4_3_rain_2"
            )
