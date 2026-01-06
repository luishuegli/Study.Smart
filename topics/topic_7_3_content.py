# Topic 7.3: Boxplot
# ULTRATHINK ENHANCED VERSION — "100x Material"
# The user should feel like they entered a Boxplot Building Simulation

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
    render_single_formula,
    render_definition,
    render_formula_breakdown,
)
from utils.layouts.foundation import (
    intuition_box,
    grey_callout,
    inject_equal_height_css,
    COLORS,
)
from data.exam_questions import get_question

# ==============================================================================
# SEMANTIC COLOR PALETTE (Matches Topic 7 conventions)
# ==============================================================================
COLOR_DATA = "#007AFF"       # Blue  — Regular data points
COLOR_QUARTILE = "#9B59B6"   # Purple — Quartiles (Q1, Q2, Q3)
COLOR_OUTLIER = "#FF4B4B"    # Red   — Outliers (the drama!)
COLOR_WHISKER = "#6B7280"    # Gray  — Whiskers (neutral)
COLOR_BOX = "#007AFF"        # Blue  — The box itself
COLOR_RESULT = "#16a34a"     # Green — Success/completion

# ==============================================================================
# CONTENT DICTIONARY — BILINGUAL (ULTRATHINK DEPTH)
# ==============================================================================

content_7_3 = {
    "title": {
        "de": "7.3 Boxplot",
        "en": "7.3 Box Plot"
    },
    "subtitle": {
        "de": "Fünf Zahlen, die alles sagen — und Ausreisser, die auffallen",
        "en": "Five Numbers That Tell Everything — And Outliers That Stand Out"
    },
    
    # =========================================================================
    # INTUITION — THE "DOCTOR'S VISIT" ANALOGY
    # =========================================================================
    "intuition": {
        "de": """<strong>Stell dir vor:</strong> Du gehst zum Arzt für einen Check-up. 
        Der Arzt könnte dir alle 50 Messwerte zeigen — Blutdruck jede Stunde, Herzfrequenz jede Minute, etc.
        <br><br>
        Stattdessen sagt er: „Hier sind <strong>5 Kennzahlen</strong>, die das Wichtigste zusammenfassen: 
        Minimum, unteres Viertel, Mitte, oberes Viertel, Maximum — und <strong>dieser eine Wert hier ist auffällig</strong>."
        <br><br>
        Genau das macht ein Boxplot: <strong>Eine ganze Datenreihe in 5 Zahlen plus Ausreisser</strong>. 
        Auf einen Blick siehst du Zentrum, Streuung und Problemfälle.""",
        
        "en": """<strong>Imagine:</strong> You go to the doctor for a check-up. 
        The doctor could show you all 50 measurements — blood pressure every hour, heart rate every minute, etc.
        <br><br>
        Instead, they say: "Here are <strong>5 key numbers</strong> that summarize everything: 
        Minimum, lower quarter, middle, upper quarter, maximum — and <strong>this one value here is unusual</strong>."
        <br><br>
        That's exactly what a boxplot does: <strong>An entire dataset in 5 numbers plus outliers</strong>. 
        At a glance, you see center, spread, and problem cases."""
    },
    
    # =========================================================================
    # DEFINITION — WHAT IS A BOXPLOT?
    # =========================================================================
    "definition": {
        "term": {"de": "Boxplot (Kastengrafik)", "en": "Box Plot (Box-and-Whisker Plot)"},
        "formal": {
            "de": "Ein Boxplot ist eine grafische Darstellung der Fünf-Zahlen-Zusammenfassung: Minimum, Q1, Median, Q3, Maximum — wobei Ausreisser separat als Punkte markiert werden.",
            "en": "A box plot is a graphical display of the five-number summary: Minimum, Q1, Median, Q3, Maximum — with outliers marked separately as points."
        },
        "plain": {
            "de": "Eine 'Schachtel mit Schnurrhaaren' — die Schachtel zeigt die mittleren 50%, die Schnurrhaare zeigen die Spannweite (ohne Ausreisser).",
            "en": "A 'box with whiskers' — the box shows the middle 50%, the whiskers show the range (excluding outliers)."
        }
    },
    
    # =========================================================================
    # ANATOMY — THE 5 PARTS (for breakdown utility)
    # =========================================================================
    "anatomy": {
        "header": {"de": "Anatomie des Boxplots", "en": "Anatomy of a Box Plot"},
        "parts": [
            {
                "name": {"de": "Der Median (Q2)", "en": "The Median (Q2)"},
                "symbol": r"Q_2 = \tilde{x}",
                "description": {
                    "de": "Die <strong>dicke Linie in der Mitte</strong> der Box. Sie teilt die Daten in zwei Hälften — 50% liegen darunter, 50% darüber.",
                    "en": "The <strong>thick line in the middle</strong> of the box. It splits the data in half — 50% below, 50% above."
                },
                "color": COLOR_QUARTILE
            },
            {
                "name": {"de": "Die Box (Q1 bis Q3)", "en": "The Box (Q1 to Q3)"},
                "symbol": r"\text{Box} = [Q_1, Q_3]",
                "description": {
                    "de": "Die <strong>Schachtel</strong> enthält die mittleren 50% aller Daten. Ihre Höhe ist der <strong>Interquartilsabstand (IQR)</strong>.",
                    "en": "The <strong>box</strong> contains the middle 50% of all data. Its height is the <strong>Interquartile Range (IQR)</strong>."
                },
                "color": COLOR_BOX
            },
            {
                "name": {"de": "Die Whisker (Schnurrhaare)", "en": "The Whiskers"},
                "symbol": r"\text{max}(x_i) \text{ mit } x_i \leq Q_3 + 1.5 \cdot \text{IQR}",
                "description": {
                    "de": "Die <strong>Linien</strong>, die aus der Box herausragen. Sie zeigen die <strong>Spannweite der 'normalen' Daten</strong> — bis zum letzten Wert, der noch kein Ausreisser ist.",
                    "en": "The <strong>lines</strong> extending from the box. They show the <strong>range of 'normal' data</strong> — up to the last value that's not yet an outlier."
                },
                "color": COLOR_WHISKER
            },
            {
                "name": {"de": "Die Ausreisser", "en": "The Outliers"},
                "symbol": r"x_i > Q_3 + 1.5 \cdot \text{IQR}",
                "description": {
                    "de": "<strong>Einzelne Punkte</strong> ausserhalb der Whisker. Diese Werte sind so extrem, dass sie separat markiert werden — sie verdienen besondere Aufmerksamkeit!",
                    "en": "<strong>Individual points</strong> beyond the whiskers. These values are so extreme they're marked separately — they deserve special attention!"
                },
                "color": COLOR_OUTLIER
            },
            {
                "name": {"de": "Der Interquartilsabstand (IQR)", "en": "The Interquartile Range (IQR)"},
                "symbol": r"\text{IQR} = Q_3 - Q_1",
                "description": {
                    "de": "Die <strong>Höhe der Box</strong>. Er misst, wie weit die mittleren 50% der Daten streuen — ein <strong>robustes Streuungsmass</strong>.",
                    "en": "The <strong>height of the box</strong>. It measures how spread out the middle 50% of data are — a <strong>robust measure of spread</strong>."
                },
                "color": COLOR_BOX
            }
        ]
    },
    
    # =========================================================================
    # IQR FORMULA (for single_formula utility)
    # =========================================================================
    "iqr_formula": {
        "header": {"de": "Der Interquartilsabstand (IQR)", "en": "The Interquartile Range (IQR)"},
        "intuition": {
            "de": "Wie breit ist die 'mittlere Hälfte' deiner Daten?",
            "en": "How wide is the 'middle half' of your data?"
        },
        "formula": r"\text{IQR} = Q_3 - Q_1",
        "variables": [
            {
                "symbol": r"\text{IQR}",
                "name": {"de": "Interquartilsabstand", "en": "Interquartile Range"},
                "description": {"de": "Die Spannweite der mittleren 50%", "en": "The spread of the middle 50%"}
            },
            {
                "symbol": r"Q_3",
                "name": {"de": "75%-Quantil", "en": "75th Percentile"},
                "description": {"de": "75% der Daten liegen darunter", "en": "75% of data lies below this"}
            },
            {
                "symbol": r"Q_1",
                "name": {"de": "25%-Quantil", "en": "25th Percentile"},
                "description": {"de": "25% der Daten liegen darunter", "en": "25% of data lies below this"}
            }
        ],
        "insight": {
            "de": "Der IQR ist <strong>robust gegen Ausreisser</strong> — im Gegensatz zur Spannweite (Max−Min), die von einem einzigen Extremwert stark beeinflusst wird.",
            "en": "The IQR is <strong>robust against outliers</strong> — unlike the range (Max−Min), which is heavily influenced by a single extreme value."
        }
    },
    
    # =========================================================================
    # WHISKER RULE — THE KEY CONCEPT
    # =========================================================================
    "whisker_rule": {
        "header": {"de": "Die 1.5×IQR-Regel", "en": "The 1.5×IQR Rule"},
        "intuition": {
            "de": "Wie entscheiden wir, was ein Ausreisser ist?",
            "en": "How do we decide what's an outlier?"
        },
        "formula": r"\text{Ausreisser, wenn: } x_i < Q_1 - 1.5 \cdot \text{IQR} \;\text{ oder }\; x_i > Q_3 + 1.5 \cdot \text{IQR}",
        "formula_en": r"\text{Outlier, if: } x_i < Q_1 - 1.5 \cdot \text{IQR} \;\text{ or }\; x_i > Q_3 + 1.5 \cdot \text{IQR}",
        "insight": {
            "de": "<strong>Warum 1.5?</strong> Bei normalverteilten Daten liegen etwa 99.3% innerhalb dieser Grenzen. Die 1.5 ist eine <strong>statistische Konvention</strong>, die gut funktioniert.",
            "en": "<strong>Why 1.5?</strong> For normally distributed data, about 99.3% falls within these bounds. The 1.5 is a <strong>statistical convention</strong> that works well."
        }
    },
    
    # =========================================================================
    # STEPS — HOW TO BUILD A BOXPLOT
    # =========================================================================
    "steps": {
        "header": {"de": "So baust du einen Boxplot", "en": "How to Build a Box Plot"},
        "intro": {
            "de": "5 Schritte — vom Datensatz zum fertigen Boxplot:",
            "en": "5 steps — from dataset to finished box plot:"
        },
        "steps": [
            {
                "title": {"de": "Daten sortieren", "en": "Sort the data"},
                "description": {
                    "de": "Ordne alle Werte von klein nach gross: $x_{(1)} \\leq x_{(2)} \\leq ... \\leq x_{(n)}$",
                    "en": "Arrange all values from smallest to largest: $x_{(1)} \\leq x_{(2)} \\leq ... \\leq x_{(n)}$"
                }
            },
            {
                "title": {"de": "Quartile berechnen", "en": "Calculate quartiles"},
                "description": {
                    "de": "Finde $Q_1$ (25%), $Q_2$ (50% = Median), $Q_3$ (75%) mit der Formel $K = \\alpha n + 1$",
                    "en": "Find $Q_1$ (25%), $Q_2$ (50% = Median), $Q_3$ (75%) using formula $K = \\alpha n + 1$"
                }
            },
            {
                "title": {"de": "IQR berechnen", "en": "Calculate IQR"},
                "description": {
                    "de": "$\\text{IQR} = Q_3 - Q_1$",
                    "en": "$\\text{IQR} = Q_3 - Q_1$"
                }
            },
            {
                "title": {"de": "Whisker-Grenzen finden", "en": "Find whisker limits"},
                "description": {
                    "de": "Untere Grenze: $Q_1 - 1.5 \\cdot \\text{IQR}$, Obere Grenze: $Q_3 + 1.5 \\cdot \\text{IQR}$",
                    "en": "Lower limit: $Q_1 - 1.5 \\cdot \\text{IQR}$, Upper limit: $Q_3 + 1.5 \\cdot \\text{IQR}$"
                }
            },
            {
                "title": {"de": "Whisker und Ausreisser bestimmen", "en": "Determine whiskers and outliers"},
                "description": {
                    "de": "Whisker enden beim <strong>letzten Datenpunkt</strong> innerhalb der Grenzen. Alles ausserhalb = Ausreisser (als Punkt markieren).",
                    "en": "Whiskers end at the <strong>last data point</strong> within limits. Anything beyond = outlier (mark as dot)."
                }
            }
        ]
    },
    
    # =========================================================================
    # WORKED EXAMPLE — DEVICE LIFESPAN (From Course Theory Example 7.3.1)
    # =========================================================================
    "worked_example": {
        "header": {"de": "Beispiel: Lebensdauer von 16 Geräten", "en": "Example: Lifespan of 16 Devices"},
        "problem": {
            "de": """<strong>Gegeben:</strong> Die Lebensdauer von 16 Geräten (in Monaten):
            <br><br>
            <code style="background:#f4f4f5; padding:8px; border-radius:4px; display:block; font-size:0.9em;">
            1.5, 3.5, 6.5, 11.5, 12.5, 14, 17, 17, 19, 20, 23.5, 32.5, 34.5, 39, 55.5, 119
            </code>
            <br>
            <strong>Frage:</strong> Erstelle einen Boxplot. Gibt es Ausreisser?""",
            "en": """<strong>Given:</strong> Lifespan of 16 devices (in months):
            <br><br>
            <code style="background:#f4f4f5; padding:8px; border-radius:4px; display:block; font-size:0.9em;">
            1.5, 3.5, 6.5, 11.5, 12.5, 14, 17, 17, 19, 20, 23.5, 32.5, 34.5, 39, 55.5, 119
            </code>
            <br>
            <strong>Question:</strong> Create a box plot. Are there outliers?"""
        },
        "steps": [
            {
                "label": {"de": "Schritt 1: Quartile finden", "en": "Step 1: Find quartiles"},
                "latex": r"Q_1 = \frac{x_{(4)} + x_{(5)}}{2} = \frac{{\color{#007AFF}11.5} + {\color{#007AFF}12.5}}{2} = {\color{#9B59B6}12}",
                "note": {"de": "Formel: K = αn + 1 = 0.25×16 + 1 = 5. Da K ganzzahlig → Mittelwert von Position 4 und 5 (die Werte 11.5 und 12.5)", "en": "Formula: K = αn + 1 = 0.25×16 + 1 = 5. Since K is integer → average of positions 4 and 5 (values 11.5 and 12.5)"}
            },
            {
                "label": {"de": "Median (Q2)", "en": "Median (Q2)"},
                "latex": r"Q_2 = \frac{x_{(8)} + x_{(9)}}{2} = \frac{{\color{#007AFF}17} + {\color{#007AFF}19}}{2} = {\color{#9B59B6}18}",
                "note": {"de": "K = 0.5×16 + 1 = 9 → Mittelwert von Position 8 und 9", "en": "K = 0.5×16 + 1 = 9 → average of positions 8 and 9"}
            },
            {
                "label": {"de": "Oberes Quartil (Q3)", "en": "Upper Quartile (Q3)"},
                "latex": r"Q_3 = \frac{x_{(12)} + x_{(13)}}{2} = \frac{{\color{#007AFF}32.5} + {\color{#007AFF}34.5}}{2} = {\color{#9B59B6}33.5}",
                "note": {"de": "K = 0.75×16 + 1 = 13 → Mittelwert von Position 12 und 13", "en": "K = 0.75×16 + 1 = 13 → average of positions 12 and 13"}
            },
            {
                "label": {"de": "Schritt 2: IQR berechnen", "en": "Step 2: Calculate IQR"},
                "latex": r"\text{IQR} = {\color{#9B59B6}Q_3} - {\color{#9B59B6}Q_1} = 33.5 - 12 = {\color{#007AFF}21.5}",
                "note": None
            },
            {
                "label": {"de": "Schritt 3: Obere Grenze", "en": "Step 3: Upper limit"},
                "latex": r"{\color{#9B59B6}Q_3} + 1.5 \cdot {\color{#007AFF}\text{IQR}} = 33.5 + 1.5 \times 21.5 = {\color{#6B7280}65.75}",
                "note": {"de": "Alles über 65.75 ist Ausreisser!", "en": "Anything above 65.75 is an outlier!"}
            },
            {
                "label": {"de": "Schritt 4: Ausreisser identifizieren", "en": "Step 4: Identify outliers"},
                "latex": r"x_{(16)} = {\color{#FF4B4B}119} > {\color{#6B7280}65.75} \;\Rightarrow\; {\color{#FF4B4B}\text{Ausreisser!}}",
                "latex_en": r"x_{(16)} = {\color{#FF4B4B}119} > {\color{#6B7280}65.75} \;\Rightarrow\; {\color{#FF4B4B}\text{Outlier!}}",
                "note": None
            }
        ],
        "answer": {
            "de": "Der Wert **119** ist ein **Ausreisser**. Das Gerät hatte eine ungewöhnlich lange Lebensdauer. Der obere Whisker endet bei **55.5** (dem letzten 'normalen' Wert).",
            "en": "The value **119** is an **outlier**. This device had an unusually long lifespan. The upper whisker ends at **55.5** (the last 'normal' value)."
        }
    },
    
    # =========================================================================
    # FRAG DICH — DECISION QUESTIONS
    # =========================================================================
    "frag_dich": {
        "header": {"de": "Frag dich: Verstehst du Boxplots?", "en": "Ask yourself: Do you understand box plots?"},
        "questions": [
            {
                "de": "Wo liegt der <strong>Median</strong> im Boxplot? Oben, Mitte oder unten der Box?",
                "en": "Where is the <strong>median</strong> in a box plot? Top, middle, or bottom of the box?"
            },
            {
                "de": "Die Whisker enden bei <strong>1.5×IQR</strong> — aber bedeutet das bei der Zahl 1.5×IQR oder beim letzten <strong>Datenpunkt</strong> davor?",
                "en": "Whiskers end at <strong>1.5×IQR</strong> — but does that mean at the value 1.5×IQR or at the last <strong>data point</strong> before it?"
            },
            {
                "de": "Kann ein Boxplot <strong>kein Ausreisser</strong> haben? Wann passiert das?",
                "en": "Can a box plot have <strong>no outliers</strong>? When does that happen?"
            },
            {
                "de": "Wenn Q<sub>1</sub> = 10 und Q<sub>3</sub> = 30, was ist der IQR? Was ist die obere Ausreisser-Grenze?",
                "en": "If Q<sub>1</sub> = 10 and Q<sub>3</sub> = 30, what is the IQR? What is the upper outlier boundary?"
            }
        ],
        "conclusion": {
            "de": "Median = Linie IN der Box | Whisker = letzter DATENPUNKT | IQR = 20, Grenze = 30 + 30 = 60",
            "en": "Median = line IN box | Whisker = last DATA POINT | IQR = 20, boundary = 30 + 30 = 60"
        }
    },
    
    # =========================================================================
    # EXAM ESSENTIALS — TRAP + TIPS
    # =========================================================================
    "exam_essentials": {
        "trap": {
            "de": "<strong>Whisker-Endpunkt ≠ 1.5×IQR-Grenze!</strong> Viele Studenten zeichnen den Whisker BIS zur berechneten Grenze (z.B. 65.75). <strong>FALSCH!</strong> Der Whisker endet beim <strong>letzten tatsächlichen Datenpunkt</strong> innerhalb der Grenze (z.B. 55.5).",
            "en": "<strong>Whisker endpoint ≠ 1.5×IQR boundary!</strong> Many students draw the whisker TO the calculated limit (e.g., 65.75). <strong>WRONG!</strong> The whisker ends at the <strong>last actual data point</strong> within the boundary (e.g., 55.5)."
        },
        "trap_formula": r"\text{Whisker} = \max(x_i : x_i \leq Q_3 + 1.5 \cdot \text{IQR}) \neq Q_3 + 1.5 \cdot \text{IQR}",
        "trap_rule": {
            "de": "Merke: Die Grenze ist ein <strong>Entscheidungskriterium</strong>, nicht das Whisker-Ende. Whisker zeigen immer auf echte Daten!",
            "en": "Remember: The boundary is a <strong>decision criterion</strong>, not the whisker endpoint. Whiskers always point to real data!"
        },
        "tips": [
            {
                "tip": {"de": "IQR für 'mittlere 50%'", "en": "IQR for 'middle 50%'"},
                "why": {
                    "de": "Wird nach dem 'Streuungsmass für die mittleren 50%' gefragt? Das ist der $\\text{IQR} = Q_3 - Q_1$.",
                    "en": "Asked for 'spread measure for the middle 50%'? That's the $\\text{IQR} = Q_3 - Q_1$."
                }
            },
            {
                "tip": {"de": "Symmetrie prüfen", "en": "Check symmetry"},
                "why": {
                    "de": "Liegt der Median ($Q_2$) genau in der Mitte der Box? Dann sind die Daten symmetrisch. Näher bei $Q_1$? Rechtsschiefe Verteilung.",
                    "en": "Is the median ($Q_2$) exactly in the middle of the box? Then data is symmetric. Closer to $Q_1$? Right-skewed distribution."
                }
            },
            {
                "tip": {"de": "Ausreisser zählen", "en": "Count outliers"},
                "why": {
                    "de": "In Prüfungen wird oft gefragt: 'Wie viele Ausreisser?' Zähle alle Punkte ausserhalb der Whisker.",
                    "en": "Exams often ask: 'How many outliers?' Count all points outside the whiskers."
                }
            }
        ]
    },
    
    # =========================================================================
    # INTERACTIVE MISSION — 100x MATERIAL
    # =========================================================================
    "mission": {
        "title": {"de": "Boxplot-Labor", "en": "Box Plot Laboratory"},
        "scenario": {
            "de": """<strong>Willkommen im Boxplot-Labor!</strong><br>
            Du bist Qualitätsingenieur in einer Elektronikfabrik. 
            Vor dir liegt eine Charge von 12 Bauteilen — du hast ihre Lebensdauer gemessen.<br>
            <strong>Deine Aufgabe:</strong> Erkunde, wie ein Boxplot auf verschiedene Datenverteilungen reagiert. 
            Füge Ausreisser hinzu, beobachte die Whisker, verstehe die 1.5×IQR-Regel in Aktion.""",
            "en": """<strong>Welcome to the Box Plot Laboratory!</strong><br>
            You're a quality engineer at an electronics factory. 
            Before you lies a batch of 12 components — you've measured their lifespan.<br>
            <strong>Your task:</strong> Explore how a box plot reacts to different data distributions. 
            Add outliers, observe the whiskers, understand the 1.5×IQR rule in action."""
        },
        "discovery": {
            "de": """<strong>Was du entdeckt hast:</strong><br>
            • Der Whisker springt NICHT zur 1.5×IQR-Grenze — er endet beim letzten <strong>echten Datenpunkt</strong><br>
            • Ein einzelner Extremwert verändert die Box NICHT (robust!)<br>
            • Die 1.5×IQR-Regel identifiziert automatisch 'verdächtige' Werte<br><br>
            <strong>Praxis-Tipp:</strong> Boxplots sind perfekt, um verschiedene Gruppen zu vergleichen (z.B. Maschinen A vs B) oder Ausreisser in grossen Datensätzen zu finden.""",
            "en": """<strong>What you discovered:</strong><br>
            • The whisker does NOT jump to the 1.5×IQR boundary — it ends at the last <strong>actual data point</strong><br>
            • A single extreme value does NOT change the box (robust!)<br>
            • The 1.5×IQR rule automatically identifies 'suspicious' values<br><br>
            <strong>Practical tip:</strong> Box plots are perfect for comparing different groups (e.g., Machine A vs B) or finding outliers in large datasets."""
        }
    }
}


# ==============================================================================
# INTERACTIVE: BOXPLOT LABORATORY — 100x MATERIAL
# ==============================================================================

@st.fragment
def boxplot_laboratory():
    """
    ULTRATHINK Interactive Element: Boxplot Laboratory
    
    The user said: "make this ridiculously good, 100x material"
    "the user should question if they are in a learning app or a boxplot building simulation"
    
    Features:
    - Real-time boxplot updates as user manipulates data
    - Visual breakdown of Q1, Q2, Q3, IQR, whiskers
    - Animated highlight when outlier threshold crossed
    - Live statistics panel showing all calculations
    - "Discovery Mode" completion when key insights demonstrated
    """
    
    # State initialization
    if "bp_lab_stage" not in st.session_state:
        st.session_state.bp_lab_stage = 0
    if "bp_lab_discoveries" not in st.session_state:
        st.session_state.bp_lab_discoveries = set()
    # NOTE: Slider value is auto-managed via key="bp_outlier_slider"
    # Do NOT create a separate state variable - causes jump-back bug!
    
    # Base data: 12 "normal" component lifespans (months)
    # Deliberately clustered to make outlier effect dramatic
    base_data = np.array([42, 45, 48, 50, 51, 52, 53, 54, 56, 58, 60, 63])
    
    # Scenario description (compact, premium feel)
    st.markdown(f"""
<div style="background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%); 
            border-left: 4px solid #007AFF; border-radius: 8px;
            padding: 16px; color: #1c1c1e;">
{t(content_7_3["mission"]["scenario"])}
</div>
""", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # === CONTROLS PANEL ===
    col_control, col_stats = st.columns([2, 1])
    
    with col_control:
        st.markdown(f"**{t({'de': 'Neues Bauteil hinzufügen', 'en': 'Add New Component'})}**")
        st.caption(t({
            "de": "Bewege den Regler, um ein 13. Bauteil mit variabler Lebensdauer hinzuzufügen:",
            "en": "Move the slider to add a 13th component with variable lifespan:"
        }))
        
        # Semantic slider coloring (Blue for data control)
        from utils.layouts.foundation import inject_slider_css
        inject_slider_css([
            {"label_contains": "Lebensdauer", "color": "#007AFF"},
            {"label_contains": "Lifespan", "color": "#007AFF"},
        ])
        
        # CORRECT PATTERN: Use key only, no value= parameter, no manual sync
        # Slider auto-syncs to st.session_state["bp_outlier_slider"]
        outlier_value = st.slider(
            t({"de": "Lebensdauer (Monate)", "en": "Lifespan (months)"}),
            min_value=20,
            max_value=150,
            value=50,  # Default only used on first render
            step=1,
            format="%d",
            key="bp_outlier_slider"
        )
        # DO NOT manually sync: st.session_state.X = outlier_value  <- CAUSES BUG
    
    # Combine data
    all_data = np.append(base_data, outlier_value)
    sorted_data = np.sort(all_data)
    n = len(sorted_data)
    
    # Calculate statistics (exact algorithm from course)
    def get_quantile(data, alpha):
        """Calculate quantile using course formula K = αn + 1"""
        n = len(data)
        k = alpha * n + 1
        if k == int(k):  # K is integer
            k = int(k)
            return 0.5 * (data[k-2] + data[k-1])  # Average of x_(K-1) and x_(K)
        else:  # K is not integer
            return data[int(np.ceil(k)) - 1]  # x_(⌈K⌉)
    
    q1 = get_quantile(sorted_data, 0.25)
    q2 = get_quantile(sorted_data, 0.50)  # Median
    q3 = get_quantile(sorted_data, 0.75)
    iqr = q3 - q1
    lower_fence = q1 - 1.5 * iqr
    upper_fence = q3 + 1.5 * iqr
    
    # Find whisker endpoints (actual data points, NOT fence values!)
    lower_whisker = sorted_data[sorted_data >= lower_fence].min() if any(sorted_data >= lower_fence) else sorted_data.min()
    upper_whisker = sorted_data[sorted_data <= upper_fence].max() if any(sorted_data <= upper_fence) else sorted_data.max()
    
    # Identify outliers
    outliers = sorted_data[(sorted_data < lower_fence) | (sorted_data > upper_fence)]
    is_outlier = outlier_value > upper_fence or outlier_value < lower_fence
    
    # Track discoveries
    if is_outlier and "outlier_found" not in st.session_state.bp_lab_discoveries:
        st.session_state.bp_lab_discoveries.add("outlier_found")
    if not is_outlier and "normal_added" not in st.session_state.bp_lab_discoveries:
        st.session_state.bp_lab_discoveries.add("normal_added")
    if upper_whisker != upper_fence and is_outlier and "whisker_jump" not in st.session_state.bp_lab_discoveries:
        st.session_state.bp_lab_discoveries.add("whisker_jump")
    
    # Track max explored value for completion
    max_explored_key = "bp_max_explored"
    if max_explored_key not in st.session_state:
        st.session_state[max_explored_key] = 50
    if outlier_value > st.session_state[max_explored_key]:
        st.session_state[max_explored_key] = outlier_value
    
    with col_stats:
        # Live Statistics Panel (WHITE background for clarity)
        fence_color = "#FF4B4B" if is_outlier else "#16a34a"
        st.markdown(f"""
<div style="background: #ffffff; border: 2px solid #e5e7eb; border-radius: 12px; padding: 16px; font-family: -apple-system, BlinkMacSystemFont, sans-serif;">
<div style="font-size: 0.7em; color: #6B7280; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 12px; font-weight: 600;">
{t({"de": "Live-Berechnungen", "en": "Live Calculations"})}
</div>
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px; font-size: 0.95em;">
<div style="color: #374151;"><span style="color:#9B59B6;font-weight:700">Q₁</span> = {q1:.1f}</div>
<div style="color: #374151;"><span style="color:#9B59B6;font-weight:700">Q₃</span> = {q3:.1f}</div>
<div style="color: #374151;"><span style="color:#9B59B6;font-weight:700">Q₂</span> = {q2:.1f}</div>
<div style="color: #007AFF; font-weight: 600;">IQR = {iqr:.1f}</div>
</div>
<hr style="border: none; border-top: 1px solid #e5e7eb; margin: 12px 0;">
<div style="font-size: 0.85em;">
<div style="color: #6B7280; font-size: 0.8em;">{t({"de": "Obere Grenze", "en": "Upper Fence"})}</div>
<div style="color: {fence_color}; font-size: 1.2em; font-weight: bold;">
{upper_fence:.1f}
</div>
<div style="color: #6B7280; font-size: 0.8em; margin-top: 8px;">{t({"de": "Oberer Whisker", "en": "Upper Whisker"})}</div>
<div style="color: #374151; font-size: 1.2em; font-weight: bold;">
{upper_whisker:.1f}
</div>
</div>
</div>
""", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # === MAIN VISUALIZATION ===
    fig = make_subplots(
        rows=1, cols=2,
        column_widths=[0.6, 0.4],
        subplot_titles=(
            t({"de": "Datenverteilung", "en": "Data Distribution"}),
            t({"de": "Boxplot", "en": "Box Plot"})
        ),
        horizontal_spacing=0.1
    )
    
    # Left: Dot plot showing all data points
    colors = [COLOR_OUTLIER if x in outliers else COLOR_DATA for x in sorted_data]
    sizes = [16 if x == outlier_value else 10 for x in sorted_data]
    
    fig.add_trace(
        go.Scatter(
            x=sorted_data,
            y=[1] * len(sorted_data),
            mode="markers",
            marker=dict(
                color=colors,
                size=sizes,
                line=dict(width=2, color="white"),
            ),
            hovertemplate="%{x:.1f} " + t({"de": "Monate", "en": "months"}) + "<extra></extra>",
            showlegend=False
        ),
        row=1, col=1
    )
    
    # Add fence lines on dot plot
    fig.add_vline(x=lower_fence, line_dash="dash", line_color=COLOR_WHISKER, 
                  annotation_text=f"Q₁-1.5·IQR = {lower_fence:.1f}", 
                  annotation_position="top left", row=1, col=1)
    fig.add_vline(x=upper_fence, line_dash="dash", line_color=COLOR_OUTLIER, 
                  annotation_text=f"Q₃+1.5·IQR = {upper_fence:.1f}", 
                  annotation_position="top right", row=1, col=1)
    
    # Shade outlier zones
    fig.add_vrect(x0=sorted_data.min() - 5, x1=lower_fence, 
                  fillcolor="rgba(255, 75, 75, 0.1)", layer="below", line_width=0, row=1, col=1)
    fig.add_vrect(x0=upper_fence, x1=sorted_data.max() + 5, 
                  fillcolor="rgba(255, 75, 75, 0.1)", layer="below", line_width=0, row=1, col=1)
    
    # Right: Actual Box Plot
    fig.add_trace(
        go.Box(
            y=sorted_data,
            boxpoints="outliers",
            jitter=0,
            marker=dict(color=COLOR_OUTLIER, size=12),
            line=dict(color=COLOR_BOX, width=2),
            fillcolor="rgba(0, 122, 255, 0.3)",
            name=t({"de": "Lebensdauer", "en": "Lifespan"}),
            hoverinfo="y",
            showlegend=False
        ),
        row=1, col=2
    )
    
    # Add Q1, Q2, Q3 annotations on boxplot
    fig.add_annotation(x=0.5, y=q1, text=f"Q₁={q1:.0f}", showarrow=False, 
                       xref="x2", yref="y2", xanchor="left", font=dict(size=11, color=COLOR_QUARTILE))
    fig.add_annotation(x=0.5, y=q2, text=f"Q₂={q2:.0f}", showarrow=False, 
                       xref="x2", yref="y2", xanchor="left", font=dict(size=11, color=COLOR_QUARTILE))
    fig.add_annotation(x=0.5, y=q3, text=f"Q₃={q3:.0f}", showarrow=False, 
                       xref="x2", yref="y2", xanchor="left", font=dict(size=11, color=COLOR_QUARTILE))
    
    # Layout - COMPACT height for better screen fit
    fig.update_layout(
        height=260,
        margin=dict(t=35, b=35, l=35, r=25),
        plot_bgcolor="white",
        paper_bgcolor="white",
        hovermode="closest",
        dragmode=False
    )
    
    fig.update_xaxes(title_text=t({"de": "Lebensdauer (Monate)", "en": "Lifespan (months)"}), 
                     showgrid=True, gridcolor="#e5e7eb", row=1, col=1)
    fig.update_yaxes(visible=False, row=1, col=1)
    fig.update_xaxes(visible=False, row=1, col=2)
    fig.update_yaxes(title_text=t({"de": "Monate", "en": "Months"}), 
                     showgrid=True, gridcolor="#e5e7eb", row=1, col=2)
    
    config = {'displayModeBar': False}
    st.plotly_chart(fig, use_container_width=True, config=config)
    
    # === DYNAMIC FEEDBACK ===
    if is_outlier:
        st.markdown(f"""
<div style="background: linear-gradient(90deg, rgba(255, 75, 75, 0.15) 0%, rgba(255, 75, 75, 0.05) 100%); 
            border-left: 4px solid #FF4B4B; border-radius: 8px; padding: 12px 16px;">
<strong style="color: #FF4B4B;">{t({"de": "Ausreisser erkannt!", "en": "Outlier Detected!"})}</strong><br>
<span style="color: #374151;">
{t({"de": f"Das Bauteil mit {outlier_value} Monaten liegt über der Grenze von {upper_fence:.1f}. Es wird als separater Punkt markiert.", 
    "en": f"The component with {outlier_value} months is above the limit of {upper_fence:.1f}. It's marked as a separate point."})}
</span>
</div>
""", unsafe_allow_html=True)
        
        # Show the KEY insight about whisker vs fence
        if upper_whisker < outlier_value:
            st.markdown(f"""
<div style="background: linear-gradient(90deg, rgba(155, 89, 182, 0.15) 0%, rgba(155, 89, 182, 0.05) 100%); 
            border-left: 4px solid #9B59B6; border-radius: 8px; padding: 12px 16px; margin-top: 8px;">
<strong style="color: #9B59B6;">{t({"de": "Beobachte den Whisker!", "en": "Watch the Whisker!"})}</strong><br>
<span style="color: #374151;">
{t({"de": f"Der obere Whisker endet bei <strong>{upper_whisker}</strong> (dem letzten 'normalen' Datenpunkt) — NICHT bei {upper_fence:.1f} (der Grenze). Das ist der häufigste Prüfungsfehler!", 
    "en": f"The upper whisker ends at <strong>{upper_whisker}</strong> (the last 'normal' data point) — NOT at {upper_fence:.1f} (the boundary). This is the most common exam mistake!"})}
</span>
</div>
""", unsafe_allow_html=True)
    else:
        st.markdown(f"""
<div style="background: linear-gradient(90deg, rgba(22, 163, 74, 0.15) 0%, rgba(22, 163, 74, 0.05) 100%); 
            border-left: 4px solid #16a34a; border-radius: 8px; padding: 12px 16px;">
<strong style="color: #16a34a;">{t({"de": "Normaler Bereich", "en": "Normal Range"})}</strong><br>
<span style="color: #374151;">
{t({"de": f"Das Bauteil mit {outlier_value} Monaten liegt innerhalb der Grenzen. Es wird in den Boxplot integriert.", 
    "en": f"The component with {outlier_value} months is within bounds. It's integrated into the box plot."})}
</span>
</div>
""", unsafe_allow_html=True)
    
    # === COMPLETION STATE ===
    discoveries_needed = 3
    discoveries_made = len(st.session_state.bp_lab_discoveries)
    
    if discoveries_made >= discoveries_needed:
        st.markdown("<br>", unsafe_allow_html=True)
        st.success(t({
            "de": "Labor-Experimente abgeschlossen! Du hast alle wichtigen Entdeckungen gemacht.",
            "en": "Lab experiments complete! You've made all the important discoveries."
        }))
        
        st.markdown(f"""
<div style="background: #f4f4f5; border-left: 4px solid #a1a1aa; border-radius: 8px; padding: 16px; color: #3f3f46;">
{t(content_7_3["mission"]["discovery"])}
</div>
""", unsafe_allow_html=True)
    else:
        # Progress indicator
        st.caption(t({
            "de": f"Entdeckungen: {discoveries_made}/{discoveries_needed} — Probiere verschiedene Werte aus!",
            "en": f"Discoveries: {discoveries_made}/{discoveries_needed} — Try different values!"
        }))


# ==============================================================================
# RENDER FUNCTION — MAIN PAGE STRUCTURE
# ==============================================================================

def render_subtopic_7_3(model):
    """7.3 Boxplot — ULTRATHINK Enhanced with 100x Material Interactive"""
    
    # Inject equal height CSS
    inject_equal_height_css()
    
    # === HEADER ===
    st.header(t(content_7_3["title"]))
    st.caption(t(content_7_3["subtitle"]))
    st.markdown("---")
    
    # === 1. INTUITION (The Doctor's Visit Analogy) ===
    intuition_box(content_7_3["intuition"])
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # === 2. DEFINITION ===
    defn = content_7_3["definition"]
    render_definition(
        term=defn["term"],
        formal=defn["formal"],
        plain=defn["plain"]
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # === 3. ANATOMY OF A BOXPLOT (ALL-IN-ONE COMPACT VIEW) ===
    st.markdown(f"### {t(content_7_3['anatomy']['header'])}")
    
    with st.container(border=True):
        # SVG diagram - BIGGER for clarity
        st.markdown(f"""
<div style="text-align: center; padding: 16px 0 20px 0;">
<svg viewBox="0 0 400 180" style="max-width: 100%; height: 200px;">
  <!-- Whisker lines -->
  <line x1="50" y1="80" x2="100" y2="80" stroke="#6B7280" stroke-width="2"/>
  <line x1="300" y1="80" x2="350" y2="80" stroke="#6B7280" stroke-width="2"/>
  <!-- Whisker caps -->
  <line x1="50" y1="60" x2="50" y2="100" stroke="#6B7280" stroke-width="2"/>
  <line x1="350" y1="60" x2="350" y2="100" stroke="#6B7280" stroke-width="2"/>
  <!-- Box -->
  <rect x="100" y="45" width="200" height="70" fill="rgba(0, 122, 255, 0.2)" stroke="#007AFF" stroke-width="2.5" rx="4"/>
  <!-- Median line -->
  <line x1="180" y1="45" x2="180" y2="115" stroke="#9B59B6" stroke-width="4"/>
  <!-- Outlier -->
  <circle cx="380" cy="80" r="8" fill="#FF4B4B" stroke="white" stroke-width="2"/>
  <!-- Labels -->
  <text x="50" y="135" text-anchor="middle" fill="#6B7280" font-size="12" font-weight="600">Min</text>
  <text x="100" y="135" text-anchor="middle" fill="#007AFF" font-size="12" font-weight="600">Q₁</text>
  <text x="180" y="30" text-anchor="middle" fill="#9B59B6" font-size="13" font-weight="700">Q₂</text>
  <text x="300" y="135" text-anchor="middle" fill="#007AFF" font-size="12" font-weight="600">Q₃</text>
  <text x="350" y="135" text-anchor="middle" fill="#6B7280" font-size="12" font-weight="600">Max*</text>
  <text x="380" y="110" text-anchor="middle" fill="#FF4B4B" font-size="11" font-weight="600">{t({"de": "Ausreisser", "en": "Outlier"})}</text>
  <!-- IQR bracket -->
  <path d="M100,150 L100,165 L300,165 L300,150" fill="none" stroke="#007AFF" stroke-width="1.5"/>
  <text x="200" y="178" text-anchor="middle" fill="#007AFF" font-size="12" font-weight="600">IQR = Q₃ − Q₁</text>
</svg>
</div>
<hr style="border: none; border-top: 1px solid #e5e7eb; margin: 0 0 16px 0;">
""", unsafe_allow_html=True)
        
        # 5 parts - looser spacing
        parts_html = ""
        for part in content_7_3["anatomy"]["parts"]:
            parts_html += f"""
<div style="display: flex; align-items: baseline; gap: 12px; margin-bottom: 10px; padding: 10px 14px; 
            background: #fafafa; border-radius: 6px; border-left: 3px solid {part['color']};">
<strong style="color: {part['color']}; font-size: 0.95em; white-space: nowrap;">{t(part['name'])}</strong>
<span style="color: #374151; font-size: 0.9em; line-height: 1.5;">{t(part['description'])}</span>
</div>
"""
        st.markdown(parts_html, unsafe_allow_html=True)
        st.caption(t({"de": "*Max ohne Ausreisser = oberer Whisker", "en": "*Max excluding outliers = upper whisker"}))
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # === 4. IQR FORMULA ===
    iqr = content_7_3["iqr_formula"]
    render_single_formula(
        title=iqr["header"],
        intuition=iqr["intuition"],
        formula=iqr["formula"],
        variables=iqr["variables"],
        insight=iqr["insight"]
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # === 5. THE 1.5×IQR RULE ===
    wr = content_7_3["whisker_rule"]
    st.markdown(f"### {t(wr['header'])}")
    with st.container(border=True):
        st.markdown(f"*{t(wr['intuition'])}*")
        if t({"de": "x", "en": "y"}) == "y" and "formula_en" in wr:
            st.latex(wr["formula_en"])
        else:
            st.latex(wr["formula"])
        st.markdown("---")
        st.markdown(f"""
<div style="background: #f4f4f5; border-left: 4px solid #a1a1aa; 
            padding: 12px 16px; border-radius: 8px; color: #3f3f46;">
{t(wr['insight'])}
</div>
""", unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # === 6. HOW TO BUILD A BOXPLOT (Steps) ===
    steps_content = content_7_3["steps"]
    st.markdown(f"### {t(steps_content['header'])}")
    
    with st.container(border=True):
        st.markdown(f"*{t(steps_content['intro'])}*")
        st.markdown("<br>", unsafe_allow_html=True)
        
        for i, step in enumerate(steps_content["steps"], 1):
            st.markdown(f"**{t({'de': 'Schritt', 'en': 'Step'})} {i}:** {t(step['title'])}")
            st.markdown(t(step["description"]), unsafe_allow_html=True)
            
            if i < len(steps_content["steps"]):
                st.markdown("---")
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # === 7. WORKED EXAMPLE ===
    we = content_7_3["worked_example"]
    render_worked_example(
        header=we["header"],
        problem=we["problem"],
        steps=we["steps"],
        answer=we["answer"]
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # === 8. INTERACTIVE: BOXPLOT LABORATORY (100x Material) ===
    st.markdown(f"### {t(content_7_3['mission']['title'])}")
    boxplot_laboratory()
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # === 9. FRAG DICH ===
    fd = content_7_3["frag_dich"]
    render_ask_yourself(
        header=fd["header"],
        questions=fd["questions"],
        conclusion=fd["conclusion"]
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # === 10. EXAM ESSENTIALS ===
    ee = content_7_3["exam_essentials"]
    render_exam_essentials(
        trap=ee["trap"],
        trap_formula=ee["trap_formula"],
        trap_rule=ee["trap_rule"],
        tips=ee["tips"]
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # === 11. MCQ PRACTICE ===
    st.markdown(f"### {t({'de': 'Prüfungstraining', 'en': 'Exam Practice'})}")
    
    # Try to get hs2015_prob1 if it exists
    q1 = get_question("7", "hs2015_prob1")
    if q1:
        st.caption(q1.get("source", "HS 2015"))
        with st.container(border=True):
            # Check if this is a problem type (not MCQ)
            if q1.get("type") == "problem" or not q1.get("options"):
                # Render as a read-through problem with solution toggle
                st.markdown(t(q1["question"]), unsafe_allow_html=True)
                
                # Solution toggle
                if st.button(t({"de": "Lösung anzeigen", "en": "Show Solution"}), key="show_solution_7_3"):
                    st.markdown("---")
                    st.markdown(t(q1.get("solution", {})), unsafe_allow_html=True)
            else:
                # MCQ rendering
                opts = q1.get("options", [])
                if opts and isinstance(opts[0], dict):
                    option_labels = [t(o) for o in opts]
                else:
                    option_labels = opts
                
                render_mcq(
                    key_suffix="7_3_boxplot",
                    question_text=t(q1["question"]),
                    options=option_labels,
                    correct_idx=q1.get("correct_idx", 0),
                    solution_text_dict=q1.get("solution", {}),
                    success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                    error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
                    client=model,
                    ai_context="Boxplot interpretation and outlier identification",
                    course_id="vwl",
                    topic_id="7",
                    subtopic_id="7.3",
                    question_id="7_3_boxplot"
                )
    else:
        # Fallback message if no question exists
        st.markdown(f"""
<div style="background: #f4f4f5; border-left: 4px solid #a1a1aa; 
            padding: 12px 16px; border-radius: 8px; color: #3f3f46;">
{t({"de": "Das Boxplot-Labor oben ist dein interaktives Training. Prüfungsfragen zu Boxplots erscheinen oft in Kombination mit Histogrammvergleichen.", 
    "en": "The Box Plot Laboratory above is your interactive training. Exam questions about box plots often appear in combination with histogram comparisons."})}
</div>
""", unsafe_allow_html=True)
