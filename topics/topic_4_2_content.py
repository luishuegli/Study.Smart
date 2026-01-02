# Topic 4.2: Bernoulli Distribution - Bernoulli-Verteilung
# ULTRATHINK ENHANCED VERSION - Fixed HTML rendering + enriched content
import streamlit as st
from utils.localization import t
from utils.quiz_helper import render_mcq
from data.exam_questions import get_question

# ==========================================
# 1. CONTENT DICTIONARY - BILINGUAL
# ==========================================
content_4_2 = {
    "title": {"de": "4.2 Bernoulli-Verteilung (diskret)", "en": "4.2 Bernoulli Distribution (Discrete)"},
    "subtitle": {
        "de": "Der fundamentale Baustein: Erfolg oder Misserfolg",
        "en": "The Fundamental Building Block: Success or Failure"
    },
    
    # --- INTUITION HOOK ---
    "intuition": {
        "header": {"de": "Die Intuition", "en": "The Intuition"},
        "text": {
            "de": "Stell dir einen <strong>einzelnen Münzwurf</strong> vor. Es gibt nur zwei Ausgänge: Kopf (Erfolg) oder Zahl (Misserfolg). Die Bernoulli-Verteilung modelliert genau diese Situation — <strong>ein einzelnes Experiment mit zwei möglichen Ergebnissen</strong>. Sie ist der Grundbaustein, aus dem die Binomialverteilung entsteht.",
            "en": "Imagine a <strong>single coin flip</strong>. There are only two outcomes: Heads (success) or Tails (failure). The Bernoulli distribution models exactly this situation — <strong>a single experiment with two possible outcomes</strong>. It's the building block from which the Binomial distribution arises."
        }
    },
    
    # --- FRAG DICH (Decision Guide) - Using HTML strong tags ---
    "frag_dich": {
        "header": {"de": "Frag dich: Ist es Bernoulli?", "en": "Ask yourself: Is it Bernoulli?"},
        "questions": [
            {"de": "Gibt es genau <strong>2 mögliche Ausgänge</strong>?", "en": "Are there exactly <strong>2 possible outcomes</strong>?"},
            {"de": "Ist es ein <strong>einzelner</strong> Versuch (nicht wiederholt)?", "en": "Is it a <strong>single</strong> trial (not repeated)?"},
            {"de": "Kann ich einen Ausgang als <strong>Erfolg (1)</strong> definieren?", "en": "Can I define one outcome as <strong>success (1)</strong>?"}
        ],
        "conclusion": {
            "de": "Alles Ja → Bernoulli-Verteilung!",
            "en": "All Yes → Bernoulli Distribution!"
        }
    },
    
    # --- WHAT IS A BERNOULLI EXPERIMENT ---
    "bernoulli_experiment": {
        "header": {"de": "Was ist ein Bernoulli-Experiment?", "en": "What is a Bernoulli Experiment?"},
        "text": {
            "de": "Ein <strong>Bernoulli-Experiment</strong> ist ein Zufallsexperiment mit genau <strong>zwei Ausgängen</strong>: Ereignis $A$ (Erfolg) und $\\bar{A}$ (Misserfolg). Das Ereignis $A$ tritt mit einer bestimmten <strong>Erfolgswahrscheinlichkeit $p$</strong> auf.",
            "en": "A <strong>Bernoulli experiment</strong> is a random experiment with exactly <strong>two outcomes</strong>: Event $A$ (success) and $\\bar{A}$ (failure). Event $A$ occurs with a specific <strong>success probability $p$</strong>."
        },
        "notation": r"X \sim \text{Ber}(p)",
        # VARIABLE DECODER - "Stupid Person Rule" applied
        "variable_decoder": {
            "header": {"de": "Was bedeutet jedes Symbol?", "en": "What does each symbol mean?"},
            "variables": [
                {
                    "symbol": "X",
                    "name": {"de": "Die Zufallsvariable", "en": "The Random Variable"},
                    "meaning": {
                        "de": "Das <strong>Ergebnis</strong> deines Experiments. $X$ kann nur zwei Werte annehmen: <strong>1</strong> (Erfolg passiert) oder <strong>0</strong> (Erfolg passiert nicht).",
                        "en": "The <strong>outcome</strong> of your experiment. $X$ can only take two values: <strong>1</strong> (success happens) or <strong>0</strong> (success doesn't happen)."
                    },
                    "example": {"de": "Münzwurf: X = 1 bedeutet 'Kopf gefallen'", "en": "Coin flip: X = 1 means 'Heads landed'"}
                },
                {
                    "symbol": r"\sim",
                    "name": {"de": "'folgt' oder 'ist verteilt nach'", "en": "'follows' or 'is distributed as'"},
                    "meaning": {
                        "de": "Dieses Symbol verbindet die Zufallsvariable mit ihrer Verteilung. Lies es als: <strong>'X folgt einer...'</strong> oder <strong>'X ist verteilt nach...'</strong>",
                        "en": "This symbol connects the random variable to its distribution. Read it as: <strong>'X follows a...'</strong> or <strong>'X is distributed as...'</strong>"
                    },
                    "example": {"de": "Wie ein Etikett auf einer Box: sagt dir, was drin ist", "en": "Like a label on a box: tells you what's inside"}
                },
                {
                    "symbol": r"\text{Ber}",
                    "name": {"de": "Bernoulli-Verteilung", "en": "Bernoulli Distribution"},
                    "meaning": {
                        "de": "Der <strong>Name</strong> der Verteilung. Benannt nach Jakob Bernoulli. Sagt dir: 'Dies ist ein Experiment mit genau 2 Ausgängen.'",
                        "en": "The <strong>name</strong> of the distribution. Named after Jakob Bernoulli. Tells you: 'This is an experiment with exactly 2 outcomes.'"
                    },
                    "example": {"de": "Wie 'BMW' für ein Auto — ein Markenname", "en": "Like 'BMW' for a car — a brand name"}
                },
                {
                    "symbol": "p",
                    "name": {"de": "Erfolgswahrscheinlichkeit", "en": "Success Probability"},
                    "meaning": {
                        "de": "Die <strong>Chance</strong>, dass dein 'Erfolg' eintritt. Eine Zahl zwischen 0 und 1. <strong>p = 0.5</strong> heisst 50% Chance, <strong>p = 0.1</strong> heisst 10% Chance.",
                        "en": "The <strong>chance</strong> that your 'success' happens. A number between 0 and 1. <strong>p = 0.5</strong> means 50% chance, <strong>p = 0.1</strong> means 10% chance."
                    },
                    "example": {"de": "Faire Münze: p = 0.5 | Würfel 6: p = 1/6 ≈ 0.17", "en": "Fair coin: p = 0.5 | Die roll 6: p = 1/6 ≈ 0.17"}
                },
                {
                    "symbol": "A",
                    "name": {"de": "Erfolg", "en": "Success"},
                    "meaning": {
                        "de": "Das Ereignis, das du als <strong>'Erfolg'</strong> definierst. Du entscheidest selbst, was Erfolg ist!",
                        "en": "The event you define as <strong>'success'</strong>. You decide what success means!"
                    },
                    "example": {"de": "Prüfung bestanden, Produkt funktioniert, Münze zeigt Kopf", "en": "Exam passed, product works, coin shows heads"}
                },
                {
                    "symbol": r"\bar{A}",
                    "name": {"de": "Misserfolg (Nicht-A)", "en": "Failure (Not-A)"},
                    "meaning": {
                        "de": "<strong>Alles andere</strong> ausser Erfolg. Wenn A nicht passiert, passiert $\\bar{A}$. Die Wahrscheinlichkeit ist <strong>1 − p</strong>.",
                        "en": "<strong>Everything else</strong> except success. If A doesn't happen, $\\bar{A}$ happens. The probability is <strong>1 − p</strong>."
                    },
                    "example": {"de": "Prüfung nicht bestanden, Produkt defekt, Münze zeigt Zahl", "en": "Exam failed, product defective, coin shows tails"}
                }
            ],
            "full_reading": {
                "de": "<strong>Lies die ganze Notation so:</strong><br>'Die Zufallsvariable X folgt einer Bernoulli-Verteilung mit Erfolgswahrscheinlichkeit p.'",
                "en": "<strong>Read the full notation as:</strong><br>'The random variable X follows a Bernoulli distribution with success probability p.'"
            }
        }
    },
    
    # --- THE MASS FUNCTION ---
    "formula": {
        "header": {"de": "Die Massenfunktion", "en": "The Mass Function"},
        "pmf_explicit": {
            "de": r"P(X = x) = \begin{cases} p & \text{wenn } x = 1 \text{ (Erfolg)} \\ 1-p & \text{wenn } x = 0 \text{ (Misserfolg)} \end{cases}",
            "en": r"P(X = x) = \begin{cases} p & \text{if } x = 1 \text{ (success)} \\ 1-p & \text{if } x = 0 \text{ (failure)} \end{cases}"
        },
        "pmf_compact": r"f_{\text{Ber}}(x; p) = p^x (1-p)^{1-x}, \quad x \in \{0, 1\}",
        "compact_explanation": {
            "de": "Diese kompakte Form nutzt einen Trick: Wenn $x=1$, wird $p^1 \\cdot (1-p)^0 = p$. Wenn $x=0$, wird $p^0 \\cdot (1-p)^1 = 1-p$.",
            "en": "This compact form uses a trick: When $x=1$, we get $p^1 \\cdot (1-p)^0 = p$. When $x=0$, we get $p^0 \\cdot (1-p)^1 = 1-p$."
        }
    },
    
    # --- PARAMETER ---
    "parameter": {
        "header": {"de": "Der Parameter", "en": "The Parameter"},
        "symbol": r"p \in [0, 1]",
        "name": {"de": "Erfolgswahrscheinlichkeit", "en": "Success Probability"},
        "meaning": {
            "de": "Die Wahrscheinlichkeit, dass $X = 1$ (Erfolg). Bei einer fairen Münze: $p = 0.5$. Bei einem Würfel (Erfolg = 6): $p = \\frac{1}{6}$.",
            "en": "The probability that $X = 1$ (success). For a fair coin: $p = 0.5$. For a die (success = 6): $p = \\frac{1}{6}$."
        }
    },
    
    # --- MOMENTS WITH DERIVATION ---
    "moments": {
        "header": {"de": "Erwartungswert & Varianz", "en": "Expected Value & Variance"},
        "expectation": {
            "title": {"de": "Erwartungswert", "en": "Expected Value"},
            "formula": r"E[X] = p",
            "derivation": {
                "de": "$E[X] = 0 \\cdot P(X=0) + 1 \\cdot P(X=1) = 0 \\cdot (1-p) + 1 \\cdot p = p$",
                "en": "$E[X] = 0 \\cdot P(X=0) + 1 \\cdot P(X=1) = 0 \\cdot (1-p) + 1 \\cdot p = p$"
            },
            "interpretation": {
                "de": "Bei $p = 0.3$ erwarte ich im Schnitt 0.3 Erfolge pro Versuch — d.h. in 30% der Fälle tritt Erfolg ein.",
                "en": "With $p = 0.3$, I expect 0.3 successes per trial on average — i.e., success occurs in 30% of cases."
            }
        },
        "variance": {
            "title": {"de": "Varianz", "en": "Variance"},
            "formula": r"V(X) = p(1-p)",
            "derivation": {
                "de": "$V(X) = E[X^2] - (E[X])^2 = p - p^2 = p(1-p)$",
                "en": "$V(X) = E[X^2] - (E[X])^2 = p - p^2 = p(1-p)$"
            },
            "interpretation": {
                "de": "<strong>Maximale Unsicherheit bei $p = 0.5$</strong> (Varianz = 0.25). Bei $p = 0$ oder $p = 1$ ist Varianz = 0 (sicheres Ergebnis, keine Streuung).",
                "en": "<strong>Maximum uncertainty at $p = 0.5$</strong> (variance = 0.25). At $p = 0$ or $p = 1$, variance = 0 (certain outcome, no spread)."
            }
        }
    },
    
    # --- KEY INSIGHT: VARIANCE PARABOLA ---
    "variance_insight": {
        "header": {"de": "Schlüsseleinsicht: Die Varianz-Parabel", "en": "Key Insight: The Variance Parabola"},
        "text": {
            "de": "Die Funktion $V(p) = p(1-p)$ ist eine <strong>nach unten offene Parabel</strong> mit Maximum bei $p = 0.5$. Je 'unsicherer' das Experiment (je näher $p$ bei 0.5), desto grösser die Streuung!",
            "en": "The function $V(p) = p(1-p)$ is a <strong>downward-opening parabola</strong> with maximum at $p = 0.5$. The more 'uncertain' the experiment (the closer $p$ is to 0.5), the greater the spread!"
        }
    },
    
    # --- EXAMPLE FROM LECTURE ---
    "example": {
        "header": {"de": "Beispiel: Mensch ärgere dich nicht", "en": "Example: Board Game Start"},
        "problem": {
            "de": "Beim Spiel 'Mensch ärgere dich nicht' muss man bei <strong>drei Würfen mindestens eine 6</strong> würfeln, um herauszukommen. Was ist die Erfolgswahrscheinlichkeit?",
            "en": "In the board game 'Ludo', you need to roll <strong>at least one 6 in three rolls</strong> to start. What is the success probability?"
        },
        "solution": {
            "de": """
<strong>Gegeben:</strong> 3 Würfe, Erfolg = mindestens eine 6

<strong>Berechnung:</strong>
$p = 1 - P(\\text{keine 6 in drei Würfen})$
$p = 1 - \\left(\\frac{5}{6}\\right)^3 = 1 - \\frac{125}{216} = \\frac{91}{216} \\approx 0.421$

<strong>Antwort:</strong> Die Wahrscheinlichkeit beträgt ca. <strong>42%</strong>.
            """,
            "en": """
<strong>Given:</strong> 3 rolls, Success = at least one 6

<strong>Calculation:</strong>
$p = 1 - P(\\text{no 6 in three rolls})$
$p = 1 - \\left(\\frac{5}{6}\\right)^3 = 1 - \\frac{125}{216} = \\frac{91}{216} \\approx 0.421$

<strong>Answer:</strong> The probability is approximately <strong>42%</strong>.
            """
        }
    },
    
    # --- CONNECTION TO BINOMIAL ---
    "link_binomial": {
        "header": {"de": "Verbindung zur Binomialverteilung", "en": "Connection to Binomial Distribution"},
        "text": {
            "de": "Die Binomialverteilung ist die <strong>Summe von $n$ unabhängigen Bernoulli-Versuchen</strong>. Wenn du $n$ mal ein Bernoulli-Experiment wiederholst und die Erfolge zählst:",
            "en": "The Binomial distribution is the <strong>sum of $n$ independent Bernoulli trials</strong>. When you repeat a Bernoulli experiment $n$ times and count the successes:"
        },
        "formula": r"\text{Wenn } Y_i \sim \text{Ber}(p), \text{ dann } X = \sum_{i=1}^{n} Y_i \sim \text{Bin}(n, p)"
    },
    
    # --- PRO TIP ---
    "pro_tip": {
        "de": """<strong>Prüfungs-Essentials:</strong><br><br>
<strong>(1) Bernoulli = EINZELNER Versuch mit 2 Ausgängen</strong><br>
<em>Warum wichtig?</em> Bernoulli ist der Grundbaustein! Münzwurf, Prüfung bestanden/nicht bestanden, Produkt defekt/OK — alles Bernoulli.<br><br>
<strong>(2) n Bernoullis = Binomial</strong><br>
<em>Warum?</em> Wenn du den gleichen Bernoulli-Versuch n-mal unabhängig wiederholst und die Erfolge zählst, landest du bei der Binomialverteilung.<br><br>
<strong>(3) Varianz maximal bei p = 0.5</strong><br>
<em>Warum?</em> V(X) = p(1-p) ist eine Parabel. Der Scheitelpunkt liegt bei p = 0.5. Dort ist die Unsicherheit am grössten — könnte genauso gut Erfolg wie Misserfolg sein.<br><br>
<strong>(4) E[X] = p und V(X) = p(1-p) auswendig lernen!</strong><br>
<em>Warum?</em> Diese kommen in fast jeder Prüfung vor. Keine Zeit fürs Herleiten — direkt anwenden!""",
        "en": """<strong>Exam essentials:</strong><br><br>
<strong>(1) Bernoulli = SINGLE trial with 2 outcomes</strong><br>
<em>Why important?</em> Bernoulli is the building block! Coin flip, exam pass/fail, product defective/OK — all Bernoulli.<br><br>
<strong>(2) n Bernoullis = Binomial</strong><br>
<em>Why?</em> When you repeat the same Bernoulli trial n times independently and count successes, you get the Binomial distribution.<br><br>
<strong>(3) Variance maximum at p = 0.5</strong><br>
<em>Why?</em> V(X) = p(1-p) is a parabola. The vertex is at p = 0.5. That's where uncertainty is greatest — equally likely to succeed or fail.<br><br>
<strong>(4) Memorize E[X] = p and V(X) = p(1-p)!</strong><br>
<em>Why?</em> These appear in almost every exam. No time to derive — apply directly!"""
    }
}


def render_subtopic_4_2(model):
    """4.2 Bernoulli-Verteilung - ULTRATHINK Enhanced with fixed HTML"""
    
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
    st.header(t(content_4_2["title"]))
    st.caption(t(content_4_2["subtitle"]))
    st.markdown("---")
    
    # --- INTUITION HOOK ---
    st.markdown(f"### {t(content_4_2['intuition']['header'])}")
    with st.container(border=True):
        st.markdown(t(content_4_2["intuition"]["text"]), unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- FRAG DICH ---
    st.markdown(f"""
    <div style="background-color: rgba(0, 122, 255, 0.08); border-radius: 12px; padding: 20px; border: 2px solid #007AFF;">
        <div style="font-weight: 700; color: #007AFF; margin-bottom: 16px; font-size: 1.1em;">
            {t(content_4_2['frag_dich']['header'])}
        </div>
        <div style="color: #1c1c1e;">
            <ol style="margin: 0; padding-left: 20px; line-height: 2;">
                {"".join([f"<li>{t(q)}</li>" for q in content_4_2['frag_dich']['questions']])}
            </ol>
        </div>
        <div style="margin-top: 16px; padding: 10px; background: #007AFF; color: white; border-radius: 8px; text-align: center; font-weight: 600;">
            {t(content_4_2['frag_dich']['conclusion'])}
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- WHAT IS A BERNOULLI EXPERIMENT (With integrated Symbol Ledger) ---
    st.markdown(f"### {t(content_4_2['bernoulli_experiment']['header'])}")
    with st.container(border=True):
        st.markdown(t(content_4_2["bernoulli_experiment"]["text"]), unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        st.latex(content_4_2["bernoulli_experiment"]["notation"])
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # --- INTEGRATED SYMBOL LEDGER (inside same container) ---
        decoder = content_4_2["bernoulli_experiment"]["variable_decoder"]
        st.markdown(f"**{t(decoder['header'])}**")
        
        # Ledger-style table with gray Zinc palette
        for var in decoder["variables"]:
            st.markdown(f"""
<div style="display: flex; align-items: flex-start; gap: 14px; padding: 12px 0; border-bottom: 1px solid #e4e4e7;">
    <div style="background: #18181b; color: white; border-radius: 6px; padding: 6px 12px; font-size: 1em; font-weight: 600; min-width: 80px; text-align: center; flex-shrink: 0;">
        ${var['symbol']}$
    </div>
    <div style="flex: 1;">
        <div style="font-weight: 600; color: #1c1c1e; margin-bottom: 2px;">{t(var['name'])}</div>
        <div style="color: #52525b; font-size: 0.95em; line-height: 1.5;">{t(var['meaning'])}</div>
        <div style="color: #71717a; font-size: 0.85em; font-style: italic; margin-top: 4px;">{t(var['example'])}</div>
    </div>
</div>
            """, unsafe_allow_html=True)
        
        # Full reading summary at the bottom
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(f"""
<div style="background: #f4f4f5; border-radius: 8px; padding: 14px;">
    <div style="color: #3f3f46; line-height: 1.5;">{t(decoder['full_reading'])}</div>
</div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)

    
    # --- FORMULA (Two forms) ---
    st.markdown(f"### {t(content_4_2['formula']['header'])}")
    
    col_explicit, col_compact = st.columns(2, gap="medium")
    
    with col_explicit:
        with st.container(border=True):
            st.markdown(f"**{t({'de': 'Explizite Form', 'en': 'Explicit Form'})}**")
            st.latex(t(content_4_2["formula"]["pmf_explicit"]))
            
            st.markdown("---")
            st.caption(t({
                "de": "Diese Form zeigt direkt, was passiert: <strong>Erfolg</strong> (x=1) hat Wahrscheinlichkeit p, <strong>Misserfolg</strong> (x=0) hat Wahrscheinlichkeit 1−p. Diese beiden müssen sich zu 1 addieren.",
                "en": "This form shows directly what happens: <strong>Success</strong> (x=1) has probability p, <strong>Failure</strong> (x=0) has probability 1−p. These two must add up to 1."
            }), unsafe_allow_html=True)
    
    with col_compact:
        with st.container(border=True):
            st.markdown(f"**{t({'de': 'Kompakte Form', 'en': 'Compact Form'})}**")
            st.latex(content_4_2["formula"]["pmf_compact"])
            st.markdown("---")
            st.caption(t(content_4_2["formula"]["compact_explanation"]))
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- PARAMETER ---
    st.markdown(f"### {t(content_4_2['parameter']['header'])}")
    with st.container(border=True):
        col_sym, col_desc = st.columns([1, 3])
        with col_sym:
            st.latex(content_4_2["parameter"]["symbol"])
        with col_desc:
            st.markdown(f"**{t(content_4_2['parameter']['name'])}**")
            st.markdown(t(content_4_2["parameter"]["meaning"]), unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- MOMENTS WITH DERIVATIONS ---
    st.markdown(f"### {t(content_4_2['moments']['header'])}")
    
    col_e, col_v = st.columns(2, gap="medium")
    
    with col_e:
        with st.container(border=True):
            st.markdown(f"**{t(content_4_2['moments']['expectation']['title'])}**")
            st.latex(content_4_2["moments"]["expectation"]["formula"])
            st.markdown("---")
            st.caption(t({'de': 'Herleitung', 'en': 'Derivation'}))
            st.markdown(t(content_4_2["moments"]["expectation"]["derivation"]))
            st.markdown("---")
            st.markdown(t(content_4_2["moments"]["expectation"]["interpretation"]), unsafe_allow_html=True)
    
    with col_v:
        with st.container(border=True):
            st.markdown(f"**{t(content_4_2['moments']['variance']['title'])}**")
            st.latex(content_4_2["moments"]["variance"]["formula"])
            st.markdown("---")
            st.caption(t({'de': 'Herleitung', 'en': 'Derivation'}))
            st.markdown(t(content_4_2["moments"]["variance"]["derivation"]))
            st.markdown("---")
            st.markdown(t(content_4_2["moments"]["variance"]["interpretation"]), unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- VARIANCE INSIGHT ---
    insight_text = t({
        "de": "Die Funktion V(p) = p(1−p) ist eine <strong>nach unten offene Parabel</strong> mit Maximum bei p = 0.5. Je 'unsicherer' das Experiment (je näher p bei 0.5), desto grösser die Streuung!",
        "en": "The function V(p) = p(1−p) is a <strong>downward-opening parabola</strong> with maximum at p = 0.5. The more 'uncertain' the experiment (the closer p is to 0.5), the greater the spread!"
    })
    st.markdown(f"""
<div style="background: #f4f4f5; padding: 16px; border-radius: 8px; border-left: 4px solid #71717a; color: #3f3f46; line-height: 1.6;">
{insight_text}
</div>""", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- EXAMPLE ---
    st.markdown(f"### {t(content_4_2['example']['header'])}")
    with st.container(border=True):
        st.markdown(t(content_4_2["example"]["problem"]), unsafe_allow_html=True)
        st.markdown("---")
        st.markdown(t(content_4_2["example"]["solution"]), unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- LINK TO BINOMIAL ---
    st.markdown(f"### {t(content_4_2['link_binomial']['header'])}")
    with st.container(border=True):
        st.markdown(t(content_4_2["link_binomial"]["text"]), unsafe_allow_html=True)
        st.latex(content_4_2["link_binomial"]["formula"])
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- PRO TIP ---
    st.markdown(f"""
    <div style="background-color: #f4f4f5; border-radius: 8px; padding: 12px; color: #3f3f46;">
        {t(content_4_2['pro_tip'])}
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- EXAM SECTION ---
    st.markdown(f"### {t({'de': 'Prüfungstraining', 'en': 'Exam Practice'})}")
    
    with st.container(border=True):
        st.info(t({
            "de": "Bernoulli wird typischerweise im Kontext der Binomialverteilung geprüft. Siehe Abschnitt 4.3 für Übungsaufgaben.",
            "en": "Bernoulli is typically tested in the context of the Binomial distribution. See section 4.3 for practice problems."
        }))
