# Topic 9.4: Summary — Confidence Intervals
# ULTRATHINK IMPLEMENTATION: Learn-Test-Learn Chunked Pattern + Feynman Pedagogy
# "If you can't explain it simply, you don't understand it well enough." — Richard Feynman

import streamlit as st
from utils.localization import t
from utils.quiz_helper import render_mcq
from utils.ask_yourself import render_ask_yourself
from utils.exam_essentials import render_exam_essentials
from utils.layouts import render_comparison, render_formula_grid, render_definition, render_decision_tree
from utils.layouts.foundation import inject_equal_height_css, grey_callout
from data.exam_questions import get_all_questions_for_topic

# ==========================================
# 1. CONTENT DICTIONARY - BILINGUAL (ULTRATHINK)
# ==========================================
content_9_4 = {
    "title": {"de": "9.4 Zusammenfassung", "en": "9.4 Summary"},
    "subtitle": {"de": "Konfidenzintervalle auf einen Blick", "en": "Confidence Intervals at a Glance"},
    
    # --- THE BIG PICTURE (Feynman Hook) ---
    "big_picture": {
        "header": {"de": "Das grosse Bild", "en": "The Big Picture"},
        "text": {
            "de": """Du hast gelernt, <strong>mit einem Netz zu fischen, statt mit einem Speer</strong>. 

<strong>Der Speer</strong> (Punktschätzung): Trifft manchmal, verfehlt oft. Keine Sicherheit.

<strong>Das Netz</strong> (Konfidenzintervall): Fängt den Fisch in 95% der Würfe — garantiert.

Diese Zusammenfassung zeigt dir: <strong>Welche Formel wann</strong>, und wie du mit dem KI <strong>gratis einen Hypothesentest</strong> bekommst.""",
            "en": """You learned to <strong>fish with a net instead of a spear</strong>.

<strong>The spear</strong> (point estimate): Sometimes hits, often misses. No guarantee.

<strong>The net</strong> (confidence interval): Catches the fish in 95% of casts — guaranteed.

This summary shows you: <strong>Which formula when</strong>, and how the CI gives you a <strong>free hypothesis test</strong>."""
        }
    },
    
    # === CHUNK 1: THE CONCEPT ===
    "chunk_concept": {
        "header": {"de": "Das Konzept", "en": "The Concept"},
        "definition": {
            "term": {"de": "Konfidenzintervall", "en": "Confidence Interval"},
            "definition": {
                "de": "Ein Bereich um den Schätzer θ̂, der den wahren Parameter θ mit Wahrscheinlichkeit (1-α) enthält.",
                "en": "A range around the estimator θ̂ that contains the true parameter θ with probability (1-α)."
            },
            "formula": r"\text{KI}_{1-\alpha} = \left[\hat{\theta} - f_n \,;\, \hat{\theta} + f_n\right]",
            "examples": [
                {"de": "95%-Niveau: 1-α = 0.95", "en": "95% level: 1-α = 0.95"},
                {"de": "99%-Niveau: 1-α = 0.99", "en": "99% level: 1-α = 0.99"}
            ]
        },
        "key_insight": {
            "de": "Das <strong>Intervall ist zufällig</strong> (hängt von der Stichprobe ab). Der <strong>Parameter ist fest</strong> (ändert sich nie). Nicht umgekehrt!",
            "en": "The <strong>interval is random</strong> (depends on the sample). The <strong>parameter is fixed</strong> (never changes). Not the other way around!"
        },
        "mcq": {
            "question": {
                "de": "Was bedeutet '95% Konfidenzniveau'?",
                "en": "What does '95% confidence level' mean?"
            },
            "options": [
                {"de": "θ liegt mit 95% Wahrscheinlichkeit im Intervall", "en": "θ is in the interval with 95% probability"},
                {"de": "95% aller möglichen Intervalle enthalten θ", "en": "95% of all possible intervals contain θ"},
                {"de": "5% der Daten sind Ausreisser", "en": "5% of the data are outliers"},
                {"de": "Das Intervall ist 95% so breit wie die Stichprobe", "en": "The interval is 95% as wide as the sample"}
            ],
            "correct_idx": 1,
            "solution": {
                "de": "<strong>Richtig: (b)</strong><br>θ ist FEST — es liegt entweder drin oder nicht. Die 95% beziehen sich auf die METHODE: Von 100 zufälligen Stichproben würden etwa 95 ein Intervall liefern, das θ enthält.",
                "en": "<strong>Correct: (b)</strong><br>θ is FIXED — it's either in or not. The 95% refers to the METHOD: From 100 random samples, about 95 would produce an interval containing θ."
            }
        }
    },
    
    # === CHUNK 2: THE FORMULAS ===
    "chunk_formulas": {
        "header": {"de": "Die Formeln", "en": "The Formulas"},
        "comparison": {
            "title": {"de": "σ bekannt vs. σ unbekannt", "en": "σ Known vs. σ Unknown"},
            "left": {
                "title": {"de": "Fall A: σ bekannt", "en": "Case A: σ Known"},
                "content": {
                    "de": """<strong>Formel:</strong>""",
                    "en": """<strong>Formula:</strong>"""
                },
                "formula": r"\bar{x} \pm z_{1-\alpha/2} \cdot \frac{\sigma}{\sqrt{n}}",
                "insight": {
                    "de": "<strong>Wann:</strong> σ ist in der Aufgabe gegeben.",
                    "en": "<strong>When:</strong> σ is given in the problem."
                }
            },
            "right": {
                "title": {"de": "Fall B: σ unbekannt", "en": "Case B: σ Unknown"},
                "content": {
                    "de": """<strong>Formel:</strong>""",
                    "en": """<strong>Formula:</strong>"""
                },
                "formula": r"\bar{x} \pm z_{1-\alpha/2} \cdot \frac{S_n}{\sqrt{n}}",
                "insight": {
                    "de": "<strong>Wann:</strong> σ nicht gegeben, n ≥ 50.",
                    "en": "<strong>When:</strong> σ not given, n ≥ 50."
                }
            }
        },
        "z_table": {
            "header": {"de": "Kritische z-Werte", "en": "Critical z-Values"},
            "values": [
                {"level": "90%", "alpha": "0.10", "z": "1.645"},
                {"level": "95%", "alpha": "0.05", "z": "1.960"},
                {"level": "99%", "alpha": "0.01", "z": "2.576"}
            ]
        },
        "mcq": {
            "question": {
                "de": "In einer Aufgabe steht: 'Die Standardabweichung beträgt σ = 12.' Welche Formel verwendest du?",
                "en": "A problem states: 'The standard deviation is σ = 12.' Which formula do you use?"
            },
            "options": [
                {"de": "x̄ ± z·σ/√n (Fall A)", "en": "x̄ ± z·σ/√n (Case A)"},
                {"de": "x̄ ± z·Sₙ/√n (Fall B)", "en": "x̄ ± z·Sₙ/√n (Case B)"},
                {"de": "x̄ ± t·Sₙ/√n (t-Verteilung)", "en": "x̄ ± t·Sₙ/√n (t-distribution)"},
                {"de": "Kann nicht berechnet werden", "en": "Cannot be calculated"}
            ],
            "correct_idx": 0,
            "solution": {
                "de": "<strong>Richtig: (a)</strong><br>Wenn σ GEGEBEN ist, verwendest du immer Fall A mit dem wahren σ. Fall B mit Sₙ ist nur für den Fall, wenn σ unbekannt ist und du ihn aus der Stichprobe schätzen musst.",
                "en": "<strong>Correct: (a)</strong><br>When σ is GIVEN, always use Case A with the true σ. Case B with Sₙ is only for when σ is unknown and you must estimate it from the sample."
            }
        }
    },
    
    # === CHUNK 3: THE DUALITY ===
    "chunk_duality": {
        "header": {"de": "Die Dualität: KI ↔ Test", "en": "The Duality: CI ↔ Test"},
        "analogy": {
            "de": """<strong>Das Gericht-Analogie:</strong> Das KI ist eine <strong>Urteilsmaschine</strong>.

Der Staatsanwalt behauptet: "μ = 100" (Nullhypothese H₀).

Du hast Beweise gesammelt und ein 95%-KI berechnet: <strong>[85, 95]</strong>.

<strong>Urteil:</strong> 100 liegt AUSSERHALB → <strong>H₀ verwerfen!</strong>

<em>Keine extra Berechnung nötig — das KI hat den Test schon gemacht.</em>""",
            "en": """<strong>The Court Analogy:</strong> The CI is a <strong>verdict machine</strong>.

The prosecutor claims: "μ = 100" (null hypothesis H₀).

You collected evidence and computed a 95% CI: <strong>[85, 95]</strong>.

<strong>Verdict:</strong> 100 is OUTSIDE → <strong>Reject H₀!</strong>

<em>No extra calculation needed — the CI already did the test.</em>"""
        },
        "matching_table": {
            "header": {"de": "Die Entsprechung", "en": "The Matching"},
            "rows": [
                {"ci": "90%", "test": "10%"},
                {"ci": "95%", "test": "5%"},
                {"ci": "99%", "test": "1%"}
            ]
        },
        "decision_rule": {
            "de": """<strong>Die Regel:</strong>
• μ₀ <strong>IM</strong> Intervall → H₀ <strong>NICHT</strong> verwerfen
• μ₀ <strong>AUSSERHALB</strong> → H₀ <strong>verwerfen</strong>""",
            "en": """<strong>The Rule:</strong>
• μ₀ <strong>INSIDE</strong> interval → <strong>Do NOT</strong> reject H₀
• μ₀ <strong>OUTSIDE</strong> → <strong>Reject</strong> H₀"""
        },
        "mcq": {
            "question": {
                "de": "Ein 99%-KI für μ ist [85, 95]. Du testest H₀: μ = 92 mit α = 1%. Die Testentscheidung ist:",
                "en": "A 99% CI for μ is [85, 95]. You test H₀: μ = 92 with α = 1%. The test decision is:"
            },
            "options": [
                {"de": "H₀ verwerfen", "en": "Reject H₀"},
                {"de": "H₀ NICHT verwerfen", "en": "Do NOT reject H₀"},
                {"de": "Mehr Information nötig", "en": "More information needed"},
                {"de": "Unentschieden", "en": "Inconclusive"}
            ],
            "correct_idx": 1,
            "solution": {
                "de": "<strong>Richtig: (b)</strong><br>μ₀ = 92 liegt INNERHALB des 99%-KI [85, 95]. Dualitätsregel: 99%-KI entspricht 1%-Test. Da 92 im Intervall liegt, wird H₀ NICHT verworfen.",
                "en": "<strong>Correct: (b)</strong><br>μ₀ = 92 lies INSIDE the 99% CI [85, 95]. Duality rule: 99% CI corresponds to 1% test. Since 92 is in the interval, H₀ is NOT rejected."
            }
        }
    },
    
    # === KEY FORMULAS GRID ===
    "key_formulas": {
        "header": {"de": "Formel-Übersicht", "en": "Formula Overview"},
        "formulas": [
            {
                "name": {"de": "KI (σ bekannt)", "en": "CI (σ known)"},
                "formula": r"\bar{x} \pm z \cdot \frac{\sigma}{\sqrt{n}}",
                "when": {"de": "σ in Aufgabe gegeben", "en": "σ given in problem"},
                "example": {"de": "z₀.₉₇₅ = 1.96 für 95%", "en": "z₀.₉₇₅ = 1.96 for 95%"}
            },
            {
                "name": {"de": "KI (σ unbekannt)", "en": "CI (σ unknown)"},
                "formula": r"\bar{x} \pm z \cdot \frac{S_n}{\sqrt{n}}",
                "when": {"de": "σ nicht gegeben, n ≥ 50", "en": "σ not given, n ≥ 50"},
                "example": {"de": "Sₙ aus Stichprobe", "en": "Sₙ from sample"}
            },
            {
                "name": {"de": "Stichprobenfehler", "en": "Sampling Error"},
                "formula": r"f_n = z \cdot \frac{\sigma}{\sqrt{n}}",
                "when": {"de": "Margin of Error", "en": "Margin of Error"},
                "example": {"de": "Schrumpft mit √n", "en": "Shrinks with √n"}
            },
            {
                "name": {"de": "Intervallbreite", "en": "Interval Width"},
                "formula": r"\text{Breite} = 2 \cdot f_n",
                "when": {"de": "Symmetrisches Intervall", "en": "Symmetric interval"},
                "example": {"de": "Wächst mit z (99% > 95%)", "en": "Grows with z (99% > 95%)"}
            }
        ]
    },
    
    # === DECISION TREE ===
    "decision_tree": {
        "header": {"de": "Welche Formel brauchst du?", "en": "Which Formula Do You Need?"},
        "root": {
            "question": {"de": "Was ist gegeben?", "en": "What is given?"},
            "options": [
                {
                    "label": {"de": "σ ist bekannt (in Aufgabe gegeben)", "en": "σ is known (given in problem)"},
                    "result_formula": r"\bar{x} \pm z_{1-\alpha/2} \cdot \frac{\sigma}{\sqrt{n}}",
                    "result_note": {"de": "Verwende das wahre σ direkt!", "en": "Use the true σ directly!"}
                },
                {
                    "label": {"de": "σ unbekannt, aber n ≥ 50", "en": "σ unknown, but n ≥ 50"},
                    "result_formula": r"\bar{x} \pm z_{1-\alpha/2} \cdot \frac{S_n}{\sqrt{n}}",
                    "result_note": {"de": "Schätze σ mit Sₙ aus der Stichprobe.", "en": "Estimate σ with Sₙ from the sample."}
                },
                {
                    "label": {"de": "Hypothesentest via Dualität", "en": "Hypothesis test via duality"},
                    "result_formula": r"\mu_0 \in \text{KI} \Rightarrow \text{H}_0 \text{ nicht verwerfen}",
                    "result_note": {"de": "95%-KI ↔ 5%-Test, 99%-KI ↔ 1%-Test", "en": "95% CI ↔ 5% test, 99% CI ↔ 1% test"}
                }
            ]
        }
    },
    
    # === ASK YOURSELF ===
    "ask_yourself": {
        "header": {"de": "Frag dich: Bist du bereit für die Prüfung?", "en": "Ask yourself: Are you ready for the exam?"},
        "questions": [
            {"de": "Was ist der Unterschied zwischen σ bekannt und σ unbekannt?", 
             "en": "What's the difference between σ known and σ unknown?"},
            {"de": "Was bedeutet '95% Konfidenz' NICHT? (Die häufigste Falle!)", 
             "en": "What does '95% confidence' NOT mean? (The most common trap!)"},
            {"de": "Wie hängen KI und Hypothesentest zusammen?", 
             "en": "How are CI and hypothesis test connected?"},
            {"de": "Was passiert mit dem Intervall, wenn n grösser wird?", 
             "en": "What happens to the interval when n increases?"},
            {"de": "95%-KI = [80, 90]. H₀: μ = 85. Verwirfst du?", 
             "en": "95% CI = [80, 90]. H₀: μ = 85. Do you reject?"}
        ],
        "conclusion": {
            "de": "Antworten: Fall A vs B (σ), nicht '95% Chance', Dualität, schmaler, NEIN (85 drin)!",
            "en": "Answers: Case A vs B (σ), not '95% chance', duality, narrower, NO (85 inside)!"
        }
    },
    
    # === EXAM ESSENTIALS ===
    "exam_essentials": {
        "tips": [
            {
                "tip": {"de": "Prüfe ZUERST: Ist σ gegeben?", "en": "Check FIRST: Is σ given?"},
                "why": {"de": "Das bestimmt, ob du Fall A (σ) oder Fall B (Sₙ) verwendest.", "en": "This determines whether you use Case A (σ) or Case B (Sₙ)."}
            },
            {
                "tip": {"de": "Intervall = Schätzer ± Fehler", "en": "Interval = Estimate ± Error"},
                "why": {"de": "Jedes KI: Mitte + Rand. Immer dieselbe Struktur.", "en": "Every CI: center + margin. Always the same structure."},
                "why_formula": r"\text{KI} = \bar{x} \pm f_n"
            },
            {
                "tip": {"de": "Dualität: 95%-KI ↔ 5%-Test", "en": "Duality: 95% CI ↔ 5% test"},
                "why": {"de": "μ₀ im KI = nicht verwerfen. μ₀ ausserhalb = verwerfen.", "en": "μ₀ inside CI = don't reject. μ₀ outside = reject."}
            },
            {
                "tip": {"de": "Mehr Konfidenz = breiteres Intervall", "en": "More confidence = wider interval"},
                "why": {"de": "99%-KI ist breiter als 95%-KI. Mehr Sicherheit braucht mehr Spielraum.", "en": "99% CI is wider than 95% CI. More confidence needs more margin."},
                "why_formula": r"z_{0.995} = 2.576 > z_{0.975} = 1.960"
            }
        ],
        "trap": {
            "de": "<strong>Die Interpretations-Falle:</strong> '95% Chance, dass θ im Intervall liegt' ist FALSCH!",
            "en": "<strong>The Interpretation Trap:</strong> '95% chance that θ is in the interval' is WRONG!"
        },
        "trap_rule": {
            "de": "θ ist FEST — es liegt entweder drin oder nicht. Die 95% beziehen sich auf die METHODE: 95% aller möglichen Intervalle würden θ enthalten.",
            "en": "θ is FIXED — it's either in or not. The 95% refers to the METHOD: 95% of all possible intervals would contain θ."
        }
    }
}


# ==========================================
# 2. CHUNK RENDER FUNCTIONS
# ==========================================

def render_chunk_concept(model):
    """Chunk 1: The Concept — Definition + Key Insight + MCQ"""
    chunk = content_9_4["chunk_concept"]
    st.markdown(f"### {t(chunk['header'])}")
    
    # Definition Card
    defn = chunk["definition"]
    with st.container(border=True):
        st.markdown(f"**{t(defn['term'])}**")
        st.markdown(f"*{t(defn['definition'])}*")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        st.latex(defn["formula"])
        
        st.markdown("---")
        
        # Examples
        st.markdown(f"**{t({'de': 'Typische Werte', 'en': 'Typical Values'})}:**")
        for ex in defn["examples"]:
            st.markdown(f"• {t(ex)}")
        
        st.markdown("---")
        
        # Key Insight
        st.markdown(f"**{t({'de': 'Schlüssel-Einsicht', 'en': 'Key Insight'})}:**")
        st.markdown(t(chunk["key_insight"]), unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # MCQ
    render_chunk_mcq(chunk["mcq"], "concept", model)


def render_chunk_formulas(model):
    """Chunk 2: The Formulas — σ known vs unknown + z-table + MCQ"""
    chunk = content_9_4["chunk_formulas"]
    st.markdown(f"### {t(chunk['header'])}")
    
    # Equal height CSS
    inject_equal_height_css()
    
    # Side-by-side comparison
    comp = chunk["comparison"]
    st.markdown(f"**{t(comp['title'])}**")
    
    c1, c2 = st.columns(2, gap="medium")
    
    with c1:
        with st.container(border=True):
            st.markdown(f"**{t(comp['left']['title'])}**")
            st.markdown(t(comp['left']['content']), unsafe_allow_html=True)
            st.latex(comp['left']['formula'])
            st.markdown("---")
            st.markdown(t(comp['left']['insight']), unsafe_allow_html=True)
    
    with c2:
        with st.container(border=True):
            st.markdown(f"**{t(comp['right']['title'])}**")
            st.markdown(t(comp['right']['content']), unsafe_allow_html=True)
            st.latex(comp['right']['formula'])
            st.markdown("---")
            st.markdown(t(comp['right']['insight']), unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Z-values table
    z_table = chunk["z_table"]
    st.markdown(f"**{t(z_table['header'])}**")
    
    with st.container(border=True):
        # Table header
        cols = st.columns([1, 1, 1])
        cols[0].markdown(f"**{t({'de': 'Niveau', 'en': 'Level'})}**")
        cols[1].markdown(f"**α**")
        cols[2].markdown(f"**z**")
        
        st.markdown("---")
        
        # Table rows
        for row in z_table["values"]:
            cols = st.columns([1, 1, 1])
            cols[0].markdown(f"**{row['level']}**")
            cols[1].markdown(row['alpha'])
            cols[2].markdown(f"**{row['z']}**")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # MCQ
    render_chunk_mcq(chunk["mcq"], "formulas", model)


def render_chunk_duality(model):
    """Chunk 3: The Duality — Court analogy + Matching table + MCQ"""
    chunk = content_9_4["chunk_duality"]
    st.markdown(f"### {t(chunk['header'])}")
    
    # Court Analogy (Grey Callout)
    st.markdown(f"""
<div style="background: #f4f4f5; border-left: 4px solid #a1a1aa; 
            padding: 12px 16px; border-radius: 8px; color: #3f3f46;">
{t(chunk["analogy"])}
</div>
""", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Matching Table
    matching = chunk["matching_table"]
    st.markdown(f"**{t(matching['header'])}**")
    
    with st.container(border=True):
        cols = st.columns([1, 1])
        cols[0].markdown(f"**{t({'de': 'KI-Niveau', 'en': 'CI Level'})}**")
        cols[1].markdown(f"**{t({'de': 'Test α', 'en': 'Test α'})}**")
        
        st.markdown("---")
        
        for row in matching["rows"]:
            cols = st.columns([1, 1])
            cols[0].markdown(f"**{row['ci']}**")
            cols[1].markdown(row['test'])
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Decision Rule
    st.markdown(f"""
<div style="background: #f4f4f5; border-left: 4px solid #a1a1aa; 
            padding: 12px 16px; border-radius: 8px; color: #3f3f46;">
{t(chunk["decision_rule"])}
</div>
""", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # MCQ
    render_chunk_mcq(chunk["mcq"], "duality", model)


def render_chunk_mcq(mcq_data, chunk_id, model):
    """Render MCQ for a chunk"""
    opts = [t(o) for o in mcq_data["options"]]
    
    with st.container(border=True):
        st.markdown(f"**{t({'de': 'Schnell-Check', 'en': 'Quick Check'})}**")
        
        render_mcq(
            key_suffix=f"9_4_{chunk_id}",
            question_text=t(mcq_data["question"]),
            options=opts,
            correct_idx=mcq_data["correct_idx"],
            solution_text_dict=mcq_data["solution"],
            success_msg_dict={"de": "Richtig!", "en": "Correct!"},
            error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
            client=model,
            ai_context=f"CI Summary: {chunk_id} concepts",
            course_id="vwl",
            topic_id="9",
            subtopic_id="9.4",
            question_id=f"9_4_quick_{chunk_id}"
        )


def render_key_formulas():
    """Render all key formulas in a 2x2 grid"""
    kf = content_9_4["key_formulas"]
    st.markdown(f"### {t(kf['header'])}")
    
    formulas = kf["formulas"]
    
    # 2x2 layout
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
    dt = content_9_4["decision_tree"]
    st.markdown(f"### {t(dt['header'])}")
    
    with st.container(border=True):
        st.markdown(f"**{t(dt['root']['question'])}**")
        
        # Create options for radio
        options = dt["root"]["options"]
        option_labels = [t(opt["label"]) for opt in options]
        
        selected = st.radio(
            t({"de": "Wähle:", "en": "Choose:"}),
            options=option_labels,
            key="9_4_decision_tree",
            horizontal=False,
            label_visibility="collapsed"
        )
        
        st.markdown("---")
        
        # Find selected option and show result
        for opt in options:
            if t(opt["label"]) == selected:
                st.markdown(f"**{t({'de': 'Formel', 'en': 'Formula'})}:**")
                st.latex(opt["result_formula"])
                if "result_note" in opt:
                    st.caption(t(opt["result_note"]))
                break


# ==========================================
# 3. MAIN RENDER FUNCTION
# ==========================================

def render_subtopic_9_4(model):
    """9.4 Summary — ULTRATHINK Learn-Test-Learn Flow"""
    
    # Inject equal height CSS
    inject_equal_height_css()
    
    st.header(t(content_9_4["title"]))
    st.caption(t(content_9_4["subtitle"]))
    st.markdown("---")
    
    # === THE BIG PICTURE (Feynman Hook) ===
    bp = content_9_4["big_picture"]
    st.markdown(f"""
<div style="background: #f4f4f5; border-left: 4px solid #a1a1aa; 
            padding: 12px 16px; border-radius: 8px; color: #3f3f46;">
<strong>{t(bp["header"])}:</strong><br><br>
{t(bp["text"])}
</div>
""", unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # === CHUNK 1: THE CONCEPT ===
    render_chunk_concept(model)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # === CHUNK 2: THE FORMULAS ===
    render_chunk_formulas(model)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # === CHUNK 3: THE DUALITY ===
    render_chunk_duality(model)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # === KEY FORMULAS GRID ===
    render_key_formulas()
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # === DECISION TREE ===
    render_formula_decision_tree()
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # === ASK YOURSELF ===
    render_ask_yourself(
        header=content_9_4["ask_yourself"]["header"],
        questions=content_9_4["ask_yourself"]["questions"],
        conclusion=content_9_4["ask_yourself"]["conclusion"]
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # === EXAM ESSENTIALS ===
    render_exam_essentials(
        tips=content_9_4["exam_essentials"]["tips"],
        trap=content_9_4["exam_essentials"]["trap"],
        trap_rule=content_9_4["exam_essentials"]["trap_rule"]
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # === OFFICIAL EXAM QUESTIONS ===
    st.markdown(f"### {t({'de': 'Offizielle Prüfungsaufgaben', 'en': 'Official Exam Questions'})}")
    
    questions = get_all_questions_for_topic("9.4")
    
    for q_id, q in questions.items():
        with st.container(border=True):
            st.caption(q.get("source", ""))
            opts = q.get("options", [])
            if opts and isinstance(opts[0], dict):
                option_labels = [t(o) for o in opts]
            else:
                option_labels = opts
            
            render_mcq(
                key_suffix=f"9_4_{q_id}",
                question_text=t(q["question"]),
                options=option_labels,
                correct_idx=q["correct_idx"],
                solution_text_dict=q["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Falsch.", "en": "Incorrect."},
                client=model,
                ai_context=f"CI Summary: {q_id}",
                course_id="vwl",
                topic_id="9",
                subtopic_id="9.4",
                question_id=q_id
            )
        st.markdown("<br>", unsafe_allow_html=True)
