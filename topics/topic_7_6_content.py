# Topic 7.6: Zusammenfassung — Descriptive Statistics Summary
# ULTRATHINK IMPLEMENTATION: Learn-Test-Learn Chunked Pattern
import streamlit as st
from utils.localization import t
from utils.quiz_helper import render_mcq
from utils.ask_yourself import render_ask_yourself
from utils.exam_essentials import render_exam_essentials
from utils.layouts import (
    render_comparison,
    render_formula_grid,
    render_single_formula,
    render_decision_tree,
)
from utils.layouts.foundation import inject_equal_height_css, grey_callout
from data.exam_questions import get_all_questions_for_topic

# ==========================================
# 1. CONTENT DICTIONARY - BILINGUAL (ULTRATHINK)
# ==========================================
content_7_6 = {
    "title": {"de": "7.6 Zusammenfassung", "en": "7.6 Summary"},
    "subtitle": {"de": "Beschreibende Statistik im Überblick", "en": "Descriptive Statistics at a Glance"},
    
    # --- CHAPTER INTUITION ---
    "intuition": {
        "header": {"de": "Das grosse Bild", "en": "The Big Picture"},
        "text": {
            "de": """Du hast gelernt, die <strong>Sprache der Rohdaten</strong> zu übersetzen. 
            Aus tausenden Zahlen kannst du jetzt: Eine <strong>Visualisierung</strong> wählen (Histogram, Boxplot, QQ-Plot), 
            ein <strong>Lagemass</strong> berechnen (Mittelwert, Median, Modus), 
            und die <strong>Streuung</strong> quantifizieren (Varianz, IQR, VK). 
            Diese Zusammenfassung zeigt dir, <strong>welches Werkzeug wann</strong> — und die häufigsten Prüfungsfallen.""",
            "en": """You've learned to <strong>translate the language of raw data</strong>. 
            From thousands of numbers, you can now: Choose a <strong>visualization</strong> (Histogram, Boxplot, QQ-Plot), 
            calculate a <strong>measure of center</strong> (Mean, Median, Mode), 
            and quantify <strong>spread</strong> (Variance, IQR, CV). 
            This summary shows you <strong>which tool when</strong> — and the most common exam traps."""
        }
    },
    
    # === CHUNK 1: VISUAL TOOLS ===
    "chunk_visual": {
        "header": {"de": "Visualisierungswerkzeuge", "en": "Visualization Tools"},
        "comparison_1": {
            "left": {
                "title": {"de": "Histogram", "en": "Histogram"},
                "formula": r"\text{Fläche} = f_j = \frac{n_j}{n}",
                "insight": {
                    "de": "<strong>Zeigt:</strong> Verteilungsform — Symmetrie, Schiefe, Peaks",
                    "en": "<strong>Shows:</strong> Distribution shape — Symmetry, skewness, peaks"
                }
            },
            "right": {
                "title": {"de": "ECDF", "en": "ECDF"},
                "formula": r"F_n(y) = \frac{\#(y_i \le y)}{n}",
                "insight": {
                    "de": "<strong>Zeigt:</strong> Quantile ablesen — Median bei F=0.5",
                    "en": "<strong>Shows:</strong> Read quantiles — Median at F=0.5"
                }
            }
        },
        "comparison_2": {
            "left": {
                "title": {"de": "Boxplot", "en": "Boxplot"},
                "formula": r"Q_1, Q_2, Q_3, \text{Whiskers}, \circ",
                "insight": {
                    "de": "<strong>Zeigt:</strong> 5-Zahlen-Zusammenfassung + Ausreisser",
                    "en": "<strong>Shows:</strong> 5-number summary + Outliers"
                }
            },
            "right": {
                "title": {"de": "QQ-Plot", "en": "QQ-Plot"},
                "formula": r"\left(F^{-1}\left(\tfrac{k-0.5}{n}\right), x_{(k)}\right)",
                "insight": {
                    "de": "<strong>Zeigt:</strong> Modell-Fit — Gerade = gute Passung",
                    "en": "<strong>Shows:</strong> Model fit — Straight line = good fit"
                }
            }
        },
        "mcq": {
            "question": {"de": "Welches Tool zeigt dir am besten, ob deine Daten normalverteilt sind?", 
                        "en": "Which tool best shows whether your data is normally distributed?"},
            "options": [
                {"de": "Histogram", "en": "Histogram"},
                {"de": "ECDF", "en": "ECDF"},
                {"de": "Boxplot", "en": "Boxplot"},
                {"de": "QQ-Plot", "en": "QQ-Plot"}
            ],
            "correct_idx": 3,
            "solution": {
                "de": "Der <strong>QQ-Plot</strong> zeigt die Abweichung von einer Referenzverteilung. Bei Normalverteilung: Punkte auf der Diagonale. Kurven = Schiefe, S-Form = falsche Verteilungsfamilie.",
                "en": "The <strong>QQ-Plot</strong> shows deviation from a reference distribution. For Normal: points on diagonal. Curves = skewness, S-shape = wrong distribution family."
            }
        }
    },
    
    # === CHUNK 2: CENTRAL TENDENCY ===
    "chunk_center": {
        "header": {"de": "Lagemasse", "en": "Measures of Central Tendency"},
        "formulas": [
            {
                "name": {"de": "Mittelwert", "en": "Mean"},
                "formula": r"\bar{x} = \frac{1}{n}\sum_{i=1}^{n} x_i",
                "when": {"de": "Kardinalskala", "en": "Cardinal scale"},
                "example": {"de": "Sensitiv zu Ausreissern!", "en": "Sensitive to outliers!"}
            },
            {
                "name": {"de": "Median", "en": "Median"},
                "formula": r"\bar{x}_{Med} = x_{\left(\frac{n+1}{2}\right)}",
                "when": {"de": "Ordinalskala", "en": "Ordinal scale"},
                "example": {"de": "Robust gegen Extremwerte", "en": "Robust to extreme values"}
            },
            {
                "name": {"de": "Modus", "en": "Mode"},
                "formula": r"\bar{x}_M = \text{argmax}(n_j)",
                "when": {"de": "Nominalskala", "en": "Nominal scale"},
                "example": {"de": "Für Kategorien (Farben, Marken)", "en": "For categories (colors, brands)"}
            }
        ],
        "mcq": {
            "question": {"de": "Ein CEO verdient 10× mehr als alle anderen. Welches Mass ist am robustesten?", 
                        "en": "A CEO earns 10× more than everyone else. Which measure is most robust?"},
            "options": [
                {"de": "Mittelwert", "en": "Mean"},
                {"de": "Median", "en": "Median"},
                {"de": "Modus", "en": "Mode"},
                {"de": "Standardabweichung", "en": "Standard deviation"}
            ],
            "correct_idx": 1,
            "solution": {
                "de": "Der <strong>Median</strong> ist immun gegen extreme Ausreisser. Er ist der mittlere Wert der sortierten Daten — ein extremes Gehalt ändert ihn nicht.",
                "en": "The <strong>Median</strong> is immune to extreme outliers. It's the middle value of sorted data — one extreme salary doesn't change it."
            }
        }
    },
    
    # === CHUNK 3: DISPERSION ===
    "chunk_dispersion": {
        "header": {"de": "Streuungsmasse", "en": "Measures of Dispersion"},
        "formulas": [
            {
                "name": {"de": "Varianz", "en": "Variance"},
                "formula": r"S^2 = \frac{1}{n}\sum_{i=1}^{n}(x_i - \bar{x})^2",
                "when": {"de": "Quadratische Streuung", "en": "Squared spread"},
                "example": {"de": "Sensitiv zu Ausreissern", "en": "Sensitive to outliers"}
            },
            {
                "name": {"de": "IQR", "en": "IQR"},
                "formula": r"\text{IQR} = Q_3 - Q_1",
                "when": {"de": "Mittlere 50%", "en": "Middle 50%"},
                "example": {"de": "Robust!", "en": "Robust!"}
            },
            {
                "name": {"de": "Spannweite", "en": "Range"},
                "formula": r"R = x_{max} - x_{min}",
                "when": {"de": "Extremwerte", "en": "Extreme values"},
                "example": {"de": "Sehr ausreissersensitiv", "en": "Very outlier-sensitive"}
            },
            {
                "name": {"de": "Variationskoeffizient", "en": "Coefficient of Variation"},
                "formula": r"VK = \frac{S}{\bar{x}}",
                "when": {"de": "Vergleich verschiedener Skalen", "en": "Compare different scales"},
                "example": {"de": "Einheitslos!", "en": "Unitless!"}
            }
        ],
        "mcq": {
            "question": {"de": r"Daimler: $S=10$, $\bar{x}=80$. Porsche: $S=25$, $\bar{x}=500$. Welche Aktie ist volatiler?", 
                        "en": r"Daimler: $S=10$, $\bar{x}=80$. Porsche: $S=25$, $\bar{x}=500$. Which stock is more volatile?"},
            "options": [
                {"de": "Daimler", "en": "Daimler"},
                {"de": "Porsche", "en": "Porsche"},
                {"de": "Gleich", "en": "Equal"},
                {"de": "Nicht vergleichbar", "en": "Not comparable"}
            ],
            "correct_idx": 0,
            "solution": {
                "de": r"<strong>Daimler!</strong> VK = S/x̄. Daimler: 10/80 = 12.5%. Porsche: 25/500 = 5%. Obwohl Porsche höhere absolute Streuung hat, ist Daimler relativ volatiler.",
                "en": r"<strong>Daimler!</strong> CV = S/x̄. Daimler: 10/80 = 12.5%. Porsche: 25/500 = 5%. Although Porsche has higher absolute spread, Daimler is relatively more volatile."
            }
        }
    },
    
    # === CHUNK 4: BOXPLOT MECHANICS ===
    "chunk_boxplot": {
        "header": {"de": "Boxplot-Mechanik", "en": "Boxplot Mechanics"},
        "formula": {
            "title": {"de": "Quantil-Position", "en": "Quantile Position"},
            "intuition": {"de": "Wo liegt das α-Quantil in der sortierten Datenreihe?", 
                         "en": "Where is the α-quantile in the sorted data series?"},
            "formula": r"K = \alpha n + 1",
            "variables": [
                {"symbol": r"K", "name": {"de": "Position", "en": "Position"}, 
                 "description": {"de": "Stelle in der sortierten Reihe", "en": "Location in sorted series"}},
                {"symbol": r"\alpha", "name": {"de": "Quantil-Level", "en": "Quantile level"}, 
                 "description": {"de": "z.B. 0.25 für Q₁, 0.5 für Median, 0.75 für Q₃", "en": "e.g. 0.25 for Q₁, 0.5 for Median, 0.75 for Q₃"}},
                {"symbol": r"n", "name": {"de": "Stichprobengrösse", "en": "Sample size"}, 
                 "description": {"de": "Anzahl der Beobachtungen", "en": "Number of observations"}}
            ],
            "insight": {"de": "K ganzzahlig → Durchschnitt von x₍ₖ₋₁₎ und x₍ₖ₎. K nicht-ganzzahlig → x₍⌊K⌋₎.", 
                       "en": "K integer → Average of x₍ₖ₋₁₎ and x₍ₖ₎. K non-integer → x₍⌊K⌋₎."}
        },
        "whisker_rule": {
            "de": "<strong>Whiskers:</strong> Enden beim tatsächlichen Datenpunkt INNERHALB der Grenze Q₁ - 1.5·IQR bzw. Q₃ + 1.5·IQR. Alles ausserhalb = Ausreisser (○).",
            "en": "<strong>Whiskers:</strong> End at actual data point WITHIN the boundary Q₁ - 1.5·IQR or Q₃ + 1.5·IQR. Anything outside = Outlier (○)."
        },
        "mcq": {
            "question": {"de": r"Bei $n=16$, $\alpha=0.25$: $K = 0.25 \cdot 16 + 1 = 5$. Wie berechnest du $Q_1$?", 
                        "en": r"For $n=16$, $\alpha=0.25$: $K = 0.25 \cdot 16 + 1 = 5$. How do you calculate $Q_1$?"},
            "options": [
                {"de": r"$x_{(5)}$", "en": r"$x_{(5)}$"},
                {"de": r"$(x_{(4)} + x_{(5)})/2$", "en": r"$(x_{(4)} + x_{(5)})/2$"},
                {"de": r"$x_{(4)}$", "en": r"$x_{(4)}$"},
                {"de": "Nicht definiert", "en": "Not defined"}
            ],
            "correct_idx": 1,
            "solution": {
                "de": r"K=5 ist <strong>ganzzahlig</strong>, also Durchschnitt von $x_{(4)}$ und $x_{(5)}$. Das ist die Regel für ganzzahlige K-Werte!",
                "en": r"K=5 is an <strong>integer</strong>, so average of $x_{(4)}$ and $x_{(5)}$. That's the rule for integer K values!"
            }
        }
    },
    
    # === KEY FORMULAS ===
    "key_formulas": {
        "header": {"de": "Formel-Übersicht", "en": "Formula Overview"},
        "formulas": [
            {"name": {"de": "Rel. Häufigkeit", "en": "Rel. Frequency"}, 
             "formula": r"f_j = \frac{n_j}{n}", 
             "when": {"de": "Anteil in Klasse", "en": "Class proportion"}, 
             "example": {"de": "Σf_j = 1", "en": "Σf_j = 1"}},
            {"name": {"de": "ECDF", "en": "ECDF"}, 
             "formula": r"F_n(y) = \frac{\#(y_i \le y)}{n}", 
             "when": {"de": "Treppenfunktion", "en": "Step function"}, 
             "example": {"de": "Sprung bei jedem Datum", "en": "Jump at each datum"}},
            {"name": {"de": "Mittelwert", "en": "Mean"}, 
             "formula": r"\bar{x} = \frac{1}{n}\sum x_i", 
             "when": {"de": "Schwerpunkt", "en": "Center of mass"}, 
             "example": {"de": "Ausreissersensitiv", "en": "Outlier-sensitive"}},
            {"name": {"de": "Varianz", "en": "Variance"}, 
             "formula": r"S^2 = \frac{1}{n}\sum(x_i - \bar{x})^2", 
             "when": {"de": "Streuung²", "en": "Spread²"}, 
             "example": {"de": "Einheit²", "en": "Unit²"}},
            {"name": {"de": "Quantil-Position", "en": "Quantile Position"}, 
             "formula": r"K = \alpha n + 1", 
             "when": {"de": "Wo in Daten?", "en": "Where in data?"}, 
             "example": {"de": "Q₁: α=0.25", "en": "Q₁: α=0.25"}},
            {"name": {"de": "VK", "en": "CV"}, 
             "formula": r"VK = \frac{S}{\bar{x}}", 
             "when": {"de": "Vergleich", "en": "Comparison"}, 
             "example": {"de": "Einheitslos", "en": "Unitless"}}
        ]
    },
    
    # === DECISION TREE ===
    "decision_tree": {
        "header": {"de": "Welches Werkzeug brauchst du?", "en": "Which Tool Do You Need?"},
        "root": {
            "question": {"de": "Was willst du herausfinden?", "en": "What do you want to find out?"},
            "options": [
                {
                    "label": {"de": "Verteilungsform sehen", "en": "See distribution shape"},
                    "result_formula": r"\text{Histogram}",
                    "result_note": {"de": "Zeigt Peaks, Schiefe, Symmetrie", "en": "Shows peaks, skewness, symmetry"}
                },
                {
                    "label": {"de": "Quantile/Median ablesen", "en": "Read quantiles/median"},
                    "result_formula": r"\text{ECDF} \text{ oder } \text{Boxplot}",
                    "result_note": {"de": "ECDF: F(y)=0.5 für Median. Boxplot: Mittellinie", "en": "ECDF: F(y)=0.5 for median. Boxplot: middle line"}
                },
                {
                    "label": {"de": "Ausreisser identifizieren", "en": "Identify outliers"},
                    "result_formula": r"\text{Boxplot}",
                    "result_note": {"de": "Punkte ausserhalb der Whiskers = Ausreisser", "en": "Points outside whiskers = outliers"}
                },
                {
                    "label": {"de": "Modell-Fit prüfen (z.B. Normalverteilung)", "en": "Check model fit (e.g., Normal)"},
                    "result_formula": r"\text{QQ-Plot}",
                    "result_note": {"de": "Diagonale = guter Fit. S-Kurve = falsches Modell", "en": "Diagonal = good fit. S-curve = wrong model"}
                },
                {
                    "label": {"de": "Beziehung zweier Variablen", "en": "Relationship between two variables"},
                    "result_formula": r"\text{Scatter Plot}",
                    "result_note": {"de": "Jeder Punkt = (x_i, y_i). Muster = Korrelation", "en": "Each point = (x_i, y_i). Pattern = correlation"}
                },
                {
                    "label": {"de": "Gruppen vergleichen", "en": "Compare groups"},
                    "result_formula": r"\text{Nebeneinander Boxplots}",
                    "result_note": {"de": "Mehrere Boxplots in einer Grafik", "en": "Multiple boxplots in one chart"}
                }
            ]
        }
    },
    
    # === ASK YOURSELF ===
    "ask_yourself": {
        "header": {"de": "Frag dich selbst", "en": "Ask Yourself"},
        "questions": [
            {"de": "Kannst du die 3 Lagemasse + ihr Skalenniveau aufzählen?", 
             "en": "Can you list the 3 measures of center + their scale level?"},
            {"de": "Wann ist der Median besser als der Mittelwert?", 
             "en": "When is the median better than the mean?"},
            {"de": "Wie berechnest du Boxplot-Whiskers von Hand?", 
             "en": "How do you calculate boxplot whiskers by hand?"},
            {"de": "Was bedeutet eine S-Kurve im QQ-Plot?", 
             "en": "What does an S-curve in a QQ-plot mean?"},
            {"de": "Histogram vs Boxplot vs QQ-Plot: Wann welches?", 
             "en": "Histogram vs Boxplot vs QQ-Plot: When which?"}
        ],
        "conclusion": {"de": "Wenn du alle mit Ja beantworten kannst, bist du bereit für Kapitel 7!", 
                      "en": "If you can answer all with Yes, you're ready for Chapter 7!"}
    },
    
    # === EXAM ESSENTIALS ===
    "exam_essentials": {
        "trap": {
            "de": "<strong>Die Whisker-Grenz-Falle:</strong> Whiskers enden NICHT bei $Q_1 - 1.5 \\cdot \\text{IQR}$! Sie enden beim nächsten tatsächlichen Datenpunkt INNERHALB dieser Grenze.",
            "en": "<strong>The Whisker Boundary Trap:</strong> Whiskers do NOT end at $Q_1 - 1.5 \\cdot \\text{IQR}$! They end at the nearest actual data point WITHIN that boundary."
        },
        "trap_rule": {
            "de": "Grenze berechnen, dann nächsten Datenwert INNERHALB finden.",
            "en": "Calculate boundary, then find nearest data value WITHIN."
        },
        "tips": [
            {
                "tip": {"de": "Immer zuerst sortieren!", "en": "Always sort first!"},
                "why": {"de": "Quantile auf unsortierte Daten anwenden = Fail. Position K existiert nur in geordneter Reihenfolge.", 
                       "en": "Applying quantiles to unsorted data = Fail. Position K only exists in sorted order."}
            },
            {
                "tip": {"de": "QQ-Achsen: Theorie = X, Daten = Y", "en": "QQ-Axes: Theory = X, Data = Y"},
                "why": {"de": "Prüfungen testen speziell diese Zuordnung. Nicht verwechseln!", 
                       "en": "Exams specifically test this assignment. Don't mix them up!"}
            },
            {
                "tip": {"de": "VK nur bei positiven Mittelwerten", "en": "CV only for positive means"},
                "why": {"de": "Division durch negative Werte macht VK sinnlos.", 
                       "en": "Division by negative values makes CV meaningless."}
            },
            {
                "tip": {"de": "Histogram: Fläche = Häufigkeit", "en": "Histogram: Area = Frequency"},
                "tip_formula": r"\text{Höhe} \ne f_j \text{ bei ungleichen Klassenbreiten!}",
                "why": {"de": "Balkenhöhe ≠ Häufigkeit bei variabler Klassenbreite.", 
                       "en": "Bar height ≠ Frequency with variable class width."}
            }
        ]
    }
}


# ==========================================
# 2. RENDER FUNCTION
# ==========================================
def render_subtopic_7_6(model):
    """7.6 Summary — ULTRATHINK Learn-Test-Learn Flow"""
    inject_equal_height_css()
    
    st.header(t(content_7_6["title"]))
    st.caption(t(content_7_6["subtitle"]))
    st.markdown("---")
    
    # === CHAPTER INTUITION (Grey Callout) ===
    st.markdown(f"""
<div style="background: #f4f4f5; border-left: 4px solid #a1a1aa; 
            padding: 12px 16px; border-radius: 8px; color: #3f3f46;">
<strong>{t(content_7_6["intuition"]["header"])}:</strong><br>
{t(content_7_6["intuition"]["text"])}
</div>
""", unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # === CHUNK 1: VISUAL TOOLS ===
    render_chunk_visual(model)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # === CHUNK 2: CENTRAL TENDENCY ===
    render_chunk_center(model)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # === CHUNK 3: DISPERSION ===
    render_chunk_dispersion(model)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # === CHUNK 4: BOXPLOT MECHANICS ===
    render_chunk_boxplot(model)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # === KEY FORMULAS ===
    render_key_formulas()
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # === DECISION TREE ===
    render_tool_wizard()
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # === ASK YOURSELF ===
    render_ask_yourself(
        header=content_7_6["ask_yourself"]["header"],
        questions=content_7_6["ask_yourself"]["questions"],
        conclusion=content_7_6["ask_yourself"]["conclusion"]
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # === EXAM ESSENTIALS ===
    render_exam_essentials(
        tips=content_7_6["exam_essentials"]["tips"],
        trap=content_7_6["exam_essentials"]["trap"],
        trap_rule=content_7_6["exam_essentials"]["trap_rule"]
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # === OFFICIAL EXAM QUESTIONS ===
    st.markdown(f"### {t({'de': 'Prüfungstraining', 'en': 'Exam Practice'})}")
    
    questions = get_all_questions_for_topic("7.6")
    
    for q_id, q in questions.items():
        with st.container(border=True):
            st.caption(q.get("source", ""))
            
            # Handle different question types
            if q.get("type") == "problem" or not q.get("options"):
                st.markdown(t(q["question"]), unsafe_allow_html=True)
                with st.expander(t({"de": "Lösung anzeigen", "en": "Show Solution"})):
                    st.markdown(t(q["solution"]), unsafe_allow_html=True)
            elif q.get("type") == "multi_stage":
                st.markdown(t(q.get("stem", {})), unsafe_allow_html=True)
                for part in q.get("parts", []):
                    st.markdown(f"---")
                    st.markdown(t(part["question"]), unsafe_allow_html=True)
                    with st.expander(t({"de": "Lösung", "en": "Solution"})):
                        st.markdown(t(part.get("solution", {})), unsafe_allow_html=True)
            else:
                opts = q.get("options", [])
                if opts and isinstance(opts[0], dict):
                    option_labels = [t(o) for o in opts]
                else:
                    option_labels = opts
                
                render_mcq(
                    key_suffix=f"7_6_{q_id}",
                    question_text=t(q["question"]),
                    options=option_labels,
                    correct_idx=q["correct_idx"],
                    solution_text_dict=q["solution"],
                    success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                    error_msg_dict={"de": "Falsch.", "en": "Incorrect."},
                    client=model,
                    ai_context=f"Descriptive Statistics Summary: {q_id}",
                    course_id="vwl",
                    topic_id="7",
                    subtopic_id="7.6",
                    question_id=q_id
                )
        st.markdown("<br>", unsafe_allow_html=True)


# ==========================================
# 3. CHUNK RENDER FUNCTIONS
# ==========================================

def render_chunk_visual(model):
    """Chunk 1: Visual Tools"""
    chunk = content_7_6["chunk_visual"]
    st.markdown(f"### {t(chunk['header'])}")
    
    # First comparison row: Histogram vs ECDF
    c1, c2 = st.columns(2, gap="medium")
    
    with c1:
        with st.container(border=True):
            comp = chunk["comparison_1"]["left"]
            st.markdown(f"**{t(comp['title'])}**")
            st.latex(comp["formula"])
            st.markdown("---")
            st.markdown(t(comp["insight"]), unsafe_allow_html=True)
    
    with c2:
        with st.container(border=True):
            comp = chunk["comparison_1"]["right"]
            st.markdown(f"**{t(comp['title'])}**")
            st.latex(comp["formula"])
            st.markdown("---")
            st.markdown(t(comp["insight"]), unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Second comparison row: Boxplot vs QQ-Plot
    c1, c2 = st.columns(2, gap="medium")
    
    with c1:
        with st.container(border=True):
            comp = chunk["comparison_2"]["left"]
            st.markdown(f"**{t(comp['title'])}**")
            st.latex(comp["formula"])
            st.markdown("---")
            st.markdown(t(comp["insight"]), unsafe_allow_html=True)
    
    with c2:
        with st.container(border=True):
            comp = chunk["comparison_2"]["right"]
            st.markdown(f"**{t(comp['title'])}**")
            st.latex(comp["formula"])
            st.markdown("---")
            st.markdown(t(comp["insight"]), unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Quick Check MCQ
    render_chunk_mcq(chunk, "visual", model)


def render_chunk_center(model):
    """Chunk 2: Central Tendency"""
    chunk = content_7_6["chunk_center"]
    st.markdown(f"### {t(chunk['header'])}")
    
    # 3-column layout for measures
    cols = st.columns(3, gap="medium")
    for col, f in zip(cols, chunk["formulas"]):
        with col:
            with st.container(border=True):
                st.markdown(f"**{t(f['name'])}**")
                st.latex(f["formula"])
                st.caption(t(f["when"]))
                st.caption(f"→ {t(f['example'])}")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Quick Check MCQ
    render_chunk_mcq(chunk, "center", model)


def render_chunk_dispersion(model):
    """Chunk 3: Dispersion"""
    chunk = content_7_6["chunk_dispersion"]
    st.markdown(f"### {t(chunk['header'])}")
    
    # 2x2 layout for dispersion measures
    formulas = chunk["formulas"]
    for i in range(0, len(formulas), 2):
        cols = st.columns(2, gap="medium")
        for j, col in enumerate(cols):
            if i + j < len(formulas):
                f = formulas[i + j]
                with col:
                    with st.container(border=True):
                        st.markdown(f"**{t(f['name'])}**")
                        st.latex(f["formula"])
                        st.caption(t(f["when"]))
                        st.caption(f"→ {t(f['example'])}")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Quick Check MCQ
    render_chunk_mcq(chunk, "dispersion", model)


def render_chunk_boxplot(model):
    """Chunk 4: Boxplot Mechanics"""
    chunk = content_7_6["chunk_boxplot"]
    st.markdown(f"### {t(chunk['header'])}")
    
    # Single formula with variables
    formula = chunk["formula"]
    render_single_formula(
        title=formula["title"],
        intuition=formula["intuition"],
        formula=formula["formula"],
        variables=formula["variables"],
        insight=formula["insight"]
    )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Whisker rule callout
    st.markdown(f"""
<div style="background: #f4f4f5; border-left: 4px solid #a1a1aa; 
            padding: 12px 16px; border-radius: 8px; color: #3f3f46;">
{t(chunk["whisker_rule"])}
</div>
""", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Quick Check MCQ
    render_chunk_mcq(chunk, "boxplot", model)


def render_chunk_mcq(chunk, chunk_id, model):
    """Render MCQ for a chunk"""
    mcq = chunk["mcq"]
    opts = [t(o) for o in mcq["options"]]
    
    with st.container(border=True):
        st.markdown(f"**{t({'de': 'Schnell-Check', 'en': 'Quick Check'})}**")
        
        render_mcq(
            key_suffix=f"7_6_{chunk_id}",
            question_text=t(mcq["question"]),
            options=opts,
            correct_idx=mcq["correct_idx"],
            solution_text_dict=mcq["solution"],
            success_msg_dict={"de": "Richtig!", "en": "Correct!"},
            error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
            client=model,
            ai_context=f"Descriptive Stats summary: {chunk_id} concepts",
            course_id="vwl",
            topic_id="7",
            subtopic_id="7.6",
            question_id=f"7_6_quick_{chunk_id}"
        )


def render_key_formulas():
    """Render all key formulas in a 2-column grid"""
    kf = content_7_6["key_formulas"]
    st.markdown(f"### {t(kf['header'])}")
    
    formulas = kf["formulas"]
    
    # 2-column layout
    for i in range(0, len(formulas), 2):
        cols = st.columns(2, gap="medium")
        for j, col in enumerate(cols):
            if i + j < len(formulas):
                f = formulas[i + j]
                with col:
                    with st.container(border=True):
                        st.markdown(f"**{t(f['name'])}**")
                        st.latex(f["formula"])
                        st.caption(t(f["when"]))
                        st.caption(f"→ {t(f['example'])}")


@st.fragment
def render_tool_wizard():
    """Interactive decision tree for tool selection"""
    dt = content_7_6["decision_tree"]
    st.markdown(f"### {t(dt['header'])}")
    
    with st.container(border=True):
        st.markdown(f"**{t(dt['root']['question'])}**")
        
        # Create options for radio
        options = dt["root"]["options"]
        option_labels = [t(opt["label"]) for opt in options]
        
        selected = st.radio(
            t({"de": "Wähle:", "en": "Choose:"}),
            options=option_labels,
            key="7_6_tool_wizard",
            horizontal=False,
            label_visibility="collapsed"
        )
        
        st.markdown("---")
        
        # Find selected option and show result
        for opt in options:
            if t(opt["label"]) == selected:
                st.markdown(f"**{t({'de': 'Empfehlung', 'en': 'Recommendation'})}:**")
                st.latex(opt["result_formula"])
                st.caption(t(opt["result_note"]))
                break
