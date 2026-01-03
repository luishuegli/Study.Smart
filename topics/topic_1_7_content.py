import streamlit as st
import plotly.graph_objects as go
import math
from views.styles import render_icon, inject_equal_height_css
from utils.localization import t
from utils.quiz_helper import render_mcq
from data.exam_questions import get_question

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
        "q1": {"title": {"de": "Prüfungstraining: HS2024 (MC 3)", "en": "Exam Practice: HS2024 (MC 3)"}},
        "q2": {"title": {"de": "Logik-Check: Unabhängigkeit (MC 5)", "en": "Logic Check: Independence (MC 5)"}}
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
    },
    
    # --- FRAG DICH (Ask Yourself) ---
    "frag_dich": {
        "header": {"de": "Frag dich: Bedingt oder Unabhängig?", "en": "Ask yourself: Conditional or Independent?"},
        "questions": [
            {"de": "Verändert <strong>Wissen über B</strong> meine Einschätzung von A?", "en": "Does <strong>knowing B</strong> change my estimate of A?"},
            {"de": "Ist $P(A|B) = P(A)$? Dann sind A und B <strong>unabhängig</strong>.", "en": "Is $P(A|B) = P(A)$? Then A and B are <strong>independent</strong>."},
            {"de": "Wird das <strong>Universum kleiner</strong> nach der Bedingung?", "en": "Does the <strong>universe shrink</strong> after the condition?"},
            {"de": "Frage ich nach $P(A \\cap B)$ (Schnitt) oder $P(A|B)$ (gegeben)?", "en": "Am I asking for $P(A \\cap B)$ (intersection) or $P(A|B)$ (given)?"}
        ],
        "conclusion": {"de": "Strich = Filter → kleines Universum. Kein Strich = Multiplikation im ganzen Universum.", "en": "Bar = Filter → smaller universe. No bar = multiplication in the whole universe."}
    },
    
    # --- EXAM ESSENTIALS ---
    "exam_essentials": {
        "trap": {
            "de": "$P(A \\cap B)$ mit $P(A|B)$ verwechseln! Der Strich $|$ bedeutet 'gegeben' — du rechnest in einem <strong>kleineren Universum</strong>.",
            "en": "Confusing $P(A \\cap B)$ with $P(A|B)$! The bar $|$ means 'given' — you calculate in a <strong>smaller universe</strong>."
        },
        "trap_rule": {
            "de": "Faustregel: Strich = Teilen durch $P(B)$. Kein Strich = Multiplizieren.",
            "en": "Rule of thumb: Bar = divide by $P(B)$. No bar = multiply."
        },
        "tips": [
            {
                "tip": {"de": "Unabhängigkeit prüfen: $P(A \\cap B) = P(A) \\cdot P(B)$", "en": "Check independence: $P(A \\cap B) = P(A) \\cdot P(B)$"},
                "why": {"de": "Wenn diese Gleichung gilt, sind A und B unabhängig. Dann ist $P(A|B) = P(A)$.", "en": "If this equation holds, A and B are independent. Then $P(A|B) = P(A)$."}
            },
            {
                "tip": {"de": "Bayes umstellen: $P(A|B) = \\frac{P(B|A) \\cdot P(A)}{P(B)}$", "en": "Rearrange Bayes: $P(A|B) = \\frac{P(B|A) \\cdot P(A)}{P(B)}$"},
                "why": {"de": "Nützlich wenn du $P(A|B)$ brauchst aber nur $P(B|A)$ gegeben ist.", "en": "Useful when you need $P(A|B)$ but only $P(B|A)$ is given."}
            },
            {
                "tip": {"de": "Bei 'gegeben' immer: Zähler = Schnitt, Nenner = Bedingung", "en": "For 'given' always: Numerator = intersection, Denominator = condition"},
                "why": {"de": "Die Formel $P(A|B) = \\frac{P(A \\cap B)}{P(B)}$ direkt anwenden.", "en": "Apply the formula $P(A|B) = \\frac{P(A \\cap B)}{P(B)}$ directly."}
            }
        ]
    }
}

def render_subtopic_1_7(model):
    """1.7 Narrative & Notation Bridge"""
    inject_equal_height_css()
    
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
    st.markdown("---")

    # --- THEORY SECTION: Using Layout B (Comparison) ---
    from utils.layouts import render_comparison
    render_comparison(
        title={"de": "Zwei Konzepte, ein Universum", "en": "Two Concepts, One Universe"},
        intuition={
            "de": "Dein Chef fragt: 'Wie wahrscheinlich ist ROT, wenn ich dir sage, dass es ein KREIS ist?' Das ist bedingte Wahrscheinlichkeit — du filterst das Universum BEVOR du zählst.",
            "en": "Your boss asks: 'How likely is RED, if I tell you it's a CIRCLE?' That's conditional probability — you filter the universe BEFORE you count."
        },
        left={
            "title": {"de": "Bedingte Wahrscheinlichkeit", "en": "Conditional Probability"},
            "intuition": {"de": "Die Wsk von A, GEGEBEN dass B passiert ist.", "en": "The probability of A, GIVEN that B happened."},
            "formula": r"P(A|B) = \frac{P(A \cap B)}{P(B)}",
            "variables": [
                {"symbol": "A|B", "name": {"de": "A gegeben B", "en": "A given B"}, "description": {"de": "der Strich = Filter", "en": "the bar = filter"}},
                {"symbol": r"P(A \cap B)", "name": {"de": "Schnitt", "en": "Intersection"}, "description": {"de": "beides passiert", "en": "both happen"}},
                {"symbol": "P(B)", "name": {"de": "Bedingung", "en": "Condition"}, "description": {"de": "dein neues Universum", "en": "your new universe"}}
            ],
            "insight": {"de": "Der Nenner P(B) schrumpft dein Universum.", "en": "The denominator P(B) shrinks your universe."}
        },
        right={
            "title": {"de": "Unabhängigkeit", "en": "Independence"},
            "intuition": {"de": "Wissen über B sagt NICHTS über A.", "en": "Knowing B tells you NOTHING about A."},
            "formula": r"P(A \cap B) = P(A) \cdot P(B)",
            "variables": [
                {"symbol": r"P(A \cap B)", "name": {"de": "Schnitt", "en": "Intersection"}, "description": {"de": "einfach multiplizieren!", "en": "just multiply!"}},
                {"symbol": "P(A)", "name": {"de": "Wsk von A", "en": "Prob of A"}, "description": {"de": "unverändert", "en": "unchanged"}},
                {"symbol": "P(B)", "name": {"de": "Wsk von B", "en": "Prob of B"}, "description": {"de": "unverändert", "en": "unchanged"}}
            ],
            "insight": {"de": "Wenn unabhängig: P(A|B) = P(A). Der Filter ändert nichts!", "en": "If independent: P(A|B) = P(A). The filter changes nothing!"}
        },
        key_difference={
            "de": "<strong>Bedingt:</strong> Filter verändert die Wsk (P(A|B) ≠ P(A)). <strong>Unabhängig:</strong> Filter ändert nichts (P(A|B) = P(A)).",
            "en": "<strong>Conditional:</strong> Filter changes the prob (P(A|B) ≠ P(A)). <strong>Independent:</strong> Filter changes nothing (P(A|B) = P(A))."
        }
    )
    
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
    st.markdown("### Experiment")
    
    # The Interactive Experiment
    with st.container(border=True):
        # 1. NARRATIVE HUD (AGGRESSIVE GUIDANCE)
        if current_noise == 3:
            st.markdown(f"""
<div style="background: #f4f4f5; border-left: 4px solid #71717a; padding: 12px 16px; border-radius: 8px; color: #18181b;">
    <strong>{t({'de': 'Schritt 1:', 'en': 'Step 1:'})}</strong> {t({'de': 'Klicke auf die Quadrate, um sie aus dem Universum zu werfen.', 'en': 'Click on the squares to kick them out of the universe.'})}
</div>
""", unsafe_allow_html=True)
        elif current_noise > 0:
            st.success(f"**{t({'de': 'Schritt 2:', 'en': 'Step 2:'})}** {t({'de': 'Gut! Das Universum schrumpft. Entferne alle Quadrate.', 'en': 'Good! The universe is shrinking. Remove all squares.'})}")
        else:
            st.balloons()
            st.success(f"**{t({'de': 'Filter Komplett!', 'en': 'Filter Complete!'})}** {t({'de': 'In der Kreis-Welt ist Rot nun viel wahrscheinlicher.', 'en': 'In the Circle-World, Red is now much more likely.'})}")
        
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
                clickmode='event+select',
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
                    st.toast("Keep the Circles! We need them for the condition.", icon="info")

        # C. The "Live Math" Panel (Right Side) - Simplified
        with col_math:
            st.markdown(f"**{t({'de': 'Live-Notation', 'en': 'Live Notation'})}**")
            # Bilingual labels for formula
            label_red = t({"de": "Rot", "en": "Red"})
            label_circle = t({"de": "Kreis", "en": "Circle"})
            label_hit = t({"de": "Treffer", "en": "Hit"})
            label_universe = t({"de": "Universum", "en": "Universe"})
            st.latex(fr"P(\text{{{label_red}}} \mid \text{{{label_circle}}}) = \frac{{\text{{\color{{#FF4B4B}}{{{label_hit}}}}}}}{{\text{{\color{{#1E88E5}}{{{label_universe}}}}}}}")
            
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown(f"**{t({'de': 'Aktueller Status:', 'en': 'Current Status:'})}**")
            
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
        if user := st.session_state.get("user"):
            update_local_progress("1", "1.7", "1_7_narrative_mission", True)
            track_question_answer(user["localId"], "vwl", "1", "1.7", "1_7_narrative_mission", True)
            
    # Reset
    if st.button("Reset Story"):
        st.session_state.visible_indices_1_7 = list(range(9))
        st.rerun()

    # --- FRAG DICH (Ask Yourself) ---
    st.markdown("<br><br>", unsafe_allow_html=True)
    from utils.ask_yourself import render_ask_yourself
    render_ask_yourself(
        header=content_1_7["frag_dich"]["header"],
        questions=content_1_7["frag_dich"]["questions"],
        conclusion=content_1_7["frag_dich"]["conclusion"]
    )
    
    # --- EXAM ESSENTIALS ---
    st.markdown("<br><br>", unsafe_allow_html=True)
    from utils.exam_essentials import render_exam_essentials
    render_exam_essentials(
        trap=content_1_7["exam_essentials"]["trap"],
        trap_rule=content_1_7["exam_essentials"]["trap_rule"],
        tips=content_1_7["exam_essentials"]["tips"]
    )

    # --- EXAM SECTION ---
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown(f"### {t({'de': 'Prüfungstraining', 'en': 'Exam Practice'})}")
    
    # Q1
    with st.container(border=True):
        st.markdown(f"**{t(content_1_7['exam']['q1']['title'])}**")
        q1_data = get_question("1.7", "hs2024_mc3")
        
        # Handle bilingual options
        q1_opts = q1_data.get("options", [])
        if q1_opts and isinstance(q1_opts[0], dict) and ('de' in q1_opts[0] or 'en' in q1_opts[0]):
            q1_option_labels = [t(o) for o in q1_opts]
        else:
            q1_option_labels = q1_opts
        
        render_mcq(
            key_suffix="1_7_q1_narrative",
            question_text=t(q1_data["question"]),
            options=q1_option_labels,
            correct_idx=q1_data["correct_idx"],
            solution_text_dict=q1_data["solution"],
            success_msg_dict={"de": "Korrekt", "en": "Correct"},
            error_msg_dict={"de": "Falsch", "en": "Incorrect"},
            client=model,
            ai_context="Conditional probability", 
            hint_text_dict=q1_data.get("hint"),
            course_id="vwl", topic_id="1", subtopic_id="1.7", question_id="1_7_q1_narrative"
        )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Q2
    with st.container(border=True):
        st.markdown(f"**{t(content_1_7['exam']['q2']['title'])}**")
        q2_data = get_question("1.7", "uebung1_mc5")
        
        # Handle bilingual options
        q2_opts = q2_data.get("options", [])
        if q2_opts and isinstance(q2_opts[0], dict) and ('de' in q2_opts[0] or 'en' in q2_opts[0]):
            q2_option_labels = [t(o) for o in q2_opts]
        else:
            q2_option_labels = q2_opts
        
        render_mcq(
            key_suffix="1_7_q2_narrative",
            question_text=t(q2_data["question"]),
            options=q2_option_labels,
            correct_idx=q2_data["correct_idx"],
            solution_text_dict=q2_data["solution"],
            success_msg_dict={"de": "Korrekt", "en": "Correct"},
            error_msg_dict={"de": "Falsch", "en": "Incorrect"},
            client=model,
            ai_context="Independence logic",
            hint_text_dict=q2_data.get("hint"),
            course_id="vwl", topic_id="1", subtopic_id="1.7", question_id="1_7_q2_narrative"
        )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # ===== EXPERIMENT 2: INDEPENDENCE BALANCE CHALLENGE =====
    st.markdown("---")
    st.markdown(f"### {t(content_1_7['independence']['mission']['title'])}")
    
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
            st.success(f"**{t({'de': 'Unabhängigkeit Erreicht!', 'en': 'Independence Achieved!'})}** {t({'de': 'Die Wahrscheinlichkeit für Rot ist in beiden Welten gleich.', 'en': 'The chance of Red is the same in both worlds.'})}")
        else:
            st.warning(f"**{t({'de': 'Die Waage steht schief:', 'en': 'The scale is unbalanced:'})}** {t({'de': 'Wissen über Kreise verändert deine Einschätzung über Rot.', 'en': 'Information about Circles changes your estimate of Red.'})}")

        
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
        
        # METRICS ROW (Moved below grid per Rule 10.6)
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
        if user := st.session_state.get("user"):
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
    
    # --- EXAM WORKBENCH: Additional MCQ Questions ---
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown(f"### {t({'de': 'Prüfungstraining: Weitere Aufgaben', 'en': 'Exam Practice: Additional Problems'})}")
    
    def render_exam_q(label, q_id, key_suffix, source_caption, override_topic_id=None):
        q_data = get_question(override_topic_id or "1.7", q_id)
        if not q_data:
            st.warning(f"Question {q_id} not found in topic {override_topic_id or '1.7'}")
            return
        
        opts = q_data.get("options", [])
        # Handle both string lists and dict lists
        if opts and isinstance(opts[0], dict):
            option_labels = [t(o) for o in opts]
        else:
            option_labels = opts
        
        with st.container(border=True):
            st.caption(source_caption)
            render_mcq(
                key_suffix=key_suffix,
                question_text=t(q_data['question']),
                options=option_labels,
                correct_idx=q_data['correct_idx'],
                solution_text_dict=q_data['solution'],
                success_msg_dict={"de": "Richtig", "en": "Correct"},
                error_msg_dict={"de": "Falsch", "en": "Incorrect"},
                client=model,
                ai_context=f"Topic 1.7: Conditional Probability. Question: {q_id}",
                course_id="vwl", topic_id="1", subtopic_id="1.7", question_id=f"1_7_{label}"
            )
    
    render_exam_q("Q1", "test1_q1", "1_7_test1_q1", "Test 1, Frage 1")
    st.markdown("<br>", unsafe_allow_html=True)
    render_exam_q("Q2", "uebung1_mc5", "1_7_uebung1_mc5", "Übung 1, MC 5")
    st.markdown("<br>", unsafe_allow_html=True)
    render_exam_q("Q3", "uebung1_mc8", "1_7_uebung1_mc8", "Übung 1, MC 8")
    st.markdown("<br>", unsafe_allow_html=True)
    render_exam_q("Q4", "uebung1_mc1", "1_7_uebung1_mc1", "Übung 1, MC 1")
    st.markdown("<br>", unsafe_allow_html=True)
    render_exam_q("Q5", "uebung1_mc2", "1_7_uebung1_mc2", "Übung 1, MC 2")
    st.markdown("<br>", unsafe_allow_html=True)
    render_exam_q("Q6", "hs2023_mc1", "1_7_hs2023_mc1", "HS 2023, MC 1")
    st.markdown("<br>", unsafe_allow_html=True)
    # test3_q1 is actually located in Topic 1.2 (QUESTIONS_1_2)
    render_exam_q("Q7", "test3_q1", "1_7_test3_q1", "Test 3, Frage 1", override_topic_id="1.2")
    st.markdown("<br>", unsafe_allow_html=True)
    render_exam_q("Q8", "hs2024_mc5", "1_7_hs2024_mc5", "HS 2024, MC 5")