import streamlit as st
import plotly.graph_objects as go
from utils.localization import t
from views.styles import render_icon
from utils.ai_helper import render_ai_tutor
from utils.quiz_helper import render_mcq

# 1. THE CONTENT DICTIONARY (Rosetta Stone Protocol)
content_1_4 = {
    "title": {"de": "1.4 Axiomatik der Wahrscheinlichkeitstheorie", "en": "1.4 Axioms of Probability Theory"},
    "theory_header": {"de": "Die 3 Kolmogorow-Axiome", "en": "The 3 Kolmogorov Axioms"},
    "intro": {
        "de": "Damit Mathematik funktioniert, müssen diese drei 'Goldenen Regeln' immer gelten:",
        "en": "For mathematics to work, these three 'Golden Rules' must always apply:"
    },
    "axioms": {
        "1": {
            "title": {"de": "1. Nicht-Negativität", "en": "1. Non-Negativity"},
            "desc": {"de": "Eine Wahrscheinlichkeit ist nie kleiner als 0.", "en": "A probability is never less than 0."},
            "latex": r"P(A) \ge 0",
            "example": {
                "de": "$\\textbf{Beispiel: Würfel werfen}$\n- $P(\\text{Sechs}) = \\frac{1}{6} \\approx 0.167$ ✓\n- $P(\\text{Unmöglich}) = 0$ ✓\n- $P(\\text{Fehler}) = -0.2$ ✗",
                "en": "$\\textbf{Example: Rolling a die}$\n- $P(\\text{Six}) = \\frac{1}{6} \\approx 0.167$ ✓\n- $P(\\text{Impossible}) = 0$ ✓\n- $P(\\text{Error}) = -0.2$ ✗"
            }
        },
        "2": {
            "title": {"de": "2. Normierung", "en": "2. Normalization"},
            "desc": {"de": "Die Wahrscheinlichkeit des gesamten Ereignisraums ist 100%.", "en": "The probability of the entire sample space is 100%."},
            "latex": r"P(S) = 1",
            "example": {
                "de": "$\\textbf{Beispiel: Münzwurf}$\n- $P(\\text{Kopf}) + P(\\text{Zahl}) = 1$\n- $\\text{Bei fairer Münze: } 0.5 + 0.5 = 1$ ✓",
                "en": "$\\textbf{Example: Coin flip}$\n- $P(\\text{Heads}) + P(\\text{Tails}) = 1$\n- $\\text{Fair coin: } 0.5 + 0.5 = 1$ ✓"
            }
        },
        "3": {
            "title": {"de": "3. Additivität", "en": "3. Additivity"},
            "desc": {"de": "Für disjunkte (getrennte) Ereignisse addieren sich die Wahrscheinlichkeiten.", "en": "For disjoint (separate) events, probabilities add up."},
            "latex": r"P(A \cup B) = P(A) + P(B)",
            "example": {
                "de": "$\\textbf{Beispiel: Würfel}$\n- $A = \\{1,2\\}$, $B = \\{5,6\\}$ $\\text{(disjunkt)}$\n- $P(A \\cup B) = \\frac{2}{6} + \\frac{2}{6} = \\frac{4}{6}$ ✓",
                "en": "$\\textbf{Example: Die roll}$\n- $A = \\{1,2\\}$, $B = \\{5,6\\}$ $\\text{(disjoint)}$\n- $P(A \\cup B) = \\frac{2}{6} + \\frac{2}{6} = \\frac{4}{6}$ ✓"
            }
        }
    },
    "interactive": {
        "header": {"de": "Axiom-Labor: Vervollständige den Raum", "en": "Axiom Lab: Complete the Space"},
        "desc": {"de": "Diese Modelle sind unvollständig. Finde die fehlende Wahrscheinlichkeit, um Axiom 2 ($P(S)=1$) zu erfüllen.", "en": "These models are incomplete. Find the missing probability to satisfy Axiom 2 ($P(S)=1$)."},
        "success_msg": {"de": "Perfekt! Der Ereignisraum ist normiert.", "en": "Perfect! The sample space is normalized."},
        "error_overflow": {"de": "Zu hoch! Axiom 2 verletzt.", "en": "Too high! Axiom 2 violated."},
        "error_gap": {"de": "Lücke! Axiom 2 nicht erfüllt.", "en": "Gap! Axiom 2 not satisfied."}
    },
    "scenarios": {
        "market": {
            "mode": "normalization", # Axiom 2
            "name": {"de": "Marktanteile (Lücke)", "en": "Market Shares (Gap)"},
            "icon": "pie-chart",
            "desc": {"de": "Der Bericht ist unvollständig. Finde den Restwert.", "en": "The report is incomplete. Find the residual value."},
            "fixed": [
                {"label": {"de": "Apple", "en": "Apple"}, "value": 0.30, "color": "#000000"},
                {"label": {"de": "Samsung", "en": "Samsung"}, "value": 0.25, "color": "#007AFF"}
            ],
            "targets": [
                {"label": {"de": "Andere", "en": "Others"}, "color": "#8E8E93"}
            ],
            "initial": 0.0
        },
        "merger": {
            "mode": "additivity", # Axiom 3
            "name": {"de": "Die Fusion (Additivität)", "en": "The Merger (Additivity)"},
            "icon": "git-merge",
            "desc": {"de": "Company A (0.15) und B (0.20) fusionieren. Wie groß ist die neue Firma?", "en": "Company A (0.15) and B (0.20) merge. How big is the new entity?"},
            "fixed": [
                {"label": {"de": "Markt Rest", "en": "Market Rest"}, "value": 0.65, "color": "#E5E5EA"}
            ],
            "targets": [
                {"label": {"de": "New Giant (A+B)", "en": "New Giant (A+B)"}, "color": "#AF52DE"}
            ],
            "correct_val": 0.35, # 0.15 + 0.20
            "initial": 0.10
        },
        "glitch": {
            "mode": "negativity", # Axiom 1
            "name": {"de": "Daten-Fehler (Nicht-Negativität)", "en": "Data Glitch (Non-Negativity)"},
            "icon": "alert-triangle",
            "desc": {"de": "Ein Algorithmus hat einen negativen Wert berechnet (-0.15). Korrigiere das.", "en": "An algorithm calculated a negative value (-0.15). Correct this."},
            "fixed": [
                {"label": {"de": "Valid Data", "en": "Valid Data"}, "value": 0.80, "color": "#34C759"}
            ],
            "targets": [
                {"label": {"de": "Error Term", "en": "Error Term"}, "color": "#FF2D55"}
            ],
            "initial": -0.15,
            "min_val": -0.20
        }
    },
    "exam": {
        "title": {"de": "Logik-Check", "en": "Logic Check"},
        "source": "Selbst erstellt / Self-created",
        "question": {
            "de": r"Welche der folgenden Wahrscheinlichkeitszuweisungen ist ungültig? ($S = \{e_1, e_2, e_3\}$)",
            "en": r"Which of the following probability assignments is invalid? ($S = \{e_1, e_2, e_3\}$)"
        },
        "options": [
            {"id": "a", "text": "P(e₁)=0.3, P(e₂)=0.3, P(e₃)=0.4"},
            {"id": "b", "text": "P(e₁)=0.5, P(e₂)=0.5, P(e₃)=0"},
            {"id": "c", "text": "P(e₁)=0.6, P(e₂)=-0.1, P(e₃)=0.5"}
        ],
        "correct_id": "c",
        "solution": {
            "de": "**Richtig! (c)**<br>Wahrscheinlichkeiten können nicht negativ sein. Dies verletzt **Axiom 1**.",
            "en": "**Correct (c)**<br>Probabilities cannot be negative. This violates **Axiom 1**."
        }
    }
}

def get_scenario_donut(scenario_key, user_values):
    """Generate the Plotly donut chart for the scenario solver.
    """
    scenario = content_1_4["scenarios"][scenario_key]
    mode = scenario.get("mode", "normalization")
    
    # Calculate fixed sum
    fixed_sum = sum(item["value"] for item in scenario["fixed"])
    user_sum = sum(user_values)
    total_prob = fixed_sum + user_sum
    
    # Build data - start with fixed slices
    labels = [t(item["label"]) for item in scenario["fixed"]]
    values = [item["value"] for item in scenario["fixed"]]
    colors = [item.get("color", "#007AFF") for item in scenario["fixed"]]
    patterns = [""] * len(scenario["fixed"])
    
    # Add user slices
    for idx, target in enumerate(scenario["targets"]):
        val = user_values[idx]
        labels.append(t(target["label"]))
        
        # Handle Negative Values (Visual Hack)
        if val < 0:
            values.append(abs(val)) # Plot absolute size
            colors.append(target["color"]) 
            patterns.append("/") # Stripe pattern for error
        else:
            values.append(val)
            colors.append(target["color"])
            patterns.append("")
    
    fig = go.Figure(data=[go.Pie(
        labels=labels,
        values=values,
        hole=0.5,
        marker=dict(
            colors=colors,
            pattern=dict(shape=patterns),
            line=dict(color='#FFFFFF', width=2)
        ),
        textinfo='label+percent',
        textposition='outside', # Move labels outside the donut
        textfont=dict(family="Arial Black, sans-serif", size=14, color="black"),
        hoverinfo='label+value',
        sort=False
    )])
    
    # HUD LOGIC BY MODE
    center_text = ""
    center_color = "black"
    
    if mode == "normalization":
        center_text = f"<b>Σ = {total_prob:.2f}</b>"
        if abs(total_prob - 1.0) < 0.001:
            center_text = "<b>100%<br>VALID</b>"
            center_color = "#34C759"
        elif total_prob > 1.0:
            center_color = "#FF3B30"
            
    elif mode == "additivity":
        # Target is specific sum (A+B)
        # We assume the user is manipulating the target slices (New Giant)
        # Current logic: total_prob includes the "Fixed" background.
        # We want to show the SUM of the target parts? Or Total?
        # Let's show the specific Sum (P(A U B))?
        # Actually user manipulated "New Giant".
        # If correct, show Valid.
        correct_val = scenario.get("correct_val", 0.0)
        # Check if user value (user_sum) matches correct_val (ignoring fixed background)
        # Wait, for "merger", fixed is 0.65. Correct output is 0.35.
        if abs(user_sum - correct_val) < 0.001:
             center_text = f"<b>P(A∪B)<br>{user_sum:.2f}</b>"
             center_color = "#34C759"
        else:
             center_text = f"<b>P(A∪B)<br>{user_sum:.2f}</b>"
             center_color = "#AF52DE" # Purple
             
    elif mode == "negativity":
        # Show the error term
        center_text = f"<b>Error<br>{user_sum:.2f}</b>"
        if user_sum < 0:
             center_color = "#FF3B30"
        elif user_sum == 0:
             center_text = "<b>VALID<br>0.00</b>"
             center_color = "#34C759"
    
    fig.update_layout(
        annotations=[dict(
            text=center_text,
            x=0.5, y=0.5, font_size=18, font_color=center_color, showarrow=False
        )],
        showlegend=False,
        margin=dict(l=80, r=80, t=60, b=60), # Increased margins for outside labels
        height=350,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    
    return fig

def render_subtopic_1_4(model):
    # --- HEADER ---
    st.header(t(content_1_4["title"]))
    st.markdown("---")

    # --- UNIFIED CAPSULE ---
    with st.container(border=True):
        
        # 1. Full Width Intro
        st.markdown(f"### {render_icon('book-open')} {t(content_1_4['theory_header'])}", unsafe_allow_html=True)
        st.markdown(t(content_1_4["intro"]))
        st.markdown("<br>", unsafe_allow_html=True)

        # 2. Columns (Left: Axiom Cards, Right: Scenario Solver)
        col_theory, col_vis = st.columns([1, 1.2], gap="large")
        
        # --- LEFT: THE 3 AXIOM CARDS (STACKED) ---
        with col_theory:
            for idx, axiom_num in enumerate(["1", "2", "3"]):
                axiom = content_1_4["axioms"][axiom_num]
                
                with st.container(border=True):
                    st.markdown(f"**{t(axiom['title'])}**")
                    st.caption(t(axiom['desc']))
                    st.latex(axiom['latex'])
                    
                    # Add example
                    st.markdown("")
                    st.markdown(t(axiom['example']), unsafe_allow_html=True)

        # --- RIGHT: SCENARIO SOLVER ---
        with col_vis:
            # Force alignment
            st.markdown("""
                <style>
                h3 { margin-top: 0 !important; padding-top: 0 !important; }
                </style>
            """, unsafe_allow_html=True)
            
            st.markdown(f"### {render_icon('puzzle')} {t(content_1_4['interactive']['header'])}", unsafe_allow_html=True)
            st.caption(t(content_1_4["interactive"]["desc"]))
            
            # Scenario Selector
            scenario_options = {t(v["name"]): k for k, v in content_1_4["scenarios"].items()}
            
            selected_name = st.selectbox(
                "Scenario",
                options=list(scenario_options.keys()),
                label_visibility="collapsed",
                key="scenario_selector_1_4"
            )
            
            scenario_key = scenario_options[selected_name]
            scenario = content_1_4["scenarios"][scenario_key]
            mode = scenario.get("mode", "normalization")
            
            # Display "Fixed" probabilities
            st.markdown("**Given:**")
            fixed_sum = 0
            for item in scenario["fixed"]:
                st.markdown(f"- {t(item['label'])}: **{item['value']:.2f}**")
                fixed_sum += item["value"]
            
            st.markdown("")
            
            # Multiple Sliders for each target
            user_values = []
            
            # Dynamic range for sliders
            min_val = scenario.get("min_val", 0.0)
            
            for target in scenario["targets"]:
                target_label = t(target["label"])
                user_val = st.slider(
                    f"Set P({target_label})",
                    min_value=min_val, 
                    max_value=1.0,
                    value=scenario.get("initial", 0.0),
                    step=0.01,
                    key=f"slider_1_4_{scenario_key}_{target_label}"
                )
                user_values.append(user_val)
            
            # LOGIC ENGINE
            user_total = sum(user_values)
            
            if mode == "normalization":
                total_prob = fixed_sum + user_total
                gap = 1.0 - total_prob
                if abs(total_prob - 1.0) < 0.001:
                    st.success(f"{t(content_1_4['interactive']['success_msg'])} (Axiom 2)")
                elif total_prob > 1.0:
                    st.error(t(content_1_4["interactive"]["error_overflow"]))
                else:
                    st.warning(f"{t(content_1_4['interactive']['error_gap'])} ({gap:.2%} missing)")
                    
            elif mode == "additivity":
                correct_val = scenario.get("correct_val", 0.0)
                if abs(user_total - correct_val) < 0.001:
                    st.success(f"Correct $P(A \\cup B) = P(A) + P(B)$ (Axiom 3). New Size: {user_total:.2f}")
                elif user_total < correct_val:
                    st.warning("Too small! $P(A \\cup B)$ must be the sum of the merging companies.")
                else:
                    st.error("Too high! Probabilities only add up, they don't multiply/expand magically.")
                    
            elif mode == "negativity":
                if user_total == 0.0:
                    st.success("Correct. Probabilities cannot be negative (Axiom 1).")
                elif user_total < 0:
                    st.error(f"Invalid! Found negative probability: {user_total:.2f}. Axiom 1 violated.")
                else:
                    st.info("Set the error term to 0.")

            st.markdown("<br>", unsafe_allow_html=True) 
            
            # The Donut Chart
            fig = get_scenario_donut(scenario_key, user_values)
            st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

    # --- EXAM WORKBENCH ---
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown(f"### {render_icon('clipboard-list')} {t(content_1_4['exam']['title'])}", unsafe_allow_html=True)
    st.caption(content_1_4['exam']['source'])
    
    with st.container(border=True):
        # Prepare Options
        opts = content_1_4["exam"]["options"]
        opt_labels = [o["text"] for o in opts]
        
        # Calculate correct index
        correct_id = content_1_4["exam"]["correct_id"]
        correct_idx = next((i for i, o in enumerate(opts) if o["id"] == correct_id), 0)
        
        render_mcq(
            key_suffix="1_4_exam",
            question_text=t(content_1_4["exam"]["question"]),
            options=opt_labels,
            correct_idx=correct_idx,
            solution_text_dict=content_1_4["exam"]["solution"],
            success_msg_dict={"de": "Korrekt", "en": "Correct"},
            error_msg_dict={"de": "Das stimmt nicht ganz.", "en": "That is not quite right."},
            model=model,
            ai_context="Context: Kolmogorov Axioms of Probability.",
            allow_retry=False,
            course_id="vwl",
            topic_id="1",
            subtopic_id="1.4",
            question_id="1_4_exam"
        )
