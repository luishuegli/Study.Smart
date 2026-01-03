# Topic 4.5: Rectangular Distribution - Rechteckverteilung (stetig)
# ULTRATHINK ENHANCED VERSION - "Stupid Person Check" Compliant
import streamlit as st
from views.styles import inject_equal_height_css
from utils.localization import t
from utils.quiz_helper import render_mcq
from data.exam_questions import get_question

# ==========================================
# 1. CONTENT DICTIONARY - BILINGUAL (ULTRATHINK)
# ==========================================
content_4_5 = {
    "title": {"de": "4.5 Rechteckverteilung (stetig)", "en": "4.5 Rectangular Distribution (Continuous)"},
    "subtitle": {"de": "Die stetige Version der Gleichverteilung", "en": "The Continuous Uniform Distribution"},
    
    # --- INTUITION HOOK ---
    "intuition": {
        "header": {"de": "Die Intuition", "en": "The Intuition"},
        "text": {
            "de": "Du stehst an der <strong>Bushaltestelle</strong>. Der Bus kommt alle 10 Minuten, aber du weisst nicht, wann der letzte Bus kam. Deine Wartezeit ist <strong>gleichmässig verteilt</strong> zwischen 0 und 10 Minuten — jede Wartezeit ist gleich wahrscheinlich!",
            "en": "You're at the <strong>bus stop</strong>. The bus comes every 10 minutes, but you don't know when the last one came. Your waiting time is <strong>uniformly distributed</strong> between 0 and 10 minutes — every waiting time is equally likely!"
        },
        "why_rectangular": {
            "de": "Warum 'Rechteck'? Wenn du die Dichtefunktion zeichnest, ist sie ein <strong>flaches Rechteck</strong> — überall gleich hoch zwischen a und b, und 0 ausserhalb.",
            "en": "Why 'Rectangular'? When you draw the density function, it's a <strong>flat rectangle</strong> — equally high everywhere between a and b, and 0 outside."
        }
    },
    
    # --- FRAG DICH (Decision Guide) ---
    "frag_dich": {
        "header": {"de": "Frag dich: Ist es Rechteckverteilt?", "en": "Ask yourself: Is it Rectangular?"},
        "questions": [
            {"de": "Ist die Variable <strong>stetig</strong> (kann jeden Wert annehmen)?", "en": "Is the variable <strong>continuous</strong> (can take any value)?"},
            {"de": "Ist jeder Wert im Intervall <strong>gleich wahrscheinlich</strong>?", "en": "Is every value in the interval <strong>equally likely</strong>?"},
            {"de": "Gibt es klare <strong>Grenzen</strong> a (Minimum) und b (Maximum)?", "en": "Are there clear <strong>boundaries</strong> a (minimum) and b (maximum)?"},
            {"de": "Weisst du <strong>nichts</strong> über den genauen Wert ausser den Grenzen?", "en": "Do you know <strong>nothing</strong> about the exact value except the boundaries?"}
        ],
        "conclusion": {"de": "Alles Ja → Rechteckverteilung!", "en": "All Yes → Rectangular Distribution!"}
    },
    
    # --- DEFINITION ---
    "definition": {
        "header": {"de": "Definition", "en": "Definition"},
        "text": {
            "de": "Eine <strong>stetige</strong> Zufallsvariable X heisst rechteckverteilt (oder stetig gleichverteilt), wenn sie jeden Wert im Intervall [a, b] mit <strong>gleicher Dichte</strong> annimmt.",
            "en": "A <strong>continuous</strong> random variable X is called rectangular distributed (or continuously uniform) if it takes every value in the interval [a, b] with <strong>equal density</strong>."
        },
        "notation": r"X \sim R(a, b) \quad \text{oder} \quad X \sim \text{Uniform}(a, b)"
    },
    
    # --- PARAMETERS WITH MEANING ---
    "parameters": {
        "header": {"de": "Die Parameter", "en": "The Parameters"},
        "a": {
            "symbol": "a",
            "name_de": "Untere Grenze",
            "name_en": "Lower Bound",
            "meaning_de": "Der <strong>kleinste mögliche Wert</strong>. Beim Busbeispiel: a = 0 (sofort da).",
            "meaning_en": "The <strong>smallest possible value</strong>. In the bus example: a = 0 (arrives immediately)."
        },
        "b": {
            "symbol": "b",
            "name_de": "Obere Grenze", 
            "name_en": "Upper Bound",
            "meaning_de": "Der <strong>grösste mögliche Wert</strong>. Beim Busbeispiel: b = 10 (maximale Wartezeit).",
            "meaning_en": "The <strong>largest possible value</strong>. In the bus example: b = 10 (maximum waiting time)."
        }
    },
    
    # --- FORMULAS WITH DERIVATION ---
    "formula": {
        "pdf": {
            "header": {"de": "Dichtefunktion (PDF)", "en": "Density Function (PDF)"},
            "formula": r"f_R(x) = \begin{cases} \frac{1}{b-a} & \text{für } a \leq x \leq b \\ 0 & \text{sonst} \end{cases}",
            "intuition_de": "Die Höhe des Rechtecks ist 1/(b-a). <strong>Warum?</strong> Weil die Fläche unter der Kurve = 1 sein muss: Höhe × Breite = (1/(b-a)) × (b-a) = 1 ✓",
            "intuition_en": "The height of the rectangle is 1/(b-a). <strong>Why?</strong> Because the area under the curve must = 1: Height × Width = (1/(b-a)) × (b-a) = 1 ✓"
        },
        "cdf": {
            "header": {"de": "Verteilungsfunktion (CDF)", "en": "Distribution Function (CDF)"},
            "formula": r"F_R(x) = \frac{x-a}{b-a} \quad \text{für } a \leq x \leq b",
            "intuition_de": "Wie viel vom Intervall liegt <strong>links</strong> von x? Es ist einfach der Bruchteil: (x-a)/(b-a).",
            "intuition_en": "How much of the interval lies <strong>to the left</strong> of x? It's simply the fraction: (x-a)/(b-a)."
        }
    },
    
    # --- KEY FORMULA: INTERVAL PROBABILITY ---
    "interval": {
        "header": {"de": "Intervallwahrscheinlichkeit (Prüfungs-Essential!)", "en": "Interval Probability (Exam Essential!)"},
        "formula": r"P(c \leq X \leq d) = \frac{d-c}{b-a}",
        "derivation": r"P(c \leq X \leq d) = F(d) - F(c) = \frac{d-a}{b-a} - \frac{c-a}{b-a} = \frac{d-c}{b-a}",
        "intuition_de": "Die Wahrscheinlichkeit ist einfach das <strong>Längenverhältnis</strong>: Wie gross ist das Teilintervall [c,d] im Vergleich zum Gesamtintervall [a,b]?",
        "intuition_en": "The probability is simply the <strong>length ratio</strong>: How large is the subinterval [c,d] compared to the total interval [a,b]?"
    },
    
    # --- MOMENTS WITH INTERPRETATION ---
    "moments": {
        "header": {"de": "Erwartungswert & Varianz", "en": "Expected Value & Variance"},
        "expectation": {
            "title_de": "Erwartungswert",
            "title_en": "Expected Value",
            "formula": r"E[X] = \frac{a + b}{2}",
            "interpretation_de": "Der <strong>Mittelpunkt</strong> des Intervalls. Logisch: bei gleicher Dichte ist der Durchschnitt genau in der Mitte!",
            "interpretation_en": "The <strong>midpoint</strong> of the interval. Logical: with equal density, the average is exactly in the middle!"
        },
        "variance": {
            "title_de": "Varianz",
            "title_en": "Variance",
            "formula": r"V(X) = \frac{(b-a)^2}{12}",
            "interpretation_de": "Je <strong>breiter</strong> das Intervall (grösseres b-a), desto grösser die Varianz. Die 12 im Nenner ist eine Konstante aus der Herleitung.",
            "interpretation_en": "The <strong>wider</strong> the interval (larger b-a), the larger the variance. The 12 in the denominator is a constant from the derivation."
        }
    },
    
    # --- WORKED EXAMPLE ---
    "example_worked": {
        "header": {"de": "Schritt-für-Schritt Beispiel", "en": "Step-by-Step Example"},
        "problem": {
            "de": "Der Bus kommt alle <strong>10 Minuten</strong>. Du kommst zufällig an die Haltestelle. (a) Wie lange wartest du <strong>im Durchschnitt</strong>? (b) Wie wahrscheinlich wartest du <strong>weniger als 3 Minuten</strong>?",
            "en": "The bus comes every <strong>10 minutes</strong>. You arrive randomly at the stop. (a) How long do you wait <strong>on average</strong>? (b) What's the probability you wait <strong>less than 3 minutes</strong>?"
        },
        "steps": [
            {
                "label": {"de": "Modell", "en": "Model"},
                "latex": r"X \sim R({\color{#007AFF}0}, {\color{#007AFF}10}), \quad {\color{#007AFF}a = 0}, \quad {\color{#007AFF}b = 10}",
                "note": {"de": "X = Wartezeit in Minuten", "en": "X = Wait time in minutes"}
            },
            {
                "label": {"de": "(a) E[X]", "en": "(a) E[X]"},
                "latex": r"E[X] = \frac{{\color{#007AFF}a} + {\color{#007AFF}b}}{2} = \frac{{\color{#007AFF}0} + {\color{#007AFF}10}}{2} = \mathbf{5 \text{ Min}}",
                "note": None
            },
            {
                "label": {"de": "(b) P(X < 3)", "en": "(b) P(X < 3)"},
                "latex": r"P(X < {\color{#FF4B4B}3}) = \frac{{\color{#FF4B4B}3} - {\color{#007AFF}0}}{{\color{#007AFF}10} - {\color{#007AFF}0}} = \frac{{\color{#FF4B4B}3}}{{\color{#007AFF}10}} = \mathbf{30\%}",
                "note": None
            }
        ],
        "check": {
            "de": "<strong>Plausibilitäts-Check:</strong> 30% macht Sinn — 3 von 10 Minuten sind 30% des Intervalls!",
            "en": "<strong>Plausibility check:</strong> 30% makes sense — 3 out of 10 minutes is 30% of the interval!"
        }
    },
    
    # --- EXAM ESSENTIALS (Merged Trap + Pro Tip) ---
    "exam_essentials": {
        "header": {"de": "Prüfungs-Essentials", "en": "Exam Essentials"},
        "items": [
            {
                "label": {"de": "Falle", "en": "Trap"},
                "title": {"de": "Dichte ≠ Wahrscheinlichkeit!", "en": "Density ≠ Probability!"},
                "formula": r"P(X = 5) = 0 \neq \frac{1}{10}",
                "content": {
                    "de": "Du brauchst immer ein <strong>Intervall</strong>.",
                    "en": "You always need an <strong>interval</strong>."
                },
                "note": {"de": "Merke: P(X = exakter Wert) = 0", "en": "Remember: P(X = exact value) = 0"},
                "type": "warning"
            },
            {
                "label": {"de": "Formel", "en": "Formula"},
                "title_formula": r"E[X] = \frac{a+b}{2}",
                "content": {
                    "de": "Der Erwartungswert ist der <strong>Mittelpunkt</strong> des Intervalls [a, b].",
                    "en": "The expected value is the <strong>midpoint</strong> of interval [a, b]."
                },
                "type": "tip"
            },
            {
                "label": {"de": "Shortcut", "en": "Shortcut"},
                "title_formula": r"P(c \leq X \leq d) = \frac{d-c}{b-a}",
                "content": {
                    "de": "Einfach das <strong>Längenverhältnis</strong>! Intervall-Länge geteilt durch Gesamtlänge.",
                    "en": "Just the <strong>length ratio</strong>! Interval length divided by total length."
                },
                "type": "tip"
            }
        ]
    }
}


def render_subtopic_4_5(model):
    """4.5 Rechteckverteilung - ULTRATHINK Enhanced with Stupid Person Check"""
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
    st.header(t(content_4_5["title"]))
    st.caption(t(content_4_5["subtitle"]))
    st.markdown("---")
    
    # --- INTUITION HOOK ---
    st.markdown(f"### {t(content_4_5['intuition']['header'])}")
    with st.container(border=True):
        st.markdown(t(content_4_5["intuition"]["text"]), unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        why_rect = t(content_4_5["intuition"]["why_rectangular"])
        st.markdown(f"""
<div style="background: #f4f4f5; border-left: 4px solid #a1a1aa; padding: 12px 16px; border-radius: 8px; color: #3f3f46;">
{why_rect}
</div>
""", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- FRAG DICH: DECISION GUIDE ---
    from utils.ask_yourself import render_ask_yourself
    render_ask_yourself(
        header=content_4_5['frag_dich']['header'],
        questions=content_4_5['frag_dich']['questions'],
        conclusion=content_4_5['frag_dich']['conclusion']
    )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- DEFINITION ---
    st.markdown(f"### {t(content_4_5['definition']['header'])}")
    with st.container(border=True):
        st.markdown(t(content_4_5["definition"]["text"]), unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        st.latex(content_4_5["definition"]["notation"])
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- PARAMETERS ---
    st.markdown(f"### {t(content_4_5['parameters']['header'])}")
    
    col_a, col_b = st.columns(2, gap="medium")
    
    with col_a:
        with st.container(border=True):
            st.markdown(f"**{content_4_5['parameters']['a']['symbol']}** — {t({'de': content_4_5['parameters']['a']['name_de'], 'en': content_4_5['parameters']['a']['name_en']})}")
            st.markdown(t({"de": content_4_5["parameters"]["a"]["meaning_de"], "en": content_4_5["parameters"]["a"]["meaning_en"]}), unsafe_allow_html=True)
    
    with col_b:
        with st.container(border=True):
            st.markdown(f"**{content_4_5['parameters']['b']['symbol']}** — {t({'de': content_4_5['parameters']['b']['name_de'], 'en': content_4_5['parameters']['b']['name_en']})}")
            st.markdown(t({"de": content_4_5["parameters"]["b"]["meaning_de"], "en": content_4_5["parameters"]["b"]["meaning_en"]}), unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- PDF & CDF ---
    col_pdf, col_cdf = st.columns(2, gap="medium")
    
    with col_pdf:
        with st.container(border=True):
            st.markdown(f"**{t(content_4_5['formula']['pdf']['header'])}**")
            st.latex(content_4_5["formula"]["pdf"]["formula"])
            st.markdown(t({"de": content_4_5["formula"]["pdf"]["intuition_de"], "en": content_4_5["formula"]["pdf"]["intuition_en"]}), unsafe_allow_html=True)
    
    with col_cdf:
        with st.container(border=True):
            st.markdown(f"**{t(content_4_5['formula']['cdf']['header'])}**")
            st.latex(content_4_5["formula"]["cdf"]["formula"])
            st.markdown(t({"de": content_4_5["formula"]["cdf"]["intuition_de"], "en": content_4_5["formula"]["cdf"]["intuition_en"]}), unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- KEY FORMULA: INTERVAL PROBABILITY ---
    st.markdown(f"### {t(content_4_5['interval']['header'])}")
    with st.container(border=True):
        st.latex(content_4_5["interval"]["formula"])
        st.caption(t({"de": "Herleitung:", "en": "Derivation:"}))
        st.latex(content_4_5["interval"]["derivation"])
        intuition_text = t({"de": content_4_5["interval"]["intuition_de"], "en": content_4_5["interval"]["intuition_en"]})
        st.markdown(f"""
<div style="background-color: rgba(0, 122, 255, 0.08); border-radius: 8px; padding: 12px; border-left: 4px solid #007AFF; color: #1c1c1e;">
{intuition_text}
</div>""", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- MOMENTS ---
    st.markdown(f"### {t(content_4_5['moments']['header'])}")
    
    col_e, col_v = st.columns(2, gap="medium")
    
    with col_e:
        with st.container(border=True):
            st.markdown(f"**{t({'de': content_4_5['moments']['expectation']['title_de'], 'en': content_4_5['moments']['expectation']['title_en']})}**")
            st.latex(content_4_5["moments"]["expectation"]["formula"])
            st.markdown("---")
            st.markdown(t({"de": content_4_5["moments"]["expectation"]["interpretation_de"], "en": content_4_5["moments"]["expectation"]["interpretation_en"]}), unsafe_allow_html=True)
    
    with col_v:
        with st.container(border=True):
            st.markdown(f"**{t({'de': content_4_5['moments']['variance']['title_de'], 'en': content_4_5['moments']['variance']['title_en']})}**")
            st.latex(content_4_5["moments"]["variance"]["formula"])
            st.markdown("---")
            st.markdown(t({"de": content_4_5["moments"]["variance"]["interpretation_de"], "en": content_4_5["moments"]["variance"]["interpretation_en"]}), unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- WORKED EXAMPLE ---
    st.markdown(f"### {t(content_4_5['example_worked']['header'])}")
    with st.container(border=True):
        
        st.markdown(t(content_4_5['example_worked']['problem']), unsafe_allow_html=True)
        
        st.markdown("---")
        
        for i, step in enumerate(content_4_5["example_worked"]["steps"]):
            if i > 0:
                st.markdown("---")
            
            st.markdown(f"**{t(step['label'])}:**")
            st.latex(step["latex"])
            
            if step.get("note"):
                st.caption(t(step["note"]))
        
        st.markdown("---")
        check_text = t(content_4_5['example_worked']['check'])
        st.markdown(f"""
<div style="background-color: #f4f4f5; border-radius: 8px; padding: 12px; border-left: 4px solid #a1a1aa; color: #3f3f46;">
{check_text}
</div>""", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- EXAM ESSENTIALS (Using Utility) ---
    from utils.exam_essentials import render_exam_essentials
    render_exam_essentials(items=content_4_5["exam_essentials"]["items"])
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- EXAM SECTION ---
    st.markdown(f"### {t({'de': 'Prüfungstraining', 'en': 'Exam Practice'})}")
    
    with st.container(border=True):
        st.markdown(f"""
<div style="background: #f4f4f5; border-left: 4px solid #a1a1aa; padding: 12px 16px; border-radius: 8px; color: #3f3f46;">
{t({"de": "Für diesen Abschnitt gibt es derzeit keine MCQ-Fragen. Die Theorie oben deckt die Prüfungsinhalte ab.", "en": "This section currently has no MCQ questions. The theory above covers the exam content."})}
</div>
""", unsafe_allow_html=True)
