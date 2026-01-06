# Topic 7.5: Streudiagramm (Scatter Plot)
# ULTRATHINK ENHANCED VERSION — "The Correlation Visualizer"
# Interactive: Correlation Slider with impeccable semantic design

import streamlit as st
import numpy as np
import plotly.graph_objects as go
from scipy import stats
from utils.localization import t
from utils.quiz_helper import render_mcq
from utils.ask_yourself import render_ask_yourself
from utils.exam_essentials import render_exam_essentials
from utils.worked_example import render_worked_example
from utils.layouts import (
    render_definition,
    render_comparison,
)
from utils.layouts.foundation import (
    intuition_box,
    grey_callout,
    inject_equal_height_css,
)

# ==============================================================================
# SEMANTIC COLOR PALETTE (Topic 7 conventions)
# ==============================================================================
COLOR_X = "#007AFF"        # Blue  — X variable (horizontal)
COLOR_Y = "#FF4B4B"        # Red   — Y variable (vertical)
COLOR_POSITIVE = "#16a34a" # Green — Positive correlation
COLOR_NEGATIVE = "#9B59B6" # Purple — Negative correlation
COLOR_NEUTRAL = "#6B7280"  # Gray  — Zero correlation / neutral
COLOR_LINE = "#000000"     # Black — Trend line


# ==============================================================================
# VISUAL COMPARISON: 1D vs 2D DATA (Like 7.4's qq_vs_histogram)
# ==============================================================================

@st.fragment
def univariate_vs_bivariate_visual():
    """
    Side-by-side visual comparison: 1D data (strip plot) vs 2D data (scatter plot).
    Uses same underlying values but shows the fundamental difference.
    """
    inject_equal_height_css()
    
    # Sample data
    np.random.seed(42)
    n = 20
    x = np.random.normal(50, 15, n)
    y = 0.8 * x + np.random.normal(0, 8, n)  # Correlated with X
    
    col1, col2 = st.columns(2, gap="medium")
    
    with col1:
        st.markdown(f"**{t({'de': 'Univariat (1D)', 'en': 'Univariate (1D)'})}** · *{t({'de': 'Nur X', 'en': 'Only X'})}*")
        
        # 1D Strip plot - points on X-axis
        fig_1d = go.Figure()
        fig_1d.add_trace(go.Scatter(
            x=x,
            y=[0] * n,  # All on same horizontal line
            mode="markers",
            marker=dict(color=COLOR_X, size=12, line=dict(width=1, color="white")),
            hovertemplate=f"X: %{{x:.1f}}<extra></extra>"
        ))
        
        fig_1d.update_layout(
            height=180,
            margin=dict(t=10, b=40, l=50, r=20),
            xaxis_title=t({"de": "Variable X", "en": "Variable X"}),
            yaxis=dict(visible=False, range=[-0.5, 0.5]),
            xaxis=dict(showgrid=True, gridcolor="#e5e7eb", range=[0, 100]),
            plot_bgcolor="white",
            paper_bgcolor="white"
        )
        st.plotly_chart(fig_1d, use_container_width=True, config={'displayModeBar': False})
        
        st.caption(t({
            "de": "Zeigt Verteilung EINER Variable (Spread, Center).",
            "en": "Shows distribution of ONE variable (spread, center)."
        }))
    
    with col2:
        st.markdown(f"**{t({'de': 'Bivariat (2D)', 'en': 'Bivariate (2D)'})}** · *{t({'de': 'X und Y', 'en': 'X and Y'})}*")
        
        # 2D Scatter plot
        fig_2d = go.Figure()
        fig_2d.add_trace(go.Scatter(
            x=x,
            y=y,
            mode="markers",
            marker=dict(color=COLOR_POSITIVE, size=12, line=dict(width=1, color="white")),
            hovertemplate=f"X: %{{x:.1f}}<br>Y: %{{y:.1f}}<extra></extra>"
        ))
        
        fig_2d.update_layout(
            height=180,
            margin=dict(t=10, b=40, l=50, r=20),
            xaxis_title=t({"de": "Variable X", "en": "Variable X"}),
            yaxis_title=t({"de": "Variable Y", "en": "Variable Y"}),
            xaxis=dict(showgrid=True, gridcolor="#e5e7eb", range=[0, 100]),
            yaxis=dict(showgrid=True, gridcolor="#e5e7eb"),
            plot_bgcolor="white",
            paper_bgcolor="white"
        )
        st.plotly_chart(fig_2d, use_container_width=True, config={'displayModeBar': False})
        
        st.caption(t({
            "de": "Zeigt BEZIEHUNG zwischen zwei Variablen.",
            "en": "Shows RELATIONSHIP between two variables."
        }))


# ==============================================================================
# CONTENT DICTIONARY — BILINGUAL (ULTRATHINK DEPTH)
# ==============================================================================

content_7_5 = {
    "title": {
        "de": "7.5 Streudiagramm",
        "en": "7.5 Scatter Plot"
    },
    "subtitle": {
        "de": "Das visuelle Werkzeug für zweidimensionale Zusammenhänge",
        "en": "The Visual Tool for Two-Dimensional Relationships"
    },
    
    # =========================================================================
    # INTUITION — THE "MAP" ANALOGY (NO EMOJIS)
    # =========================================================================
    "intuition": {
        "de": """<strong>Stell dir eine Landkarte vor:</strong> Jeder Punkt zeigt, 
        wo du zu einem bestimmten Zeitpunkt warst. Die X-Koordinate zeigt, wie weit du nach 
        <strong>Osten</strong> gegangen bist. Die Y-Koordinate zeigt, wie weit nach <strong>Norden</strong>.
        <br><br>
        <strong>Wenn alle Punkte in einer Linie nach Nordosten gehen</strong> → Starke positive Beziehung.
        <br>
        <strong>Wenn die Punkte zufällig verstreut sind</strong> → Keine erkennbare Beziehung.
        <br><br>
        <strong>Das ist ein Streudiagramm:</strong> Es zeigt, ob zwei Variablen <em>zusammen variieren</em> 
        oder <em>unabhängig voneinander</em> sind. Jeder Punkt ist ein Datenpaar (x, y).""",
        
        "en": """<strong>Imagine a map:</strong> Each dot shows where you were at a specific moment. 
        The X-coordinate shows how far you went <strong>East</strong>. The Y-coordinate shows how far 
        <strong>North</strong>.
        <br><br>
        <strong>If all dots line up toward the Northeast</strong> → Strong positive relationship.
        <br>
        <strong>If dots are randomly scattered</strong> → No recognizable relationship.
        <br><br>
        <strong>That's a scatter plot:</strong> It shows whether two variables <em>vary together</em> 
        or are <em>independent</em> of each other. Each point is a data pair (x, y)."""
    },
    
    # =========================================================================
    # DEFINITION
    # =========================================================================
    "definition": {
        "term": {"de": "Streudiagramm (Scatter Plot)", "en": "Scatter Plot"},
        "formal": {
            "de": "Ein Streudiagramm stellt Paare von Beobachtungen (xᵢ, yᵢ) als Punkte in einem zweidimensionalen Koordinatensystem dar. Es zeigt Beziehungen, Cluster und Ausreisser zwischen zwei Variablen.",
            "en": "A scatter plot represents pairs of observations (xᵢ, yᵢ) as points in a two-dimensional coordinate system. It reveals relationships, clusters, and outliers between two variables."
        },
        "plain": {
            "de": "X-Achse = Variable 1 | Y-Achse = Variable 2 | Jeder Punkt = Ein Datenpaar",
            "en": "X-axis = Variable 1 | Y-axis = Variable 2 | Each dot = One data pair"
        }
    },
    
    # =========================================================================
    # COMPARISON: 1D vs 2D DATA
    # =========================================================================
    "comparison": {
        "title": {"de": "Univariate vs. Bivariate Daten", "en": "Univariate vs. Bivariate Data"},
        "left": {
            "title": {"de": "Univariate Daten (1D)", "en": "Univariate Data (1D)"},
            "formula": None,
            "description": {
                "de": "<strong>Eine</strong> Variable pro Beobachtung.<br>Punkte liegen auf einer Linie.",
                "en": "<strong>One</strong> variable per observation.<br>Points lie on a line."
            },
            "example": {
                "de": "Histogramm, Boxplot, ECDF",
                "en": "Histogram, Boxplot, ECDF"
            }
        },
        "right": {
            "title": {"de": "Bivariate Daten (2D)", "en": "Bivariate Data (2D)"},
            "formula": None,
            "description": {
                "de": "<strong>Zwei</strong> Variablen pro Beobachtung.<br>Punkte verteilen sich in der Fläche.",
                "en": "<strong>Two</strong> variables per observation.<br>Points spread across the plane."
            },
            "example": {
                "de": "Streudiagramm, Korrelation",
                "en": "Scatter plot, Correlation"
            }
        }
    },
    
    # =========================================================================
    # WORKED EXAMPLE: Correlation Matching (Übung 3, Question 7)
    # =========================================================================
    "worked_example": {
        "header": {"de": "Beispiel: Korrelation ablesen", "en": "Example: Reading Correlation"},
        "problem": {
            "de": """<strong>Aufgabe (Übung 3):</strong> Vier Streudiagramme sind gegeben. 
            Ordne jeden der folgenden Korrelationskoeffizienten dem richtigen Diagramm zu:
            <br><br>
            <code style="background:#f4f4f5; padding:8px; border-radius:4px; display:block;">
            ρ = 0, ρ = -0.7, ρ = 0.6, ρ = 0.9
            </code>""",
            "en": """<strong>Problem (Exercise 3):</strong> Four scatter plots are given. 
            Match each of the following correlation coefficients to the correct diagram:
            <br><br>
            <code style="background:#f4f4f5; padding:8px; border-radius:4px; display:block;">
            ρ = 0, ρ = -0.7, ρ = 0.6, ρ = 0.9
            </code>"""
        },
        "steps": [
            {
                "label": {"de": "Schritt 1: Die Extremwerte erkennen", "en": "Step 1: Identify extreme values"},
                "latex": r"{\color{#16a34a}\rho = 0.9} \;\text{(fast perfekte Linie)} \quad {\color{#6B7280}\rho = 0} \;\text{(Punktwolke)}",
                "latex_en": r"{\color{#16a34a}\rho = 0.9} \;\text{(almost perfect line)} \quad {\color{#6B7280}\rho = 0} \;\text{(cloud)}",
                "note": {"de": "Leicht zu erkennen: engste Linie vs. zufällige Streuung", "en": "Easy to spot: tightest line vs. random scatter"}
            },
            {
                "label": {"de": "Schritt 2: Richtung prüfen", "en": "Step 2: Check direction"},
                "latex": r"{\color{#9B59B6}\rho = -0.7}: \;\text{Punkte fallen} \;\searrow \quad {\color{#16a34a}\rho = 0.6}: \;\text{Punkte steigen} \;\nearrow",
                "latex_en": r"{\color{#9B59B6}\rho = -0.7}: \;\text{Points fall} \;\searrow \quad {\color{#16a34a}\rho = 0.6}: \;\text{Points rise} \;\nearrow",
                "note": {"de": "Negativ = abfallend, Positiv = ansteigend", "en": "Negative = downward, Positive = upward"}
            },
            {
                "label": {"de": "Schritt 3: Stärke vergleichen", "en": "Step 3: Compare strength"},
                "latex": r"|{\color{#9B59B6}-0.7}| > |{\color{#16a34a}0.6}| \;\Rightarrow\; \text{engere Punktwolke bei } -0.7",
                "latex_en": r"|{\color{#9B59B6}-0.7}| > |{\color{#16a34a}0.6}| \;\Rightarrow\; \text{tighter cloud for } -0.7",
                "note": {"de": "Je näher an ±1, desto enger die Punkte um die Linie", "en": "Closer to ±1 = points tighter around the line"}
            }
        ],
        "answer": {
            "de": "Merken: Richtung (↗/↘) = Vorzeichen von ρ — Streubreite = Betrag von ρ — Keine Richtung → ρ ≈ 0",
            "en": "Remember: Direction (↗/↘) = sign of ρ — Scatter width = magnitude of ρ — No pattern → ρ ≈ 0"
        }
    },
    
    # =========================================================================
    # FRAG DICH
    # =========================================================================
    "frag_dich": {
        "header": {"de": "Frag dich: Verstehst du Streudiagramme?", "en": "Ask yourself: Do you understand scatter plots?"},
        "questions": [
            {
                "de": "Die Punkte bilden eine <strong>enge Linie von links-unten nach rechts-oben</strong> — ist ρ positiv oder negativ?",
                "en": "The points form a <strong>tight line from bottom-left to top-right</strong> — is ρ positive or negative?"
            },
            {
                "de": "Was bedeutet es, wenn die Punkte eine <strong>kreisförmige Wolke</strong> bilden?",
                "en": "What does it mean if the points form a <strong>circular cloud</strong>?"
            },
            {
                "de": "Welches Diagramm zeigt Zusammenhänge besser: <strong>Histogramm oder Streudiagramm</strong>?",
                "en": "Which diagram shows relationships better: <strong>Histogram or Scatter plot</strong>?"
            },
            {
                "de": "Ein <strong>Ausreisser</strong> liegt weit von allen anderen Punkten — wie beeinflusst er ρ?",
                "en": "An <strong>outlier</strong> lies far from all other points — how does it affect ρ?"
            }
        ],
        "conclusion": {
            "de": "Positiv (↗) | ρ ≈ 0 | Streudiagramm | Ausreisser verzerren ρ stark!",
            "en": "Positive (↗) | ρ ≈ 0 | Scatter plot | Outliers distort ρ strongly!"
        }
    },
    
    # =========================================================================
    # EXAM ESSENTIALS
    # =========================================================================
    "exam_essentials": {
        "trap": {
            "de": "<strong>Korrelation ≠ Kausalität:</strong> Nur weil zwei Variablen zusammen variieren, heisst das nicht, dass eine die andere <em>verursacht</em>. Beispiel: Eiscremeverkäufe und Sonnenbrandrate korrelieren — aber Eis verursacht keinen Sonnenbrand!",
            "en": "<strong>Correlation ≠ Causation:</strong> Just because two variables vary together doesn't mean one <em>causes</em> the other. Example: Ice cream sales and sunburn rate correlate — but ice cream doesn't cause sunburn!"
        },
        "trap_rule": {
            "de": "Sage immer: 'X und Y sind korreliert' — niemals 'X verursacht Y' (ohne weiteren Beweis).",
            "en": "Always say: 'X and Y are correlated' — never 'X causes Y' (without further evidence)."
        },
        "tips": [
            {
                "tip": {"de": "Richtung ablesen: Punkte ↗ = positiv, ↘ = negativ", "en": "Read direction: Points ↗ = positive, ↘ = negative"},
                "why": {"de": "Das Vorzeichen von $\\rho$ entspricht der Steigung der gedachten Linie.", "en": "The sign of $\\rho$ matches the slope of the imaginary line."}
            },
            {
                "tip": {"de": "Streubreite = Stärke: Enge Linie → $|\\rho|$ nahe 1", "en": "Scatter width = Strength: Tight line → $|\\rho|$ close to 1"},
                "why": {"de": "Je weniger Abweichung von der Linie, desto stärker der Zusammenhang.", "en": "Less deviation from the line means stronger relationship."}
            },
            {
                "tip": {"de": "Ausreisser prüfen: Ein Punkt kann $\\rho$ stark verändern", "en": "Check outliers: One point can dramatically change $\\rho$"},
                "why": {"de": "Korrelation ist nicht robust — immer das Diagramm visuell prüfen!", "en": "Correlation is not robust — always check the plot visually!"}
            }
        ]
    },
    
    # =========================================================================
    # MCQ QUESTIONS (2 NEW)
    # =========================================================================
    "mcq_1": {
        "question": {
            "de": "In einem Streudiagramm bilden die Punkte eine enge Linie, die von links-oben nach rechts-unten verläuft. Was ist der wahrscheinlichste Korrelationskoeffizient?",
            "en": "In a scatter plot, the points form a tight line running from top-left to bottom-right. What is the most likely correlation coefficient?"
        },
        "options": [
            {"id": "a", "de": "$\\rho \\approx +0.9$", "en": "$\\rho \\approx +0.9$"},
            {"id": "b", "de": "$\\rho \\approx -0.9$", "en": "$\\rho \\approx -0.9$"},
            {"id": "c", "de": "$\\rho \\approx 0$", "en": "$\\rho \\approx 0$"},
            {"id": "d", "de": "$\\rho \\approx +0.3$", "en": "$\\rho \\approx +0.3$"}
        ],
        "correct_id": "b",
        "solution": {
            "de": "<strong>Richtig ist (b)</strong><br>Links-oben nach rechts-unten = <strong>abfallend</strong> → negativer Korrelationskoeffizient. 'Enge Linie' bedeutet <strong>starke</strong> Korrelation → nahe an -1.",
            "en": "<strong>Correct is (b)</strong><br>Top-left to bottom-right = <strong>downward</strong> → negative correlation coefficient. 'Tight line' means <strong>strong</strong> correlation → close to -1."
        }
    },
    "mcq_2": {
        "question": {
            "de": "Was kann man aus einem Streudiagramm NICHT direkt ablesen?",
            "en": "What can you NOT directly read from a scatter plot?"
        },
        "options": [
            {"id": "a", "de": "Die Richtung des Zusammenhangs (positiv/negativ)", "en": "The direction of the relationship (positive/negative)"},
            {"id": "b", "de": "Die ungefähre Stärke des Zusammenhangs", "en": "The approximate strength of the relationship"},
            {"id": "c", "de": "Ob X die Ursache für Y ist", "en": "Whether X causes Y"},
            {"id": "d", "de": "Ob Ausreisser vorhanden sind", "en": "Whether outliers are present"}
        ],
        "correct_id": "c",
        "solution": {
            "de": "<strong>Richtig ist (c)</strong><br>Korrelation zeigt nur Zusammenhang, keine Ursache-Wirkung-Beziehung. Kausalität erfordert zusätzliche Evidenz (z.B. Experimente).",
            "en": "<strong>Correct is (c)</strong><br>Correlation only shows association, not cause-and-effect. Causation requires additional evidence (e.g., experiments)."
        }
    }
}


# ==============================================================================
# INTERACTIVE: CORRELATION EXPLORER (OPTION A — IMPECCABLE VERSION)
# ==============================================================================

@st.fragment
def correlation_explorer():
    """
    ULTRATHINK Interactive: Correlation Explorer
    
    The student adjusts correlation and sample size sliders and immediately
    sees how the scatter plot changes. Semantic colors reinforce the concept.
    """
    
    # Scenario box (grey callout)
    st.markdown(f"""
<div style="background: #f4f4f5; border-left: 4px solid #a1a1aa; 
            padding: 12px 16px; border-radius: 8px; color: #3f3f46;">
<strong>{t({"de": "Deine Mission", "en": "Your Mission"})}:</strong><br>
{t({"de": "Entdecke, wie verschiedene Korrelationswerte aussehen. Bewege den Schieberegler und beobachte das Muster!", 
    "en": "Discover how different correlation values look. Move the slider and observe the pattern!"})}
</div>
""", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # === SLIDER STYLING (via utility) ===
    from utils.layouts.foundation import inject_slider_css
    inject_slider_css([
        {"label_contains": "ρ", "color": "#16a34a"},     # Green for correlation (positive by default)
        {"label_contains": "n =", "color": "#007AFF"},   # Blue for sample size
    ])
    
    # === CONTROLS ===
    col_ctrl, col_viz = st.columns([1, 2], gap="medium")
    
    with col_ctrl:
        st.markdown(f"**{t({'de': 'Korrelation einstellen', 'en': 'Set Correlation'})}**")
        
        # Correlation slider with semantic gradient
        rho = st.slider(
            "ρ = " + t({"de": "Korrelation", "en": "Correlation"}),
            min_value=-1.0,
            max_value=1.0,
            value=0.0,
            step=0.1,
            key="corr_explorer_rho"
        )
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Sample size slider
        n_samples = st.slider(
            "n = " + t({"de": "Stichprobengrösse", "en": "Sample size"}),
            min_value=20,
            max_value=200,
            value=50,
            step=10,
            key="corr_explorer_n"
        )
        
        # Regenerate button
        if st.button(t({"de": "Neue Daten", "en": "New Data"}), key="corr_explorer_regen", use_container_width=True):
            st.session_state.corr_explorer_seed = np.random.randint(0, 10000)
    
    # Use seed for reproducibility
    if "corr_explorer_seed" not in st.session_state:
        st.session_state.corr_explorer_seed = 42
    
    np.random.seed(st.session_state.corr_explorer_seed)
    
    # === GENERATE CORRELATED DATA ===
    # Method: Generate X, then Y = rho*X + sqrt(1-rho²)*noise
    x = np.random.normal(0, 1, n_samples)
    noise = np.random.normal(0, 1, n_samples)
    y = rho * x + np.sqrt(1 - rho**2) * noise
    
    # === DETERMINE SEMANTIC COLOR ===
    if rho > 0.3:
        dot_color = COLOR_POSITIVE  # Green for positive
        interpretation_key = "positive"
    elif rho < -0.3:
        dot_color = COLOR_NEGATIVE  # Purple for negative
        interpretation_key = "negative"
    else:
        dot_color = COLOR_NEUTRAL  # Gray for near-zero
        interpretation_key = "zero"
    
    with col_viz:
        # Create scatter plot
        fig = go.Figure()
        
        # Add scatter points with semantic color
        fig.add_trace(go.Scatter(
            x=x,
            y=y,
            mode="markers",
            marker=dict(
                color=dot_color,
                size=10,
                line=dict(width=1, color="white"),
                opacity=0.8
            ),
            hovertemplate=f"X: %{{x:.2f}}<br>Y: %{{y:.2f}}<extra></extra>",
            showlegend=False
        ))
        
        # Add trend line if correlation is noticeable
        if abs(rho) > 0.1:
            slope, intercept, _, _, _ = stats.linregress(x, y)
            x_line = np.array([x.min(), x.max()])
            y_line = slope * x_line + intercept
            fig.add_trace(go.Scatter(
                x=x_line,
                y=y_line,
                mode="lines",
                line=dict(color=COLOR_LINE, width=2, dash="dash"),
                name=t({"de": "Trendlinie", "en": "Trend line"}),
                hoverinfo="skip"
            ))
        
        fig.update_layout(
            height=320,
            margin=dict(t=40, b=50, l=60, r=30),
            xaxis_title=t({"de": "Variable X", "en": "Variable X"}),
            yaxis_title=t({"de": "Variable Y", "en": "Variable Y"}),
            plot_bgcolor="white",
            paper_bgcolor="white",
            xaxis=dict(
                showgrid=True, 
                gridcolor="#e5e7eb", 
                zeroline=True, 
                zerolinecolor="#d1d5db",
                scaleanchor="y",
                scaleratio=1
            ),
            yaxis=dict(
                showgrid=True, 
                gridcolor="#e5e7eb", 
                zeroline=True, 
                zerolinecolor="#d1d5db"
            ),
            showlegend=False
        )
        
        config = {'displayModeBar': False}
        st.plotly_chart(fig, use_container_width=True, config=config)
    
    # === LIVE INTERPRETATION ===
    interpretations = {
        "positive": {
            "de": f"<strong style='color:{COLOR_POSITIVE}'>Positive Korrelation (ρ = {rho:+.1f}):</strong> Wenn X steigt, steigt auch Y. Je enger die Punkte, desto stärker der Zusammenhang.",
            "en": f"<strong style='color:{COLOR_POSITIVE}'>Positive Correlation (ρ = {rho:+.1f}):</strong> As X increases, Y increases too. The tighter the points, the stronger the relationship."
        },
        "negative": {
            "de": f"<strong style='color:{COLOR_NEGATIVE}'>Negative Korrelation (ρ = {rho:+.1f}):</strong> Wenn X steigt, sinkt Y. Die Punkte fallen von links-oben nach rechts-unten.",
            "en": f"<strong style='color:{COLOR_NEGATIVE}'>Negative Correlation (ρ = {rho:+.1f}):</strong> As X increases, Y decreases. Points fall from top-left to bottom-right."
        },
        "zero": {
            "de": f"<strong style='color:{COLOR_NEUTRAL}'>Keine/schwache Korrelation (ρ = {rho:+.1f}):</strong> Die Punkte bilden eine Wolke ohne klares Muster. X und Y sind (fast) unabhängig.",
            "en": f"<strong style='color:{COLOR_NEUTRAL}'>No/Weak Correlation (ρ = {rho:+.1f}):</strong> Points form a cloud with no clear pattern. X and Y are (almost) independent."
        }
    }
    
    st.markdown(f"""
<div style="background: linear-gradient(90deg, {dot_color}22 0%, {dot_color}08 100%); 
            border-left: 4px solid {dot_color}; border-radius: 8px; padding: 12px 16px;">
{t(interpretations[interpretation_key])}
</div>
""", unsafe_allow_html=True)
    
    # === DISCOVERY TRACKING ===
    if "corr_explorer_discoveries" not in st.session_state:
        st.session_state.corr_explorer_discoveries = set()
    
    # Track which regions student has explored
    if rho >= 0.7:
        st.session_state.corr_explorer_discoveries.add("strong_positive")
    elif rho <= -0.7:
        st.session_state.corr_explorer_discoveries.add("strong_negative")
    elif -0.2 <= rho <= 0.2:
        st.session_state.corr_explorer_discoveries.add("near_zero")
    
    discoveries = st.session_state.corr_explorer_discoveries
    
    if len(discoveries) >= 3:
        st.success(t({
            "de": "Ausgezeichnet! Du hast alle drei Hauptmuster entdeckt: starke positive, starke negative und keine Korrelation.",
            "en": "Excellent! You've discovered all three main patterns: strong positive, strong negative, and no correlation."
        }))
        
        # Discovery debrief
        st.markdown(f"""
<div style="background: #f4f4f5; border-left: 4px solid #a1a1aa; 
            padding: 12px 16px; border-radius: 8px; color: #3f3f46;">
<strong>{t({"de": "Was du gelernt hast", "en": "What you learned"})}:</strong><br>
{t({"de": "Der Korrelationskoeffizient ρ beschreibt Richtung (Vorzeichen) und Stärke (Betrag) des linearen Zusammenhangs. Ein Blick auf das Streudiagramm zeigt dir sofort, welches ρ plausibel ist.", 
    "en": "The correlation coefficient ρ describes direction (sign) and strength (magnitude) of the linear relationship. A glance at the scatter plot instantly tells you which ρ is plausible."})}
</div>
""", unsafe_allow_html=True)
    else:
        # Progress indicator
        progress_labels = {
            "strong_positive": t({"de": "stark positiv (ρ > 0.7)", "en": "strong positive (ρ > 0.7)"}),
            "strong_negative": t({"de": "stark negativ (ρ < -0.7)", "en": "strong negative (ρ < -0.7)"}),
            "near_zero": t({"de": "nahe Null (-0.2 < ρ < 0.2)", "en": "near zero (-0.2 < ρ < 0.2)"})
        }
        discovered = [progress_labels[d] for d in discoveries]
        remaining = [progress_labels[k] for k in ["strong_positive", "strong_negative", "near_zero"] if k not in discoveries]
        
        st.caption(t({
            "de": f"Entdeckungen: {len(discoveries)}/3 — Probiere noch: {', '.join(remaining)}",
            "en": f"Discoveries: {len(discoveries)}/3 — Try: {', '.join(remaining)}"
        }))


# ==============================================================================
# MAIN RENDER FUNCTION
# ==============================================================================

def render_subtopic_7_5(model):
    """7.5 Streudiagramm — ULTRATHINK Enhanced"""
    
    # Inject equal height CSS for comparison sections
    inject_equal_height_css()
    
    st.header(t(content_7_5["title"]))
    st.caption(t(content_7_5["subtitle"]))
    st.markdown("---")
    
    # === 1. INTUITION ===
    intuition_box(content_7_5["intuition"])
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # === 2. DEFINITION (with visual) ===
    defn = content_7_5["definition"]
    
    col_def, col_vis = st.columns([1.2, 1], gap="medium")
    
    with col_def:
        render_definition(
            term=defn["term"],
            formal=defn["formal"],
            plain=defn["plain"]
        )
    
    with col_vis:
        with st.container(border=True):
            st.markdown(f"**{t({'de': 'Beispiel', 'en': 'Example'})}**")
            # Simple example scatter plot
            np.random.seed(123)
            x_ex = np.random.uniform(10, 90, 15)
            y_ex = 0.6 * x_ex + np.random.normal(0, 12, 15)
            
            fig_ex = go.Figure()
            fig_ex.add_trace(go.Scatter(
                x=x_ex, y=y_ex, mode="markers",
                marker=dict(color=COLOR_POSITIVE, size=12, line=dict(width=1, color="white")),
                hoverinfo="skip"
            ))
            fig_ex.update_layout(
                height=140,
                margin=dict(t=10, b=30, l=40, r=20),
                xaxis_title="X",
                yaxis_title="Y",
                xaxis=dict(showgrid=True, gridcolor="#e5e7eb"),
                yaxis=dict(showgrid=True, gridcolor="#e5e7eb"),
                plot_bgcolor="white",
                paper_bgcolor="white"
            )
            st.plotly_chart(fig_ex, use_container_width=True, config={'displayModeBar': False})
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # === 3. COMPARISON: 1D vs 2D (Visual) ===
    st.markdown(f"### {t({'de': 'Univariate vs. Bivariate Daten', 'en': 'Univariate vs. Bivariate Data'})}")
    univariate_vs_bivariate_visual()
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # === 4. INTERACTIVE: Correlation Explorer ===
    st.markdown(f"### {t({'de': 'Interaktiv: Korrelations-Explorer', 'en': 'Interactive: Correlation Explorer'})}")
    correlation_explorer()
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # === 5. WORKED EXAMPLE ===
    we = content_7_5["worked_example"]
    render_worked_example(
        header=we["header"],
        problem=we["problem"],
        steps=we["steps"],
        answer=we["answer"]
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # === 6. FRAG DICH ===
    fd = content_7_5["frag_dich"]
    render_ask_yourself(
        header=fd["header"],
        questions=fd["questions"],
        conclusion=fd["conclusion"]
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # === 7. EXAM ESSENTIALS ===
    ee = content_7_5["exam_essentials"]
    render_exam_essentials(
        trap=ee["trap"],
        trap_rule=ee["trap_rule"],
        tips=ee["tips"]
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # === 8. MCQ PRACTICE ===
    st.markdown(f"### {t({'de': 'Prüfungstraining', 'en': 'Exam Practice'})}")
    
    # MCQ 1
    mcq1 = content_7_5["mcq_1"]
    opts1 = mcq1["options"]
    opt_labels1 = [t({"de": o["de"], "en": o["en"]}) for o in opts1]
    correct_idx1 = next((i for i, o in enumerate(opts1) if o["id"] == mcq1["correct_id"]), 0)
    
    with st.container(border=True):
        render_mcq(
            key_suffix="7_5_mcq1",
            question_text=t(mcq1["question"]),
            options=opt_labels1,
            correct_idx=correct_idx1,
            solution_text_dict=mcq1["solution"],
            success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
            error_msg_dict={"de": "Falsch.", "en": "Incorrect."},
            client=model,
            ai_context="Question about reading correlation from scatter plot direction",
            course_id="vwl",
            topic_id="7",
            subtopic_id="7.5",
            question_id="7_5_mcq1"
        )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # MCQ 2
    mcq2 = content_7_5["mcq_2"]
    opts2 = mcq2["options"]
    opt_labels2 = [t({"de": o["de"], "en": o["en"]}) for o in opts2]
    correct_idx2 = next((i for i, o in enumerate(opts2) if o["id"] == mcq2["correct_id"]), 0)
    
    with st.container(border=True):
        render_mcq(
            key_suffix="7_5_mcq2",
            question_text=t(mcq2["question"]),
            options=opt_labels2,
            correct_idx=correct_idx2,
            solution_text_dict=mcq2["solution"],
            success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
            error_msg_dict={"de": "Falsch.", "en": "Incorrect."},
            client=model,
            ai_context="Question about correlation vs causation",
            course_id="vwl",
            topic_id="7",
            subtopic_id="7.5",
            question_id="7_5_mcq2"
        )
