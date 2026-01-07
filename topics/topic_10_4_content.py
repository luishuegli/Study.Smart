# Topic 10.4: The p-Value (Der p-Wert)
# ULTRATHINK Feynman-style implementation: "The Evidence Meter"
import streamlit as st
import numpy as np
import plotly.graph_objects as go
from scipy import stats
from utils.localization import t
from utils.quiz_helper import render_mcq
from utils.ask_yourself import render_ask_yourself
from utils.exam_essentials import render_exam_essentials
from utils.layouts import render_comparison, render_definition
from utils.layouts.foundation import inject_equal_height_css

# ==============================================================================
# CONTENT DICTIONARY
# ==============================================================================

content_10_4 = {
    "title": {"de": "10.4 Der p-Wert", "en": "10.4 The p-Value"},
    
    # --- TALENT SHOW ANALOGY (Intuition) ---
    "intuition": {
        "de": """<strong>Stell dir vor, du bist Juror bei einer Talentshow:</strong><br><br>
• Ein Kandidat behauptet, er sei nur ein <strong>DURCHSCHNITTLICHER</strong> Sänger (H₀)<br>
• Er trifft 20 hohe Töne perfekt (deine Daten)<br><br>
<strong>Du fragst dich:</strong> "Wie wahrscheinlich ist es, dass ein DURCHSCHNITTLICHER Sänger 20 Töne perfekt trifft?"<br><br>
→ Wenn diese Wahrscheinlichkeit <strong>winzig</strong> ist (z.B. 0.1%), sagst du:<br>
<em>"Du bist NICHT durchschnittlich — du bist aussergewöhnlich!"</em><br><br>
<strong>Diese Wahrscheinlichkeit ist der p-Wert.</strong>""",
        "en": """<strong>Imagine you're a talent show judge:</strong><br><br>
• A contestant claims they're just an <strong>AVERAGE</strong> singer (H₀)<br>
• They hit 20 high notes perfectly (your data)<br><br>
<strong>You ask:</strong> "How likely is it that an AVERAGE singer hits 20 notes perfectly?"<br><br>
→ If this probability is <strong>tiny</strong> (e.g., 0.1%), you say:<br>
<em>"You're NOT average — you're exceptional!"</em><br><br>
<strong>This probability is the p-value.</strong>"""
    },
    
    # --- DEFINITION ---
    "definition": {
        "term": {"de": "p-Wert", "en": "p-Value"},
        "definition": {
            "de": "Der p-Wert ist das <strong>kleinste Signifikanzniveau α</strong>, bei dem die Nullhypothese mit den beobachteten Daten abgelehnt würde.",
            "en": "The p-value is the <strong>smallest significance level α</strong> at which the null hypothesis would be rejected with the observed data."
        },
        "formula": r"p = P(|T| \geq |t| \mid H_0)",
        "variables": [
            {"symbol": "p", "name": {"de": "p-Wert", "en": "p-Value"}, 
             "desc": {"de": "Die Wahrscheinlichkeit, die wir berechnen", "en": "The probability we calculate"}},
            {"symbol": "T", "name": {"de": "Teststatistik", "en": "Test Statistic"}, 
             "desc": {"de": "Zufallsvariable unter H₀", "en": "Random variable under H₀"}},
            {"symbol": "t", "name": {"de": "Beobachteter Wert", "en": "Observed Value"}, 
             "desc": {"de": "Der tatsächliche Wert aus deinen Daten", "en": "The actual value from your data"}},
            {"symbol": "H_0", "name": {"de": "Nullhypothese", "en": "Null Hypothesis"}, 
             "desc": {"de": "Annahme, die wir testen", "en": "Assumption we're testing"}}
        ],
        "insight": {
            "de": "<strong>VORSICHT:</strong> Der p-Wert ist NICHT die Wahrscheinlichkeit, dass H₀ wahr ist!<br>Er ist die Wahrscheinlichkeit, solche DATEN zu sehen, WENN H₀ wahr wäre.",
            "en": "<strong>CAUTION:</strong> The p-value is NOT the probability that H₀ is true!<br>It's the probability of seeing such DATA IF H₀ were true."
        }
    },
    
    # --- DECISION RULE ---
    "decision_rule": {
        "reject": {"de": "p < α → H₀ ablehnen", "en": "p < α → Reject H₀"},
        "reject_meaning": {"de": "Daten zu extrem um durch H₀ erklärt zu werden", "en": "Data too extreme to be explained by H₀"},
        "keep": {"de": "p ≥ α → H₀ nicht ablehnen", "en": "p ≥ α → Don't reject H₀"},
        "keep_meaning": {"de": "Daten könnten unter H₀ plausibel auftreten", "en": "Data could plausibly occur under H₀"}
    },
    
    # --- COMPARISON: Two Approaches ---
    "comparison": {
        "left": {
            "title": {"de": "Kritischer-Wert-Ansatz", "en": "Critical Value Approach"},
            "content": {
                "de": "<strong>Entscheidungsregel:</strong><br>Lehne H₀ ab, wenn |T| > c<br><br><em>«Ist mein T jenseits der Grenze?»</em>",
                "en": "<strong>Decision rule:</strong><br>Reject H₀ if |T| > c<br><br><em>«Is my T beyond the threshold?»</em>"
            }
        },
        "right": {
            "title": {"de": "p-Wert-Ansatz", "en": "p-Value Approach"},
            "content": {
                "de": "<strong>Entscheidungsregel:</strong><br>Lehne H₀ ab, wenn p < α<br><br><em>«Wie extrem ist mein Ergebnis?»</em>",
                "en": "<strong>Decision rule:</strong><br>Reject H₀ if p < α<br><br><em>«How extreme is my result?»</em>"
            }
        }
    },
    
    # --- ASK YOURSELF (Unicode, no LaTeX) ---
    "frag_dich": {
        "header": {
            "de": "Frag dich: Verstehst du den p-Wert?",
            "en": "Ask yourself: Do you understand the p-value?"
        },
        "questions": [
            {"de": "p = 0.03 und α = 0.05 — Lehnst du H₀ ab?", 
             "en": "p = 0.03 and α = 0.05 — Do you reject H₀?"},
            {"de": "Wenn p = 0.51, ist das starke Evidenz gegen H₀?", 
             "en": "If p = 0.51, is that strong evidence against H₀?"},
            {"de": "«p = 0.02 heisst, H₀ ist mit 2% Wahrscheinlichkeit wahr» — Korrekt?", 
             "en": "«p = 0.02 means H₀ has 2% probability of being true» — Correct?"},
            {"de": "Warum verdoppeln wir p bei zweiseitigen Tests?", 
             "en": "Why do we double p for two-sided tests?"}
        ],
        "conclusion": {
            "de": "Goldene Regel: p < α → Ablehnen | p ≥ α → Nicht ablehnen",
            "en": "Golden Rule: p < α → Reject | p ≥ α → Don't reject"
        }
    },
    
    # --- EXAM ESSENTIALS ---
    "exam_essentials": {
        "trap": {
            "de": "«p = 0.03 bedeutet, dass H₀ mit 3% Wahrscheinlichkeit wahr ist»",
            "en": "«p = 0.03 means H₀ is 3% likely to be true»"
        },
        "trap_rule": {
            "de": "p-Wert = Wahrscheinlichkeit der DATEN, nicht der Hypothese!",
            "en": "p-value = probability of DATA, not the hypothesis!"
        },
        "tips": [
            {
                "tip": {"de": "Bei zweiseitigem Test: p = 2 · P(Z > |z|)", "en": "For two-sided test: p = 2 · P(Z > |z|)"},
                "why": {"de": "Beide Enden ('Tails') zählen bei zweiseitigen Tests.", "en": "Both tails count in two-sided tests."},
                "why_formula": r"p = 2 \cdot P(Z > |z|)"
            },
            {
                "tip": {"de": "Immer p UND Entscheidung angeben", "en": "Always report both p AND your decision"},
                "why": {"de": "Prüfer wollen den Rechenweg UND die Schlussfolgerung sehen.", "en": "Examiners want to see both the calculation AND the conclusion."}
            },
            {
                "tip": {"de": "p-Wert ist stetig — es gibt keine 'Grauzone'", "en": "p-value is continuous — there's no 'gray zone'"},
                "why": {"de": "p = 0.049 und p = 0.051 sind praktisch gleich — aber die Entscheidung ist binär!", "en": "p = 0.049 and p = 0.051 are practically equal — but the decision is binary!"}
            }
        ]
    },
    
    # --- MCQ (from hs2024_mc8) ---
    "mcq": {
        "source": "HS 2024 Januar, MC #8",
        "question": {
            "de": r"Angenommen, $X \sim N(\mu, 5)$ mit $\sigma^2 = 5$. Wir testen $H_0: \mu = 8$ gegen $H_1: \mu \neq 8$ mit nur 5 Beobachtungen. Der ML-Schätzer ist $\hat{\mu} = 4.95$. Wie gross ist der p-Wert?",
            "en": r"Assume $X \sim N(\mu, 5)$ with $\sigma^2 = 5$. We test $H_0: \mu = 8$ against $H_1: \mu \neq 8$ with only 5 observations. The MLE estimate is $\hat{\mu} = 4.95$. What is the p-value?"
        },
        "options": [
            {"id": "a", "de": "0.0011", "en": "0.0011"},
            {"id": "b", "de": "0.0022", "en": "0.0022"},
            {"id": "c", "de": "0.1738", "en": "0.1738"},
            {"id": "d", "de": "0.3476", "en": "0.3476"}
        ],
        "correct_id": "b",
        "solution": {
            "de": r"<strong>Richtig: (b) 0.0022</strong><br><br><strong>Schritt 1:</strong> Teststatistik berechnen<br>$Z = \frac{\hat{\mu} - \mu_0}{\sigma / \sqrt{n}} = \frac{4.95 - 8}{\sqrt{5} / \sqrt{5}} = \frac{-3.05}{1} = -3.05$<br><br><strong>Schritt 2:</strong> p-Wert (zweiseitig)<br>$p = 2 \cdot P(Z < -3.05) \approx 2 \cdot 0.0011 = 0.0022$<br><br>Da $p = 0.0022 < 0.05$, lehnen wir $H_0$ ab.",
            "en": r"<strong>Correct: (b) 0.0022</strong><br><br><strong>Step 1:</strong> Calculate test statistic<br>$Z = \frac{\hat{\mu} - \mu_0}{\sigma / \sqrt{n}} = \frac{4.95 - 8}{\sqrt{5} / \sqrt{5}} = \frac{-3.05}{1} = -3.05$<br><br><strong>Step 2:</strong> p-value (two-sided)<br>$p = 2 \cdot P(Z < -3.05) \approx 2 \cdot 0.0011 = 0.0022$<br><br>Since $p = 0.0022 < 0.05$, we reject $H_0$."
        }
    }
}

# ==============================================================================
# INTERACTIVE: THE EVIDENCE METER (WOW Element)
# ==============================================================================

@st.fragment
def evidence_meter_interactive():
    """
    The Evidence Meter: An immersive p-value explorer.
    
    The student drags the sample mean slider and watches:
    1. The test statistic T update in real-time
    2. The p-value "evidence meter" fill/drain
    3. The shaded area on the normal curve change
    4. The verdict flip between "Don't Reject" and "REJECT!"
    
    This creates an immediate, visceral understanding of p-values.
    """
    
    # State initialization with SLIDER KEY-ONLY PATTERN
    # (no manual sync - let Streamlit auto-sync via key)
    
    # --- SCENARIO BOX ---
    st.markdown(f"""
<div style="background: #f4f4f5; border-left: 4px solid #a1a1aa; 
            padding: 16px 20px; border-radius: 8px; color: #3f3f46; margin-bottom: 20px;">
<strong>{t({"de": "Szenario: Die Qualitätsprüfung", "en": "Scenario: Quality Control"})}</strong><br><br>
{t({"de": "Eine Maschine soll Teile mit μ₀ = 100g produzieren. Eine Qualitätsingenieurin nimmt eine Stichprobe und misst x̄. Sie fragt: «Ist die Maschine noch korrekt eingestellt?»",
    "en": "A machine should produce parts with μ₀ = 100g. A quality engineer takes a sample and measures x̄. She asks: «Is the machine still correctly calibrated?»"})}
</div>
""", unsafe_allow_html=True)
    
    # --- MISSION STATEMENT ---
    st.markdown(f"**{t({'de': 'Mission', 'en': 'Mission'})}:** {t({'de': 'Finde heraus, wie der p-Wert auf deine Stichprobe reagiert!', 'en': 'Discover how the p-value responds to your sample!'})}")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Fixed parameters (realistic quality control)
    mu_0 = 100.0  # Null hypothesis value
    sigma = 5.0   # Known population std dev
    n = 25        # Sample size
    alpha = 0.05  # Significance level
    
    # Parameters display
    st.markdown(f"""
<div style="background: #f4f4f5; padding: 12px 16px; border-radius: 8px; color: #3f3f46; margin-bottom: 16px;">
<strong>{t({"de": "Gegeben", "en": "Given"})}:</strong> 
μ₀ = {mu_0}g, σ = {sigma}g, n = {n}, α = {alpha}
</div>
""", unsafe_allow_html=True)
    
    # Two column layout: Controls + Chart
    col_ctrl, col_viz = st.columns([1, 1.6], gap="medium")
    
    with col_ctrl:
        # Blue slider CSS for sample mean control
        from utils.layouts.foundation import inject_slider_css
        inject_slider_css([
            {"label_contains": "Stichprobenmittelwert", "color": "#007AFF"},
            {"label_contains": "Sample Mean", "color": "#007AFF"},
            {"label_contains": "x̄", "color": "#007AFF"},
        ])
        
        # The main slider - sample mean
        x_bar_label = t({"de": "Stichprobenmittelwert", "en": "Sample Mean"})
        st.markdown(f"**{x_bar_label}** x̄")
        x_bar = st.slider(
            label="x̄",
            min_value=90.0,
            max_value=110.0,
            value=100.0,  # Start at null hypothesis
            step=0.1,
            key="pval_xbar",
            label_visibility="collapsed"
        )
        
        # Calculate test statistic
        se = sigma / np.sqrt(n)  # Standard error
        z = (x_bar - mu_0) / se  # Z-score
        
        # Calculate p-value (two-sided)
        p_value = 2 * (1 - stats.norm.cdf(abs(z)))
        
        # Decision
        reject = p_value < alpha
        
        # Display results with semantic colors
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Test statistic (always black)
        st.markdown(f"**{t({'de': 'Teststatistik', 'en': 'Test Statistic'})}:** T = {z:.3f}")
        
        # P-value with color based on magnitude
        if p_value < 0.01:
            p_color = "#dc2626"  # Very significant - dark red
        elif p_value < 0.05:
            p_color = "#FF4B4B"  # Significant - red
        elif p_value < 0.10:
            p_color = "#f97316"  # Marginal - orange
        else:
            p_color = "#16a34a"  # Not significant - green
        
        st.markdown(f"**p-{t({'de': 'Wert', 'en': 'Value'})}:** <span style='color:{p_color}; font-weight:bold; font-size:1.3em;'>{p_value:.4f}</span>", unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # THE VERDICT - Big visual impact
        if reject:
            st.markdown(f"""
<div style="background: linear-gradient(135deg, #FF4B4B 0%, #dc2626 100%); 
            color: white; padding: 20px; border-radius: 12px; text-align: center;
            box-shadow: 0 4px 15px rgba(255, 75, 75, 0.4);">
<div style="font-size: 0.9em; opacity: 0.9;">{t({"de": "URTEIL", "en": "VERDICT"})}</div>
<div style="font-size: 1.4em; font-weight: bold; margin-top: 8px;">
{t({"de": "H₀ ABLEHNEN!", "en": "REJECT H₀!"})}
</div>
<div style="font-size: 0.85em; margin-top: 8px; opacity: 0.9;">
p = {p_value:.4f} < α = {alpha}
</div>
</div>
""", unsafe_allow_html=True)
        else:
            st.markdown(f"""
<div style="background: linear-gradient(135deg, #16a34a 0%, #15803d 100%); 
            color: white; padding: 20px; border-radius: 12px; text-align: center;
            box-shadow: 0 4px 15px rgba(22, 163, 74, 0.4);">
<div style="font-size: 0.9em; opacity: 0.9;">{t({"de": "URTEIL", "en": "VERDICT"})}</div>
<div style="font-size: 1.4em; font-weight: bold; margin-top: 8px;">
{t({"de": "H₀ nicht ablehnen", "en": "Don't reject H₀"})}
</div>
<div style="font-size: 0.85em; margin-top: 8px; opacity: 0.9;">
p = {p_value:.4f} ≥ α = {alpha}
</div>
</div>
""", unsafe_allow_html=True)
    
    with col_viz:
        # Create the visualization
        x = np.linspace(-4, 4, 500)
        y = stats.norm.pdf(x)
        
        fig = go.Figure()
        
        # Shade the p-value regions (both tails for two-sided)
        z_abs = abs(z)
        
        # Left tail (always shade if we have any z)
        mask_left = x <= -z_abs
        if np.any(mask_left):
            fig.add_trace(go.Scatter(
                x=x[mask_left], y=y[mask_left],
                fill='tozeroy', 
                fillcolor='rgba(255, 75, 75, 0.5)' if reject else 'rgba(22, 163, 74, 0.3)',
                line=dict(color='rgba(0,0,0,0)'),
                name='p-value area',
                showlegend=True
            ))
        
        # Right tail
        mask_right = x >= z_abs
        if np.any(mask_right):
            fig.add_trace(go.Scatter(
                x=x[mask_right], y=y[mask_right],
                fill='tozeroy', 
                fillcolor='rgba(255, 75, 75, 0.5)' if reject else 'rgba(22, 163, 74, 0.3)',
                line=dict(color='rgba(0,0,0,0)'),
                showlegend=False
            ))
        
        # The main curve
        fig.add_trace(go.Scatter(
            x=x, y=y,
            mode='lines',
            line=dict(color='#1c1c1e', width=2),
            showlegend=False
        ))
        
        # Mark the test statistic position
        if z != 0:
            fig.add_vline(x=z, line=dict(color='#007AFF', width=3, dash='solid'),
                         annotation_text=f"T={z:.2f}", annotation_position="top")
            fig.add_vline(x=-z, line=dict(color='#007AFF', width=3, dash='solid'),
                         annotation_text=f"T={-z:.2f}", annotation_position="top")
        
        # Critical value lines (α = 0.05, two-sided → ±1.96)
        c = stats.norm.ppf(1 - alpha/2)
        fig.add_vline(x=c, line=dict(color='#a1a1aa', width=2, dash='dash'))
        fig.add_vline(x=-c, line=dict(color='#a1a1aa', width=2, dash='dash'))
        
        fig.update_layout(
            height=300,
            margin=dict(l=20, r=20, t=40, b=60),
            xaxis=dict(
                title=t({"de": "Z-Wert", "en": "Z-Score"}),
                range=[-4, 4],
                zeroline=True,
                zerolinecolor='#e5e7eb',
                zerolinewidth=1
            ),
            yaxis=dict(
                title="",
                showticklabels=False,
                zeroline=False
            ),
            legend=dict(
                orientation="h",
                yanchor="top",
                y=-0.25,
                xanchor="center",
                x=0.5
            ),
            clickmode='none',
            hovermode=False
        )
        
        st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
        
        # Explanation caption
        if reject:
            explanation = t({
                "de": f"Die schattierten Flächen (p = {p_value:.4f}) sind KLEINER als α = {alpha}. Die Daten sind zu extrem für H₀!",
                "en": f"The shaded areas (p = {p_value:.4f}) are SMALLER than α = {alpha}. The data is too extreme for H₀!"
            })
        else:
            explanation = t({
                "de": f"Die schattierten Flächen (p = {p_value:.4f}) sind GRÖSSER als α = {alpha}. Die Daten sind mit H₀ kompatibel.",
                "en": f"The shaded areas (p = {p_value:.4f}) are LARGER than α = {alpha}. The data is compatible with H₀."
            })
        st.caption(explanation)
    
    # --- KEY INSIGHT BOX ---
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Dynamic insight based on current slider position
    if abs(z) < 0.5:
        insight_text = t({
            "de": "💡 Deine Stichprobe ist sehr nah an μ₀ — das ist genau das, was wir unter H₀ erwarten würden!",
            "en": "💡 Your sample is very close to μ₀ — exactly what we'd expect under H₀!"
        })
    elif abs(z) < 1.96:
        insight_text = t({
            "de": "💡 Deine Stichprobe weicht ab, aber nicht genug um zu überzeugen. Brauchen stärkere Evidenz!",
            "en": "💡 Your sample deviates, but not enough to convince. Need stronger evidence!"
        })
    elif abs(z) < 2.58:
        insight_text = t({
            "de": "🔥 Jetzt wird's spannend! Diese Abweichung ist schwer durch Zufall zu erklären.",
            "en": "🔥 Now it's getting interesting! This deviation is hard to explain by chance."
        })
    else:
        insight_text = t({
            "de": "🎯 Extrem unwahrscheinlich unter H₀! Diese Evidenz ist überwältigend.",
            "en": "🎯 Extremely unlikely under H₀! This evidence is overwhelming."
        })
    
    st.markdown(f"""
<div style="background: #f4f4f5; border-left: 4px solid #a1a1aa; 
            padding: 12px 16px; border-radius: 8px; color: #3f3f46;">
{insight_text}
</div>
""", unsafe_allow_html=True)


# ==============================================================================
# MAIN RENDER FUNCTION
# ==============================================================================

def render_subtopic_10_4(model):
    """10.4 Der p-Wert — The p-Value"""
    
    st.header(t(content_10_4["title"]))
    st.markdown("---")
    
    # Inject equal height CSS for side-by-side containers
    inject_equal_height_css()
    
    # ==========================================================================
    # 1. THE TALENT SHOW ANALOGY (Intuition First)
    # ==========================================================================
    st.markdown(f"### {t({'de': 'Die Kernidee: Die Talentshow', 'en': 'The Core Idea: The Talent Show'})}")
    
    with st.container(border=True):
        st.markdown(t(content_10_4["intuition"]), unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # ==========================================================================
    # 2. FORMAL DEFINITION
    # ==========================================================================
    st.markdown(f"### {t({'de': 'Die formale Definition', 'en': 'The Formal Definition'})}")
    
    defn = content_10_4["definition"]
    
    with st.container(border=True):
        # Term and definition
        st.markdown(f"**{t(defn['term'])}**")
        st.markdown(t(defn["definition"]), unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Formula
        st.latex(defn["formula"])
        
        st.markdown("---")
        
        # Variable Decoder
        st.markdown(f"**{t({'de': 'Variablen-Decoder', 'en': 'Variable Decoder'})}:**")
        for var in defn["variables"]:
            symbol = var["symbol"]
            name = t(var["name"])
            desc = t(var["desc"])
            st.markdown(f"• ${symbol}$ = **{name}** — {desc}")
        
        st.markdown("---")
        
        # Key Insight (CRITICAL for understanding)
        st.markdown(f"""
<div style="background: #fef2f2; border-left: 4px solid #dc2626; 
            padding: 12px 16px; border-radius: 8px; color: #991b1b;">
{t(defn['insight'])}
</div>
""", unsafe_allow_html=True)
        st.markdown("")  # Spacer to prevent cutoff
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # ==========================================================================
    # 3. THE DECISION RULE (Visual, Clear)
    # ==========================================================================
    st.markdown(f"### {t({'de': 'Die Entscheidungsregel', 'en': 'The Decision Rule'})}")
    
    rule = content_10_4["decision_rule"]
    
    col1, col2 = st.columns(2, gap="medium")
    
    with col1:
        with st.container(border=True):
            st.latex(r"p < \alpha \rightarrow \text{Reject } H_0")
            st.caption(t(rule['reject_meaning']))
    
    with col2:
        with st.container(border=True):
            st.latex(r"p \geq \alpha \rightarrow \text{Don't reject } H_0")
            st.caption(t(rule['keep_meaning']))
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # ==========================================================================
    # 4. TWO APPROACHES COMPARISON
    # ==========================================================================
    st.markdown(f"### {t({'de': 'Zwei Wege, ein Ziel', 'en': 'Two Paths, One Goal'})}")
    
    comp = content_10_4["comparison"]
    
    render_comparison(
        left={
            "title": comp["left"]["title"],
            "intuition": comp["left"]["content"]
        },
        right={
            "title": comp["right"]["title"],
            "intuition": comp["right"]["content"]
        },
        show_header=False
    )
    
    # Add a unifying caption
    st.caption(t({"de": "Beide Ansätze führen zur gleichen Entscheidung — wähle den, der dir klarer ist!", 
                  "en": "Both approaches lead to the same decision — choose whichever is clearer to you!"}))
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # ==========================================================================
    # 5. INTERACTIVE: THE EVIDENCE METER (WOW Element)
    # ==========================================================================
    st.markdown(f"### {t({'de': 'Interaktiv: Der Evidenz-Messer', 'en': 'Interactive: The Evidence Meter'})}")
    
    evidence_meter_interactive()
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # ==========================================================================
    # 6. ASK YOURSELF (Frag Dich)
    # ==========================================================================
    render_ask_yourself(
        header=content_10_4["frag_dich"]["header"],
        questions=content_10_4["frag_dich"]["questions"],
        conclusion=content_10_4["frag_dich"]["conclusion"]
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # ==========================================================================
    # 7. EXAM ESSENTIALS
    # ==========================================================================
    render_exam_essentials(
        trap=content_10_4["exam_essentials"]["trap"],
        trap_rule=content_10_4["exam_essentials"]["trap_rule"],
        tips=content_10_4["exam_essentials"]["tips"]
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # ==========================================================================
    # 8. MCQ (From HS2024)
    # ==========================================================================
    st.markdown(f"### {t({'de': 'Übung', 'en': 'Exercise'})}")
    st.caption(content_10_4["mcq"]["source"])
    
    mcq = content_10_4["mcq"]
    opts = mcq["options"]
    opt_labels = [t({"de": o["de"], "en": o["en"]}) for o in opts]
    correct_idx = next((i for i, o in enumerate(opts) if o["id"] == mcq["correct_id"]), 0)
    
    render_mcq(
        key_suffix="10_4_pvalue",
        question_text=t(mcq["question"]),
        options=opt_labels,
        correct_idx=correct_idx,
        solution_text_dict=mcq["solution"],
        success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
        error_msg_dict={"de": "Falsch.", "en": "Incorrect."},
        client=model,
        ai_context="Topic 10.4: The p-Value - testing calculation of p-value for two-sided z-test with known variance",
        course_id="vwl",
        topic_id="10",
        subtopic_id="10.4",
        question_id="10_4_pvalue"
    )
