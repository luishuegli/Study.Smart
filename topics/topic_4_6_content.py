# Topic 4.6: Exponential Distribution - Exponentialverteilung
# ULTRATHINK ENHANCED VERSION
import streamlit as st
from views.styles import inject_equal_height_css
from utils.localization import t
from utils.layouts.foundation import grey_info
from utils.quiz_helper import render_mcq
from data.exam_questions import get_question
import numpy as np
import plotly.graph_objects as go
from scipy.stats import expon

# ==========================================
# 1. CONTENT DICTIONARY - BILINGUAL (ULTRATHINK)
# ==========================================
content_4_6 = {
    "title": {"de": "4.6 Exponentialverteilung (stetig)", "en": "4.6 Exponential Distribution (Continuous)"},
    "subtitle": {
        "de": "Die Verteilung der Warte- und Lebensdauern",
        "en": "The Distribution of Waiting and Lifetime"
    },
    
    # --- INTUITION HOOK ---
    "intuition": {
        "header": {"de": "Die Intuition", "en": "The Intuition"},
        "text": {
            "de": "Wie lange brennt eine **Glühbirne** noch? Wie lange muss ich auf den nächsten **Bus** warten? Wie lange funktioniert mein **Laptop** noch? Die Exponentialverteilung modelliert die **Wartezeit bis zum nächsten Ereignis** — und hat eine faszinierende Eigenschaft: Sie ist **gedächtnislos**.",
            "en": "How long will a **light bulb** last? How long until the next **bus** arrives? How long will my **laptop** keep working? The exponential distribution models the **waiting time until the next event** — and has a fascinating property: It's **memoryless**."
        }
    },
    
    # --- FRAG DICH (Decision Guide) ---
    "frag_dich": {
        "header": {"de": "Frag dich: Ist es Exponential?", "en": "Ask yourself: Is it Exponential?"},
        "questions": [
            {"de": "Modelliere ich eine <strong>Wartezeit/Lebensdauer</strong>?", "en": "Am I modeling a <strong>waiting time/lifetime</strong>?"},
            {"de": "Ist die Wartezeit <strong>stetig</strong> (jeder positive Wert möglich)?", "en": "Is the waiting time <strong>continuous</strong> (any positive value possible)?"},
            {"de": "Ist die Ausfallrate <strong>konstant</strong> über die Zeit?", "en": "Is the failure rate <strong>constant</strong> over time?"},
            {"de": "Hängt das Ereignis mit einem <strong>Poisson-Prozess</strong> zusammen?", "en": "Is the event related to a <strong>Poisson process</strong>?"}
        ],
        "conclusion": {
            "de": "Mehrfach Ja → Exponentialverteilung prüfen!",
            "en": "Multiple Yes → Check Exponential Distribution!"
        }
    },
    
    # --- DEFINITION ---
    "definition": {
        "header": {"de": "Definition", "en": "Definition"},
        "text": {
            "de": "Eine **stetige** Zufallsvariable $X$ mit Wertevorrat $[0, \\infty)$ heisst **exponentialverteilt** mit Parameter $\\lambda > 0$.",
            "en": "A **continuous** random variable $X$ with value range $[0, \\infty)$ is called **exponentially distributed** with parameter $\\lambda > 0$."
        },
        "notation": r"X \sim \text{Ex}(\lambda)"
    },
    
    # --- FORMULAS (With Breakdown) ---
    "formula": {
        "header": {"de": "Dichte- und Verteilungsfunktion", "en": "Density and Distribution Function"},
        "pdf": r"f_{\text{Ex}}(x; \lambda) = \lambda e^{-\lambda x}, \quad x \geq 0",
        "cdf": r"F_{\text{Ex}}(x; \lambda) = 1 - e^{-\lambda x}, \quad x \geq 0",
        "breakdown": {
            "header": {"de": "Was bedeutet jede Formel? (Intuition!)", "en": "What does each formula mean? (Intuition!)"},
            "pdf_intuition": {
                "de": "<strong>PDF f(x) = λe<sup>-λx</sup>:</strong> Je länger du wartest (größeres x), desto unwahrscheinlicher wird diese spezifische Wartezeit. Das e<sup>-λx</sup> ist ein 'Verfall' — hohe Wahrscheinlichkeit für kurze Wartezeiten, niedrige für lange.",
                "en": "<strong>PDF f(x) = λe<sup>-λx</sup>:</strong> The longer you wait (larger x), the less likely that specific waiting time becomes. The e<sup>-λx</sup> is a 'decay' — high probability for short waits, low for long waits."
            },
            "cdf_intuition": {
                "de": "<strong>CDF F(x) = 1 - e<sup>-λx</sup>:</strong> 'Wie wahrscheinlich ist es, dass ich innerhalb von x Zeiteinheiten fertig bin?' Startet bei 0 (für x=0), nähert sich 1 für große x. Bei x = 1/λ (mittlere Wartezeit) ist F ≈ 63%.",
                "en": "<strong>CDF F(x) = 1 - e<sup>-λx</sup>:</strong> 'How likely is it that I finish within x time units?' Starts at 0 (for x=0), approaches 1 for large x. At x = 1/λ (mean wait), F ≈ 63%."
            },
            "example": {
                "de": "<strong>Beispiel:</strong> Glühbirne hält durchschnittlich 5000 Stunden → λ = 1/5000. P(kaputt vor 2500h) = 1 - e<sup>-0.0002×2500</sup> = 1 - e<sup>-0.5</sup> ≈ 39%.",
                "en": "<strong>Example:</strong> Bulb lasts on average 5000 hours → λ = 1/5000. P(broken before 2500h) = 1 - e<sup>-0.0002×2500</sup> = 1 - e<sup>-0.5</sup> ≈ 39%."
            }
        },
        "survival": {
            "header": {"de": "Überlebenswahrscheinlichkeit", "en": "Survival Probability"},
            "formula": r"P(X > x) = e^{-\lambda x}",
            "meaning_de": "Die Wahrscheinlichkeit, dass das System NOCH läuft nach Zeit x. <br><br><strong>Beispiel:</strong> Glühbirne mit λ = 0.001 pro Stunde → P(überlebt 1000h) = e<sup>−1</sup> ≈ 37%.",
            "meaning_en": "The probability that the system is STILL running after time x. <br><br><strong>Example:</strong> Light bulb with λ = 0.001 per hour → P(survives 1000h) = e<sup>−1</sup> ≈ 37%."
        }
    },
    
    # --- PARAMETER WITH MEANING ---
    "parameter": {
        "header": {"de": "Der Parameter", "en": "The Parameter"},
        "symbol": r"\lambda > 0",
        "name_de": "Ereignisrate",
        "name_en": "Event Rate",
        "meaning_de": "Durchschnittliche Anzahl von Ereignissen pro Zeiteinheit. ACHTUNG: Die mittlere Wartezeit ist $\\frac{1}{\\lambda}$!",
        "meaning_en": "Average number of events per time unit. CAUTION: The mean waiting time is $\\frac{1}{\\lambda}$!"
    },
    
    # --- MOMENTS WITH INTERPRETATION ---
    "moments": {
        "header": {"de": "Erwartungswert & Varianz", "en": "Expected Value & Variance"},
        "expectation": {
            "title_de": "Erwartungswert",
            "title_en": "Expected Value",
            "formula": r"E[X] = \frac{1}{\lambda}",
            "interpretation_de": "Die durchschnittliche Wartezeit bis zum Ereignis. Wenn $\\lambda = 2$ pro Stunde, warte ich im Schnitt $\\frac{1}{2}$ Stunde = 30 Minuten.",
            "interpretation_en": "The average waiting time until the event. If $\\lambda = 2$ per hour, I wait on average $\\frac{1}{2}$ hour = 30 minutes."
        },
        "variance": {
            "title_de": "Varianz",
            "title_en": "Variance",
            "formula": r"V(X) = \frac{1}{\lambda^2}",
            "interpretation_de": "Niedrige Rate = hohe Varianz. Seltene Ereignisse haben grosse Streuung in der Wartezeit.",
            "interpretation_en": "Low rate = high variance. Rare events have large variation in waiting time."
        }
    },
    
    # --- THE KEY PROPERTY: MEMORYLESSNESS ---
    "memoryless": {
        "header": {"de": "Gedächtnislosigkeit (DIE Kernidee!)", "en": "Memorylessness (THE Core Idea!)"},
        "text": {
            "de": "Stell dir eine Glühbirne vor, die schon 1000 Stunden brennt. Ist sie 'müde'? Bei der Exponentialverteilung: <strong>NEIN!</strong> Die Wahrscheinlichkeit, noch weitere 100 Stunden zu brennen, ist <strong>dieselbe</strong> wie bei einer neuen Birne.",
            "en": "Imagine a light bulb that has been burning for 1000 hours. Is it 'tired'? With the exponential distribution: <strong>NO!</strong> The probability of burning another 100 hours is <strong>the same</strong> as for a new bulb."
        },
        "formula": r"P(X > s + t \mid X > s) = P(X > t)",
        "meaning": {
            "de": "'Gegeben, ich habe schon s gewartet, ist die Restwartezeit unabhängig davon.'",
            "en": "'Given that I've already waited s, the remaining waiting time is independent of that.'"
        },
        "counterexample": {
            "de": "Kontrast: Bei einem Auto ist das NICHT so. Ein 10 Jahre altes Auto ist wahrscheinlicher defekt als ein neues. → Nicht exponential!",
            "en": "Contrast: For a car, this is NOT true. A 10-year-old car is more likely to break down than a new one. → Not exponential!"
        }
    },
    
    # --- CONNECTION TO POISSON ---
    "connection": {
        "header": {"de": "Verbindung zur Poisson-Verteilung", "en": "Connection to Poisson Distribution"},
        "text": {
            "de": "Poisson und Exponential sind Geschwister! Sie beschreiben denselben Prozess aus zwei Perspektiven:",
            "en": "Poisson and Exponential are siblings! They describe the same process from two perspectives:"
        },
        "comparison": [
            {"de": "<strong>Poisson</strong>: Wie VIELE Ereignisse in einer festen Zeit?", "en": "<strong>Poisson</strong>: How MANY events in a fixed time?"},
            {"de": "<strong>Exponential</strong>: Wie LANGE bis zum nächsten Ereignis?", "en": "<strong>Exponential</strong>: How LONG until the next event?"}
        ],
        "same_lambda": {
            "de": "Beide verwenden dasselbe λ (Ereignisrate)!",
            "en": "Both use the same λ (event rate)!"
        }
    },
    
    # --- WORKED EXAMPLE ---
    "example_worked": {
        "header": {"de": "Schritt-für-Schritt Beispiel", "en": "Step-by-Step Example"},
        "problem": {
            "de": "Die mittlere Lebensdauer einer Glühbirne beträgt <strong>5000 Stunden</strong>. Wie wahrscheinlich ist, dass sie weniger als halb so lange brennt?",
            "en": "The average lifetime of a light bulb is <strong>5000 hours</strong>. What is the probability that it burns less than half as long?"
        },
        "steps": [
            {
                "label": {"de": "Gegeben", "en": "Given"},
                "latex": r"E[X] = {\color{#007AFF}5000} \text{ h} \quad \Rightarrow \quad {\color{#007AFF}\lambda = \frac{1}{5000}}",
                "note": None
            },
            {
                "label": {"de": "Gesucht", "en": "Find"},
                "latex": r"P(X < {\color{#FF4B4B}2500})",
                "note": {"de": "Halb so lang wie erwartet", "en": "Half the expected lifetime"}
            },
            {
                "label": {"de": "Formel", "en": "Formula"},
                "latex": r"P(X < {\color{#FF4B4B}2500}) = F({\color{#FF4B4B}2500}) = 1 - e^{-{\color{#007AFF}\lambda} \cdot {\color{#FF4B4B}2500}}",
                "note": None
            },
            {
                "label": {"de": "Rechnung", "en": "Calculation"},
                "latex": r"= 1 - e^{-\frac{{\color{#FF4B4B}2500}}{{\color{#007AFF}5000}}} = 1 - e^{-0.5} \approx 1 - 0.6065 = \mathbf{0.3935}",
                "note": None
            }
        ],
        "answer": {
            "de": "Die Wahrscheinlichkeit beträgt etwa **39.35%**.",
            "en": "The probability is approximately **39.35%**."
        }
    },
    
    # --- EXAM ESSENTIALS (Merged Trap + Pro Tip) ---
    "exam_essentials": {
        "header": {"de": "Prüfungs-Essentials", "en": "Exam Essentials"},
        "items": [
            {
                "label": {"de": "Falle", "en": "Trap"},
                "title": {"de": "λ vs. 1/λ verwechseln!", "en": "Confusing λ and 1/λ!"},
                "content": {
                    "de": "'Mittlere Lebensdauer = 5000h' ist E[X] = 1/λ, <strong>nicht λ</strong>!<br><em>Merke:</em> λ = Rate (pro Zeit), 1/λ = mittlere Wartezeit",
                    "en": "'Average lifetime = 5000h' is E[X] = 1/λ, <strong>not λ</strong>!<br><em>Remember:</em> λ = rate (per time), 1/λ = mean waiting time"
                },
                "type": "warning"
            },
            {
                "label": {"de": "Formel", "en": "Formula"},
                "title": {"de": "P(X > x) = e^−λx", "en": "P(X > x) = e^−λx"},
                "content": {
                    "de": "Auswendig lernen! 'Wie wahrscheinlich dauert es länger als x?' → direkt anwenden.",
                    "en": "Memorize this! 'How likely does it last longer than x?' → apply directly."
                },
                "type": "tip"
            },
            {
                "label": {"de": "Konzept", "en": "Concept"},
                "title": {"de": "Gedächtnislosigkeit", "en": "Memorylessness"},
                "content": {
                    "de": "P(X > s+t | X > s) = P(X > t). Die Restwartezeit ist unabhängig davon, wie lange du schon gewartet hast!",
                    "en": "P(X > s+t | X > s) = P(X > t). Remaining time is independent of how long you've already waited!"
                },
                "type": "tip"
            }
        ]
    }
}


def render_subtopic_4_6(model):
    """4.6 Exponentialverteilung - ULTRATHINK Enhanced"""
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
    st.header(t(content_4_6["title"]))
    st.caption(t(content_4_6["subtitle"]))
    st.markdown("---")
    
    # --- INTUITION HOOK ---
    st.markdown(f"### {t(content_4_6['intuition']['header'])}")
    with st.container(border=True):
        st.markdown(t(content_4_6["intuition"]["text"]))
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- FRAG DICH: DECISION GUIDE ---
    from utils.ask_yourself import render_ask_yourself
    render_ask_yourself(
        header=content_4_6['frag_dich']['header'],
        questions=content_4_6['frag_dich']['questions'],
        conclusion=content_4_6['frag_dich']['conclusion']
    )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- DEFINITION ---
    st.markdown(f"### {t(content_4_6['definition']['header'])}")
    with st.container(border=True):
        st.markdown(t(content_4_6["definition"]["text"]))
        st.markdown("<br>", unsafe_allow_html=True)
        st.latex(content_4_6["definition"]["notation"])
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- PDF, CDF, SURVIVAL ---
    st.markdown(f"### {t(content_4_6['formula']['header'])}")
    
    col_pdf, col_cdf = st.columns(2, gap="medium")
    
    with col_pdf:
        with st.container(border=True):
            st.markdown(f"**{t({'de': 'Dichtefunktion (PDF)', 'en': 'Density Function (PDF)'})}**")
            st.latex(content_4_6["formula"]["pdf"])
            st.markdown("---")
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown(t(content_4_6["formula"]["breakdown"]["pdf_intuition"]), unsafe_allow_html=True)
    
    with col_cdf:
        with st.container(border=True):
            st.markdown(f"**{t({'de': 'Verteilungsfunktion (CDF)', 'en': 'Distribution Function (CDF)'})}**")
            st.latex(content_4_6["formula"]["cdf"])
            st.markdown("---")
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown(t(content_4_6["formula"]["breakdown"]["cdf_intuition"]), unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Example callout
    example_text = t(content_4_6["formula"]["breakdown"]["example"])
    st.markdown(f"""
<div style="background-color: #f4f4f5; border-radius: 8px; padding: 12px; border-left: 4px solid #a1a1aa; color: #3f3f46;">
{example_text}
</div>""", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    with st.container(border=True):
        st.markdown(f"**{t(content_4_6['formula']['survival']['header'])}**")
        col_f, col_m = st.columns([1, 2])
        with col_f:
            st.latex(content_4_6["formula"]["survival"]["formula"])
        with col_m:
            st.markdown(t({"de": content_4_6["formula"]["survival"]["meaning_de"], "en": content_4_6["formula"]["survival"]["meaning_en"]}), unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- PARAMETER ---
    st.markdown(f"### {t(content_4_6['parameter']['header'])}")
    with st.container(border=True):
        col_sym, col_desc = st.columns([1, 3])
        with col_sym:
            st.latex(content_4_6["parameter"]["symbol"])
        with col_desc:
            st.markdown(f"**{t({'de': content_4_6['parameter']['name_de'], 'en': content_4_6['parameter']['name_en']})}**")
            st.warning(t({"de": content_4_6["parameter"]["meaning_de"], "en": content_4_6["parameter"]["meaning_en"]}))
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- MOMENTS ---
    st.markdown(f"### {t(content_4_6['moments']['header'])}")
    
    col_e, col_v = st.columns(2, gap="medium")
    
    with col_e:
        with st.container(border=True):
            st.markdown(f"**{t({'de': content_4_6['moments']['expectation']['title_de'], 'en': content_4_6['moments']['expectation']['title_en']})}**")
            st.latex(content_4_6["moments"]["expectation"]["formula"])
            st.markdown("---")
            st.markdown(t({"de": content_4_6["moments"]["expectation"]["interpretation_de"], "en": content_4_6["moments"]["expectation"]["interpretation_en"]}))
    
    with col_v:
        with st.container(border=True):
            st.markdown(f"**{t({'de': content_4_6['moments']['variance']['title_de'], 'en': content_4_6['moments']['variance']['title_en']})}**")
            st.latex(content_4_6["moments"]["variance"]["formula"])
            st.markdown("---")
            st.markdown(t({"de": content_4_6["moments"]["variance"]["interpretation_de"], "en": content_4_6["moments"]["variance"]["interpretation_en"]}))
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- MEMORYLESSNESS (Key Property) ---
    st.markdown(f"### {t(content_4_6['memoryless']['header'])}")
    with st.container(border=True):
        st.markdown(t(content_4_6['memoryless']['text']), unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.latex(content_4_6["memoryless"]["formula"])
        st.markdown(t(content_4_6["memoryless"]["meaning"]))
        
        st.markdown("<br>", unsafe_allow_html=True)
        # Counterexample as grey callout
        counterexample_text = t(content_4_6["memoryless"]["counterexample"])
        st.markdown(f"""
<div style="background:#f4f4f5; padding:12px; border-radius:8px; color:#3f3f46; border-left: 4px solid #a1a1aa;">
{counterexample_text}
</div>""", unsafe_allow_html=True)
    
    # --- CONNECTION TO POISSON ---
    st.markdown(f"### {t(content_4_6['connection']['header'])}")
    with st.container(border=True):
        st.markdown(t(content_4_6["connection"]["text"]))
        
        for item in content_4_6["connection"]["comparison"]:
            st.markdown(t({"de": item["de"], "en": item["en"]}), unsafe_allow_html=True)
        
        same_lambda_text = t(content_4_6["connection"]["same_lambda"])
        st.markdown(f"""
<div style="background: #f4f4f5; border-left: 4px solid #a1a1aa; padding: 12px 16px; border-radius: 8px; color: #3f3f46;">
<strong>{same_lambda_text}</strong>
</div>
""", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- WORKED EXAMPLE ---
    st.markdown(f"### {t(content_4_6['example_worked']['header'])}")
    with st.container(border=True):
        
        st.markdown(t(content_4_6['example_worked']['problem']), unsafe_allow_html=True)
        
        st.markdown("---")
        
        for i, step in enumerate(content_4_6["example_worked"]["steps"]):
            if i > 0:
                st.markdown("---")
            
            st.markdown(f"**{t(step['label'])}:**")
            st.latex(step["latex"])
            
            if step.get("note"):
                st.caption(t(step["note"]))
        
        st.markdown("---")
        st.markdown(f"**{t(content_4_6['example_worked']['answer'])}**")
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- INTERACTIVE MISSION: EXPONENTIAL DISCOVERY ---
    st.markdown(f"### {t({'de': 'Mission: Der Zerfall-Durchbruch', 'en': 'Mission: The Decay Breakthrough'})}")
    
    # Mission state initialization
    if "exp_mission_done" not in st.session_state:
        st.session_state.exp_mission_done = False
    
    with st.container(border=True):
        # REAL-WORLD SCENARIO
        st.markdown(f"""
<div style="background: rgba(0, 122, 255, 0.08); padding:14px; border-radius:8px; color:#1c1c1e; margin-bottom:12px; border-left: 4px solid #007AFF;">
<strong>{t({'de': 'Szenario:', 'en': 'Scenario:'})}</strong> {t({'de': 'Ein Qualitätsingenieur testet Bauteile. Er muss wissen: Bei welcher Ausfallrate (λ) überleben weniger als 10% der Teile eine 2-jährige Garantiezeit?', 'en': 'A quality engineer tests components. They need to know: At what failure rate (λ) will less than 10% of parts survive a 2-year warranty period?'})}
</div>""", unsafe_allow_html=True)
        
        # THE MISSION GOAL
        t_checkpoint = 2.0
        target_survival = 0.10
        st.markdown(f"""
<div style="background:#f4f4f5; padding:16px; border-radius:8px; color:#3f3f46; border-left: 4px solid #a1a1aa;">
<strong>{t({'de': 'Deine Aufgabe:', 'en': 'Your Mission:'})}</strong> {t({'de': f'Finde den λ-Wert, bei dem die Überlebenswahrscheinlichkeit P(T > {t_checkpoint:.0f}) unter {target_survival*100:.0f}% fällt!', 'en': f'Find the λ value where survival probability P(T > {t_checkpoint:.0f}) drops below {target_survival*100:.0f}%!'})}
</div>""", unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        col_ctrl, col_chart = st.columns([1.2, 2.3], gap="large")
        
        with col_ctrl:
            lam = st.slider("λ", min_value=0.1, max_value=2.5, value=0.5, step=0.1, key="exp_lambda")
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            # Calculate probabilities
            mean_time = 1 / lam
            surv_prob = np.exp(-lam * t_checkpoint)
            goal_reached = surv_prob < target_survival
            
            # Semantic colored formula display
            prob_color = "#34C759" if goal_reached else "#FF4B4B"
            st.markdown(f"""
<div style="font-size: 1.0em;">
<strong>P(T > {t_checkpoint:.0f})</strong> = e<sup>-<span style="color:#007AFF;">λ</span>t</sup> = e<sup>-{lam:.1f}×{t_checkpoint:.0f}</sup> = <span style="color:{prob_color}; font-weight:bold;">{surv_prob:.1%}</span>
</div>""", unsafe_allow_html=True)
            
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown(f"**E[T] = 1/<span style='color:#007AFF;'>λ</span> = {mean_time:.2f}**", unsafe_allow_html=True)
            
            # Progress feedback
            st.markdown("<br>", unsafe_allow_html=True)
            if surv_prob >= 0.50:
                grey_info(t({"de": "λ ist noch klein. Der Zerfall ist langsam — hohe Überlebensrate.", "en": "λ is still small. Decay is slow — high survival rate."}))
            elif surv_prob >= target_survival:
                st.warning(t({"de": f"Fast da! P(T>2) = {surv_prob:.1%} — erhöhe λ für schnelleren Zerfall!", "en": f"Almost there! P(T>2) = {surv_prob:.1%} — increase λ for faster decay!"}))
            else:
                if not st.session_state.exp_mission_done:
                    st.balloons()
                    st.session_state.exp_mission_done = True
                    from utils.progress_tracker import track_question_answer
                    if user := st.session_state.get("user"):
                        track_question_answer(user["localId"], "vwl", "4", "4.6", "exp_mission", True)
                
                st.success(t({"de": f"Mission erfüllt! Bei λ = {lam:.1f} ist P(T>2) = {surv_prob:.1%} < 10%", "en": f"Mission Complete! At λ = {lam:.1f}, P(T>2) = {surv_prob:.1%} < 10%"}))
        
        with col_chart:
            t_range = np.linspace(0, 10, 200)
            survival_vals = np.exp(-lam * t_range)
            
            fig = go.Figure()
            
            # Survival curve
            fig.add_trace(go.Scatter(
                x=t_range, y=survival_vals,
                mode='lines', line=dict(color='#007AFF', width=2),
                name='S(t) = P(T > t)',
                hovertemplate='t=%{x:.1f}<br>S(t)=%{y:.3f}<extra></extra>'
            ))
            
            # Target checkpoint line
            fig.add_vline(x=t_checkpoint, line_dash="solid", line_color="#FF4B4B", line_width=2,
                         annotation_text=f"t={t_checkpoint:.0f}", annotation_position="top")
            
            # Target probability line
            fig.add_hline(y=target_survival, line_dash="dot", line_color="#a1a1aa", line_width=1,
                         annotation_text="10% Target", annotation_position="right")
            
            # Mean line
            fig.add_vline(x=mean_time, line_dash="dash", line_color="#34C759", line_width=2,
                         annotation_text=f"E[T]={mean_time:.1f}", annotation_position="bottom")
            
            # Mark current survival at checkpoint
            fig.add_trace(go.Scatter(
                x=[t_checkpoint], y=[surv_prob],
                mode='markers', marker=dict(size=12, color=prob_color, symbol='circle'),
                showlegend=False
            ))
            
            fig.update_layout(
                xaxis=dict(title="t", fixedrange=True, showgrid=False),
                yaxis=dict(title="S(t)", fixedrange=True, showgrid=True, gridcolor='#E5E5EA', range=[0, 1.1]),
                height=300,
                margin=dict(l=40, r=20, t=30, b=50),
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                legend=dict(orientation="h", y=1.1, x=0.5, xanchor="center")
            )
            
            st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
        
        # Mastery insight (shown after completion)
        if goal_reached:
            st.markdown(f"""
<div style="background:#f4f4f5; padding:16px; border-radius:8px; color:#3f3f46; margin-top:12px; border-left: 4px solid #a1a1aa;">
<strong>{t({'de': 'Was du entdeckt hast:', 'en': 'What you discovered:'})}</strong> {t({'de': 'Höheres λ bedeutet schnellerer Zerfall. Bei λ ≈ 1.15 ist die Überlebenswahrscheinlichkeit nach t=2 bereits unter 10%. Die Formel S(t) = e^(-λt) fällt exponentiell!', 'en': 'Higher λ means faster decay. At λ ≈ 1.15, survival probability after t=2 is already below 10%. The formula S(t) = e^(-λt) falls exponentially!'})}
</div>""", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- EXAM ESSENTIALS (Using Utility) ---
    from utils.exam_essentials import render_exam_essentials
    render_exam_essentials(items=content_4_6["exam_essentials"]["items"])
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- EXAM SECTION ---
    st.markdown(f"### {t({'de': 'Prüfungstraining', 'en': 'Exam Practice'})}")
    
    with st.container(border=True):
        st.markdown(f"""
<div style="background: #f4f4f5; border-left: 4px solid #a1a1aa; padding: 12px 16px; border-radius: 8px; color: #3f3f46;">
{t({"de": "Für diesen Abschnitt gibt es derzeit keine MCQ-Fragen. Die Theorie oben deckt die Prüfungsinhalte ab.", "en": "This section currently has no MCQ questions. The theory above covers the exam content."})}
</div>
""", unsafe_allow_html=True)
