import streamlit as st
import plotly.graph_objects as go
import numpy as np
import random
from views.styles import render_icon
from utils.localization import t
from utils.quiz_helper import render_mcq

# --- DATA STRUCTURE ---
content_1_7 = {
    "title": {"de": "1.7 Bedingte Wahrscheinlichkeit", "en": "1.7 Conditional Probability"},
    
    # STORY: Plain language problem framing
    "story": {
        "problem": {
            "de": """
Sie analysieren einen Datensatz mit Formen.

Ihr Chef fragt: **"Von allen KREISEN, wie viele Prozent sind ROT?"**
            """,
            "en": """
You're analyzing a dataset of shapes.

Your boss asks: **"Out of all the CIRCLES, what percentage are RED?"**
            """
        },
        "notation_intro": {
            "de": r"In mathematischer Notation wird dies als $P(\text{Rot}|\text{Kreis})$ oder $P(A|B)$ geschrieben.",
            "en": r"In math notation, this is written as $P(\text{Red}|\text{Circle})$ or $P(A|B)$."
        },
        "symbol_meaning": {
            "de": r"Das Symbol $|$ bedeutet **\"gegeben\"** oder **\"innerhalb der Welt von\"**.",
            "en": r"The $|$ symbol means **\"given\"** or **\"within the world of\"**."
        },
        "task": {
            "de": "**Ihre Aufgabe:** Finden Sie diesen Prozentsatz durch Filtern und Zählen.",
            "en": "**Your task:** Find this percentage by filtering and counting."
        }
    },
    
    # FEEDBACK: After each step
    "feedback": {
        "filter_success": {
            "title": {
                "de": "Sie haben die Daten gefiltert!",
                "en": "You filtered the data!"
            },
            "intuition": {
                "de": r"**Intuition:** Sie haben gerade alle Quadrate entfernt. Jetzt sehen Sie nur noch das \"Kreis-Universum\" $B$.",
                "en": r"**Intuition:** You just removed all the squares. Now you're only looking at the \"Circle Universe\" $B$."
            },
            "notation": {
                "de": r"**In der Notation:** Der Teil $|B$ bedeutet: Wir befinden uns jetzt in Welt $B$",
                "en": r"**In notation:** The $|B$ part means we're now in world $B$"
            },
            "next": {
                "de": "**Nächster Schritt:** Zählen Sie, was Sie sehen.",
                "en": "**Next step:** Count what you see."
            }
        },
        "success": {
            "title": {
                "de": "Perfekt!",
                "en": "Perfect!"
            },
            "check_title": {
                "de": "**Intuitions-Check:**",
                "en": "**Intuition Check:**"
            },
            "check_items": {
                "de": [
                    "Sie haben **6 Kreise** insgesamt gefunden (Ihr neues Universum)",
                    "**3 davon** sind rot (Ihr Ziel innerhalb dieses Universums)",
                    r"$\frac{3}{6} = 0.50 = 50\%$"
                ],
                "en": [
                    "You found **6 circles** total (your new universe)",
                    "**3 of them** are red (your target within that universe)",
                    r"$\frac{3}{6} = 0.50 = 50\%$"
                ]
            },
            "calculated_title": {
                "de": "**Was Sie gerade berechnet haben:**",
                "en": "**What you just calculated:**"
            },
            "calculated_formula": r"P(A|B) = \frac{3}{6} = 0.50",
            "translation": {
                "de": r"**Übersetzung:** \"Von allen Kreisen ist die Hälfte rot.\"",
                "en": r"**Translation:** \"Out of all circles, half are red.\""
            },
            "big_picture_title": {
                "de": "**Das große Bild:**",
                "en": "**The bigger picture:**"
            },
            "big_picture_items": {
                "de": [
                    r"Ohne Filter: $P(A) = \frac{3}{9} = 0.33$ (von allen Formen)",
                    r"Mit Filter: $P(A|B) = \frac{3}{6} = 0.50$ (von allen Kreisen)"
                ],
                "en": [
                    r"Without filter: $P(A) = \frac{3}{9} = 0.33$ (of all shapes)",
                    r"With filter: $P(A|B) = \frac{3}{6} = 0.50$ (of all circles)"
                ]
            },
            "conclusion": {
                "de": "Die bedingte Wahrscheinlichkeit ändert sich, weil Sie Ihr Universum eingeschränkt haben!",
                "en": "The conditional probability changes because you narrowed your universe!"
            }
        }
    },
    
    "interactive": {
        "controls": {
            "all": {"de": "Alle Formen", "en": "All Shapes"},
            "filter": {"de": "Nur Kreise (B)", "en": "Circles Only (B)"}
        },
        "inputs": {
            "denom_label": {"de": "Wie viele Kreise insgesamt?", "en": "How many circles total?"},
            "num_label": {"de": "Wie viele sind rot?", "en": "How many are red?"},
        },
        "guidance": {
            "initial": {
                "de": "Wählen Sie 'Nur Kreise' um zu starten.",
                "en": "Select 'Circles Only' to start."
            }
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
            "question": {"de": "**Gegeben:** $\mathbb{P}(A)=\\frac{1}{2}$, $\mathbb{P}(B)=\\frac{2}{3}$ und $\mathbb{P}(A\\cap B)=\\frac{1}{4}$.\n\n**Gesucht:** $\mathbb{P}(A|\\overline{B})$.  ", "en": "**Given:** $\mathbb{P}(A)=\\frac{1}{2}$, $\mathbb{P}(B)=\\frac{2}{3}$ and $\mathbb{P}(A\\cap B)=\\frac{1}{4}$.\n\n**Find:** $\mathbb{P}(A|\\overline{B})$."},
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
            "options": {
                "de": [
                    "Unabhängig und Disjunkt",
                    "Abhängig und Disjunkt",
                    "Unabhängig und Nicht-Disjunkt",
                    "Abhängig und Nicht-Disjunkt"
                ],
                "en": [
                    "Independent & Disjoint",
                    "Dependent & Disjoint",
                    "Independent & Joint",
                    "Dependent & Joint"
                ]
            },
            "correct_idx": 1,
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
    }
}

def render_subtopic_1_7(model):
    """1.7 Visual Sanitation Edition"""
    
    # 1. CSS: Force Perfect Pill Centering + Square Grid + Center Metrics
    st.markdown("""
    <style>
        /* Force Pills to Center */
        div[role="radiogroup"] {
            justify-content: center !important;
            width: 100% !important;
        }
        
        /* Center Metrics */
        div[data-testid="metric-container"] {
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
        }
    </style>
    """, unsafe_allow_html=True)

    st.header(t(content_1_7["title"]))
    st.markdown("---")
    
    # --- TOP ROW: THEORY ---
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

    st.markdown("<br><br>", unsafe_allow_html=True)

    # --- INIT STATE ---
    pills_key = "filter_1_7_clean"
    opt_all = t(content_1_7["interactive"]["controls"]["all"])
    opt_filter = t(content_1_7["interactive"]["controls"]["filter"])
    
    # Default state
    if pills_key not in st.session_state:
        st.session_state[pills_key] = opt_all
    
    selection = st.session_state[pills_key]
    is_filtered = (selection == opt_filter)

    # --- THE MONOLITH ---
    with st.container(border=True):
        
        # 1. PROBLEM STATEMENT (Full width - story-driven opening)
        # Combine all text into one block for full-width rendering
        problem_text = f"""
{t(content_1_7["story"]["problem"])}

{t(content_1_7["story"]["notation_intro"])}

{t(content_1_7["story"]["symbol_meaning"])}

{t(content_1_7["story"]["task"])}
        """
        st.markdown(problem_text)
        
        st.markdown("---")
        
        # 2. SCOREBOARD (Full Width - Use 2 columns for better spacing)
        correct_denom = 6 # Total Circles
        correct_num = 3   # Red Circles
        total_n = 9
        current_n = correct_denom if is_filtered else total_n
        
        # Full width columns
        c1, c2 = st.columns(2)
        with c1:
            st.metric(
                t({"de": "Ziel (Rote Kreise)", "en": "Target (Red Circles)"}), 
                f"{correct_num}"
            )
        with c2:
            # Renamed from "Universe Size" to "Total Shapes (N)"
            st.metric(
                t({"de": "Gesamte Formen (N)", "en": "Total Shapes (N)"}), 
                f"{current_n}", 
                delta=t({"de": "Gefiltert", "en": "Filtered"}) if is_filtered else t({"de": "Gesamt", "en": "Full"})
            )

        st.divider()

        # 3. THE STAGE (Perfect Square Chart + Centered Pills)
        # Use columns to center the chart physically
        left, center, right = st.columns([0.2, 3, 0.2])
        
        with center:
            # CHART GENERATION (FORCE SQUARE ASPECT RATIO)
            fig = go.Figure()
            c_target, c_univ, c_noise = "#FF4B4B", "#1E88E5", "#E0E0E0"
            
            # 3x3 Grid Data
            points = [
                {"x": 0, "y": 2, "c": c_target, "s": "circle", "is_sq": False}, 
                {"x": 1, "y": 2, "c": c_univ, "s": "circle", "is_sq": False}, 
                {"x": 2, "y": 2, "c": c_univ, "s": "circle", "is_sq": False}, 
                
                {"x": 0, "y": 1, "c": c_noise, "s": "square", "is_sq": True},   
                {"x": 1, "y": 1, "c": c_target, "s": "circle", "is_sq": False}, 
                {"x": 2, "y": 1, "c": c_univ, "s": "circle", "is_sq": False},   
                
                {"x": 0, "y": 0, "c": c_target, "s": "circle", "is_sq": False}, 
                {"x": 1, "y": 0, "c": c_noise, "s": "square", "is_sq": True},   
                {"x": 2, "y": 0, "c": c_noise, "s": "square", "is_sq": True},   
            ]
            
            x_vals, y_vals, colors, opacities, symbols = [], [], [], [], []
            for p in points:
                x_vals.append(p["x"])
                y_vals.append(p["y"])
                colors.append(p["c"])
                symbols.append(p["s"])
                # Ghost Logic
                if is_filtered and p["is_sq"]:
                    opacities.append(0.05)
                else:
                    opacities.append(1.0)

            fig.add_trace(go.Scatter(
                x=x_vals, y=y_vals, mode='markers',
                marker=dict(size=30, color=colors, symbol=symbols, opacity=opacities),
                hoverinfo='none'
            ))
            
            # FORCE SQUARE ASPECT RATIO (Critical Fix)
            fig.update_layout(
                xaxis=dict(
                    visible=False, 
                    fixedrange=True, 
                    range=[-0.5, 2.5],
                    constrain='domain'  # Critical for square
                ),
                yaxis=dict(
                    visible=False, 
                    fixedrange=True, 
                    range=[-0.5, 2.5],
                    scaleanchor="x",   # Lock to X axis
                    scaleratio=1        # 1:1 square ratio
                ),
                margin=dict(l=20, r=20, t=20, b=20),
                height=300,
                dragmode=False,
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
            )
            
            st.plotly_chart(fig, use_container_width=True, config={'staticPlot': False, 'displayModeBar': False})
            
            # CENTERED PILLS
            st.markdown("<br>", unsafe_allow_html=True)
            st.pills(
                "", 
                options=[opt_all, opt_filter], 
                key=pills_key, 
                label_visibility="collapsed"
            )

        # 4. WORKSPACE (Sliders for instant feedback + Formula)
        st.divider()

        if is_filtered:
            # FEEDBACK: Filter Success (No emojis, proper LaTeX)
            st.success(t(content_1_7["feedback"]["filter_success"]["title"]))
            st.markdown(t(content_1_7["feedback"]["filter_success"]["intuition"]))
            st.markdown(t(content_1_7["feedback"]["filter_success"]["notation"]))
            st.markdown(t(content_1_7["feedback"]["filter_success"]["next"]))
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            # SLIDERS (instant feedback instead of number inputs)
            i1, i2 = st.columns(2)
            with i1:
                denom_in = st.slider(
                    t(content_1_7["interactive"]["inputs"]["denom_label"]), 
                    min_value=0, 
                    max_value=9, 
                    value=0,
                    step=1, 
                    key="slider_den"
                )
            with i2:
                num_in = st.slider(
                    t(content_1_7["interactive"]["inputs"]["num_label"]), 
                    min_value=0, 
                    max_value=9, 
                    value=0,
                    step=1, 
                    key="slider_num"
                )

            is_correct = (denom_in == correct_denom and num_in == correct_num)
            
            st.markdown("<br>", unsafe_allow_html=True)

            # Dynamic Formula Area (Color-coded, always visible)
            disp_num = f"\\color{{#FF4B4B}}{{{num_in}}}" if num_in > 0 else "?"
            disp_denom = f"\\color{{#1E88E5}}{{{denom_in}}}" if denom_in > 0 else "?"
            
            # Calc result or ?
            if denom_in > 0:
                res_val = f"{num_in/denom_in:.2f}"
            else:
                res_val = "?"

            formula_latex = fr"P(A|B) = \frac{{\text{{\color{{#FF4B4B}}{{\text{{Red Circles}}}}}}}}{{\text{{\color{{#1E88E5}}{{\text{{Total Circles}}}}}}}} = \frac{{{disp_num}}}{{{disp_denom}}} = {res_val}"
            
            st.latex(formula_latex)
            
            if is_correct:
                st.markdown("<br>", unsafe_allow_html=True)
                st.success(t(content_1_7["feedback"]["success"]["title"]))
                
                # Intuition Check
                st.markdown(t(content_1_7["feedback"]["success"]["check_title"]))
                for item in t(content_1_7["feedback"]["success"]["check_items"]):
                    st.markdown(f"- {item}")
                
                st.markdown("<br>", unsafe_allow_html=True)
                
                # What you calculated
                st.markdown(t(content_1_7["feedback"]["success"]["calculated_title"]))
                st.latex(content_1_7["feedback"]["success"]["calculated_formula"])
                st.markdown(t(content_1_7["feedback"]["success"]["translation"]))
                
                st.markdown("<br>", unsafe_allow_html=True)
                
                # The bigger picture
                st.markdown(t(content_1_7["feedback"]["success"]["big_picture_title"]))
                for item in t(content_1_7["feedback"]["success"]["big_picture_items"]):
                    st.markdown(f"- {item}")
                
                st.markdown("<br>", unsafe_allow_html=True)
                st.markdown(t(content_1_7["feedback"]["success"]["conclusion"]))
                
                # Track Progress
                from utils.progress_tracker import update_local_progress, track_question_answer
                user = st.session_state.get("user")
                if user:
                    update_local_progress("1", "1.7", "1_7_analyst_mission_clean", True)
                    track_question_answer(user["localId"], "vwl", "1", "1.7", "1_7_analyst_mission_clean", True)
        
        else:
            # Base state guidance
            st.info(t(content_1_7["interactive"]["guidance"]["initial"]))
            st.markdown("<br>", unsafe_allow_html=True)
            st.latex(r"P(A) = \frac{\text{Red}}{\text{Total Universe}}")

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
            key_suffix="1_7_q1_clean",
            question_text=t(content_1_7["exam"]["q1"]["question"]),
            options=content_1_7["exam"]["q1"]["options"],
            correct_idx=content_1_7["exam"]["q1"]["options"].index(content_1_7["exam"]["q1"]["correct_opt"]),
            solution_text_dict=content_1_7["exam"]["q1"]["solution"],
            success_msg_dict={"de": "Korrekt", "en": "Correct"},
            error_msg_dict={"de": "Falsch", "en": "Incorrect"},
            model=model,
            ai_context="Conditional probability calculations",  
            hint_text_dict=content_1_7["exam"]["q1"]["hint"],
            course_id="vwl", topic_id="1", subtopic_id="1.7", question_id="1_7_q1_clean"
        )
        
    # Q2
    st.markdown("<br>", unsafe_allow_html=True)
    with st.container(border=True):
        st.markdown(f"**{t(content_1_7['exam']['q2']['title'])}**")
        render_mcq(
            key_suffix="1_7_q2_clean",
            question_text=t(content_1_7["exam"]["q2"]["question"]),
            options=t(content_1_7["exam"]["q2"]["options"]),
            correct_idx=content_1_7["exam"]["q2"]["correct_idx"],
            solution_text_dict=content_1_7["exam"]["q2"]["solution"],
            success_msg_dict={"de": "Korrekt", "en": "Correct"},
            error_msg_dict={"de": "Falsch", "en": "Incorrect"},
            model=model,
            ai_context="Independence vs Disjoint logic check", 
            hint_text_dict=content_1_7["exam"]["q2"]["hint"],
            course_id="vwl", topic_id="1", subtopic_id="1.7", question_id="1_7_q2_clean"
        )
