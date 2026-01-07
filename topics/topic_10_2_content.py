# Topic 10.2: Critical Region and Test Statistic (Kritischer Bereich und Teststatistik)
# ULTRATHINK Feynman-style implementation: "Nightclub Bouncer Analogy"
import streamlit as st
import numpy as np
import plotly.graph_objects as go
from scipy import stats
from utils.localization import t
from utils.quiz_helper import render_mcq
from utils.ask_yourself import render_ask_yourself
from utils.exam_essentials import render_exam_essentials
from utils.layouts import render_comparison, render_single_formula, render_steps
from utils.layouts.foundation import inject_equal_height_css

# ==============================================================================
# CONTENT DICTIONARY
# ==============================================================================

content_10_2 = {
    "title": {"de": "10.2 Kritischer Bereich und Teststatistik", "en": "10.2 Critical Region and Test Statistic"},
    
    # --- BOUNCER ANALOGY (Intuition) ---
    "intuition": {
        "de": """<strong>Stell dir einen Türsteher vor einem Club vor:</strong><br><br>
• Er prüft dein <strong>ALTER</strong> auf dem Ausweis (= Teststatistik $T$)<br>
• Wenn ALTER < 21 → <strong>EINTRITT VERWEIGERT</strong> ($H_0$ ablehnen)<br>
• Die Grenze 21 ist der <strong>kritische Wert $c$</strong><br>
• Alle Alter unter 21 bilden den <strong>Ablehnbereich $R$</strong><br><br>
<em>In der Statistik ist dein Stichprobenergebnis der "Ausweis" — und der kritische Wert ist die "Altersgrenze".</em>""",
        "en": """<strong>Imagine a bouncer at a nightclub:</strong><br><br>
• He checks your <strong>AGE</strong> on your ID (= test statistic $T$)<br>
• If AGE < 21 → <strong>ENTRY DENIED</strong> (reject $H_0$)<br>
• The threshold 21 is the <strong>critical value $c$</strong><br>
• All ages below 21 form the <strong>rejection region $R$</strong><br><br>
<em>In statistics, your sample result is the "ID" — and the critical value is the "age limit".</em>"""
    },
    
    # --- COMPARISON: S₀ vs S₁ ---
    "s0_card": {
        "title": {"de": "S₀ — Nicht-Ablehnbereich", "en": "S₀ — Non-Rejection Region"},
        "subtitle": {"de": "«Sichere Zone»", "en": "«Safe Zone»"},
        "content": {
            "de": "• $T \\notin R$ → $H_0$ wird NICHT abgelehnt<br>• Beweise zu schwach<br>• Status quo bleibt bestehen",
            "en": "• $T \\notin R$ → $H_0$ is NOT rejected<br>• Evidence too weak<br>• Status quo remains"
        }
    },
    "s1_card": {
        "title": {"de": "S₁ — Kritischer Bereich", "en": "S₁ — Critical Region"},
        "subtitle": {"de": "«Gefahrenzone»", "en": "«Danger Zone»"},
        "content": {
            "de": "• $T \\in R$ → $H_0$ wird ABGELEHNT<br>• Starke Beweise gegen $H_0$<br>• Schlussfolgerung ändert sich",
            "en": "• $T \\in R$ → $H_0$ is REJECTED<br>• Strong evidence against $H_0$<br>• Conclusion changes"
        }
    },
    
    # --- TEST STATISTIC ---
    "test_statistic": {
        "intuition": {
            "de": "Die Teststatistik misst: «Wie weit ist meine Stichprobe von der $H_0$-Behauptung entfernt?»",
            "en": "The test statistic measures: «How far is my sample from the $H_0$ claim?»"
        },
        "variables": [
            {"symbol": "T", "name": {"de": "Teststatistik", "en": "Test Statistic"}, 
             "desc": {"de": "Berechneter Wert aus deinen Daten", "en": "Calculated value from your data"}},
            {"symbol": "f", "name": {"de": "Funktion", "en": "Function"}, 
             "desc": {"de": "Formel zur Berechnung (z.B. $Z$-Wert, $t$-Wert)", "en": "Formula for calculation (e.g., $Z$-score, $t$-score)"}},
            {"symbol": "X_i", "name": {"de": "Stichprobendaten", "en": "Sample Data"}, 
             "desc": {"de": "Die einzelnen Beobachtungen", "en": "The individual observations"}}
        ],
        "insight": {
            "de": "Je grösser $|T|$, desto extremer ist deine Stichprobe — und desto eher lehnst du $H_0$ ab.",
            "en": "The larger $|T|$, the more extreme your sample — and the more likely you reject $H_0$."
        }
    },
    
    # --- STEPS: Finding Critical Value ---
    "steps": {
        "header": {"de": "Kritischen Wert finden", "en": "Finding the Critical Value"},
        "steps_list": [
            {
                "label": {"de": "Schritt 1: Signifikanzniveau wählen", "en": "Step 1: Choose Significance Level"},
                "content": {"de": "Typisch: $\\alpha = 5\\%$, $1\\%$, oder $10\\%$", "en": "Typical: $\\alpha = 5\\%$, $1\\%$, or $10\\%$"}
            },
            {
                "label": {"de": "Schritt 2: Kritischen Wert aus Tabelle", "en": "Step 2: Look Up Critical Value"},
                "content": {
                    "de": "• Zweiseitig: $c = z_{1-\\alpha/2}$<br>• Einseitig: $c = z_{1-\\alpha}$",
                    "en": "• Two-sided: $c = z_{1-\\alpha/2}$<br>• One-sided: $c = z_{1-\\alpha}$"
                }
            },
            {
                "label": {"de": "Schritt 3: Ablehnbereich definieren", "en": "Step 3: Define Rejection Region"},
                "content": {
                    "de": "$R = \\{T \\mid |T| > c\\}$ (zweiseitig)<br>$R = \\{T \\mid T > c\\}$ oder $\\{T \\mid T < -c\\}$ (einseitig)",
                    "en": "$R = \\{T \\mid |T| > c\\}$ (two-sided)<br>$R = \\{T \\mid T > c\\}$ or $\\{T \\mid T < -c\\}$ (one-sided)"
                }
            }
        ]
    },
    
    # --- ASK YOURSELF (NO LaTeX - use Unicode) ---
    "frag_dich": {
        "header": {
            "de": "Frag dich: Verstehst du den kritischen Bereich?",
            "en": "Ask yourself: Do you understand the critical region?"
        },
        "questions": [
            {"de": "Wenn α von 5% auf 1% sinkt — wird der kritische Bereich grösser oder kleiner?", 
             "en": "If α decreases from 5% to 1% — does the critical region get bigger or smaller?"},
            {"de": "T = 2.5 und c = 1.96 (zweiseitig). Lehnst du H₀ ab?", 
             "en": "T = 2.5 and c = 1.96 (two-sided). Do you reject H₀?"},
            {"de": "Was ist der Unterschied zwischen dem kritischen Wert c und der Teststatistik T?", 
             "en": "What's the difference between critical value c and test statistic T?"},
            {"de": "Warum hat ein zweiseitiger Test ZWEI kritische Werte?", 
             "en": "Why does a two-sided test have TWO critical values?"}
        ],
        "conclusion": {
            "de": "Goldene Regel: c kommt aus der Tabelle, T kommt aus deinen Daten!",
            "en": "Golden Rule: c comes from the table, T comes from your data!"
        }
    },
    
    # --- EXAM ESSENTIALS ---
    "exam_essentials": {
        "trap": {
            "de": "«Kritischer Wert» mit «Teststatistik» verwechseln — $c$ ist aus der Tabelle, $T$ ist aus deinen Daten!",
            "en": "Confusing «critical value» with «test statistic» — $c$ is from the table, $T$ is from your data!"
        },
        "trap_rule": {
            "de": "Merke: $c$ = Tabellenwert (fix), $T$ = Stichprobenwert (variabel)",
            "en": "Remember: $c$ = table value (fixed), $T$ = sample value (varies)"
        },
        "tips": [
            {
                "tip": {"de": "Immer Verteilung skizzieren — $c$ einzeichnen und Ablehnbereich schattieren", 
                        "en": "Always sketch the distribution — mark $c$ and shade the rejection region"},
                "why": {"de": "Visualisierung verhindert Vorzeichenfehler", "en": "Visualization prevents sign errors"}
            },
            {
                "tip": {"de": "Bei zweiseitigen Tests: $\\alpha$ aufteilen! Jeder Rand bekommt $\\alpha/2$", 
                        "en": "For two-sided tests: split $\\alpha$! Each tail gets $\\alpha/2$"},
                "why": {"de": "Bei $\\alpha = 5\\%$ zweiseitig: je 2.5% links und rechts", "en": "At $\\alpha = 5\\%$ two-sided: 2.5% on left and right each"}
            },
            {
                "tip": {"de": "Tabelle prüfen: $z$-Tabelle ($\\sigma$ bekannt) vs. $t$-Tabelle ($\\sigma$ unbekannt)", 
                        "en": "Check your table: $z$-table ($\\sigma$ known) vs. $t$-table ($\\sigma$ unknown)"},
                "why": {"de": "Falsche Tabelle → falscher kritischer Wert → falsche Entscheidung", 
                        "en": "Wrong table → wrong critical value → wrong decision"}
            }
        ]
    },
    
    # --- MCQ ---
    "mcq": {
        "question": {
            "de": "Bei einem zweiseitigen Test mit $\\alpha = 5\\%$ ist der kritische Wert $c = 1.96$. Die berechnete Teststatistik ist $T = 2.3$. Was ist die korrekte Entscheidung?",
            "en": "In a two-sided test with $\\alpha = 5\\%$, the critical value is $c = 1.96$. The calculated test statistic is $T = 2.3$. What is the correct decision?"
        },
        "options": [
            {"id": "a", "de": "$H_0$ nicht ablehnen, da $T < c$", "en": "Do not reject $H_0$, since $T < c$"},
            {"id": "b", "de": "$H_0$ ablehnen, da $|T| > c$", "en": "Reject $H_0$, since $|T| > c$"},
            {"id": "c", "de": "$H_0$ ablehnen, da $T = 2.3$ positiv ist", "en": "Reject $H_0$, since $T = 2.3$ is positive"},
            {"id": "d", "de": "Kann nicht entschieden werden ohne Stichprobengrösse", "en": "Cannot be decided without sample size"}
        ],
        "correct_id": "b",
        "solution": {
            "de": "<strong>Richtig: (b)</strong><br><br>Bei einem zweiseitigen Test vergleichen wir $|T|$ mit $c$.<br>$|T| = |2.3| = 2.3 > 1.96 = c$<br><br>Da der Betrag der Teststatistik grösser ist als der kritische Wert, fällt $T$ in den Ablehnbereich.<br><br>(a) ist falsch: Wir vergleichen $|T|$, nicht $T$.<br>(c) ist falsch: Das Vorzeichen allein ist nicht entscheidend.<br>(d) ist falsch: Die Stichprobengrösse ist bereits in $T$ eingeflossen.",
            "en": "<strong>Correct: (b)</strong><br><br>In a two-sided test, we compare $|T|$ with $c$.<br>$|T| = |2.3| = 2.3 > 1.96 = c$<br><br>Since the absolute value of the test statistic exceeds the critical value, $T$ falls in the rejection region.<br><br>(a) is wrong: We compare $|T|$, not $T$.<br>(c) is wrong: The sign alone is not decisive.<br>(d) is wrong: Sample size is already incorporated in $T$."
        }
    }
}

# ==============================================================================
# INTERACTIVE: CRITICAL REGION VISUALIZER
# ==============================================================================

@st.fragment
def critical_region_visualizer():
    """Interactive visualization showing how α and test type affect critical region."""
    
    # State initialization
    if "cr_alpha" not in st.session_state:
        st.session_state.cr_alpha = 0.05
    if "cr_test_type" not in st.session_state:
        st.session_state.cr_test_type = "two"
    
    # CSS to make st.button look like pills - ULTRATHINK FIX
    # Problem 1: Font color - use wildcard * to catch ALL nested elements
    # Problem 2: Size - use FIXED height (not min-height) with box-sizing: border-box
    st.markdown("""
<style>
/* ULTRATHINK: Force ALL buttons to FIXED size and WHITE text */
.stButton > button,
.stButton > button[kind="secondary"],
.stButton > button[kind="primary"],
div[data-testid="stButton"] > button,
[data-testid="stHorizontalBlock"] .stButton > button {
    border-radius: 20px !important;
    padding: 8px 16px !important;
    font-weight: 500 !important;
    font-size: 0.9em !important;
    height: 38px !important;
    min-height: 38px !important;
    max-height: 38px !important;
    border: 1px solid #000 !important;
    background: #000 !important;
    background-color: #000 !important;
    color: #fff !important;
    box-sizing: border-box !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
}
.stButton > button:hover,
div[data-testid="stButton"] > button:hover {
    background: #333 !important;
    background-color: #333 !important;
    border-color: #333 !important;
}
/* CRITICAL: Force ALL nested elements to white text */
.stButton > button *,
div[data-testid="stButton"] > button * {
    color: #fff !important;
    margin: 0 !important;
    padding: 0 !important;
}
</style>
""", unsafe_allow_html=True)
    
    # SHARED PILL STYLE - EXACT SAME for selected (HTML) and unselected (st.button via CSS)
    PILL_STYLE = """background:#000;color:#fff;
        padding:8px 16px;border-radius:20px;text-align:center;
        font-weight:500;height:38px;box-sizing:border-box;
        display:flex;align-items:center;justify-content:center;"""
    
    # Scenario box
    scenario_label = t({"de": "Szenario", "en": "Scenario"})
    scenario_text = t({"de": "Eine Qualitätsingenieurin testet, ob die Maschineneinstellung μ = 100g ist. Sie verwendet verschiedene Signifikanzniveaus und Testarten.", 
                       "en": "A quality engineer tests whether machine output μ = 100g. She uses different significance levels and test types."})
    st.markdown(f"""
<div style="background: #f4f4f5; border-left: 4px solid #a1a1aa; 
            padding: 12px 16px; border-radius: 8px; color: #3f3f46; margin-bottom: 16px;">
<strong>{scenario_label}:</strong><br>
{scenario_text}
</div>
""", unsafe_allow_html=True)
    
    # Controls
    col_ctrl, col_chart = st.columns([1, 1.8], gap="medium")
    
    with col_ctrl:
        alpha_label = t({'de': 'Signifikanzniveau', 'en': 'Significance Level'})
        st.markdown(f"**{alpha_label}** α")
        
        # Alpha selection - consistent sizing
        alpha_options = [("1%", 0.01), ("5%", 0.05), ("10%", 0.10)]
        alpha_cols = st.columns(3)
        for i, (label, val) in enumerate(alpha_options):
            with alpha_cols[i]:
                is_selected = st.session_state.cr_alpha == val
                if is_selected:
                    # Selected state - SAME style as CSS for consistency
                    st.markdown(f'<div style="{PILL_STYLE}font-size:0.9em;">{label}</div>', 
                        unsafe_allow_html=True)
                else:
                    # Unselected - styled by CSS above
                    if st.button(label, key=f"alpha_{val}", use_container_width=True):
                        st.session_state.cr_alpha = val
                        st.rerun(scope="fragment")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        st.markdown(f"**{t({'de': 'Test-Typ', 'en': 'Test Type'})}**")
        
        # Test type selection - consistent sizing
        test_options = [
            ("←", "left"),
            ("↔", "two"),
            ("→", "right")
        ]
        test_cols = st.columns(3)
        for i, (symbol, key) in enumerate(test_options):
            with test_cols[i]:
                is_selected = st.session_state.cr_test_type == key
                if is_selected:
                    # Selected state - SAME style as CSS for consistency
                    st.markdown(f'<div style="{PILL_STYLE}font-size:1.1em;">{symbol}</div>', 
                        unsafe_allow_html=True)
                else:
                    # Unselected - styled by CSS above
                    if st.button(symbol, key=f"test_{key}", use_container_width=True):
                        st.session_state.cr_test_type = key
                        st.rerun(scope="fragment")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Show computed critical value
        alpha = st.session_state.cr_alpha
        test_type = st.session_state.cr_test_type
        
        if test_type == "two":
            c = stats.norm.ppf(1 - alpha/2)
            c_str = f"±{c:.3f}"
            c_label = t({"de": f"Kritische Werte: $c = {c_str}$", "en": f"Critical values: $c = {c_str}$"})
        elif test_type == "right":
            c = stats.norm.ppf(1 - alpha)
            c_str = f"{c:.3f}"
            c_label = t({"de": f"Kritischer Wert: $c = {c_str}$", "en": f"Critical value: $c = {c_str}$"})
        else:  # left
            c = stats.norm.ppf(alpha)
            c_str = f"{c:.3f}"
            c_label = t({"de": f"Kritischer Wert: $c = {c_str}$", "en": f"Critical value: $c = {c_str}$"})
        
        alpha_pct = int(alpha * 100)
        # Simple text display - no border
        st.markdown(f"**{c_label}**")
        st.markdown(f"α = {alpha_pct}%")
    
    with col_chart:
        # Create normal distribution curve
        x = np.linspace(-4, 4, 500)
        y = stats.norm.pdf(x)
        
        fig = go.Figure()
        
        # Non-rejection region (blue fill)
        if test_type == "two":
            c_val = stats.norm.ppf(1 - alpha/2)
            # Middle (safe) region
            mask_safe = (x >= -c_val) & (x <= c_val)
            fig.add_trace(go.Scatter(
                x=x[mask_safe], y=y[mask_safe],
                fill='tozeroy', fillcolor='rgba(0, 122, 255, 0.3)',
                line=dict(color='rgba(0,0,0,0)'),
                name=t({"de": "Nicht ablehnen", "en": "Don't reject"}),
                showlegend=True
            ))
            # Left rejection region
            mask_left = x < -c_val
            fig.add_trace(go.Scatter(
                x=x[mask_left], y=y[mask_left],
                fill='tozeroy', fillcolor='rgba(255, 75, 75, 0.5)',
                line=dict(color='rgba(0,0,0,0)'),
                name=t({"de": "Ablehnen", "en": "Reject"}),
                showlegend=True
            ))
            # Right rejection region
            mask_right = x > c_val
            fig.add_trace(go.Scatter(
                x=x[mask_right], y=y[mask_right],
                fill='tozeroy', fillcolor='rgba(255, 75, 75, 0.5)',
                line=dict(color='rgba(0,0,0,0)'),
                showlegend=False
            ))
            # Critical value lines
            fig.add_vline(x=-c_val, line=dict(color='#FF4B4B', width=2, dash='dash'))
            fig.add_vline(x=c_val, line=dict(color='#FF4B4B', width=2, dash='dash'))
            
        elif test_type == "right":
            c_val = stats.norm.ppf(1 - alpha)
            # Safe region (left of c)
            mask_safe = x <= c_val
            fig.add_trace(go.Scatter(
                x=x[mask_safe], y=y[mask_safe],
                fill='tozeroy', fillcolor='rgba(0, 122, 255, 0.3)',
                line=dict(color='rgba(0,0,0,0)'),
                name=t({"de": "Nicht ablehnen", "en": "Don't reject"}),
                showlegend=True
            ))
            # Rejection region (right of c)
            mask_reject = x > c_val
            fig.add_trace(go.Scatter(
                x=x[mask_reject], y=y[mask_reject],
                fill='tozeroy', fillcolor='rgba(255, 75, 75, 0.5)',
                line=dict(color='rgba(0,0,0,0)'),
                name=t({"de": "Ablehnen", "en": "Reject"}),
                showlegend=True
            ))
            fig.add_vline(x=c_val, line=dict(color='#FF4B4B', width=2, dash='dash'))
            
        else:  # left
            c_val = stats.norm.ppf(alpha)
            # Safe region (right of c)
            mask_safe = x >= c_val
            fig.add_trace(go.Scatter(
                x=x[mask_safe], y=y[mask_safe],
                fill='tozeroy', fillcolor='rgba(0, 122, 255, 0.3)',
                line=dict(color='rgba(0,0,0,0)'),
                name=t({"de": "Nicht ablehnen", "en": "Don't reject"}),
                showlegend=True
            ))
            # Rejection region (left of c)
            mask_reject = x < c_val
            fig.add_trace(go.Scatter(
                x=x[mask_reject], y=y[mask_reject],
                fill='tozeroy', fillcolor='rgba(255, 75, 75, 0.5)',
                line=dict(color='rgba(0,0,0,0)'),
                name=t({"de": "Ablehnen", "en": "Reject"}),
                showlegend=True
            ))
            fig.add_vline(x=c_val, line=dict(color='#FF4B4B', width=2, dash='dash'))
        
        # Add the curve outline
        fig.add_trace(go.Scatter(
            x=x, y=y,
            mode='lines',
            line=dict(color='#1c1c1e', width=2),
            showlegend=False
        ))
        
        fig.update_layout(
            height=280,
            margin=dict(l=20, r=20, t=30, b=40),
            xaxis=dict(
                title=t({"de": "Teststatistik T", "en": "Test Statistic T"}),
                range=[-4, 4],
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
                y=-0.35,
                xanchor="center",
                x=0.5
            ),
            clickmode='none',
            hovermode=False
        )
        
        st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
    
    # Interpretation box - GREY CALLOUT (no green border!)
    alpha_pct = int(alpha * 100)
    c_val_str = f"{c:.3f}"
    if test_type == "two":
        interpretation = t({
            "de": f"Bei α = {alpha_pct}% und zweiseitigem Test: Lehne H₀ ab wenn |T| > {c_val_str}",
            "en": f"With α = {alpha_pct}% and two-sided test: Reject H₀ if |T| > {c_val_str}"
        })
    elif test_type == "right":
        interpretation = t({
            "de": f"Bei α = {alpha_pct}% und rechtsseitigem Test: Lehne H₀ ab wenn T > {c_val_str}",
            "en": f"With α = {alpha_pct}% and right-sided test: Reject H₀ if T > {c_val_str}"
        })
    else:
        interpretation = t({
            "de": f"Bei α = {alpha_pct}% und linksseitigem Test: Lehne H₀ ab wenn T < {c_val_str}",
            "en": f"With α = {alpha_pct}% and left-sided test: Reject H₀ if T < {c_val_str}"
        })
    
    # Simple bold text - no border
    st.markdown(f"**{interpretation}**")


# ==============================================================================
# MAIN RENDER FUNCTION
# ==============================================================================

def render_subtopic_10_2(model):
    """10.2 Kritischer Bereich und Teststatistik — Critical Region and Test Statistic"""
    
    st.header(t(content_10_2["title"]))
    st.markdown("---")
    
    # Inject equal height CSS for side-by-side containers
    inject_equal_height_css()
    
    # ==========================================================================
    # 1. THE BOUNCER ANALOGY (Intuition First)
    # ==========================================================================
    st.markdown(f"### {t({'de': 'Die Kernidee: Der Türsteher', 'en': 'The Core Idea: The Bouncer'})}")
    
    with st.container(border=True):
        st.markdown(t(content_10_2["intuition"]), unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # ==========================================================================
    # 2. S₀ vs S₁ (Side-by-Side Comparison) — BLACK HEADERS
    # ==========================================================================
    st.markdown(f"### {t({'de': 'Die zwei Bereiche', 'en': 'The Two Regions'})}")
    
    col1, col2 = st.columns(2, gap="medium")
    
    with col1:
        with st.container(border=True):
            # BLACK header (no colors)
            st.markdown(f"**{t(content_10_2['s0_card']['title'])}**")
            st.markdown(f"*{t(content_10_2['s0_card']['subtitle'])}*")
            st.markdown("---")
            st.markdown(t(content_10_2['s0_card']['content']), unsafe_allow_html=True)
    
    with col2:
        with st.container(border=True):
            # BLACK header (no colors)
            st.markdown(f"**{t(content_10_2['s1_card']['title'])}**")
            st.markdown(f"*{t(content_10_2['s1_card']['subtitle'])}*")
            st.markdown("---")
            st.markdown(t(content_10_2['s1_card']['content']), unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # ==========================================================================
    # 3. THE TEST STATISTIC
    # ==========================================================================
    st.markdown(f"### {t({'de': 'Die Teststatistik', 'en': 'The Test Statistic'})}")
    
    ts = content_10_2["test_statistic"]
    
    with st.container(border=True):
        # Intuition (italic, no math)
        st.markdown(f"*{t(ts['intuition'])}*")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # The formula
        st.latex(r"T = f(X_1, X_2, \ldots, X_n)")
        
        st.markdown("---")
        
        # Variable decoder
        st.markdown(f"**{t({'de': 'Variablen-Decoder', 'en': 'Variable Decoder'})}:**")
        for var in ts["variables"]:
            symbol = var["symbol"]
            name = t(var["name"])
            desc = t(var["desc"])
            st.markdown(f"• ${symbol}$ = **{name}** — {desc}")
        
        st.markdown("---")
        
        # Key insight
        st.markdown(f"""
<div style="background: #f4f4f5; border-left: 4px solid #a1a1aa; 
            padding: 12px 16px; border-radius: 8px; color: #3f3f46;">
<strong>{t({"de": "Aha-Moment", "en": "Key Insight"})}:</strong><br>
{t(ts['insight'])}
</div>
""", unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # ==========================================================================
    # 4. STEPS: Finding Critical Value
    # ==========================================================================
    st.markdown(f"### {t(content_10_2['steps']['header'])}")
    
    with st.container(border=True):
        for i, step in enumerate(content_10_2['steps']['steps_list']):
            if i > 0:
                st.markdown("---")
            st.markdown(f"**{t(step['label'])}**")
            st.markdown(t(step['content']), unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # ==========================================================================
    # 5. INTERACTIVE: CRITICAL REGION VISUALIZER
    # ==========================================================================
    st.markdown(f"### {t({'de': 'Interaktiv: Ablehnbereich visualisieren', 'en': 'Interactive: Visualize the Rejection Region'})}")
    
    critical_region_visualizer()
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # ==========================================================================
    # 6. ASK YOURSELF (Frag Dich)
    # ==========================================================================
    render_ask_yourself(
        header=content_10_2["frag_dich"]["header"],
        questions=content_10_2["frag_dich"]["questions"],
        conclusion=content_10_2["frag_dich"]["conclusion"]
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # ==========================================================================
    # 7. EXAM ESSENTIALS
    # ==========================================================================
    render_exam_essentials(
        trap=content_10_2["exam_essentials"]["trap"],
        trap_rule=content_10_2["exam_essentials"]["trap_rule"],
        tips=content_10_2["exam_essentials"]["tips"]
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # ==========================================================================
    # 8. MCQ
    # ==========================================================================
    st.markdown(f"### {t({'de': 'Übung', 'en': 'Exercise'})}")
    
    mcq = content_10_2["mcq"]
    opts = mcq["options"]
    opt_labels = [t({"de": o["de"], "en": o["en"]}) for o in opts]
    correct_idx = next((i for i, o in enumerate(opts) if o["id"] == mcq["correct_id"]), 0)
    
    render_mcq(
        key_suffix="10_2_critical",
        question_text=t(mcq["question"]),
        options=opt_labels,
        correct_idx=correct_idx,
        solution_text_dict=mcq["solution"],
        success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
        error_msg_dict={"de": "Falsch.", "en": "Incorrect."},
        client=model,
        ai_context="Topic 10.2: Critical Region and Test Statistic - testing understanding of rejection regions, critical values, and test statistics",
        course_id="vwl",
        topic_id="10",
        subtopic_id="10.2",
        question_id="10_2_critical"
    )
