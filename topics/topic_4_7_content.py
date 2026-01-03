# Topic 4.7: Normal Distribution - Normalverteilung
# ULTRATHINK ENHANCED VERSION
import streamlit as st
from views.styles import inject_equal_height_css
from utils.localization import t
from utils.quiz_helper import render_mcq
from data.exam_questions import get_question
import numpy as np
import plotly.graph_objects as go
from scipy.stats import norm

# ==========================================
# 1. CONTENT DICTIONARY - BILINGUAL (ULTRATHINK)
# ==========================================
content_4_7 = {
    "title": {"de": "4.7 Normalverteilung (stetig)", "en": "4.7 Normal Distribution (Continuous)"},
    "subtitle": {
        "de": "Die Königin der Verteilungen",
        "en": "The Queen of Distributions"
    },
    
    # --- INTUITION HOOK ---
    "intuition": {
        "header": {"de": "Die Intuition", "en": "The Intuition"},
        "text": {
            "de": "Körpergrössen, IQ-Werte, Messfehler, Aktienrenditen - all diese Phänomene entstehen durch **viele kleine, unabhängige Einflüsse**, die sich addieren. Genetik + Ernährung + Umwelt = Körpergrösse. Diese Summe vieler kleiner Zufälle erzeugt die berühmte **Glockenkurve**. Das ist der Zentrale Grenzwertsatz in Aktion!",
            "en": "Heights, IQ scores, measurement errors, stock returns - all these phenomena arise from **many small, independent influences** that add up. Genetics + nutrition + environment = height. This sum of many small random effects creates the famous **bell curve**. This is the Central Limit Theorem in action!"
        }
    },
    
    # --- FRAG DICH (Decision Guide) ---
    "frag_dich": {
        "header": {"de": "Frag dich: Ist es Normal?", "en": "Ask yourself: Is it Normal?"},
        "questions": [
            {"de": "Entsteht der Wert durch <strong>viele kleine Einflüsse</strong>?", "en": "Does the value arise from <strong>many small influences</strong>?"},
            {"de": "Ist die Variable <strong>stetig</strong> (kann jeden Wert annehmen)?", "en": "Is the variable <strong>continuous</strong> (can take any value)?"},
            {"de": "Ist die Verteilung <strong>symmetrisch</strong> um den Mittelwert?", "en": "Is the distribution <strong>symmetric</strong> around the mean?"},
            {"de": "Ist es eine <strong>Summe/Durchschnitt</strong> von Zufallsvariablen?", "en": "Is it a <strong>sum/average</strong> of random variables?"}
        ],
        "conclusion": {
            "de": "Mehrfach Ja → Normalverteilung wahrscheinlich!",
            "en": "Multiple Yes → Normal distribution likely!"
        }
    },
    
    # --- STANDARD NORMAL ---
    "standard": {
        "header": {"de": "Standardnormalverteilung", "en": "Standard Normal Distribution"},
        "text": {
            "de": "Die **Referenzverteilung** mit Zentrum bei 0 und Streuung von 1. Alle anderen Normalverteilungen können auf diese zurückgeführt werden!",
            "en": "The **reference distribution** centered at 0 with spread of 1. All other normal distributions can be reduced to this one!"
        },
        "notation": r"Z \sim N(0, 1)",
        "pdf": r"\phi(z) = \frac{1}{\sqrt{2\pi}} e^{-\frac{z^2}{2}}, \quad z \in \mathbb{R}",
        "moments": {
            "de": "E[Z] = 0 (zentriert) und V(Z) = 1 (standardisiert)",
            "en": "E[Z] = 0 (centered) and V(Z) = 1 (standardized)"
        }
    },
    
    # --- GENERAL NORMAL ---
    "general": {
        "header": {"de": "Allgemeine Normalverteilung", "en": "General Normal Distribution"},
        "text": {
            "de": "Die allgemeine Form, verschoben um μ und gestreckt/gestaucht um σ.",
            "en": "The general form, shifted by μ and stretched/compressed by σ."
        },
        "notation": r"X \sim N(\mu, \sigma^2)",
        "pdf": r"f_N(x; \mu, \sigma^2) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}"
    },
    
    # --- PARAMETERS WITH MEANING ---
    "parameters": {
        "header": {"de": "Die Parameter", "en": "The Parameters"},
        "mu": {
            "symbol": r"\mu \in \mathbb{R}",
            "name_de": "Lageparameter",
            "name_en": "Location Parameter",
            "meaning_de": "WO liegt das Zentrum der Glocke? Verschiebt die Kurve horizontal.",
            "meaning_en": "WHERE is the center of the bell? Shifts the curve horizontally."
        },
        "sigma": {
            "symbol": r"\sigma > 0",
            "name_de": "Streuungsparameter",
            "name_en": "Scale Parameter",
            "meaning_de": "WIE BREIT ist die Glocke? Kleines σ = steile, enge Glocke. Grosses σ = flache, breite Glocke.",
            "meaning_en": "HOW WIDE is the bell? Small σ = steep, narrow bell. Large σ = flat, wide bell."
        }
    },
    
    # --- MOMENTS WITH INTERPRETATION ---
    "moments": {
        "header": {"de": "Erwartungswert & Varianz", "en": "Expected Value & Variance"},
        "expectation": {
            "title_de": "Erwartungswert",
            "title_en": "Expected Value",
            "formula": r"E[X] = \mu",
            "interpretation_de": "Der Gipfel der Glockenkurve. 50% der Werte liegen links davon, 50% rechts.",
            "interpretation_en": "The peak of the bell curve. 50% of values lie to the left, 50% to the right."
        },
        "variance": {
            "title_de": "Varianz",
            "title_en": "Variance",
            "formula": r"V(X) = \sigma^2",
            "interpretation_de": "Je grösser $\\sigma^2$, desto 'unsicherer' der Ausgang - die Werte streuen stärker.",
            "interpretation_en": "The larger $\\sigma^2$, the more 'uncertain' the outcome - values spread more."
        }
    },
    
    # --- Z-TRANSFORMATION (Core Skill) ---
    "z_transform": {
        "header": {"de": "Die Z-Transformation (Prüfungs-Essential!)", "en": "The Z-Transformation (Exam Essential!)"},
        "why": {
            "de": "Problem: Es gibt unendlich viele Normalverteilungen, aber nur EINE Z-Tabelle. Lösung: Jede Normalverteilung auf die Standardnormalverteilung **zurückführen**.",
            "en": "Problem: There are infinitely many normal distributions, but only ONE Z-table. Solution: **Reduce** every normal distribution to the standard normal."
        },
        "formula": r"Z = \frac{X - \mu}{\sigma}",
        "meaning": {
            "de": "Interpretation: 'Wie viele Standardabweichungen ist X vom Mittelwert entfernt?'",
            "en": "Interpretation: 'How many standard deviations is X away from the mean?'"
        },
        "then": {
            "de": "Dann nachschlagen: Φ(z) = P(Z ≤ z) in der Tabelle.",
            "en": "Then look up: Φ(z) = P(Z ≤ z) in the table."
        }
    },
    
    # --- STEP-BY-STEP Z-CALCULATION ---
    "example_z": {
        "header": {"de": "Schritt-für-Schritt: Z-Transformation", "en": "Step-by-Step: Z-Transformation"},
        "problem": {
            "de": "Sei <strong>X ∼ N(100, 225)</strong> (also μ = 100, σ = 15). Berechne <strong>P(X ≤ 115)</strong>.",
            "en": "Let <strong>X ∼ N(100, 225)</strong> (so μ = 100, σ = 15). Calculate <strong>P(X ≤ 115)</strong>."
        },
        "steps": [
            {
                "label_de": "Schritt 1",
                "label_en": "Step 1",
                "action_de": "Standardisieren",
                "action_en": "Standardize",
                "content": r"Z = \frac{115 - 100}{15} = \frac{15}{15} = 1"
            },
            {
                "label_de": "Schritt 2",
                "label_en": "Step 2",
                "action_de": "Umformulieren",
                "action_en": "Reformulate",
                "content_de": "P(X ≤ 115) = P(Z ≤ 1)",
                "content_en": "P(X ≤ 115) = P(Z ≤ 1)"
            },
            {
                "label_de": "Schritt 3",
                "label_en": "Step 3",
                "action_de": "Tabelle",
                "action_en": "Table",
                "content_de": "Φ(1) = 0.8413 (aus Z-Tabelle)",
                "content_en": "Φ(1) = 0.8413 (from Z-table)"
            }
        ],
        "answer": {
            "de": "Es sind also **84.13%** der Werte kleiner oder gleich 115.",
            "en": "So **84.13%** of values are less than or equal to 115."
        }
    },
    
    # --- EMPIRICAL RULE (68-95-99.7) ---
    "empirical": {
        "header": {"de": "Die 68-95-99.7 Regel (Merken!)", "en": "The 68-95-99.7 Rule (Memorize!)"},
        "text": {
            "de": "Ohne Tabelle abschätzen - diese Zahlen solltest du im Schlaf kennen:",
            "en": "Estimate without a table - know these numbers by heart:"
        },
        "rules": [
            {
                "range": "μ ± 1σ",
                "percent": "68%",
                "meaning_de": "Etwa 2/3 aller Werte",
                "meaning_en": "About 2/3 of all values"
            },
            {
                "range": "μ ± 2σ",
                "percent": "95%",
                "meaning_de": "Fast alle Werte",
                "meaning_en": "Almost all values"
            },
            {
                "range": "μ ± 3σ",
                "percent": "99.7%",
                "meaning_de": "Praktisch alle Werte",
                "meaning_en": "Practically all values"
            }
        ]
    },
    
    # --- SYMMETRY TRICKS ---
    "symmetry": {
        "header": {"de": "Symmetrie-Tricks für die Prüfung", "en": "Symmetry Tricks for Exams"},
        "rules": [
            {
                "formula": r"\Phi(-z) = 1 - \Phi(z)",
                "meaning_de": "Negative Z-Werte über Symmetrie berechnen",
                "meaning_en": "Calculate negative Z-values via symmetry"
            },
            {
                "formula": r"P(Z > z) = 1 - \Phi(z)",
                "meaning_de": "Obere Wahrscheinlichkeit = 1 minus untere",
                "meaning_en": "Upper probability = 1 minus lower"
            },
            {
                "formula": r"P(a < Z < b) = \Phi(b) - \Phi(a)",
                "meaning_de": "Intervall = Differenz der Verteilungsfunktionen",
                "meaning_en": "Interval = Difference of distribution functions"
            }
        ]
    },
    
    # --- KEY PROPERTY: REPRODUCTIVE ---
    "reproductive": {
        "header": {"de": "Reproduktive Eigenschaft", "en": "Reproductive Property"},
        "text": {
            "de": "Die Summe unabhängiger normalverteilter Zufallsvariablen ist wieder normalverteilt! Das ist bei den meisten anderen Verteilungen NICHT der Fall.",
            "en": "The sum of independent normally distributed random variables is again normally distributed! This is NOT the case for most other distributions."
        },
        "formula": r"\text{Wenn } X_i \sim N(\mu_i, \sigma_i^2) \text{ unabhängig: } \sum X_i \sim N\left(\sum \mu_i, \sum \sigma_i^2\right)"
    },
    
    # --- EXAM ESSENTIALS (Merged Trap + Pro Tip) ---
    "exam_essentials": {
        "header": {"de": "Prüfungs-Essentials", "en": "Exam Essentials"},
        "items": [
            {
                "label": {"de": "Falle", "en": "Trap"},
                "title": {"de": "N(μ, σ²) vs N(μ, σ)", "en": "N(μ, σ²) vs N(μ, σ)"},
                "content": {
                    "de": "Notation variiert! Prüfe IMMER ob der Parameter σ oder σ² ist.<br><em>Beispiel:</em> N(100, 225) bedeutet σ² = 225, also <strong>σ = 15</strong>",
                    "en": "Notation varies! ALWAYS check if the parameter is σ or σ².<br><em>Example:</em> N(100, 225) means σ² = 225, so <strong>σ = 15</strong>"
                },
                "type": "warning"
            },
            {
                "label": {"de": "Formel", "en": "Formula"},
                "title": {"de": "Z = (X - μ)/σ immer standardisieren", "en": "Always standardize Z = (X - μ)/σ"},
                "content": {
                    "de": "Die Z-Tabelle gilt nur für N(0,1)! Jede Normalverteilung muss erst umgerechnet werden.",
                    "en": "Z-table only works for N(0,1)! Every normal distribution must first be converted."
                },
                "type": "tip"
            },
            {
                "label": {"de": "Symmetrie", "en": "Symmetry"},
                "title": {"de": "Φ(-z) = 1 - Φ(z)", "en": "Φ(-z) = 1 - Φ(z)"},
                "content": {
                    "de": "Die Tabelle zeigt oft nur positive z-Werte. Für negative z: nutze die Symmetrie.",
                    "en": "Table often shows only positive z-values. For negative z: use symmetry."
                },
                "type": "tip"
            },
            {
                "label": {"de": "Merken", "en": "Memorize"},
                "title": {"de": "Φ(1.96) ≈ 0.975 für 95%-CI", "en": "Φ(1.96) ≈ 0.975 for 95% CI"},
                "content": {
                    "de": "DER wichtigste z-Wert! 2.5% in jedem Schwanz → 95% in der Mitte.",
                    "en": "THE most important z-value! 2.5% in each tail → 95% in the middle."
                },
                "type": "tip"
            }
        ]
    }
}


def render_subtopic_4_7(model):
    """4.7 Normalverteilung - ULTRATHINK Enhanced"""
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
    st.header(t(content_4_7["title"]))
    st.caption(t(content_4_7["subtitle"]))
    st.markdown("---")
    
    # --- INTUITION HOOK ---
    st.markdown(f"### {t(content_4_7['intuition']['header'])}")
    with st.container(border=True):
        st.markdown(t(content_4_7["intuition"]["text"]))
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- FRAG DICH: DECISION GUIDE ---
    from utils.ask_yourself import render_ask_yourself
    render_ask_yourself(
        header=content_4_7['frag_dich']['header'],
        questions=content_4_7['frag_dich']['questions'],
        conclusion=content_4_7['frag_dich']['conclusion']
    )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- STANDARD vs GENERAL (Two Columns) ---
    col_std, col_gen = st.columns(2, gap="medium")
    
    with col_std:
        with st.container(border=True):
            st.markdown(f"### {t(content_4_7['standard']['header'])}")
            st.markdown(t(content_4_7["standard"]["text"]))
            st.latex(content_4_7["standard"]["notation"])
            st.markdown("<br>", unsafe_allow_html=True)
            st.caption(t({"de": "Dichtefunktion:", "en": "Density function:"}))
            st.latex(content_4_7["standard"]["pdf"])
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown(t(content_4_7["standard"]["moments"]))
    
    with col_gen:
        with st.container(border=True):
            st.markdown(f"### {t(content_4_7['general']['header'])}")
            st.markdown(t(content_4_7["general"]["text"]))
            st.latex(content_4_7["general"]["notation"])
            st.markdown("<br>", unsafe_allow_html=True)
            st.caption(t({"de": "Dichtefunktion:", "en": "Density function:"}))
            st.latex(content_4_7["general"]["pdf"])
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- PARAMETERS WITH MEANING ---
    st.markdown(f"### {t(content_4_7['parameters']['header'])}")
    
    col_mu, col_sigma = st.columns(2, gap="medium")
    
    with col_mu:
        with st.container(border=True):
            st.latex(content_4_7["parameters"]["mu"]["symbol"])
            st.markdown(f"**{t({'de': content_4_7['parameters']['mu']['name_de'], 'en': content_4_7['parameters']['mu']['name_en']})}**")
            st.markdown(t({"de": content_4_7["parameters"]["mu"]["meaning_de"], "en": content_4_7["parameters"]["mu"]["meaning_en"]}))
    
    with col_sigma:
        with st.container(border=True):
            st.latex(content_4_7["parameters"]["sigma"]["symbol"])
            st.markdown(f"**{t({'de': content_4_7['parameters']['sigma']['name_de'], 'en': content_4_7['parameters']['sigma']['name_en']})}**")
            st.markdown(t({"de": content_4_7["parameters"]["sigma"]["meaning_de"], "en": content_4_7["parameters"]["sigma"]["meaning_en"]}))
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- MOMENTS WITH INTERPRETATION ---
    st.markdown(f"### {t(content_4_7['moments']['header'])}")
    
    col_e, col_v = st.columns(2, gap="medium")
    
    with col_e:
        with st.container(border=True):
            st.markdown(f"**{t({'de': content_4_7['moments']['expectation']['title_de'], 'en': content_4_7['moments']['expectation']['title_en']})}**")
            st.latex(content_4_7["moments"]["expectation"]["formula"])
            st.markdown("---")
            st.markdown(t({"de": content_4_7["moments"]["expectation"]["interpretation_de"], "en": content_4_7["moments"]["expectation"]["interpretation_en"]}))
    
    with col_v:
        with st.container(border=True):
            st.markdown(f"**{t({'de': content_4_7['moments']['variance']['title_de'], 'en': content_4_7['moments']['variance']['title_en']})}**")
            st.latex(content_4_7["moments"]["variance"]["formula"])
            st.markdown("---")
            st.markdown(t({"de": content_4_7["moments"]["variance"]["interpretation_de"], "en": content_4_7["moments"]["variance"]["interpretation_en"]}))
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- Z-TRANSFORMATION (Prüfungs-Essential!) ---
    st.markdown(f"### {t(content_4_7['z_transform']['header'])}")
    with st.container(border=True):
        st.markdown(t(content_4_7["z_transform"]["why"]))
        st.markdown("<br>", unsafe_allow_html=True)
        
        col_formula, col_meaning = st.columns([1, 2])
        with col_formula:
            st.latex(content_4_7["z_transform"]["formula"])
        with col_meaning:
            st.info(t(content_4_7["z_transform"]["meaning"]))
        
        st.markdown(t(content_4_7["z_transform"]["then"]))
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- STEP-BY-STEP EXAMPLE ---
    st.markdown(f"### {t(content_4_7['example_z']['header'])}")
    with st.container(border=True):
        
        st.markdown(f"""
        <div style="background:#fafafa; border-radius:8px; padding:12px; margin-bottom:16px;">
            {t(content_4_7['example_z']['problem'])}
        </div>
        """, unsafe_allow_html=True)
        
        for i, step in enumerate(content_4_7["example_z"]["steps"]):
            if i > 0:
                st.markdown("---")
            label = t({"de": step["label_de"], "en": step["label_en"]})
            action = t({"de": step["action_de"], "en": step["action_en"]})
            
            col_step, col_content = st.columns([1, 3])
            with col_step:
                st.markdown(f"""
                <div style="background:#18181b; color:white; padding:8px 16px; border-radius:9999px; text-align:center; display:inline-block;">
                    <strong>{label}</strong> · <small>{action}</small>
                </div>
                """, unsafe_allow_html=True)
            with col_content:
                if "content" in step:
                    st.latex(step["content"])
                else:
                    st.markdown(t({"de": step["content_de"], "en": step["content_en"]}))
        
        st.markdown("---")
        st.markdown(f"**{t(content_4_7['example_z']['answer'])}**")
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- INTERACTIVE MISSION: Z-SCORE DISCOVERY ---
    st.markdown(f"### {t({'de': 'Mission: Der Z-Score Durchbruch', 'en': 'Mission: The Z-Score Breakthrough'})}")
    
    # Mission state initialization
    if "zscore_mission_done" not in st.session_state:
        st.session_state.zscore_mission_done = False
    
    with st.container(border=True):
        # REAL-WORLD SCENARIO
        st.markdown(f"""
<div style="background: rgba(0, 122, 255, 0.08); padding:14px; border-radius:8px; color:#1c1c1e; margin-bottom:12px; border-left: 4px solid #007AFF;">
<strong>{t({'de': 'Szenario:', 'en': 'Scenario:'})}</strong> {t({'de': 'Ein Unternehmen möchte Bonuszahlungen an die Top 5% der Verkäufer vergeben. Sie müssen wissen: Welcher Verkaufswert (X) markiert die Grenze zum „Elite-Status"?', 'en': 'A company wants to award bonuses to the top 5% of salespeople. They need to know: What sales value (X) marks the threshold for "Elite Status"?'})}
</div>""", unsafe_allow_html=True)
        
        # THE MISSION GOAL
        target_prob = 0.95
        tolerance = 0.005
        st.markdown(f"""
<div style="background:#f4f4f5; padding:16px; border-radius:8px; color:#3f3f46; border-left: 4px solid #a1a1aa;">
<strong>{t({'de': 'Deine Aufgabe:', 'en': 'Your Mission:'})}</strong> {t({'de': f'Finde den X-Wert, bei dem P(X ≤ x) = {target_prob*100:.0f}% ist! (Hinweis: Welcher Z-Wert gehört zu 95%?)', 'en': f'Find the X value where P(X ≤ x) = {target_prob*100:.0f}%! (Hint: What Z-score corresponds to 95%?)'})}
</div>""", unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        col_ctrl, col_chart = st.columns([1.2, 2.3], gap="large")
        
        with col_ctrl:
            mu = st.slider("μ", min_value=50.0, max_value=150.0, value=100.0, step=5.0, key="norm_mu")
            sigma = st.slider("σ", min_value=5.0, max_value=30.0, value=15.0, step=1.0, key="norm_sigma")
            x_val = st.slider("X", min_value=mu - 3*sigma, max_value=mu + 3*sigma, value=mu, step=1.0, key="norm_x")
            
            st.markdown("<br>", unsafe_allow_html=True)
            z_score = (x_val - mu) / sigma
            prob = norm.cdf(z_score)
            goal_reached = abs(prob - target_prob) < tolerance
            
            # Semantic colored formula display
            z_color = "#007AFF"
            prob_color = "#34C759" if goal_reached else "#FF4B4B"
            
            st.markdown(f"""
<div style="font-size: 1.0em;">
<strong>Z</strong> = (<span style="color:#FF4B4B;">X</span> - <span style="color:#34C759;">μ</span>) / σ = ({x_val:.0f} - {mu:.0f}) / {sigma:.0f} = <span style="color:{z_color}; font-weight:bold;">{z_score:.2f}</span>
</div>""", unsafe_allow_html=True)
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            st.markdown(f"""
<div style="font-size: 1.1em;">
P(X ≤ {x_val:.0f}) = Φ({z_score:.2f}) = <span style="color:{prob_color}; font-weight:bold;">{prob:.1%}</span>
</div>""", unsafe_allow_html=True)
            
            # Progress feedback
            st.markdown("<br>", unsafe_allow_html=True)
            if prob < 0.80:
                st.info(t({"de": "X ist noch zu klein. Schiebe X nach rechts!", "en": "X is still too small. Push X to the right!"}))
            elif prob < target_prob - tolerance:
                st.warning(t({"de": f"Fast da! P = {prob:.1%} — noch etwas höher mit X!", "en": f"Almost there! P = {prob:.1%} — push X a bit higher!"}))
            elif prob > target_prob + tolerance:
                st.warning(t({"de": f"Zu weit! P = {prob:.1%} — X etwas zurück nehmen.", "en": f"Too far! P = {prob:.1%} — pull X back a bit."}))
            else:
                if not st.session_state.zscore_mission_done:
                    st.balloons()
                    st.session_state.zscore_mission_done = True
                    from utils.progress_tracker import track_question_answer
                    if user := st.session_state.get("user"):
                        track_question_answer(user["localId"], "vwl", "4", "4.7", "zscore_mission", True)
                
                st.success(t({"de": f"Mission erfüllt! Bei X = {x_val:.0f} ist Z ≈ 1.645 und P ≈ 95%", "en": f"Mission Complete! At X = {x_val:.0f}, Z ≈ 1.645 and P ≈ 95%"}))
        
        with col_chart:
            x_range = np.linspace(mu - 4*sigma, mu + 4*sigma, 400)
            y_pdf = norm.pdf(x_range, mu, sigma)
            
            fig = go.Figure()
            
            # Shaded area - color based on goal
            fill_color = 'rgba(52, 199, 89, 0.3)' if goal_reached else 'rgba(0, 122, 255, 0.3)'
            x_fill = x_range[x_range <= x_val]
            y_fill = norm.pdf(x_fill, mu, sigma)
            fig.add_trace(go.Scatter(
                x=np.concatenate([x_fill, x_fill[::-1]]),
                y=np.concatenate([y_fill, np.zeros_like(y_fill)]),
                fill='toself', fillcolor=fill_color,
                line=dict(width=0), showlegend=False,
                hoverinfo='skip'
            ))
            
            # Bell curve
            fig.add_trace(go.Scatter(
                x=x_range, y=y_pdf,
                mode='lines', line=dict(color='#007AFF', width=2),
                showlegend=False,
                hovertemplate='x=%{x:.1f}<extra></extra>'
            ))
            
            # Vertical line at X (red = selection)
            fig.add_vline(x=x_val, line_dash="solid", line_color="#FF4B4B", line_width=2,
                         annotation_text=f"X={x_val:.0f}", annotation_position="top")
            
            # Mean line (green = reference)
            fig.add_vline(x=mu, line_dash="dash", line_color="#34C759", line_width=1,
                         annotation_text="μ", annotation_position="top")
            
            fig.update_layout(
                xaxis=dict(title="X", fixedrange=True, showgrid=False),
                yaxis=dict(title="f(x)", fixedrange=True, showgrid=True, gridcolor='#E5E5EA'),
                height=300,
                margin=dict(l=40, r=20, t=30, b=50),
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
            )
            
            st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
        
        # Mastery insight (shown after completion)
        if goal_reached:
            st.markdown(f"""
<div style="background:#f4f4f5; padding:16px; border-radius:8px; color:#3f3f46; margin-top:12px; border-left: 4px solid #a1a1aa;">
<strong>{t({'de': 'Was du entdeckt hast:', 'en': 'What you discovered:'})}</strong> {t({'de': 'Der Z-Wert ≈ 1.645 ist der magische Schwellenwert für 95%. Egal welche μ und σ — X = μ + 1.645σ gibt immer 95%!', 'en': 'The Z-value ≈ 1.645 is the magic threshold for 95%. No matter what μ and σ — X = μ + 1.645σ always gives 95%!'})}
</div>""", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- 68-95-99.7 RULE ---
    rules_html = "".join([f'''<tr>
<td style="padding:8px; font-family:monospace; font-weight:bold;">{r['range']}</td>
<td style="padding:8px; text-align:center; font-weight:bold; color:#3f3f46;">{r['percent']}</td>
<td style="padding:8px;">{t({'de': r['meaning_de'], 'en': r['meaning_en']})}</td>
</tr>''' for r in content_4_7['empirical']['rules']])
    
    st.markdown(f"""<div style="background-color: #f4f4f5; border-radius: 12px; padding: 20px; border: 2px solid #a1a1aa;">
<div style="font-weight: 700; color: #3f3f46; margin-bottom: 12px; font-size: 1.1em;">
{t(content_4_7['empirical']['header'])}
</div>
<div style="color: #3f3f46; margin-bottom: 12px;">
{t(content_4_7['empirical']['text'])}
</div>
<table style="width:100%; border-collapse: collapse;">
<tr style="background:#e4e4e7;">
<th style="padding:8px; text-align:left; border-bottom:1px solid #a1a1aa;">Bereich/Range</th>
<th style="padding:8px; text-align:center; border-bottom:1px solid #a1a1aa;">%</th>
<th style="padding:8px; text-align:left; border-bottom:1px solid #a1a1aa;">Bedeutung/Meaning</th>
</tr>
{rules_html}
</table>
</div>""", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- SYMMETRY TRICKS ---
    st.markdown(f"### {t(content_4_7['symmetry']['header'])}")
    with st.container(border=True):
        
        for rule in content_4_7["symmetry"]["rules"]:
            col_f, col_m = st.columns([1, 2])
            with col_f:
                st.latex(rule["formula"])
            with col_m:
                st.caption(t({"de": rule["meaning_de"], "en": rule["meaning_en"]}))
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- REPRODUCTIVE PROPERTY ---
    st.markdown(f"### {t(content_4_7['reproductive']['header'])}")
    with st.container(border=True):
        st.markdown(t(content_4_7["reproductive"]["text"]))
        st.latex(content_4_7["reproductive"]["formula"])
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- EXAM ESSENTIALS (Using Utility) ---
    from utils.exam_essentials import render_exam_essentials
    render_exam_essentials(items=content_4_7["exam_essentials"]["items"])
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- EXAM SECTION ---
    st.markdown(f"### {t({'de': 'Prüfungstraining', 'en': 'Exam Practice'})}")
    
    q_data = get_question("4.7", "normal_std")
    if q_data:
        with st.container(border=True):
            st.caption(q_data.get("source", ""))
            opts = q_data.get("options", [])
            if opts and isinstance(opts[0], dict):
                option_labels = [t(o) for o in opts]
            else:
                option_labels = opts
            
            render_mcq(
                key_suffix="4_7_normal",
                question_text=t(q_data["question"]),
                options=option_labels,
                correct_idx=q_data["correct_idx"],
                solution_text_dict=q_data["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
                client=model,
                ai_context="Normal distribution",
                course_id="vwl",
                topic_id="4",
                subtopic_id="4.7",
                question_id="4_7_normal"
            )
    else:
        with st.container(border=True):
            st.info(t({
                "de": "Für diesen Abschnitt gibt es derzeit keine MCQ-Fragen. Die Theorie oben deckt die Prüfungsinhalte ab.",
                "en": "This section currently has no MCQ questions. The theory above covers the exam content."
            }))
