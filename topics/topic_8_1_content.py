# Topic 8.1: Intuitive Heuristic Approaches for Estimators
# POINT ESTIMATION - The art of guessing population parameters from samples

import streamlit as st
import numpy as np
import plotly.graph_objects as go
from utils.localization import t
from utils.quiz_helper import render_mcq
from utils.ask_yourself import render_ask_yourself
from utils.exam_essentials import render_exam_essentials
from utils.worked_example import render_worked_example
from utils.layouts import render_definition, render_comparison, render_formula_breakdown
from utils.layouts.foundation import grey_callout, intuition_box, key_insight, inject_equal_height_css
from data.exam_questions import QUESTIONS_8

# ============================================================================
# CONTENT DICTIONARY - All bilingual content
# ============================================================================

content_8_1 = {
    "title": {
        "de": "8.1 Intuitiv heuristische Ansätze für Schätzfunktionen",
        "en": "8.1 Intuitive Heuristic Approaches for Estimators"
    },
    "subtitle": {
        "de": "Wie schätzen wir unbekannte Grössen aus Stichproben?",
        "en": "How do we estimate unknown quantities from samples?"
    },
    
    # THE BIG PICTURE - Pool Temperature Analogy
    "intuition": {
        "de": """Stell dir vor, du möchtest die <strong>durchschnittliche Wassertemperatur</strong> deines Schwimmbeckens wissen. 
Du kannst nicht jedes einzelne Wassermolekül messen — das wäre unmöglich. 
Stattdessen tauchst du deine Hand an 5 verschiedenen Stellen ein und berechnest den Durchschnitt.

<strong>Das ist genau das, was Schätzfunktionen tun:</strong> Sie nehmen eine Stichprobe und berechnen daraus einen Wert, 
der möglichst nahe am wahren (aber unbekannten) Wert der gesamten Population liegt.""",
        "en": """Imagine you want to know the <strong>average water temperature</strong> of your swimming pool. 
You can't measure every single water molecule — that would be impossible. 
Instead, you dip your hand in at 5 different spots and calculate the average.

<strong>This is exactly what estimators do:</strong> They take a sample and compute a value 
that should be as close as possible to the true (but unknown) population value."""
    },
    
    # THE THREE MUSKETEERS - Three Key Estimators
    "three_estimators": {
        "header": {"de": "Die drei wichtigsten Schätzer", "en": "The Three Key Estimators"},
        "intro": {
            "de": "Für verschiedene Parameter brauchen wir verschiedene Schätzer:",
            "en": "For different parameters, we need different estimators:"
        }
    },
    
    # Estimator 1: Sample Mean
    "estimator_mean": {
        "name": {"de": "Stichprobenmittel", "en": "Sample Mean"},
        "symbol": r"\hat{\mu} = \bar{X}",
        "formula": r"\hat{\mu} = \bar{X} = \frac{1}{n} \sum_{i=1}^{n} X_i",
        "what_it_estimates": {"de": "Populationsmittel", "en": "Population mean"},
        "when_to_use": {"de": "Durchschnittswerte (Grösse, Gewicht, Einkommen)", "en": "Average values (height, weight, income)"},
        "example": {"de": "10 Studenten messen → Durchschnitt = Schätzer für alle Studenten", "en": "Measure 10 students → Average = estimator for all students"}
    },
    
    # Estimator 2: Sample Variance
    "estimator_variance": {
        "name": {"de": "Stichprobenvarianz", "en": "Sample Variance"},
        "symbol": r"\hat{\sigma}^2 = S^2",
        "formula": r"\hat{\sigma}^2 = S^2 = \frac{1}{n} \sum_{i=1}^{n} (X_i - \bar{X})^2",
        "what_it_estimates": {"de": "Populationsvarianz", "en": "Population variance"},
        "when_to_use": {"de": "Streuung (Risiko, Qualitätskontrolle)", "en": "Spread (risk, quality control)"},
        "example": {"de": "Wie stark schwanken Paketgewichte?", "en": "How much do package weights vary?"}
    },
    
    # Estimator 3: Sample Proportion
    "estimator_proportion": {
        "name": {"de": "Stichprobenanteil", "en": "Sample Proportion"},
        "symbol": r"\hat{p}",
        "formula": r"\hat{p} = \frac{1}{n} \sum_{i=1}^{n} X_i = \frac{\text{Anzahl Erfolge}}{n}",
        "formula_en": r"\hat{p} = \frac{1}{n} \sum_{i=1}^{n} X_i = \frac{\text{Number of successes}}{n}",
        "what_it_estimates": {"de": "Erfolgswahrscheinlichkeit p", "en": "Success probability p"},
        "when_to_use": {"de": "Anteile (Fehlerquote, Wahlprognose)", "en": "Proportions (defect rate, election polls)"},
        "example": {"de": "8 von 100 Teilen defekt → p = 0.08", "en": "8 of 100 parts defective → p = 0.08"}
    },
    
    # HAT NOTATION
    "hat_notation": {
        "title": {"de": "Die 'Hut'-Notation", "en": "The 'Hat' Notation"},
        "definition": {
            "de": "Das Dach-Symbol ^ bedeutet 'geschätzt aus Daten'. Wenn du θ (theta) siehst, ist das der wahre (unbekannte) Parameter. Wenn du θ̂ (theta-Hut) siehst, ist das dein Schätzwert aus der Stichprobe.",
            "en": "The hat symbol ^ means 'estimated from data'. When you see θ (theta), that's the true (unknown) parameter. When you see θ̂ (theta-hat), that's your estimate from the sample."
        }
    },
    
    # WORKED EXAMPLE
    "worked_example": {
        "header": {"de": "Rechenbeispiel: Studentengrössen", "en": "Worked Example: Student Heights"},
        "problem": {
            "de": "Aus einer Vorlesung werden 10 Studenten zufällig ausgewählt. Ihre Körpergrössen (in cm) sind: 176, 180, 181, 168, 177, 186, 184, 173, 182, 177. Schätze die mittlere Körpergrösse aller Studenten.",
            "en": "From a lecture, 10 students are randomly selected. Their heights (in cm) are: 176, 180, 181, 168, 177, 186, 184, 173, 182, 177. Estimate the mean height of all students."
        },
        "steps": [
            {
                "label": {"de": "Gegeben", "en": "Given"},
                "latex": r"n = {\color{#007AFF}10}, \quad X_i = \{176, 180, 181, 168, 177, 186, 184, 173, 182, 177\}",
                "note": {"de": "Stichprobengrösse und Daten", "en": "Sample size and data"}
            },
            {
                "label": {"de": "Formel", "en": "Formula"},
                "latex": r"\hat{\mu} = \bar{X} = \frac{1}{n} \sum_{i=1}^{n} X_i",
                "note": {"de": "Stichprobenmittel als Schätzer", "en": "Sample mean as estimator"}
            },
            {
                "label": {"de": "Summe berechnen", "en": "Calculate sum"},
                "latex": r"\sum_{i=1}^{10} X_i = 176 + 180 + \ldots + 177 = {\color{#9B59B6}1784}",
                "note": {"de": "Alle Werte addieren", "en": "Add all values"}
            },
            {
                "label": {"de": "Ergebnis", "en": "Result"},
                "latex": r"\hat{\mu} = \bar{X} = \frac{{\color{#9B59B6}1784}}{{\color{#007AFF}10}} = {\color{#16a34a}178.4 \text{ cm}}",
                "note": {"de": "Punktschätzung", "en": "Point estimate"}
            }
        ],
        "answer": {
            "de": "Die geschätzte mittlere Körpergrösse beträgt 178.4 cm",
            "en": "The estimated mean height is 178.4 cm"
        }
    },
    
    # KEY INSIGHT
    "key_insight": {
        "de": "Der Schlüssel: Ein Schätzer ist selbst eine <strong>Zufallsvariable</strong>. Wenn du eine andere Stichprobe ziehst, erhältst du einen anderen Schätzwert. Deshalb hat jeder Schätzer einen Erwartungswert und eine Varianz. Je grösser die Stichprobe, desto stabiler der Schätzer.",
        "en": "The key: An estimator is itself a <strong>random variable</strong>. If you draw a different sample, you get a different estimate. That's why every estimator has an expected value and variance. The larger the sample, the more stable the estimator."
    },
    
    # FRAG DICH (Ask Yourself)
    "frag_dich": {
        "header": {"de": "Frag dich: Erkennst du Schätzprobleme?", "en": "Ask yourself: Can you recognize estimation problems?"},
        "questions": [
            {"de": "Du hast 10 Studenten gemessen. Was ist dein Schätzer für das Populationsmittel?", 
             "en": "You measured 10 students. What is your estimator for the population mean?"},
            {"de": "Eine Fabrik prüft 100 Produkte und findet 8 defekte. Was ist p̂?", 
             "en": "A factory checks 100 products and finds 8 defective. What is p̂?"},
            {"de": "Warum verwenden wir X̄ statt nur X₁?", 
             "en": "Why do we use X̄ instead of just X₁?"},
            {"de": "Was bedeutet das ^ Symbol in der Statistik?", 
             "en": "What does the ^ symbol mean in statistics?"}
        ],
        "conclusion": {
            "de": "Wenn du alle Fragen beantworten kannst, verstehst du das Grundprinzip der Punktschätzung!",
            "en": "If you can answer all questions, you understand the basic principle of point estimation!"
        }
    },
    
    # EXAM ESSENTIALS
    "exam_essentials": {
        "trap": {
            "de": "Verwechslung von n und (n-1) bei der Varianz! Die Stichprobenvarianz S² = (1/n)Σ(Xᵢ-X̄)² ist <strong>verzerrt</strong>. Für einen <strong>erwartungstreuen</strong> Schätzer muss durch (n-1) geteilt werden.",
            "en": "Confusing n and (n-1) for variance! The sample variance S² = (1/n)Σ(Xᵢ-X̄)² is <strong>biased</strong>. For an <strong>unbiased</strong> estimator, divide by (n-1)."
        },
        "trap_rule": {
            "de": "Fragen nach 'erwartungstreuem Varianzschätzer'? Immer (n-1) im Nenner!",
            "en": "Question asks for 'unbiased variance estimator'? Always (n-1) in denominator!"
        },
        "tips": [
            {
                "tip": {"de": "Hut = Schätzung", "en": "Hat = Estimate"},
                "why": {"de": "θ̂ bedeutet immer 'geschätzt aus Daten', θ ist der wahre Wert.", "en": "θ̂ always means 'estimated from data', θ is the true value."}
            },
            {
                "tip": {"de": "Gewichte summieren zu 1", "en": "Weights sum to 1"},
                "why": {"de": "Für erwartungstreue lineare Schätzer muss Σwᵢ = 1 gelten.", "en": "For unbiased linear estimators, Σwᵢ = 1 must hold."},
                "why_formula": r"\sum_{i=1}^{n} w_i = 1 \implies E[\hat{\theta}] = \theta"
            },
            {
                "tip": {"de": "Mehr Stichproben = weniger Varianz", "en": "More samples = less variance"},
                "why": {"de": "Die Varianz des Stichprobenmittels schrumpft mit n.", "en": "The variance of the sample mean shrinks with n."},
                "why_formula": r"\text{Var}(\bar{X}) = \frac{\sigma^2}{n}"
            }
        ]
    }
}


# ============================================================================
# INTERACTIVE: ESTIMATOR SHOWDOWN (WITH CHART)
# ============================================================================

@st.fragment
def estimator_showdown():
    """Interactive comparison of two estimators with visualization."""
    
    # Initialize state
    if "sd_rounds" not in st.session_state:
        st.session_state.sd_rounds = 0
        st.session_state.sd_a_wins = 0
        st.session_state.sd_b_wins = 0
        st.session_state.sd_history_a = []
        st.session_state.sd_history_b = []
    
    true_mu = 50
    sigma = 10
    
    # Scenario - relatable example
    st.markdown(f"""
<div style="background: #f4f4f5; border-left: 4px solid #a1a1aa; 
            padding: 12px 16px; border-radius: 8px; color: #3f3f46;">
<strong>{t({"de": "Szenario", "en": "Scenario"})}:</strong> {t({"de": "Du fragst 2 Freunde, wie lange die Pizza-Lieferung dauert. Der wahre Wert ist 50 Min. Wie kombinierst du ihre Schätzungen am besten?", "en": "You ask 2 friends how long pizza delivery takes. The true value is 50 min. How do you best combine their guesses?"})}
</div>
""", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Formulas using proper st.latex() - with variance formulas
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown(f"**A: {t({'de': 'Stichprobenmittel', 'en': 'Sample Mean'})}**")
        st.latex(r"\hat{\mu}_A = \frac{X_1 + X_2}{2}")
        st.latex(r"\text{Var} = \frac{\sigma^2}{2} = 5.0")
        st.markdown(f"<span style='color: #007AFF; font-weight: bold;'>{t({'de': 'EFFIZIENT', 'en': 'EFFICIENT'})}</span>", unsafe_allow_html=True)
    with col_b:
        st.markdown(f"**B: {t({'de': 'Gewichteter Durchschnitt', 'en': 'Weighted Average'})}**")
        st.latex(r"\hat{\mu}_B = \frac{X_1}{3} + \frac{2X_2}{3}")
        st.latex(r"\text{Var} = \frac{5\sigma^2}{9} = 5.56")
        st.markdown(f"<span style='color: #FF4B4B; font-weight: bold;'>{t({'de': 'WENIGER EFFIZIENT', 'en': 'LESS EFFICIENT'})}</span>", unsafe_allow_html=True)
    
    # Buttons
    b1, b2, b3 = st.columns(3)
    with b1:
        run = st.button(t({"de": "Runde spielen", "en": "Play Round"}), key="sd_run", use_container_width=True, type="primary")
    with b2:
        can_sim = st.session_state.sd_rounds >= 3
        sim = st.button(t({"de": "100x Simulieren", "en": "Simulate 100x"}), key="sd_sim", use_container_width=True, disabled=not can_sim)
        if not can_sim and st.session_state.sd_rounds > 0:
            st.caption(t({"de": f"Noch {3 - st.session_state.sd_rounds} Runden", "en": f"{3 - st.session_state.sd_rounds} more rounds"}))
    with b3:
        reset = st.button(t({"de": "Reset", "en": "Reset"}), key="sd_reset", use_container_width=True)
    
    # Handle actions
    if reset:
        st.session_state.sd_rounds = 0
        st.session_state.sd_a_wins = 0
        st.session_state.sd_b_wins = 0
        st.session_state.sd_history_a = []
        st.session_state.sd_history_b = []
        st.session_state.sd_last = None
        st.rerun(scope="fragment")
    
    if run:
        x1, x2 = np.random.normal(true_mu, sigma, 2)
        est_a, est_b = (x1 + x2) / 2, x1/3 + 2*x2/3
        err_a, err_b = abs(est_a - true_mu), abs(est_b - true_mu)
        st.session_state.sd_rounds += 1
        st.session_state.sd_history_a.append(err_a)
        st.session_state.sd_history_b.append(err_b)
        winner = "A" if err_a < err_b else "B"
        if err_a < err_b:
            st.session_state.sd_a_wins += 1
        else:
            st.session_state.sd_b_wins += 1
        st.session_state.sd_last = {"x1": x1, "x2": x2, "a": est_a, "b": est_b, "err_a": err_a, "err_b": err_b, "winner": winner}
        st.rerun(scope="fragment")
    
    if sim and can_sim:
        for _ in range(100):
            x1, x2 = np.random.normal(true_mu, sigma, 2)
            err_a, err_b = abs((x1+x2)/2 - true_mu), abs(x1/3 + 2*x2/3 - true_mu)
            st.session_state.sd_rounds += 1
            st.session_state.sd_history_a.append(err_a)
            st.session_state.sd_history_b.append(err_b)
            if err_a < err_b:
                st.session_state.sd_a_wins += 1
            else:
                st.session_state.sd_b_wins += 1
        st.session_state.sd_last = None
        st.rerun(scope="fragment")
    
    # Show last round calculation breakdown (if available)
    if hasattr(st.session_state, 'sd_last') and st.session_state.sd_last:
        lr = st.session_state.sd_last
        with st.container(border=True):
            st.markdown(f"**{t({'de': 'Letzte Runde', 'en': 'Last Round'})}:** {t({'de': 'Freund 1 sagt', 'en': 'Friend 1 says'})} **{lr['x1']:.1f}** min, {t({'de': 'Freund 2 sagt', 'en': 'Friend 2 says'})} **{lr['x2']:.1f}** min")
            
            res_a, res_b = st.columns(2)
            with res_a:
                st.markdown(f"**A ({t({'de': 'Stichprobenmittel', 'en': 'Sample Mean'})}):**")
                st.latex(fr"\frac{{{lr['x1']:.1f} + {lr['x2']:.1f}}}{{2}} = {lr['a']:.1f}")
                st.caption(f"{t({'de': 'Fehler', 'en': 'Error'})}: |{lr['a']:.1f} - 50| = **{lr['err_a']:.1f}**")
            with res_b:
                st.markdown(f"**B ({t({'de': 'Gewichtet', 'en': 'Weighted'})}):**")
                st.latex(fr"\frac{{{lr['x1']:.1f}}}{{3}} + \frac{{2 \cdot {lr['x2']:.1f}}}{{3}} = {lr['b']:.1f}")
                st.caption(f"{t({'de': 'Fehler', 'en': 'Error'})}: |{lr['b']:.1f} - 50| = **{lr['err_b']:.1f}**")
            
            winner_color = "#007AFF" if lr["winner"] == "A" else "#FF4B4B"
            st.markdown(f"<div style='text-align: center; font-size: 1.2em;'><strong style='color: {winner_color};'>{lr['winner']} {t({'de': 'gewinnt diese Runde', 'en': 'wins this round'})}!</strong></div>", unsafe_allow_html=True)
    
    # Results
    if st.session_state.sd_rounds > 0:
        total = st.session_state.sd_rounds
        a_wins = st.session_state.sd_a_wins
        b_wins = st.session_state.sd_b_wins
        
        # Scoreboard
        m1, m2, m3 = st.columns(3)
        with m1:
            st.metric(t({"de": "Runden", "en": "Rounds"}), total)
        with m2:
            st.metric(t({"de": "A: Stichprobenmittel", "en": "A: Sample Mean"}), f"{a_wins} ({(a_wins/total)*100:.0f}%)")
        with m3:
            st.metric(t({"de": "B: Gewichtet", "en": "B: Weighted"}), f"{b_wins} ({(b_wins/total)*100:.0f}%)")
    
    # Chart - always show, add lines only when data exists
    fig = go.Figure()
    
    if len(st.session_state.sd_history_a) >= 1:
        rounds = list(range(1, len(st.session_state.sd_history_a) + 1))
        running_avg_a = [np.mean(st.session_state.sd_history_a[:i+1]) for i in range(len(st.session_state.sd_history_a))]
        running_avg_b = [np.mean(st.session_state.sd_history_b[:i+1]) for i in range(len(st.session_state.sd_history_b))]
        
        fig.add_trace(go.Scatter(x=rounds, y=running_avg_a, mode='lines+markers', name='A', line=dict(color='#007AFF', width=2), marker=dict(size=6)))
        fig.add_trace(go.Scatter(x=rounds, y=running_avg_b, mode='lines+markers', name='B', line=dict(color='#FF4B4B', width=2), marker=dict(size=6)))
    
    fig.update_layout(
        title=t({"de": "Durchschnittsfehler", "en": "Average Error"}),
        xaxis_title=t({"de": "Runde", "en": "Round"}),
        yaxis_title=t({"de": "Fehler", "en": "Error"}),
        xaxis=dict(range=[0, max(20, len(st.session_state.sd_history_a) + 5)]),
        yaxis=dict(range=[0, 15]),
        height=200,
        margin=dict(l=40, r=20, t=40, b=30),
        legend=dict(orientation="h", yanchor="bottom", y=-0.25, xanchor="center", x=0.5),
        hovermode=False
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Insight - show when pattern is clear with intuitive explanation
    if st.session_state.sd_rounds >= 10 and st.session_state.sd_a_wins > st.session_state.sd_b_wins:
        total = st.session_state.sd_rounds
        a_wins = st.session_state.sd_a_wins
        with st.container(border=True):
            st.markdown(f"**{t({'de': 'Entdeckung', 'en': 'Discovery'})}:** A {t({'de': 'gewinnt', 'en': 'wins'})} {(a_wins/total)*100:.0f}%!")
            st.markdown(t({
                "de": "**Warum?** Wenn du einem Freund mehr Gewicht gibst (B), gehst du ein Risiko ein: Was wenn genau dieser Freund daneben liegt? Indem du beide gleich gewichtest (A), balancierst du ihre Fehler aus. Keiner dominiert — und im Durchschnitt bist du näher dran.",
                "en": "**Why?** If you weight one friend more (B), you're taking a risk: what if that friend is wrong? By weighting both equally (A), you balance out their errors. Neither dominates — and on average, you're closer to the truth."
            }))


# ============================================================================
# MAIN RENDER FUNCTION
# ============================================================================

def render_subtopic_8_1(model):
    """Render Topic 8.1: Intuitive Heuristic Approaches for Estimators"""
    
    # Title and subtitle
    st.header(t(content_8_1["title"]))
    st.markdown(f"*{t(content_8_1['subtitle'])}*")
    st.markdown("---")
    
    # Inject equal height CSS for side-by-side containers
    inject_equal_height_css()
    
    # =========================================================================
    # SECTION 1: THE BIG PICTURE (Intuition)
    # =========================================================================
    st.markdown(f"### {t({'de': 'Intuition', 'en': 'Intuition'})}")
    
    with st.container(border=True):
        st.markdown(t(content_8_1["intuition"]), unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # =========================================================================
    # SECTION 2: THE THREE KEY ESTIMATORS
    # =========================================================================
    st.markdown(f"### {t(content_8_1['three_estimators']['header'])}")
    st.markdown(t(content_8_1['three_estimators']['intro']))
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Estimator cards in a grid
    est_cols = st.columns(3, gap="medium")
    
    estimators = ["estimator_mean", "estimator_variance", "estimator_proportion"]
    colors = ["#007AFF", "#9B59B6", "#FF4B4B"]
    
    for col, est_key, color in zip(est_cols, estimators, colors):
        est = content_8_1[est_key]
        with col:
            with st.container(border=True):
                st.markdown(f"**{t(est['name'])}**")
                st.latex(est['symbol'])
                st.markdown("---")
                st.markdown(f"*{t({'de': 'Schätzt', 'en': 'Estimates'})}:* {t(est['what_it_estimates'])}")
                st.markdown(f"*{t({'de': 'Wann', 'en': 'When'})}:* {t(est['when_to_use'])}")
                st.caption(f"{t({'de': 'Beispiel', 'en': 'Example'})}: {t(est['example'])}")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Full formulas
    st.markdown(f"#### {t({'de': 'Die vollständigen Formeln', 'en': 'The Complete Formulas'})}")
    
    formula_cols = st.columns(2, gap="medium")
    
    with formula_cols[0]:
        with st.container(border=True):
            st.markdown(f"**{t(content_8_1['estimator_mean']['name'])}** — {t({'de': 'für Populationsmittel μ', 'en': 'for population mean μ'})}")
            st.latex(content_8_1['estimator_mean']['formula'])
            st.markdown("---")
            st.markdown(f"**{t(content_8_1['estimator_variance']['name'])}** — {t({'de': 'für Populationsvarianz σ²', 'en': 'for population variance σ²'})}")
            st.latex(content_8_1['estimator_variance']['formula'])
    
    with formula_cols[1]:
        with st.container(border=True):
            st.markdown(f"**{t(content_8_1['estimator_proportion']['name'])}** — {t({'de': 'für Erfolgswahrscheinlichkeit p', 'en': 'for success probability p'})}")
            # Use bilingual formula
            if t({"de": "x", "en": "y"}) == "y" and "formula_en" in content_8_1['estimator_proportion']:
                st.latex(content_8_1['estimator_proportion']['formula_en'])
            else:
                st.latex(content_8_1['estimator_proportion']['formula'])
            st.markdown("---")
            # Variable decoder
            st.markdown(f"**{t({'de': 'Dabei ist', 'en': 'Where'})}:**")
            st.markdown(f"$n$ = {t({'de': 'Stichprobengrösse', 'en': 'Sample size'})}")
            st.markdown(f"$X_i$ = {t({'de': 'i-ter Stichprobenwert', 'en': 'i-th sample value'})}")
            st.markdown(f"$\\bar{{X}}$ = {t({'de': 'Stichprobenmittel', 'en': 'Sample mean'})}")
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # =========================================================================
    # SECTION 3: HAT NOTATION
    # =========================================================================
    st.markdown(f"### {t(content_8_1['hat_notation']['title'])}")
    
    with st.container(border=True):
        not_cols = st.columns([1, 2])
        
        with not_cols[0]:
            st.markdown(f"""
<div style="display: flex; flex-direction: column; justify-content: center; align-items: center; padding: 70px 0;">
<span style="font-size: 5em; line-height: 1;">θ̂</span>
<em style="margin-top: 12px;">theta-hat</em>
</div>
""", unsafe_allow_html=True)
        
        with not_cols[1]:
            st.markdown(t(content_8_1['hat_notation']['definition']))
            st.markdown("---")
            st.markdown(f"""
| {t({"de": "Symbol", "en": "Symbol"})} | {t({"de": "Bedeutung", "en": "Meaning"})} |
|--------|----------|
| $\\theta$ | {t({"de": "Wahrer (unbekannter) Parameter", "en": "True (unknown) parameter"})} |
| $\\hat{{\\theta}}$ | {t({"de": "Geschätzter Wert aus Stichprobe", "en": "Estimated value from sample"})} |
| $T = t(X_1, \\ldots, X_n)$ | {t({"de": "Schätzfunktion (Zufallsvariable)", "en": "Estimator function (random variable)"})} |
""")
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # =========================================================================
    # SECTION 4: WORKED EXAMPLE
    # =========================================================================
    render_worked_example(
        header=content_8_1["worked_example"]["header"],
        problem=content_8_1["worked_example"]["problem"],
        steps=content_8_1["worked_example"]["steps"],
        answer=content_8_1["worked_example"]["answer"]
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # =========================================================================
    # SECTION 5: KEY INSIGHT
    # =========================================================================
    st.markdown(f"### {t({'de': 'Der Aha-Moment', 'en': 'Key Insight'})}")
    
    with st.container(border=True):
        st.markdown(t(content_8_1["key_insight"]), unsafe_allow_html=True)
        st.markdown("---")
        col_e, col_v = st.columns(2)
        with col_e:
            st.latex(r"E[T] = \mu_T")
            st.caption(t({"de": "Erwartungswert des Schätzers", "en": "Expected value of estimator"}))
        with col_v:
            st.latex(r"V(T) = \sigma_T^2")
            st.caption(t({"de": "Varianz des Schätzers", "en": "Variance of estimator"}))
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # =========================================================================
    # SECTION 6: INTERACTIVE - ESTIMATOR SHOWDOWN
    # =========================================================================
    st.markdown(f"### {t({'de': 'Interaktiv: Schätzer-Duell', 'en': 'Interactive: Estimator Showdown'})}")
    
    estimator_showdown()
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # =========================================================================
    # SECTION 7: FRAG DICH (Ask Yourself)
    # =========================================================================
    render_ask_yourself(
        header=content_8_1["frag_dich"]["header"],
        questions=content_8_1["frag_dich"]["questions"],
        conclusion=content_8_1["frag_dich"]["conclusion"]
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # =========================================================================
    # SECTION 8: EXAM ESSENTIALS
    # =========================================================================
    render_exam_essentials(
        trap=content_8_1["exam_essentials"]["trap"],
        trap_rule=content_8_1["exam_essentials"]["trap_rule"],
        tips=content_8_1["exam_essentials"]["tips"]
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # =========================================================================
    # SECTION 9: MCQ
    # =========================================================================
    st.markdown(f"### {t({'de': 'Prüfungstraining', 'en': 'Exam Practice'})}")
    
    # Get the question
    q = QUESTIONS_8.get("hs2023_mc10")
    if q:
        st.caption(f"Source: {q.get('source', 'Unknown')}")
        
        options = q.get("options", [])
        option_labels = [t({"de": o["de"], "en": o["en"]}) for o in options]
        
        with st.container(border=True):
            render_mcq(
                key_suffix="8_1_unbiased",
                question_text=t(q["question"]),
                options=option_labels,
                correct_idx=q["correct_idx"],
                solution_text_dict=q["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Falsch.", "en": "Incorrect."},
                client=model,
                ai_context="Question about unbiased estimators in point estimation. Tests understanding of E[estimator] = true parameter.",
                course_id="vwl",
                topic_id="8",
                subtopic_id="8.1",
                question_id="8_1_unbiased"
            )
