# Topic 4.1: Discrete Uniform Distribution - Gleichförmige Verteilung
# ULTRATHINK ENHANCED VERSION
import streamlit as st
from views.styles import inject_equal_height_css
from utils.localization import t
from utils.quiz_helper import render_mcq
from data.exam_questions import get_question

# ==========================================
# 1. CONTENT DICTIONARY - BILINGUAL (ULTRATHINK)
# ==========================================
content_4_1 = {
    "title": {"de": "4.1 Gleichförmige Verteilung (diskret)", "en": "4.1 Uniform Distribution (Discrete)"},
    "subtitle": {
        "de": "Die Verteilung der perfekten Fairness",
        "en": "The Distribution of Perfect Fairness"
    },
    
    # --- INTUITION HOOK ---
    "intuition": {
        "header": {"de": "Die Intuition", "en": "The Intuition"},
        "text": {
            "de": "Stell dir einen **perfekt fairen Würfel** vor. Keine Seite ist schwerer, keine ist bevorzugt. Jede Zahl von 1 bis 6 hat **exakt dieselbe Chance**: $\\frac{1}{6}$. Das ist die diskrete Gleichverteilung — das mathematische Modell für **perfekte Fairness**.",
            "en": "Imagine a **perfectly fair die**. No side is heavier, none is favored. Each number from 1 to 6 has **exactly the same chance**: $\\frac{1}{6}$. This is the discrete uniform distribution — the mathematical model for **perfect fairness**."
        }
    },
    
    # --- FRAG DICH (Decision Guide) ---
    "frag_dich": {
        "header": {"de": "Frag dich: Ist es Gleichverteilt?", "en": "Ask yourself: Is it Uniform?"},
        "questions": [
            {"de": "Haben ALLE Ausgänge <strong>exakt dieselbe</strong> Wahrscheinlichkeit?", "en": "Do ALL outcomes have <strong>exactly the same</strong> probability?"},
            {"de": "Ist die Anzahl der Ausgänge <strong>endlich</strong>?", "en": "Is the number of outcomes <strong>finite</strong>?"},
            {"de": "Ist das Experiment 'fair' (kein Ausgang bevorzugt)?", "en": "Is the experiment 'fair' (no outcome favored)?"}
        ],
        "conclusion": {
            "de": "Alles Ja → Diskrete Gleichverteilung!",
            "en": "All Yes → Discrete Uniform Distribution!"
        }
    },
    
    # --- DEFINITION ---
    "definition": {
        "header": {"de": "Definition", "en": "Definition"},
        "text": {
            "de": "Eine Zufallsvariable $X$ mit $m$ (endlich vielen) Ausprägungen heisst **diskret gleichverteilt**, wenn alle Ausgänge dieselbe Wahrscheinlichkeit haben.",
            "en": "A random variable $X$ with $m$ (finitely many) outcomes is called **discretely uniform distributed** if all outcomes have the same probability."
        },
        "notation": {
            "de": r"X \sim \text{GL}(m) \quad \text{oder} \quad X \sim \text{Uniform}(m)",
            "en": r"X \sim \text{GL}(m) \quad \text{or} \quad X \sim \text{Uniform}(m)"
        },
        "breakdown": {
            "header": {"de": "Was bedeutet diese Notation?", "en": "What does this notation mean?"},
            "parts": [
                {
                    "symbol": r"X",
                    "meaning_de": "<strong>Die Zufallsvariable:</strong> Das Ergebnis unseres Zufallsexperiments. Beispiel: 'Welche Zahl zeigt der Würfel?'",
                    "meaning_en": "<strong>The random variable:</strong> The outcome of our random experiment. Example: 'What number shows on the die?'"
                },
                {
                    "symbol": r"\sim",
                    "meaning_de": "<strong>ist verteilt wie:</strong> Dieses Symbol bedeutet 'folgt der Verteilung'. Lies: 'X ist verteilt gemäss...'",
                    "meaning_en": "<strong>is distributed as:</strong> This symbol means 'follows the distribution'. Read: 'X is distributed according to...'"
                },
                {
                    "symbol": r"\text{GL}(m)",
                    "meaning_de": "<strong>Gleichverteilung:</strong> GL = 'Gleich' (alle Ausgänge gleich wahrscheinlich). Die Zahl m in Klammern ist die Anzahl möglicher Ausgänge.",
                    "meaning_en": "<strong>Uniform distribution:</strong> GL = German abbreviation for 'Gleichverteilung'. The number m in parentheses is the count of possible outcomes."
                },
                {
                    "symbol": r"m",
                    "meaning_de": "<strong>Anzahl Ausgänge:</strong> Beim Würfel ist m = 6 (sechs Seiten). Bei einer Münze wäre m = 2.",
                    "meaning_en": "<strong>Number of outcomes:</strong> For a die, m = 6 (six sides). For a coin, m = 2."
                }
            ],
            "example": {
                "de": "<strong>Beispiel:</strong> 'X ~ GL(6)' bedeutet: 'X ist eine Zufallsvariable mit 6 gleichwahrscheinlichen Ausgängen' — ein fairer Würfel!",
                "en": "<strong>Example:</strong> 'X ~ GL(6)' means: 'X is a random variable with 6 equally likely outcomes' — a fair die!"
            }
        }
    },
    
    # --- THE FORMULA (With Breakdown) ---
    "formula": {
        "header": {"de": "Die Massenfunktion", "en": "The Mass Function"},
        "pmf": {
            "de": r"P(X = x_i) = \frac{1}{m} \quad \text{für alle } i = 1, 2, \ldots, m",
            "en": r"P(X = x_i) = \frac{1}{m} \quad \text{for all } i = 1, 2, \ldots, m"
        },
        "breakdown": {
            "header": {"de": "Was bedeutet das? (Intuition!)", "en": "What does this mean? (Intuition!)"},
            "parts": [
                {
                    "symbol": r"P(X = x_i)",
                    "meaning_de": "<strong>Lies:</strong> 'Die Wahrscheinlichkeit, dass X den Wert xᵢ annimmt'. Bei einem Würfel: P(X = 3) = 'Wahrscheinlichkeit, eine 3 zu würfeln'.",
                    "meaning_en": "<strong>Read:</strong> 'The probability that X takes the value xᵢ'. For a die: P(X = 3) = 'Probability of rolling a 3'."
                },
                {
                    "symbol": r"\frac{1}{m}",
                    "meaning_de": "<strong>Warum 1/m?</strong> Bei m möglichen Ausgängen hat jeder GENAU denselben Anteil: 1 geteilt durch m. Würfel: 1/6 ≈ 16.7% pro Seite.",
                    "meaning_en": "<strong>Why 1/m?</strong> With m possible outcomes, each has EXACTLY the same share: 1 divided by m. Die: 1/6 ≈ 16.7% per side."
                },
                {
                    "symbol_de": r"\text{für alle } i",
                    "symbol_en": r"\text{for all } i",
                    "meaning_de": "<strong>Für ALLE:</strong> Das ist der Schlüssel! Diese Formel gilt für JEDEN Ausgang gleich. Keine Seite ist bevorzugt. Das ist 'Gleichverteilung' = gleiche Wahrscheinlichkeit für alle.",
                    "meaning_en": "<strong>For ALL:</strong> This is the key! This formula applies EQUALLY to every outcome. No side is favored. That's 'uniform distribution' = equal probability for all."
                }
            ],
            "example": {
                "label": {"de": "Konkret:", "en": "Concrete:"},
                "text": {"de": "Würfel mit", "en": "Die with"},
                "formula": r"m = 6: \quad P(X = 1) = P(X = 2) = \ldots = P(X = 6) = \frac{1}{6} \approx 0.167"
            }
        }
    },
    
    # --- PARAMETER ---
    "parameter": {
        "header": {"de": "Der Parameter", "en": "The Parameter"},
        "symbol": r"m \in \{1, 2, 3, \ldots\}",
        "name_de": "Anzahl möglicher Ausgänge",
        "name_en": "Number of possible outcomes",
        "meaning_de": "Wie viele verschiedene Werte kann $X$ annehmen? Bei einem Würfel: $m = 6$.",
        "meaning_en": "How many different values can $X$ take? For a die: $m = 6$."
    },
    
    # --- MOMENTS WITH INTERPRETATION ---
    "moments": {
        "header": {"de": "Erwartungswert & Varianz", "en": "Expected Value & Variance"},
        "expectation": {
            "title_de": "Erwartungswert",
            "title_en": "Expected Value",
            "formula_general": r"E[X] = \sum_{i=1}^{m} x_i \cdot \frac{1}{m} = \frac{1}{m} \sum_{i=1}^{m} x_i",
            "formula_1_to_m": {
                "de": r"E[X] = \frac{m+1}{2} \quad \text{(wenn } X \in \{1, 2, \ldots, m\}\text{)}",
                "en": r"E[X] = \frac{m+1}{2} \quad \text{(if } X \in \{1, 2, \ldots, m\}\text{)}"
            },
            "interpretation_de": "Der 'Schwerpunkt' der Verteilung. Beim fairen Würfel: $E[X] = \\frac{7}{2} = 3.5$ — kein realer Ausgang, aber der langfristige Durchschnitt!",
            "interpretation_en": "The 'center of mass' of the distribution. For a fair die: $E[X] = \\frac{7}{2} = 3.5$ — not a real outcome, but the long-run average!"
        },
        "variance": {
            "title_de": "Varianz",
            "title_en": "Variance",
            "formula_1_to_m": {
                "de": r"V(X) = \frac{m^2 - 1}{12} \quad \text{(wenn } X \in \{1, 2, \ldots, m\}\text{)}",
                "en": r"V(X) = \frac{m^2 - 1}{12} \quad \text{(if } X \in \{1, 2, \ldots, m\}\text{)}"
            },
            "interpretation_de": "Misst die Streuung. Je mehr Ausgänge ($m$ gross), desto höher die Varianz.",
            "interpretation_en": "Measures the spread. More outcomes ($m$ large) means higher variance."
        }
    },
    
    # --- WORKED EXAMPLE ---
    "example_worked": {
        "header": {"de": "Beispiel: Fairer Würfel", "en": "Example: Fair Die"},
        "problem": {
            "de": "Ein fairer Würfel wird geworfen. Berechne $E[X]$ und $V(X)$.",
            "en": "A fair die is rolled. Calculate $E[X]$ and $V(X)$."
        },
        "solution": {
            "de": """
**Gegeben:** $m = 6$, $X \\in \\{1, 2, 3, 4, 5, 6\\}$

**Erwartungswert:**
$E[X] = \\frac{6+1}{2} = \\frac{7}{2} = 3.5$

**Varianz:**
$V(X) = \\frac{6^2 - 1}{12} = \\frac{35}{12} \\approx 2.92$
            """,
            "en": """
**Given:** $m = 6$, $X \\in \\{1, 2, 3, 4, 5, 6\\}$

**Expected Value:**
$E[X] = \\frac{6+1}{2} = \\frac{7}{2} = 3.5$

**Variance:**
$V(X) = \\frac{6^2 - 1}{12} = \\frac{35}{12} \\approx 2.92$
            """
        }
    },
    
    # --- EXAM ESSENTIALS (Merged Trap + Pro Tip) ---
    "exam_essentials": {
        "header": {"de": "Prüfungs-Essentials", "en": "Exam Essentials"},
        "trap": {
            "de": "Die Summe zweier gleichverteilter Zufallsvariablen ist NICHT gleichverteilt. Beispiel: 2 Würfel → Summe ist NICHT uniform (7 ist am wahrscheinlichsten).",
            "en": "The sum of two uniformly distributed random variables is NOT uniform. Example: 2 dice → Sum is NOT uniform (7 is most likely)."
        },
        "trap_rule": {
            "de": "Gleichverteilung ist NICHT reproduktiv!",
            "en": "Uniform distribution is NOT reproductive!"
        },
        "tips": [
            {
                "tip": {"de": "P = 1/m für jeden Ausgang", "en": "P = 1/m for each outcome"},
                "why": {"de": "\"Gleich\"verteilung = alle gleich wahrscheinlich. Bei m Möglichkeiten muss sich 1 (= 100%) auf alle aufteilen.", "en": "\"Uniform\" distribution = all equally likely. With m possibilities, 1 (= 100%) must split evenly."}
            },
            {
                "tip": {"de": "E[X] = (m+1)/2 als Schnellformel", "en": "E[X] = (m+1)/2 as shortcut formula"},
                "why": {"de": "Funktioniert nur wenn X ∈ {1, 2, ..., m}. Der Durchschnitt von 1 bis m ist immer die Mitte.", "en": "Only works when X ∈ {1, 2, ..., m}. The average of 1 to m is always the midpoint."}
            },
            {
                "tip": {"de": "Summen sind NICHT gleichverteilt", "en": "Sums are NOT uniformly distributed"},
                "why": {"de": "Bei 2 Würfeln: nur 1 Weg für Summe 2 (1+1), aber 6 Wege für Summe 7. Mehr Wege = höhere Wahrscheinlichkeit.", "en": "With 2 dice: only 1 way to get sum 2 (1+1), but 6 ways to get sum 7. More ways = higher probability."}
            }
        ]
    }
}


def render_subtopic_4_1(model):
    """4.1 Gleichförmige Verteilung - ULTRATHINK Enhanced"""
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
    
    /* COMPACT DIVIDER: Aggressive spacing reduction */
    [data-testid="stVerticalBlockBorderWrapper"] hr {
        margin-top: 2px !important;
        margin-bottom: 2px !important;
    }
    
    /* Reduce vertical spacing of elements within bordered containers */
    [data-testid="stVerticalBlockBorderWrapper"] [data-testid="stMarkdownContainer"] {
        margin-bottom: 0 !important;
    }
    
    /* Compact column gaps within containers */
    [data-testid="stVerticalBlockBorderWrapper"] [data-testid="stHorizontalBlock"] {
        gap: 4px !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # --- HEADER ---
    st.header(t(content_4_1["title"]))
    st.caption(t(content_4_1["subtitle"]))
    st.markdown("---")
    
    # --- INTUITION HOOK (Header-Out Protocol) ---
    st.markdown(f"### {t(content_4_1['intuition']['header'])}")
    with st.container(border=True):
        st.markdown(t(content_4_1["intuition"]["text"]))
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- FRAG DICH ---
    from utils.ask_yourself import render_ask_yourself
    render_ask_yourself(
        header=content_4_1['frag_dich']['header'],
        questions=content_4_1['frag_dich']['questions'],
        conclusion=content_4_1['frag_dich']['conclusion']
    )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- DEFINITION ---
    st.markdown(f"### {t(content_4_1['definition']['header'])}")
    with st.container(border=True):
        st.markdown(t(content_4_1["definition"]["text"]))
        st.latex(t(content_4_1["definition"]["notation"]))
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(f"**{t(content_4_1['definition']['breakdown']['header'])}**")
        
        for part in content_4_1["definition"]["breakdown"]["parts"]:
            col_sym, col_mean = st.columns([1, 3])
            with col_sym:
                st.latex(part["symbol"])
            with col_mean:
                st.markdown(t({"de": part["meaning_de"], "en": part["meaning_en"]}), unsafe_allow_html=True)
            st.markdown("---")
        
        st.markdown("<br>", unsafe_allow_html=True)
        example_data = content_4_1["definition"]["breakdown"]["example"]
        st.markdown(f"""
<div style="background-color: #f4f4f5; border-radius: 8px; padding: 12px; border-left: 4px solid #a1a1aa; color: #3f3f46;">
    {t(example_data)}
</div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- FORMULA WITH BREAKDOWN ---
    st.markdown(f"### {t(content_4_1['formula']['header'])}")
    with st.container(border=True):
        st.latex(t(content_4_1["formula"]["pmf"]))
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(f"**{t(content_4_1['formula']['breakdown']['header'])}**")
        
        for i, part in enumerate(content_4_1["formula"]["breakdown"]["parts"]):
            if i > 0:
                st.markdown("---")
            col_sym, col_mean = st.columns([1, 3])
            with col_sym:
                # Handle bilingual symbols
                if "symbol_de" in part:
                    st.latex(t({"de": part["symbol_de"], "en": part["symbol_en"]}))
                else:
                    st.latex(part["symbol"])
            with col_mean:
                st.markdown(t({"de": part["meaning_de"], "en": part["meaning_en"]}), unsafe_allow_html=True)
        
        st.markdown("---")
        example_data = content_4_1["formula"]["breakdown"]["example"]
        st.markdown(f"**{t(example_data['label'])}** {t(example_data['text'])}")
        st.latex(example_data["formula"])
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- PARAMETER ---
    st.markdown(f"### {t(content_4_1['parameter']['header'])}")
    with st.container(border=True):
        col_sym, col_desc = st.columns([1, 3])
        with col_sym:
            st.latex(content_4_1["parameter"]["symbol"])
        with col_desc:
            st.markdown(f"**{t({'de': content_4_1['parameter']['name_de'], 'en': content_4_1['parameter']['name_en']})}**")
            st.caption(t({"de": content_4_1["parameter"]["meaning_de"], "en": content_4_1["parameter"]["meaning_en"]}))
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- MOMENTS ---
    st.markdown(f"### {t(content_4_1['moments']['header'])}")
    
    col_e, col_v = st.columns(2, gap="medium")
    
    with col_e:
        with st.container(border=True):
            st.markdown(f"**{t({'de': content_4_1['moments']['expectation']['title_de'], 'en': content_4_1['moments']['expectation']['title_en']})}**")
            st.latex(t(content_4_1["moments"]["expectation"]["formula_1_to_m"]))
            st.markdown("---")
            st.markdown(t({"de": content_4_1["moments"]["expectation"]["interpretation_de"], "en": content_4_1["moments"]["expectation"]["interpretation_en"]}))
    
    with col_v:
        with st.container(border=True):
            st.markdown(f"**{t({'de': content_4_1['moments']['variance']['title_de'], 'en': content_4_1['moments']['variance']['title_en']})}**")
            st.latex(t(content_4_1["moments"]["variance"]["formula_1_to_m"]))
            st.markdown("---")
            st.markdown(t({"de": content_4_1["moments"]["variance"]["interpretation_de"], "en": content_4_1["moments"]["variance"]["interpretation_en"]}))
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- WORKED EXAMPLE ---
    with st.container(border=True):
        st.markdown(f"### {t(content_4_1['example_worked']['header'])}")
        st.markdown(t(content_4_1["example_worked"]["problem"]))
        st.markdown("---")
        st.markdown(t(content_4_1["example_worked"]["solution"]))
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- EXAM ESSENTIALS ---
    from utils.exam_essentials import render_exam_essentials
    render_exam_essentials(
        trap=content_4_1["exam_essentials"]["trap"],
        trap_rule=content_4_1["exam_essentials"]["trap_rule"],
        tips=content_4_1["exam_essentials"]["tips"]
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- EXAM SECTION ---
    st.markdown(f"### {t({'de': 'Prüfungstraining', 'en': 'Exam Practice'})}")
    
    q_data = get_question("4.1", "uniform_dice")
    if q_data:
        with st.container(border=True):
            st.caption(q_data.get("source", ""))
            opts = q_data.get("options", [])
            if opts and isinstance(opts[0], dict):
                option_labels = [t(o) for o in opts]
            else:
                option_labels = opts
            
            render_mcq(
                key_suffix="4_1_uniform",
                question_text=t(q_data["question"]),
                options=option_labels,
                correct_idx=q_data["correct_idx"],
                solution_text_dict=q_data["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
                client=model,
                ai_context="Uniform distribution",
                course_id="vwl",
                topic_id="4",
                subtopic_id="4.1",
                question_id="4_1_uniform"
            )
    else:
        with st.container(border=True):
            st.markdown(f"""
<div style="background: #f4f4f5; border-left: 4px solid #a1a1aa; padding: 12px 16px; border-radius: 8px; color: #3f3f46;">
{t({"de": "Für diesen Abschnitt gibt es derzeit keine MCQ-Fragen.", "en": "This section currently has no MCQ questions."})}
</div>
""", unsafe_allow_html=True)
