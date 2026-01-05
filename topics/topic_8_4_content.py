# Topic 8.4: Zusammenfassung — Point Estimation Summary
# ULTRATHINK IMPLEMENTATION: Learn-Test-Learn Chunked Pattern
import streamlit as st
from utils.localization import t
from utils.quiz_helper import render_mcq
from utils.ask_yourself import render_ask_yourself
from utils.exam_essentials import render_exam_essentials
from utils.layouts import render_comparison, render_formula_grid, render_decision_tree
from utils.layouts.foundation import inject_equal_height_css
from data.exam_questions import get_all_questions_for_topic
from utils.problem_renderer import render_open_question, render_multi_stage_problem

# ==========================================
# 1. CONTENT DICTIONARY - BILINGUAL
# ==========================================
content_8_4 = {
    "title": {"de": "8.4 Zusammenfassung", "en": "8.4 Summary"},
    "subtitle": {"de": "Punktschätzung im Überblick", "en": "Point Estimation at a Glance"},
    
    # --- CHAPTER INTUITION ---
    "intuition": {
        "header": {"de": "Das grosse Bild", "en": "The Big Picture"},
        "text": {
            "de": """Du hast gelernt, <strong>unbekannte Parameter aus Stichproben zu schätzen</strong>. 
            Von der Grundidee (Stichprobenmittel = Populationsmittel) über die <strong>4 Qualitätseigenschaften</strong> 
            (Erwartungstreue, Konsistenz, Effizienz, MSE) bis zu den <strong>2 Konstruktionsmethoden</strong> (MOM, MLE). 
            Diese Zusammenfassung zeigt dir, <strong>welche Formel wann</strong> — und die häufigsten Prüfungsfallen.""",
            "en": """You've learned to <strong>estimate unknown parameters from samples</strong>. 
            From the basic idea (sample mean = population mean) to the <strong>4 quality properties</strong> 
            (Unbiasedness, Consistency, Efficiency, MSE) to the <strong>2 construction methods</strong> (MOM, MLE). 
            This summary shows you <strong>which formula when</strong> — and the most common exam traps."""
        }
    },
    
    # === CHUNK 1: THE THREE ESTIMATORS ===
    "chunk_estimators": {
        "header": {"de": "Die drei wichtigsten Schätzer", "en": "The Three Key Estimators"},
        "estimators": [
            {
                "name": {"de": "Stichprobenmittel", "en": "Sample Mean"},
                "formula": r"\hat{\mu} = \bar{X} = \frac{1}{n}\sum_{i=1}^{n} X_i",
                "estimates": {"de": "Populationsmittel μ", "en": "Population mean μ"},
                "when": {"de": "Durchschnittswerte (Grösse, Gewicht)", "en": "Average values (height, weight)"}
            },
            {
                "name": {"de": "Stichprobenvarianz", "en": "Sample Variance"},
                "formula": r"\hat{\sigma}^2 = S^2_{n-1} = \frac{1}{n-1}\sum_{i=1}^{n}(X_i - \bar{X})^2",
                "estimates": {"de": "Populationsvarianz σ²", "en": "Population variance σ²"},
                "when": {"de": "Streuung, Risiko", "en": "Spread, risk"}
            },
            {
                "name": {"de": "Stichprobenanteil", "en": "Sample Proportion"},
                "formula": r"\hat{p} = \frac{\text{Erfolge}}{n}",
                "formula_en": r"\hat{p} = \frac{\text{Successes}}{n}",
                "estimates": {"de": "Erfolgswahrscheinlichkeit p", "en": "Success probability p"},
                "when": {"de": "Anteile, Quoten", "en": "Proportions, rates"}
            }
        ],
        "mcq": {
            "question": {"de": "Welcher Schätzer ist für den Populationsanteil $p$ zuständig?", 
                        "en": "Which estimator is used for the population proportion $p$?"},
            "options": [
                {"de": "$\\bar{X}$ (Stichprobenmittel)", "en": "$\\bar{X}$ (Sample Mean)"},
                {"de": "$S^2$ (Stichprobenvarianz)", "en": "$S^2$ (Sample Variance)"},
                {"de": "$\\hat{p}$ (Stichprobenanteil)", "en": "$\\hat{p}$ (Sample Proportion)"},
                {"de": "MSE (Mittlerer quadratischer Fehler)", "en": "MSE (Mean Squared Error)"}
            ],
            "correct_idx": 2,
            "solution": {
                "de": "$\\hat{p}$ <strong>(Stichprobenanteil)</strong> schätzt die Erfolgswahrscheinlichkeit $p$ aus der Stichprobe: Anzahl Erfolge geteilt durch $n$.",
                "en": "$\\hat{p}$ <strong>(Sample Proportion)</strong> estimates the success probability $p$ from the sample: number of successes divided by $n$."
            }
        }
    },
    
    # === CHUNK 2: THE FOUR PROPERTIES ===
    "chunk_properties": {
        "header": {"de": "Die 4 Eigenschaften", "en": "The 4 Properties"},
        "properties": [
            {
                "name": {"de": "Erwartungstreue", "en": "Unbiasedness"},
                "formula": r"E[T] = \theta",
                "meaning": {"de": "Trifft im Durchschnitt den wahren Wert", "en": "Hits the true value on average"}
            },
            {
                "name": {"de": "Konsistenz", "en": "Consistency"},
                "formula": r"T_n \xrightarrow{P} \theta",
                "meaning": {"de": "Wird mit mehr Daten immer genauer", "en": "Gets more precise with more data"}
            },
            {
                "name": {"de": "Effizienz", "en": "Efficiency"},
                "formula": r"\text{Var}(T) \leq \text{Var}(U)",
                "meaning": {"de": "Kleinste Varianz unter allen unbiased Schätzern", "en": "Smallest variance among all unbiased estimators"}
            },
            {
                "name": {"de": "MSE", "en": "MSE"},
                "formula": r"\text{MSE} = \text{Bias}^2 + \text{Var}",
                "meaning": {"de": "Gesamtfehler (Verzerrung + Streuung)", "en": "Total error (bias + variance)"}
            }
        ],
        "mcq": {
            "question": {"de": "Welche Eigenschaft bedeutet: Je grösser $n$, desto näher am wahren Wert?", 
                        "en": "Which property means: The larger $n$, the closer to the true value?"},
            "options": [
                {"de": "Erwartungstreue: $E[T] = \\theta$", "en": "Unbiasedness: $E[T] = \\theta$"},
                {"de": "Konsistenz: $T_n \\xrightarrow{P} \\theta$", "en": "Consistency: $T_n \\xrightarrow{P} \\theta$"},
                {"de": "Effizienz: $\\text{Var}(T) \\leq \\text{Var}(U)$", "en": "Efficiency: $\\text{Var}(T) \\leq \\text{Var}(U)$"},
                {"de": "Bias: $\\theta - E[T]$", "en": "Bias: $\\theta - E[T]$"}
            ],
            "correct_idx": 1,
            "solution": {
                "de": "<strong>Konsistenz</strong> bedeutet, dass der Schätzer stochastisch gegen den wahren Wert konvergiert, wenn $n \\to \\infty$.",
                "en": "<strong>Consistency</strong> means the estimator converges in probability to the true value as $n \\to \\infty$."
            }
        }
    },
    
    # === CHUNK 3: n vs (n-1) ===
    "chunk_variance": {
        "header": {"de": "n vs (n-1) — Der Varianz-Trick", "en": "n vs (n-1) — The Variance Trick"},
        "comparison": {
            "left": {
                "title": {"de": "S² (VERZERRT)", "en": "S² (BIASED)"},
                "formula": r"S^2 = \frac{1}{n}\sum(X_i - \bar{X})^2",
                "insight": {"de": "Unterschätzt systematisch!", "en": "Systematically underestimates!"}
            },
            "right": {
                "title": {"de": "S²ₙ₋₁ (UNVERZERRT)", "en": "S²ₙ₋₁ (UNBIASED)"},
                "formula": r"S^2_{n-1} = \frac{1}{n-1}\sum(X_i - \bar{X})^2",
                "insight": {"de": "Trifft den wahren Wert!", "en": "Hits the true value!"}
            }
        },
        "mcq": {
            "question": {"de": "Für einen erwartungstreuen Varianzschätzer teilst du durch...", 
                        "en": "For an unbiased variance estimator, you divide by..."},
            "options": [
                {"de": "$n$", "en": "$n$"},
                {"de": "$n-1$", "en": "$n-1$"},
                {"de": "$n+1$", "en": "$n+1$"},
                {"de": "$2n$", "en": "$2n$"}
            ],
            "correct_idx": 1,
            "solution": {
                "de": "<strong>$(n-1)$</strong> — Wir verlieren einen Freiheitsgrad durch die Schätzung von $\\bar{X}$. Das korrigiert die Verzerrung!",
                "en": "<strong>$(n-1)$</strong> — We lose one degree of freedom from estimating $\\bar{X}$. This corrects the bias!"
            }
        }
    },
    
    # === CHUNK 4: MOM vs MLE ===
    "chunk_methods": {
        "header": {"de": "MOM vs MLE", "en": "MOM vs MLE"},
        "comparison": {
            "left": {
                "title": {"de": "Momentenmethode (MOM)", "en": "Method of Moments (MOM)"},
                "formula": r"\bar{X} = E[X] \implies \text{solve for } \theta",
                "insight": {"de": "Schnell und einfach — setze Sample = Theorie", "en": "Quick and simple — set sample = theory"}
            },
            "right": {
                "title": {"de": "Maximum-Likelihood (MLE)", "en": "Maximum Likelihood (MLE)"},
                "formula": r"\frac{d \log L(\theta)}{d\theta} = 0",
                "insight": {"de": "Optimal — maximiere Plausibilität", "en": "Optimal — maximize plausibility"}
            }
        },
        "mcq": {
            "question": {"de": "Für $U[0,b]$: Sind MOM und MLE gleich?", 
                        "en": "For $U[0,b]$: Are MOM and MLE the same?"},
            "options": [
                {"de": "Ja, beide: $2 \\cdot \\bar{X}$", "en": "Yes, both: $2 \\cdot \\bar{X}$"},
                {"de": "Ja, beide: $\\max(X_i)$", "en": "Yes, both: $\\max(X_i)$"},
                {"de": "Nein: MOM $= 2\\bar{X}$, MLE $= \\max(X_i)$", "en": "No: MOM $= 2\\bar{X}$, MLE $= \\max(X_i)$"},
                {"de": "Nein: MOM $= \\max(X_i)$, MLE $= 2\\bar{X}$", "en": "No: MOM $= \\max(X_i)$, MLE $= 2\\bar{X}$"}
            ],
            "correct_idx": 2,
            "solution": {
                "de": "<strong>MOM $= 2\\bar{X}$, MLE $= \\max(X_i)$</strong> — Bei der Gleichverteilung sind sie verschieden! MLE ist hier besser: $b$ muss $\\geq \\max(X_i)$ sein.",
                "en": "<strong>MOM $= 2\\bar{X}$, MLE $= \\max(X_i)$</strong> — For Uniform, they differ! MLE is better here: $b$ must be $\\geq \\max(X_i)$."
            }
        }
    },
    
    # === KEY FORMULAS ===
    "key_formulas": {
        "header": {"de": "Formel-Übersicht", "en": "Formula Overview"},
        "formulas": [
            {"name": {"de": "Stichprobenmittel", "en": "Sample Mean"}, 
             "formula": r"\bar{X} = \frac{1}{n}\sum X_i", 
             "when": {"de": "Schätzer für μ", "en": "Estimator for μ"}, 
             "example": {"de": "Erwartungstreu", "en": "Unbiased"}},
            {"name": {"de": "Unbiased Variance", "en": "Unbiased Variance"}, 
             "formula": r"S^2_{n-1} = \frac{1}{n-1}\sum(X_i-\bar{X})^2", 
             "when": {"de": "Schätzer für σ²", "en": "Estimator for σ²"}, 
             "example": {"de": "(n-1) im Nenner!", "en": "(n-1) in denominator!"}},
            {"name": {"de": "Erwartungstreue", "en": "Unbiasedness"}, 
             "formula": r"E[T] = \theta", 
             "when": {"de": "Kein Bias", "en": "No bias"}, 
             "example": {"de": "Bias = 0", "en": "Bias = 0"}},
            {"name": {"de": "Konsistenz", "en": "Consistency"}, 
             "formula": r"T_n \xrightarrow{P} \theta", 
             "when": {"de": "Konvergenz", "en": "Convergence"}, 
             "example": {"de": "Var → 0", "en": "Var → 0"}},
            {"name": {"de": "MOM", "en": "MOM"}, 
             "formula": r"\bar{X} = E[X]", 
             "when": {"de": "Schnell", "en": "Quick"}, 
             "example": {"de": "Gleichsetzen", "en": "Set equal"}},
            {"name": {"de": "MLE", "en": "MLE"}, 
             "formula": r"\frac{d\ell}{d\theta} = 0", 
             "when": {"de": "Optimal", "en": "Optimal"}, 
             "example": {"de": "Log-Likelihood", "en": "Log-Likelihood"}}
        ]
    },
    
    # === ASK YOURSELF ===
    # NOTE: render_ask_yourself uses unsafe_allow_html=True which disables LaTeX
    # So we use Unicode symbols instead
    "ask_yourself": {
        "header": {"de": "Frag dich selbst", "en": "Ask Yourself"},
        "questions": [
            {"de": "Was bedeutet θ̂ vs θ?", "en": "What does θ̂ vs θ mean?"},
            {"de": "Welche Eigenschaft bedeutet E[T] = θ?", "en": "Which property means E[T] = θ?"},
            {"de": "Warum teilen wir durch (n-1) bei der Varianz?", "en": "Why divide by (n-1) for variance?"},
            {"de": "Für Poisson: Sind MOM und MLE gleich?", "en": "For Poisson: Are MOM and MLE the same?"},
            {"de": "Was unterscheidet Konsistenz von Erwartungstreue?", "en": "What distinguishes consistency from unbiasedness?"}
        ],
        "conclusion": {"de": "Wenn du alle beantworten kannst, bist du bereit für Kapitel 8!", 
                      "en": "If you can answer all, you're ready for Chapter 8!"}
    },
    
    # === EXAM ESSENTIALS ===
    "exam_essentials": {
        "trap": {
            "de": "Verwechslung von <strong>$n$ und $(n-1)$</strong> bei der Varianz! Bei 'erwartungstreuer Varianzschätzer' IMMER durch $(n-1)$ teilen.",
            "en": "Confusing <strong>$n$ and $(n-1)$</strong> for variance! For 'unbiased variance estimator' ALWAYS divide by $(n-1)$."
        },
        "trap_rule": {
            "de": "Merke: 1 Freiheitsgrad geht verloren durch Schätzung von $\\bar{X}$",
            "en": "Remember: 1 degree of freedom is lost from estimating $\\bar{X}$"
        },
        "tips": [
            {
                "tip": {"de": "Hut = Schätzung", "en": "Hat = Estimate"},
                "why": {"de": "$\\hat{\\theta}$ = geschätzt aus Daten, $\\theta$ = wahrer Wert", "en": "$\\hat{\\theta}$ = estimated from data, $\\theta$ = true value"}
            },
            {
                "tip": {"de": "Konsistenz braucht zwei Bedingungen", "en": "Consistency needs two conditions"},
                "why": {"de": "Erwartungstreu (asymptotisch) + Varianz $\\to 0$", "en": "Unbiased (asymptotically) + Variance $\\to 0$"}
            },
            {
                "tip": {"de": "MLE für $U[0,b]$: $\\max(X_i)$", "en": "MLE for $U[0,b]$: $\\max(X_i)$"},
                "why": {"de": "NICHT $2\\bar{X}$! Das ist MOM.", "en": "NOT $2\\bar{X}$! That's MOM."},
                "why_formula": r"\hat{b}_{MLE} = \max(X_1, \ldots, X_n)"
            }
        ]
    }
}


# ==========================================
# 2. RENDER FUNCTION
# ==========================================
def render_subtopic_8_4(model):
    """8.4 Summary — ULTRATHINK Learn-Test-Learn Flow"""
    inject_equal_height_css()
    
    st.header(t(content_8_4["title"]))
    st.caption(t(content_8_4["subtitle"]))
    st.markdown("---")
    
    # === CHAPTER INTUITION (Grey Callout) ===
    st.markdown(f"""
<div style="background: #f4f4f5; border-left: 4px solid #a1a1aa; 
            padding: 12px 16px; border-radius: 8px; color: #3f3f46;">
<strong>{t(content_8_4["intuition"]["header"])}:</strong><br>
{t(content_8_4["intuition"]["text"])}
</div>
""", unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # === CHUNK 1: THE THREE ESTIMATORS ===
    render_chunk_estimators(model)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # === CHUNK 2: THE FOUR PROPERTIES ===
    render_chunk_properties(model)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # === CHUNK 3: n vs (n-1) ===
    render_chunk_variance(model)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # === CHUNK 4: MOM vs MLE ===
    render_chunk_methods(model)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # === KEY FORMULAS ===
    render_key_formulas()
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # === ASK YOURSELF ===
    render_ask_yourself(
        header=content_8_4["ask_yourself"]["header"],
        questions=content_8_4["ask_yourself"]["questions"],
        conclusion=content_8_4["ask_yourself"]["conclusion"]
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # === EXAM ESSENTIALS ===
    render_exam_essentials(
        tips=content_8_4["exam_essentials"]["tips"],
        trap=content_8_4["exam_essentials"]["trap"],
        trap_rule=content_8_4["exam_essentials"]["trap_rule"]
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # === OFFICIAL EXAM QUESTIONS ===
    st.markdown(f"### {t({'de': 'Prüfungstraining', 'en': 'Exam Practice'})}")
    
    questions = get_all_questions_for_topic("8.4")
    
    for q_id, q in questions.items():
        q_type = q.get("type", "mc")
        
        if q_type == "multi_stage":
            render_multi_stage_problem(
                key_suffix=f"8_4_{q_id}",
                stem_text=q.get("stem", {}),
                parts=q.get("parts", []),
                source=q.get("source", ""),
                model=model,
                ai_context=f"Estimation Problem: {q_id}",
                course_id="vwl",
                topic_id="8",
                subtopic_id="8.4",
                question_id=q_id
            )
        elif q_type == "problem" or q_type == "open":
            render_open_question(
                key_suffix=f"8_4_{q_id}",
                question_text=q["question"],
                solution_text_dict=q["solution"],
                source=q.get("source", ""),
                hints=q.get("hints", []),
                model=model,
                ai_context=f"Estimation Problem: {q_id}",
                course_id="vwl",
                topic_id="8",
                subtopic_id="8.4",
                question_id=q_id
            )
        else:
            # MC type
            with st.container(border=True):
                st.caption(q.get("source", ""))
                opts = q.get("options", [])
                if opts and isinstance(opts[0], dict):
                    option_labels = [t(o) for o in opts]
                else:
                    option_labels = opts
                
                render_mcq(
                    key_suffix=f"8_4_{q_id}",
                    question_text=t(q["question"]),
                    options=option_labels,
                    correct_idx=q["correct_idx"],
                    solution_text_dict=q["solution"],
                    success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                    error_msg_dict={"de": "Falsch.", "en": "Incorrect."},
                    client=model,
                    ai_context=f"Estimation Drill: {q_id}",
                    course_id="vwl",
                    topic_id="8",
                    subtopic_id="8.4",
                    question_id=q_id
                )
        st.markdown("<br>", unsafe_allow_html=True)


# ==========================================
# 3. CHUNK RENDER FUNCTIONS
# ==========================================

def render_chunk_estimators(model):
    """Chunk 1: The Three Key Estimators"""
    chunk = content_8_4["chunk_estimators"]
    st.markdown(f"### {t(chunk['header'])}")
    
    # 3-column layout for estimators
    cols = st.columns(3, gap="medium")
    
    for col, est in zip(cols, chunk["estimators"]):
        with col:
            with st.container(border=True):
                st.markdown(f"**{t(est['name'])}**")
                # Use bilingual formula if available
                if "formula_en" in est and t({"de": "x", "en": "y"}) == "y":
                    st.latex(est["formula_en"])
                else:
                    st.latex(est["formula"])
                st.markdown("---")
                st.markdown(f"*{t({'de': 'Schätzt', 'en': 'Estimates'})}:* {t(est['estimates'])}")
                st.caption(t(est["when"]))
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Quick Check MCQ
    render_chunk_mcq(chunk, "estimators", model)


def render_chunk_properties(model):
    """Chunk 2: The Four Properties"""
    chunk = content_8_4["chunk_properties"]
    st.markdown(f"### {t(chunk['header'])}")
    
    # 2x2 layout for properties
    props = chunk["properties"]
    for i in range(0, len(props), 2):
        cols = st.columns(2, gap="medium")
        for j, col in enumerate(cols):
            if i + j < len(props):
                prop = props[i + j]
                with col:
                    with st.container(border=True):
                        st.markdown(f"**{t(prop['name'])}**")
                        st.latex(prop["formula"])
                        st.caption(t(prop["meaning"]))
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Quick Check MCQ
    render_chunk_mcq(chunk, "properties", model)


def render_chunk_variance(model):
    """Chunk 3: n vs (n-1)"""
    chunk = content_8_4["chunk_variance"]
    st.markdown(f"### {t(chunk['header'])}")
    
    render_comparison(
        title={"de": "", "en": ""},
        left=chunk["comparison"]["left"],
        right=chunk["comparison"]["right"],
        show_header=False
    )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Quick Check MCQ
    render_chunk_mcq(chunk, "variance", model)


def render_chunk_methods(model):
    """Chunk 4: MOM vs MLE"""
    chunk = content_8_4["chunk_methods"]
    st.markdown(f"### {t(chunk['header'])}")
    
    render_comparison(
        title={"de": "", "en": ""},
        left=chunk["comparison"]["left"],
        right=chunk["comparison"]["right"],
        show_header=False
    )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Quick Check MCQ
    render_chunk_mcq(chunk, "methods", model)


def render_chunk_mcq(chunk, chunk_id, model):
    """Render MCQ for a chunk"""
    mcq = chunk["mcq"]
    opts = [t(o) for o in mcq["options"]]
    
    with st.container(border=True):
        st.markdown(f"**{t({'de': 'Schnell-Check', 'en': 'Quick Check'})}**")
        
        render_mcq(
            key_suffix=f"8_4_{chunk_id}",
            question_text=t(mcq["question"]),
            options=opts,
            correct_idx=mcq["correct_idx"],
            solution_text_dict=mcq["solution"],
            success_msg_dict={"de": "Richtig!", "en": "Correct!"},
            error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
            client=model,
            ai_context=f"Point Estimation summary: {chunk_id} concepts",
            course_id="vwl",
            topic_id="8",
            subtopic_id="8.4",
            question_id=f"8_4_quick_{chunk_id}"
        )


def render_key_formulas():
    """Render all key formulas in a 2-column grid"""
    kf = content_8_4["key_formulas"]
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
