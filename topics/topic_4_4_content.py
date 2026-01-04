# Topic 4.4: Poisson Distribution - Poisson-Verteilung
# ULTRATHINK ENHANCED VERSION
import streamlit as st
from views.styles import inject_equal_height_css
import re
from utils.localization import t
from utils.layouts.foundation import grey_info
from utils.quiz_helper import render_mcq
from data.exam_questions import get_question
import numpy as np
import plotly.graph_objects as go
from scipy.stats import poisson

# ==========================================
# 1. CONTENT DICTIONARY - BILINGUAL (ULTRATHINK)
# ==========================================
content_4_4 = {
    "title": {"de": "4.4 Poisson-Verteilung (diskret)", "en": "4.4 Poisson Distribution (Discrete)"},
    "subtitle": {
        "de": "Seltene Ereignisse in grossen Zeiträumen",
        "en": "Rare Events Over Large Time Periods"
    },
    
    # --- INTUITION HOOK ---
    "intuition": {
        "header": {"de": "Die Intuition", "en": "The Intuition"},
        "text": {
            "de": "Wie viele **Tore** fallen in einem Fussballspiel? Wie viele **Kunden** betreten den Laden pro Stunde? Wie viele **Serverabstürze** passieren pro Monat? Diese Ereignisse haben eines gemeinsam: Sie sind **selten** (verglichen mit allen möglichen Zeitpunkten), aber sie passieren mit einer gewissen **durchschnittlichen Rate** $\\lambda$.",
            "en": "How many **goals** are scored in a soccer match? How many **customers** enter the store per hour? How many **server crashes** happen per month? These events have something in common: They are **rare** (compared to all possible moments), but they happen at some **average rate** $\\lambda$."
        }
    },
    
    # --- FRAG DICH (Decision Guide) ---
    "frag_dich": {
        "header": {"de": "Frag dich: Ist es Poisson?", "en": "Ask yourself: Is it Poisson?"},
        "questions": [
            {"de": "Zähle ich Ereignisse <strong>pro Zeiteinheit/Fläche</strong>?", "en": "Am I counting events <strong>per time unit/area</strong>?"},
            {"de": "Sind die Ereignisse <strong>selten</strong> (viele Möglichkeiten, wenig Realisierungen)?", "en": "Are the events <strong>rare</strong> (many opportunities, few occurrences)?"},
            {"de": "Gibt es eine bekannte <strong>durchschnittliche Rate</strong> λ?", "en": "Is there a known <strong>average rate</strong> λ?"},
            {"de": "Sind die Ereignisse <strong>unabhängig</strong> voneinander?", "en": "Are the events <strong>independent</strong> of each other?"}
        ],
        "conclusion": {
            "de": "4× Ja → Poisson-Verteilung anwenden!",
            "en": "4× Yes → Apply Poisson Distribution!"
        }
    },
    
    # --- DEFINITION ---
    "definition": {
        "header": {"de": "Definition", "en": "Definition"},
        "text": {
            "de": "Eine Zufallsvariable $X$ mit abzählbar unendlich vielen Werten ($x = 0, 1, 2, 3, \\ldots$) heisst **Poisson-verteilt** mit Parameter $\\lambda > 0$.",
            "en": "A random variable $X$ with countably infinite values ($x = 0, 1, 2, 3, \\ldots$) is called **Poisson distributed** with parameter $\\lambda > 0$."
        },
        "notation": r"X \sim \text{Poi}(\lambda)"
    },
    
    # --- THE FORMULA (With Breakdown) ---
    "formula": {
        "header": {"de": "Die Massenfunktion", "en": "The Mass Function"},
        "pmf": r"f_{\text{Po}}(x; \lambda) = \frac{\lambda^x \cdot e^{-\lambda}}{x!}",
        "range": {"de": "x = 0, 1, 2, 3, ... (beliebig viele Ereignisse möglich)", "en": "x = 0, 1, 2, 3, ... (any number of events possible)"},
        "breakdown": {
            "header": {"de": "Was bedeutet jeder Teil? (Intuition!)", "en": "What does each part mean? (Intuition!)"},
            "parts": [
                {
                    "symbol": r"\lambda^x",
                    "meaning_de": "<strong>Warum λ hoch x?</strong> Stell dir vor, du erwartest λ = 4 Anrufe/Stunde. Die Chance, dass das erste Ereignis passiert, hängt von λ ab, das zweite auch, usw. Bei x Ereignissen: λ × λ × ... × λ = λ<sup>x</sup>. Je mehr Ereignisse du willst, desto höher muss die Rate 'zusammenwirken'.",
                    "meaning_en": "<strong>Why λ to the power x?</strong> Imagine you expect λ = 4 calls/hour. The chance of the first event depends on λ, the second too, etc. For x events: λ × λ × ... × λ = λ<sup>x</sup>. The more events you want, the more the rate has to 'cooperate'."
                },
                {
                    "symbol": r"e^{-\lambda}",
                    "meaning_de": "<strong>Warum e<sup>-λ</sup>?</strong> Das ist die Wahrscheinlichkeit, dass KEIN Ereignis passiert (P(X=0) = e<sup>-λ</sup>). Es ist der 'Grundpreis' — je höher λ, desto unwahrscheinlicher, dass nichts passiert. Es sorgt auch dafür, dass alle Wahrscheinlichkeiten zusammen = 1 ergeben.",
                    "meaning_en": "<strong>Why e<sup>-λ</sup>?</strong> This is the probability that NO event happens (P(X=0) = e<sup>-λ</sup>). It's the 'base price' — the higher λ, the less likely nothing happens. It also ensures all probabilities sum to 1."
                },
                {
                    "symbol": r"x!",
                    "meaning_de": "<strong>Warum x! im Nenner?</strong> Die Ereignisse passieren in beliebiger Reihenfolge. Anruf A um 10:15, B um 10:30 ist dasselbe wie B um 10:15, A um 10:30. Bei x Ereignissen gibt es x! Reihenfolgen — wir teilen durch x!, um nicht mehrfach zu zählen.",
                    "meaning_en": "<strong>Why x! in denominator?</strong> Events happen in any order. Call A at 10:15, B at 10:30 is the same as B at 10:15, A at 10:30. With x events there are x! orderings — we divide by x! to avoid counting multiple times."
                }
            ]
        }
    },
    
    # --- PARAMETER WITH MEANING ---
    "parameter": {
        "header": {"de": "Der Parameter", "en": "The Parameter"},
        "symbol": r"\lambda > 0",
        "name_de": "Erwartete Ereignisrate",
        "name_en": "Expected Event Rate",
        "meaning_de": "Wie viele Ereignisse erwarte ich **durchschnittlich** pro Zeiteinheit/Fläche? Das ist gleichzeitig Erwartungswert UND Varianz!",
        "meaning_en": "How many events do I expect **on average** per time unit/area? This is BOTH expected value AND variance!"
    },
    
    # --- MOMENTS WITH INTERPRETATION (THE KEY INSIGHT) ---
    "moments": {
        "header": {"de": "Erwartungswert & Varianz", "en": "Expected Value & Variance"},
        "key_property": {
            "header": {"de": "DIE Schlüsseleigenschaft", "en": "THE Key Property"},
            "text": {
                "de": "Bei der Poisson-Verteilung sind Erwartungswert und Varianz **identisch**! Das ist einzigartig und ein sofortiges Erkennungszeichen.",
                "en": "For the Poisson distribution, expected value and variance are **identical**! This is unique and an immediate recognition sign."
            }
        },
        "expectation": {
            "title_de": "Erwartungswert",
            "title_en": "Expected Value",
            "formula": r"E[X] = \lambda",
            "interpretation_de": "Die durchschnittliche Anzahl von Ereignissen. Bei $\\lambda = 5$ erwarte ich im Schnitt 5 Ereignisse pro Zeiteinheit.",
            "interpretation_en": "The average number of events. With $\\lambda = 5$, I expect 5 events on average per time unit."
        },
        "variance": {
            "title_de": "Varianz",
            "title_en": "Variance",
            "formula": r"V(X) = \lambda",
            "interpretation_de": "Die Streuung wächst MIT der Rate! Mehr erwartete Ereignisse = mehr Variabilität.",
            "interpretation_en": "The spread grows WITH the rate! More expected events = more variability."
        }
    },
    
    # --- APPROXIMATION (Binomial → Poisson) ---
    "approximation": {
        "header": {"de": "Binomial-Approximation", "en": "Binomial Approximation"},
        "when": {
            "de": "Wann verwenden? Wenn Binomial(n, p) mit: $n \\geq 100$ und $p \\leq 0.05$ (oft auch $n \\cdot p \\leq 10$)",
            "en": "When to use? When Binomial(n, p) with: $n \\geq 100$ and $p \\leq 0.05$ (often also $n \\cdot p \\leq 10$)"
        },
        "formula": r"\text{Bin}(n, p) \approx \text{Poi}(\lambda) \quad \text{mit } \lambda = n \cdot p",
        "why": {
            "de": "Warum? Die Binomialformel mit grossen $n$ ist rechnerisch mühsam. Poisson ist einfacher!",
            "en": "Why? The binomial formula with large $n$ is computationally tedious. Poisson is simpler!"
        }
    },
    
    # --- WORKED EXAMPLE ---
    "example_worked": {
        "header": {"de": "Schritt-für-Schritt Beispiel", "en": "Step-by-Step Example"},
        "problem": {
            "de": "Ein Callcenter erhält **durchschnittlich 4 Anrufe pro Minute**. Wie wahrscheinlich ist es, dass in einer Minute **genau 6 Anrufe** eingehen?",
            "en": "A call center receives **on average 4 calls per minute**. What is the probability that **exactly 6 calls** arrive in one minute?"
        },
        "steps": [
            {
                "label": {"de": "Gegeben", "en": "Given"},
                "latex": r"{\color{#007AFF}\lambda = 4}",
                "note": {"de": "(Rate pro Minute)", "en": "(rate per minute)"}
            },
            {
                "label": {"de": "Gesucht", "en": "Find"},
                "latex": r"P(X = {\color{#FF4B4B}6}) \text{ wobei } X \sim \text{Poi}({\color{#007AFF}4})",
                "latex_en": r"P(X = {\color{#FF4B4B}6}) \text{ where } X \sim \text{Poi}({\color{#007AFF}4})",
                "note": None
            },
            {
                "label": {"de": "Formel", "en": "Formula"},
                "latex": r"P(X = {\color{#FF4B4B}6}) = \frac{{\color{#007AFF}4}^{\color{#FF4B4B}6} \cdot e^{-{\color{#007AFF}4}}}{{\color{#FF4B4B}6}!}",
                "note": {"de": "λ^x · e^(-λ) / x!", "en": "λ^x · e^(-λ) / x!"}
            },
            {
                "label": {"de": "Rechnung", "en": "Calculation"},
                "latex": r"= \frac{4096 \cdot 0.0183}{720} \approx \mathbf{0.104}",
                "note": None
            }
        ],
        "answer": {
            "de": "Die Wahrscheinlichkeit beträgt etwa **10.4%**.",
            "en": "The probability is approximately **10.4%**."
        }
    },
    
    # --- RECOGNITION SIGNALS ---
    "signals": {
        "header": {"de": "Signalwörter erkennen", "en": "Recognize Signal Words"},
        "keywords": {
            "trigger_de": ["pro Stunde/Tag/Monat/Jahr", "durchschnittlich X pro...", "Rate", "seltene Ereignisse", "Anzahl der Unfälle/Anrufe/Kunden"],
            "trigger_en": ["per hour/day/month/year", "on average X per...", "rate", "rare events", "number of accidents/calls/customers"]
        },
        "vs_binomial": {
            "header": {"de": "Poisson vs. Binomial", "en": "Poisson vs. Binomial"},
            "items": [
                {"de": "<strong>Poisson</strong>: Feste ZEIT, variable Anzahl", "en": "<strong>Poisson</strong>: Fixed TIME, variable count"},
                {"de": "<strong>Binomial</strong>: Feste VERSUCHE, zähle Erfolge", "en": "<strong>Binomial</strong>: Fixed TRIALS, count successes"}
            ]
        }
    },
    
    # --- EXAM ESSENTIALS (Merged Trap + Pro Tip) ---
    "exam_essentials": {
        "header": {"de": "Prüfungs-Essentials", "en": "Exam Essentials"},
        "trap": {
            "de": "Zeitintervall-Anpassung vergessen! Wenn λ = 2 pro Stunde, aber du fragst nach 30 Minuten, dann ist λ₃₀min = 1.",
            "en": "Forgetting time interval adjustment! If λ = 2 per hour but you're asking about 30 minutes, then λ₃₀min = 1."
        },
        "trap_rule": {
            "de": "λ skaliert linear mit der Zeit/Fläche!",
            "en": "λ scales linearly with time/area!"
        },
        "tips": [
            {
                "tip": {"de": "Wenn E[X] = V(X) gegeben → sofort Poisson!", "en": "If E[X] = V(X) is given → immediately Poisson!"},
                "why": {"de": "EINZIGE Verteilung wo Erwartungswert = Varianz = λ. Wenn du das siehst, ist die Verteilung bereits identifiziert!", "en": "ONLY distribution where expected value = variance = λ. When you see this, the distribution is already identified!"}
            },
            {
                "tip": {"de": "λ immer an Zeitintervall anpassen", "en": "Always adjust λ to time interval"},
                "why": {"de": "λ = 2 pro Stunde aber du fragst nach 30 Minuten? Dann λ₃₀min = 1. Vergiss nie die Umrechnung!", "en": "λ = 2 per hour but asking about 30 minutes? Then λ₃₀min = 1. Never forget to convert!"}
            },
            {
                "tip": {"de": "Poisson approximiert Binomial wenn n gross und p klein", "en": "Poisson approximates Binomial when n large and p small"},
                "why": {"de": "Faustregel: n > 30 und p < 0.05 → nutze Poisson mit λ = n·p. Spart Rechenaufwand!", "en": "Rule of thumb: n > 30 and p < 0.05 → use Poisson with λ = n·p. Saves computation!"}
            },
            {
                "tip": {"de": "P(X = 0) = e⁻λ auswendig!", "en": "Memorize P(X = 0) = e⁻λ!"},
                "why": {"de": "'Kein Anruf in einer Stunde?' Diese Frage kommt oft. e⁻λ direkt anwenden spart Zeit.", "en": "'No call in an hour?' This question comes up often. Apply e⁻λ directly to save time."}
            }
        ]
    }
}


def render_subtopic_4_4(model):
    """4.4 Poisson-Verteilung - ULTRATHINK Enhanced"""
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
    st.header(t(content_4_4["title"]))
    st.caption(t(content_4_4["subtitle"]))
    st.markdown("---")
    
    # --- INTUITION HOOK ---
    st.markdown(f"### {t(content_4_4['intuition']['header'])}")
    with st.container(border=True):
        st.markdown(t(content_4_4["intuition"]["text"]))
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- FRAG DICH: DECISION GUIDE ---
    from utils.ask_yourself import render_ask_yourself
    render_ask_yourself(
        header=content_4_4['frag_dich']['header'],
        questions=content_4_4['frag_dich']['questions'],
        conclusion=content_4_4['frag_dich']['conclusion']
    )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- DEFINITION ---
    st.markdown(f"### {t(content_4_4['definition']['header'])}")
    with st.container(border=True):
        st.markdown(t(content_4_4["definition"]["text"]))
        st.markdown("<br>", unsafe_allow_html=True)
        st.latex(content_4_4["definition"]["notation"])
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- THE FORMULA WITH BREAKDOWN ---
    st.markdown(f"### {t(content_4_4['formula']['header'])}")
    with st.container(border=True):
        st.latex(content_4_4["formula"]["pmf"])
        st.caption(t(content_4_4["formula"]["range"]))
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(f"**{t(content_4_4['formula']['breakdown']['header'])}**")
        
        for i, part in enumerate(content_4_4["formula"]["breakdown"]["parts"]):
            if i > 0:
                st.markdown("---")
            col_sym, col_mean = st.columns([1, 3])
            with col_sym:
                st.latex(part["symbol"])
            with col_mean:
                st.markdown(t({"de": part["meaning_de"], "en": part["meaning_en"]}), unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- PARAMETER WITH MEANING ---
    st.markdown(f"### {t(content_4_4['parameter']['header'])}")
    with st.container(border=True):
        col_sym, col_desc = st.columns([1, 3])
        with col_sym:
            st.latex(content_4_4["parameter"]["symbol"])
        with col_desc:
            st.markdown(f"**{t({'de': content_4_4['parameter']['name_de'], 'en': content_4_4['parameter']['name_en']})}**")
            st.caption(t({"de": content_4_4["parameter"]["meaning_de"], "en": content_4_4["parameter"]["meaning_en"]}))
    
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- MOMENTS WITH INTERPRETATION ---
    st.markdown(f"### {t(content_4_4['moments']['header'])}")
    
    col_e, col_v = st.columns(2, gap="medium")
    
    with col_e:
        with st.container(border=True):
            st.markdown(f"**{t({'de': content_4_4['moments']['expectation']['title_de'], 'en': content_4_4['moments']['expectation']['title_en']})}**")
            st.latex(content_4_4["moments"]["expectation"]["formula"])
            st.markdown("---")
            st.markdown(t({"de": content_4_4["moments"]["expectation"]["interpretation_de"], "en": content_4_4["moments"]["expectation"]["interpretation_en"]}))
    
    with col_v:
        with st.container(border=True):
            st.markdown(f"**{t({'de': content_4_4['moments']['variance']['title_de'], 'en': content_4_4['moments']['variance']['title_en']})}**")
            st.latex(content_4_4["moments"]["variance"]["formula"])
            st.markdown("---")
            st.markdown(t({"de": content_4_4["moments"]["variance"]["interpretation_de"], "en": content_4_4["moments"]["variance"]["interpretation_en"]}))
    
    # Add Key Property note inline (zinc neutral styling)
    st.markdown(f"""
<div style="background-color: #f4f4f5; border-radius: 8px; padding: 12px; margin-top: 12px;">
    <strong style="color: #3f3f46;">{t(content_4_4['moments']['key_property']['header'])}:</strong>
    <span style="color: #52525b;">{t(content_4_4['moments']['key_property']['text'])}</span>
</div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- APPROXIMATION ---
    st.markdown(f"### {t(content_4_4['approximation']['header'])}")
    with st.container(border=True):
        st.markdown(t(content_4_4["approximation"]["when"]))
        st.latex(content_4_4["approximation"]["formula"])
        st.markdown(t(content_4_4["approximation"]["why"]))
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- WORKED EXAMPLE ---
    st.markdown(f"### {t(content_4_4['example_worked']['header'])}")
    with st.container(border=True):
        
        st.markdown(t(content_4_4['example_worked']['problem']), unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Steps with proper LaTeX and plain labels
        for i, step in enumerate(content_4_4["example_worked"]["steps"]):
            if i > 0:
                st.markdown("---")
            
            st.markdown(f"**{t(step['label'])}:**")
            
            # Use latex_en if available and language is English
            if "latex_en" in step and t({"de": "x", "en": "y"}) == "y":
                st.latex(step["latex_en"])
            else:
                st.latex(step["latex"])
            
            if step.get("note"):
                st.caption(t(step["note"]))
        
        st.markdown("---")
        st.markdown(f"**{t(content_4_4['example_worked']['answer'])}**")
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- INTERACTIVE MISSION: POISSON DISCOVERY ---
    st.markdown(f"### {t({'de': 'Mission: Die Poisson-Entdeckung', 'en': 'Mission: The Poisson Discovery'})}")
    
    # Mission state initialization
    if "poisson_mission_done" not in st.session_state:
        st.session_state.poisson_mission_done = False
    
    with st.container(border=True):
        # REAL-WORLD SCENARIO
        st.markdown(f"""
<div style="background: rgba(0, 122, 255, 0.08); padding:14px; border-radius:8px; color:#1c1c1e; margin-bottom:12px; border-left: 4px solid #007AFF;">
<strong>{t({'de': 'Szenario:', 'en': 'Scenario:'})}</strong> {t({'de': 'Eine Notaufnahme plant die Schichtbesetzung. Sie müssen wissen: Ab welcher durchschnittlichen Ankunftsrate (λ) ist es fast sicher, dass mindestens ein Patient pro Stunde kommt?', 'en': 'An emergency room is planning shift coverage. They need to know: At what average arrival rate (λ) is it almost certain that at least one patient arrives per hour?'})}
</div>""", unsafe_allow_html=True)
        
        # THE MISSION GOAL
        target_p0 = 0.05
        st.markdown(f"""
<div style="background:#f4f4f5; padding:16px; border-radius:8px; color:#3f3f46; border-left: 4px solid #a1a1aa;">
<strong>{t({'de': 'Deine Aufgabe:', 'en': 'Your Mission:'})}</strong> {t({'de': f'Finde den λ-Wert, bei dem P(X=0) unter {target_p0*100:.0f}% fällt!', 'en': f'Find the λ value where P(X=0) drops below {target_p0*100:.0f}%!'})}
</div>""", unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        col_ctrl, col_chart = st.columns([1.2, 2.3], gap="large")
        
        with col_ctrl:
            lam = st.slider("λ", min_value=0.5, max_value=8.0, value=1.0, step=0.5, key="poisson_lambda")
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            # Calculate probabilities
            p0 = poisson.pmf(0, lam)
            goal_reached = p0 < target_p0
            
            # Semantic colored formula display
            p0_color = "#34C759" if goal_reached else "#FF4B4B"
            st.markdown(f"""
<div style="font-size: 1.1em;">
<strong>P(X=0)</strong> = e<sup>-λ</sup> = e<sup>-{lam:.1f}</sup> = <span style="color:{p0_color}; font-weight:bold;">{p0:.3f}</span>
</div>""", unsafe_allow_html=True)
            
            # Progress feedback
            st.markdown("<br>", unsafe_allow_html=True)
            if p0 >= 0.20:
                grey_info(t({"de": "λ ist noch klein. Die Wahrscheinlichkeit für 0 Ereignisse ist hoch.", "en": "λ is still small. Probability of 0 events is high."}))
            elif p0 >= target_p0:
                st.warning(t({"de": f"Fast da! P(X=0) = {p0:.1%} — noch etwas höher mit λ!", "en": f"Almost there! P(X=0) = {p0:.1%} — push λ a bit higher!"}))
            else:
                if not st.session_state.poisson_mission_done:
                    st.balloons()
                    st.session_state.poisson_mission_done = True
                    # Track progress
                    from utils.progress_tracker import track_question_answer
                    if user := st.session_state.get("user"):
                        track_question_answer(user["localId"], "vwl", "4", "4.4", "poisson_mission", True)
                
                st.success(t({"de": f"Mission erfüllt! Bei λ = {lam:.1f} ist P(X=0) = {p0:.1%} < 5%", "en": f"Mission Complete! At λ = {lam:.1f}, P(X=0) = {p0:.1%} < 5%"}))
            
            # Additional insights
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown(f"**E[X] = Var(X) = <span style='color:#007AFF;'>{lam:.1f}</span>**", unsafe_allow_html=True)
        
        with col_chart:
            x_vals = np.arange(0, int(lam * 2.5) + 5)
            y_vals = poisson.pmf(x_vals, lam)
            
            # Color bars: highlight x=0 differently
            bar_colors = ['#FF4B4B' if x == 0 else '#007AFF' for x in x_vals]
            
            fig = go.Figure()
            fig.add_trace(go.Bar(
                x=x_vals, y=y_vals,
                marker_color=bar_colors,
                hovertemplate='x=%{x}<br>P(X=x)=%{y:.4f}<extra></extra>'
            ))
            
            # Mark the mean
            fig.add_vline(x=lam, line_dash="dash", line_color="#34C759", line_width=2,
                         annotation_text=f"μ=λ={lam}", annotation_position="top")
            
            # Target line for P(X=0)
            fig.add_hline(y=target_p0, line_dash="dot", line_color="#a1a1aa", line_width=1,
                         annotation_text="5% Target", annotation_position="right")
            
            fig.update_layout(
                xaxis=dict(title="x", fixedrange=True, showgrid=False),
                yaxis=dict(title="P(X=x)", fixedrange=True, showgrid=True, gridcolor='#E5E5EA'),
                height=300,
                margin=dict(l=40, r=20, t=30, b=50),
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                showlegend=False
            )
            
            st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
        
        # Mastery insight (shown after completion)
        if goal_reached:
            st.markdown(f"""
<div style="background:#f4f4f5; padding:16px; border-radius:8px; color:#3f3f46; margin-top:12px; border-left: 4px solid #a1a1aa;">
<strong>{t({'de': 'Was du entdeckt hast:', 'en': 'What you discovered:'})}</strong> {t({'de': 'Bei höherem λ (mehr erwartete Ereignisse) wird "0 Ereignisse" immer unwahrscheinlicher. Die Formel P(X=0) = e^(-λ) fällt exponentiell!', 'en': 'With higher λ (more expected events), "0 events" becomes increasingly unlikely. The formula P(X=0) = e^(-λ) falls exponentially!'})}
</div>""", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- RECOGNITION SIGNALS (UNIFIED CARD) ---
    st.markdown(f"### {t({'de': 'Schnellübersicht: Poisson-Signale', 'en': 'Quick Reference: Poisson Signals'})}")
    
    # Build keywords HTML
    lang = "trigger_de" if t({"de": "x", "en": "y"}) == "x" else "trigger_en"
    keywords = content_4_4["signals"]["keywords"][lang]
    keywords_html = "".join([f"<span style='background:#dcfce7; padding:5px 12px; border-radius:6px; color:#16a34a; margin:4px; display:inline-block; font-weight:500;'>{kw}</span>" for kw in keywords])
    
    # Build vs-binomial HTML (properly render the <strong> tags)
    vs_items_html = "".join([f"<li style='margin-bottom:10px;'>{t({'de': item['de'], 'en': item['en']})}</li>" for item in content_4_4["signals"]["vs_binomial"]["items"]])
    
    st.markdown(f"""
    <div style="display: flex; gap: 24px; align-items: stretch;">
        <div style="flex: 1; background: #f9fafb; border-radius: 12px; padding: 20px; border: 1px solid #e5e7eb;">
            <div style="font-weight: 600; color: #16a34a; margin-bottom: 16px; font-size: 0.95em;">
                {t({'de': 'Poisson-Signale', 'en': 'Poisson Signals'})}
            </div>
            <div style="line-height: 2.2;">
                {keywords_html}
            </div>
        </div>
        <div style="flex: 1; background: #f9fafb; border-radius: 12px; padding: 20px; border: 1px solid #e5e7eb;">
            <div style="font-weight: 600; color: #6b7280; margin-bottom: 12px; font-size: 0.95em;">
                {t(content_4_4['signals']['vs_binomial']['header'])}
            </div>
            <ul style="margin: 0; padding-left: 20px; color: #374151; line-height: 1.8;">
                {vs_items_html}
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- EXAM ESSENTIALS ---
    from utils.exam_essentials import render_exam_essentials
    render_exam_essentials(
        trap=content_4_4["exam_essentials"]["trap"],
        trap_rule=content_4_4["exam_essentials"]["trap_rule"],
        tips=content_4_4["exam_essentials"]["tips"]
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- EXAM SECTION ---
    st.markdown(f"### {t({'de': 'Prüfungstraining', 'en': 'Exam Practice'})}")
    
    q_data = get_question("4.4", "poisson_rate")
    if q_data:
        with st.container(border=True):
            st.caption(q_data.get("source", ""))
            opts = q_data.get("options", [])
            if opts and isinstance(opts[0], dict):
                option_labels = [t(o) for o in opts]
            else:
                option_labels = opts
            
            render_mcq(
                key_suffix="4_4_poisson",
                question_text=t(q_data["question"]),
                options=option_labels,
                correct_idx=q_data["correct_idx"],
                solution_text_dict=q_data["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
                client=model,
                ai_context="Poisson distribution",
                course_id="vwl",
                topic_id="4",
                subtopic_id="4.4",
                question_id="4_4_poisson"
            )
    else:
        with st.container(border=True):
            st.markdown(f"""
<div style="background: #f4f4f5; border-left: 4px solid #a1a1aa; padding: 12px 16px; border-radius: 8px; color: #3f3f46;">
{t({"de": "Für diesen Abschnitt gibt es derzeit keine MCQ-Fragen. Die Theorie oben deckt die Prüfungsinhalte ab.", "en": "This section currently has no MCQ questions. The theory above covers the exam content."})}
</div>
""", unsafe_allow_html=True)
