# Topic 5.4: Sum of Two or More Random Variables
import streamlit as st
import numpy as np
from utils.localization import t
from utils.layouts.foundation import grey_info
from utils.quiz_helper import render_mcq
from utils.ask_yourself import render_ask_yourself
from utils.exam_essentials import render_exam_essentials
from utils.layouts import render_comparison, render_decision_tree, render_single_formula
from utils.worked_example import render_worked_example
from utils.layouts.foundation import grey_callout, key_insight
from data.exam_questions import get_question

# Content dictionaries
content_5_4 = {
    "title": {
        "de": "5.4 Summe von zwei oder mehreren Zufallsvariablen",
        "en": "5.4 Sum of Two or More Random Variables"
    },
    "intuition": {
        "de": "Stell dir zwei Würfel vor. Der Erwartungswert ihrer Summe ist einfach: Addiere die Einzelerwartungswerte. Aber wie 'streut' die Summe? Das hängt davon ab, ob die Würfel 'zusammenspielen' oder nicht.",
        "en": "Imagine two dice. The expected value of their sum is simple: add the individual expectations. But how much does the sum 'spread'? That depends on whether the dice 'play together' or not."
    },
}


def render_subtopic_5_4(model):
    """5.4 Summe von zwei oder mehreren Zufallsvariablen"""
    
    st.header(t(content_5_4["title"]))
    st.markdown("---")
    
    # --- THEORY SECTION ---
    render_comparison(
        title={"de": "Linearität: Erwartungswert vs. Varianz", "en": "Linearity: Expectation vs. Variance"},
        intuition=content_5_4["intuition"],
        left={
            "title": {"de": "Erwartungswert (IMMER linear)", "en": "Expected Value (ALWAYS linear)"},
            "intuition": {"de": "Die Durchschnitte addieren sich — egal ob abhängig oder nicht.", "en": "Averages add up — regardless of dependence."},
            "formula": r"E[X + Y] = E[X] + E[Y]",
            "variables": [
                {"symbol": "E[X]", "name": {"de": "Erwartungswert von X", "en": "Expected value of X"}, "description": {"de": "Langfristiger Durchschnitt von X", "en": "Long-run average of X"}},
            ],
            "insight": {"de": "Funktioniert IMMER, selbst bei abhängigen Variablen!", "en": "Works ALWAYS, even for dependent variables!"},
        },
        right={
            "title": {"de": "Varianz (Kovarianz-abhängig)", "en": "Variance (Covariance-dependent)"},
            "intuition": {"de": "Die Streuung hängt davon ab, wie X und Y zusammenspielen.", "en": "The spread depends on how X and Y interact."},
            "formula": r"\text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y) + 2\text{Cov}(X,Y)",
            "variables": [
                {"symbol": r"\text{Cov}(X,Y)", "name": {"de": "Kovarianz", "en": "Covariance"}, "description": {"de": "Misst gemeinsame Bewegung", "en": "Measures joint movement"}},
            ],
            "insight": {"de": "Nur wenn Cov=0 (unkorreliert) vereinfacht sich die Formel!", "en": "Only when Cov=0 (uncorrelated) does the formula simplify!"},
        },
        key_difference={
            "de": "Erwartungswert ignoriert Abhängigkeiten. Varianz nicht — deshalb brauchen wir den Kovarianz-Term!",
            "en": "Expectation ignores dependence. Variance doesn't — that's why we need the covariance term!"
        }
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- DECISION TREE: When can I add variances? ---
    render_decision_tree(
        title={"de": "Wann kann ich Varianzen einfach addieren?", "en": "When Can I Simply Add Variances?"},
        decisions=[
            {
                "condition": {"de": "X und Y sind unabhängig", "en": "X and Y are independent"},
                "result": {"de": "Var(X+Y) = Var(X) + Var(Y)", "en": "Var(X+Y) = Var(X) + Var(Y)"},
                "highlight": True
            },
            {
                "condition": {"de": "X und Y sind unkorreliert (Cov=0)", "en": "X and Y are uncorrelated (Cov=0)"},
                "result": {"de": "Var(X+Y) = Var(X) + Var(Y)", "en": "Var(X+Y) = Var(X) + Var(Y)"},
            },
            {
                "condition": {"de": "X und Y sind korreliert", "en": "X and Y are correlated"},
                "result": {"de": "Var(X+Y) = Var(X) + Var(Y) + 2Cov(X,Y)", "en": "Var(X+Y) = Var(X) + Var(Y) + 2Cov(X,Y)"},
            },
        ]
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- SAMPLE MEAN THEORY (using render_single_formula) ---
    render_single_formula(
        title={"de": "Das Stichprobenmittel", "en": "The Sample Mean"},
        intuition={"de": "Je mehr Beobachtungen, desto genauer wird der Durchschnitt. Die Unsicherheit im Mittelwert schrumpft mit der Wurzel aus n.", 
                   "en": "More observations mean a more precise average. The uncertainty in the mean shrinks with the square root of n."},
        formula=r"\text{Var}(\bar{X}_n) = \frac{\sigma^2}{n}",
        variables=[
            {"symbol": r"\bar{X}_n", "name": {"de": "Stichprobenmittel", "en": "Sample Mean"}, "description": {"de": "Durchschnitt von n Beobachtungen", "en": "Average of n observations"}},
            {"symbol": r"\sigma^2", "name": {"de": "Varianz", "en": "Variance"}, "description": {"de": "Streuung einer Einzelmessung", "en": "Spread of one measurement"}},
            {"symbol": "n", "name": {"de": "Stichprobengrösse", "en": "Sample size"}, "description": {"de": "Anzahl Beobachtungen", "en": "Number of observations"}},
        ],
        insight={"de": "Das √n-Gesetz: Verdopple n → Halbiere die Standardabweichung des Mittelwerts.", 
                 "en": "The √n-law: Double n → Halve the standard deviation of the mean."}
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- WORKED EXAMPLE with CONNECTION COLORING ---
    # Each distinct value gets its own color that persists throughout
    # σ²_X = 100 → Blue | σ²_Y = 64 → Red | ρ = 0.5 → Purple | Cov = 40 → Gray | Answer → Green
    render_worked_example(
        header={"de": "Rechenbeispiel: Portfolio-Varianz", "en": "Worked Example: Portfolio Variance"},
        problem={
            "de": "Zwei Aktien: $\\text{Var}(X) = {\\color{#007AFF}100}$, $\\text{Var}(Y) = {\\color{#FF4B4B}64}$, $\\rho_{XY} = {\\color{#9B59B6}0.5}$. Was ist $\\text{Var}(X+Y)$?",
            "en": "Two stocks: $\\text{Var}(X) = {\\color{#007AFF}100}$, $\\text{Var}(Y) = {\\color{#FF4B4B}64}$, $\\rho_{XY} = {\\color{#9B59B6}0.5}$. What is $\\text{Var}(X+Y)$?"
        },
        steps=[
            {
                "label": {"de": "Gegeben", "en": "Given"},
                "latex": r"\sigma_X^2 = {\color{#007AFF}100}, \quad \sigma_Y^2 = {\color{#FF4B4B}64}, \quad \rho = {\color{#9B59B6}0.5}",
                "note": {"de": "Daraus: σ_X = 10, σ_Y = 8", "en": "Thus: σ_X = 10, σ_Y = 8"}
            },
            {
                "label": {"de": "Kovarianz berechnen", "en": "Calculate Covariance"},
                "latex": r"\text{Cov}(X,Y) = {\color{#9B59B6}0.5} \cdot 10 \cdot 8 = {\color{#6B7280}40}",
            },
            {
                "label": {"de": "Formel anwenden", "en": "Apply Formula"},
                "latex": r"\text{Var}(X+Y) = {\color{#007AFF}100} + {\color{#FF4B4B}64} + 2 \cdot {\color{#6B7280}40} = {\color{#16a34a}244}",
            },
        ],
        answer={"de": "Die Portfolio-Varianz beträgt **244**.", "en": "The portfolio variance is **244**."},
        check={"de": "Plausibilitätsprüfung: Ohne Korrelation wäre Var(X+Y) = 164. Mit positiver Korrelation erhöht sich das Risiko auf 244.", 
               "en": "Plausibility check: Without correlation, Var(X+Y) = 164. With positive correlation, risk increases to 244."}
    )

    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- INTERACTIVE MISSION: Sample Mean Simulator ---
    st.markdown(f"### {t({'de': 'Interaktive Mission: Das √n-Gesetz entdecken', 'en': 'Interactive Mission: Discover the √n-Law'})}")
    
    # Scenario first (grey callout)
    grey_callout(
        {"de": "Szenario", "en": "Scenario"},
        {"de": "Ein Qualitätsingenieur entnimmt wiederholt Stichproben aus der Produktion. Jede Einzelmessung hat Varianz σ² = 100. Wie sehr 'streut' der Mittelwert bei unterschiedlichen Stichprobengrössen?",
         "en": "A quality engineer repeatedly takes samples from production. Each individual measurement has variance σ² = 100. How much does the mean 'spread' for different sample sizes?"}
    )
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"**{t({'de': 'Mission', 'en': 'Mission'})}:** {t({'de': 'Beobachte, wie die Streuung des Mittelwerts mit wachsendem n schrumpft.', 'en': 'Observe how the spread of the mean shrinks as n grows.'})}")
    
    @st.fragment
    def sample_mean_simulator():
        # Fixed parameters
        sigma_sq = 100  # Variance of individual observation
        sigma = 10      # Standard deviation
        mu = 50         # Mean
        n_simulations = 500  # Number of sample means to generate
        
        # Slider - use key directly, no separate session state needed
        n = st.slider(
            t({"de": "Stichprobengrösse (n)", "en": "Sample size (n)"}),
            min_value=1,
            max_value=50,
            value=5,
            key="5_4_n_slider"
        )
        
        # Calculate theoretical values
        var_mean = sigma_sq / n
        sd_mean = np.sqrt(var_mean)
        
        # Simulate sample means - use n as part of seed for variety
        np.random.seed(42 + n)
        samples = np.random.normal(mu, sigma, size=(n_simulations, n))
        sample_means = samples.mean(axis=1)
        
        # Create histogram
        import plotly.graph_objects as go
        
        # Fixed x-axis range for reference
        x_min = mu - 4 * sigma
        x_max = mu + 4 * sigma
        
        fig = go.Figure()
        
        # Histogram of sample means
        fig.add_trace(go.Histogram(
            x=sample_means,
            nbinsx=30,
            marker_color='#007AFF',
            opacity=0.7,
            name=t({"de": "Stichprobenmittel", "en": "Sample Means"})
        ))
        
        # Add vertical lines for ±1 SD - position annotations to avoid overlap
        # Use shapes instead of vline for better control
        fig.add_shape(
            type="line", x0=mu - sd_mean, x1=mu - sd_mean, y0=0, y1=1,
            yref="paper", line=dict(color="#FF4B4B", width=2, dash="dash")
        )
        fig.add_shape(
            type="line", x0=mu + sd_mean, x1=mu + sd_mean, y0=0, y1=1,
            yref="paper", line=dict(color="#FF4B4B", width=2, dash="dash")
        )
        fig.add_shape(
            type="line", x0=mu, x1=mu, y0=0, y1=1,
            yref="paper", line=dict(color="#6B7280", width=2)
        )
        
        # Add annotations below the chart at different x positions to avoid overlap
        fig.add_annotation(
            x=mu, y=1.08, yref="paper", text=f"μ = {mu}",
            showarrow=False, font=dict(color="#6B7280", size=11)
        )
        # Only show ±σ annotations if they're far enough apart (n small = wide spread)
        if sd_mean > 3:
            fig.add_annotation(
                x=mu - sd_mean, y=1.08, yref="paper", text=f"−σ̄",
                showarrow=False, font=dict(color="#FF4B4B", size=11)
            )
            fig.add_annotation(
                x=mu + sd_mean, y=1.08, yref="paper", text=f"+σ̄",
                showarrow=False, font=dict(color="#FF4B4B", size=11)
            )
        
        fig.update_layout(
            title=t({"de": f"Verteilung von X̄ bei n = {n}", "en": f"Distribution of X̄ with n = {n}"}),
            xaxis_title=t({"de": "Wert des Stichprobenmittels", "en": "Sample Mean Value"}),
            yaxis_title=t({"de": "Häufigkeit", "en": "Frequency"}),
            xaxis=dict(range=[x_min, x_max]),
            showlegend=False,
            height=350,
            margin=dict(t=60, b=50),
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # FLOW COLORING: Trace cause → effect
        # n = Blue (user INPUT)
        # σ² = Gray (GIVEN/fixed)
        # Var(X̄) = Result color (risk-based: red=high, green=low)
        # σ_X̄ = Purple (INTERMEDIATE - derived from Var, distinct color)
        
        input_color = "#007AFF"  # Blue - what user controls
        given_color = "#6B7280"  # Gray - fixed parameter
        intermediate_color = "#9B59B6"  # Purple - transformation of result
        
        # Result color based on outcome quality
        if n >= 25:
            result_color = "#16a34a"  # Green - good outcome (low variance)
        else:
            result_color = "#FF4B4B"  # Red - warning (high variance)
        
        # Dynamic formula display with Flow Coloring
        # Shows: input (n) → given (σ²) → result (Var) → intermediate (σ)
        c1, c2 = st.columns(2)
        with c1:
            st.latex(fr"\text{{Var}}(\bar{{X}}_{{{{\color{{{input_color}}}{n}}}}}) = \frac{{{{\color{{{given_color}}}{sigma_sq}}}}}{{{{\color{{{input_color}}}{n}}}}} = {{\color{{{result_color}}}{var_mean:.2f}}}")
        with c2:
            st.latex(fr"\sigma_{{\bar{{X}}}} = \sqrt{{{{\color{{{result_color}}}{var_mean:.2f}}}}} = {{\color{{{intermediate_color}}}{sd_mean:.2f}}}")
        
        # Feedback based on n - NO EMOJI
        if n >= 25:
            st.success(t({
                "de": f"Mission geschafft! Bei n = {n} ist die Standardabweichung des Mittelwerts nur noch {sd_mean:.2f} (statt {sigma} für eine Einzelmessung).",
                "en": f"Mission complete! With n = {n}, the standard deviation of the mean is only {sd_mean:.2f} (instead of {sigma} for a single measurement)."
            }))
            
            # Discovery debrief
            st.markdown("<br>", unsafe_allow_html=True)
            grey_callout(
                {"de": "Was du entdeckt hast", "en": "What You Discovered"},
                {"de": f"Mit n = {n} Messungen ist der Mittelwert viel 'stabiler' als eine Einzelmessung. Die Unsicherheit sinkt um den Faktor √{n} ≈ {np.sqrt(n):.1f}. Das ist das √n-Gesetz — die Grundlage für statistische Präzision!",
                 "en": f"With n = {n} measurements, the mean is much more 'stable' than a single measurement. Uncertainty drops by factor √{n} ≈ {np.sqrt(n):.1f}. This is the √n-law — the foundation of statistical precision!"}
            )
        elif n >= 10:
            grey_info(t({
                "de": f"Gut! Bei n = {n} ist σ̄ = {sd_mean:.2f}. Erhöhe n weiter auf 25+ um den vollen Effekt zu sehen.",
                "en": f"Good! With n = {n}, σ̄ = {sd_mean:.2f}. Increase n to 25+ to see the full effect."
            }))
        else:
            st.caption(t({
                "de": f"Bei n = {n} ist die Streuung noch gross (σ̄ = {sd_mean:.2f}). Erhöhe n um den Effekt zu beobachten.",
                "en": f"With n = {n}, the spread is still large (σ̄ = {sd_mean:.2f}). Increase n to observe the effect."
            }))
    
    sample_mean_simulator()
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- FRAG DICH (ASK YOURSELF) ---
    render_ask_yourself(
        header={"de": "Frag dich: Können Varianzen addiert werden?", "en": "Ask yourself: Can variances be added?"},
        questions=[
            {"de": "Sind X und Y unabhängig (oder zumindest unkorreliert)?", "en": "Are X and Y independent (or at least uncorrelated)?"},
            {"de": "Wenn ja: Var(X+Y) = Var(X) + Var(Y). Fertig!", "en": "If yes: Var(X+Y) = Var(X) + Var(Y). Done!"},
            {"de": "Wenn nein: Vergiss den Kovarianz-Term nicht!", "en": "If no: Don't forget the covariance term!"},
            {"de": "Bei X - Y: Minus vor Y ändert das Vorzeichen der Kovarianz!", "en": "For X - Y: The minus before Y changes the sign of covariance!"},
        ],
        conclusion={"de": "E[] addiert IMMER. Var() nur bei Cov = 0!", "en": "E[] adds ALWAYS. Var() only when Cov = 0!"}
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- EXAM ESSENTIALS ---
    render_exam_essentials(
        trap={
            "de": "Varianzen einfach addieren, ohne zu prüfen ob die Variablen unkorreliert sind.",
            "en": "Simply adding variances without checking if variables are uncorrelated."
        },
        trap_rule={
            "de": "Var(X+Y) = Var(X) + Var(Y) + 2·Cov(X,Y). Der Cov-Term ist nur dann 0, wenn X und Y unkorreliert sind!",
            "en": "Var(X+Y) = Var(X) + Var(Y) + 2·Cov(X,Y). The Cov term is only 0 when X and Y are uncorrelated!"
        },
        tips=[
            {
                "tip": {"de": "E[X+Y] = E[X] + E[Y] gilt IMMER", "en": "E[X+Y] = E[X] + E[Y] holds ALWAYS"},
                "why": {"de": "Linearität des Erwartungswerts — keine Bedingungen nötig!", "en": "Linearity of expectation — no conditions needed!"}
            },
            {
                "tip": {"de": "Var(X-Y) = Var(X) + Var(Y) - 2·Cov(X,Y)", "en": "Var(X-Y) = Var(X) + Var(Y) - 2·Cov(X,Y)"},
                "why": {"de": "Das Minus vor Y ändert das Vorzeichen vor der Kovarianz, nicht vor Var(Y)!", "en": "The minus before Y changes the sign before covariance, not before Var(Y)!"}
            },
            {
                "tip": {"de": "Var(X̄ₙ) = σ²/n — das √n-Gesetz", "en": "Var(X̄ₙ) = σ²/n — the √n-law"},
                "why": {"de": "Verdopple n → Halbiere die Standardabweichung des Mittelwerts.", "en": "Double n → Halve the standard deviation of the mean."}
            },
        ]
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- EXAM SECTION ---
    st.markdown(f"### {t({'de': 'Prüfungstraining', 'en': 'Exam Practice'})}")
    
    # MCQ 1: uebung3_mc10 (Correlation range)
    q1 = get_question("5.4", "uebung3_mc10")
    if q1:
        st.caption(q1.get("source", ""))
        with st.container(border=True):
            opts = q1.get("options", [])
            if opts and isinstance(opts[0], dict):
                option_labels = [t(o) for o in opts]
            else:
                option_labels = opts
            
            render_mcq(
                key_suffix="5_4_range",
                question_text=t(q1["question"]),
                options=option_labels,
                correct_idx=q1["correct_idx"],
                solution_text_dict=q1["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
                client=model,
                ai_context="Range of correlation coefficient",
                course_id="vwl",
                topic_id="5",
                subtopic_id="5.4",
                question_id="5_4_range"
            )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # MCQ 2: uebung3_mc11 (Corr = 0.8 interpretation)
    q2 = get_question("5.4", "uebung3_mc11")
    if q2:
        st.caption(q2.get("source", ""))
        with st.container(border=True):
            opts = q2.get("options", [])
            if opts and isinstance(opts[0], dict):
                option_labels = [t(o) for o in opts]
            else:
                option_labels = opts
            
            render_mcq(
                key_suffix="5_4_interp",
                question_text=t(q2["question"]),
                options=option_labels,
                correct_idx=q2["correct_idx"],
                solution_text_dict=q2["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
                client=model,
                ai_context="Interpreting correlation values",
                course_id="vwl",
                topic_id="5",
                subtopic_id="5.4",
                question_id="5_4_interp"
            )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # MCQ 3: hs2015_mc6 (Bienaymé / Variance additivity)
    q3 = get_question("5.4", "hs2015_mc6")
    if q3:
        st.caption(q3.get("source", ""))
        with st.container(border=True):
            opts = q3.get("options", [])
            if opts and isinstance(opts[0], dict):
                option_labels = [t(o) for o in opts]
            else:
                option_labels = opts
            
            render_mcq(
                key_suffix="5_4_bienayme",
                question_text=t(q3["question"]),
                options=option_labels,
                correct_idx=q3["correct_idx"],
                solution_text_dict=q3["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
                client=model,
                ai_context="Bienaymé's identity and variance of sums",
                course_id="vwl",
                topic_id="5",
                subtopic_id="5.4",
                question_id="5_4_bienayme"
            )
