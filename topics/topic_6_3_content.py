# Topic 6.3: Summary — Central Limit Theorem
# ULTRATHINK IMPLEMENTATION: Learn-Test-Learn Chunked Pattern (like 5.5)
import streamlit as st
from utils.localization import t
from utils.quiz_helper import render_mcq
from utils.ask_yourself import render_ask_yourself
from utils.exam_essentials import render_exam_essentials
from utils.layouts import (
    render_comparison,
    render_formula_grid,
    render_definition,
    render_decision_tree,
)
from utils.layouts.foundation import inject_equal_height_css
from data.exam_questions import get_all_questions_for_topic

# ==========================================
# 1. CONTENT DICTIONARY - BILINGUAL (ULTRATHINK)
# ==========================================
content_6_3 = {
    "title": {"de": "6.3 Zusammenfassung", "en": "6.3 Summary"},
    "subtitle": {"de": "Der zentrale Grenzwertsatz im Überblick", "en": "The Central Limit Theorem at a Glance"},
    
    # --- CHAPTER INTUITION ---
    "intuition": {
        "header": {"de": "Das grosse Bild", "en": "The Big Picture"},
        "text": {
            "de": "Du hast das <strong>mächtigste Werkzeug der Statistik</strong> kennengelernt: Der zentrale Grenzwertsatz (ZGS) erlaubt dir, <strong>jede Verteilung</strong> mit der Normalverteilung zu approximieren — wenn die Stichprobe gross genug ist. Diese Zusammenfassung zeigt dir, <strong>welche Formel wann</strong> und die häufigsten Prüfungsfallen.",
            "en": "You've learned the <strong>most powerful tool in statistics</strong>: The Central Limit Theorem (CLT) allows you to approximate <strong>any distribution</strong> with the Normal distribution — if the sample is large enough. This summary shows you <strong>which formula when</strong> and the most common exam traps."
        }
    },
    
    # === CHUNK 1: SUM VS MEAN ===
    "chunk_sum_mean": {
        "header": {"de": "Summe vs. Mittelwert", "en": "Sum vs. Mean"},
        "comparison": {
            "left": {
                "title": {"de": "Die Summe", "en": "The Sum"},
                "formula": r"S_n = \sum_{i=1}^{n} X_i",
                "distribution_formula": r"S_n \approx N(n\mu, n\sigma^2)",
                "insight": {
                    "de": "Varianz <strong>wächst</strong> mit n. Mehr Würfe = mehr Streuung im Total!",
                    "en": "Variance <strong>grows</strong> with n. More rolls = more spread in the total!"
                }
            },
            "right": {
                "title": {"de": "Der Mittelwert", "en": "The Mean"},
                "formula": r"\bar{X} = \frac{1}{n}\sum_{i=1}^{n} X_i",
                "distribution_formula": r"\bar{X} \approx N\left(\mu, \frac{\sigma^2}{n}\right)",
                "insight": {
                    "de": "Varianz <strong>schrumpft</strong> mit n. Grössere Stichprobe = präzisere Schätzung!",
                    "en": "Variance <strong>shrinks</strong> with n. Larger sample = more precise estimate!"
                }
            }
        },
        "mcq": {
            "question": {"de": "Wenn n grösser wird, was passiert mit der Varianz des Stichprobenmittelwerts?", "en": "As n increases, what happens to the variance of the sample mean?"},
            "options": [
                {"de": "Sie wächst proportional zu n", "en": "It grows proportionally to n"},
                {"de": "Sie schrumpft proportional zu 1/n", "en": "It shrinks proportionally to 1/n"},
                {"de": "Sie bleibt gleich", "en": "It stays the same"},
                {"de": "Sie wird negativ", "en": "It becomes negative"}
            ],
            "correct_idx": 1,
            "solution": {
                "de": "Die Varianz des Mittelwerts ist σ²/n — je grösser n, desto kleiner die Varianz. Das ist der Präzisionsgewinn durch grössere Stichproben!",
                "en": "The variance of the mean is σ²/n — the larger n, the smaller the variance. This is the precision gain from larger samples!"
            }
        }
    },
    
    # === CHUNK 2: STANDARDIZATION ===
    "chunk_standardization": {
        "header": {"de": "Standardisierung", "en": "Standardization"},
        "formulas": [
            {
                "name": {"de": "Summe standardisieren", "en": "Standardize Sum"},
                "formula": r"Z = \frac{S_n - n\mu}{\sigma\sqrt{n}}",
                "when": {"de": "Wenn du die Wahrscheinlichkeit einer Summe suchst", "en": "When you need the probability of a sum"},
                "example": {"de": "P(Gesamtgewinn > 100)", "en": "P(Total profit > 100)"}
            },
            {
                "name": {"de": "Mittelwert standardisieren", "en": "Standardize Mean"},
                "formula": r"Z = \frac{\bar{X} - \mu}{\sigma / \sqrt{n}}",
                "when": {"de": "Wenn du die Wahrscheinlichkeit eines Durchschnitts suchst", "en": "When you need the probability of an average"},
                "example": {"de": "P(Durchschnittsgewicht < 80kg)", "en": "P(Average weight < 80kg)"}
            }
        ],
        "mcq": {
            "question": {"de": "Um die Summe zu standardisieren, teilst du durch...", "en": "To standardize the sum, you divide by..."},
            "options": [
                {"de": r"$\sigma$", "en": r"$\sigma$"},
                {"de": r"$\sigma\sqrt{n}$", "en": r"$\sigma\sqrt{n}$"},
                {"de": r"$\sigma/\sqrt{n}$", "en": r"$\sigma/\sqrt{n}$"},
                {"de": r"$n\sigma$", "en": r"$n\sigma$"}
            ],
            "correct_idx": 1,
            "solution": {
                "de": r"Die Standardabweichung der Summe ist $\sigma\sqrt{n}$ (Varianz ist $n\sigma^2$). Der Nenner ist IMMER die Standardabweichung der Grösse, die du standardisierst!",
                "en": r"The standard deviation of the sum is $\sigma\sqrt{n}$ (variance is $n\sigma^2$). The denominator is ALWAYS the standard deviation of the quantity you're standardizing!"
            }
        }
    },
    
    # === CHUNK 3: DE MOIVRE-LAPLACE ===
    "chunk_demoivre": {
        "header": {"de": "De Moivre-Laplace & Korrektur", "en": "De Moivre-Laplace & Correction"},
        "comparison": {
            "left": {
                "title": {"de": "Ohne Korrektur", "en": "Without Correction"},
                "formula": r"Z = \frac{X - np}{\sqrt{np(1-p)}}",
                "insight": {
                    "de": "Schneller, aber <strong>weniger genau</strong>",
                    "en": "Faster, but <strong>less accurate</strong>"
                }
            },
            "right": {
                "title": {"de": "Mit Korrektur (Prüfung!)", "en": "With Correction (Exam!)"},
                "formula": r"Z = \frac{X \pm 0.5 - np}{\sqrt{np(1-p)}}",
                "insight": {
                    "de": "<strong>Standard für Prüfungen!</strong> Genauere Approximation",
                    "en": "<strong>Exam standard!</strong> More accurate approximation"
                }
            }
        },
        "mnemonic": {
            "header": {"de": "Welche Richtung?", "en": "Which Direction?"},
            "rows": [
                {"want": r"P(X \geq k)", "adjust": r"k - 0.5", "reason": {"de": "Intervall nach links erweitern", "en": "Extend interval leftward"}},
                {"want": r"P(X \leq k)", "adjust": r"k + 0.5", "reason": {"de": "Intervall nach rechts erweitern", "en": "Extend interval rightward"}},
                {"want": r"P(X > k)", "adjust": r"k + 0.5", "reason": {"de": "k selbst ausschliessen", "en": "Exclude k itself"}},
                {"want": r"P(X < k)", "adjust": r"k - 0.5", "reason": {"de": "k selbst ausschliessen", "en": "Exclude k itself"}}
            ]
        },
        "mcq": {
            "question": {"de": "Für P(X ≥ 60) mit Stetigkeitskorrektur, welchen Wert verwendest du?", "en": "For P(X ≥ 60) with continuity correction, which value do you use?"},
            "options": [
                {"de": "60.5", "en": "60.5"},
                {"de": "59.5", "en": "59.5"},
                {"de": "60", "en": "60"},
                {"de": "61", "en": "61"}
            ],
            "correct_idx": 1,
            "solution": {
                "de": "P(X ≥ k) → k - 0.5 = 59.5. Du erweiterst das Intervall nach LINKS, um den diskreten Wert 60 vollständig einzuschliessen!",
                "en": "P(X ≥ k) → k - 0.5 = 59.5. You extend the interval LEFTWARD to fully include the discrete value 60!"
            }
        }
    },
    
    # === CHUNK 4: i.i.d. CONDITIONS ===
    "chunk_iid": {
        "header": {"de": "Wann gilt der ZGS?", "en": "When Does CLT Apply?"},
        "definition": {
            "term": {"de": "i.i.d. (unabhängig und identisch verteilt)", "en": "i.i.d. (independent and identically distributed)"},
            "conditions": [
                {
                    "name": {"de": "Unabhängig", "en": "Independent"},
                    "explanation": {"de": "Wissen über eine Variable sagt NICHTS über die anderen aus", "en": "Knowing one variable tells you NOTHING about the others"},
                    "example": {"de": "Würfelwürfe beeinflussen sich nicht gegenseitig", "en": "Dice rolls don't influence each other"}
                },
                {
                    "name": {"de": "Identisch verteilt", "en": "Identically distributed"},
                    "explanation": {"de": "Alle Variablen haben die GLEICHE Verteilung (gleiche μ, gleiche σ²)", "en": "All variables have the SAME distribution (same μ, same σ²)"},
                    "example": {"de": "Alle Würfe mit demselben fairen Würfel", "en": "All rolls with the same fair die"}
                },
                {
                    "name": {"de": "Grosses n", "en": "Large n"},
                    "explanation": {"de": "Faustregel: n ≥ 30 (oder np ≥ 5 und n(1-p) ≥ 5 für Binomial)", "en": "Rule of thumb: n ≥ 30 (or np ≥ 5 and n(1-p) ≥ 5 for Binomial)"},
                    "example": {"de": "Bei n = 100 ist die Approximation sehr gut", "en": "With n = 100, the approximation is very good"}
                }
            ]
        },
        "mcq": {
            "question": {"de": "Welche Situation verletzt die i.i.d.-Bedingung?", "en": "Which situation violates the i.i.d. condition?"},
            "options": [
                {"de": "100 Würfe mit demselben Würfel", "en": "100 rolls with the same die"},
                {"de": "Gewichte von 50 zufällig ausgewählten Studenten", "en": "Weights of 50 randomly selected students"},
                {"de": "Aktienkurse an aufeinanderfolgenden Tagen", "en": "Stock prices on consecutive days"},
                {"de": "Stichprobe mit Zurücklegen aus einer Urne", "en": "Sample with replacement from an urn"}
            ],
            "correct_idx": 2,
            "solution": {
                "de": "Aktienkurse sind ABHÄNGIG (der Kurs heute beeinflusst den Kurs morgen) und oft NICHT identisch verteilt. Die anderen Beispiele erfüllen i.i.d.!",
                "en": "Stock prices are DEPENDENT (today's price influences tomorrow's) and often NOT identically distributed. The other examples satisfy i.i.d.!"
            }
        }
    },
    
    # === KEY FORMULAS ===
    "key_formulas": {
        "header": {"de": "Formel-Übersicht", "en": "Formula Overview"},
        "formulas": [
            {
                "name": {"de": "ZGS Summe", "en": "CLT Sum"},
                "formula": r"S_n \approx N(n\mu, n\sigma^2)",
                "when": {"de": "Summe von i.i.d. Variablen", "en": "Sum of i.i.d. variables"},
                "example": {"de": "Gesamtgewinn nach n Spielen", "en": "Total profit after n games"}
            },
            {
                "name": {"de": "ZGS Mittelwert", "en": "CLT Mean"},
                "formula": r"\bar{X} \approx N\left(\mu, \frac{\sigma^2}{n}\right)",
                "when": {"de": "Stichprobenmittelwert", "en": "Sample mean"},
                "example": {"de": "Durchschnittsgewicht einer Stichprobe", "en": "Average weight of a sample"}
            },
            {
                "name": {"de": "Standardisierung Summe", "en": "Standardize Sum"},
                "formula": r"Z = \frac{S_n - n\mu}{\sigma\sqrt{n}}",
                "when": {"de": "Summe auf Z-Tabelle", "en": "Sum to Z-table"},
                "example": {"de": "P(Summe > k) berechnen", "en": "Calculate P(Sum > k)"}
            },
            {
                "name": {"de": "Standardisierung Mittelwert", "en": "Standardize Mean"},
                "formula": r"Z = \frac{\bar{X} - \mu}{\sigma / \sqrt{n}}",
                "when": {"de": "Mittelwert auf Z-Tabelle", "en": "Mean to Z-table"},
                "example": {"de": "P(Durchschnitt < k) berechnen", "en": "Calculate P(Average < k)"}
            },
            {
                "name": {"de": "De Moivre-Laplace", "en": "De Moivre-Laplace"},
                "formula": r"Z = \frac{X - np}{\sqrt{np(1-p)}}",
                "when": {"de": "Binomial mit grossem n", "en": "Binomial with large n"},
                "example": {"de": "P(Anzahl Erfolge ≥ k)", "en": "P(Number of successes ≥ k)"}
            },
            {
                "name": {"de": "Stetigkeitskorrektur", "en": "Continuity Correction"},
                "formula": r"X \pm 0.5",
                "when": {"de": "Diskret → Stetig", "en": "Discrete → Continuous"},
                "example": {"de": "P(X ≥ k) → P(X ≥ k-0.5)", "en": "P(X ≥ k) → P(X ≥ k-0.5)"}
            }
        ]
    },
    
    # === DECISION TREE ===
    "decision_tree": {
        "header": {"de": "Welche Formel brauchst du?", "en": "Which Formula Do You Need?"},
        "root": {
            "question": {"de": "Was für Daten hast du?", "en": "What kind of data do you have?"},
            "options": [
                {
                    "label": {"de": "Summe von i.i.d. Variablen", "en": "Sum of i.i.d. variables"},
                    "result_formula": r"S_n \approx N(n\mu, n\sigma^2), \quad Z = \frac{S_n - n\mu}{\sigma\sqrt{n}}",
                    "result_note": {"de": "Varianz WÄCHST mit n!", "en": "Variance GROWS with n!"}
                },
                {
                    "label": {"de": "Mittelwert von i.i.d. Variablen", "en": "Mean of i.i.d. variables"},
                    "result_formula": r"\bar{X} \approx N\left(\mu, \frac{\sigma^2}{n}\right), \quad Z = \frac{\bar{X} - \mu}{\sigma/\sqrt{n}}",
                    "result_note": {"de": "Varianz SCHRUMPFT mit n!", "en": "Variance SHRINKS with n!"}
                },
                {
                    "label": {"de": "Binomialverteilung (Anzahl Erfolge)", "en": "Binomial distribution (number of successes)"},
                    "next_question": {"de": "Brauchst du Stetigkeitskorrektur?", "en": "Do you need continuity correction?"},
                    "branches": [
                        {
                            "condition": {"de": "Ja (Standard für Prüfung)", "en": "Yes (Exam standard)"},
                            "result_formula": r"Z = \frac{X \pm 0.5 - np}{\sqrt{np(1-p)}}",
                            "result_note": {"de": "P(X ≥ k) → k-0.5, P(X ≤ k) → k+0.5", "en": "P(X ≥ k) → k-0.5, P(X ≤ k) → k+0.5"}
                        },
                        {
                            "condition": {"de": "Nein (schnelle Schätzung)", "en": "No (quick estimate)"},
                            "result_formula": r"Z = \frac{X - np}{\sqrt{np(1-p)}}",
                            "result_note": {"de": "Weniger genau, aber akzeptabel für grosse n", "en": "Less accurate, but acceptable for large n"}
                        }
                    ]
                }
            ]
        }
    },
    
    # === ASK YOURSELF ===
    "ask_yourself": {
        "header": {"de": "Frag dich selbst", "en": "Ask Yourself"},
        "questions": [
            {"de": "Kannst du Summe und Mittelwert standardisieren?", "en": "Can you standardize both sum and mean?"},
            {"de": "Was passiert mit der Varianz bei Summe vs. Mittelwert?", "en": "What happens to variance for sum vs. mean?"},
            {"de": "Wann brauchst du die Stetigkeitskorrektur?", "en": "When do you need continuity correction?"},
            {"de": "In welche Richtung korrigierst du bei P(X ≥ k)?", "en": "Which direction do you correct for P(X ≥ k)?"},
            {"de": "Was bedeutet i.i.d. und warum ist es wichtig?", "en": "What does i.i.d. mean and why is it important?"}
        ],
        "conclusion": {
            "de": "Wenn du alle beantworten kannst, bist du bereit für Prüfungsaufgaben zu Kapitel 6!",
            "en": "If you can answer all of these, you're ready for Chapter 6 exam questions!"
        }
    },
    
    # === EXAM ESSENTIALS ===
    "exam_essentials": {
        "tips": [
            {
                "tip": {"de": "Summe: Varianz WÄCHST, Mittelwert: Varianz SCHRUMPFT", "en": "Sum: Variance GROWS, Mean: Variance SHRINKS"},
                "tip_formula": r"\text{Var}(S_n) = n\sigma^2 \quad \text{vs.} \quad \text{Var}(\bar{X}) = \frac{\sigma^2}{n}",
                "why": {"de": "Das ist der Kern des ZGS — nicht verwechseln!", "en": "This is the core of CLT — don't confuse them!"}
            },
            {
                "tip": {"de": "Nenner beim Standardisieren = Standardabweichung der Grösse", "en": "Denominator when standardizing = standard deviation of the quantity"},
                "why": {"de": "Summe: $\\sigma\\sqrt{n}$, Mittelwert: $\\sigma/\\sqrt{n}$, Binomial: $\\sqrt{np(1-p)}$", "en": "Sum: $\\sigma\\sqrt{n}$, Mean: $\\sigma/\\sqrt{n}$, Binomial: $\\sqrt{np(1-p)}$"}
            },
            {
                "tip": {"de": "i.i.d. prüfen: Unabhängig + Identisch verteilt + Grosses n", "en": "Check i.i.d.: Independent + Identically distributed + Large n"},
                "why": {"de": "Ohne i.i.d. funktioniert der ZGS nicht!", "en": "Without i.i.d., the CLT doesn't work!"}
            },
            {
                "tip": {"de": "Stetigkeitskorrektur: Bei diskreten Daten IMMER anwenden", "en": "Continuity correction: ALWAYS apply for discrete data"},
                "tip_formula": r"P(X \geq k) \to P(X \geq k-0.5)",
                "why": {"de": "Die Prüfung erwartet es — vergessen kostet Punkte!", "en": "The exam expects it — forgetting costs points!"}
            }
        ],
        "trap": {
            "de": "<strong>Die Korrektur-Richtungs-Falle:</strong> Bei $P(X \\geq k)$ wird k KLEINER ($k-0.5$), bei $P(X \\leq k)$ wird k GRÖSSER ($k+0.5$). Die Richtung ist kontraintuitiv!",
            "en": "<strong>The Correction Direction Trap:</strong> For $P(X \\geq k)$, k becomes SMALLER ($k-0.5$), for $P(X \\leq k)$, k becomes LARGER ($k+0.5$). The direction is counterintuitive!"
        },
        "trap_rule": {
            "de": "Merke: Du erweiterst immer das Intervall, um den diskreten Wert vollständig einzuschliessen.",
            "en": "Remember: You always extend the interval to fully include the discrete value."
        }
    }
}


# ==========================================
# 2. RENDER FUNCTION
# ==========================================
def render_subtopic_6_3(model):
    """6.3 Summary — ULTRATHINK Learn-Test-Learn Flow"""
    inject_equal_height_css()
    
    st.header(t(content_6_3["title"]))
    st.caption(t(content_6_3["subtitle"]))
    st.markdown("---")
    
    # === CHAPTER INTUITION (Grey Callout) ===
    st.markdown(f"""
<div style="background: #f4f4f5; border-left: 4px solid #a1a1aa; 
            padding: 12px 16px; border-radius: 8px; color: #3f3f46;">
<strong>{t(content_6_3["intuition"]["header"])}:</strong><br>
{t(content_6_3["intuition"]["text"])}
</div>
""", unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # === CHUNK 1: SUM VS MEAN ===
    render_chunk_sum_mean(model)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # === CHUNK 2: STANDARDIZATION ===
    render_chunk_standardization(model)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # === CHUNK 3: DE MOIVRE-LAPLACE ===
    render_chunk_demoivre(model)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # === CHUNK 4: i.i.d. CONDITIONS ===
    render_chunk_iid(model)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # === KEY FORMULAS ===
    render_key_formulas()
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # === DECISION TREE ===
    render_formula_decision_tree()
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # === ASK YOURSELF ===
    render_ask_yourself(
        header=content_6_3["ask_yourself"]["header"],
        questions=content_6_3["ask_yourself"]["questions"],
        conclusion=content_6_3["ask_yourself"]["conclusion"]
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # === EXAM ESSENTIALS ===
    render_exam_essentials(
        tips=content_6_3["exam_essentials"]["tips"],
        trap=content_6_3["exam_essentials"]["trap"],
        trap_rule=content_6_3["exam_essentials"]["trap_rule"]
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # === OFFICIAL EXAM QUESTIONS ===
    st.markdown(f"### {t({'de': 'Offizielle Prüfungsaufgaben', 'en': 'Official Exam Questions'})}")
    
    questions = get_all_questions_for_topic("6.3")
    
    for q_id, q in questions.items():
        with st.container(border=True):
            st.caption(q.get("source", ""))
            opts = q.get("options", [])
            if opts and isinstance(opts[0], dict):
                option_labels = [t(o) for o in opts]
            else:
                option_labels = opts
            
            render_mcq(
                key_suffix=f"6_3_{q_id}",
                question_text=t(q["question"]),
                options=option_labels,
                correct_idx=q["correct_idx"],
                solution_text_dict=q["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Falsch.", "en": "Incorrect."},
                client=model,
                ai_context=f"CLT Summary: {q_id}",
                course_id="vwl",
                topic_id="6",
                subtopic_id="6.3",
                question_id=q_id
            )
        st.markdown("<br>", unsafe_allow_html=True)


# ==========================================
# 3. CHUNK RENDER FUNCTIONS
# ==========================================

def render_chunk_sum_mean(model):
    """Chunk 1: Sum vs Mean comparison"""
    chunk = content_6_3["chunk_sum_mean"]
    st.markdown(f"### {t(chunk['header'])}")
    
    # Side-by-side comparison
    c1, c2 = st.columns(2, gap="medium")
    
    with c1:
        with st.container(border=True):
            st.markdown(f"**{t(chunk['comparison']['left']['title'])}**")
            st.latex(chunk['comparison']['left']['formula'])
            st.markdown("---")
            st.markdown(f"**{t({'de': 'Verteilung', 'en': 'Distribution'})}:**")
            st.latex(chunk['comparison']['left']['distribution_formula'])
            st.markdown("---")
            st.markdown(t(chunk['comparison']['left']['insight']), unsafe_allow_html=True)
    
    with c2:
        with st.container(border=True):
            st.markdown(f"**{t(chunk['comparison']['right']['title'])}**")
            st.latex(chunk['comparison']['right']['formula'])
            st.markdown("---")
            st.markdown(f"**{t({'de': 'Verteilung', 'en': 'Distribution'})}:**")
            st.latex(chunk['comparison']['right']['distribution_formula'])
            st.markdown("---")
            st.markdown(t(chunk['comparison']['right']['insight']), unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # MCQ
    render_chunk_mcq(chunk, "sum_mean", model)


def render_chunk_standardization(model):
    """Chunk 2: Standardization formulas"""
    chunk = content_6_3["chunk_standardization"]
    st.markdown(f"### {t(chunk['header'])}")
    
    # 2-column formula grid
    cols = st.columns(2, gap="medium")
    for col, f in zip(cols, chunk["formulas"]):
        with col:
            with st.container(border=True):
                st.markdown(f"**{t(f['name'])}**")
                st.latex(f["formula"])
                st.caption(t(f["when"]))
                st.caption(f"→ {t(f['example'])}")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # MCQ
    render_chunk_mcq(chunk, "standardization", model)


def render_chunk_demoivre(model):
    """Chunk 3: De Moivre-Laplace with correction"""
    chunk = content_6_3["chunk_demoivre"]
    st.markdown(f"### {t(chunk['header'])}")
    
    # Side-by-side comparison
    c1, c2 = st.columns(2, gap="medium")
    
    with c1:
        with st.container(border=True):
            st.markdown(f"**{t(chunk['comparison']['left']['title'])}**")
            st.latex(chunk['comparison']['left']['formula'])
            st.markdown("---")
            st.markdown(t(chunk['comparison']['left']['insight']), unsafe_allow_html=True)
    
    with c2:
        with st.container(border=True):
            st.markdown(f"**{t(chunk['comparison']['right']['title'])}**")
            st.latex(chunk['comparison']['right']['formula'])
            st.markdown("---")
            st.markdown(t(chunk['comparison']['right']['insight']), unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Mnemonic Table
    mnemonic = chunk["mnemonic"]
    st.markdown(f"**{t(mnemonic['header'])}**")
    
    with st.container(border=True):
        # Build table using columns
        header_cols = st.columns([2, 2, 3])
        header_cols[0].markdown(f"**{t({'de': 'Du willst', 'en': 'You want'})}**")
        header_cols[1].markdown(f"**{t({'de': 'Korrektur', 'en': 'Correction'})}**")
        header_cols[2].markdown(f"**{t({'de': 'Warum', 'en': 'Why'})}**")
        
        st.markdown("---")
        
        for row in mnemonic["rows"]:
            row_cols = st.columns([2, 2, 3])
            row_cols[0].latex(row["want"])
            row_cols[1].latex(row["adjust"])
            row_cols[2].markdown(t(row["reason"]))
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # MCQ
    render_chunk_mcq(chunk, "demoivre", model)


def render_chunk_iid(model):
    """Chunk 4: i.i.d. conditions"""
    chunk = content_6_3["chunk_iid"]
    st.markdown(f"### {t(chunk['header'])}")
    
    # Definition card
    defn = chunk["definition"]
    with st.container(border=True):
        st.markdown(f"**{t(defn['term'])}**")
        st.markdown("---")
        
        for condition in defn["conditions"]:
            st.markdown(f"**{t(condition['name'])}**")
            st.markdown(t(condition["explanation"]))
            st.caption(f"→ {t(condition['example'])}")
            st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # MCQ
    render_chunk_mcq(chunk, "iid", model)


def render_chunk_mcq(chunk, chunk_id, model):
    """Render MCQ for a chunk"""
    mcq = chunk["mcq"]
    opts = [t(o) for o in mcq["options"]]
    
    with st.container(border=True):
        st.markdown(f"**{t({'de': 'Schnell-Check', 'en': 'Quick Check'})}**")
        
        render_mcq(
            key_suffix=f"6_3_{chunk_id}",
            question_text=t(mcq["question"]),
            options=opts,
            correct_idx=mcq["correct_idx"],
            solution_text_dict=mcq["solution"],
            success_msg_dict={"de": "Richtig!", "en": "Correct!"},
            error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
            client=model,
            ai_context=f"CLT summary: {chunk_id} concepts",
            course_id="vwl",
            topic_id="6",
            subtopic_id="6.3",
            question_id=f"6_3_quick_{chunk_id}"
        )


def render_key_formulas():
    """Render all key formulas in a 2-column grid"""
    kf = content_6_3["key_formulas"]
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
def render_formula_decision_tree():
    """Interactive decision tree for formula selection"""
    dt = content_6_3["decision_tree"]
    st.markdown(f"### {t(dt['header'])}")
    
    with st.container(border=True):
        st.markdown(f"**{t(dt['root']['question'])}**")
        
        # Create options for radio
        options = dt["root"]["options"]
        option_labels = [t(opt["label"]) for opt in options]
        
        selected = st.radio(
            t({"de": "Wähle:", "en": "Choose:"}),
            options=option_labels,
            key="6_3_decision_tree",
            horizontal=False,
            label_visibility="collapsed"
        )
        
        st.markdown("---")
        
        # Find selected option and show result
        for opt in options:
            if t(opt["label"]) == selected:
                if "result_formula" in opt:
                    st.markdown(f"**{t({'de': 'Formel', 'en': 'Formula'})}:**")
                    st.latex(opt["result_formula"])
                    if "result_note" in opt:
                        st.caption(t(opt["result_note"]))
                elif "next_question" in opt:
                    # Second-level question
                    st.markdown(f"**{t(opt['next_question'])}**")
                    
                    branch_labels = [t(b["condition"]) for b in opt["branches"]]
                    branch_selected = st.radio(
                        t({"de": "Bedingung:", "en": "Condition:"}),
                        options=branch_labels,
                        key="6_3_decision_tree_branch",
                        horizontal=True,
                        label_visibility="collapsed"
                    )
                    
                    for branch in opt["branches"]:
                        if t(branch["condition"]) == branch_selected:
                            st.markdown(f"**{t({'de': 'Formel', 'en': 'Formula'})}:**")
                            st.latex(branch["result_formula"])
                            if "result_note" in branch:
                                st.caption(t(branch["result_note"]))
                break
