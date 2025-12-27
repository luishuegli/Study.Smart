import streamlit as st
import plotly.graph_objects as go
import math
from views.styles import render_icon
from utils.localization import t
from utils.quiz_helper import render_mcq

# --- 0. SAFETY CHECK ---
try:
    st_version = st.__version__.split(".")
    if int(st_version[0]) == 1 and int(st_version[1]) < 35:
        st.error(f"Update needed. Streamlit {st.__version__} doesn't support click events. Run `pip install --upgrade streamlit`.")
except:
    pass

# --- DATA & STORY ---
content_1_7 = {
    "title": {"de": "1.7 Bedingte Wahrscheinlichkeit", "en": "1.7 Conditional Probability"},
    "story": {
        "intro": {
            "de": "Dein Chef fragt: **'Wie hoch ist die Wahrscheinlichkeit für ROT, gegeben dass es ein KREIS ist?'**",
            "en": "Your boss asks: **'What is the probability of RED, given that it is a CIRCLE?'**"
        },
        "notation": {
            "de": "In Mathe-Sprache: $P(\\text{Rot} | \\text{Kreis})$. Der Strich $|$ ist der Filter.",
            "en": "In math notation: $P(\\text{Red} | \\text{Circle})$. The bar $|$ is the Filter."
        },
        "instruction": {
            "de": "Deine Aufgabe: Sei der Filter. Klicke auf alles, was **KEIN KREIS** ist, um es aus dem Universum zu werfen.",
            "en": "Your Mission: Be the Filter. Click on everything that is **NOT A CIRCLE** to kick it out of the universe."
        }
    },
    "theory_cards": {
        "cond": {
            "title": {"de": "Bedingte Wahrscheinlichkeit", "en": "Conditional Probability"},
            "def": {"de": "Die Wahrscheinlichkeit von A, *gegeben* B.", "en": "The probability of A, *given* B."},
            "latex": r"P(A|B) = \frac{P(A \cap B)}{P(B)}"
        },
        "indep": {
            "title": {"de": "Unabhängigkeit", "en": "Independence"},
            "def": {"de": "Information über B ändert nichts an A.", "en": "Information about B implies nothing about A."},
            "latex": r"P(A \cap B) = P(A) \cdot P(B)"
        }
    },
    "exam": {
        "q1": {
            "title": {"de": "Prüfungstraining: HS2024 (MC 3)", "en": "Exam Practice: HS2024 (MC 3)"},
            "question": {"de": "**Gegeben:** $\\mathbb{P}(A)=\\frac{1}{2}$, $\\mathbb{P}(B)=\\frac{2}{3}$ und $\\mathbb{P}(A\\cap B)=\\frac{1}{4}$.\n\n**Gesucht:** $\\mathbb{P}(A|\\overline{B})$.", "en": "**Given:** $\\mathbb{P}(A)=\\frac{1}{2}$, $\\mathbb{P}(B)=\\frac{2}{3}$ and $\\mathbb{P}(A\\cap B)=\\frac{1}{4}$.\n\n**Find:** $\\mathbb{P}(A|\\overline{B})$."},
            "options": ["0.25", "0.50", "0.75", "0.33"],
            "correct_opt": "0.75",
            "solution": {
                "de": r"""
**Schritt 1: Formel aufstellen**
$P(A|\overline{B}) = \frac{P(A \cap \overline{B})}{P(\overline{B})}$

**Schritt 2: Nenner berechnen**
$P(\overline{B}) = 1 - P(B) = 1 - \frac{2}{3} = \frac{1}{3}$.

**Schritt 3: Zähler berechnen**
$P(A \cap \overline{B})$ ist 'A ohne B'.
$P(A \cap \overline{B}) = P(A) - P(A \cap B) = \frac{1}{2} - \frac{1}{4} = \frac{1}{4}$.

**Schritt 4: Einsetzen**
$\frac{1/4}{1/3} = \frac{1}{4} \cdot \frac{3}{1} = \frac{3}{4} = \mathbf{0.75}$.
                """,
                "en": r"""
**Step 1: Setup Formula**
$P(A|\overline{B}) = \frac{P(A \cap \overline{B})}{P(\overline{B})}$

**Step 2: Calculate Denominator**
$P(\overline{B}) = 1 - P(B) = 1 - \frac{2}{3} = \frac{1}{3}$.

**Step 3: Calculate Numerator**
$P(A \cap \overline{B})$ is 'A without B'.
$P(A \cap \overline{B}) = P(A) - P(A \cap B) = \frac{1}{2} - \frac{1}{4} = \frac{1}{4}$.

**Step 4: Solve**
$\frac{1/4}{1/3} = \frac{1}{4} \cdot \frac{3}{1} = \frac{3}{4} = \mathbf{0.75}$.
                """
            },
            "hint": {
                "de": "Hinweis: Nutze die Formel $P(A|\\overline{B}) = \\frac{P(A \\cap \\overline{B})}{P(\\overline{B})}$.",
                "en": "Hint: Use the formula $P(A|\\overline{B}) = \\frac{P(A \\cap \\overline{B})}{P(\\overline{B})}$."
            }
        },
        "q2": {
            "title": {"de": "Logik-Check: Unabhängigkeit (MC 5)", "en": "Logic Check: Independence (MC 5)"},
            "question": {
                "de": "**Zufallsexperiment:** Ziehen von 4 Zahlen aus den ersten 12 Primzahlen (ohne Zurücklegen).\n\n$A$: Summe ist ungerade.\n$B$: Alle 4 Zahlen sind ungerade.\n\n**Sind $A$ und $B$ unabhängig oder disjunkt?**",
                "en": "**Experiment:** Draw 4 numbers from the first 12 primes (without replacement).\n\n$A$: Sum is odd.\n$B$: All 4 numbers are odd.\n\n**Are $A$ and $B$ independent or disjoint?**"
            },
            "options": [
                "Unabhängig und Disjunkt",
                "Abhängig und Disjunkt",
                "Unabhängig und Nicht-Disjunkt",
                "Abhängig und Nicht-Disjunkt"
            ],
            "correct_opt": "Abhängig und Disjunkt",
            "solution": {
                "de": r"""
**Analyse:**
Es gibt nur *eine* gerade Primzahl (2).
$A$ (Summe Ungerade) braucht die 2 (3 ungerade + 1 gerade).
$B$ (Alle Ungerade) verbietet die 2.
$\Rightarrow$ Disjunkt.

**Abhängigkeit:**
Disjunkt impliziert Abhängigkeit (wenn $P>0$), da das Eintreten von A das Eintreten von B ausschließt.
                """,
                "en": r"""
**Analysis:**
There is only *one* even prime (2).
$A$ (Odd Sum) requires 2 (3 odd + 1 even).
$B$ (All Odd) forbids 2.
$\Rightarrow$ Disjoint.

**Dependency:**
Disjoint implies dependency (if $P>0$), because A occurring prevents B from occurring.
                """
            },
            "hint": {
                "de": "Hinweis: Wie viele gerade Primzahlen gibt es?",
                "en": "Hint: How many even prime numbers are there?"
            }
        }
    },
    "feedback": {
        "success": {
            "title": {"de": "Mission erfüllt!", "en": "Mission Accomplished!"},
            "mastery_title": {"de": "Was hast du gerade getan?", "en": "What did you just do?"},
            "intuition_title": {"de": "1. Die Intuition", "en": "1. The Intuition"},
            "check_items": {
                "de": [
                    "Du hast die Quadrate als 'unmöglich' markiert.",
                    "Dein neues Universum besteht nur noch aus 6 Kreisen.",
                    "Innerhalb dieser 6 Kreise sind 3 rot."
                ],
                "en": [
                    "You marked the squares as 'impossible'.",
                    "Your new universe now consists only of 6 circles.",
                    "Within these 6 circles, 3 are red."
                ]
            },
            "math_title": {"de": "2. Die Mathematik", "en": "2. The Math"},
            "calculated_formula": r"P(A|B) = \frac{3}{6} = 0.50",
            "translation": {
                "de": "Bedingte Wahrscheinlichkeit ist einfach eine Wahrscheinlichkeit in einem kleineren Universum.",
                "en": "Conditional probability is simply a probability calculated in a smaller universe."
            },
            "big_picture_title": {"de": "3. Der Lerneffekt", "en": "3. The Learning Effect"},
            "comparison_intro": {
                "de": "Durch das Entfernen der Quadrate hast du die **Grundlage** verändert:",
                "en": "By removing the squares, you changed the **Baseline**:"
            },
            "original_prob": {"de": "Ursprüngliche Wahrscheinlichkeit", "en": "Original Probability"},
            "conditional_prob": {"de": "Bedingte Wahrscheinlichkeit", "en": "Conditional Probability"},
            "conclusion": {
                "de": "Information (B) reduziert Unsicherheit, indem sie das Universum verkleinert.",
                "en": "Information (B) reduces uncertainty by shrinking the possible universe."
            }
        }
    },
    "independence": {
        "mission": {
            "title": {"de": "Die Balance-Aufgabe", "en": "The Balance Challenge"},
            "intro": {
                "de": "Deine Aufgabe: **Balanciere die Waage**. Klicke auf Formen, um sie zu ändern, bis die Wahrscheinlichkeit für ROT in beiden Welten gleich ist.",
                "en": "Your Mission: **Balance the Scale**. Click shapes to change them until the probability of RED is the same in both worlds."
            },
            "instruction": {
                "de": "Klicke auf eine Form, um sie zu ändern: Blaues Quadrat → Rotes Quadrat → Blauer Kreis → Roter Kreis",
                "en": "Click a shape to cycle: Blue Square → Red Square → Blue Circle → Red Circle"
            }
        },
        "metrics": {
            "p_a_label": {"de": "Gesamt-Welt", "en": "Total World"},
            "p_a_given_b_label": {"de": "Kreis-Welt", "en": "Circle World"},
            "status_dependent": {"de": "Abhängig", "en": "Dependent"},
            "status_independent": {"de": "Unabhängig!", "en": "Independent!"}
        },
        "feedback": {
            "dependent": {
                "de": "Die Wahrscheinlichkeit für ROT ist in der Kreis-Welt anders als in der Gesamt-Welt. Das bedeutet: **Information über Kreise verändert deine Einschätzung über ROT**.",
                "en": "The probability of RED is different in the Circle World than in the Total World. This means: **Information about Circles changes your belief about RED**."
            },
            "independent": {
                "de": "Perfekt! Die Wahrscheinlichkeit für ROT ist in beiden Welten gleich. **Information über Kreise gibt dir keine neue Information über ROT**.",
                "en": "Perfect! The probability of RED is the same in both worlds. **Information about Circles gives you no new information about RED**."
            }
        },
        "mastery": {
            "title": {"de": "Was hast du entdeckt?", "en": "What did you discover?"},
            "intuition_title": {"de": "1. Die Intuition", "en": "1. The Intuition"},
            "check_items": {
                "de": [
                    "Du hast die Formen so arrangiert, dass der Anteil ROT überall gleich ist.",
                    "In der Gesamt-Welt und in der Kreis-Welt ist der Anteil ROT identisch.",
                    "Das bedeutet: Wissen über 'Kreis' ändert nichts an der Wahrscheinlichkeit für 'Rot'."
                ],
                "en": [
                    "You arranged the shapes so the proportion of RED is the same everywhere.",
                    "In the Total World and in the Circle World, the proportion of RED is identical.",
                    "This means: Knowing 'Circle' doesn't change the probability of 'Red'."
                ]
            },
            "math_title": {"de": "2. Die Mathematik", "en": "2. The Math"},
            "translation": {
                "de": "Unabhängigkeit bedeutet: Der Filter gibt keine neue Information.",
                "en": "Independence means: The filter provides no new information."
            },
            "big_picture_title": {"de": "3. Der Lerneffekt", "en": "3. The Learning Effect"},
            "comparison_intro": {
                "de": "Du hast die **Balance** erreicht:",
                "en": "You achieved the **Balance**:"
            },
            "conclusion": {
                "de": "Unabhängigkeit ist die Abwesenheit von Information. Wenn A und B unabhängig sind, sagt B dir nichts über A.",
                "en": "Independence is the absence of information. When A and B are independent, B tells you nothing about A."
            }
        }
    }
}

def render_subtopic_1_7(model):
    """1.7 Narrative & Notation Bridge"""
    
    # FIX: Global CSS to prevent LaTeX cutoff in this topic
    st.markdown("""
        <style>
        /* Fix LaTeX rendering cutoff - scoped to this page */
        div[data-testid="stMarkdownContainer"] div.katex-display,
        div[data-testid="stMarkdownContainer"] .katex-html {
            overflow: visible !important;
            padding-top: 20px !important;
            padding-bottom: 20px !important;
        }
        </style>
    """, unsafe_allow_html=True)
    
    st.header(t(content_1_7["title"]))

    # --- THEORY CARDS ---
    with st.container(border=True):
        c1, c2 = st.columns(2, gap="medium")
        with c1:
            st.markdown(f"**{t(content_1_7['theory_cards']['cond']['title'])}**")
            st.caption(t(content_1_7["theory_cards"]["cond"]["def"]))
            st.latex(content_1_7["theory_cards"]["cond"]["latex"])
        with c2:
            st.markdown(f"**{t(content_1_7['theory_cards']['indep']['title'])}**")
            st.caption(t(content_1_7["theory_cards"]["indep"]["def"]))
            st.latex(content_1_7["theory_cards"]["indep"]["latex"])
    
    st.markdown("<br>", unsafe_allow_html=True)

    # --- 1. STATE ---
    if "visible_indices_1_7" not in st.session_state:
        st.session_state.visible_indices_1_7 = list(range(9))

    # Grid Data (N=9)
    # 0-2: Red Circles (Target)
    # 3-5: Blue Circles (Condition B)
    # 6-8: Squares (Noise)
    points_data = [
        {"idx": 0, "x": 0, "y": 2, "c": "#FF4B4B", "s": "circle", "type": "target"},
        {"idx": 1, "x": 1, "y": 1, "c": "#FF4B4B", "s": "circle", "type": "target"},
        {"idx": 2, "x": 0, "y": 0, "c": "#FF4B4B", "s": "circle", "type": "target"},
        {"idx": 3, "x": 1, "y": 2, "c": "#1E88E5", "s": "circle", "type": "cond"},
        {"idx": 4, "x": 2, "y": 2, "c": "#1E88E5", "s": "circle", "type": "cond"},
        {"idx": 5, "x": 2, "y": 1, "c": "#1E88E5", "s": "circle", "type": "cond"},
        {"idx": 6, "x": 0, "y": 1, "c": "#E0E0E0", "s": "square", "type": "noise"},
        {"idx": 7, "x": 1, "y": 0, "c": "#E0E0E0", "s": "square", "type": "noise"},
        {"idx": 8, "x": 2, "y": 0, "c": "#E0E0E0", "s": "square", "type": "noise"},
    ]

    # --- 2. CALCULATE LIVE STATS ---
    visible_set = set(st.session_state.visible_indices_1_7)
    current_noise = sum(1 for p in points_data if p["idx"] in visible_set and p["type"] == "noise")
    current_denom = len(visible_set)
    is_done = (current_noise == 0)

    # --- 3. LAYOUT: STORY MODE ---
    
    # Section Header with Icon - Add inline CSS to ensure icon is on the left
    st.markdown(f"""
        <style>
        .icon-header {{
            display: flex !important;
            align-items: center !important;
            gap: 12px !important;
            margin-bottom: 16px !important;
        }}
        .icon-header svg {{
            flex-shrink: 0 !important;
        }}
        </style>
        <div class="icon-header">
            {render_icon('target', size=24)}
            <h3 style="margin:0;">Experiment</h3>
        </div>
    """, unsafe_allow_html=True)
    
    # The Interactive Experiment
    with st.container(border=True):
        # 1. NARRATIVE HUD (AGGRESSIVE GUIDANCE)
        if current_noise == 3:
            st.info(f"🎯 **{t({'de': 'Schritt 1:', 'en': 'Step 1:'})}** {t({'de': 'Klicke auf die Quadrate, um sie aus dem Universum zu werfen.', 'en': 'Click on the squares to kick them out of the universe.'})}")
        elif current_noise > 0:
            st.success(f"✨ **{t({'de': 'Schritt 2:', 'en': 'Step 2:'})}** {t({'de': 'Gut! Das Universum schrumpft. Entferne alle Quadrate.', 'en': 'Good! The universe is shrinking. Remove all squares.'})}")
        else:
            st.balloons()
            st.success(f"🏆 **{t({'de': 'Filter Komplett!', 'en': 'Filter Complete!'})}** {t({'de': 'In der Kreis-Welt ist Rot nun viel wahrscheinlicher.', 'en': 'In the Circle-World, Red is now much more likely.'})}")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        col_vis, col_math = st.columns([1.5, 1], gap="large")

        with col_vis:
            st.caption("Click the Squares to remove them.")
            
            # CHART GENERATION
            x, y, c, s, op, ids = [], [], [], [], [], []
            for p in points_data:
                x.append(p["x"])
                y.append(p["y"])
                c.append(p["c"])
                s.append(p["s"])
                ids.append(p["idx"])
                op.append(1.0 if p["idx"] in visible_set else 0.05) # Ghosting

            fig = go.Figure()
            fig.add_trace(go.Scatter(
                x=x, y=y, mode='markers',
                marker=dict(size=50, color=c, symbol=s, opacity=op, line=dict(width=0)),
                hoverinfo='none', ids=ids
            ))

            fig.update_layout(
                xaxis=dict(visible=False, fixedrange=True, range=[-0.5, 2.5]),
                yaxis=dict(visible=False, fixedrange=True, range=[-0.5, 2.5], scaleanchor="x", scaleratio=1),
                margin=dict(l=10, r=10, t=10, b=10),
                height=350,
                clickmode='event+select', dragmode=False,
                plot_bgcolor='rgba(0,0,0,0)'
            )

            event = st.plotly_chart(fig, on_select="rerun", selection_mode="points", use_container_width=True, key="story_chart_1_7", config={'displayModeBar': False})

            # HANDLE CLICK - Optimized for instant response
            if event and event.get("selection") and event["selection"].get("points"):
                clicked_point = event["selection"]["points"][0]
                p_idx = points_data[clicked_point["point_index"]]["idx"]
                p_type = points_data[clicked_point["point_index"]]["type"]
                
                if p_type == "noise" and p_idx in st.session_state.visible_indices_1_7:
                    st.session_state.visible_indices_1_7.remove(p_idx)
                    st.rerun()
                elif p_type != "noise" and p_idx in st.session_state.visible_indices_1_7:
                    st.toast("⚠️ Keep the Circles! We need them for the condition.", icon="⚠️")

        # C. The "Live Math" Panel (Right Side) - Simplified
        with col_math:
            st.markdown(f"**{t({'de': 'Live-Notation', 'en': 'Live Notation'})}**")
            st.latex(fr"P(\text{{Rot}} \mid \text{{Kreis}}) = \frac{{\text{{\color{{#FF4B4B}}{{Treffer}}}}}}{{\text{{\color{{#1E88E5}}{{Universum}}}}}}")
            
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown("**Current Status:**")
            
            # Color coding: Red numerator (target), Blue denominator (universe/condition)
            num_color = "#FF4B4B"  # Always red for target
            denom_color = "#1E88E5"  # Always blue for universe/condition
            
            # The Live Equation with proper color coding
            st.latex(fr"P = \frac{{\color{{{num_color}}}{{3}}}}{{\color{{{denom_color}}}{{{current_denom}}}}}")
            
            # Brief feedback during progress
            if not is_done:
                removed_count = 3 - current_noise
                st.info(f"Squares Removed: {removed_count}/3")
    
    # THE MASTERY CARD - Full Width Below the Interactive Section
    if is_done:
        st.success(t(content_1_7["feedback"]["success"]["title"]))
        
        with st.container(border=True):
            st.markdown(f"### {t(content_1_7['feedback']['success']['mastery_title'])}")
            
            # Column split for visual clarity
            col_a, col_b = st.columns([1, 1])
            
            with col_a:
                st.markdown(f"**{t(content_1_7['feedback']['success']['intuition_title'])}**")
                for item in t(content_1_7["feedback"]["success"]["check_items"]):
                    st.markdown(f"- {item}")
            
            with col_b:
                st.markdown(f"**{t(content_1_7['feedback']['success']['math_title'])}**")
                st.latex(content_1_7["feedback"]["success"]["calculated_formula"])
                st.info(t(content_1_7["feedback"]["success"]["translation"]))

            st.divider()
            
            st.markdown(f"**{t(content_1_7['feedback']['success']['big_picture_title'])}**")
            st.markdown(t(content_1_7["feedback"]["success"]["comparison_intro"]))
            
            # Side-by-side comparison
            comp_col1, comp_col2 = st.columns(2)
            with comp_col1:
                st.markdown(f"**{t(content_1_7['feedback']['success']['original_prob'])}:**")
                st.latex(r"P(A) = \frac{3}{9} = 0.33")
            with comp_col2:
                st.markdown(f"**{t(content_1_7['feedback']['success']['conditional_prob'])}:**")
                st.latex(r"P(A|B) = \frac{3}{6} = 0.50")
            
            st.markdown("<br>", unsafe_allow_html=True)
            st.warning(t(content_1_7["feedback"]["success"]["conclusion"]))
        
        # Progress Tracking
        from utils.progress_tracker import update_local_progress, track_question_answer
        user = st.session_state.get("user")
        if user:
            update_local_progress("1", "1.7", "1_7_narrative_mission", True)
            track_question_answer(user["localId"], "vwl", "1", "1.7", "1_7_narrative_mission", True)
            
    # Reset
    if st.button("Reset Story"):
        st.session_state.visible_indices_1_7 = list(range(9))
        st.rerun()

    # --- EXAM SECTION ---
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown(f"""
        <div class="icon-header">
            {render_icon('clipboard-list', size=24)}
            <h3 style="margin:0;">{t({'de': 'Prüfungstraining', 'en': 'Exam Practice'})}</h3>
        </div>
    """, unsafe_allow_html=True)
    
    # Q1
    with st.container(border=True):
        st.markdown(f"**{t(content_1_7['exam']['q1']['title'])}**")
        render_mcq(
            key_suffix="1_7_q1_narrative",
            question_text=t(content_1_7["exam"]["q1"]["question"]),
            options=content_1_7["exam"]["q1"]["options"],
            correct_idx=content_1_7["exam"]["q1"]["options"].index(content_1_7["exam"]["q1"]["correct_opt"]),
            solution_text_dict=content_1_7["exam"]["q1"]["solution"],
            success_msg_dict={"de": "Korrekt", "en": "Correct"},
            error_msg_dict={"de": "Falsch", "en": "Incorrect"},
            model=model,
            ai_context="Conditional probability", 
            hint_text_dict=content_1_7["exam"]["q1"]["hint"],
            course_id="vwl", topic_id="1", subtopic_id="1.7", question_id="1_7_q1_narrative"
        )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Q2
    with st.container(border=True):
        st.markdown(f"**{t(content_1_7['exam']['q2']['title'])}**")
        render_mcq(
            key_suffix="1_7_q2_narrative",
            question_text=t(content_1_7["exam"]["q2"]["question"]),
            options=content_1_7["exam"]["q2"]["options"],
            correct_idx=content_1_7["exam"]["q2"]["options"].index(content_1_7["exam"]["q2"]["correct_opt"]),
            solution_text_dict=content_1_7["exam"]["q2"]["solution"],
            success_msg_dict={"de": "Korrekt", "en": "Correct"},
            error_msg_dict={"de": "Falsch", "en": "Incorrect"},
            model=model,
            ai_context="Independence logic",
            hint_text_dict=content_1_7["exam"]["q2"]["hint"],
            course_id="vwl", topic_id="1", subtopic_id="1.7", question_id="1_7_q2_narrative"
        )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # ===== EXPERIMENT 2: INDEPENDENCE BALANCE CHALLENGE =====
    st.markdown("---")
    st.markdown(f"""
        <div class="icon-header">
            {render_icon('target', size=24)}
            <h3 style="margin:0;">{t(content_1_7['independence']['mission']['title'])}</h3>
        </div>
    """, unsafe_allow_html=True)
    
    # --- STATE INITIALIZATION ---
    if "shapes_1_7_balance" not in st.session_state:
        # Initial dependent state: mostly blue squares, few circles, only 1 red circle
        st.session_state.shapes_1_7_balance = [
            {"color": "blue", "shape": "square"},
            {"color": "blue", "shape": "square"},
            {"color": "blue", "shape": "square"},
            {"color": "blue", "shape": "square"},
            {"color": "blue", "shape": "square"},
            {"color": "blue", "shape": "square"},
            {"color": "blue", "shape": "square"},
            {"color": "blue", "shape": "square"},
            {"color": "blue", "shape": "circle"},
            {"color": "blue", "shape": "circle"},
            {"color": "blue", "shape": "circle"},
            {"color": "red", "shape": "circle"},
        ]

    shapes = st.session_state.shapes_1_7_balance

    # --- CALCULATE PROBABILITIES ---
    total = len(shapes)
    red_count = sum(1 for s in shapes if s["color"] == "red")
    circle_count = sum(1 for s in shapes if s["shape"] == "circle")
    red_circle_count = sum(1 for s in shapes if s["color"] == "red" and s["shape"] == "circle")

    P_A = red_count / total if total > 0 else 0
    P_B = circle_count / total if total > 0 else 0
    P_A_given_B = red_circle_count / circle_count if circle_count > 0 else 0
    P_A_and_B = red_circle_count / total if total > 0 else 0

    # Independence check
    is_independent = math.isclose(P_A_and_B, P_A * P_B, rel_tol=0.01) if P_B > 0 else False

    # --- THE INTERACTIVE SANDBOX ---
    with st.container(border=True):
        # 1. NARRATIVE HUD (AGGRESSIVE GUIDANCE)
        if is_independent:
            st.balloons()
            st.success(f"🏆 **{t({'de': 'Unabhängigkeit Erreicht!', 'en': 'Independence Achieved!'})}** {t({'de': 'Die Wahrscheinlichkeit für Rot ist in beiden Welten gleich.', 'en': 'The chance of Red is the same in both worlds.'})}")
        else:
            st.warning(f"⚖️ **{t({'de': 'Die Waage steht schief:', 'en': 'The scale is unbalanced:'})}** {t({'de': 'Wissen über Kreise verändert deine Einschätzung über Rot.', 'en': 'Information about Circles changes your estimate of Red.'})}")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # METRICS ROW
        met_col1, met_col2 = st.columns(2)
        with met_col1:
            st.metric(
                label=f"P(A) - {t(content_1_7['independence']['metrics']['p_a_label'])}",
                value=f"{P_A:.2f}"
            )
        with met_col2:
            st.metric(
                label=f"P(A|B) - {t(content_1_7['independence']['metrics']['p_a_given_b_label'])}",
                value=f"{P_A_given_B:.2f}" if circle_count > 0 else "N/A"
            )
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # INTERACTIVE GRID (4x3)
        x_coords = []
        y_coords = []
        colors = []
        symbols = []
        
        for idx, shape in enumerate(shapes):
            x = idx % 4
            y = 2 - (idx // 4)  # Reverse y for top-to-bottom
            x_coords.append(x)
            y_coords.append(y)
            
            # Color mapping
            color_map = {"red": "#FF4B4B", "blue": "#1E88E5"}
            colors.append(color_map[shape["color"]])
            
            # Symbol mapping
            symbol_map = {"circle": "circle", "square": "square"}
            symbols.append(symbol_map[shape["shape"]])
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=x_coords, y=y_coords, mode='markers',
            marker=dict(size=60, color=colors, symbol=symbols, line=dict(width=2, color="#333")),
            hoverinfo='none',
            ids=list(range(len(shapes)))
        ))
        
        fig.update_layout(
            xaxis=dict(visible=False, fixedrange=True, range=[-0.5, 3.5]),
            yaxis=dict(visible=False, fixedrange=True, range=[-0.5, 2.5], scaleanchor="x", scaleratio=1),
            margin=dict(l=10, r=10, t=10, b=10),
            height=300,
            clickmode='event+select',
            dragmode=False,
            plot_bgcolor='rgba(0,0,0,0)'
        )
        
        event = st.plotly_chart(fig, on_select="rerun", selection_mode="points", use_container_width=True, key="balance_chart_1_7", config={'displayModeBar': False})
        
        # HANDLE CLICK - Cycle through states
        if event and event.get("selection") and event["selection"].get("points"):
            clicked_idx = event["selection"]["points"][0]["point_index"]
            current_shape = shapes[clicked_idx]
            
            # Cycle logic: blue_square -> red_square -> blue_circle -> red_circle -> blue_square
            if current_shape["color"] == "blue" and current_shape["shape"] == "square":
                shapes[clicked_idx] = {"color": "red", "shape": "square"}
            elif current_shape["color"] == "red" and current_shape["shape"] == "square":
                shapes[clicked_idx] = {"color": "blue", "shape": "circle"}
            elif current_shape["color"] == "blue" and current_shape["shape"] == "circle":
                shapes[clicked_idx] = {"color": "red", "shape": "circle"}
            elif current_shape["color"] == "red" and current_shape["shape"] == "circle":
                shapes[clicked_idx] = {"color": "blue", "shape": "square"}
            
            st.rerun()
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # INDEPENDENCE STATUS
        if is_independent:
            st.success(f"{t(content_1_7['independence']['metrics']['status_independent'])}")
            st.markdown(t(content_1_7["independence"]["feedback"]["independent"]))
        else:
            st.warning(f"{t(content_1_7['independence']['metrics']['status_dependent'])}")
            st.markdown(t(content_1_7["independence"]["feedback"]["dependent"]))
    
    # --- MASTERY CARD (Full Width) ---
    if is_independent:
        st.markdown("<br>", unsafe_allow_html=True)
        
        with st.container(border=True):
            st.markdown(f"### {t(content_1_7['independence']['mastery']['title'])}")
            
            # Column split for visual clarity
            col_a, col_b = st.columns([1, 1])
            
            with col_a:
                st.markdown(f"**{t(content_1_7['independence']['mastery']['intuition_title'])}**")
                for item in t(content_1_7["independence"]["mastery"]["check_items"]):
                    st.markdown(f"- {item}")
            
            with col_b:
                st.markdown(f"**{t(content_1_7['independence']['mastery']['math_title'])}**")
                st.latex(fr"P(A \cap B) = {P_A:.2f} \times {P_B:.2f} = {P_A * P_B:.2f}")
                st.info(t(content_1_7["independence"]["mastery"]["translation"]))

            st.divider()
            
            st.markdown(f"**{t(content_1_7['independence']['mastery']['big_picture_title'])}**")
            st.markdown(t(content_1_7["independence"]["mastery"]["comparison_intro"]))
            
            # Side-by-side comparison
            comp_col1, comp_col2 = st.columns(2)
            with comp_col1:
                st.markdown(f"**P(A):**")
                st.latex(fr"P(A) = {P_A:.2f}")
            with comp_col2:
                st.markdown(f"**P(A|B):**")
                st.latex(fr"P(A|B) = {P_A_given_B:.2f}")
            
            st.markdown("<br>", unsafe_allow_html=True)
            st.warning(t(content_1_7["independence"]["mastery"]["conclusion"]))
        
        # Progress Tracking
        from utils.progress_tracker import update_local_progress, track_question_answer
        user = st.session_state.get("user")
        if user:
            update_local_progress("1", "1.7", "1_7_balance_mission", True)
            track_question_answer(user["localId"], "vwl", "1", "1.7", "1_7_balance_mission", True)
    
    # Reset button
    if st.button("Reset Grid"):
        st.session_state.shapes_1_7_balance = [
            {"color": "blue", "shape": "square"},
            {"color": "blue", "shape": "square"},
            {"color": "blue", "shape": "square"},
            {"color": "blue", "shape": "square"},
            {"color": "blue", "shape": "square"},
            {"color": "blue", "shape": "square"},
            {"color": "blue", "shape": "square"},
            {"color": "blue", "shape": "square"},
            {"color": "blue", "shape": "circle"},
            {"color": "blue", "shape": "circle"},
            {"color": "blue", "shape": "circle"},
            {"color": "red", "shape": "circle"},
        ]
        st.rerun()