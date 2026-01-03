# Topic 3.7: Summary — Random Variables
import streamlit as st
import numpy as np
import plotly.graph_objects as go
from scipy.special import comb
from views.styles import inject_equal_height_css
from utils.localization import t
from utils.quiz_helper import render_mcq
from utils.ask_yourself import render_ask_yourself
from utils.exam_essentials import render_exam_essentials
from data.exam_questions import get_question
from utils.progress_tracker import track_question_answer, update_local_progress

# ==========================================
# 1. CONTENT DICTIONARY
# ==========================================
content_3_7 = {
    "title": {"de": "3.7 Zusammenfassung", "en": "3.7 Summary"},
    "subtitle": {"de": "Alles Wichtige zu Zufallsvariablen", "en": "Everything Important About Random Variables"},
    
    # CHAPTER INTUITION
    "intuition": {
        "header": {"de": "Die Intuition", "en": "The Intuition"},
        "text": {
            "de": "Dieses Kapitel hat dir die **drei Werkzeuge** gegeben, um Zufallsvariablen vollständig zu verstehen: (1) **Verteilungen** (PDF/CDF) — wie wahrscheinlich ist jeder Wert? (2) **Erwartungswert** (E[X]) — das 'Zentrum' der Verteilung (3) **Varianz** (Var) — wie 'breit' ist die Streuung? Diese Zusammenfassung zeigt dir die Formeln mit Erklärungen, wann du welche brauchst.",
            "en": "This chapter gave you the **three tools** to fully understand random variables: (1) **Distributions** (PDF/CDF) — how likely is each value? (2) **Expected Value** (E[X]) — the 'center' of the distribution (3) **Variance** (Var) — how 'spread out' is it? This summary shows you the formulas with explanations of when to use each."
        }
    },
    
    # FORMULA CARDS with full context (matching Topic 1.6 standard)
    "formula_cards": [
        {
            "title": {"de": "CDF → PDF", "en": "CDF → PDF"},
            "intuition": {"de": "Du hast die kumulative Verteilung und willst die Dichte.", "en": "You have the cumulative distribution and want the density."},
            "formula": r"f(x) = F'(x)",
            "variables": [
                {"symbol": "f(x)", "name": {"de": "PDF", "en": "PDF"}, "desc": {"de": "Dichtefunktion", "en": "Density function"}},
                {"symbol": "F(x)", "name": {"de": "CDF", "en": "CDF"}, "desc": {"de": "Kumulative Verteilung", "en": "Cumulative distribution"}},
                {"symbol": "F'(x)", "name": {"de": "Ableitung", "en": "Derivative"}, "desc": {"de": "Steigung der CDF", "en": "Slope of CDF"}}
            ],
            "when": {"de": "Aufgabe gibt CDF, fragt nach PDF/Dichte", "en": "Problem gives CDF, asks for PDF/density"}
        },
        {
            "title": {"de": "PDF → CDF", "en": "PDF → CDF"},
            "intuition": {"de": "Du hast die Dichte und willst die Wahrscheinlichkeit bis x.", "en": "You have the density and want probability up to x."},
            "formula": r"F(x) = \int_{-\infty}^{x} f(t)\,dt",
            "variables": [
                {"symbol": "F(x)", "name": {"de": "CDF", "en": "CDF"}, "desc": {"de": "P(X ≤ x)", "en": "P(X ≤ x)"}},
                {"symbol": "f(t)", "name": {"de": "PDF", "en": "PDF"}, "desc": {"de": "Dichtefunktion", "en": "Density function"}},
                {"symbol": r"\int", "name": {"de": "Integral", "en": "Integral"}, "desc": {"de": "Fläche unter Kurve", "en": "Area under curve"}}
            ],
            "when": {"de": "Aufgabe gibt PDF, fragt nach P(X ≤ x)", "en": "Problem gives PDF, asks for P(X ≤ x)"}
        },
        {
            "title": {"de": "E[X] diskret", "en": "E[X] discrete"},
            "intuition": {"de": "Gewichteter Durchschnitt aller möglichen Werte.", "en": "Weighted average of all possible values."},
            "formula": r"E[X] = \sum_x x \cdot P(X=x)",
            "variables": [
                {"symbol": "E[X]", "name": {"de": "Erwartungswert", "en": "Expected Value"}, "desc": {"de": "Das 'Zentrum'", "en": "The 'center'"}},
                {"symbol": "x", "name": {"de": "Werte", "en": "Values"}, "desc": {"de": "Mögliche Ergebnisse", "en": "Possible outcomes"}},
                {"symbol": "P(X=x)", "name": {"de": "Wahrscheinlichkeit", "en": "Probability"}, "desc": {"de": "Gewicht jedes Werts", "en": "Weight of each value"}}
            ],
            "when": {"de": "Tabelle mit Werten + Wahrscheinlichkeiten gegeben", "en": "Table with values + probabilities given"}
        },
        {
            "title": {"de": "E[X] stetig", "en": "E[X] continuous"},
            "intuition": {"de": "Wie diskret, aber mit Integral statt Summe.", "en": "Like discrete, but with integral instead of sum."},
            "formula": r"E[X] = \int x \cdot f(x)\,dx",
            "variables": [
                {"symbol": "E[X]", "name": {"de": "Erwartungswert", "en": "Expected Value"}, "desc": {"de": "Das 'Zentrum'", "en": "The 'center'"}},
                {"symbol": "f(x)", "name": {"de": "PDF", "en": "PDF"}, "desc": {"de": "Dichtefunktion", "en": "Density function"}},
                {"symbol": r"\int", "name": {"de": "Integral", "en": "Integral"}, "desc": {"de": "Über alle x", "en": "Over all x"}}
            ],
            "when": {"de": "Stetige Verteilung (PDF) gegeben", "en": "Continuous distribution (PDF) given"}
        },
        {
            "title": {"de": "Varianz (Shortcut)", "en": "Variance (Shortcut)"},
            "intuition": {"de": "Wie weit streuen die Werte vom Zentrum? IMMER diesen Shortcut nutzen!", "en": "How far do values spread from center? ALWAYS use this shortcut!"},
            "formula": r"Var(X) = E[X^2] - (E[X])^2",
            "variables": [
                {"symbol": "Var(X)", "name": {"de": "Varianz", "en": "Variance"}, "desc": {"de": "Streuungsmaß", "en": "Spread measure"}},
                {"symbol": "E[X²]", "name": {"de": "2. Moment", "en": "2nd Moment"}, "desc": {"de": "Erwartungswert der Quadrate", "en": "Expected value of squares"}},
                {"symbol": "(E[X])²", "name": {"de": "Quadrat von E[X]", "en": "Square of E[X]"}, "desc": {"de": "Zentrum zum Quadrat", "en": "Center squared"}}
            ],
            "when": {"de": "Immer wenn Varianz gefragt! 'E vom Quadrat minus Quadrat vom E'", "en": "Whenever variance asked! 'E of square minus square of E'"}
        },
        {
            "title": {"de": "Standardisierung", "en": "Standardization"},
            "intuition": {"de": "Wandle jeden Wert in 'Anzahl Standardabweichungen vom Mittelwert' um.", "en": "Convert any value to 'number of standard deviations from mean'."},
            "formula": r"Z = \frac{X - \mu}{\sigma}",
            "variables": [
                {"symbol": "Z", "name": {"de": "Z-Score", "en": "Z-Score"}, "desc": {"de": "Standardisierter Wert", "en": "Standardized value"}},
                {"symbol": "X", "name": {"de": "Originalwert", "en": "Original value"}, "desc": {"de": "Der Rohwert", "en": "The raw value"}},
                {"symbol": r"\mu", "name": {"de": "Mittelwert", "en": "Mean"}, "desc": {"de": "Zentrum", "en": "Center"}},
                {"symbol": r"\sigma", "name": {"de": "Std.abw.", "en": "Std.dev."}, "desc": {"de": "Streuung", "en": "Spread"}}
            ],
            "when": {"de": "Vergleich zwischen Skalen oder Z-Tabelle nutzen", "en": "Comparing across scales or using Z-table"}
        }
    ],
    
    # ASK YOURSELF
    "ask_yourself": {
        "header": {"de": "Frag dich selbst", "en": "Ask Yourself"},
        "questions": [
            {"de": "Wann benutze ich die PDF und wann die CDF?", "en": "When do I use the PDF vs the CDF?"},
            {"de": "Was ist der Unterschied zwischen E[X²] und (E[X])²?", "en": "What's the difference between E[X²] and (E[X])²?"},
            {"de": "Warum ändert Var(X+b) die Varianz nicht?", "en": "Why doesn't Var(X+b) change the variance?"},
            {"de": "Was bedeutet 'gleiche Verteilung' vs 'X = Y'?", "en": "What does 'same distribution' mean vs 'X = Y'?"},
        ],
        "conclusion": {
            "de": "Wenn du diese Fragen beantworten kannst, bist du bereit für die Prüfung!",
            "en": "If you can answer these questions, you're ready for the exam!"
        }
    },
    
    # INTERACTIVE
    "interactive": {
        "title": {"de": "Die Symmetrie-Maschine", "en": "The Symmetry Explorer"},
        "desc": {
            "de": "Ruben und Jochen spielen ein faires Münzspiel. Toggle die Overlay-Ansicht!",
            "en": "Ruben and Jochen play a fair coin game. Toggle the overlay view!"
        }
    },
    
    # EXAM ESSENTIALS
    "exam_essentials": {
        "tips": [
            {
                "tip": {"de": "Varianz-Shortcut: E[X²] - (E[X])² statt E[(X-μ)²]", "en": "Variance Shortcut: E[X²] - (E[X])² instead of E[(X-μ)²]"},
                "why": {"de": "Viel schneller zu rechnen!", "en": "Much faster to calculate!"}
            },
            {
                "tip": {"de": "CDF-Sandwich: P(a<X≤b) = F(b) - F(a)", "en": "CDF Sandwich: P(a<X≤b) = F(b) - F(a)"},
                "why": {"de": "Funktioniert für diskret UND stetig!", "en": "Works for discrete AND continuous!"}
            },
            {
                "tip": {"de": "Lineare Transformation: Var(aX+b) = a²Var(X) — b verschwindet!", "en": "Linear Transform: Var(aX+b) = a²Var(X) — b disappears!"},
                "why": {"de": "Verschiebung ändert Streuung nicht.", "en": "Shifting doesn't change spread."}
            },
            {
                "tip": {"de": "Symmetrie-Hack: Symmetrisch um 0 → E[X] = 0", "en": "Symmetry Hack: Symmetric around 0 → E[X] = 0"},
                "why": {"de": "Sofort ablesen, nicht rechnen!", "en": "Read off instantly, don't calculate!"}
            },
            {
                "tip": {"de": "Z-Score Reisepass: Standardisiere zu N(0,1), dann eine Tabelle für alle!", "en": "Z-Score Passport: Standardize to N(0,1), then one table for all!"},
                "why": {"de": "Universal für jede Normalverteilung.", "en": "Universal for any normal distribution."}
            }
        ],
        "trap": {
            "de": "<strong>Gleiche Verteilung ≠ Gleiche Variable:</strong> X und Y können dieselbe Verteilung haben, aber X ≠ Y. Beispiel: Ruben's Gewinn X und Jochen's Gewinn -X haben GLEICHE Verteilung, aber X ≠ -X!",
            "en": "<strong>Same Distribution ≠ Same Variable:</strong> X and Y can have the same distribution, but X ≠ Y. Example: Ruben's winnings X and Jochen's winnings -X have the SAME distribution, but X ≠ -X!"
        },
        "trap_rule": {
            "de": "Verwechsle nie 'identisch verteilt' mit 'gleich'!",
            "en": "Never confuse 'identically distributed' with 'equal'!"
        }
    }
}


def render_subtopic_3_7(model):
    """3.7 Summary — Complete chapter review
    
    Order: Intuition → Theory → Ask Yourself → Interactive → Exam Essentials → MCQ
    """
    
    inject_equal_height_css()
    
    st.header(t(content_3_7["title"]))
    st.caption(t(content_3_7["subtitle"]))
    st.markdown("---")
    
    # === SECTION 1: INTUITION (Header-Out) ===
    st.markdown(f"### {t(content_3_7['intuition']['header'])}")
    with st.container(border=True):
        st.markdown(t(content_3_7["intuition"]["text"]))
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # === SECTION 2: THEORY (FORMULA CARDS with Variable Decoder) ===
    st.markdown(f"### {t({'de': 'Formel-Spickzettel', 'en': 'Formula Cheat Sheet'})}")
    
    render_formula_cards()
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # === SECTION 3: ASK YOURSELF ===
    render_ask_yourself(
        header=content_3_7["ask_yourself"]["header"],
        questions=content_3_7["ask_yourself"]["questions"],
        conclusion=content_3_7["ask_yourself"]["conclusion"]
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # === SECTION 4: INTERACTIVE (SYMMETRY EXPLORER) ===
    render_symmetry_explorer()
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # === SECTION 5: EXAM ESSENTIALS ===
    render_exam_essentials(
        tips=content_3_7["exam_essentials"]["tips"],
        trap=content_3_7["exam_essentials"]["trap"],
        trap_rule=content_3_7["exam_essentials"]["trap_rule"]
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # === SECTION 6: MCQ ===
    st.markdown(f"### {t({'de': 'Prüfungstraining', 'en': 'Exam Practice'})}")
    
    q_data = get_question("3.7", "hs2024_mc11")
    if q_data:
        with st.container(border=True):
            st.caption(q_data.get("source", ""))
            opts = q_data.get("options", [])
            if opts and isinstance(opts[0], dict):
                option_labels = [t(o) for o in opts]
            else:
                option_labels = opts
            
            render_mcq(
                key_suffix="3_7_mc11",
                question_text=t(q_data["question"]),
                options=option_labels,
                correct_idx=q_data["correct_idx"],
                solution_text_dict=q_data["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Falsch.", "en": "Incorrect."},
                client=model,
                ai_context="Symmetric distributions in fair coin games.",
                course_id="vwl",
                topic_id="3",
                subtopic_id="3.7",
                question_id="hs2024_mc11"
            )


def render_formula_cards():
    """Render formula cards in 2-column grid with FULL context per card.
    
    Each card includes:
    - Title
    - Intuition (when to use)
    - Formula
    - Variable Decoder
    - 'When to use' hint
    """
    cards = content_3_7["formula_cards"]
    
    # Render in 2-column grid
    for i in range(0, len(cards), 2):
        c1, c2 = st.columns(2, gap="medium")
        
        # Left card
        with c1:
            render_single_formula_card(cards[i])
        
        # Right card (if exists)
        if i + 1 < len(cards):
            with c2:
                render_single_formula_card(cards[i + 1])


def render_single_formula_card(card):
    """Render a single formula card matching Topic 1.6 gold standard.
    
    Structure (ONE container with --- separators):
    1. Title (bold)
    2. Intuition (italic, no math)
    3. Formula (prominent)
    --- separator ---
    4. Variables: bullet list
    --- separator ---
    5. When/Insight (italic)
    """
    with st.container(border=True):
        # 1. Title
        st.markdown(f"**{t(card['title'])}**")
        
        # 2. Intuition (italic, no nested container)
        st.markdown(f"*{t(card['intuition'])}*")
        
        # 3. Formula (prominent)
        st.latex(card['formula'])
        
        # --- Variable Decoder ---
        st.markdown("---")
        st.markdown(f"**{t({'de': 'Variablen', 'en': 'Variables'})}:**")
        for v in card['variables']:
            name = t(v['name'])
            desc = t(v['desc'])
            st.markdown(f"• ${v['symbol']}$ = **{name}** — {desc}")
        
        # --- When to use (insight) ---
        st.markdown("---")
        st.markdown(f"*{t(card['when'])}*")


@st.fragment
def render_symmetry_explorer():
    """Interactive symmetry visualization"""
    inter = content_3_7["interactive"]
    st.markdown(f"### {t(inter['title'])}")
    
    with st.container(border=True):
        st.markdown(t(inter["desc"]))
        st.markdown("---")
        
        # State
        if "sym_n_rounds" not in st.session_state:
            st.session_state.sym_n_rounds = 10
        if "sym_show_overlay" not in st.session_state:
            st.session_state.sym_show_overlay = False
        if "sym_mission_done" not in st.session_state:
            st.session_state.sym_mission_done = False
        
        col_ctrl, col_vis = st.columns([1, 2], gap="large")
        
        with col_ctrl:
            n_rounds = st.slider(
                t({"de": "Runden (n)", "en": "Rounds (n)"}),
                2, 20, st.session_state.sym_n_rounds, 2,
                key="sym_n_rounds"
            )
            
            show_overlay = st.toggle(
                t({"de": "Zeige -X Overlay", "en": "Show -X Overlay"}),
                value=st.session_state.sym_show_overlay,
                key="sym_show_overlay"
            )
            
            if show_overlay:
                if not st.session_state.sym_mission_done:
                    st.balloons()
                    st.session_state.sym_mission_done = True
                    user = st.session_state.get("user")
                    if user:
                        track_question_answer(user["localId"], "vwl", "3", "3.7", "3_7_symmetry_mission", True)
                        update_local_progress("3", "3.7", "3_7_symmetry_mission", True)
                
                st.success(t({"de": "Identisch! X und -X haben dieselbe Verteilung.", "en": "Identical! X and -X have the same distribution."}))
            else:
                st.info(t({"de": "Toggle aktivieren!", "en": "Toggle to reveal!"}))
        
        with col_vis:
            fig = create_symmetry_plot(n_rounds, show_overlay)
            st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
        
        # Pro tip
        st.markdown(f"""
<div style="background: #f4f4f5; border-radius: 8px; padding: 12px; color: #3f3f46; margin-top: 8px;">
<strong>Pro Tip:</strong> {t({'de': 'Bei fairen Spielen haben X und -X IMMER dieselbe Verteilung. "Gleiche Verteilung" ≠ "X = Y"!', 'en': 'In fair games, X and -X ALWAYS have the same distribution. "Same distribution" ≠ "X = Y"!'})}
</div>
""", unsafe_allow_html=True)


def create_symmetry_plot(n_rounds, show_overlay):
    """Create distribution visualization"""
    values = list(range(-n_rounds, n_rounds + 1, 2))
    probs = []
    for x in values:
        k = (x + n_rounds) // 2
        prob = comb(n_rounds, k, exact=True) * (0.5 ** n_rounds)
        probs.append(prob)
    
    fig = go.Figure()
    
    # X (Ruben) - Blue
    fig.add_trace(go.Bar(
        x=values, y=probs,
        name="X (Ruben)",
        marker_color='#007AFF',
        opacity=0.8, width=1.5
    ))
    
    # -X (Jochen) - Purple overlay
    if show_overlay:
        fig.add_trace(go.Bar(
            x=values, y=probs,
            name="-X (Jochen)",
            marker_color='#AF52DE',
            opacity=0.5, width=1.5
        ))
    
    fig.add_vline(x=0, line_dash="dash", line_color="#6B7280", line_width=1)
    
    fig.update_layout(
        xaxis=dict(title=t({"de": "Gewinn", "en": "Winnings"}), fixedrange=True, showgrid=False),
        yaxis=dict(title="P", fixedrange=True, showgrid=True, gridcolor='#E5E5EA'),
        barmode='overlay',
        height=280,
        margin=dict(l=40, r=20, t=20, b=40),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        legend=dict(orientation="h", y=1.1, x=0.5, xanchor="center")
    )
    
    return fig
