# Topic 7.2: Messzahlen zur Beschreibung statistischer Verteilungen
# ULTRATHINK ENHANCED VERSION — "Stupid Person Principle" Applied
# Every concept explained so clearly a 12-year-old would understand

import streamlit as st
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from utils.localization import t
from utils.quiz_helper import render_mcq
from utils.ask_yourself import render_ask_yourself
from utils.exam_essentials import render_exam_essentials
from utils.worked_example import render_worked_example
from utils.layouts import (
    render_comparison,
    render_single_formula,
    render_formula_grid,
)
from utils.layouts.foundation import (
    intuition_box,
    grey_callout,
    inject_equal_height_css,
    COLORS,
)
from data.exam_questions import get_question

# ==============================================================================
# SEMANTIC COLOR PALETTE (Matches synthesis.md Connection Coloring)
# ==============================================================================
# These colors create VISUAL CONNECTIONS across formulas and explanations
COLOR_DATA = "#007AFF"      # Blue  — The raw data points (xᵢ)
COLOR_CENTER = "#9B59B6"    # Purple — Center measures (x̄, Median)
COLOR_SPREAD = "#FF4B4B"    # Red   — Spread/deviation (xᵢ - x̄)
COLOR_RESULT = "#16a34a"    # Green — Final computed result
COLOR_NEUTRAL = "#6B7280"   # Gray  — Neutral/reference

# ==============================================================================
# CONTENT DICTIONARY — BILINGUAL (ULTRATHINK DEPTH)
# ==============================================================================

content_7_2 = {
    "title": {
        "de": "7.2 Messzahlen zur Beschreibung statistischer Verteilungen",
        "en": "7.2 Measures for Describing Statistical Distributions"
    },
    "subtitle": {
        "de": "Das statistische Toolkit: Wie man 1000 Zahlen in 5 zusammenfasst",
        "en": "The Statistical Toolkit: How to Summarize 1000 Numbers in 5"
    },
    
    # =========================================================================
    # INTUITION — THE "GRANDMA TEST" ANALOGY
    # No math symbols. A 12-year-old should understand.
    # =========================================================================
    "intuition": {
        "de": """<strong>Stell dir vor:</strong> Du bist Chef einer Fabrik mit 500 Mitarbeitern. 
        Jeder verdient unterschiedlich viel — von 2'500 CHF bis 15'000 CHF monatlich.
        <br><br>
        <strong>Das Problem:</strong> Dein Vorgesetzter fragt: "Wie viel verdienen deine Leute so?"
        <br><br>
        Du kannst nicht 500 Zahlen auflisten. Du brauchst <strong>eine Zahl, die "typisch" ist</strong> 
        (das ist das <em>Lagemaß</em>) und <strong>eine Zahl, die zeigt wie unterschiedlich 
        die Gehälter sind</strong> (das ist das <em>Streuungsmaß</em>).
        <br><br>
        Genau das lernst du hier: <strong>Wie man viele Zahlen in wenige, aussagekräftige Kennzahlen packt.</strong>""",
        
        "en": """<strong>Imagine:</strong> You're the manager of a factory with 500 employees. 
        Everyone earns different amounts — from 2,500 CHF to 15,000 CHF monthly.
        <br><br>
        <strong>The Problem:</strong> Your boss asks: "How much do your people earn?"
        <br><br>
        You can't list 500 numbers. You need <strong>one number that's "typical"</strong> 
        (that's the <em>location measure</em>) and <strong>one number showing how different 
        the salaries are</strong> (that's the <em>dispersion measure</em>).
        <br><br>
        That's exactly what you'll learn: <strong>How to pack many numbers into few, meaningful statistics.</strong>"""
    },
    
    # =========================================================================
    # LOCATION MEASURES — MEAN VS MEDIAN VS MODE (3-WAY COMPARISON)
    # =========================================================================
    "location_header": {
        "de": "Lagemaße: Wo liegt das 'Typische'?",
        "en": "Location Measures: Where is the 'Typical' Value?"
    },
    
    "location_intuition": {
        "de": """Es gibt <strong>drei Wege</strong>, das "Typische" zu messen — und jeder passt zu einer anderen Situation:
        <ul style="margin-top: 12px; line-height: 1.8;">
        <li><strong>Mittelwert:</strong> Wenn du alles zusammenzählst und gerecht verteilst</li>
        <li><strong>Median:</strong> Der Wert genau in der Mitte, wenn du alle sortierst</li>
        <li><strong>Modus:</strong> Der Wert, der am häufigsten vorkommt</li>
        </ul>""",
        "en": """There are <strong>three ways</strong> to measure "typical" — and each fits a different situation:
        <ul style="margin-top: 12px; line-height: 1.8;">
        <li><strong>Mean:</strong> When you add everything up and share equally</li>
        <li><strong>Median:</strong> The value exactly in the middle when you sort all values</li>
        <li><strong>Mode:</strong> The value that appears most often</li>
        </ul>"""
    },
    
    "mean": {
        "title": {"de": "Mittelwert (Durchschnitt)", "en": "Mean (Average)"},
        "intuition": {
            "de": "Alle Werte zusammenzählen, dann durch die Anzahl teilen",
            "en": "Add all values together, then divide by the count"
        },
        "formula": r"\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i",
        "variables": [
            {"symbol": r"\bar{x}", "name": {"de": "Mittelwert", "en": "Mean"}, 
             "description": {"de": "Das Ergebnis — der Durchschnitt", "en": "The result — the average"}},
            {"symbol": r"n", "name": {"de": "Anzahl", "en": "Count"}, 
             "description": {"de": "Wie viele Werte du hast", "en": "How many values you have"}},
            {"symbol": r"x_i", "name": {"de": "Einzelwert", "en": "Single value"}, 
             "description": {"de": "Jeder einzelne Datenpunkt", "en": "Each individual data point"}},
        ],
        "insight": {
            "de": "Der Mittelwert ist <strong>empfindlich gegenüber Ausreissern</strong>. "
                  "Ein CEO mit 1 Million Gehalt kann den Durchschnitt aller Angestellten stark verzerren.",
            "en": "The mean is <strong>sensitive to outliers</strong>. "
                  "A CEO earning 1 million can heavily distort the average of all employees."
        },
        "when_to_use": {
            "de": "Wenn deine Daten auf einer <strong>Kardinalskala</strong> sind (z.B. Einkommen in CHF, Temperatur in °C) und <strong>keine extremen Ausreisser</strong> hast.",
            "en": "When your data is on a <strong>cardinal scale</strong> (e.g., income in CHF, temperature in °C) and <strong>no extreme outliers</strong>."
        }
    },
    
    "median": {
        "title": {"de": "Median (Zentralwert)", "en": "Median (Central Value)"},
        "intuition": {
            "de": "Alle Werte sortieren — der Median ist der Wert genau in der Mitte",
            "en": "Sort all values — the median is the value exactly in the middle"
        },
        "formula": r"\text{Med} = \begin{cases} x_{\frac{n+1}{2}} & \text{n ungerade} \\ \frac{1}{2}(x_{\frac{n}{2}} + x_{\frac{n}{2}+1}) & \text{n gerade} \end{cases}",
        "formula_en": r"\text{Med} = \begin{cases} x_{\frac{n+1}{2}} & \text{n odd} \\ \frac{1}{2}(x_{\frac{n}{2}} + x_{\frac{n}{2}+1}) & \text{n even} \end{cases}",
        "insight": {
            "de": "Der Median ist <strong>robust</strong> — Ausreisser stören ihn kaum. "
                  "Darum wird bei Gehältern oft der Median statt dem Mittelwert angegeben.",
            "en": "The median is <strong>robust</strong> — outliers barely affect it. "
                  "That's why salary reports often show median instead of mean."
        },
        "when_to_use": {
            "de": "Bei <strong>Ordinalskala</strong> (z.B. Schulnoten) oder wenn <strong>Ausreisser</strong> vorhanden sind (z.B. Immobilienpreise).",
            "en": "For <strong>ordinal scale</strong> (e.g., grades) or when <strong>outliers</strong> are present (e.g., real estate prices)."
        }
    },
    
    "mode": {
        "title": {"de": "Modus (Modalwert)", "en": "Mode"},
        "intuition": {
            "de": "Der Wert, der am häufigsten vorkommt — der 'Publikumsliebling'",
            "en": "The value that appears most often — the 'crowd favorite'"
        },
        "formula": r"x^M = x_i \text{ mit } h_i \geq h_j \text{ für alle } j",
        "formula_en": r"x^M = x_i \text{ with } h_i \geq h_j \text{ for all } j",
        "insight": {
            "de": "Der Modus ist das <strong>einzige Lagemaß für Nominalskala</strong>. "
                  "Beispiel: Die beliebteste Autofarbe ist 'Weiss' — hier macht ein Durchschnitt keinen Sinn.",
            "en": "The mode is the <strong>only location measure for nominal scale</strong>. "
                  "Example: The most popular car color is 'White' — averaging colors makes no sense."
        },
        "when_to_use": {
            "de": "Bei <strong>Nominalskala</strong> (z.B. Farben, Kategorien) oder wenn du den <strong>häufigsten Wert</strong> suchst.",
            "en": "For <strong>nominal scale</strong> (e.g., colors, categories) or when looking for the <strong>most frequent value</strong>."
        }
    },
    
    # =========================================================================
    # DISPERSION MEASURES — THE SPREAD ARSENAL
    # =========================================================================
    "dispersion_header": {
        "de": "Streuungsmaße: Wie unterschiedlich sind die Werte?",
        "en": "Dispersion Measures: How Different Are the Values?"
    },
    
    "dispersion_intuition": {
        "de": """Zwei Klassen haben beide einen Notendurchschnitt von 4.0. 
        Aber: In Klasse A haben alle 4er, in Klasse B gibt es 1er und 6er. 
        <strong>Die Streuung zeigt diesen Unterschied.</strong>""",
        "en": """Two classes both have an average grade of 4.0. 
        But: In Class A everyone has 4s, in Class B there are 1s and 6s. 
        <strong>The dispersion shows this difference.</strong>"""
    },
    
    "dispersion_formulas": [
        {
            "name": {"de": "Spannweite", "en": "Range"},
            "description": {"de": "Grösster minus kleinster Wert — schnell, aber anfällig für Ausreisser", 
                           "en": "Largest minus smallest value — quick, but sensitive to outliers"},
            "formula": r"\text{Range} = x_{\max} - x_{\min}"
        },
        {
            "name": {"de": "Interquartilsabstand (IQR)", "en": "Interquartile Range (IQR)"},
            "description": {"de": "Die 'mittleren 50%' — robust gegen Ausreisser", 
                           "en": "The 'middle 50%' — robust against outliers"},
            "formula": r"\text{IQR} = Q_3 - Q_1"
        },
        {
            "name": {"de": "Empirische Varianz", "en": "Empirical Variance"},
            "description": {"de": "Durchschnittliche quadrierte Abweichung vom Mittelwert", 
                           "en": "Average squared deviation from the mean"},
            "formula": r"S^2 = \frac{1}{n} \sum_{i=1}^{n} (x_i - \bar{x})^2"
        },
        {
            "name": {"de": "Standardabweichung", "en": "Standard Deviation"},
            "description": {"de": "Wurzel aus Varianz — gleiche Einheit wie Daten!", 
                           "en": "Square root of variance — same unit as data!"},
            "formula": r"S = \sqrt{S^2} = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (x_i - \bar{x})^2}"
        }
    ],
    
    "dispersion_key_takeaway": {
        "de": "<strong>Faustregel:</strong> Spannweite für schnelle Übersicht, IQR bei Ausreissern, "
              "Varianz/Standardabweichung für genaue Analyse.",
        "en": "<strong>Rule of thumb:</strong> Range for quick overview, IQR with outliers, "
              "Variance/Standard Deviation for precise analysis."
    },
    
    # =========================================================================
    # COEFFICIENT OF VARIATION — THE UNIVERSAL COMPARATOR
    # =========================================================================
    "vk": {
        "header": {"de": "Variationskoeffizient (VK)", "en": "Coefficient of Variation (CV)"},
        "intuition_label": {"de": "Warum brauchen wir das?", "en": "Why Do We Need This?"},
        "intuition": {
            "de": """<strong>Das Problem:</strong> Du willst die Streuung von Aktienkurs A (CHF 50, S = CHF 5) 
            mit Aktienkurs B (CHF 500, S = CHF 20) vergleichen. 
            <br><br>
            A hat S = 5, B hat S = 20. Ist B also 4× so volatil? <strong>Nein!</strong>
            <br><br>
            Du musst die Streuung <strong>relativ zum Mittelwert</strong> betrachten:
            A streut um 10% (5/50), B nur um 4% (20/500). <strong>A ist relativ volatiler!</strong>""",
            "en": """<strong>The Problem:</strong> You want to compare the spread of Stock A (CHF 50, S = CHF 5) 
            with Stock B (CHF 500, S = CHF 20).
            <br><br>
            A has S = 5, B has S = 20. Is B 4× more volatile? <strong>No!</strong>
            <br><br>
            You need to consider spread <strong>relative to the mean</strong>:
            A varies by 10% (5/50), B only by 4% (20/500). <strong>A is relatively more volatile!</strong>"""
        },
        "formula": r"\text{VK} = \frac{S}{\bar{x}}",
        "variables": [
            {"symbol": r"\text{VK}", "name": {"de": "Variationskoeffizient", "en": "Coefficient of Variation"}, 
             "description": {"de": "Relative Streuung (dimensionslos oder in %)", "en": "Relative spread (dimensionless or in %)"}},
            {"symbol": r"S", "name": {"de": "Standardabweichung", "en": "Standard Deviation"}, 
             "description": {"de": "Absolute Streuung", "en": "Absolute spread"}},
            {"symbol": r"\bar{x}", "name": {"de": "Mittelwert", "en": "Mean"}, 
             "description": {"de": "Muss ≠ 0 sein!", "en": "Must be ≠ 0!"}},
        ],
        "insight": {
            "de": "Der VK macht Streuungen <strong>vergleichbar</strong>, auch wenn die Daten in völlig "
                  "verschiedenen Einheiten oder Grössenordnungen vorliegen.",
            "en": "The CV makes spreads <strong>comparable</strong>, even when data are in completely "
                  "different units or magnitudes."
        }
    },
    
    # =========================================================================
    # WORKED EXAMPLE — STOCK VOLATILITY (FROM COURSE THEORY)
    # =========================================================================
    "worked_example": {
        "header": {"de": "Praxis: Welche Aktie ist volatiler?", "en": "Practice: Which Stock Is More Volatile?"},
        "problem": {
            "de": """<strong>Gegeben (250 Handelstage):</strong><br>
            • Daimler-Aktie: Mittelwert = <span style='color:#9B59B6;font-weight:600'>50.59 €</span>, 
              Standardabweichung = <span style='color:#FF4B4B;font-weight:600'>36.18 €</span><br>
            • Porsche-Aktie: Mittelwert = <span style='color:#9B59B6;font-weight:600'>396.10 €</span>, 
              Standardabweichung = <span style='color:#FF4B4B;font-weight:600'>182.96 €</span>
            <br><br>
            <strong>Frage:</strong> Welche Aktie streut relativ stärker?""",
            "en": """<strong>Given (250 trading days):</strong><br>
            • Daimler Stock: Mean = <span style='color:#9B59B6;font-weight:600'>€50.59</span>, 
              Std Dev = <span style='color:#FF4B4B;font-weight:600'>€36.18</span><br>
            • Porsche Stock: Mean = <span style='color:#9B59B6;font-weight:600'>€396.10</span>, 
              Std Dev = <span style='color:#FF4B4B;font-weight:600'>€182.96</span>
            <br><br>
            <strong>Question:</strong> Which stock has higher relative volatility?"""
        },
        "steps": [
            {
                "label": {"de": "Schritt 1: VK für Daimler", "en": "Step 1: CV for Daimler"},
                "latex": r"\text{VK}_{\text{Daimler}} = \frac{{\color{#FF4B4B}36.18}}{{\color{#9B59B6}50.59}} = {\color{#16a34a}0.715} = 71.5\%",
                "note": {"de": "Rot = Streuung, Lila = Mittelwert, Grün = Ergebnis", "en": "Red = Spread, Purple = Mean, Green = Result"}
            },
            {
                "label": {"de": "Schritt 2: VK für Porsche", "en": "Step 2: CV for Porsche"},
                "latex": r"\text{VK}_{\text{Porsche}} = \frac{{\color{#FF4B4B}182.96}}{{\color{#9B59B6}396.10}} = {\color{#16a34a}0.462} = 46.2\%",
                "note": None
            }
        ],
        "answer": {
            "de": "<strong>Fazit:</strong> Obwohl Porsche eine höhere absolute Standardabweichung hat (€182.96 vs €36.18), "
                  "ist <strong>Daimler relativ volatiler</strong> (71.5% vs 46.2%). Der VK deckt das auf!",
            "en": "<strong>Conclusion:</strong> Although Porsche has higher absolute standard deviation (€182.96 vs €36.18), "
                  "<strong>Daimler is relatively more volatile</strong> (71.5% vs 46.2%). The CV reveals this!"
        }
    },
    
    # =========================================================================
    # FRAG DICH — DECISION QUESTIONS
    # =========================================================================
    "frag_dich": {
        "header": {"de": "Frag dich: Welches Maß passt?", "en": "Ask yourself: Which Measure Fits?"},
        "questions": [
            {"de": "Meine Daten sind <strong>Kategorien</strong> (Farben, Marken) → Welches Lagemaß?", 
             "en": "My data are <strong>categories</strong> (colors, brands) → Which location measure?"},
            {"de": "Ich habe <strong>Ausreisser</strong> in meinen Daten → Mittelwert oder Median?", 
             "en": "I have <strong>outliers</strong> in my data → Mean or Median?"},
            {"de": "Ich will <strong>zwei Variablen vergleichen</strong>, die in verschiedenen Einheiten sind → Welches Streuungsmaß?", 
             "en": "I want to <strong>compare two variables</strong> in different units → Which dispersion measure?"},
            {"de": "Meine Daten sind <strong>Schulnoten (1-6)</strong> → Kardinale oder Ordinalskala?", 
             "en": "My data are <strong>school grades (1-6)</strong> → Cardinal or Ordinal scale?"},
        ],
        "conclusion": {"de": "Kategorien → Modus | Ausreisser → Median | Vergleich → VK | Noten → Ordinal (Median)", 
                       "en": "Categories → Mode | Outliers → Median | Comparison → CV | Grades → Ordinal (Median)"}
    },
    
    # =========================================================================
    # EXAM ESSENTIALS — TRAP + TIPS
    # =========================================================================
    "exam_essentials": {
        "trap": {
            "de": "<strong>n statt n-1 bei der Stichprobenvarianz:</strong> Die 'empirische Varianz' im Skript "
                  "teilt durch $n$. Bei <em>Schätzung</em> der Populationsvarianz aus einer Stichprobe "
                  "muss man durch $n-1$ teilen (erwartungstreue Schätzung)!",
            "en": "<strong>n instead of n-1 for sample variance:</strong> The 'empirical variance' in the script "
                  "divides by $n$. When <em>estimating</em> population variance from a sample, "
                  "you must divide by $n-1$ (unbiased estimator)!"
        },
        "trap_formula": r"S^2_{\text{emp}} = \frac{1}{n}\sum(x_i-\bar{x})^2 \quad \text{vs} \quad \hat{\sigma}^2 = \frac{1}{n-1}\sum(x_i-\bar{x})^2",
        "trap_rule": {
            "de": "Lies die Aufgabe genau: 'Empirische Varianz' = n, 'Stichprobenvarianz (erwartungstreu)' = n-1",
            "en": "Read the problem carefully: 'Empirical variance' = n, 'Sample variance (unbiased)' = n-1"
        },
        "tips": [
            {
                "tip": {"de": "Median bei Ausreissern", "en": "Median with Outliers"},
                "why": {"de": "Ein CEO-Gehalt von 1 Mio. verzerrt den Mittelwert massiv, "
                              "aber der Median bleibt stabil — er ist robust.", 
                        "en": "A CEO salary of 1 million massively distorts the mean, "
                              "but the median stays stable — it's robust."}
            },
            {
                "tip": {"de": "VK für unterschiedliche Einheiten", "en": "CV for Different Units"},
                "why": {"de": "Vergleich von Temperaturschwankungen (°C) mit Gewichtsschwankungen (kg)? "
                              "Nur der VK macht das möglich.", 
                        "en": "Comparing temperature fluctuations (°C) with weight fluctuations (kg)? "
                              "Only the CV makes this possible."}
            },
            {
                "tip": {"de": "Quantile-Formel mit K", "en": "Quantile Formula with K"},
                "why": {"de": "K = αn + 1 berechnen. Wenn K ganzzahlig → Mittelwert von x(K-1) und x(K). "
                              "Nicht ganzzahlig → nimm x(K).", 
                        "en": "Calculate K = αn + 1. If K is integer → average of x(K-1) and x(K). "
                              "Not integer → take x(K)."}
            }
        ]
    },
    
    # =========================================================================
    # INTERACTIVE MISSION CONTENT
    # =========================================================================
    "mission": {
        "title": {"de": "Mission: Ausreisser-Sensitivität", "en": "Mission: Outlier Sensitivity"},
        "scenario": {
            "de": """<strong>Szenario:</strong> Du analysierst die Gehälter eines Teams mit 10 Mitarbeitern. 
            Alle verdienen zwischen 4'000 und 6'000 CHF — bis der neue CEO kommt.
            <br><br>
            <strong>Deine Aufgabe:</strong> Beobachte, wie sich Mittelwert und Median verändern, 
            wenn du das CEO-Gehalt anpasst. Entdecke, warum der Median "robust" heisst.""",
            "en": """<strong>Scenario:</strong> You're analyzing salaries of a team with 10 employees. 
            Everyone earns between 4,000 and 6,000 CHF — until the new CEO arrives.
            <br><br>
            <strong>Your Task:</strong> Observe how mean and median change 
            when you adjust the CEO salary. Discover why the median is called "robust"."""
        },
        "discovery": {
            "de": """<strong>Was du entdeckt hast:</strong><br>
            Der Mittelwert reagiert stark auf Ausreisser — je höher das CEO-Gehalt, desto mehr verschiebt sich der Durchschnitt.<br>
            Der Median bleibt <strong>stabil</strong>, weil er nur die Position in der Mitte betrachtet, nicht den Wert selbst.<br><br>
            <strong>Praxis-Tipp:</strong> Bei Gehaltsstatistiken, Immobilienpreisen oder Vermögensverteilungen 
            wird oft der Median angegeben — genau aus diesem Grund!""",
            "en": """<strong>What you discovered:</strong><br>
            The mean reacts strongly to outliers — the higher the CEO salary, the more the average shifts.<br>
            The median stays <strong>stable</strong> because it only looks at the middle position, not the value itself.<br><br>
            <strong>Practical tip:</strong> For salary statistics, real estate prices, or wealth distributions, 
            the median is often reported — exactly for this reason!"""
        }
    }
}


# ==============================================================================
# INTERACTIVE: OUTLIER SENSITIVITY MISSION (OPTION D - ULTRATHINK)
# ==============================================================================

@st.fragment
def outlier_sensitivity_mission():
    """
    ULTRATHINK Interactive Element: Outlier Sensitivity Mission
    
    Pedagogical Design:
    - Students see a team of 10 employees with typical salaries
    - They control a slider to add a CEO salary (from 5k to 100k)
    - Two charts show: (1) All salaries with CEO marked (2) Mean vs Median comparison
    - Semantic colors: Blue = original data, Red = outlier/CEO, Purple = Mean, Green = Median
    - Real-time feedback on how much the mean shifts while median stays stable
    
    This demonstrates WHY median is "robust" in a visceral, interactive way.
    """
    
    # State initialization
    if "osm_completed" not in st.session_state:
        st.session_state.osm_completed = False
    if "osm_max_ceo" not in st.session_state:
        st.session_state.osm_max_ceo = 5000  # Track highest CEO salary explored
    
    # Base team salaries (carefully designed to show effect clearly)
    # Deliberately clustered around 5000 to make outlier effect dramatic
    base_salaries = np.array([4200, 4500, 4800, 5000, 5000, 5200, 5400, 5600, 5800, 6000])
    n_original = len(base_salaries)
    
    # Scenario description (grey callout)
    st.markdown(f"""
<div style="background: #f4f4f5; border-left: 4px solid #a1a1aa; 
            padding: 12px 16px; border-radius: 8px; color: #3f3f46;">
{t(content_7_2["mission"]["scenario"])}
</div>
""", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Mission statement
    st.markdown(f"**{t({'de': 'Mission', 'en': 'Mission'})}:** {t({'de': 'Finde heraus, was mit Mittelwert und Median passiert!', 'en': 'Find out what happens to mean and median!'})}")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    ceo_salary = st.slider(
        t({"de": "CEO-Gehalt (CHF)", "en": "CEO Salary (CHF)"}),
        min_value=5000,
        max_value=100000,
        value=5000,
        step=1000,
        format="%d",
        key="ceo_salary_slider"
    )
    
    # Track exploration for completion
    if ceo_salary > st.session_state.osm_max_ceo:
        st.session_state.osm_max_ceo = ceo_salary
    
    # Add CEO to salaries
    all_salaries = np.append(base_salaries, ceo_salary)
    
    # Calculate statistics
    original_mean = np.mean(base_salaries)
    original_median = np.median(base_salaries)
    new_mean = np.mean(all_salaries)
    new_median = np.median(all_salaries)
    
    # Calculate shifts
    mean_shift = new_mean - original_mean
    median_shift = new_median - original_median
    mean_shift_pct = (mean_shift / original_mean) * 100
    median_shift_pct = (median_shift / original_median) * 100 if original_median != 0 else 0
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # === VISUALIZATION ===
    # Create side-by-side charts using Plotly
    fig = make_subplots(
        rows=1, cols=2,
        subplot_titles=(
            t({"de": "Gehaltsverteilung", "en": "Salary Distribution"}),
            t({"de": "Mittelwert vs Median", "en": "Mean vs Median"})
        ),
        horizontal_spacing=0.12
    )
    
    # Chart 1: Salary Distribution (Bar chart with CEO highlighted)
    colors = [COLOR_DATA if s != ceo_salary else COLOR_SPREAD for s in all_salaries]
    sorted_indices = np.argsort(all_salaries)
    sorted_salaries = all_salaries[sorted_indices]
    sorted_colors = [colors[i] for i in sorted_indices]
    
    fig.add_trace(
        go.Bar(
            x=[f"P{i+1}" if sorted_salaries[i] != ceo_salary else "CEO" for i in range(len(sorted_salaries))],
            y=sorted_salaries,
            marker_color=sorted_colors,
            showlegend=False,
            hovertemplate="%{y:,.0f} CHF<extra></extra>"
        ),
        row=1, col=1
    )
    
    # Add mean and median lines on chart 1
    fig.add_hline(
        y=new_mean, 
        line_dash="dash", 
        line_color=COLOR_CENTER,
        annotation_text=f"x̄ = {new_mean:,.0f}",
        annotation_position="right",
        row=1, col=1
    )
    fig.add_hline(
        y=new_median, 
        line_dash="solid", 
        line_color=COLOR_RESULT,
        annotation_text=f"Med = {new_median:,.0f}",
        annotation_position="right",
        row=1, col=1
    )
    
    # Chart 2: Mean vs Median Comparison (shows the shift)
    categories = ["Original", "Mit CEO"]
    
    # Mean bars
    fig.add_trace(
        go.Bar(
            x=categories,
            y=[original_mean, new_mean],
            name=t({"de": "Mittelwert", "en": "Mean"}),
            marker_color=COLOR_CENTER,
            text=[f"{original_mean:,.0f}", f"{new_mean:,.0f}"],
            textposition="auto",
            textfont=dict(size=12, color="white"),
            hovertemplate="%{y:,.0f} CHF<extra></extra>"
        ),
        row=1, col=2
    )
    
    # Median bars
    fig.add_trace(
        go.Bar(
            x=categories,
            y=[original_median, new_median],
            name=t({"de": "Median", "en": "Median"}),
            marker_color=COLOR_RESULT,
            text=[f"{original_median:,.0f}", f"{new_median:,.0f}"],
            textposition="auto",
            textfont=dict(size=12, color="white"),
            hovertemplate="%{y:,.0f} CHF<extra></extra>"
        ),
        row=1, col=2
    )
    
    # Layout
    fig.update_layout(
        height=400,
        barmode="group",
        showlegend=True,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        margin=dict(t=60, b=50, l=60, r=40),
        hovermode="x unified",
        dragmode=False
    )
    
    fig.update_xaxes(title_text=t({"de": "Mitarbeiter", "en": "Employee"}), row=1, col=1)
    fig.update_yaxes(title_text="CHF", row=1, col=1)
    fig.update_xaxes(title_text="", row=1, col=2)
    fig.update_yaxes(title_text="CHF", row=1, col=2)
    
    # Disable interactivity for cleaner UX
    fig.update_layout(clickmode='none')
    config = {'displayModeBar': False, 'staticPlot': False}
    
    st.plotly_chart(fig, use_container_width=True, config=config)
    
    # === REAL-TIME FEEDBACK ===
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Color-coded feedback boxes
    col1, col2 = st.columns(2)
    
    with col1:
        # Mean shift (purple background for center measure)
        shift_color = COLOR_SPREAD if mean_shift_pct > 10 else COLOR_NEUTRAL
        st.markdown(f"""
<div style="background: rgba(155, 89, 182, 0.1); border: 2px solid {COLOR_CENTER}; 
            padding: 16px; border-radius: 8px; text-align: center;">
<strong style="color: {COLOR_CENTER};">{t({"de": "Mittelwert-Verschiebung", "en": "Mean Shift"})}</strong><br>
<span style="font-size: 1.8em; font-weight: 700; color: {shift_color};">
+{mean_shift:,.0f} CHF ({mean_shift_pct:.1f}%)
</span>
</div>
""", unsafe_allow_html=True)
    
    with col2:
        # Median shift (green background for robust measure)
        med_color = COLOR_RESULT if median_shift_pct < 5 else COLOR_NEUTRAL
        st.markdown(f"""
<div style="background: rgba(22, 163, 74, 0.1); border: 2px solid {COLOR_RESULT}; 
            padding: 16px; border-radius: 8px; text-align: center;">
<strong style="color: {COLOR_RESULT};">{t({"de": "Median-Verschiebung", "en": "Median Shift"})}</strong><br>
<span style="font-size: 1.8em; font-weight: 700; color: {med_color};">
+{median_shift:,.0f} CHF ({median_shift_pct:.1f}%)
</span>
</div>
""", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # === LEGEND (Semantic Color Explanation) ===
    st.markdown(f"""
<div style="background: #f8fafc; border: 1px solid #e2e8f0; padding: 12px 16px; border-radius: 8px;">
<strong>{t({"de": "Farbcode", "en": "Color Code"})}:</strong>
<span style="color: {COLOR_DATA}; font-weight: 600;">●</span> {t({"de": "Team-Gehälter", "en": "Team Salaries"})} | 
<span style="color: {COLOR_SPREAD}; font-weight: 600;">●</span> {t({"de": "CEO (Ausreisser)", "en": "CEO (Outlier)"})} | 
<span style="color: {COLOR_CENTER}; font-weight: 600;">●</span> {t({"de": "Mittelwert", "en": "Mean"})} | 
<span style="color: {COLOR_RESULT}; font-weight: 600;">●</span> {t({"de": "Median (robust)", "en": "Median (robust)"})}
</div>
""", unsafe_allow_html=True)
    
    # === COMPLETION STATE ===
    # Trigger when user has explored high CEO salaries
    if st.session_state.osm_max_ceo >= 50000 and not st.session_state.osm_completed:
        st.session_state.osm_completed = True
    
    if st.session_state.osm_completed:
        st.markdown("<br>", unsafe_allow_html=True)
        st.success(t({
            "de": "Mission abgeschlossen! Du hast entdeckt, warum der Median 'robust' genannt wird.",
            "en": "Mission Complete! You discovered why the median is called 'robust'."
        }))
        
        # Discovery debrief
        st.markdown(f"""
<div style="background: #f4f4f5; border-left: 4px solid #a1a1aa; 
            padding: 12px 16px; border-radius: 8px; color: #3f3f46;">
{t(content_7_2["mission"]["discovery"])}
</div>
""", unsafe_allow_html=True)


# ==============================================================================
# RENDER FUNCTION — MAIN PAGE STRUCTURE
# ==============================================================================

def render_subtopic_7_2(model):
    """7.2 Messzahlen zur Beschreibung statistischer Verteilungen — ULTRATHINK Enhanced"""
    
    # Inject equal height CSS for comparison sections
    inject_equal_height_css()
    
    # === HEADER ===
    st.header(t(content_7_2["title"]))
    st.caption(t(content_7_2["subtitle"]))
    st.markdown("---")
    
    # === 1. INTUITION (The "Grandma Test" Analogy) ===
    intuition_box(content_7_2["intuition"])
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # === 2. LOCATION MEASURES (Mean vs Median vs Mode) ===
    st.markdown(f"### {t(content_7_2['location_header'])}")
    
    # Overview intuition for location measures
    st.markdown(f"""
<div style="background: #f4f4f5; border-left: 4px solid #a1a1aa; 
            padding: 12px 16px; border-radius: 8px; color: #3f3f46; margin-bottom: 16px;">
{t(content_7_2["location_intuition"])}
</div>
""", unsafe_allow_html=True)
    
    # Vertical cards for 3 location measures (avoid narrow columns for formulas)
    for measure_key in ["mean", "median", "mode"]:
        measure = content_7_2[measure_key]
        
        with st.container(border=True):
            st.markdown(f"**{t(measure['title'])}**")
            st.markdown(f"*{t(measure['intuition'])}*")
            
            # Handle bilingual formulas for median/mode
            if "formula_en" in measure:
                formula = measure["formula_en"] if t({"de": "x", "en": "y"}) == "y" else measure["formula"]
            else:
                formula = measure["formula"]
            st.latex(formula)
            
            st.markdown("---")
            
            # Variable decoder (only for mean, others are more complex)
            if measure_key == "mean" and "variables" in measure:
                st.markdown(f"**{t({'de': 'Variablen-Decoder', 'en': 'Variable Decoder'})}:**")
                for v in measure["variables"]:
                    name = t(v["name"])
                    desc = t(v.get("description", {"de": "", "en": ""}))
                    desc_part = f" — {desc}" if desc else ""
                    st.markdown(f"• ${v['symbol']}$ = **{name}**{desc_part}")
                st.markdown("---")
            
            # When to use
            st.markdown(f"**{t({'de': 'Wann verwenden?', 'en': 'When to use?'})}** {t(measure['when_to_use'])}")
            
            # Key insight
            st.markdown("---")
            st.markdown(f"""
<div style="background: #f4f4f5; border-left: 4px solid #a1a1aa; 
            padding: 12px 16px; border-radius: 8px; color: #3f3f46;">
<strong>{t({"de": "Aha-Moment", "en": "Key Insight"})}:</strong><br>{t(measure['insight'])}
</div>
""", unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # === 3. DISPERSION MEASURES (Formula Grid) ===
    st.markdown(f"### {t(content_7_2['dispersion_header'])}")
    
    # Intuition paragraph
    st.markdown(f"""
<div style="background: #f4f4f5; border-left: 4px solid #a1a1aa; 
            padding: 12px 16px; border-radius: 8px; color: #3f3f46; margin-bottom: 16px;">
{t(content_7_2["dispersion_intuition"])}
</div>
""", unsafe_allow_html=True)
    
    render_formula_grid(
        formulas=content_7_2["dispersion_formulas"],
        key_takeaway=content_7_2["dispersion_key_takeaway"],
        show_header=False
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # === 4. COEFFICIENT OF VARIATION ===
    vk = content_7_2["vk"]
    render_single_formula(
        title=vk["header"],
        intuition_label=vk["intuition_label"],
        intuition=vk["intuition"],
        formula=vk["formula"],
        variables=vk["variables"],
        insight=vk["insight"]
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # === 5. WORKED EXAMPLE ===
    we = content_7_2["worked_example"]
    render_worked_example(
        header=we["header"],
        problem=we["problem"],
        steps=we["steps"],
        answer=we["answer"]
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # === 6. INTERACTIVE MISSION ===
    st.markdown(f"### {t(content_7_2['mission']['title'])}")
    with st.container(border=True):
        outlier_sensitivity_mission()
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # === 7. FRAG DICH ===
    fd = content_7_2["frag_dich"]
    render_ask_yourself(
        header=fd["header"],
        questions=fd["questions"],
        conclusion=fd["conclusion"]
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # === 8. EXAM ESSENTIALS ===
    ee = content_7_2["exam_essentials"]
    render_exam_essentials(
        trap=ee["trap"],
        trap_formula=ee["trap_formula"],
        trap_rule=ee["trap_rule"],
        tips=ee["tips"]
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # === 9. EXAM PRACTICE (MCQs) ===
    st.markdown(f"### {t({'de': 'Prüfungstraining', 'en': 'Exam Practice'})}")
    
    # MCQ 1: test4_q3 (Mean, Median, Mode)
    q1 = get_question("7", "test4_q3")
    if q1:
        st.caption(q1.get("source", ""))
        with st.container(border=True):
            opts = q1.get("options", [])
            if opts and isinstance(opts[0], dict):
                option_labels = [t(o) for o in opts]
            else:
                option_labels = opts
            
            render_mcq(
                key_suffix="7_2_measures",
                question_text=t(q1["question"]),
                options=option_labels,
                correct_idx=q1["correct_idx"],
                solution_text_dict=q1["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
                client=model,
                ai_context="Mean, Median, Mode identification",
                course_id="vwl",
                topic_id="7",
                subtopic_id="7.2",
                question_id="7_2_measures"
            )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # MCQ 2: hs2015_mc9 (Variance from normal distribution)
    q2 = get_question("7", "hs2015_mc9")
    if q2:
        st.caption(q2.get("source", ""))
        with st.container(border=True):
            opts = q2.get("options", [])
            if opts and isinstance(opts[0], dict):
                option_labels = [t(o) for o in opts]
            else:
                option_labels = opts
            
            render_mcq(
                key_suffix="7_2_variance",
                question_text=t(q2["question"]),
                options=option_labels,
                correct_idx=q2["correct_idx"],
                solution_text_dict=q2["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
                client=model,
                ai_context="Calculating variance from normal distribution percentiles",
                course_id="vwl",
                topic_id="7",
                subtopic_id="7.2",
                question_id="7_2_variance"
            )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # MCQ 3: hs2023_mc4 (Variance from PDF)
    q3 = get_question("7", "hs2023_mc4")
    if q3:
        st.caption(q3.get("source", ""))
        with st.container(border=True):
            opts = q3.get("options", [])
            if opts and isinstance(opts[0], dict):
                option_labels = [t(o) for o in opts]
            else:
                option_labels = opts
            
            render_mcq(
                key_suffix="7_2_pdf_var",
                question_text=t(q3["question"]),
                options=option_labels,
                correct_idx=q3["correct_idx"],
                solution_text_dict=q3["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
                client=model,
                ai_context="Calculating variance from probability density function",
                course_id="vwl",
                topic_id="7",
                subtopic_id="7.2",
                question_id="7_2_pdf_var"
            )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # MCQ 4: test3_q3 (Variance of linear combination)
    q4 = get_question("7", "test3_q3")
    if q4:
        st.caption(q4.get("source", ""))
        with st.container(border=True):
            opts = q4.get("options", [])
            if opts and isinstance(opts[0], dict):
                option_labels = [t(o) for o in opts]
            else:
                option_labels = opts
            
            render_mcq(
                key_suffix="7_2_var_combo",
                question_text=t(q4["question"]),
                options=option_labels,
                correct_idx=q4["correct_idx"],
                solution_text_dict=q4["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
                client=model,
                ai_context="Variance of linear combination with correlation",
                course_id="vwl",
                topic_id="7",
                subtopic_id="7.2",
                question_id="7_2_var_combo"
            )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # MCQ 5: hs2023_mc9 (Covariance calculation)
    q5 = get_question("7", "hs2023_mc9")
    if q5:
        st.caption(q5.get("source", ""))
        with st.container(border=True):
            opts = q5.get("options", [])
            if opts and isinstance(opts[0], dict):
                option_labels = [t(o) for o in opts]
            else:
                option_labels = opts
            
            render_mcq(
                key_suffix="7_2_cov",
                question_text=t(q5["question"]),
                options=option_labels,
                correct_idx=q5["correct_idx"],
                solution_text_dict=q5["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
                client=model,
                ai_context="Covariance calculation with linear transformation",
                course_id="vwl",
                topic_id="7",
                subtopic_id="7.2",
                question_id="7_2_cov"
            )
