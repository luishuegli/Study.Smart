# Topic 8.2: Properties of Point Estimators
# Fixed implementation with all rules applied

import streamlit as st
import numpy as np
import plotly.graph_objects as go
from utils.localization import t
from utils.layouts.foundation import grey_info, key_insight, inject_equal_height_css
from utils.layouts import render_comparison
from utils.quiz_helper import render_mcq
from utils.ask_yourself import render_ask_yourself
from utils.exam_essentials import render_exam_essentials
from data.exam_questions import get_question

# =============================================================================
# CONTENT DICTIONARY (Bilingual)
# =============================================================================
content_8_2 = {
    "title": {"de": "8.2 Eigenschaften von Punktschätzungen", "en": "8.2 Properties of Point Estimators"},
    "subtitle": {"de": "Wie beurteilen wir die Qualität eines Schätzers?", "en": "How do we judge the quality of an estimator?"},
    
    # 4 Friends Intuition
    "intuition_header": {"de": "Die 4 Eigenschaften eines guten Schätzers", "en": "The 4 Properties of a Good Estimator"},
    "intuition_intro": {
        "de": "Stell dir vor, du fragst Freunde, wie gross du bist. Jeder misst dich und gibt dir eine Schätzung. Welche Eigenschaften sollte ein guter 'Schätz-Freund' haben?",
        "en": "Imagine asking friends to estimate your height. Each one measures you and gives an estimate. What properties should a good 'estimator friend' have?"
    },
    "friend_honest": {
        "de": "**Der Ehrliche** — Trifft im Durchschnitt den wahren Wert (Erwartungstreue)",
        "en": "**The Honest One** — Hits the true value on average (Unbiasedness)"
    },
    "friend_learning": {
        "de": "**Der Lernende** — Wird mit der Zeit immer ehrlicher (Asymptotische Erwartungstreue)",
        "en": "**The Learner** — Gets more honest over time (Asymptotic Unbiasedness)"
    },
    "friend_reliable": {
        "de": "**Der Zuverlässige** — Schätzungen werden mit mehr Daten immer genauer (Konsistenz)",
        "en": "**The Reliable One** — Estimates get more precise with more data (Consistency)"
    },
    "friend_sharp": {
        "de": "**Der Präzise** — Hat unter allen ehrlichen Freunden die engsten Schätzungen (Effizienz)",
        "en": "**The Sharp One** — Among honest friends, has the tightest estimates (Efficiency)"
    },
    "intuition_summary": {
        "de": "Alle 4 Eigenschaften beantworten: **Kann ich diesem Schätzer vertrauen?**",
        "en": "All 4 properties answer: **Can I trust this estimator?**"
    },
    
    # Section A: Unbiasedness
    "section_a_title": {"de": "Erwartungstreue (Unbiasedness)", "en": "Unbiasedness"},
    "unbiased_definition": {
        "de": "Eine Schätzfunktion T heisst **erwartungstreu** für den Parameter θ, wenn der Erwartungswert des Schätzers gleich dem wahren Parameter ist.",
        "en": "An estimator T is called **unbiased** for the parameter θ if the expected value of the estimator equals the true parameter."
    },
    "bias_definition": {
        "de": "Die **Verzerrung (Bias)** misst den systematischen Fehler:",
        "en": "The **Bias** measures the systematic error:"
    },
    "unbiased_insight": {
        "de": "Der Stichprobenmittelwert ist erwartungstreu für den Populationsmittelwert, weil jede Beobachtung denselben Erwartungswert hat und Durchschnittsbildung das nicht ändert.",
        "en": "The sample mean is unbiased for the population mean because each observation has the same expected value, and averaging doesn't change that."
    },
    
    # Section B: Asymptotic Unbiasedness
    "section_b_title": {"de": "Asymptotische Erwartungstreue", "en": "Asymptotic Unbiasedness"},
    "asymp_definition": {
        "de": "Wenn die Verzerrung mit zunehmendem Stichprobenumfang gegen Null geht, heisst der Schätzer **asymptotisch erwartungstreu**.",
        "en": "If the bias approaches zero as sample size increases, the estimator is called **asymptotically unbiased**."
    },
    
    # Section C: n vs n-1
    "section_c_title": {"de": "Der n vs (n-1) Trick", "en": "The n vs (n-1) Trick"},
    
    # Section D: Consistency  
    "section_d_title": {"de": "Konsistenz", "en": "Consistency"},
    "consistency_definition": {
        "de": "Eine Schätzfunktion ist **konsistent**, wenn sie mit wachsender Stichprobengrösse stochastisch gegen den wahren Parameter konvergiert.",
        "en": "An estimator is **consistent** if it converges in probability to the true parameter as sample size grows."
    },
    "consistency_cond1": {
        "de": "Erwartungstreu ist (mindestens asymptotisch)",
        "en": "Unbiased (at least asymptotically)"
    },
    "consistency_cond2": {
        "de": "Seine Varianz gegen Null geht für n gegen unendlich",
        "en": "Its variance goes to zero as n approaches infinity"
    },
    
    # Section E: Efficiency
    "section_e_title": {"de": "Effizienz", "en": "Efficiency"},
    "efficiency_definition": {
        "de": "Unter allen erwartungstreuen Schätzern ist jener **effizient**, der die kleinste Varianz hat.",
        "en": "Among all unbiased estimators, the one with the **smallest variance** is called efficient."
    },
    "efficiency_insight": {
        "de": "Effizienz vergleicht NUR erwartungstreue Schätzer! Ein verzerrter Schätzer kann kleinere Varianz haben, ist aber trotzdem nicht effizient.",
        "en": "Efficiency only compares unbiased estimators! A biased estimator may have smaller variance but is still not efficient."
    },
    
    # Interactive missions
    "mission_consistency": {"de": "Mission: Konsistenz erleben", "en": "Mission: Experience Consistency"},
    "mission_efficiency": {"de": "Mission: Effizienz-Showdown", "en": "Mission: Efficiency Showdown"},
}

# =============================================================================
# INTERACTIVE ELEMENTS
# =============================================================================

@st.fragment
def consistency_visualizer():
    """Interactive: Shows how distribution shrinks as n increases"""
    
    # Use on_change pattern to prevent slider jumping
    if "cons_n" not in st.session_state:
        st.session_state.cons_n = 10
    
    def update_n():
        st.session_state.cons_n = st.session_state._cons_slider_temp
    
    st.markdown(f"**{t({'de': 'Beobachte, wie dein Schätzer ZUVERLÄSSIGER wird', 'en': 'Watch how your estimator gets MORE RELIABLE'})}**")
    
    # Scenario box
    grey_info(t({
        "de": "<strong>Szenario:</strong> Du schätzt die durchschnittliche Lieferzeit einer Pizzeria (wahrer Wert: 30 min). Mit jeder zusätzlichen Beobachtung wird dein Schätzer präziser.",
        "en": "<strong>Scenario:</strong> You're estimating a pizzeria's average delivery time (true value: 30 min). Each additional observation makes your estimate more precise."
    }))
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Blue slider CSS (semantic: n = sample size)
    st.markdown("""
<style>
.stSlider div[data-baseweb="slider"] > div:first-child > div:first-child { background-color: #007AFF !important; }
.stSlider div[role="slider"] { background-color: #FFFFFF !important; border: 2px solid #007AFF !important; }
</style>
""", unsafe_allow_html=True)
    
    # Slider with on_change callback
    st.slider(
        t({"de": "Stichprobengrösse n", "en": "Sample size n"}),
        min_value=5, max_value=100, value=st.session_state.cons_n,
        key="_cons_slider_temp",
        on_change=update_n
    )
    n_val = st.session_state.cons_n
    
    # Parameters
    true_theta = 30  # True delivery time
    sigma = 10       # Population standard deviation
    se = sigma / np.sqrt(n_val)  # Standard error
    
    # Generate x values for distribution
    x = np.linspace(true_theta - 4*sigma/np.sqrt(5), true_theta + 4*sigma/np.sqrt(5), 200)
    y = (1 / (se * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - true_theta) / se) ** 2)
    
    # Create Plotly figure
    fig = go.Figure()
    
    # Add distribution curve
    fig.add_trace(go.Scatter(
        x=x, y=y,
        mode='lines',
        fill='tozeroy',
        fillcolor='rgba(0, 122, 255, 0.3)',
        line=dict(color='#007AFF', width=2),
        name=t({"de": "Verteilung von X̄", "en": "Distribution of X̄"})
    ))
    
    # Add vertical line at true theta
    fig.add_vline(x=true_theta, line_dash="dash", line_color="#007AFF", line_width=2,
                  annotation_text=f"θ = {true_theta}", annotation_position="top")
    
    fig.update_layout(
        height=250,
        margin=dict(l=20, r=20, t=30, b=20),
        xaxis_title=t({"de": "Geschätzte Lieferzeit (min)", "en": "Estimated delivery time (min)"}),
        yaxis_title=t({"de": "Dichte", "en": "Density"}),
        showlegend=False,
        xaxis=dict(range=[true_theta - 15, true_theta + 15]),
    )
    
    st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
    
    # Live feedback - use proper formatting with border-left
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
<div style="background: #f4f4f5; border-left: 4px solid #a1a1aa; padding: 12px 16px; border-radius: 8px; text-align: center; color: #3f3f46;">
<strong>{t({"de": "Standardfehler", "en": "Standard Error"})}</strong><br>
SE = {se:.2f}
</div>
""", unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
<div style="background: #f4f4f5; border-left: 4px solid #a1a1aa; padding: 12px 16px; border-radius: 8px; text-align: center; color: #3f3f46;">
<strong>{t({"de": "95% der Schätzungen", "en": "95% of estimates"})}</strong><br>
{t({"de": "innerhalb", "en": "within"})} <strong>±{1.96*se:.2f}</strong>
</div>
""", unsafe_allow_html=True)
    
    # Completion insight
    if n_val >= 50:
        st.markdown("<br>", unsafe_allow_html=True)
        st.success(t({
            "de": "Siehst du, wie eng die Kurve wird? DAS ist Konsistenz — mehr Daten bedeuten zuverlässigere Schätzungen! Die Varianz geht gegen Null.",
            "en": "See how tight the curve gets? THAT'S consistency — more data means more reliable estimates! The variance approaches zero."
        }))



# =============================================================================
# MAIN RENDER FUNCTION
# =============================================================================

def render_subtopic_8_2(model):
    """8.2 Eigenschaften von Punktschätzungen"""
    
    st.header(t(content_8_2["title"]))
    st.caption(t(content_8_2["subtitle"]))
    st.markdown("---")
    
    # =========================================================================
    # INTUITION: The 4 Friends
    # =========================================================================
    st.markdown(f"### {t(content_8_2['intuition_header'])}")
    
    with st.container(border=True):
        st.markdown(t(content_8_2["intuition_intro"]))
        st.markdown("<br>", unsafe_allow_html=True)
        
        # 4 friends with semantic colors (Blue, Purple, Gray, Red only)
        st.markdown(f"<span style='color: #007AFF;'>{t(content_8_2['friend_honest'])}</span>", unsafe_allow_html=True)
        st.markdown(f"<span style='color: #9B59B6;'>{t(content_8_2['friend_learning'])}</span>", unsafe_allow_html=True)
        st.markdown(f"<span style='color: #6B7280;'>{t(content_8_2['friend_reliable'])}</span>", unsafe_allow_html=True)
        st.markdown(f"<span style='color: #FF4B4B;'>{t(content_8_2['friend_sharp'])}</span>", unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(t(content_8_2["intuition_summary"]))
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # =========================================================================
    # SECTION A: Unbiasedness
    # =========================================================================
    st.markdown(f"### {t(content_8_2['section_a_title'])}")
    
    with st.container(border=True):
        # Title + Definition
        st.markdown(f"**{t({'de': 'Erwartungstreue', 'en': 'Unbiasedness'})}**")
        st.markdown(f"*{t(content_8_2['unbiased_definition'])}*")
        
        # Formula
        st.latex(r"E[T] = \theta")
        
        # Variable Decoder (inside container)
        st.markdown("---")
        st.markdown(f"**{t({'de': 'Variablen', 'en': 'Variables'})}:**")
        st.markdown(f"• $T$ = **{t({'de': 'Schätzfunktion', 'en': 'Estimator'})}** — {t({'de': 'Die Formel, die wir zur Schätzung verwenden', 'en': 'The formula we use to estimate'})}")
        st.markdown(fr"• $\theta$ = **{t({'de': 'Wahrer Parameter', 'en': 'True parameter'})}** — {t({'de': 'Der unbekannte Wert in der Population', 'en': 'The unknown value in the population'})}")
        st.markdown(f"• $E[T]$ = **{t({'de': 'Erwartungswert', 'en': 'Expected value'})}** — {t({'de': 'Durchschnitt über alle möglichen Stichproben', 'en': 'Average over all possible samples'})}")
        
        # Bias formula (INSIDE container)
        st.markdown("---")
        st.markdown(f"**{t(content_8_2['bias_definition'])}**")
        st.latex(r"\text{Bias} = \theta - E[T]")
        st.markdown(t({
            "de": "Wenn Bias = 0, dann ist der Schätzer **erwartungstreu**.",
            "en": "If Bias = 0, the estimator is **unbiased**."
        }))
        
        # Key insight (INSIDE container)
        st.markdown("---")
        st.markdown(f"**{t({'de': 'Aha-Moment', 'en': 'Key Insight'})}:** {t(content_8_2['unbiased_insight'])}")
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # =========================================================================
    # SECTION B: Asymptotic Unbiasedness
    # =========================================================================
    st.markdown(f"### {t(content_8_2['section_b_title'])}")
    
    with st.container(border=True):
        # Title + Definition
        st.markdown(f"**{t({'de': 'Asymptotische Erwartungstreue', 'en': 'Asymptotic Unbiasedness'})}**")
        st.markdown(f"*{t(content_8_2['asymp_definition'])}*")
        
        # Formula
        st.latex(r"\lim_{n \to \infty} E[T_n] = \theta")
        
        # Variable Decoder (inside container)
        st.markdown("---")
        st.markdown(f"**{t({'de': 'Variablen', 'en': 'Variables'})}:**")
        st.markdown(f"• $n$ = **{t({'de': 'Stichprobengrösse', 'en': 'Sample size'})}**")
        st.markdown(f"• $T_n$ = **{t({'de': 'Schätzer bei n Beobachtungen', 'en': 'Estimator with n observations'})}**")
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # =========================================================================
    # SECTION C: Variance Bias (n vs n-1)
    # =========================================================================
    st.markdown(f"### {t(content_8_2['section_c_title'])}")
    
    render_comparison(
        title={"de": "Stichprobenvarianz: Verzerrt vs. Unverzerrt", "en": "Sample Variance: Biased vs. Unbiased"},
        left={
            "title": {"de": "S² (VERZERRT)", "en": "S² (BIASED)"},
            "formula": r"S^2 = \frac{1}{n} \sum_{i=1}^{n}(X_i - \bar{X})^2",
            "insight": {
                "de": "Unterschätzt systematisch!",
                "en": "Systematically underestimates!"
            }
        },
        right={
            "title": {"de": "S²ₙ₋₁ (UNVERZERRT)", "en": "S²ₙ₋₁ (UNBIASED)"},
            "formula": r"S^2_{n-1} = \frac{1}{n-1} \sum_{i=1}^{n}(X_i - \bar{X})^2",
            "insight": {
                "de": "Trifft den wahren Wert!",
                "en": "Hits the true value!"
            }
        },
        show_header=False
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # =========================================================================
    # SECTION D: Consistency
    # =========================================================================
    st.markdown(f"### {t(content_8_2['section_d_title'])}")
    
    with st.container(border=True):
        # Title + Definition
        st.markdown(f"**{t({'de': 'Konsistenz', 'en': 'Consistency'})}**")
        st.markdown(f"*{t(content_8_2['consistency_definition'])}*")
        
        # Formula
        st.latex(r"\hat{\theta}_n \xrightarrow{P} \theta \quad \text{as } n \to \infty")
        
        # Variable Decoder (inside container)
        st.markdown("---")
        st.markdown(f"**{t({'de': 'Variablen', 'en': 'Variables'})}:**")
        st.markdown(fr"• $\hat{{\theta}}_n$ = **{t({'de': 'Schätzer', 'en': 'Estimator'})}** — {t({'de': 'basierend auf n Beobachtungen', 'en': 'based on n observations'})}")
        st.markdown(fr"• $\xrightarrow{{P}}$ = **{t({'de': 'Konvergiert stochastisch', 'en': 'Converges in probability'})}**")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Theorem box
    with st.container(border=True):
        st.markdown(f"**{t({'de': 'Theorem: Bedingungen für Konsistenz', 'en': 'Theorem: Conditions for Consistency'})}**")
        st.markdown(f"1. {t(content_8_2['consistency_cond1'])}")
        st.markdown(f"2. {t(content_8_2['consistency_cond2'])}")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Interactive: Consistency Visualizer - Header OUTSIDE
    st.markdown(f"#### {t(content_8_2['mission_consistency'])}")
    with st.container(border=True):
        consistency_visualizer()
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # =========================================================================
    # SECTION E: Efficiency
    # =========================================================================
    st.markdown(f"### {t(content_8_2['section_e_title'])}")
    
    with st.container(border=True):
        # Title + Definition
        st.markdown(f"**{t({'de': 'Effizienz', 'en': 'Efficiency'})}**")
        st.markdown(f"*{t(content_8_2['efficiency_definition'])}*")
        
        # Formula
        st.latex(r"\text{Var}(T) \leq \text{Var}(U_k) \quad \forall \text{ unbiased } U_k")
        
        # Variable Decoder (inside container)
        st.markdown("---")
        st.markdown(f"**{t({'de': 'Variablen', 'en': 'Variables'})}:**")
        st.markdown(f"• $T$ = **{t({'de': 'Effizientester Schätzer', 'en': 'Most efficient estimator'})}**")
        st.markdown(f"• $U_k$ = **{t({'de': 'Alle anderen erwartungstreuen Schätzer', 'en': 'All other unbiased estimators'})}**")
        
        # Key insight (inside container)
        st.markdown("---")
        st.markdown(f"**{t({'de': 'Aha-Moment', 'en': 'Key Insight'})}:** {t(content_8_2['efficiency_insight'])}")
        
        # Tip (inside container)
        st.markdown("---")
        st.markdown(t({
            "de": "**Tipp:** Das interaktive Effizienz-Duell findest du in Abschnitt 8.1 — dort kannst du sehen, warum gleiche Gewichte gewinnen!",
            "en": "**Tip:** The interactive Efficiency Showdown is in Section 8.1 — see there why equal weights win!"
        }))
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # =========================================================================
    # FRAG DICH (Ask Yourself)
    # =========================================================================
    render_ask_yourself(
        header={"de": "Frag dich selbst", "en": "Ask Yourself"},
        questions=[
            {"de": "Welche Eigenschaft bedeutet: Erwartungswert des Schätzers = wahrer Parameter?", "en": "Which property means: expected value of estimator = true parameter?"},
            {"de": "Warum teilen wir durch (n-1) statt n bei der Stichprobenvarianz?", "en": "Why do we divide by (n-1) instead of n for sample variance?"},
            {"de": "Was unterscheidet Konsistenz von Erwartungstreue?", "en": "What distinguishes consistency from unbiasedness?"},
            {"de": "Kann ein Schätzer konsistent aber verzerrt sein?", "en": "Can an estimator be consistent but biased?"},
        ],
        conclusion={"de": "Ja zu allen? Du hast 8.2 gemeistert!", "en": "Yes to all? You've mastered 8.2!"}
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # =========================================================================
    # EXAM ESSENTIALS
    # =========================================================================
    render_exam_essentials(
        tips=[
            {
                "tip": {"de": r"Immer $(n-1)$ für erwartungstreue Varianz", "en": r"Always $(n-1)$ for unbiased variance"},
                "why": {"de": r"Die naive Formel mit $\frac{1}{n}$ unterschätzt systematisch", "en": r"The naive formula with $\frac{1}{n}$ systematically underestimates"},
                "tip_formula": r"S^2_{n-1} = \frac{1}{n-1} \sum (X_i - \bar{X})^2"
            },
            {
                "tip": {"de": "Konsistenz = Unbiased + Varianz gegen 0", "en": "Consistency = Unbiased + Variance to 0"},
                "why": {"de": "Beide Bedingungen müssen erfüllt sein", "en": "Both conditions must be satisfied"}
            },
            {
                "tip": {"de": "Effizienz vergleicht NUR erwartungstreue Schätzer", "en": "Efficiency compares ONLY unbiased estimators"},
                "why": {"de": "Ein verzerrter Schätzer kann kleinere Varianz haben, ist aber nicht effizient", "en": "A biased estimator may have smaller variance but is not efficient"}
            }
        ],
        trap={
            "de": r"Die naive Stichprobenvarianz $\frac{1}{n}$ mit der korrekten $\frac{1}{n-1}$ verwechseln",
            "en": r"Confusing the naive sample variance $\frac{1}{n}$ with the correct $\frac{1}{n-1}$"
        },
        trap_rule={
            "de": "Merke: Wir verlieren 1 Freiheitsgrad durch die Schätzung des Mittelwerts",
            "en": "Remember: We lose 1 degree of freedom from estimating the mean"
        }
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # =========================================================================
    # EXAM PRACTICE (MCQs)
    # =========================================================================
    st.markdown(f"### {t({'de': 'Prüfungstraining', 'en': 'Exam Practice'})}")
    
    # MCQ 1: hs2023_mc10 (Unbiased estimator)
    q1 = get_question("8", "hs2023_mc10")
    if q1:
        with st.container(border=True):
            st.caption(q1.get("source", ""))
            opts = q1.get("options", [])
            if opts and isinstance(opts[0], dict):
                option_labels = [t(o) for o in opts]
            else:
                option_labels = opts
            
            render_mcq(
                key_suffix="8_2_unbiased",
                question_text=t(q1["question"]),
                options=option_labels,
                correct_idx=q1["correct_idx"],
                solution_text_dict=q1["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
                client=model,
                ai_context="Identifying unbiased estimators",
                course_id="vwl",
                topic_id="8",
                subtopic_id="8.2",
                question_id="8_2_unbiased"
            )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # MCQ 2: hs2015_mc10 (Consistency vs unbiasedness)
    q2 = get_question("8", "hs2015_mc10")
    if q2:
        with st.container(border=True):
            st.caption(q2.get("source", ""))
            opts = q2.get("options", [])
            if opts and isinstance(opts[0], dict):
                option_labels = [t(o) for o in opts]
            else:
                option_labels = opts
            
            render_mcq(
                key_suffix="8_2_consistency",
                question_text=t(q2["question"]),
                options=option_labels,
                correct_idx=q2["correct_idx"],
                solution_text_dict=q2["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
                client=model,
                ai_context="Distinguishing between unbiasedness and consistency",
                course_id="vwl",
                topic_id="8",
                subtopic_id="8.2",
                question_id="8_2_consistency"
            )
