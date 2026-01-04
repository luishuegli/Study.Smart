# Topic 5.5: Summary — Multidimensional Random Variables
# ULTRATHINK REDESIGN: Learn-Test-Learn Chunked Pattern (like 4.9)
import streamlit as st
from views.styles import inject_equal_height_css
from utils.localization import t
from utils.quiz_helper import render_mcq
from utils.ask_yourself import render_ask_yourself
from utils.exam_essentials import render_exam_essentials
from utils.layouts import render_decision_tree
from data.exam_questions import get_question

# ==========================================
# 1. CONTENT DICTIONARY - CHUNKED BY CONCEPT
# ==========================================
content_5_5 = {
    "title": {"de": "5.5 Zusammenfassung", "en": "5.5 Summary"},
    "subtitle": {"de": "Mehrdimensionale Zufallsvariablen im Überblick", "en": "Multidimensional Random Variables at a Glance"},
    
    # --- CHAPTER INTUITION ---
    "intuition": {
        "header": {"de": "Das grosse Bild", "en": "The Big Picture"},
        "text": {
            "de": "Du hast gelernt, <strong>zwei Zufallsvariablen zusammen</strong> zu analysieren — wie sie gemeinsam verteilt sind, ob sie voneinander abhängen, und wie ihre Summen und Differenzen sich verhalten. Diese Zusammenfassung zeigt dir <strong>wann du welche Formel brauchst</strong> und die häufigsten Prüfungsfallen.",
            "en": "You've learned to analyze <strong>two random variables together</strong> — how they're jointly distributed, whether they depend on each other, and how their sums and differences behave. This summary shows you <strong>when to use which formula</strong> and the most common exam traps."
        }
    },
    
    # === CHUNK 1: BUILDING BLOCKS ===
    "chunk_building": {
        "header": {"de": "Baustein-Verteilungen", "en": "Building Block Distributions"},
        "formulas": [
            {
                "name": {"de": "Gemeinsam", "en": "Joint"}, 
                "formula": r"f_{X,Y}(x,y)",
                "when": {"de": "Wenn du beide Variablen gleichzeitig betrachtest", "en": "When you consider both variables simultaneously"},
                "example": {"de": "Eine Zelle in der Tabelle: P(X=1, Y=2)", "en": "One cell in the table: P(X=1, Y=2)"}
            },
            {
                "name": {"de": "Randverteilung", "en": "Marginal"}, 
                "formula": r"f_X(x) = \sum_y f_{X,Y}(x,y)",
                "when": {"de": "Wenn du nur eine Variable isoliert betrachtest", "en": "When you consider only one variable in isolation"},
                "example": {"de": "Zeilensumme für X, Spaltensumme für Y", "en": "Row sum for X, column sum for Y"}
            }
        ],
        "cards": [
            {
                "name": {"de": "Gemeinsame Verteilung", "en": "Joint Distribution"}, 
                "formula": r"f_{X,Y}(x,y)", 
                "oneliner": {"de": "Beide gleichzeitig — eine Zelle der Tabelle", "en": "Both at once — one cell of the table"}
            },
            {
                "name": {"de": "Randverteilung", "en": "Marginal Distribution"}, 
                "formula": r"f_X(x), f_Y(y)", 
                "oneliner": {"de": "Summiere über die andere Variable", "en": "Sum over the other variable"}
            }
        ],
        "mcq": {
            "question": {"de": "Wie findest du die Randverteilung von X aus einer gemeinsamen Tabelle?", "en": "How do you find the marginal distribution of X from a joint table?"},
            "options": [
                {"de": "Summiere über alle Y-Werte (Zeile)", "en": "Sum over all Y values (row)"},
                {"de": "Summiere über alle X-Werte (Spalte)", "en": "Sum over all X values (column)"},
                {"de": "Dividiere durch die Summe", "en": "Divide by the sum"},
                {"de": "Multipliziere die Randverteilungen", "en": "Multiply the marginals"}
            ],
            "correct_idx": 0,
            "solution": {"de": "Für die Randverteilung von X summierst du ÜBER alle Y-Werte einer Zeile. Für Y wäre es die Spalte!", "en": "For the marginal of X, you sum OVER all Y values in a row. For Y, it would be the column!"}
        }
    },
    
    # === CHUNK 2: RELATIONSHIPS ===
    "chunk_relationships": {
        "header": {"de": "Beziehungen zwischen Variablen", "en": "Relationships Between Variables"},
        "formulas": [
            {
                "name": {"de": "Bedingt", "en": "Conditional"}, 
                "formula": r"f_{X|Y}(x|y) = \frac{f_{X,Y}(x,y)}{f_Y(y)}",
                "when": {"de": "Wenn du wissen willst, wie sich X verhält, gegeben Y=y", "en": "When you want to know how X behaves, given that Y=y"},
                "example": {"de": "P(Note=1 | Lernzeit≥10h)", "en": "P(Grade=A | StudyTime≥10h)"}
            },
            {
                "name": {"de": "Unabhängigkeit", "en": "Independence"}, 
                "formula": r"f_{X,Y}(x,y) = f_X(x) \cdot f_Y(y)",
                "when": {"de": "Prüfen, ob Y Informationen über X liefert", "en": "Checking if Y provides information about X"},
                "example": {"de": "Gilt für ALLE Zellen: Zelle = Zeile × Spalte?", "en": "Does it hold for ALL cells: cell = row × column?"}
            }
        ],
        "cards": [
            {
                "name": {"de": "Bedingte Verteilung", "en": "Conditional Distribution"}, 
                "formula": r"f_{X|Y}(x|y)", 
                "oneliner": {"de": "Was ändert sich, wenn du Y kennst?", "en": "What changes if you know Y?"}
            },
            {
                "name": {"de": "Stochastische Unabhängigkeit", "en": "Stochastic Independence"}, 
                "formula": r"f = f_X \cdot f_Y", 
                "oneliner": {"de": "Y verrät nichts über X", "en": "Y reveals nothing about X"}
            },
            {
                "name": {"de": "Kovarianz", "en": "Covariance"}, 
                "formula": r"\text{Cov}(X,Y)", 
                "oneliner": {"de": "Nur Richtung, nicht skaliert", "en": "Direction only, not scaled"}
            },
            {
                "name": {"de": "Korrelation", "en": "Correlation"}, 
                "formula": r"\rho_{X,Y} \in [-1,1]", 
                "oneliner": {"de": "Richtung + Stärke (normiert)", "en": "Direction + Strength (normalized)"}
            }
        ],
        "mcq": {
            "question": {"de": "Wenn dies gilt, bedeutet das...", "en": "If this holds, it means..."},
            "question_formula": r"\text{Cov}(X,Y) = 0",
            "options": [
                {"de": "X und Y sind unabhängig", "en": "X and Y are independent"},
                {"de": "X und Y sind unkorreliert (kein linearer Zusammenhang)", "en": "X and Y are uncorrelated (no linear relationship)"},
                {"de": "X und Y haben keinen Zusammenhang", "en": "X and Y have no relationship"},
                {"de": "X = Y", "en": "X = Y"}
            ],
            "correct_idx": 1,
            "solution": {"de": "Klassische Falle! Cov = 0 bedeutet NUR 'unkorreliert'. Unabhängigkeit ist STÄRKER: Unabhängig → Cov = 0, aber NICHT umgekehrt!", "en": "Classic trap! Cov = 0 only means 'uncorrelated'. Independence is STRONGER: Independent → Cov = 0, but NOT vice versa!"}
        }
    },
    
    # === CHUNK 3: COMBINING VARIABLES ===
    "chunk_combining": {
        "header": {"de": "Variablen kombinieren", "en": "Combining Variables"},
        "formulas": [
            {
                "name": {"de": "Erwartungswert Summe", "en": "Expected Value Sum"}, 
                "formula": r"E[X+Y] = E[X] + E[Y]",
                "when": {"de": "Immer! Egal ob abhängig oder nicht", "en": "Always! Regardless of dependence"},
                "example": {"de": "E[Gewinn₁ + Gewinn₂] = E[Gewinn₁] + E[Gewinn₂]", "en": "E[Profit₁ + Profit₂] = E[Profit₁] + E[Profit₂]"}
            },
            {
                "name": {"de": "Varianz Summe", "en": "Variance Sum"}, 
                "formula": r"\text{Var}(X+Y) = \sigma_X^2 + \sigma_Y^2 + 2\text{Cov}",
                "when": {"de": "Wenn X und Y abhängig sind (oder unklar)", "en": "When X and Y are dependent (or unclear)"},
                "example": {"de": "Portfolio-Risiko mit korrelierten Aktien", "en": "Portfolio risk with correlated stocks"}
            },
            {
                "name": {"de": "Varianz Differenz", "en": "Variance Difference"}, 
                "formula": r"\text{Var}(X-Y) = \sigma_X^2 + \sigma_Y^2 - 2\text{Cov}",
                "when": {"de": "Minus nur beim Cov! Varianzen addieren sich", "en": "Minus only on Cov! Variances still add"},
                "example": {"de": "Var(Einnahmen - Ausgaben)", "en": "Var(Revenue - Expenses)"}
            }
        ],
        "cards": [
            {
                "name": {"de": "Erwartungswert", "en": "Expected Value"}, 
                "formula": r"E[X \pm Y]", 
                "oneliner": {"de": "Immer additiv — egal ob abhängig!", "en": "Always additive — regardless of dependence!"}
            },
            {
                "name": {"de": "Varianz Summe", "en": "Variance of Sum"}, 
                "formula": r"\text{Var}(X+Y)", 
                "oneliner": {"de": "Addiere + 2·Cov (Vorsicht Vorzeichen!)", "en": "Add + 2·Cov (watch the sign!)"}
            },
            {
                "name": {"de": "Varianz Differenz", "en": "Variance of Difference"}, 
                "formula": r"\text{Var}(X-Y)", 
                "oneliner": {"de": "Addiere - 2·Cov (Varianz ist immer positiv!)", "en": "Add - 2·Cov (variance is always positive!)"}
            }
        ],
        "mcq": {
            "question": {"de": "X, Y unabhängig. Gegeben:", "en": "X, Y independent. Given:"},
            "question_formula": r"\text{Var}(X) = 4, \quad \text{Var}(Y) = 9. \quad \text{Var}(X - Y) = ?",
            "options": [
                {"de": "13", "en": "13"},
                {"de": "-5", "en": "-5"},
                {"de": "5", "en": "5"},
                {"de": "Kann nicht berechnet werden", "en": "Cannot be calculated"}
            ],
            "correct_idx": 0,
            "solution": {"de": "Unabhängig → Cov = 0 → Var(X-Y) = Var(X) + Var(Y) = 4 + 9 = 13. Die Minus-Falle! Varianz ADDIERT sich immer!", "en": "Independent → Cov = 0 → Var(X-Y) = Var(X) + Var(Y) = 4 + 9 = 13. The minus trap! Variance ALWAYS adds!"}
        }
    },
    
    # === KEY FORMULAS (ALL) with context ===
    "key_formulas": {
        "header": {"de": "Formel-Übersicht", "en": "Formula Overview"},
        "formulas": [
            {
                "name": {"de": "Randverteilung", "en": "Marginal"}, 
                "formula": r"f_X(x) = \sum_y f_{X,Y}(x,y)",
                "when": {"de": "Variable isolieren", "en": "Isolate one variable"},
                "example": {"de": "Zeilensumme (für X) oder Spaltensumme (für Y)", "en": "Row sum (for X) or column sum (for Y)"}
            },
            {
                "name": {"de": "Bedingte Verteilung", "en": "Conditional"}, 
                "formula": r"f_{X|Y} = \frac{f_{X,Y}}{f_Y}",
                "when": {"de": "Verteilung von X, wenn Y bekannt", "en": "Distribution of X when Y is known"},
                "example": {"de": "Zelle ÷ Spaltensumme", "en": "Cell ÷ column total"}
            },
            {
                "name": {"de": "Unabhängigkeit", "en": "Independence"}, 
                "formula": r"f_{X,Y} = f_X \cdot f_Y",
                "when": {"de": "Prüfen ob X und Y unabhängig", "en": "Check if X and Y are independent"},
                "example": {"de": "JEDE Zelle = Zeile × Spalte?", "en": "EVERY cell = row × column?"}
            },
            {
                "name": {"de": "Kovarianz", "en": "Covariance"}, 
                "formula": r"\text{Cov} = E[XY] - E[X]E[Y]",
                "when": {"de": "Lineare Richtung messen", "en": "Measure linear direction"},
                "example": {"de": "Verschiebungssatz — schneller als Definition!", "en": "Shift formula — faster than definition!"}
            },
            {
                "name": {"de": "Korrelation", "en": "Correlation"}, 
                "formula": r"\rho = \frac{\text{Cov}}{\sigma_X \sigma_Y}",
                "when": {"de": "Lineare Stärke + Richtung (normiert)", "en": "Linear strength + direction (normalized)"},
                "example": {"de": "ρ = 0.8 → stark positiv linear", "en": "ρ = 0.8 → strong positive linear"}
            },
            {
                "name": {"de": "E[aX + bY]", "en": "E[aX + bY]"}, 
                "formula": r"a \cdot E[X] + b \cdot E[Y]",
                "when": {"de": "Erwartungswert linearer Kombination", "en": "Expected value of linear combination"},
                "example": {"de": "E[3X - 2Y] = 3E[X] - 2E[Y]", "en": "E[3X - 2Y] = 3E[X] - 2E[Y]"}
            },
            {
                "name": {"de": "Var(X+Y)", "en": "Var(X+Y)"}, 
                "formula": r"\sigma_X^2 + \sigma_Y^2 + 2\text{Cov}",
                "when": {"de": "Varianz einer Summe", "en": "Variance of a sum"},
                "example": {"de": "Falls unabhängig: Cov = 0 → nur addieren", "en": "If independent: Cov = 0 → just add"}
            },
            {
                "name": {"de": "Var(aX+b)", "en": "Var(aX+b)"}, 
                "formula": r"a^2 \cdot \text{Var}(X)",
                "when": {"de": "Varianz bei Skalierung", "en": "Variance under scaling"},
                "example": {"de": "Var(3X + 5) = 9·Var(X), Konstante fällt weg!", "en": "Var(3X + 5) = 9·Var(X), constant vanishes!"}
            }
        ]
    },
    
    # === ASK YOURSELF ===
    "ask_yourself": {
        "header": {"de": "Frag dich selbst", "en": "Ask Yourself"},
        "questions": [
            {"de": "Kannst du von Gemeinsam → Randverteilung gehen?", "en": "Can you go from Joint → Marginal?"},
            {"de": "Wie prüfst du Unabhängigkeit in einer Tabelle?", "en": "How do you check independence in a table?"},
            {"de": "Wann ist Var(X+Y) ≠ Var(X) + Var(Y)?", "en": "When is Var(X+Y) ≠ Var(X) + Var(Y)?"},
            {"de": "Cov = 0 bedeutet was genau? (Vorsicht!)", "en": "Cov = 0 means what exactly? (Careful!)"},
            {"de": "Warum ADDIERT sich die Varianz einer Differenz?", "en": "Why does variance of a difference ADD?"}
        ],
        "conclusion": {
            "de": "Wenn du alle beantworten kannst, bist du bereit für Prüfungsaufgaben zu Kapitel 5!",
            "en": "If you can answer all of these, you're ready for Chapter 5 exam questions!"
        }
    },
    
    # === EXAM ESSENTIALS (ALL TRAPS FROM 5.1-5.4) ===
    "exam_essentials": {
        "tips": [
            {
                "tip": {"de": "Für Randverteilung: Summiere ÜBER alle Werte der anderen Variable", "en": "For marginal: Sum OVER all values of the other variable"},
                "tip_formula": r"f_X(x) = \sum_y f_{X,Y}(x,y)",
                "why": {"de": "Die Richtung ist entscheidend! f_X → Zeile summieren, f_Y → Spalte summieren.", "en": "Direction matters! f_X → sum row, f_Y → sum column."}
            },
            {
                "tip": {"de": "Unabhängigkeit prüfen: Jede Zelle = Zeile × Spalte?", "en": "Check independence: Every cell = row × column?"},
                "tip_formula": r"f_{X,Y}(x,y) = f_X(x) \cdot f_Y(y) \quad \forall (x,y)",
                "why": {"de": "Alle Zellen müssen die Regel erfüllen, nicht nur eine!", "en": "ALL cells must satisfy the rule, not just one!"}
            },
            {
                "tip": {"de": "Verschiebungssatz für Kovarianz:", "en": "Shift formula for Covariance:"},
                "tip_formula": r"\text{Cov}(X,Y) = E[XY] - E[X] \cdot E[Y]",
                "why": {"de": "Prüfungs-Favorit! Weniger Rechenschritte als die Definition.", "en": "Exam favorite! Fewer calculation steps than the definition."}
            },
            {
                "tip": {"de": "Bei Summen/Differenzen: Varianz IMMER addieren!", "en": "For sums/differences: Variance ALWAYS adds!"},
                "tip_formula": r"\text{Var}(X-Y) = \text{Var}(X) + \text{Var}(Y) - 2\text{Cov}(X,Y)",
                "why": {"de": "Das Minus ist nur beim Cov-Term!", "en": "The minus is only on the Cov term!"}
            },
            {
                "tip": {"de": "Korrelation liegt immer im Intervall:", "en": "Correlation is always in the interval:"},
                "tip_formula": r"\rho_{X,Y} \in [-1, 1]",
                "why": {"de": "Wenn ausserhalb → Rechenfehler! Schneller Plausibilitäts-Check.", "en": "If outside → calculation error! Quick sanity check."}
            }
        ],
        "trap": {
            "de": "<strong>Die Cov = 0 Falle:</strong> Unkorreliert ≠ Unabhängig! Cov = 0 bedeutet nur 'kein linearer Zusammenhang'. Es kann trotzdem eine nicht-lineare Abhängigkeit bestehen.",
            "en": "<strong>The Cov = 0 Trap:</strong> Uncorrelated ≠ Independent! Cov = 0 only means 'no linear relationship'. There can still be a non-linear dependence."
        },
        "trap_rule": {
            "de": "Unabhängig → Cov = 0.  Aber:  Cov = 0 → NICHT unbedingt unabhängig!",
            "en": "Independent → Cov = 0.  But:  Cov = 0 → NOT necessarily independent!"
        }
    },
    
    # === DECISION TREE with LaTeX formulas ===
    "decision_tree": {
        "header": {"de": "Welche Formel brauchst du?", "en": "Which Formula Do You Need?"},
        "root": {
            "question": {"de": "Was wird gefragt?", "en": "What is being asked?"},
            "options": [
                {
                    "label": {"de": "Erwartungswert einer Kombination", "en": "Expected value of a combination"},
                    "result_formula": r"E[aX + bY] = a \cdot E[X] + b \cdot E[Y]",
                    "result_note": {"de": "Immer linear! Egal ob abhängig.", "en": "Always linear! Regardless of dependence."}
                },
                {
                    "label": {"de": "Varianz einer Summe/Differenz", "en": "Variance of a sum/difference"},
                    "next_question": {"de": "Sind X und Y unabhängig?", "en": "Are X and Y independent?"},
                    "branches": [
                        {
                            "condition": {"de": "Ja, unabhängig", "en": "Yes, independent"},
                            "result_formula": r"\text{Var}(X \pm Y) = \text{Var}(X) + \text{Var}(Y)",
                            "result_note": {"de": "Cov = 0, also fällt der Term weg", "en": "Cov = 0, so the term vanishes"}
                        },
                        {
                            "condition": {"de": "Nein / Nicht gesagt", "en": "No / Not stated"},
                            "result_formula": r"\text{Var}(X+Y) = \text{Var}(X) + \text{Var}(Y) + 2\text{Cov}(X,Y)",
                            "result_note": {"de": "Minus bei Differenz: -2Cov", "en": "Minus for difference: -2Cov"}
                        }
                    ]
                },
                {
                    "label": {"de": "Kovarianz berechnen", "en": "Calculate covariance"},
                    "result_formula": r"\text{Cov}(X,Y) = E[XY] - E[X] \cdot E[Y]",
                    "result_note": {"de": "Verschiebungssatz — Prüfungs-Favorit!", "en": "Shift formula — Exam favorite!"}
                },
                {
                    "label": {"de": "Korrelation berechnen", "en": "Calculate correlation"},
                    "result_formula": r"\rho_{X,Y} = \frac{\text{Cov}(X,Y)}{\sigma_X \cdot \sigma_Y}",
                    "result_note": {"de": "Normiert auf [-1, 1]", "en": "Normalized to [-1, 1]"}
                },
                {
                    "label": {"de": "Unabhängigkeit prüfen", "en": "Check independence"},
                    "result_formula": r"f_{X,Y}(x,y) = f_X(x) \cdot f_Y(y) \quad \forall (x,y)",
                    "result_note": {"de": "Muss für ALLE Zellen gelten!", "en": "Must hold for ALL cells!"}
                }
            ]
        }
    }
}


def render_subtopic_5_5(model):
    """5.5 Summary — ULTRATHINK Learn-Test-Learn Flow"""
    inject_equal_height_css()
    
    # --- CSS for equal height and styling ---
    st.markdown("""
    <style>
    [data-testid="stHorizontalBlock"] { align-items: stretch !important; }
    [data-testid="column"], [data-testid="stColumn"] { 
        display: flex !important; 
        flex-direction: column !important; 
    }
    [data-testid="column"] > div, [data-testid="stColumn"] > div { 
        flex: 1 !important; 
        display: flex !important; 
        flex-direction: column !important; 
        height: 100% !important; 
    }
    div[data-testid="stVerticalBlock"], 
    div[data-testid="stVerticalBlockBorderWrapper"] { 
        flex: 1 !important; 
        display: flex !important; 
        flex-direction: column !important; 
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.header(t(content_5_5["title"]))
    st.caption(t(content_5_5["subtitle"]))
    st.markdown("---")
    
    # === CHAPTER INTUITION ===
    st.markdown(f"""
<div style="background: #f4f4f5; border-left: 4px solid #a1a1aa; 
            padding: 12px 16px; border-radius: 8px; color: #3f3f46;">
<strong>{t(content_5_5["intuition"]["header"])}:</strong><br>
{t(content_5_5["intuition"]["text"])}
</div>
""", unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # === CHUNK 1: BUILDING BLOCKS ===
    render_chunk(content_5_5["chunk_building"], "building", model)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # === CHUNK 2: RELATIONSHIPS ===
    render_chunk(content_5_5["chunk_relationships"], "relationships", model)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # === CHUNK 3: COMBINING VARIABLES ===
    render_chunk(content_5_5["chunk_combining"], "combining", model)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # === KEY FORMULAS ===
    render_key_formulas()
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # === DECISION TREE (Interactive) ===
    render_formula_decision_tree()
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # === ASK YOURSELF ===
    render_ask_yourself(
        header=content_5_5["ask_yourself"]["header"],
        questions=content_5_5["ask_yourself"]["questions"],
        conclusion=content_5_5["ask_yourself"]["conclusion"]
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # === EXAM ESSENTIALS ===
    render_exam_essentials(
        tips=content_5_5["exam_essentials"]["tips"],
        trap=content_5_5["exam_essentials"]["trap"],
        trap_rule=content_5_5["exam_essentials"]["trap_rule"]
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # === ADDITIONAL EXAM QUESTIONS ===
    st.markdown(f"### {t({'de': 'Offizielle Prüfungsaufgaben', 'en': 'Official Exam Questions'})}")
    
    question_ids = [
        "uebung3_mc2", "uebung3_mc3", "uebung3_mc4", 
        "uebung3_mc6", "uebung3_mc8", "uebung3_mc12", "uebung3_mc13",
        "test3_mc3", "test3_mc4", "test4_mc2", "test5_mc2"
    ]
    
    for q_id in question_ids:
        q = get_question("5.5", q_id)
        if q:
            with st.container(border=True):
                st.caption(q.get("source", ""))
                opts = q.get("options", [])
                if opts and isinstance(opts[0], dict):
                    option_labels = [t(o) for o in opts]
                else:
                    option_labels = opts
                
                render_mcq(
                    key_suffix=f"5_5_{q_id}",
                    question_text=t(q["question"]),
                    options=option_labels,
                    correct_idx=q["correct_idx"],
                    solution_text_dict=q["solution"],
                    success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                    error_msg_dict={"de": "Falsch.", "en": "Incorrect."},
                    client=model,
                    ai_context=f"MultiVariate Summary: {q_id}",
                    course_id="vwl",
                    topic_id="5",
                    subtopic_id="5.5",
                    question_id=q_id
                )
            st.markdown("<br>", unsafe_allow_html=True)


def render_chunk(chunk, chunk_id, model):
    """Render a chunk: formulas first (with context), then compact cards with LaTeX, then MCQ"""
    st.markdown(f"### {t(chunk['header'])}")
    
    # --- FORMULAS PER CHUNK with when/example context ---
    if "formulas" in chunk:
        # Use max 2 columns per layout.md rule
        num_formulas = len(chunk["formulas"])
        if num_formulas <= 2:
            cols = st.columns(num_formulas, gap="medium")
        else:
            cols = st.columns(min(3, num_formulas), gap="medium")
        
        for col, f in zip(cols, chunk["formulas"]):
            with col:
                with st.container(border=True):
                    st.markdown(f"**{t(f['name'])}**")
                    st.latex(f["formula"])
                    if "when" in f:
                        st.caption(t(f['when']))
                    if "example" in f:
                        st.caption(f"→ {t(f['example'])}")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- Compact cards with PROPER LaTeX rendering ---
    # Use st.container with st.latex instead of raw HTML
    num_cards = len(chunk["cards"])
    card_cols = st.columns(num_cards, gap="small")
    for col, card in zip(card_cols, chunk["cards"]):
        with col:
            with st.container(border=True):
                st.markdown(f"**{t(card['name'])}**")
                st.latex(card["formula"])
                st.caption(t(card["oneliner"]))
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- MCQ immediately after ---
    mcq = chunk["mcq"]
    opts = [t(o) for o in mcq["options"]]
    
    with st.container(border=True):
        st.markdown(f"**{t({'de': 'Schnell-Check', 'en': 'Quick Check'})}**")
        
        # Render question formula if present
        if "question_formula" in mcq:
            st.latex(mcq["question_formula"])
        
        render_mcq(
            key_suffix=f"5_5_{chunk_id}",
            question_text=t(mcq["question"]),
            options=opts,
            correct_idx=mcq["correct_idx"],
            solution_text_dict=mcq["solution"],
            success_msg_dict={"de": "Richtig!", "en": "Correct!"},
            error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
            client=model,
            ai_context=f"Chapter 5 summary: {chunk_id} concepts",
            course_id="vwl",
            topic_id="5",
            subtopic_id="5.5",
            question_id=f"5_5_quick_{chunk_id}"
        )


def render_key_formulas():
    """Render all key formulas in a compact 2-column grid with when/example"""
    kf = content_5_5["key_formulas"]
    st.markdown(f"### {t(kf['header'])}")
    
    formulas = kf["formulas"]
    
    # 2-column layout (max 2 per layout.md rule)
    for i in range(0, len(formulas), 2):
        cols = st.columns(2, gap="medium")
        for j, col in enumerate(cols):
            if i + j < len(formulas):
                f = formulas[i + j]
                with col:
                    with st.container(border=True):
                        st.markdown(f"**{t(f['name'])}**")
                        st.latex(f["formula"])
                        st.caption(t(f['when']))
                        st.caption(f"→ {t(f['example'])}")


@st.fragment
def render_formula_decision_tree():
    """Interactive decision tree for formula selection with LaTeX formulas"""
    dt = content_5_5["decision_tree"]
    st.markdown(f"### {t(dt['header'])}")
    
    with st.container(border=True):
        st.markdown(f"**{t(dt['root']['question'])}**")
        
        # Create options for pills
        options = dt["root"]["options"]
        option_labels = [t(opt["label"]) for opt in options]
        
        selected = st.radio(
            t({"de": "Wähle:", "en": "Choose:"}),
            options=option_labels,
            key="5_5_decision_tree",
            horizontal=False,
            label_visibility="collapsed"
        )
        
        st.markdown("---")
        
        # Find selected option and show result with LaTeX
        for opt in options:
            if t(opt["label"]) == selected:
                if "result_formula" in opt:
                    st.markdown(f"**{t({'de': 'Formel', 'en': 'Formula'})}:**")
                    st.latex(opt["result_formula"])
                    if "result_note" in opt:
                        st.caption(t(opt['result_note']))
                elif "next_question" in opt:
                    # Second-level question
                    st.markdown(f"**{t(opt['next_question'])}**")
                    
                    branch_labels = [t(b["condition"]) for b in opt["branches"]]
                    branch_selected = st.radio(
                        t({"de": "Bedingung:", "en": "Condition:"}),
                        options=branch_labels,
                        key="5_5_decision_tree_branch",
                        horizontal=True,
                        label_visibility="collapsed"
                    )
                    
                    for branch in opt["branches"]:
                        if t(branch["condition"]) == branch_selected:
                            st.markdown(f"**{t({'de': 'Formel', 'en': 'Formula'})}:**")
                            st.latex(branch["result_formula"])
                            if "result_note" in branch:
                                st.caption(t(branch['result_note']))
                break
