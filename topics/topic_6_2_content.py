# Topic 6.2: CLT Applications — De Moivre-Laplace & Continuity Correction
# ULTRATHINK IMPLEMENTATION
import streamlit as st
import numpy as np
from scipy import stats
from utils.localization import t
from utils.layouts.foundation import grey_info
from utils.quiz_helper import render_mcq
from utils.ask_yourself import render_ask_yourself
from utils.exam_essentials import render_exam_essentials
from utils.worked_example import render_worked_example
from utils.layouts import (
    render_single_formula,
    render_comparison,
    render_steps,
)
from utils.layouts.foundation import grey_callout, intuition_box, inject_equal_height_css

# ==========================================
# 1. CONTENT DICTIONARY - BILINGUAL
# ==========================================

content_6_2 = {
    "title": {"de": "6.2 Anwendungen des ZGS", "en": "6.2 Applications of the CLT"},
    "subtitle": {
        "de": "Von diskret zu stetig — das ±0.5 Geheimnis",
        "en": "From discrete to continuous — the ±0.5 secret"
    },
    
    # --- INTUITION (ONE combined intuition for entire topic) ---
    "intuition": {
        "de": "Stell dir vor, du wirfst eine Münze 100 Mal. Du kannst 0, 1, 2, ... oder 100 Mal Kopf bekommen — nur ganze Zahlen (Binomialverteilung). Aber wenn n gross genug ist, sieht diese Verteilung aus wie eine Glockenkurve (Normalverteilung). Das Problem: Die Normalverteilung kennt auch 50.3 oder 49.7. Wie passt das zusammen? Das ist, wo die Stetigkeitskorrektur ins Spiel kommt: Wir 'verschmieren' jede ganze Zahl um ±0.5, um die Lücken zu füllen.",
        "en": "Imagine flipping a coin 100 times. You can get 0, 1, 2, ... or 100 heads — only whole numbers (Binomial distribution). But when n is large enough, this distribution looks like a bell curve (Normal distribution). The problem: The Normal also knows 50.3 or 49.7. How do we bridge this? That's where the continuity correction comes in: We 'smear' each integer by ±0.5 to fill the gaps."
    },
    
    # --- DE MOIVRE-LAPLACE THEOREM (no separate intuition - covered above) ---
    "theorem": {
        "title": {"de": "Der Satz von De Moivre-Laplace", "en": "De Moivre-Laplace Theorem"},
        "formula": r"Z_n = \frac{S_n - np}{\sqrt{np(1-p)}} \xrightarrow{d} N(0,1)",
        "variables": [
            {"symbol": r"S_n", "name": {"de": "Anzahl Erfolge", "en": "Number of successes"}, "description": {"de": "Summe der Bernoulli-Variablen (binomialverteilt)", "en": "Sum of Bernoulli variables (binomially distributed)"}},
            {"symbol": r"n", "name": {"de": "Anzahl Versuche", "en": "Number of trials"}, "description": {"de": "Wie oft wir das Experiment wiederholen", "en": "How many times we repeat the experiment"}},
            {"symbol": r"p", "name": {"de": "Erfolgswahrscheinlichkeit", "en": "Success probability"}, "description": {"de": "Wahrscheinlichkeit für Erfolg bei einem Versuch", "en": "Probability of success in one trial"}},
            {"symbol": r"np", "name": {"de": "Erwarteter Wert", "en": "Expected value"}, "description": {"de": "Durchschnittliche Anzahl Erfolge", "en": "Average number of successes"}},
            {"symbol": r"\sqrt{np(1-p)}", "name": {"de": "Standardabweichung", "en": "Standard deviation"}, "description": {"de": "Streuung der Binomialverteilung", "en": "Spread of the Binomial distribution"}},
        ],
        "insight": {
            "de": "Der Schlüssel: Das ist der ZGS für den SPEZIALFALL, wo alle X_i Bernoulli(p) sind. Die Binomialverteilung wird zur Normalverteilung!",
            "en": "The key: This is the CLT for the SPECIAL CASE where all X_i are Bernoulli(p). The Binomial distribution becomes the Normal distribution!"
        }
    },
    
    # --- CONTINUITY CORRECTION COMPARISON ---
    "correction": {
        "title": {"de": "Die Stetigkeitskorrektur", "en": "The Continuity Correction"},
        "intuition": {
            "de": "Die Binomialverteilung ist diskret (0, 1, 2, ...), die Normalverteilung ist stetig. Um diese Lücke zu überbrücken, verschieben wir unseren Wert um ±0.5.",
            "en": "The Binomial distribution is discrete (0, 1, 2, ...), the Normal is continuous. To bridge this gap, we shift our value by ±0.5."
        },
        "left": {
            "title": {"de": "OHNE Korrektur", "en": "WITHOUT Correction"},
            "intuition": {"de": "Direkte Standardisierung", "en": "Direct standardization"},
            "formula": r"\begin{aligned} &P(X \geq 60) \\ &\approx P\left(Z \geq \frac{60-50}{5}\right) \\ &= P(Z \geq 2.0) \end{aligned}",
            "insight": {"de": "Fehler: ca. 2% Abweichung", "en": "Error: ~2% deviation"}
        },
        "right": {
            "title": {"de": "MIT Korrektur", "en": "WITH Correction"},
            "intuition": {"de": "Anpassung um -0.5", "en": "Adjustment by -0.5"},
            "formula": r"\begin{aligned} &P(X \geq 60) \\ &\approx P\left(Z \geq \frac{59.5-50}{5}\right) \\ &= P(Z \geq 1.9) \end{aligned}",
            "insight": {"de": "Genauere Approximation!", "en": "More accurate approximation!"}
        },
        "key_difference": {
            "de": "Welche Richtung?",
            "en": "Which direction?"
        },
        "key_difference_visual": True  # Triggers visual rendering instead of text + formula
    },
    
    # --- STEP-BY-STEP PROCEDURE ---
    "steps": {
        "title": {"de": "Schritt-für-Schritt: De Moivre-Laplace anwenden", "en": "Step-by-Step: Applying De Moivre-Laplace"},
        "steps_list": [
            {"action": {"de": "Identifiziere n und p", "en": "Identify n and p"}, "explanation": {"de": "Anzahl Versuche und Erfolgswahrscheinlichkeit aus der Aufgabe", "en": "Number of trials and success probability from the problem"}},
            {"action": {"de": "Berechne Erwartungswert und Streuung", "en": "Calculate mean and spread"}, "formula": r"\mu = np, \quad \sigma = \sqrt{np(1-p)}"},
            {"action": {"de": "Wende Stetigkeitskorrektur an", "en": "Apply continuity correction"}, "explanation": {"de": "±0.5 je nach Fragestellung", "en": "±0.5 depending on the question"}, "formula": r"P(X \geq k) \to k-0.5, \quad P(X \leq k) \to k+0.5"},
            {"action": {"de": "Standardisiere", "en": "Standardize"}, "formula": r"Z = \frac{X \pm 0.5 - \mu}{\sigma}"},
            {"action": {"de": "Nachschlagen", "en": "Look up"}, "explanation": {"de": "Z-Wert in Standardnormaltabelle nachschlagen", "en": "Look up Z-value in standard normal table"}},
        ]
    },
    
    # --- WORKED EXAMPLE ---
    "worked_example": {
        "header": {"de": "Beispiel: Ist die Münze fair?", "en": "Example: Is the Coin Fair?"},
        "problem": {
            "de": "Eine Münze wird <strong style='color:#007AFF'>100</strong> Mal geworfen. Wir beobachten <strong style='color:#FF4B4B'>60</strong> Mal Kopf. Angenommen die Münze ist fair (<strong style='color:#FF4B4B'>p = 0.5</strong>), wie wahrscheinlich ist dieses Ergebnis?",
            "en": "A coin is flipped <strong style='color:#007AFF'>100</strong> times. We observe <strong style='color:#FF4B4B'>60</strong> heads. Assuming the coin is fair (<strong style='color:#FF4B4B'>p = 0.5</strong>), how likely is this result?"
        },
        "steps": [
            {"label": {"de": "Gegeben", "en": "Given"}, "latex": r"n = {\color{#007AFF}100}, \quad p = {\color{#FF4B4B}0.5}", "note": {"de": "Faire Münze: p = 0.5", "en": "Fair coin: p = 0.5"}},
            {"label": {"de": "Erwartungswert und Streuung", "en": "Mean and Spread"}, "latex": r"\mu = {\color{#007AFF}100} \cdot {\color{#FF4B4B}0.5} = {\color{#9B59B6}50}, \quad \sigma = \sqrt{{\color{#007AFF}100} \cdot {\color{#FF4B4B}0.5} \cdot {\color{#FF4B4B}0.5}} = {\color{#6B7280}5}", "note": None},
            {"label": {"de": "Stetigkeitskorrektur", "en": "Continuity Correction"}, "latex": r"P(X \geq 60) \rightarrow P(X \geq 59.5)", "note": {"de": "Wir suchen ≥, also -0.5", "en": "We want ≥, so -0.5"}},
            {"label": {"de": "Standardisierung", "en": "Standardization"}, "latex": r"Z = \frac{59.5 - {\color{#9B59B6}50}}{{\color{#6B7280}5}} = {\color{#16a34a}1.9}", "note": None},
            {"label": {"de": "Nachschlagen", "en": "Look up"}, "latex": r"P(Z \geq {\color{#16a34a}1.9}) = 1 - \Phi(1.9) \approx 0.0287", "note": None},
        ],
        "answer": {
            "de": "Nur 2.87% Wahrscheinlichkeit bei fairer Münze. Das ist verdächtig!",
            "en": "Only 2.87% probability for a fair coin. That's suspicious!"
        }
    },
    
    # --- FRAG DICH ---
    "frag_dich": {
        "header": {"de": "Frag dich: Wann brauche ich was?", "en": "Ask yourself: When do I need what?"},
        "questions": [
            {"de": "Sind die X<sub>i</sub> Bernoulli (Erfolg/Misserfolg)?", "en": "Are the X<sub>i</sub> Bernoulli (success/failure)?"},
            {"de": "Approximiere ich DISKRET mit STETIG?", "en": "Am I approximating DISCRETE with CONTINUOUS?"},
            {"de": "Suche ich P(X ≥ k)? Dann: k - 0.5", "en": "Am I looking for P(X ≥ k)? Then: k - 0.5"},
            {"de": "Suche ich P(X ≤ k)? Dann: k + 0.5", "en": "Am I looking for P(X ≤ k)? Then: k + 0.5"},
            {"de": "Ist np ≥ 5 UND n(1-p) ≥ 5? Sonst ist die Approximation schlecht!", "en": "Is np ≥ 5 AND n(1-p) ≥ 5? Otherwise the approximation is poor!"},
        ],
        "conclusion": {"de": "Alle JA? → De Moivre-Laplace mit Korrektur!", "en": "All YES? → De Moivre-Laplace with correction!"}
    },
    
    # --- EXAM ESSENTIALS ---
    "exam_essentials": {
        "trap": {
            "de": "Die Stetigkeitskorrektur vergessen! Studenten berechnen direkt ohne die ±0.5 Anpassung.",
            "en": "Forgetting the continuity correction! Students calculate directly without the ±0.5 adjustment."
        },
        "trap_formula": {
            "de": r"Z = \frac{X - np}{\sigma} \quad \text{FALSCH!}",
            "en": r"Z = \frac{X - np}{\sigma} \quad \text{WRONG!}"
        },
        "trap_rule": {
            "de": "Für diskrete X immer zuerst X um ±0.5 anpassen, DANN standardisieren.",
            "en": "For discrete X, always adjust X by ±0.5 FIRST, then standardize."
        },
        "tips": [
            {
                "tip": {"de": "Prüfe: Diskret → Stetig? Dann ±0.5", "en": "Check: Discrete → Continuous? Then ±0.5"},
                "tip_formula": r"P(X \geq k) \rightarrow P(X \geq k - 0.5)",
                "why": {"de": "Prüfungen lieben diesen Stolperstein.", "en": "Exams love this stumbling block."}
            },
            {
                "tip": {"de": "Faustregel für Gültigkeit", "en": "Rule of Thumb for Validity"},
                "tip_formula": r"np \geq 5 \quad \text{AND} \quad n(1-p) \geq 5",
                "why": {"de": "Approximation funktioniert nur, wenn beide Enden genug Masse haben.", "en": "Approximation only works if both tails have enough mass."}
            },
            {
                "tip": {"de": "Merkhilfe für die Richtung", "en": "Memory aid for direction"},
                "why": {"de": "Du willst k immer mit-erfassen, also erweitere den Bereich.", "en": "You always want to include k, so expand the range."},
                "why_formula": r"P(X \geq k) \to k - 0.5 \quad | \quad P(X \leq k) \to k + 0.5"
            },
        ]
    },
}

# ==========================================
# 2. INTERACTIVE: CONTINUITY CORRECTION COMPARATOR
# ==========================================

@st.fragment
def continuity_correction_interactive():
    """Interactive element to compare WITH vs WITHOUT continuity correction."""
    
    # Scenario
    grey_callout(
        {"de": "Szenario", "en": "Scenario"},
        {"de": "Du bist Qualitätskontrolleur. Bei n Produkten ist jedes mit Wahrscheinlichkeit p defekt. Du fragst: Wie wahrscheinlich sind mindestens k defekte Produkte?", 
         "en": "You're a quality controller. Among n products, each is defective with probability p. You ask: How likely are at least k defective products?"}
    )
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown(f"**{t({'de': 'Mission', 'en': 'Mission'})}:** {t({'de': 'Beobachte, wie die Stetigkeitskorrektur das Ergebnis beeinflusst.', 'en': 'Observe how the continuity correction affects the result.'})}")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Semantic slider colors: n=blue, p=purple, k=red (same CSS pattern as topic 1.5)
    st.markdown("""
<style>
/* 1. n (Blue) */
.stSlider:has([aria-label*="n ="]) div[data-baseweb="slider"] > div:first-child > div:first-child { background-color: #007AFF !important; }
.stSlider:has([aria-label*="n ="]) div[role="slider"] { background-color: #FFFFFF !important; border: 2px solid #007AFF !important; }

/* 2. p (Purple) */
.stSlider:has([aria-label*="p ="]) div[data-baseweb="slider"] > div:first-child > div:first-child { background-color: #9B59B6 !important; }
.stSlider:has([aria-label*="p ="]) div[role="slider"] { background-color: #FFFFFF !important; border: 2px solid #9B59B6 !important; }

/* 3. k (Red) */
.stSlider:has([aria-label*="k ="]) div[data-baseweb="slider"] > div:first-child > div:first-child { background-color: #FF4B4B !important; }
.stSlider:has([aria-label*="k ="]) div[role="slider"] { background-color: #FFFFFF !important; border: 2px solid #FF4B4B !important; }
</style>
""", unsafe_allow_html=True)
    
    # Controls with visible labeled sliders (so CSS can target them)
    col1, col2, col3 = st.columns(3)
    with col1:
        n = st.slider("n = Sample Size", min_value=20, max_value=200, value=70, step=10, key="cc_n")
    with col2:
        p = st.slider("p = Probability", min_value=0.1, max_value=0.5, value=0.3, step=0.05, key="cc_p")
    with col3:
        k = st.slider("k = Threshold", min_value=int(n*p*0.5), max_value=int(n*p*1.5), value=int(n*p*1.2), step=1, key="cc_k")
    
    # Calculations
    mu = n * p
    sigma = np.sqrt(n * p * (1 - p))
    
    # Without correction
    z_without = (k - mu) / sigma
    p_without = 1 - stats.norm.cdf(z_without)
    
    # With correction
    z_with = (k - 0.5 - mu) / sigma
    p_with = 1 - stats.norm.cdf(z_with)
    
    # Exact Binomial
    p_exact = 1 - stats.binom.cdf(k - 1, n, p)
    
    # Display results
    st.markdown("<br>", unsafe_allow_html=True)
    
    inject_equal_height_css()
    
    # TOP ROW: WITHOUT and WITH (2 columns)
    c1, c2 = st.columns(2, gap="medium")
    
    # WITHOUT Correction
    with c1:
        with st.container(border=True):
            st.markdown(f"**{t({'de': 'OHNE Korrektur', 'en': 'WITHOUT Correction'})}**")
            st.latex(rf"Z = \frac{{{k} - {mu:.1f}}}{{{sigma:.2f}}} = {z_without:.3f}")
            st.latex(rf"\Rightarrow \quad P(X \geq {k}) \approx {p_without:.4f}")
    
    # WITH Correction
    with c2:
        with st.container(border=True):
            st.markdown(f"**{t({'de': 'MIT Korrektur', 'en': 'WITH Correction'})}**")
            st.latex(rf"Z = \frac{{{k - 0.5} - {mu:.1f}}}{{{sigma:.2f}}} = {z_with:.3f}")
            st.latex(rf"\Rightarrow \quad P(X \geq {k}) \approx {p_with:.4f}")
    
    # BOTTOM ROW: EXACT (full width) - with full formula
    with st.container(border=True):
        st.markdown(f"**{t({'de': 'EXAKT (Binomial)', 'en': 'EXACT (Binomial)'})}**")
        st.latex(rf"P(X \geq {k}) = \sum_{{i={k}}}^{{{n}}} \binom{{{n}}}{{i}} {p}^i (1-{p})^{{{n}-i}} = {p_exact:.4f}")
    
    # Error comparison
    error_without = abs(p_without - p_exact)
    error_with = abs(p_with - p_exact)
    
    if error_without > error_with:
        st.success(t({
            "de": f"MIT Korrektur ist näher am exakten Wert! Fehler: {error_with:.4f} vs {error_without:.4f}",
            "en": f"WITH correction is closer to exact! Error: {error_with:.4f} vs {error_without:.4f}"
        }))
    else:
        grey_info(t({
            "de": f"In diesem Fall sind beide Approximationen ähnlich. Fehler: {error_with:.4f} vs {error_without:.4f}",
            "en": f"In this case both approximations are similar. Error: {error_with:.4f} vs {error_without:.4f}"
        }))
    
    # Discovery debrief
    st.markdown("<br>", unsafe_allow_html=True)
    grey_callout(
        {"de": "Was du gelernt hast", "en": "What you learned"},
        {"de": "Die Stetigkeitskorrektur (±0.5) verringert den Fehler, wenn wir eine diskrete Verteilung (Binomial) mit einer stetigen (Normal) approximieren. Der Unterschied wird umso wichtiger, je kleiner n oder je extremer k.", 
         "en": "The continuity correction (±0.5) reduces the error when approximating a discrete distribution (Binomial) with a continuous one (Normal). The difference becomes more important with smaller n or more extreme k."}
    )


# ==========================================
# 3. MCQ QUESTIONS
# ==========================================

QUESTIONS_6_2 = {
    "uebung4_prob3": {
        "source": "Übung 4, Probe #3",
        "type": "mc",
        "question": {
            "de": r"Produktion $n=2000$. Zurückweisung wenn $>200$ defekt. Gesucht: max $p$, damit mit 95% Wahrscheinlichkeit NICHT zurückgewiesen ($k \le 200$).",
            "en": r"Production $n=2000$. Rejection if $>200$ defective. Find: max $p$ such that with 95% probability it is NOT rejected ($k \le 200$)."
        },
        "options": [
            {"de": "0.080", "en": "0.080"},
            {"de": "0.090", "en": "0.090"},
            {"de": "0.100", "en": "0.100"},
            {"de": "0.110", "en": "0.110"}
        ],
        "correct_idx": 1,
        "solution": {
            "de": r"<strong>Richtig: 0.090</strong><br>$P(X \le 200) = 0.95 \implies Z=1.645$. Auflösen nach p ergibt ca. 9%.",
            "en": r"<strong>Correct: 0.090</strong><br>$P(X \le 200) = 0.95 \implies Z=1.645$. Solving for p gives ~9%."
        }
    },
    "hs2022_mc10": {
        "source": "HS 2023 Januar, MC #9",
        "type": "mc",
        "question": {
            "de": r"Schach-Engine-Züge: Ein starker Spieler findet mit $p=0.3$ zufällig einen Top-Engine-Zug. Algorithmus sperrt bei $\geq 340$ Top-Zügen in 1000 Zügen. Wie hoch ist die Wahrscheinlichkeit, einen ehrlichen Spieler fälschlich zu sperren?",
            "en": r"Chess engine moves: A strong player finds a top engine move by chance with $p=0.3$. Algorithm bans at $\geq 340$ top moves in 1000 moves. What's the probability of falsely banning an honest player?"
        },
        "options": [
            {"de": "0.1%", "en": "0.1%"},
            {"de": "0.3%", "en": "0.3%"},
            {"de": "0.5%", "en": "0.5%"},
            {"de": "0.7%", "en": "0.7%"}
        ],
        "correct_idx": 1,
        "solution": {
            "de": r"<strong>Richtig: 0.3%</strong><br>$\mu = 300, \sigma = \sqrt{1000 \cdot 0.3 \cdot 0.7} \approx 14.5$.<br>$Z = (340-300)/14.5 \approx 2.76$.<br>$P(Z > 2.76) \approx 0.003 = 0.3\%$.",
            "en": r"<strong>Correct: 0.3%</strong><br>$\mu = 300, \sigma = \sqrt{1000 \cdot 0.3 \cdot 0.7} \approx 14.5$.<br>$Z = (340-300)/14.5 \approx 2.76$.<br>$P(Z > 2.76) \approx 0.003 = 0.3\%$."
        }
    },
    "hs2023_mc3": {
        "source": "HS 2023 Januar, MC #3",
        "type": "mc",
        "question": {
            "de": r"Öltanker mit 30000 m³ Kapazität. Bei $>27040$ Tonnen läuft er auf Grund. Gewicht von 1 m³ Öl: $\mu=0.9$, $\sigma^2=?$. Kapitän schätzt Grundlauf-Risiko auf 0.2%. Welche Varianz $\sigma^2$ nimmt er an?",
            "en": r"Oil tanker with 30,000 m³ capacity. It runs aground if $>27,040$ tons. Weight of 1 m³ oil: $\mu=0.9$, $\sigma^2=?$. Captain estimates grounding risk at 0.2%. What variance $\sigma^2$ does he assume?"
        },
        "options": [
            {"de": "0.0064", "en": "0.0064"},
            {"de": "0.0802", "en": "0.0802"},
            {"de": "193.1477", "en": "193.1477"},
            {"de": "Nicht genügend Informationen", "en": "Not enough information"}
        ],
        "correct_idx": 0,
        "solution": {
            "de": r"<strong>Richtig: 0.0064</strong><br>Puffer = 27040 - 30000·0.9 = 40. $z \approx 2.88$ (für 0.2%).<br>$40 = 2.88 \cdot \sqrt{30000}\sigma$.<br>$\sigma \approx 0.08 \Rightarrow \sigma^2 = 0.0064$.",
            "en": r"<strong>Correct: 0.0064</strong><br>Buffer = 27040 - 30000·0.9 = 40. $z \approx 2.88$ (for 0.2%).<br>$40 = 2.88 \cdot \sqrt{30000}\sigma$.<br>$\sigma \approx 0.08 \Rightarrow \sigma^2 = 0.0064$."
        }
    }
}


# ==========================================
# 4. MAIN RENDER FUNCTION
# ==========================================

def render_subtopic_6_2(model):
    """Render Topic 6.2: CLT Applications — De Moivre-Laplace & Continuity Correction"""
    
    st.header(t(content_6_2["title"]))
    st.caption(t(content_6_2["subtitle"]))
    st.markdown("---")
    
    # ═══════════════════════════════════════════════════════════════
    # 1. INTUITION (Outside container)
    # ═══════════════════════════════════════════════════════════════
    intuition_box(content_6_2["intuition"])
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # ═══════════════════════════════════════════════════════════════
    # 2. DE MOIVRE-LAPLACE THEOREM
    # ═══════════════════════════════════════════════════════════════
    render_single_formula(
        title=content_6_2["theorem"]["title"],
        intuition=None,  # No separate intuition - covered in page intro
        formula=content_6_2["theorem"]["formula"],
        variables=content_6_2["theorem"]["variables"],
        insight=content_6_2["theorem"]["insight"]
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # ═══════════════════════════════════════════════════════════════
    # 3. CONTINUITY CORRECTION COMPARISON
    # ═══════════════════════════════════════════════════════════════
    render_comparison(
        title=content_6_2["correction"]["title"],
        intuition=None,  # No separate intuition - covered in page intro
        left=content_6_2["correction"]["left"],
        right=content_6_2["correction"]["right"],
        key_difference=None  # We render the mnemonic below
    )
    
    # Clean mnemonic - one simple rule
    st.markdown(f"### {t({'de': 'Merke', 'en': 'Remember'})}")
    with st.container(border=True):
        # The core insight in one sentence
        st.markdown(t({
            "de": "**Du willst die Zahl k mit-erfassen.** Dazu musst du den Bereich *erweitern*:",
            "en": "**You want to include the number k.** So you must *expand* the range:"
        }))
        
        # Simple inline table using markdown
        st.markdown(f"""
| {t({"de": "Frage", "en": "Question"})} | {t({"de": "Bedeutet", "en": "Means"})} | {t({"de": "Korrektur", "en": "Correction"})} |
|:---|:---|:---|
| $P(X \\geq k)$ | {t({"de": "mindestens k", "en": "at least k"})} | $k - 0.5$ |
| $P(X \\leq k)$ | {t({"de": "höchstens k", "en": "at most k"})} | $k + 0.5$ |
""")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # ═══════════════════════════════════════════════════════════════
    # 4. STEP-BY-STEP PROCEDURE
    # ═══════════════════════════════════════════════════════════════
    render_steps(
        title=content_6_2["steps"]["title"],
        steps=content_6_2["steps"]["steps_list"]
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # ═══════════════════════════════════════════════════════════════
    # 5. WORKED EXAMPLE
    # ═══════════════════════════════════════════════════════════════
    render_worked_example(
        header=content_6_2["worked_example"]["header"],
        problem=content_6_2["worked_example"]["problem"],
        steps=content_6_2["worked_example"]["steps"],
        answer=content_6_2["worked_example"]["answer"]
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # ═══════════════════════════════════════════════════════════════
    # 6. INTERACTIVE: Continuity Correction Comparator
    # ═══════════════════════════════════════════════════════════════
    st.markdown(f"### {t({'de': 'Interaktiv: Stetigkeitskorrektur testen', 'en': 'Interactive: Test Continuity Correction'})}")
    continuity_correction_interactive()
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # ═══════════════════════════════════════════════════════════════
    # 7. FRAG DICH - Blue themed with st.container for proper LaTeX
    # ═══════════════════════════════════════════════════════════════
    # Inject scoped CSS to make the next container blue-bordered
    st.markdown("""
<style>
/* Blue border for Ask Yourself container */
[data-testid="stVerticalBlockBorderWrapper"]:has(div[data-testid="stMarkdown"] > div > p > strong:first-child:contains("1.")) > div {
    border-color: #007AFF !important;
    border-width: 2px !important;
    background-color: rgba(0, 122, 255, 0.04) !important;
}
</style>
""", unsafe_allow_html=True)
    
    st.markdown(f"**<span style='color: #007AFF; font-size: 1.1em;'>{t(content_6_2['frag_dich']['header'])}</span>**", unsafe_allow_html=True)
    
    with st.container(border=True):
        # Question 1
        st.markdown(f"**1.** {t({'de': 'Sind die', 'en': 'Are the'})} $X_i$ {t({'de': 'Bernoulli (Erfolg/Misserfolg)?', 'en': 'Bernoulli (success/failure)?'})}")
        
        # Question 2
        st.markdown(f"**2.** {t({'de': 'Approximiere ich DISKRET mit STETIG?', 'en': 'Am I approximating DISCRETE with CONTINUOUS?'})}")
        
        # Question 3 with LaTeX
        st.markdown(f"**3.** {t({'de': 'Suche ich', 'en': 'Am I looking for'})} $P(X \\geq k)$? {t({'de': 'Dann:', 'en': 'Then:'})} $k - 0.5$")
        
        # Question 4 with LaTeX
        st.markdown(f"**4.** {t({'de': 'Suche ich', 'en': 'Am I looking for'})} $P(X \\leq k)$? {t({'de': 'Dann:', 'en': 'Then:'})} $k + 0.5$")
        
        # Question 5 with LaTeX
        st.markdown(f"**5.** {t({'de': 'Gültigkeitsprüfung:', 'en': 'Validity check:'})} $np \\geq 5$ {t({'de': 'UND', 'en': 'AND'})} $n(1-p) \\geq 5$")
        st.markdown(f"*{t({'de': 'Sonst ist die Approximation schlecht!', 'en': 'Otherwise the approximation is poor!'})}*")
        
        # Conclusion button INSIDE the container
        st.markdown(f"""
<div style="background: #007AFF; color: white; padding: 12px 20px; border-radius: 8px; text-align: center; font-weight: bold; margin-top: 12px;">
{t(content_6_2['frag_dich']['conclusion'])}
</div>
""", unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # ═══════════════════════════════════════════════════════════════
    # 8. EXAM ESSENTIALS
    # ═══════════════════════════════════════════════════════════════
    render_exam_essentials(
        trap=content_6_2["exam_essentials"]["trap"],
        trap_formula=content_6_2["exam_essentials"]["trap_formula"],
        trap_rule=content_6_2["exam_essentials"]["trap_rule"],
        tips=content_6_2["exam_essentials"]["tips"]
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # ═══════════════════════════════════════════════════════════════
    # 9. MCQ SECTION
    # ═══════════════════════════════════════════════════════════════
    st.markdown(f"### {t({'de': 'Prüfungstraining', 'en': 'Exam Practice'})}")
    
    for q_id, q in QUESTIONS_6_2.items():
        st.caption(q.get("source", ""))
        with st.container(border=True):
            opts = q.get("options", [])
            option_labels = [t(o) for o in opts]
            
            render_mcq(
                key_suffix=f"6_2_{q_id}",
                question_text=t(q["question"]),
                options=option_labels,
                correct_idx=q["correct_idx"],
                solution_text_dict=q["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Falsch.", "en": "Incorrect."},
                client=model,
                ai_context=f"De Moivre-Laplace: {q_id}",
                course_id="vwl",
                topic_id="6",
                subtopic_id="6.2",
                question_id=q_id
            )
        st.markdown("<br>", unsafe_allow_html=True)
