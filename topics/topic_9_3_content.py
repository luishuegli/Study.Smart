# Topic 9.3: Connection with Hypothesis Tests
# ULTRATHINK Implementation with Feynman Pedagogy
# "The Duality: CI and Test are Two Sides of the Same Coin"

import streamlit as st
import numpy as np
import plotly.graph_objects as go
from scipy import stats
from utils.localization import t
from utils.quiz_helper import render_mcq
from utils.ask_yourself import render_ask_yourself
from utils.exam_essentials import render_exam_essentials
from utils.worked_example import render_worked_example
from utils.layouts.foundation import inject_equal_height_css

# =============================================================================
# CONTENT DICTIONARY (Bilingual)
# =============================================================================
content_9_3 = {
    "title": {"de": "9.3 Zusammenhang mit Hypothesentests", "en": "9.3 Connection with Hypothesis Tests"},
    "subtitle": {
        "de": "Das Geheimnis: KI und Test sind zwei Seiten derselben Münze",
        "en": "The Secret: CI and Test are Two Sides of the Same Coin"
    },
    
    # INTUITION — The Courtroom Analogy (NO math, NO emojis)
    "intuition": {
        "de": """<strong>Die Idee:</strong> Stell dir einen Gerichtssaal vor.

Der Ankläger behauptet: <em>"Der wahre Wert ist genau 100!"</em> (Das ist die Nullhypothese.)

Du hast Beweise gesammelt (deine Stichprobe) und ein Konfidenzintervall berechnet: <strong>[95, 99]</strong>.

Der angeklagte Wert (100) liegt <strong>AUSSERHALB</strong> deines Intervalls.

<strong>Urteil:</strong> Verwirf die Anklage! Die Beweise unterstützen den Wert 100 nicht.

<em>Genau das ist, was ein Hypothesentest auch sagt — ohne extra Rechnung!</em>""",
        "en": """<strong>The Idea:</strong> Imagine a courtroom.

The prosecutor claims: <em>"The true value is exactly 100!"</em> (That's the null hypothesis.)

You collected evidence (your sample) and computed a confidence interval: <strong>[95, 99]</strong>.

The accused value (100) is <strong>OUTSIDE</strong> your interval.

<strong>Verdict:</strong> Reject the claim! The evidence doesn't support 100.

<em>This is exactly what a hypothesis test concludes — no extra calculation needed!</em>"""
    },
    
    # VARIABLE DECODER
    "variables": [
        {"symbol": r"\mu_0", "name": {"de": "Hypothetischer Wert", "en": "Hypothesized Value"}, 
         "desc": {"de": "Der 'Angeklagte' — der Wert, den wir testen", "en": "The 'accused' — the value we're testing"}},
        {"symbol": r"\alpha", "name": {"de": "Signifikanzniveau", "en": "Significance Level"}, 
         "desc": {"de": "Wie streng ist die Jury? (z.B. 5%)", "en": "How strict is the jury? (e.g., 5%)"}},
        {"symbol": r"1-\alpha", "name": {"de": "Konfidenzniveau", "en": "Confidence Level"}, 
         "desc": {"de": "Wie breit ist dein Netz? (z.B. 95%)", "en": "How wide is your net? (e.g., 95%)"}}
    ],
    
    # WORKED EXAMPLE
    "worked_example": {
        "header": {"de": "Beide Wege zum selben Ziel", "en": "Both Paths to the Same Goal"},
        "steps": [
            {
                "label": {"de": "Weg A — KI-Methode", "en": "Path A — CI Method"},
                "latex": r"\text{KI} = \left[ 103 \pm 1.96 \times \frac{16}{8} \right] = [99.08, 106.92]",
                "latex_en": r"\text{CI} = \left[ 103 \pm 1.96 \times \frac{16}{8} \right] = [99.08, 106.92]",
                "note": {"de": "Ist 100 drin? JA → Nicht verwerfen", "en": "Is 100 inside? YES → Don't reject"}
            },
            {
                "label": {"de": "Weg B — Test-Methode", "en": "Path B — Test Method"},
                "latex": r"Z = \frac{103 - 100}{16/8} = \frac{3}{2} = 1.5",
                "note": {"de": "Ist |1.5| > 1.96? NEIN → Nicht verwerfen", "en": "Is |1.5| > 1.96? NO → Don't reject"}
            }
        ],
        "answer": {
            "de": "Beide Methoden sagen: H₀ nicht verwerfen!",
            "en": "Both methods say: Do not reject H₀!"
        }
    },
    
    # ASK YOURSELF
    "frag_dich": {
        "header": {"de": "Frag dich: Verstehst du die Dualität?", "en": "Ask yourself: Do you understand the duality?"},
        "questions": [
            {"de": "Dein 95%-KI ist [82, 94]. H₀ sagt μ = 90. Verwirfst du?", 
             "en": "Your 95% CI is [82, 94]. H₀ says μ = 90. Do you reject?"},
            {"de": "Dein 95%-KI ist [82, 94]. H₀ sagt μ = 100. Verwirfst du?", 
             "en": "Your 95% CI is [82, 94]. H₀ says μ = 100. Do you reject?"},
            {"de": "Du verwirfst H₀ bei α = 5%. Was verrät dir dein KI über μ₀?", 
             "en": "You reject H₀ at α = 5%. What does your CI tell you about μ₀?"},
            {"de": "Warum stimmen beide Methoden IMMER überein?", 
             "en": "Why do both methods ALWAYS agree?"}
        ],
        "conclusion": {
            "de": "Antworten: Nein (90 drin), Ja (100 draussen), μ₀ draussen, Gleicher Z-Wert!",
            "en": "Answers: No (90 inside), Yes (100 outside), μ₀ outside, Same Z-score!"
        }
    },
    
    # EXAM ESSENTIALS
    "exam_essentials": {
        "trap": {
            "de": "95%-KI mit 1%-Test vergleichen (oder umgekehrt)! Die Niveaus müssen übereinstimmen.",
            "en": "Comparing 95% CI with 1% test (or vice versa)! The levels must match."
        },
        "trap_rule": {
            "de": "Regel: α + Konfidenzniveau = 1. IMMER.",
            "en": "Rule: α + confidence level = 1. ALWAYS."
        },
        "tips": [
            {
                "tip": {"de": "Schnelltest via KI", "en": "Quick test via CI"},
                "why": {"de": "KI schon da? μ₀ ausserhalb → sofort verwerfen, gleiche Antwort wie Test", "en": "CI already computed? μ₀ outside → reject immediately, same answer as test"}
            },
            {
                "tip": {"de": "Niveaus matchen!", "en": "Match the levels!"},
                "why": {"de": "95%-KI geht mit 5%-Test. 99%-KI geht mit 1%-Test.", "en": "95% CI goes with 5% test. 99% CI goes with 1% test."}
            }
        ]
    },
    
    # MCQ
    "mcq": {
        "question": {
            "de": "Ein 99%-Konfidenzintervall für μ ist [85, 95]. Bei einem Test mit Signifikanzniveau α = 1% testen Sie H₀: μ = 92. Welches ist die korrekte Testentscheidung?",
            "en": "A 99% confidence interval for μ is [85, 95]. At significance level α = 1%, you test H₀: μ = 92. What is the correct test decision?"
        },
        "options": [
            {"de": "H₀ verwerfen", "en": "Reject H₀"},
            {"de": "H₀ nicht verwerfen", "en": "Do not reject H₀"},
            {"de": "Nicht genügend Informationen", "en": "Not enough information"},
            {"de": "Hängt von der Stichprobengrösse ab", "en": "Depends on sample size"}
        ],
        "correct_idx": 1,
        "solution": {
            "de": "<strong>Richtig: (b) H₀ nicht verwerfen</strong><br>Der Wert μ₀ = 92 liegt INNERHALB des 99%-KI [85, 95]. Bei der Dualität: 99%-KI entspricht α = 1% Test. Da 92 im Intervall liegt, wird H₀ NICHT verworfen.",
            "en": "<strong>Correct: (b) Do not reject H₀</strong><br>The value μ₀ = 92 lies INSIDE the 99% CI [85, 95]. By duality: 99% CI corresponds to α = 1% test. Since 92 is in the interval, H₀ is NOT rejected."
        }
    }
}


# =============================================================================
# INTERACTIVE: Simplified "Verdict Detector" — Clean visualization
# =============================================================================

@st.fragment
def verdict_detector_interactive():
    """Interactive: Move μ₀ and watch both verdicts update together"""
    
    # State initialization
    if "vd_mu0" not in st.session_state:
        st.session_state.vd_mu0 = 500
    if "vd_confidence_idx" not in st.session_state:
        st.session_state.vd_confidence_idx = 1  # 95%
    
    # Fixed sample parameters
    x_bar = 502  # Sample mean (fixed)
    sigma = 12   # Known standard deviation
    n = 50       # Sample size
    se = sigma / np.sqrt(n)  # Standard error ≈ 1.70
    
    # Confidence level options
    confidence_options = ["90%", "95%", "99%"]
    z_values = [1.645, 1.96, 2.576]
    alpha_values = [0.10, 0.05, 0.01]
    
    # Blue slider CSS for μ₀ control
    from utils.layouts.foundation import inject_slider_css
    inject_slider_css([
        {"label_contains": "Wert", "color": "#007AFF"},
        {"label_contains": "value", "color": "#007AFF"},
    ])
    
    # Controls in columns
    c1, c2 = st.columns([1.5, 1])
    
    with c1:
        st.markdown(f"**{t({'de': 'Behaupteter Wert', 'en': 'Claimed Value'})}** $\\mu_0$")
        mu0 = st.slider(
            t({"de": "Wert verschieben", "en": "Move value"}),
            min_value=490, max_value=515, value=st.session_state.vd_mu0,
            key="vd_mu0_slider",
            label_visibility="collapsed"
        )
        st.session_state.vd_mu0 = mu0
    
    with c2:
        st.markdown(f"**{t({'de': 'Konfidenzniveau', 'en': 'Confidence Level'})}**")
        btn_cols = st.columns(3)
        for i, (col, opt) in enumerate(zip(btn_cols, confidence_options)):
            with col:
                is_selected = st.session_state.vd_confidence_idx == i
                if is_selected:
                    st.markdown(f'''<div style="background:#000;color:#fff;
                        padding:8px 12px;border-radius:20px;text-align:center;
                        font-weight:500;font-size:0.9em;">{opt}</div>''', 
                        unsafe_allow_html=True)
                else:
                    if st.button(opt, key=f"vd_conf_{i}", use_container_width=True):
                        st.session_state.vd_confidence_idx = i
                        st.rerun(scope="fragment")
    
    # Calculate values
    conf_idx = st.session_state.vd_confidence_idx
    z_crit = z_values[conf_idx]
    alpha = alpha_values[conf_idx]
    
    ci_lower = x_bar - z_crit * se
    ci_upper = x_bar + z_crit * se
    
    is_inside = ci_lower <= mu0 <= ci_upper
    z_score = (x_bar - mu0) / se
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Display current values as LaTeX (separate from chart for clarity)
    col_info1, col_info2 = st.columns(2)
    with col_info1:
        st.latex(rf"\bar{{x}} = {x_bar} \quad \text{{(Sample Mean)}}")
    with col_info2:
        st.latex(rf"\text{{CI}} = [{ci_lower:.1f}, {ci_upper:.1f}]")
    
    # SIMPLIFIED VISUALIZATION — Just show the verdict visually
    verdict_color = "#16a34a" if is_inside else "#FF4B4B"
    verdict_bg = "rgba(22, 163, 74, 0.1)" if is_inside else "rgba(255, 75, 75, 0.1)"
    
    # Single clear verdict display
    inject_equal_height_css()
    
    col_ci, col_test = st.columns(2, gap="medium")
    
    with col_ci:
        verdict_ci = t({"de": "INNERHALB", "en": "INSIDE"}) if is_inside else t({"de": "AUSSERHALB", "en": "OUTSIDE"})
        st.markdown(f"""
<div style="background: {verdict_bg}; border: 2px solid {verdict_color}; 
            padding: 20px; border-radius: 12px; text-align: center;">
<div style="color: #6B7280; font-size: 0.9em; margin-bottom: 8px;">{t({"de": "KI-Methode", "en": "CI Method"})}</div>
<div style="color: {verdict_color}; font-size: 1.4em; font-weight: 700;">μ₀ = {mu0}</div>
<div style="color: {verdict_color}; font-size: 1.1em; margin-top: 8px;">{verdict_ci} [{ci_lower:.1f}, {ci_upper:.1f}]</div>
</div>
""", unsafe_allow_html=True)
    
    with col_test:
        verdict_test = t({"de": "NICHT verwerfen", "en": "Don't reject"}) if is_inside else t({"de": "VERWERFEN", "en": "REJECT"})
        z_comparison = "<" if is_inside else ">"
        st.markdown(f"""
<div style="background: {verdict_bg}; border: 2px solid {verdict_color}; 
            padding: 20px; border-radius: 12px; text-align: center;">
<div style="color: #6B7280; font-size: 0.9em; margin-bottom: 8px;">{t({"de": "Test-Methode", "en": "Test Method"})}</div>
<div style="color: {verdict_color}; font-size: 1.4em; font-weight: 700;">H₀ {verdict_test}</div>
<div style="color: #6B7280; font-size: 0.9em; margin-top: 8px;">|Z| = {abs(z_score):.2f} {z_comparison} {z_crit}</div>
</div>
""", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Discovery debrief
    if not is_inside:
        st.success(t({
            "de": "Sobald μ₀ das Intervall verlässt, wechseln BEIDE Urteile zu 'Verwerfen'. Das ist die Dualität!",
            "en": "As soon as μ₀ exits the interval, BOTH verdicts switch to 'Reject'. That's the duality!"
        }))


# =============================================================================
# MAIN RENDER FUNCTION
# =============================================================================

def render_subtopic_9_3(model):
    """9.3 Zusammenhang mit Hypothesentests"""
    
    st.header(t(content_9_3["title"]))
    st.caption(t(content_9_3["subtitle"]))
    st.markdown("---")
    
    # =========================================================================
    # INTUITION — The Courtroom (No math, no emojis)
    # =========================================================================
    st.markdown(f"### {t({'de': 'Die Idee', 'en': 'The Idea'})}")
    
    with st.container(border=True):
        st.markdown(t(content_9_3["intuition"]), unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # =========================================================================
    # THE DUALITY RULE — with proper LaTeX
    # =========================================================================
    st.markdown(f"### {t({'de': 'Die Dualitätsregel', 'en': 'The Duality Rule'})}")
    
    with st.container(border=True):
        # The rule in prose
        st.markdown(t({
            "de": "Bei Signifikanzniveau α wird die Nullhypothese **verworfen**, genau dann, wenn:",
            "en": "At significance level α, the null hypothesis is **rejected** if and only if:"
        }))
        
        # The formula in proper LaTeX
        st.latex(r"\mu_0 \text{ liegt } \textbf{AUSSERHALB} \text{ des } (1-\alpha)\text{-KI}" if t({"de": "de", "en": "en"}) == "de" else r"\mu_0 \text{ is } \textbf{OUTSIDE} \text{ the } (1-\alpha)\text{ CI}")
        
        st.markdown("")
        
        # Variable Decoder
        st.markdown("---")
        st.markdown(f"**{t({'de': 'Variablen', 'en': 'Variables'})}:**")
        for var in content_9_3["variables"]:
            st.markdown(f"• ${var['symbol']}$ = **{t(var['name'])}** — {t(var['desc'])}")
        
        # Key Insight with proper LaTeX separation
        st.markdown("---")
        st.markdown(f"**{t({'de': 'Aha-Moment', 'en': 'Key Insight'})}:**")
        st.markdown(t({
            "de": "Beide Methoden verwenden **denselben Z-Wert**:",
            "en": "Both methods use the **same Z-score**:"
        }))
        st.latex(r"Z = \frac{\bar{x} - \mu_0}{\sigma / \sqrt{n}}")
        st.markdown(t({
            "de": "• Test fragt: Ist |Z| > z_krit?  • KI fragt: Ist μ₀ ausserhalb?  → **Gleiche Antwort!**",
            "en": "• Test asks: Is |Z| > z_crit?  • CI asks: Is μ₀ outside?  → **Same answer!**"
        }))
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # =========================================================================
    # SIDE-BY-SIDE COMPARISON — with proper LaTeX
    # =========================================================================
    inject_equal_height_css()
    
    st.markdown(f"### {t({'de': 'Zwei Wege, Eine Antwort', 'en': 'Two Paths, One Answer'})}")
    
    col_left, col_right = st.columns(2, gap="medium")
    
    with col_left:
        with st.container(border=True):
            st.markdown(f"**{t({'de': 'Hypothesentest-Ansatz', 'en': 'Hypothesis Test Approach'})}**")
            st.markdown(t({"de": "**1.** Stelle Hypothese auf:", "en": "**1.** State hypothesis:"}))
            st.latex(r"H_0: \mu = \mu_0")
            st.markdown(t({"de": "**2.** Berechne:", "en": "**2.** Calculate:"}))
            st.latex(r"Z = \frac{\bar{x} - \mu_0}{SE}")
            st.markdown(t({"de": "**3.** Vergleiche |Z| mit kritischem Wert", "en": "**3.** Compare |Z| to critical value"}))
            st.markdown(t({"de": "**4.** |Z| > z_krit → Verwirf H₀", "en": "**4.** |Z| > z_crit → Reject H₀"}))
            st.markdown("")
    
    with col_right:
        with st.container(border=True):
            st.markdown(f"**{t({'de': 'Konfidenzintervall-Ansatz', 'en': 'Confidence Interval Approach'})}**")
            st.markdown(t({"de": "**1.** Berechne KI:", "en": "**1.** Calculate CI:"}))
            st.latex(r"\left[\bar{x} \pm z_{1-\alpha/2} \cdot SE\right]")
            st.markdown(t({"de": "**2.** Prüfe Position von μ₀", "en": "**2.** Check position of μ₀"}))
            st.markdown(t({"de": "**3.** Innerhalb → Nicht verwerfen", "en": "**3.** Inside → Don't reject"}))
            st.markdown(t({"de": "**4.** Ausserhalb → Verwirf H₀", "en": "**4.** Outside → Reject H₀"}))
            st.markdown("")
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # =========================================================================
    # INTERACTIVE — The Verdict Detector
    # =========================================================================
    st.markdown(f"### {t({'de': 'Interaktiv: Der Urteils-Detektor', 'en': 'Interactive: The Verdict Detector'})}")
    
    # Scenario
    st.markdown(f"""
<div style="background: #f4f4f5; border-left: 4px solid #a1a1aa; padding: 12px 16px; border-radius: 8px; color: #3f3f46;">
<strong>{t({"de": "Szenario", "en": "Scenario"})}:</strong> {t({"de": "Eine Fabrik behauptet μ₀ = 500g. Du misst n = 50 Pakete und berechnest x̄ = 502g.", "en": "A factory claims μ₀ = 500g. You measure n = 50 packages and calculate x̄ = 502g."})}
</div>
""", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(t({
        "de": "**Mission:** Bewege μ₀ und beobachte: Beide Urteile wechseln **synchron**!",
        "en": "**Mission:** Move μ₀ and observe: Both verdicts switch **in sync**!"
    }))
    st.markdown("<br>", unsafe_allow_html=True)
    
    verdict_detector_interactive()
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # =========================================================================
    # WORKED EXAMPLE — with proper LaTeX
    # =========================================================================
    st.markdown(f"### {t(content_9_3['worked_example']['header'])}")
    
    with st.container(border=True):
        st.markdown(t({
            "de": "**Problem:** Eine Fabrik behauptet μ = 100g. Du misst n = 64, erhältst x̄ = 103g, σ = 16g. Teste bei α = 5%.",
            "en": "**Problem:** A factory claims μ = 100g. You measure n = 64, get x̄ = 103g, σ = 16g. Test at α = 5%."
        }))
        
        st.markdown("---")
        
        for step in content_9_3["worked_example"]["steps"]:
            st.markdown(f"**{t(step['label'])}**")
            # Use language-appropriate LaTeX if available
            latex_formula = step.get('latex_en', step['latex']) if t({"de": "de", "en": "en"}) == "en" else step['latex']
            st.latex(latex_formula)
            st.markdown(f"*{t(step['note'])}*")
            st.markdown("")
        
        st.markdown("---")
        st.success(t(content_9_3["worked_example"]["answer"]))
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # =========================================================================
    # ASK YOURSELF
    # =========================================================================
    render_ask_yourself(
        header=content_9_3["frag_dich"]["header"],
        questions=content_9_3["frag_dich"]["questions"],
        conclusion=content_9_3["frag_dich"]["conclusion"]
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # =========================================================================
    # EXAM ESSENTIALS
    # =========================================================================
    render_exam_essentials(
        trap=content_9_3["exam_essentials"]["trap"],
        trap_rule=content_9_3["exam_essentials"]["trap_rule"],
        tips=content_9_3["exam_essentials"]["tips"]
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # =========================================================================
    # EXAM PRACTICE (MCQ)
    # =========================================================================
    st.markdown(f"### {t({'de': 'Prüfungstraining', 'en': 'Exam Practice'})}")
    st.caption("Study.Smart — CI/Test Duality")
    
    mcq = content_9_3["mcq"]
    opts = mcq["options"]
    opt_labels = [t(o) for o in opts]
    
    render_mcq(
        key_suffix="9_3_duality",
        question_text=t(mcq["question"]),
        options=opt_labels,
        correct_idx=mcq["correct_idx"],
        solution_text_dict=mcq["solution"],
        success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
        error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
        client=model,
        ai_context="Testing understanding of CI-Hypothesis Test duality",
        course_id="vwl",
        topic_id="9",
        subtopic_id="9.3",
        question_id="9_3_duality"
    )
