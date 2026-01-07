# Topic 10.3: Power Function and Types of Errors (Gütefunktion und Arten von Fehlern)
# ULTRATHINK Feynman-style implementation: "The Smoke Detector Analogy"
# 
# THE BIG IDEA: Every hypothesis test is like a smoke detector.
# Two ways to fail: cry wolf (Type I) or miss the fire (Type II).
# The interactive shows the SEESAW effect - you can't win at both.

import streamlit as st
import numpy as np
import plotly.graph_objects as go
from scipy import stats
from utils.localization import t
from utils.quiz_helper import render_mcq
from utils.ask_yourself import render_ask_yourself
from utils.exam_essentials import render_exam_essentials
from utils.layouts.foundation import inject_equal_height_css

# ==============================================================================
# CONTENT DICTIONARY
# ==============================================================================

content_10_3 = {
    "title": {"de": "10.3 Gütefunktion und Arten von Fehlern", "en": "10.3 Power Function and Types of Errors"},
    
    # --- THE SMOKE DETECTOR ANALOGY ---
    "intuition": {
        "de": """<strong>Stell dir vor, du baust einen Rauchmelder:</strong><br><br>
Der Rauchmelder muss eine einfache Frage beantworten: <strong>«Gibt es Feuer?»</strong><br><br>
<strong>Zwei Arten von Fehlern sind möglich:</strong><br>
• <span style="color:#FF4B4B; font-weight:600;">FEHLALARM</span> — Der Melder kreischt wegen angebranntem Toast. Kein echtes Feuer, aber Panik.<br>
• <span style="color:#F97316; font-weight:600;">VERSCHLAFENER BRAND</span> — Der Melder bleibt stumm bei echtem Feuer. Katastrophe!<br><br>
<em>Je empfindlicher der Melder (kleinerer kritischer Wert), desto mehr Fehlalarme — aber auch weniger verschlafene Brände. Das ist der Trade-off.</em>""",
        "en": """<strong>Imagine you're building a smoke detector:</strong><br><br>
The detector must answer a simple question: <strong>«Is there a fire?»</strong><br><br>
<strong>Two types of mistakes are possible:</strong><br>
• <span style="color:#FF4B4B; font-weight:600;">FALSE ALARM</span> — The detector screams at burnt toast. No real fire, but panic.<br>
• <span style="color:#F97316; font-weight:600;">MISSED FIRE</span> — The detector stays silent during a real fire. Catastrophe!<br><br>
<em>The more sensitive the detector (smaller critical value), the more false alarms — but also fewer missed fires. That's the trade-off.</em>"""
    },
    
    # --- 2x2 DECISION MATRIX CONTENT ---
    "matrix": {
        "header_reality": {"de": "Realität", "en": "Reality"},
        "header_decision": {"de": "Entscheidung", "en": "Decision"},
        "h0_true": {"de": "H₀ wahr (kein Feuer)", "en": "H₀ true (no fire)"},
        "h0_false": {"de": "H₀ falsch (echtes Feuer)", "en": "H₀ false (real fire)"},
        "dont_reject": {"de": "H₀ nicht ablehnen", "en": "Don't reject H₀"},
        "reject": {"de": "H₀ ablehnen", "en": "Reject H₀"},
        "correct_tn": {"de": "Richtig: Kein Alarm, kein Feuer", "en": "Correct: No alarm, no fire"},
        "correct_tp": {"de": "Richtig: Alarm bei Feuer = Power (1-β)", "en": "Correct: Alarm on fire = Power (1-β)"},
        "type1": {"de": "Typ-I-Fehler (α): Fehlalarm!", "en": "Type I Error (α): False alarm!"},
        "type2": {"de": "Typ-II-Fehler (β): Brand verschlafen!", "en": "Type II Error (β): Missed fire!"}
    },
    
    # --- TYPE I ERROR ---
    "type1": {
        "title": {"de": "Typ-I-Fehler (α)", "en": "Type I Error (α)"},
        "subtitle": {"de": "«Fehlalarm»", "en": "«False Alarm»"},
        "explanation": {
            "de": "Du lehnst H₀ ab, <strong>obwohl H₀ wahr ist</strong>.<br>Wie ein Rauchmelder, der bei Toast kreischt.",
            "en": "You reject H₀ <strong>even though H₀ is true</strong>.<br>Like a smoke detector screaming at toast."
        },
        "formula_desc": {"de": "Wahrscheinlichkeit eines Fehlalarms", "en": "Probability of a false alarm"}
    },
    
    # --- TYPE II ERROR ---
    "type2": {
        "title": {"de": "Typ-II-Fehler (β)", "en": "Type II Error (β)"},
        "subtitle": {"de": "«Verschlafener Brand»", "en": "«Missed Fire»"},
        "explanation": {
            "de": "Du behältst H₀, <strong>obwohl H₀ falsch ist</strong>.<br>Wie ein Rauchmelder, der bei echtem Feuer schweigt.",
            "en": "You keep H₀ <strong>even though H₀ is false</strong>.<br>Like a smoke detector staying silent during a fire."
        },
        "formula_desc": {"de": "Wahrscheinlichkeit, einen echten Effekt zu verpassen", "en": "Probability of missing a real effect"}
    },
    
    # --- POWER ---
    "power": {
        "title": {"de": "Güte (Power) = 1 - β", "en": "Power = 1 - β"},
        "subtitle": {"de": "«Treffsicherheit»", "en": "«Detection Rate»"},
        "explanation": {
            "de": "Die Wahrscheinlichkeit, H₀ korrekt abzulehnen, <strong>wenn H₀ falsch ist</strong>.<br>Wie oft der Melder bei echtem Feuer anspringt.",
            "en": "The probability of correctly rejecting H₀ <strong>when H₀ is false</strong>.<br>How often the detector goes off during a real fire."
        },
        "formula_desc": {"de": "Je höher, desto besser. Ziel: Power ≥ 80%", "en": "Higher is better. Goal: Power ≥ 80%"}
    },
    
    # --- THE KEY INSIGHT ---
    "key_insight": {
        "de": """<strong>Das Dilemma:</strong><br>
• Senkst du α (weniger Fehlalarme), <strong>steigt β</strong> (mehr verschlafene Brände).<br>
• Senkst du β (weniger verschlafene Brände), <strong>steigt α</strong> (mehr Fehlalarme).<br><br>
<strong>Einziger Ausweg:</strong> Grössere Stichprobe (n↑) → Beide Fehler sinken!""",
        "en": """<strong>The Dilemma:</strong><br>
• Lower α (fewer false alarms), <strong>β increases</strong> (more missed fires).<br>
• Lower β (fewer missed fires), <strong>α increases</strong> (more false alarms).<br><br>
<strong>Only escape:</strong> Larger sample size (n↑) → Both errors decrease!"""
    },
    
    # --- ASK YOURSELF ---
    "frag_dich": {
        "header": {
            "de": "Frag dich: Verstehst du die Fehlertypen?",
            "en": "Ask yourself: Do you understand the error types?"
        },
        "questions": [
            {"de": "Ein Schwangerschaftstest zeigt positiv, aber du bist nicht schwanger — welcher Fehler?",
             "en": "A pregnancy test shows positive, but you're not pregnant — which error?"},
            {"de": "Ein Krebstest zeigt negativ, aber du hast Krebs — welcher Fehler ist SCHLIMMER?",
             "en": "A cancer test shows negative, but you have cancer — which error is WORSE?"},
            {"de": "Wie kannst du BEIDE Fehler gleichzeitig senken?",
             "en": "How can you reduce BOTH errors at the same time?"},
            {"de": "Warum setzen Forscher α typisch auf 5% und nicht auf 0.1%?",
             "en": "Why do researchers typically set α at 5% and not 0.1%?"}
        ],
        "conclusion": {
            "de": "Goldene Regel: α kontrollierst DU, β ist eine KONSEQUENZ!",
            "en": "Golden Rule: YOU control α, β is a CONSEQUENCE!"
        }
    },
    
    # --- EXAM ESSENTIALS ---
    "exam_essentials": {
        "trap": {
            "de": "«H₀ nicht ablehnen» bedeutet NICHT «H₀ ist wahr»! Es heisst nur: zu wenig Beweis.",
            "en": "«Not rejecting H₀» does NOT mean «H₀ is true»! It just means: insufficient evidence."
        },
        "trap_rule": {
            "de": "Sage nie «H₀ akzeptieren» — sage «H₀ nicht ablehnen»",
            "en": "Never say «accept H₀» — say «fail to reject H₀»"
        },
        "tips": [
            {
                "tip": {"de": "α wird VOR dem Test festgelegt (typisch: 5%)", "en": "α is set BEFORE the test (typically: 5%)"},
                "why": {"de": "Du darfst α nicht anpassen, nachdem du die Daten gesehen hast!", "en": "You cannot adjust α after seeing the data!"}
            },
            {
                "tip": {"de": "Grösseres n → höhere Power (1-β)", "en": "Larger n → higher Power (1-β)"},
                "why": {"de": "Mehr Daten = bessere Unterscheidung zwischen H₀ und H₁.", "en": "More data = better discrimination between H₀ and H₁."}
            },
            {
                "tip": {"de": "Power ≥ 80% ist der Goldstandard", "en": "Power ≥ 80% is the gold standard"},
                "why": {"de": "Bei weniger Power ist dein Test zu schwach, um echte Effekte zu finden.", "en": "With less power, your test is too weak to find real effects."}
            }
        ]
    },
    
    # --- MCQ ---
    "mcq": {
        "question": {
            "de": "Ein Arzt möchte testen, ob ein neues Medikament wirksamer ist als ein Placebo. Welche Aussage ist KORREKT?",
            "en": "A doctor wants to test whether a new drug is more effective than a placebo. Which statement is CORRECT?"
        },
        "options": [
            {"id": "a", "de": "Ein Typ-I-Fehler bedeutet: Das Medikament wirkt nicht, aber wir behaupten es wirkt", 
             "en": "A Type I error means: The drug doesn't work, but we claim it works"},
            {"id": "b", "de": "Ein Typ-II-Fehler bedeutet: Das Medikament wirkt, aber wir behaupten es wirkt nicht", 
             "en": "A Type II error means: The drug works, but we claim it doesn't work"},
            {"id": "c", "de": "Beide (a) und (b) sind korrekt", 
             "en": "Both (a) and (b) are correct"},
            {"id": "d", "de": "Power = β", 
             "en": "Power = β"}
        ],
        "correct_id": "c",
        "solution": {
            "de": """<strong>Richtig: (c) Beide sind korrekt.</strong><br><br>
<strong>Typ-I-Fehler (α):</strong> H₀ ist wahr (Medikament wirkt NICHT), aber wir lehnen H₀ ab (behaupten es wirkt).<br>
<strong>Typ-II-Fehler (β):</strong> H₀ ist falsch (Medikament WIRKT), aber wir behalten H₀ (behaupten es wirkt nicht).<br><br>
(d) ist falsch: Power = 1 - β, nicht β.""",
            "en": """<strong>Correct: (c) Both are correct.</strong><br><br>
<strong>Type I Error (α):</strong> H₀ is true (drug does NOT work), but we reject H₀ (claim it works).<br>
<strong>Type II Error (β):</strong> H₀ is false (drug DOES work), but we keep H₀ (claim it doesn't work).<br><br>
(d) is wrong: Power = 1 - β, not β."""
        }
    }
}


# ==============================================================================
# THE 2x2 DECISION MATRIX VISUALIZATION
# ==============================================================================

def render_decision_matrix():
    """Render the 2x2 decision matrix with semantic colors."""
    
    matrix = content_10_3["matrix"]
    
    # Build the HTML table with semantic colors
    table_html = f"""
<div style="overflow-x: auto;">
<table style="width:100%; border-collapse: collapse; font-size: 0.95em;">
    <thead>
        <tr style="background: #f4f4f5;">
            <th style="border: 1px solid #d4d4d8; padding: 12px; text-align: center;"></th>
            <th style="border: 1px solid #d4d4d8; padding: 12px; text-align: center; font-weight: 600; color: #007AFF;">{t(matrix['h0_true'])}</th>
            <th style="border: 1px solid #d4d4d8; padding: 12px; text-align: center; font-weight: 600; color: #F97316;">{t(matrix['h0_false'])}</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="border: 1px solid #d4d4d8; padding: 12px; text-align: center; font-weight: 600; background: #f4f4f5;">{t(matrix['dont_reject'])}</td>
            <td style="border: 1px solid #d4d4d8; padding: 16px; text-align: center; background: #dcfce7; color: #166534;">
                <strong>✓</strong><br>{t(matrix['correct_tn'])}
            </td>
            <td style="border: 1px solid #d4d4d8; padding: 16px; text-align: center; background: #ffedd5; color: #9a3412;">
                <strong>β</strong><br>{t(matrix['type2'])}
            </td>
        </tr>
        <tr>
            <td style="border: 1px solid #d4d4d8; padding: 12px; text-align: center; font-weight: 600; background: #f4f4f5;">{t(matrix['reject'])}</td>
            <td style="border: 1px solid #d4d4d8; padding: 16px; text-align: center; background: #fee2e2; color: #991b1b;">
                <strong>α</strong><br>{t(matrix['type1'])}
            </td>
            <td style="border: 1px solid #d4d4d8; padding: 16px; text-align: center; background: #dcfce7; color: #166534;">
                <strong>1-β</strong><br>{t(matrix['correct_tp'])}
            </td>
        </tr>
    </tbody>
</table>
</div>
"""
    st.markdown(table_html, unsafe_allow_html=True)


# ==============================================================================
# INTERACTIVE: THE α-β SEESAW (The WOW Element)
# ==============================================================================

@st.fragment
def power_tradeoff_visualizer():
    """
    THE WOW ELEMENT: Interactive visualization showing the α-β trade-off.
    
    Two overlapping distributions (H₀ and H₁) with a movable critical value.
    Students visually SEE that reducing α increases β and vice versa.
    The only way to improve both is to increase n.
    """
    
    # === SCENARIO BOX ===
    scenario_text = t({
        "de": """<strong>Szenario: Der Fabriktest</strong><br>
Eine Fabrik produziert Schrauben mit einem Sollgewicht von µ₀ = 10g. Der Qualitätsmanager testet, ob eine neue Maschine vom Sollgewicht abweicht.<br><br>
<strong>Mission:</strong> Bewege die Regler und beobachte, wie α und β sich gegenseitig beeinflussen!""",
        "en": """<strong>Scenario: The Factory Test</strong><br>
A factory produces screws with a target weight of µ₀ = 10g. The quality manager tests whether a new machine deviates from the target.<br><br>
<strong>Mission:</strong> Move the sliders and observe how α and β affect each other!"""
    })
    
    st.markdown(f"""
<div style="background: #f4f4f5; border-left: 4px solid #a1a1aa; 
            padding: 12px 16px; border-radius: 8px; color: #3f3f46;">
{scenario_text}
</div>
""", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # === CSS FOR BLUE SLIDERS ===
    from utils.layouts.foundation import inject_slider_css
    inject_slider_css([
        {"label_contains": "Kritischer", "color": "#007AFF"},
        {"label_contains": "Critical", "color": "#007AFF"},
        {"label_contains": "Stichprobengrösse", "color": "#007AFF"},
        {"label_contains": "Sample", "color": "#007AFF"},
    ])
    
    # === CONTROLS ===
    col_ctrl, col_chart = st.columns([1, 1.8], gap="medium")
    
    with col_ctrl:
        # Critical value slider (determines α directly)
        st.markdown(f"**{t({'de': 'Kritischer Wert c', 'en': 'Critical Value c'})}**")
        c_val = st.slider(
            t({"de": "Kritischer Wert", "en": "Critical value"}),
            min_value=1.0, max_value=3.0, value=1.96, step=0.05,
            key="power_c_slider",
            label_visibility="collapsed"
        )
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Sample size slider
        st.markdown(f"**{t({'de': 'Stichprobengrösse n', 'en': 'Sample Size n'})}**")
        n_val = st.slider(
            t({"de": "Stichprobengrösse", "en": "Sample size"}),
            min_value=10, max_value=100, value=30, step=5,
            key="power_n_slider",
            label_visibility="collapsed"
        )
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Effect size (fixed for simplicity, but shown)
        effect_size = 0.5  # Cohen's d = 0.5 (medium effect)
        st.caption(t({"de": f"Effektstärke: mittel (d = {effect_size})", 
                      "en": f"Effect size: medium (d = {effect_size})"}))
        
        st.markdown("---")
        
        # === COMPUTED VALUES ===
        # Standard error
        sigma = 2.0  # Population SD
        se = sigma / np.sqrt(n_val)
        
        # True mean under H₁ (effect size determines this)
        mu_0 = 10.0
        mu_1 = mu_0 + effect_size * sigma  # H₁: µ = 11g
        
        # Alpha (probability of rejecting H₀ when H₀ is true)
        # For two-sided test: α = 2 * P(Z > c)
        alpha = 2 * (1 - stats.norm.cdf(c_val))
        
        # Beta (probability of NOT rejecting H₀ when H₁ is true)
        # For right-tail: β = P(Z < c - (µ₁ - µ₀)/SE | H₁)
        # Simplified for one-sided right:
        z_beta = c_val - (mu_1 - mu_0) / se
        beta = stats.norm.cdf(z_beta)
        
        power = 1 - beta
        
        # Display values with color coding
        alpha_pct = alpha * 100
        beta_pct = beta * 100
        power_pct = power * 100
        
        st.markdown(f"""
<div style="background: #fee2e2; border-left: 4px solid #FF4B4B; padding: 10px 14px; border-radius: 6px; margin-bottom: 8px;">
<strong style="color: #991b1b;">α = {alpha_pct:.1f}%</strong><br>
<span style="color: #7f1d1d; font-size: 0.85em;">{t({"de": "Fehlalarm-Risiko", "en": "False alarm risk"})}</span>
</div>
""", unsafe_allow_html=True)
        
        st.markdown(f"""
<div style="background: #ffedd5; border-left: 4px solid #F97316; padding: 10px 14px; border-radius: 6px; margin-bottom: 8px;">
<strong style="color: #9a3412;">β = {beta_pct:.1f}%</strong><br>
<span style="color: #7c2d12; font-size: 0.85em;">{t({"de": "Verschlaf-Risiko", "en": "Miss rate"})}</span>
</div>
""", unsafe_allow_html=True)
        
        # Power box with conditional color (green if >= 80%, yellow otherwise)
        power_bg = "#dcfce7" if power >= 0.8 else "#fef3c7"
        power_border = "#16a34a" if power >= 0.8 else "#d97706"
        power_color = "#166534" if power >= 0.8 else "#92400e"
        power_status = t({"de": "Gut!", "en": "Good!"}) if power >= 0.8 else t({"de": "Zu schwach", "en": "Too weak"})
        
        st.markdown(f"""
<div style="background: {power_bg}; border-left: 4px solid {power_border}; padding: 10px 14px; border-radius: 6px;">
<strong style="color: {power_color};">Power = {power_pct:.1f}%</strong> {power_status}<br>
<span style="color: {power_color}; font-size: 0.85em;">{t({"de": "Treffsicherheit", "en": "Detection rate"})}</span>
</div>
""", unsafe_allow_html=True)
    
    with col_chart:
        # === THE VISUALIZATION: Two overlapping distributions ===
        x = np.linspace(mu_0 - 4*se, mu_1 + 4*se, 500)
        
        # H₀ distribution (centered at μ₀)
        y_h0 = stats.norm.pdf(x, loc=mu_0, scale=se)
        
        # H₁ distribution (centered at μ₁)  
        y_h1 = stats.norm.pdf(x, loc=mu_1, scale=se)
        
        fig = go.Figure()
        
        # Critical value in data units
        c_data = mu_0 + c_val * se
        c_data_left = mu_0 - c_val * se
        
        # --- H₀ DISTRIBUTION (Blue) ---
        # Non-rejection region (light blue fill)
        mask_h0_safe = (x >= c_data_left) & (x <= c_data)
        fig.add_trace(go.Scatter(
            x=x[mask_h0_safe], y=y_h0[mask_h0_safe],
            fill='tozeroy', fillcolor='rgba(0, 122, 255, 0.15)',
            line=dict(color='rgba(0,0,0,0)'),
            name=t({"de": "H₀ (kein Fehler)", "en": "H₀ (no error)"}),
            showlegend=True
        ))
        
        # Right rejection region under H₀ (α - RED - Type I Error)
        mask_h0_alpha_right = x > c_data
        fig.add_trace(go.Scatter(
            x=x[mask_h0_alpha_right], y=y_h0[mask_h0_alpha_right],
            fill='tozeroy', fillcolor='rgba(255, 75, 75, 0.4)',
            line=dict(color='rgba(0,0,0,0)'),
            name=f"α = {alpha_pct:.1f}% " + t({"de": "(Typ-I)", "en": "(Type I)"}),
            showlegend=True
        ))
        
        # Left rejection region under H₀ (α - RED)
        mask_h0_alpha_left = x < c_data_left
        fig.add_trace(go.Scatter(
            x=x[mask_h0_alpha_left], y=y_h0[mask_h0_alpha_left],
            fill='tozeroy', fillcolor='rgba(255, 75, 75, 0.4)',
            line=dict(color='rgba(0,0,0,0)'),
            showlegend=False
        ))
        
        # --- H₁ DISTRIBUTION (Orange/Green) ---
        # β region under H₁ (miss - ORANGE - Type II Error)
        mask_h1_beta = (x >= c_data_left) & (x <= c_data)
        fig.add_trace(go.Scatter(
            x=x[mask_h1_beta], y=y_h1[mask_h1_beta],
            fill='tozeroy', fillcolor='rgba(249, 115, 22, 0.35)',
            line=dict(color='rgba(0,0,0,0)'),
            name=f"β = {beta_pct:.1f}% " + t({"de": "(Typ-II)", "en": "(Type II)"}),
            showlegend=True
        ))
        
        # Power region under H₁ (correct detection - GREEN)
        mask_h1_power = x > c_data
        fig.add_trace(go.Scatter(
            x=x[mask_h1_power], y=y_h1[mask_h1_power],
            fill='tozeroy', fillcolor='rgba(22, 163, 74, 0.35)',
            line=dict(color='rgba(0,0,0,0)'),
            name=f"Power = {power_pct:.1f}%",
            showlegend=True
        ))
        
        # --- DISTRIBUTION CURVES (outlines) ---
        fig.add_trace(go.Scatter(
            x=x, y=y_h0,
            mode='lines',
            line=dict(color='#007AFF', width=2.5),
            name="H₀",
            showlegend=False
        ))
        
        fig.add_trace(go.Scatter(
            x=x, y=y_h1,
            mode='lines',
            line=dict(color='#F97316', width=2.5),
            name="H₁",
            showlegend=False
        ))
        
        # --- CRITICAL VALUE LINES ---
        fig.add_vline(x=c_data, line=dict(color='#1c1c1e', width=2, dash='dash'))
        fig.add_vline(x=c_data_left, line=dict(color='#1c1c1e', width=2, dash='dash'))
        
        # Add labels for distributions
        fig.add_annotation(x=mu_0, y=max(y_h0)*1.1, text="H₀", 
                          font=dict(color='#007AFF', size=14, family='Arial Black'),
                          showarrow=False)
        fig.add_annotation(x=mu_1, y=max(y_h1)*1.1, text="H₁", 
                          font=dict(color='#F97316', size=14, family='Arial Black'),
                          showarrow=False)
        
        fig.update_layout(
            height=320,
            margin=dict(l=20, r=20, t=40, b=60),
            xaxis=dict(
                title=t({"de": "Stichprobenmittelwert (g)", "en": "Sample Mean (g)"}),
                zeroline=False
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
                x=0.5,
                font=dict(size=11)
            ),
            clickmode='none',
            hovermode=False
        )
        
        st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
    
    # === THE AHA MOMENT: Dynamic Insight ===
    if alpha_pct < 2:
        insight = t({
            "de": "α ist sehr klein → Kaum Fehlalarme, aber du verpasst viele echte Effekte (β hoch, Power niedrig)!",
            "en": "α is very small → Few false alarms, but you miss many real effects (β high, Power low)!"
        })
        insight_color = "#F97316"
    elif power_pct >= 80:
        insight = t({
            "de": "Perfekt! Power ≥ 80% bedeutet: Du findest echte Effekte zuverlässig.",
            "en": "Perfect! Power ≥ 80% means: You reliably detect real effects."
        })
        insight_color = "#16a34a"
    elif power_pct < 50:
        insight = t({
            "de": "Achtung! Power < 50% = Der Test ist nutzlos (schlimmer als Münzwurf).",
            "en": "Warning! Power < 50% = The test is useless (worse than coin flip)."
        })
        insight_color = "#dc2626"
    else:
        insight = t({
            "de": "Erhöhe n um Power zu steigern — ohne α zu verändern!",
            "en": "Increase n to boost Power — without changing α!"
        })
        insight_color = "#6B7280"
    
    st.markdown(f"""
<div style="background: #f4f4f5; border-radius: 8px; padding: 12px 16px; margin-top: 8px;">
<span style="color: {insight_color}; font-weight: 600;">{insight}</span>
</div>
""", unsafe_allow_html=True)


# ==============================================================================
# MAIN RENDER FUNCTION
# ==============================================================================

def render_subtopic_10_3(model):
    """10.3 Gütefunktion und Arten von Fehlern — Power Function and Types of Errors"""
    
    st.header(t(content_10_3["title"]))
    st.markdown("---")
    
    # Inject equal height CSS for side-by-side containers
    inject_equal_height_css()
    
    # ==========================================================================
    # 1. THE SMOKE DETECTOR ANALOGY (Intuition First)
    # ==========================================================================
    st.markdown(f"### {t({'de': 'Die Kernidee: Der Rauchmelder', 'en': 'The Core Idea: The Smoke Detector'})}")
    
    with st.container(border=True):
        st.markdown(t(content_10_3["intuition"]), unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # ==========================================================================
    # 2. THE 2x2 DECISION MATRIX
    # ==========================================================================
    st.markdown(f"### {t({'de': 'Die Entscheidungsmatrix', 'en': 'The Decision Matrix'})}")
    
    with st.container(border=True):
        render_decision_matrix()
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # ==========================================================================
    # 3. THE THREE ERROR TYPES (Side by Side)
    # ==========================================================================
    st.markdown(f"### {t({'de': 'Die drei Konzepte', 'en': 'The Three Concepts'})}")
    
    # Type I and Type II side by side
    col1, col2 = st.columns(2, gap="medium")
    
    type1 = content_10_3["type1"]
    type2 = content_10_3["type2"]
    
    with col1:
        with st.container(border=True):
            # Red accent header
            st.markdown(f"""
<div style="color: #FF4B4B; font-size: 1.2em; font-weight: 700; margin-bottom: 4px;">{t(type1['title'])}</div>
<div style="font-style: italic; color: #6B7280; margin-bottom: 12px;">{t(type1['subtitle'])}</div>
""", unsafe_allow_html=True)
            st.latex(r"P(\text{Reject } H_0 \mid H_0 \text{ true}) = \alpha")
            st.markdown("---")
            st.markdown(t(type1['explanation']), unsafe_allow_html=True)
            st.caption(t(type1['formula_desc']))
    
    with col2:
        with st.container(border=True):
            # Orange accent header
            st.markdown(f"""
<div style="color: #F97316; font-size: 1.2em; font-weight: 700; margin-bottom: 4px;">{t(type2['title'])}</div>
<div style="font-style: italic; color: #6B7280; margin-bottom: 12px;">{t(type2['subtitle'])}</div>
""", unsafe_allow_html=True)
            st.latex(r"P(\text{Keep } H_0 \mid H_0 \text{ false}) = \beta")
            st.markdown("---")
            st.markdown(t(type2['explanation']), unsafe_allow_html=True)
            st.caption(t(type2['formula_desc']))
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Power (full width)
    power = content_10_3["power"]
    
    with st.container(border=True):
        # Green accent header
        st.markdown(f"""
<div style="color: #16a34a; font-size: 1.2em; font-weight: 700; margin-bottom: 4px;">{t(power['title'])}</div>
<div style="font-style: italic; color: #6B7280; margin-bottom: 12px;">{t(power['subtitle'])}</div>
""", unsafe_allow_html=True)
        st.latex(r"\pi(\theta) = P(T \in R \mid \theta) = 1 - \beta")
        st.markdown("---")
        st.markdown(t(power['explanation']), unsafe_allow_html=True)
        st.caption(t(power['formula_desc']))
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Key Insight Box
    st.markdown(f"""
<div style="background: #f4f4f5; border-left: 4px solid #a1a1aa; 
            padding: 12px 16px; border-radius: 8px; color: #3f3f46;">
{t(content_10_3['key_insight'])}
</div>
""", unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # ==========================================================================
    # 4. INTERACTIVE: THE α-β SEESAW
    # ==========================================================================
    st.markdown(f"### {t({'de': 'Interaktiv: Der α-β Trade-off', 'en': 'Interactive: The α-β Trade-off'})}")
    
    power_tradeoff_visualizer()
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # ==========================================================================
    # 5. ASK YOURSELF (Frag Dich)
    # ==========================================================================
    render_ask_yourself(
        header=content_10_3["frag_dich"]["header"],
        questions=content_10_3["frag_dich"]["questions"],
        conclusion=content_10_3["frag_dich"]["conclusion"]
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # ==========================================================================
    # 6. EXAM ESSENTIALS
    # ==========================================================================
    render_exam_essentials(
        trap=content_10_3["exam_essentials"]["trap"],
        trap_rule=content_10_3["exam_essentials"]["trap_rule"],
        tips=content_10_3["exam_essentials"]["tips"]
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # ==========================================================================
    # 7. MCQ
    # ==========================================================================
    st.markdown(f"### {t({'de': 'Übung', 'en': 'Exercise'})}")
    
    mcq = content_10_3["mcq"]
    opts = mcq["options"]
    opt_labels = [t({"de": o["de"], "en": o["en"]}) for o in opts]
    correct_idx = next((i for i, o in enumerate(opts) if o["id"] == mcq["correct_id"]), 0)
    
    render_mcq(
        key_suffix="10_3_errors",
        question_text=t(mcq["question"]),
        options=opt_labels,
        correct_idx=correct_idx,
        solution_text_dict=mcq["solution"],
        success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
        error_msg_dict={"de": "Falsch.", "en": "Incorrect."},
        client=model,
        ai_context="Topic 10.3: Power Function and Types of Errors - testing understanding of Type I (α) and Type II (β) errors, and power = 1-β",
        course_id="vwl",
        topic_id="10",
        subtopic_id="10.3",
        question_id="10_3_errors"
    )
