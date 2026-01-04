# Topic 7.4: Quantile-Quantile Plot (QQ-Plot)
# ULTRATHINK ENHANCED VERSION — "Apple Would Be Jealous"
# Two-phase interactive: Distribution Lab → Pattern Detective

import streamlit as st
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from scipy import stats
from utils.localization import t
from utils.quiz_helper import render_mcq
from utils.ask_yourself import render_ask_yourself
from utils.exam_essentials import render_exam_essentials
from utils.worked_example import render_worked_example
from utils.layouts import (
    render_single_formula,
    render_comparison,
    render_definition,
)
from utils.layouts.foundation import (
    intuition_box,
    grey_callout,
    inject_equal_height_css,
    COLORS,
)

# ==============================================================================
# SEMANTIC COLOR PALETTE (Matches Topic 7 conventions)
# ==============================================================================
COLOR_DATA = "#007AFF"       # Blue  — Empirical data points
COLOR_THEORY = "#9B59B6"     # Purple — Theoretical line
COLOR_MATCH = "#16a34a"      # Green  — Perfect match / close to diagonal
COLOR_MISMATCH = "#FF4B4B"   # Red   — Deviation from diagonal
COLOR_NEUTRAL = "#6B7280"    # Gray  — Neutral / reference

# ==============================================================================
# CONTENT DICTIONARY — BILINGUAL (ULTRATHINK DEPTH)
# ==============================================================================

content_7_4 = {
    "title": {
        "de": "7.4 Quantile-Quantile Plot (QQ-Plot)",
        "en": "7.4 Quantile-Quantile Plot (QQ-Plot)"
    },
    "subtitle": {
        "de": "Der Spiegel, der zeigt, ob deine Daten zur Theorie passen",
        "en": "The Mirror That Reveals If Your Data Fits The Theory"
    },
    
    # =========================================================================
    # INTUITION — THE "MAGIC MIRROR" ANALOGY
    # =========================================================================
    "intuition": {
        "de": """<strong>Stell dir einen magischen Spiegel vor:</strong> Du stehst wie geplant vor dem Spiegel.
        Das Spiegelbild zeigt, wie du <em>aussehen solltest</em> (Theorie). Du selbst bist, wie du <em>wirklich aussiehst</em> (Daten).
        <br><br>
        <strong>Wenn das Spiegelbild perfekt zu dir passt</strong> → du siehst eine gerade Linie (Diagonale).
        <br>
        <strong>Wenn etwas nicht stimmt</strong> → das Bild verzerrt sich (Kurven, Abweichungen).
        <br><br>
        <strong>Das ist ein QQ-Plot:</strong> Er vergleicht, wo deine Datenpunkte <em>tatsächlich</em> liegen 
        mit wo sie <em>liegen sollten</em>, wenn sie einer bestimmten Verteilung folgen würden. 
        <strong>Diagonale = perfekte Übereinstimmung.</strong>""",
        
        "en": """<strong>Imagine a magic mirror:</strong> You stand in front of the mirror as planned.
        The reflection shows what you <em>should look like</em> (Theory). You yourself are what you <em>actually look like</em> (Data).
        <br><br>
        <strong>If the reflection matches you perfectly</strong> → you see a straight line (diagonal).
        <br>
        <strong>If something is off</strong> → the image distorts (curves, deviations).
        <br><br>
        <strong>That's a QQ-Plot:</strong> It compares where your data points <em>actually</em> lie 
        with where they <em>should</em> lie if they followed a specific distribution. 
        <strong>Diagonal = perfect match.</strong>"""
    },
    
    # =========================================================================
    # DEFINITION
    # =========================================================================
    "definition": {
        "term": {"de": "QQ-Plot (Quantile-Quantile Plot)", "en": "QQ-Plot (Quantile-Quantile Plot)"},
        "formal": {
            "de": "Ein QQ-Plot vergleicht die empirischen Quantile einer Stichprobe mit den theoretischen Quantilen einer angenommenen Verteilung. Punkte auf der Diagonalen bedeuten perfekte Übereinstimmung.",
            "en": "A QQ-Plot compares the empirical quantiles of a sample with the theoretical quantiles of an assumed distribution. Points on the diagonal indicate perfect agreement."
        },
        "plain": {
            "de": "X-Achse = 'Wo sollte der Punkt sein?' | Y-Achse = 'Wo ist er wirklich?' | Diagonale = 'Treffer!'",
            "en": "X-axis = 'Where should the point be?' | Y-axis = 'Where is it really?' | Diagonal = 'Match!'"
        }
    },
    
    # =========================================================================
    # COMPARISON: QQ-PLOT VS HISTOGRAM
    # =========================================================================
    "comparison": {
        "header": {"de": "QQ-Plot vs. Histogramm", "en": "QQ-Plot vs. Histogram"},
        "left": {
            "title": {"de": "QQ-Plot", "en": "QQ-Plot"},
            "formula": None,
            "description": {
                "de": "Testet, ob Daten zu <strong>EINER spezifischen</strong> Verteilung passen. Nutzt jeden einzelnen Datenpunkt.",
                "en": "Tests if data fits <strong>ONE specific</strong> distribution. Uses every single data point."
            },
            "example": {
                "de": "→ Perfekt für: 'Sind diese Prüfungsnoten normalverteilt?'",
                "en": "→ Perfect for: 'Are these exam scores normally distributed?'"
            }
        },
        "right": {
            "title": {"de": "Histogramm", "en": "Histogram"},
            "formula": None,
            "description": {
                "de": "Zeigt die <strong>allgemeine Form</strong> der Verteilung. Gruppiert Daten in Klassen (Bins).",
                "en": "Shows the <strong>general shape</strong> of the distribution. Groups data into classes (bins)."
            },
            "example": {
                "de": "→ Perfekt für: 'Ist die Verteilung schief oder symmetrisch?'",
                "en": "→ Perfect for: 'Is the distribution skewed or symmetric?'"
            }
        }
    },
    
    # =========================================================================
    # FORMULA
    # =========================================================================
    "formula": {
        "header": {"de": "Die QQ-Plot Koordinaten", "en": "The QQ-Plot Coordinates"},
        "intuition": {
            "de": "Jeder Punkt vergleicht: 'Wo sollte dieser Wert theoretisch sein?' vs. 'Wo ist er wirklich?'",
            "en": "Each point compares: 'Where should this value theoretically be?' vs. 'Where is it really?'"
        },
        "formula": r"\left( \underbrace{F^{-1}\left(\frac{k - 0.5}{n}\right)}_{\substack{\text{Theoretical} \\ \text{Quantile}}}, \; \underbrace{x_{(k)}}_{\substack{\text{Empirical} \\ \text{Quantile}}} \right), \quad k = 1, \ldots, n",
        "formula_en": r"\left( \underbrace{F^{-1}\left(\frac{k - 0.5}{n}\right)}_{\text{Theory}}, \; \underbrace{x_{(k)}}_{\text{Data}} \right), \quad k = 1, \ldots, n",
        "variables": [
            {
                "symbol": r"F^{-1}",
                "name": {"de": "Inverse Verteilungsfunktion", "en": "Inverse CDF"},
                "description": {"de": "Die 'Umkehrung' der theoretischen Verteilung — gibt den Wert für eine Wahrscheinlichkeit", "en": "The 'inverse' of the theoretical distribution — returns the value for a probability"}
            },
            {
                "symbol": r"x_{(k)}",
                "name": {"de": "k-ter geordneter Wert", "en": "k-th ordered value"},
                "description": {"de": "Der k-kleinste Wert in deiner Stichprobe (empirisches Quantil)", "en": "The k-th smallest value in your sample (empirical quantile)"}
            },
            {
                "symbol": r"n",
                "name": {"de": "Stichprobengrösse", "en": "Sample size"},
                "description": {"de": "Anzahl der Datenpunkte", "en": "Number of data points"}
            }
        ],
        "insight": {
            "de": "<strong>Der Schlüssel:</strong> Wenn die Punkte auf der Diagonalen liegen, hat jeder Datenpunkt <em>genau den Wert</em>, den die theoretische Verteilung vorhersagt. Kurven = systematische Abweichung!",
            "en": "<strong>The key:</strong> When points lie on the diagonal, each data point has <em>exactly the value</em> the theoretical distribution predicts. Curves = systematic deviation!"
        }
    },
    
    # =========================================================================
    # WORKED EXAMPLE — CONTINUATION OF 7.3.1
    # =========================================================================
    "worked_example": {
        "header": {"de": "Beispiel: Geräte-Lebensdauer (Fortsetzung von 7.3)", "en": "Example: Device Lifespan (Continuation from 7.3)"},
        "problem": {
            "de": """<strong>Erinnerung aus 7.3:</strong> Wir hatten 16 Geräte mit diesen Lebensdauern (Monate):
            <br><br>
            <code style="background:#f4f4f5; padding:8px; border-radius:4px; display:block; font-size:0.9em;">
            1.5, 3.5, 6.5, 11.5, 12.5, 14, 17, 17, 19, 20, 23.5, 32.5, 34.5, 39, 55.5, 119
            </code>
            <br>
            <strong>Neue Frage:</strong> Folgen diese Daten einer Normalverteilung? Erstelle einen QQ-Plot zur Überprüfung.""",
            "en": """<strong>Recall from 7.3:</strong> We had 16 devices with these lifespans (months):
            <br><br>
            <code style="background:#f4f4f5; padding:8px; border-radius:4px; display:block; font-size:0.9em;">
            1.5, 3.5, 6.5, 11.5, 12.5, 14, 17, 17, 19, 20, 23.5, 32.5, 34.5, 39, 55.5, 119
            </code>
            <br>
            <strong>New question:</strong> Do these data follow a Normal distribution? Create a QQ-plot to check."""
        },
        "steps": [
            {
                "label": {"de": "Schritt 1: Theoretische Quantile berechnen", "en": "Step 1: Calculate theoretical quantiles"},
                "latex": r"\text{Für } k=1: \quad F^{-1}\left(\frac{1-0.5}{16}\right) = F^{-1}(0.03125) = {\color{#9B59B6}-1.86}",
                "latex_en": r"\text{For } k=1: \quad F^{-1}\left(\frac{1-0.5}{16}\right) = F^{-1}(0.03125) = {\color{#9B59B6}-1.86}",
                "note": {"de": "Wir benutzen die Standard-Normalverteilung als Referenz", "en": "We use the Standard Normal distribution as reference"}
            },
            {
                "label": {"de": "Schritt 2: Punkte plotten", "en": "Step 2: Plot points"},
                "latex": r"\text{Punkt 1: } \left({\color{#9B59B6}-1.86}, \; {\color{#007AFF}1.5}\right), \quad \text{Punkt 16: } \left({\color{#9B59B6}+1.86}, \; {\color{#FF4B4B}119}\right)",
                "latex_en": r"\text{Point 1: } \left({\color{#9B59B6}-1.86}, \; {\color{#007AFF}1.5}\right), \quad \text{Point 16: } \left({\color{#9B59B6}+1.86}, \; {\color{#FF4B4B}119}\right)",
                "note": {"de": "Theorie (x) vs. tatsächlicher Wert (y)", "en": "Theory (x) vs. actual value (y)"}
            },
            {
                "label": {"de": "Schritt 3: Muster erkennen", "en": "Step 3: Recognize the pattern"},
                "latex": r"\text{Punkt 16 liegt } {\color{#FF4B4B}\text{weit über}} \text{ der Diagonalen} \;\Rightarrow\; \text{Ausreisser!}",
                "latex_en": r"\text{Point 16 lies } {\color{#FF4B4B}\text{far above}} \text{ the diagonal} \;\Rightarrow\; \text{Outlier!}",
                "note": None
            }
        ],
        "answer": {
            "de": "**Fazit:** Die Daten sind **NICHT normalverteilt**. Der QQ-Plot zeigt eine starke Abweichung am rechten Ende (der Ausreisser 119 aus dem Boxplot!). Die restlichen Punkte liegen näher an der Diagonalen, aber mit leichter Rechtsschiefe.",
            "en": "**Conclusion:** The data are **NOT normally distributed**. The QQ-plot shows strong deviation at the right end (the outlier 119 from the box plot!). The remaining points lie closer to the diagonal, but with slight right-skewness."
        }
    },
    
    # =========================================================================
    # PATTERN INTERPRETATIONS (For Interactive Phase 2)
    # =========================================================================
    "patterns": [
        {
            "id": "normal",
            "name": {"de": "Normalverteilung", "en": "Normal Distribution"},
            "description": {
                "de": "Punkte liegen auf der Diagonalen",
                "en": "Points lie on the diagonal"
            },
            "interpretation": {"de": "Perfekte Übereinstimmung!", "en": "Perfect match!"},
            "visual": "diagonal"
        },
        {
            "id": "right_skew",
            "name": {"de": "Rechtsschiefe", "en": "Right-Skewed"},
            "description": {
                "de": "Punkte biegen nach oben am rechten Ende",
                "en": "Points curve upward at the right end"
            },
            "interpretation": {"de": "Mehr extreme hohe Werte als erwartet", "en": "More extreme high values than expected"},
            "visual": "banana_up"
        },
        {
            "id": "left_skew", 
            "name": {"de": "Linksschiefe", "en": "Left-Skewed"},
            "description": {
                "de": "Punkte biegen nach unten am linken Ende",
                "en": "Points curve downward at the left end"
            },
            "interpretation": {"de": "Mehr extreme niedrige Werte als erwartet", "en": "More extreme low values than expected"},
            "visual": "banana_down"
        },
        {
            "id": "heavy_tails",
            "name": {"de": "Schwere Ränder", "en": "Heavy Tails"},
            "description": {
                "de": "S-Kurve: beide Enden weichen ab",
                "en": "S-curve: both ends deviate"
            },
            "interpretation": {"de": "Mehr Extremwerte als Normal erwartet (Leptokurtisch)", "en": "More extreme values than Normal expects (Leptokurtic)"},
            "visual": "s_curve"
        }
    ],
    
    # =========================================================================
    # FRAG DICH
    # =========================================================================
    "frag_dich": {
        "header": {"de": "Frag dich: Verstehst du QQ-Plots?", "en": "Ask yourself: Do you understand QQ-plots?"},
        "questions": [
            {
                "de": "Die Punkte biegen am <strong>rechten Ende nach oben</strong> — ist die Verteilung links- oder rechtschief?",
                "en": "The points curve <strong>upward at the right end</strong> — is the distribution left-skewed or right-skewed?"
            },
            {
                "de": "Was bedeutet eine <strong>S-Kurve</strong> im QQ-Plot?",
                "en": "What does an <strong>S-curve</strong> in the QQ-plot mean?"
            },
            {
                "de": "Warum nutzen wir <strong>(k-0.5)/n</strong> statt <strong>k/n</strong> für die theoretischen Quantile?",
                "en": "Why do we use <strong>(k-0.5)/n</strong> instead of <strong>k/n</strong> for theoretical quantiles?"
            },
            {
                "de": "Die X-Achse zeigt <strong>theoretische</strong> Werte, die Y-Achse zeigt <strong>?</strong>",
                "en": "The X-axis shows <strong>theoretical</strong> values, the Y-axis shows <strong>?</strong>"
            }
        ],
        "conclusion": {
            "de": "Rechtschief | S-Kurve = schwere Ränder | Vermeidet Randeffekte | Empirische (echte) Daten",
            "en": "Right-skewed | S-curve = heavy tails | Avoids edge effects | Empirical (real) data"
        }
    },
    
    # =========================================================================
    # EXAM ESSENTIALS
    # =========================================================================
    "exam_essentials": {
        "trap": {
            "de": "<strong>'Diagonale = EXAKT auf der Linie'</strong> — Viele Studenten erwarten perfekte Punkte. In der Realität gibt es <em>immer</em> Streuung um die Diagonale. Erst <strong>systematische Kurven</strong> zeigen Abweichungen!",
            "en": "<strong>'Diagonal = EXACTLY on the line'</strong> — Many students expect perfect points. In reality, there's <em>always</em> scatter around the diagonal. Only <strong>systematic curves</strong> show deviations!"
        },
        "trap_rule": {
            "de": "Merke: Kleine zufällige Abweichungen = normal. Kurven/Muster = Problem.",
            "en": "Remember: Small random deviations = normal. Curves/patterns = problem."
        },
        "tips": [
            {
                "tip": {"de": "S-Kurve = Falsche Verteilungsfamilie", "en": "S-curve = Wrong distribution family"},
                "why": {
                    "de": "Eine S-Kurve (beide Enden weichen ab) bedeutet, dass die Daten schwerere oder leichtere Ränder haben als die angenommene Verteilung.",
                    "en": "An S-curve (both ends deviate) means the data has heavier or lighter tails than the assumed distribution."
                }
            },
            {
                "tip": {"de": "Banane = Schiefe", "en": "Banana = Skewness"},
                "why": {
                    "de": "Biegen sich die Punkte nur an einem Ende? Dann ist die Verteilung schief (rechts = nach oben, links = nach unten).",
                    "en": "Do points curve at only one end? Then the distribution is skewed (right = upward, left = downward)."
                }
            },
            {
                "tip": {"de": "Einzelner Ausreisser ≠ Ablehnung", "en": "Single outlier ≠ Rejection"},
                "why": {
                    "de": "Ein einzelner Punkt weit weg von der Diagonalen kann ein Ausreisser sein — nicht unbedingt eine falsche Verteilungsannahme. Schau auf das Gesamtmuster!",
                    "en": "A single point far from the diagonal could be an outlier — not necessarily a wrong distribution assumption. Look at the overall pattern!"
                }
            }
        ]
    },
    
    # =========================================================================
    # INTERACTIVE MISSION — TWO PHASES
    # =========================================================================
    "mission_lab": {
        "title": {"de": "Phase 1: Verteilungs-Labor", "en": "Phase 1: Distribution Lab"},
        "scenario": {
            "de": """<strong>Willkommen im Verteilungs-Labor!</strong><br>
            Generiere Zufallsdaten aus verschiedenen Verteilungen und beobachte, wie sich der QQ-Plot verändert.
            <br><br>
            <strong>Deine Mission:</strong> Entdecke, wie verschiedene Verteilungen verschiedene QQ-Plot-Muster erzeugen.""",
            "en": """<strong>Welcome to the Distribution Lab!</strong><br>
            Generate random data from different distributions and observe how the QQ-plot changes.
            <br><br>
            <strong>Your mission:</strong> Discover how different distributions create different QQ-plot patterns."""
        }
    },
    "mission_detective": {
        "title": {"de": "Phase 2: Muster-Detektiv", "en": "Phase 2: Pattern Detective"},
        "scenario": {
            "de": """<strong>Du bist jetzt ein QQ-Plot Detektiv!</strong><br>
            Schaue dir das Muster an und identifiziere, welche Verteilung dahinter steckt.""",
            "en": """<strong>You're now a QQ-Plot Detective!</strong><br>
            Look at the pattern and identify which distribution is behind it."""
        }
    },
    
    # =========================================================================
    # MCQ QUESTIONS (2 NEW)
    # =========================================================================
    "mcq_1": {
        "question": {
            "de": "In einem QQ-Plot gegen die Normalverteilung biegen sich die Punkte am rechten Ende nach oben. Was bedeutet das?",
            "en": "In a QQ-plot against the Normal distribution, the points curve upward at the right end. What does this mean?"
        },
        "options": [
            {"id": "a", "de": "Die Daten sind normalverteilt", "en": "The data is normally distributed"},
            {"id": "b", "de": "Die Daten sind linksschief", "en": "The data is left-skewed"},
            {"id": "c", "de": "Die Daten sind rechtsschief (mehr hohe Extremwerte)", "en": "The data is right-skewed (more high extreme values)"},
            {"id": "d", "de": "Die Stichprobe ist zu klein", "en": "The sample is too small"}
        ],
        "correct_id": "c",
        "solution": {
            "de": "<strong>Richtig ist (c)</strong><br>Wenn Punkte am rechten Ende nach oben biegen, bedeutet das: Die beobachteten hohen Werte sind <em>höher</em> als die Theorie vorhersagt → Rechtsschiefe Verteilung mit schwererem rechten Rand.",
            "en": "<strong>Correct is (c)</strong><br>When points curve upward at the right end, it means: The observed high values are <em>higher</em> than theory predicts → Right-skewed distribution with heavier right tail."
        }
    },
    "mcq_2": {
        "question": {
            "de": "Was zeigt die X-Achse eines QQ-Plots?",
            "en": "What does the X-axis of a QQ-plot show?"
        },
        "options": [
            {"id": "a", "de": "Die beobachteten Datenpunkte", "en": "The observed data points"},
            {"id": "b", "de": "Die theoretischen Quantile der angenommenen Verteilung", "en": "The theoretical quantiles of the assumed distribution"},
            {"id": "c", "de": "Die Häufigkeiten", "en": "The frequencies"},
            {"id": "d", "de": "Die Klassenbreiten", "en": "The class widths"}
        ],
        "correct_id": "b",
        "solution": {
            "de": "<strong>Richtig ist (b)</strong><br>Die X-Achse zeigt, wo die Punkte <em>liegen sollten</em>, wenn die Daten der theoretischen Verteilung folgen würden. Die Y-Achse zeigt, wo sie <em>tatsächlich</em> liegen.",
            "en": "<strong>Correct is (b)</strong><br>The X-axis shows where points <em>should</em> lie if the data followed the theoretical distribution. The Y-axis shows where they <em>actually</em> lie."
        }
    }
}


# ==============================================================================
# INTERACTIVE: QQ-PLOT VS HISTOGRAM COMPARISON
# ==============================================================================

@st.fragment
def qq_vs_histogram_interactive():
    """
    Interactive visual comparison: Same data shown as QQ-Plot vs Histogram.
    COMPACT layout to fit on screen.
    """
    
    # Compact intro + controls in one row
    col_intro, col_pills = st.columns([1, 1.5])
    
    with col_intro:
        st.markdown(f"""
<div style="background: #f4f4f5; border-left: 4px solid #a1a1aa; 
            padding: 10px 14px; border-radius: 8px; color: #3f3f46; font-size: 0.9em;">
<strong>{t({"de": "Vergleiche", "en": "Compare"})}:</strong> {t({"de": "Gleiche Daten, zwei Ansichten.", "en": "Same data, two views."})}
</div>
""", unsafe_allow_html=True)
    
    with col_pills:
        # Initialize state
        if "qq_compare_selection" not in st.session_state:
            st.session_state.qq_compare_selection = "Normal"
        
        # Black pill buttons
        btn_cols = st.columns(3)
        options = ["Normal", t({"de": "Schief", "en": "Skewed"}), t({"de": "Ausreisser", "en": "Outlier"})]
        keys = ["Normal", "Skewed", "Outlier"]
        
        for i, (col, opt, key) in enumerate(zip(btn_cols, options, keys)):
            with col:
                is_selected = st.session_state.qq_compare_selection == key
                if is_selected:
                    st.markdown(f"""
<div style="background: #000; color: #fff; padding: 8px 16px; border-radius: 20px; 
            text-align: center; font-weight: 500; font-size: 0.9em;">{opt}</div>
""", unsafe_allow_html=True)
                else:
                    if st.button(opt, key=f"qq_pill_{key}", use_container_width=True):
                        st.session_state.qq_compare_selection = key
                        st.rerun(scope="fragment")
        
        data_type = st.session_state.qq_compare_selection
    
    # Generate data based on selection
    np.random.seed(42)
    n = 50
    
    normal_label = "Normal"
    skewed_label = "Skewed"

    
    if data_type == normal_label:
        data = np.random.normal(50, 10, n)
    elif data_type == skewed_label:
        data = np.random.exponential(20, n) + 20
    else:  # Outlier
        data = np.random.normal(50, 10, n)
        data[0] = 120
    
    # Side-by-side plots - COMPACT
    col_qq, col_hist = st.columns(2, gap="small")
    
    sorted_data = np.sort(data)
    theoretical_quantiles = stats.norm.ppf(np.arange(1, n + 1) / (n + 1))
    
    with col_qq:
        st.markdown(f"**QQ-Plot** · *{t({'de': 'Diagonale = Treffer', 'en': 'Diagonal = match'})}*")
        
        fig_qq = go.Figure()
        
        # Diagonal line
        line_min = min(theoretical_quantiles.min(), (sorted_data.min() - 50) / 10)
        line_max = max(theoretical_quantiles.max(), (sorted_data.max() - 50) / 10)
        fig_qq.add_trace(go.Scatter(
            x=[line_min, line_max], y=[line_min * 10 + 50, line_max * 10 + 50],
            mode="lines", line=dict(color=COLOR_THEORY, width=2, dash="dash"),
            hoverinfo="skip", showlegend=False
        ))
        
        # Points
        fig_qq.add_trace(go.Scatter(
            x=theoretical_quantiles, y=sorted_data, mode="markers",
            marker=dict(color=COLOR_DATA, size=7), showlegend=False,
            hovertemplate="Theory: %{x:.2f}<br>Data: %{y:.1f}<extra></extra>"
        ))
        
        fig_qq.update_layout(
            height=200, margin=dict(t=10, b=35, l=45, r=10),
            xaxis_title=t({"de": "Theorie", "en": "Theory"}),
            yaxis_title=t({"de": "Daten", "en": "Data"}),
            plot_bgcolor="white", paper_bgcolor="white",
            xaxis=dict(showgrid=True, gridcolor="#e5e7eb"),
            yaxis=dict(showgrid=True, gridcolor="#e5e7eb"),
        )
        st.plotly_chart(fig_qq, use_container_width=True, config={'displayModeBar': False})
    
    with col_hist:
        st.markdown(f"**Histogram** · *{t({'de': 'Form, aber welche?', 'en': 'Shape, but which?'})}*")
        
        fig_hist = go.Figure()
        fig_hist.add_trace(go.Histogram(
            x=data, nbinsx=10,
            marker=dict(color=COLOR_DATA, line=dict(color="white", width=1))
        ))
        
        fig_hist.update_layout(
            height=200, margin=dict(t=10, b=35, l=45, r=10),
            xaxis_title=t({"de": "Wert", "en": "Value"}),
            yaxis_title=t({"de": "Anzahl", "en": "Count"}),
            plot_bgcolor="white", paper_bgcolor="white",
            xaxis=dict(showgrid=True, gridcolor="#e5e7eb"),
            yaxis=dict(showgrid=True, gridcolor="#e5e7eb"),
            bargap=0.05
        )
        st.plotly_chart(fig_hist, use_container_width=True, config={'displayModeBar': False})
    
    # Compact key difference (single line)
    st.caption(t({
        "de": "QQ-Plot testet EINE Verteilung (Abweichungen sichtbar) — Histogramm zeigt Form (aber welche genau?)",
        "en": "QQ-Plot tests ONE distribution (deviations visible) — Histogram shows shape (but which exactly?)"
    }))


# ==============================================================================
# INTERACTIVE PHASE 1: DISTRIBUTION LAB
# ==============================================================================

@st.fragment
def qq_distribution_lab():
    """
    ULTRATHINK Interactive Phase 1: Distribution Lab
    
    Students generate random data from different distributions and watch
    how the QQ-plot pattern changes in real-time.
    """
    
    # Scenario box
    st.markdown(f"""
<div style="background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%); 
            border-left: 4px solid #007AFF; border-radius: 8px;
            padding: 16px; color: #1c1c1e;">
{t(content_7_4["mission_lab"]["scenario"])}
</div>
""", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # === CONTROLS ===
    col_ctrl, col_viz = st.columns([1, 2])
    
    with col_ctrl:
        st.markdown(f"**{t({'de': 'Wähle die wahre Verteilung', 'en': 'Choose the true distribution'})}**")
        
        dist_choice = st.radio(
            t({"de": "Verteilung", "en": "Distribution"}),
            options=["Normal", "Exponential", "Uniform", "Right-Skewed"],
            key="qq_lab_dist",
            label_visibility="collapsed"
        )
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Semantic slider coloring (Blue = sample size)
        st.markdown("""
        <style>
        .stSlider:has([aria-label*="n ="]) div[data-baseweb="slider"] > div:first-child > div:first-child { 
            background-color: #007AFF !important; 
        }
        .stSlider:has([aria-label*="n ="]) div[role="slider"] { 
            background-color: #FFFFFF !important; 
            border: 2px solid #007AFF !important; 
        }
        </style>
        """, unsafe_allow_html=True)
        
        n_samples = st.slider(
            "n = " + t({"de": "Stichprobengrösse", "en": "Sample size"}),
            min_value=10,
            max_value=100,
            value=30,
            step=5,
            key="qq_lab_n"
        )
        
        # Regenerate button
        if st.button(t({"de": "Neue Daten generieren", "en": "Generate New Data"}), key="qq_lab_regen", use_container_width=True):
            st.session_state.qq_lab_seed = np.random.randint(0, 10000)
    
    # Use seed for reproducibility within fragment
    if "qq_lab_seed" not in st.session_state:
        st.session_state.qq_lab_seed = 42
    
    np.random.seed(st.session_state.qq_lab_seed)
    
    # Generate data based on selection
    if dist_choice == "Normal":
        data = np.random.normal(0, 1, n_samples)
        true_dist = "Normal"
    elif dist_choice == "Exponential":
        data = np.random.exponential(1, n_samples)
        true_dist = "Exponential"
    elif dist_choice == "Uniform":
        data = np.random.uniform(-2, 2, n_samples)
        true_dist = "Uniform"
    else:  # Right-Skewed
        data = np.random.lognormal(0, 0.5, n_samples)
        true_dist = "Right-Skewed"
    
    # Calculate QQ-plot coordinates (vs Normal)
    sorted_data = np.sort(data)
    n = len(sorted_data)
    theoretical_quantiles = stats.norm.ppf(np.arange(1, n + 1) / (n + 1))
    
    # Determine deviation from diagonal
    deviations = np.abs(sorted_data - theoretical_quantiles)
    mean_deviation = np.mean(deviations)
    
    with col_viz:
        # Create QQ-plot
        fig = go.Figure()
        
        # Diagonal reference line
        line_min = min(theoretical_quantiles.min(), sorted_data.min())
        line_max = max(theoretical_quantiles.max(), sorted_data.max())
        fig.add_trace(go.Scatter(
            x=[line_min, line_max],
            y=[line_min, line_max],
            mode="lines",
            line=dict(color=COLOR_THEORY, width=2, dash="dash"),
            name=t({"de": "Perfekte Übereinstimmung", "en": "Perfect Match"}),
            hoverinfo="skip"
        ))
        
        # Color points by deviation from diagonal
        colors = [COLOR_MATCH if d < 0.5 else (COLOR_NEUTRAL if d < 1.0 else COLOR_MISMATCH) for d in deviations]
        
        # QQ-plot points
        fig.add_trace(go.Scatter(
            x=theoretical_quantiles,
            y=sorted_data,
            mode="markers",
            marker=dict(
                color=colors,
                size=10,
                line=dict(width=1, color="white")
            ),
            name=t({"de": "Datenpunkte", "en": "Data Points"}),
            hovertemplate=f"{t({'de': 'Theorie', 'en': 'Theory'})}: %{{x:.2f}}<br>{t({'de': 'Daten', 'en': 'Data'})}: %{{y:.2f}}<extra></extra>"
        ))
        
        fig.update_layout(
            height=300,
            margin=dict(t=40, b=40, l=50, r=30),
            xaxis_title=t({"de": "Theoretische Quantile (Normal)", "en": "Theoretical Quantiles (Normal)"}),
            yaxis_title=t({"de": "Empirische Quantile", "en": "Empirical Quantiles"}),
            plot_bgcolor="white",
            paper_bgcolor="white",
            showlegend=True,
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
            xaxis=dict(showgrid=True, gridcolor="#e5e7eb", zeroline=True, zerolinecolor="#d1d5db"),
            yaxis=dict(showgrid=True, gridcolor="#e5e7eb", zeroline=True, zerolinecolor="#d1d5db"),
        )
        
        config = {'displayModeBar': False}
        st.plotly_chart(fig, use_container_width=True, config=config)
    
    # === LIVE INTERPRETATION ===
    if true_dist == "Normal":
        interpretation_color = COLOR_MATCH
        interpretation_text = t({
            "de": f"<strong>Perfekte Übereinstimmung!</strong> Die Daten stammen aus einer Normalverteilung → Punkte liegen auf der Diagonalen.",
            "en": f"<strong>Perfect match!</strong> The data comes from a Normal distribution → points lie on the diagonal."
        })
    elif true_dist == "Exponential":
        interpretation_color = COLOR_MISMATCH
        interpretation_text = t({
            "de": f"<strong>Starke Rechtsschiefe!</strong> Die Exponentialverteilung hat nur positive Werte und einen schweren rechten Rand → S-Kurve nach oben.",
            "en": f"<strong>Strong right-skew!</strong> The Exponential distribution has only positive values and a heavy right tail → S-curve upward."
        })
    elif true_dist == "Uniform":
        interpretation_color = "#FFD700"
        interpretation_text = t({
            "de": f"<strong>Leichte Ränder!</strong> Die Gleichverteilung hat weniger Extremwerte als die Normalverteilung → umgekehrte S-Kurve.",
            "en": f"<strong>Light tails!</strong> The Uniform distribution has fewer extreme values than Normal → inverted S-curve."
        })
    else:
        interpretation_color = COLOR_MISMATCH
        interpretation_text = t({
            "de": f"<strong>Rechtsschiefe Log-Normal!</strong> Punkte biegen am rechten Ende stark nach oben → mehr hohe Extremwerte als erwartet.",
            "en": f"<strong>Right-skewed Log-Normal!</strong> Points curve strongly upward at the right end → more high extreme values than expected."
        })
    
    st.markdown(f"""
<div style="background: linear-gradient(90deg, {interpretation_color}22 0%, {interpretation_color}08 100%); 
            border-left: 4px solid {interpretation_color}; border-radius: 8px; padding: 12px 16px;">
{interpretation_text}
</div>
""", unsafe_allow_html=True)
    
    # Track discoveries
    if "qq_lab_discoveries" not in st.session_state:
        st.session_state.qq_lab_discoveries = set()
    
    st.session_state.qq_lab_discoveries.add(true_dist)
    
    if len(st.session_state.qq_lab_discoveries) >= 3:
        st.markdown("<br>", unsafe_allow_html=True)
        st.success(t({
            "de": "Ausgezeichnet! Du hast mindestens 3 verschiedene Verteilungen erkundet. Weiter zu Phase 2!",
            "en": "Excellent! You've explored at least 3 different distributions. On to Phase 2!"
        }))
    else:
        st.caption(t({
            "de": f"Entdeckungen: {len(st.session_state.qq_lab_discoveries)}/3 — Probiere verschiedene Verteilungen!",
            "en": f"Discoveries: {len(st.session_state.qq_lab_discoveries)}/3 — Try different distributions!"
        }))


# ==============================================================================
# INTERACTIVE PHASE 2: PATTERN DETECTIVE
# ==============================================================================

@st.fragment
def qq_pattern_detective():
    """
    ULTRATHINK Interactive Phase 2: Pattern Detective
    
    Students are shown a QQ-plot pattern and must identify what it means.
    """
    
    # Scenario box
    st.markdown(f"""
<div style="background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%); 
            border-left: 4px solid #9B59B6; border-radius: 8px;
            padding: 16px; color: #1c1c1e;">
{t(content_7_4["mission_detective"]["scenario"])}
</div>
""", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Initialize state
    if "qq_detective_round" not in st.session_state:
        st.session_state.qq_detective_round = 0
    if "qq_detective_score" not in st.session_state:
        st.session_state.qq_detective_score = 0
    if "qq_detective_seed" not in st.session_state:
        st.session_state.qq_detective_seed = 123
    if "qq_detective_complete" not in st.session_state:
        st.session_state.qq_detective_complete = False
    
    # Limit to 15 patterns
    MAX_PATTERNS = 15
    
    if st.session_state.qq_detective_round >= MAX_PATTERNS:
        st.success(t({
            "de": f"Ausgezeichnet! Du hast alle {MAX_PATTERNS} Muster abgeschlossen. Score: {st.session_state.qq_detective_score}/{MAX_PATTERNS}",
            "en": f"Excellent! You've completed all {MAX_PATTERNS} patterns. Score: {st.session_state.qq_detective_score}/{MAX_PATTERNS}"
        }))
        if st.button(t({"de": "Nochmal spielen", "en": "Play again"}), key="qq_detective_restart"):
            st.session_state.qq_detective_round = 0
            st.session_state.qq_detective_score = 0
            st.rerun(scope="fragment")
        return
    
    # Patterns to detect (cycle through)
    patterns = [
        {"dist": "normal", "name": {"de": "Normalverteilung (Diagonale)", "en": "Normal (Diagonal)"}},
        {"dist": "right_skew", "name": {"de": "Rechtsschiefe (Kurve nach oben)", "en": "Right-Skewed (Upward curve)"}},
        {"dist": "heavy_tails", "name": {"de": "Schwere Ränder (S-Kurve)", "en": "Heavy Tails (S-curve)"}},
        {"dist": "light_tails", "name": {"de": "Leichte Ränder (Umgekehrte S-Kurve)", "en": "Light Tails (Inverted S-curve)"}},
    ]
    
    current_pattern = patterns[st.session_state.qq_detective_round % len(patterns)]
    
    # Generate data for this pattern
    np.random.seed(st.session_state.qq_detective_seed + st.session_state.qq_detective_round)
    n = 40
    
    if current_pattern["dist"] == "normal":
        data = np.random.normal(0, 1, n)
        correct_answer = 0
    elif current_pattern["dist"] == "right_skew":
        data = np.random.lognormal(0, 0.6, n)
        correct_answer = 1
    elif current_pattern["dist"] == "heavy_tails":
        data = np.random.standard_t(3, n)  # t-distribution with 3 df = heavy tails
        correct_answer = 2
    else:  # light_tails
        data = np.random.uniform(-2, 2, n)
        correct_answer = 3
    
    # Calculate QQ coordinates
    sorted_data = np.sort(data)
    theoretical_quantiles = stats.norm.ppf(np.arange(1, n + 1) / (n + 1))
    
    col_plot, col_answer = st.columns([1.5, 1])
    
    with col_plot:
        # Create QQ-plot (mystery version - no labels revealing answer)
        fig = go.Figure()
        
        # Diagonal line
        line_min = min(theoretical_quantiles.min(), sorted_data.min())
        line_max = max(theoretical_quantiles.max(), sorted_data.max())
        fig.add_trace(go.Scatter(
            x=[line_min, line_max],
            y=[line_min, line_max],
            mode="lines",
            line=dict(color=COLOR_THEORY, width=2, dash="dash"),
            showlegend=False
        ))
        
        # Points
        fig.add_trace(go.Scatter(
            x=theoretical_quantiles,
            y=sorted_data,
            mode="markers",
            marker=dict(color=COLOR_DATA, size=9, line=dict(width=1, color="white")),
            showlegend=False
        ))
        
        fig.update_layout(
            height=280,
            margin=dict(t=30, b=40, l=50, r=20),
            xaxis_title=t({"de": "Theoretisch (Normal)", "en": "Theoretical (Normal)"}),
            yaxis_title=t({"de": "Beobachtet", "en": "Observed"}),
            plot_bgcolor="white",
            paper_bgcolor="white",
            xaxis=dict(showgrid=True, gridcolor="#e5e7eb"),
            yaxis=dict(showgrid=True, gridcolor="#e5e7eb"),
        )
        
        st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
    
    with col_answer:
        st.markdown(f"**{t({'de': 'Was zeigt dieses Muster?', 'en': 'What does this pattern show?'})}**")
        
        options = [
            t({"de": "Normalverteilung", "en": "Normal Distribution"}),
            t({"de": "Rechtsschiefe Verteilung", "en": "Right-Skewed Distribution"}),
            t({"de": "Schwere Ränder (mehr Extremwerte)", "en": "Heavy Tails (more extremes)"}),
            t({"de": "Leichte Ränder (weniger Extremwerte)", "en": "Light Tails (fewer extremes)"})
        ]
        
        answer_key = f"qq_detective_answer_{st.session_state.qq_detective_round}"
        selected = st.radio(
            t({"de": "Deine Antwort", "en": "Your answer"}),
            options=options,
            key=answer_key,
            label_visibility="collapsed"
        )
        
        check_key = f"qq_detective_check_{st.session_state.qq_detective_round}"
        if st.button(t({"de": "Antwort prüfen", "en": "Check Answer"}), key=check_key, type="primary"):
            selected_idx = options.index(selected)
            if selected_idx == correct_answer:
                st.session_state.qq_detective_score += 1
                st.success(t({"de": "Richtig!", "en": "Correct!"}))
            else:
                st.error(t({
                    "de": f"Leider falsch. Richtig wäre: {t(current_pattern['name'])}",
                    "en": f"Sorry, wrong. Correct was: {t(current_pattern['name'])}"
                }))
            
            # Move to next round
            st.session_state.qq_detective_round += 1
            st.rerun(scope="fragment")
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(f"**{t({'de': 'Punktestand', 'en': 'Score'})}:** {st.session_state.qq_detective_score}/{st.session_state.qq_detective_round}")
    
    # Completion
    if st.session_state.qq_detective_score >= 3:
        st.markdown("<br>", unsafe_allow_html=True)
        st.success(t({
            "de": "Meisterhaft! Du bist ein echter QQ-Plot Detektiv!",
            "en": "Masterful! You're a true QQ-Plot Detective!"
        }))


# ==============================================================================
# RENDER FUNCTION — MAIN PAGE STRUCTURE
# ==============================================================================

def render_subtopic_7_4(model):
    """7.4 Quantile-Quantile Plot — ULTRATHINK Apple-Quality Implementation"""
    
    # Inject equal height CSS
    inject_equal_height_css()
    
    # === HEADER ===
    st.header(t(content_7_4["title"]))
    st.caption(t(content_7_4["subtitle"]))
    st.markdown("---")
    
    # === 1. INTUITION (Magic Mirror Analogy) ===
    intuition_box(content_7_4["intuition"])
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # === 2. DEFINITION ===
    defn = content_7_4["definition"]
    render_definition(
        term=defn["term"],
        formal=defn["formal"],
        plain=defn["plain"]
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # === 3. INTERACTIVE COMPARISON: QQ-PLOT VS HISTOGRAM ===
    st.markdown(f"### {t({'de': 'QQ-Plot vs. Histogramm', 'en': 'QQ-Plot vs. Histogram'})}")
    qq_vs_histogram_interactive()
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # === 4. FORMULA ===
    formula = content_7_4["formula"]
    # Use bilingual formula
    formula_str = formula["formula_en"] if t({"de": "x", "en": "y"}) == "y" else formula["formula"]
    render_single_formula(
        title=formula["header"],
        intuition=formula["intuition"],
        formula=formula_str,
        variables=formula["variables"],
        insight=formula["insight"]
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # === 5. WORKED EXAMPLE (Continuation of 7.3.1) ===
    ex = content_7_4["worked_example"]
    render_worked_example(
        header=ex["header"],
        problem=ex["problem"],
        steps=ex["steps"],
        answer=ex["answer"]
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # === 6. INTERACTIVE: TWO-PHASE MISSION ===
    st.markdown(f"### {t({'de': 'Interaktives Labor', 'en': 'Interactive Lab'})}")
    
    tab_lab, tab_detective = st.tabs([
        t(content_7_4["mission_lab"]["title"]),
        t(content_7_4["mission_detective"]["title"])
    ])
    
    with tab_lab:
        qq_distribution_lab()
    
    with tab_detective:
        qq_pattern_detective()
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # === 7. FRAG DICH ===
    frag = content_7_4["frag_dich"]
    render_ask_yourself(
        header=frag["header"],
        questions=frag["questions"],
        conclusion=frag["conclusion"]
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # === 8. EXAM ESSENTIALS ===
    exam = content_7_4["exam_essentials"]
    render_exam_essentials(
        trap=exam["trap"],
        trap_rule=exam["trap_rule"],
        tips=exam["tips"]
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # === 9. MCQs ===
    st.markdown(f"### {t({'de': 'Prüfungstraining', 'en': 'Exam Practice'})}")
    
    # MCQ 1
    mcq1 = content_7_4["mcq_1"]
    opts1 = mcq1["options"]
    opt_labels1 = [t({"de": o["de"], "en": o["en"]}) for o in opts1]
    correct_idx1 = next((i for i, o in enumerate(opts1) if o["id"] == mcq1["correct_id"]), 0)
    
    with st.container(border=True):
        render_mcq(
            key_suffix="7_4_mcq1",
            question_text=t(mcq1["question"]),
            options=opt_labels1,
            correct_idx=correct_idx1,
            solution_text_dict=mcq1["solution"],
            success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
            error_msg_dict={"de": "Falsch.", "en": "Incorrect."},
            client=model,
            ai_context="QQ-Plot interpretation: upward curve at right end means right-skewed data",
            course_id="vwl",
            topic_id="7",
            subtopic_id="7.4",
            question_id="7_4_mcq1"
        )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # MCQ 2
    mcq2 = content_7_4["mcq_2"]
    opts2 = mcq2["options"]
    opt_labels2 = [t({"de": o["de"], "en": o["en"]}) for o in opts2]
    correct_idx2 = next((i for i, o in enumerate(opts2) if o["id"] == mcq2["correct_id"]), 0)
    
    with st.container(border=True):
        render_mcq(
            key_suffix="7_4_mcq2",
            question_text=t(mcq2["question"]),
            options=opt_labels2,
            correct_idx=correct_idx2,
            solution_text_dict=mcq2["solution"],
            success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
            error_msg_dict={"de": "Falsch.", "en": "Incorrect."},
            client=model,
            ai_context="QQ-Plot axes: X-axis shows theoretical quantiles, Y-axis shows empirical (observed) data",
            course_id="vwl",
            topic_id="7",
            subtopic_id="7.4",
            question_id="7_4_mcq2"
        )
