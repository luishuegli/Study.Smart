import streamlit as st
import plotly.graph_objects as go
from utils.localization import t
from views.styles import render_icon

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
        "coin": {
            "name": {"de": "Gezinkte Münze", "en": "Biased Coin"},
            "given": [{"label": "Kopf (Heads)", "value": 0.35}],
            "target_label": {"de": "Zahl (Tails)", "en": "Tails"},
            "color": "#FF9500"  # Orange
        },
        "market": {
            "name": {"de": "Aktienmarkt", "en": "Stock Market"},
            "given": [{"label": "Bull Market", "value": 0.45}, {"label": "Bear Market", "value": 0.30}],
            "target_label": {"de": "Seitwärts (Neutral)", "en": "Neutral"},
            "color": "#AF52DE"  # Purple
        },
        "quality": {
            "name": {"de": "Qualitätskontrolle", "en": "Quality Control"},
            "given": [{"label": "OK", "value": 0.92}, {"label": "Ausschuss", "value": 0.03}],
            "target_label": {"de": "Nacharbeit", "en": "Rework"},
            "color": "#FF2D55"  # Red
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
            "en": "**Correct! (c)**<br>Probabilities cannot be negative. This violates **Axiom 1**."
        }
    }
}

def get_scenario_donut(scenario_key, user_value):
    """Generate the Plotly donut chart for the scenario solver."""
    scenario = content_1_4["scenarios"][scenario_key]
    
    # Calculate given sum
    given_sum = sum(item["value"] for item in scenario["given"])
    total_prob = given_sum + user_value
    
    # Build data
    labels = [item["label"] for item in scenario["given"]]
    values = [item["value"] for item in scenario["given"]]
    
    # Add user slice
    target_label = t(scenario["target_label"])
    labels.append(target_label)
    values.append(user_value)
    
    # Colors: Given slices in Apple Blue, User slice in scenario color
    colors = ["#007AFF"] * len(scenario["given"]) + [scenario["color"]]
    
    fig = go.Figure(data=[go.Pie(
        labels=labels,
        values=values,
        hole=0.5,  # Larger hole for HUD
        marker=dict(
            colors=colors,
            line=dict(color='#FFFFFF', width=2)
        ),
        textinfo='label+percent',
        # BOLD TYPOGRAPHY - BLACK TEXT (smaller size)
        textfont=dict(
            family="Arial Black, sans-serif",
            size=14,
            color="black"
        ),
        insidetextfont=dict(
            family="Arial Black, sans-serif",
            size=14,
            color="black"
        ),
        hoverinfo='label+value',
        sort=False
    )])
    
    # THE CENTER HUD (Dynamic Color)
    center_text = f"<b>Σ = {total_prob:.2f}</b>"
    center_color = "black"
    
    # Success: Green
    if abs(total_prob - 1.0) < 0.001:
        center_text = "<b>100%<br>VALID</b>"
        center_color = "#34C759"  # Apple Green
    # Overflow: Red
    elif total_prob > 1.0:
        center_color = "#FF3B30"  # Apple Red
    
    fig.update_layout(
        annotations=[dict(
            text=center_text,
            x=0.5,
            y=0.5,
            font_size=20,
            font_color=center_color,
            showarrow=False
        )],
        showlegend=False,
        margin=dict(l=10, r=10, t=10, b=10),
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
            scenario_options = {
                t(content_1_4["scenarios"]["coin"]["name"]): "coin",
                t(content_1_4["scenarios"]["market"]["name"]): "market",
                t(content_1_4["scenarios"]["quality"]["name"]): "quality"
            }
            
            selected_name = st.selectbox(
                "Scenario",
                options=list(scenario_options.keys()),
                label_visibility="collapsed",
                key="scenario_selector_1_4"
            )
            
            scenario_key = scenario_options[selected_name]
            scenario = content_1_4["scenarios"][scenario_key]
            
            # Display "Given" probabilities
            st.markdown("**Given:**")
            given_sum = 0
            for item in scenario["given"]:
                st.markdown(f"- {item['label']}: **{item['value']:.2f}**")
                given_sum += item["value"]
            
            st.markdown("")
            
            # The Solver Slider
            target_label = t(scenario["target_label"])
            missing_correct = 1.0 - given_sum
            
            user_val = st.slider(
                f"Set P({target_label})",
                min_value=0.0,
                max_value=1.0,
                value=0.0,
                step=0.01,
                key=f"slider_1_4_{scenario_key}"
            )
            
            # Validation Feedback (moved above chart to prevent overlap)
            total_prob = given_sum + user_val
            gap = 1.0 - total_prob
            
            if abs(total_prob - 1.0) < 0.001:
                st.success(t(content_1_4["interactive"]["success_msg"]))
            elif total_prob > 1.0:
                st.error(t(content_1_4["interactive"]["error_overflow"]))
            elif total_prob < 1.0:
                st.warning(f"{t(content_1_4['interactive']['error_gap'])} ({gap:.2%} missing)")
            
            st.markdown("<br>", unsafe_allow_html=True)  # Increased spacer to prevent overlap
            
            # The Donut Chart
            fig = get_scenario_donut(scenario_key, user_val)
            st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

    # --- EXAM WORKBENCH ---
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown(f"### {render_icon('clipboard-list')} {t(content_1_4['exam']['title'])}", unsafe_allow_html=True)
    st.caption(content_1_4['exam']['source'])
    
    with st.container(border=True):
        st.markdown(t(content_1_4["exam"]["question"]))
        
        # Options
        opts = content_1_4["exam"]["options"]
        opt_labels = [o["text"] for o in opts]
        
        # Radio with instant feedback
        radio_key = "mcq_1_4"
        user_selection = st.radio(
            "Selection", 
            options=opt_labels, 
            index=None, 
            key=radio_key,
            label_visibility="collapsed"
        )
        
        # Instant feedback when selection is made
        if user_selection:
            selected_idx = opt_labels.index(user_selection)
            selected_id = opts[selected_idx]["id"]
            
            if selected_id == content_1_4["exam"]["correct_id"]:
                st.success(t({"de": "Korrekt!", "en": "Correct!"}))
                st.session_state.show_sol_1_4 = True
            else:
                st.error(t({"de": "Das stimmt nicht ganz.", "en": "That is not quite right."}))
        
        # Solution (only show if correct answer was selected)
        if st.session_state.get("show_sol_1_4", False):
            st.markdown("---")
            # Fix: Use unsafe_allow_html=True to render HTML tags properly
            sol_text = t(content_1_4["exam"]["solution"])
            st.markdown(sol_text, unsafe_allow_html=True)
            
            # AI Tutor
            st.markdown("---")
            st.caption(f"{render_icon('bot')} AI Tutor", unsafe_allow_html=True)
            
            # AI Response Area (appears above input)
            if "ai_response_1_4" in st.session_state:
                st.markdown(f"**AI:** {st.session_state['ai_response_1_4']}")
                st.markdown("---")
            
            # Input and Button
            c_ai_1, c_ai_2 = st.columns([4, 1])
            with c_ai_1:
                ai_q = st.text_input(
                    t({"de": "Frage:", "en": "Question:"}), 
                    key="ai_q_1_4", 
                    placeholder=t({"de": "Was ist unklar?", "en": "What is unclear?"}),
                    label_visibility="collapsed"
                )
            with c_ai_2:
                if st.button("Ask", key="ai_btn_1_4", type="primary", use_container_width=True):
                    if model and ai_q:
                        with st.spinner("..."):
                            prompt = f"Context: Kolmogorov Axioms of Probability. User Question: {ai_q}"
                            try:
                                response = model.generate_content(prompt)
                                st.session_state["ai_response_1_4"] = response.text
                                st.rerun()
                            except Exception as e:
                                st.error(f"Error: {e}")
                    elif not model:
                        st.error("Model unavailable")
