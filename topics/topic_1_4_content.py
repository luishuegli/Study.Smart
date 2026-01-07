import streamlit as st
import plotly.graph_objects as go
from utils.localization import t
from utils.layouts.foundation import grey_info
from views.styles import render_icon, inject_equal_height_css
from utils.ai_helper import render_ai_tutor
from utils.quiz_helper import render_mcq
from data.exam_questions import get_question

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
                "de": r"$P(\text{Sechs}) = \frac{1}{6} \checkmark$" + "\n" + r"$P(\text{Error}) = -0.2$ false",
                "en": r"$P(\text{Six}) = \frac{1}{6} \checkmark$" + "\n" + r"$P(\text{Error}) = -0.2$ false"
            }
        },
        "2": {
            "title": {"de": "2. Normierung", "en": "2. Normalization"},
            "desc": {"de": "Die Wahrscheinlichkeit des gesamten Ereignisraums ist 100%.", "en": "The probability of the entire sample space is 100%."},
            "latex": r"P(S) = 1",
            "example": {
                "de": r"$P(\text{Kopf}) + P(\text{Zahl}) = 1$ $\checkmark$",
                "en": r"$P(\text{Heads}) + P(\text{Tails}) = 1$ $\checkmark$"
            }
        },
        "3": {
            "title": {"de": "3. Additivität", "en": "3. Additivity"},
            "desc": {"de": "Für disjunkte Ereignisse addieren sich die Wahrscheinlichkeiten.", "en": "For disjoint events, probabilities add up."},
            "latex": r"P(A \cup B) = P(A) + P(B)",
            "example": {
                "de": r"$A = \{1,2\}, B = \{5,6\}$" + "\n" + r"$P(A \cup B) = \frac{4}{6}$ $\checkmark$",
                "en": r"$A = \{1,2\}, B = \{5,6\}$" + "\n" + r"$P(A \cup B) = \frac{4}{6}$ $\checkmark$"
            }
        }
    },
    "interactive": {
        "header": {"de": "Axiom-Labor", "en": "Axiom Lab"},
        "desc": {"de": "Finde die fehlende Wahrscheinlichkeit, um Axiom 2 zu erfüllen.", "en": "Find the missing probability to satisfy Axiom 2."},
        "success_msg": {"de": "Perfekt! Der Ereignisraum ist normiert.", "en": "Perfect! The sample space is normalized."},
        "error_overflow": {"de": "Zu hoch! Axiom 2 verletzt.", "en": "Too high! Axiom 2 violated."},
        "error_gap": {"de": "Lücke! Axiom 2 nicht erfüllt.", "en": "Gap! Axiom 2 not satisfied."}
    },
    "scenarios": {
        "market": {
            "mode": "normalization",
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
            "mode": "additivity",
            "name": {"de": "Die Fusion (Additivität)", "en": "The Merger (Additivity)"},
            "icon": "git-merge",
            "desc": {"de": "Company A (0.15) und B (0.20) fusionieren. Wie groß ist die neue Firma?", "en": "Company A (0.15) and B (0.20) merge. How big is the new entity?"},
            "fixed": [
                {"label": {"de": "Markt Rest", "en": "Market Rest"}, "value": 0.65, "color": "#E5E5EA"}
            ],
            "targets": [
                {"label": {"de": "New Giant (A+B)", "en": "New Giant (A+B)"}, "color": "#AF52DE"}
            ],
            "correct_val": 0.35,
            "initial": 0.10
        },
        "glitch": {
            "mode": "negativity",
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
    }
}

def get_scenario_donut(scenario_key, user_values):
    """Generate the Plotly donut chart for the scenario solver."""
    scenario = content_1_4["scenarios"][scenario_key]
    mode = scenario.get("mode", "normalization")
    
    fixed_sum = sum(item["value"] for item in scenario["fixed"])
    user_sum = sum(user_values)
    total_prob = fixed_sum + user_sum
    
    labels = [t(item["label"]) for item in scenario["fixed"]]
    values = [item["value"] for item in scenario["fixed"]]
    colors = [item.get("color", "#007AFF") for item in scenario["fixed"]]
    patterns = [""] * len(scenario["fixed"])
    
    for idx, target in enumerate(scenario["targets"]):
        val = user_values[idx]
        labels.append(t(target["label"]))
        
        if val < 0:
            values.append(abs(val))
            colors.append(target["color"]) 
            patterns.append("/")
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
        textposition='outside',
        textfont=dict(family="Arial Black, sans-serif", size=12, color="black"),
        hoverinfo='label+value',
        sort=False
    )])
    
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
        correct_val = scenario.get("correct_val", 0.0)
        if abs(user_sum - correct_val) < 0.001:
            center_text = f"<b>P(A∪B)<br>{user_sum:.2f}</b>"
            center_color = "#34C759"
        else:
            center_text = f"<b>P(A∪B)<br>{user_sum:.2f}</b>"
            center_color = "#AF52DE"
             
    elif mode == "negativity":
        center_text = f"<b>Error<br>{user_sum:.2f}</b>"
        if user_sum < 0:
            center_color = "#FF3B30"
        elif user_sum == 0:
            center_text = "<b>VALID<br>0.00</b>"
            center_color = "#34C759"
    
    fig.update_layout(
        annotations=[dict(
            text=center_text,
            x=0.5, y=0.5, font_size=16, font_color=center_color, showarrow=False
        )],
        showlegend=False,
        margin=dict(l=60, r=60, t=40, b=40),
        height=300,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    
    return fig

def render_subtopic_1_4(model):
    inject_equal_height_css()
    
    # --- HEADER ---
    st.header(t(content_1_4["title"]))
    st.markdown("---")

    # --- THEORY SECTION ---
    st.markdown(f"### {t(content_1_4['theory_header'])}")
    st.caption(t(content_1_4["intro"]))
    st.markdown("<br>", unsafe_allow_html=True)
    
    # === ROW 1: THREE AXIOM CARDS SIDE-BY-SIDE ===
    c1, c2, c3 = st.columns(3, gap="small")
    
    axiom_cols = [c1, c2, c3]
    for idx, axiom_num in enumerate(["1", "2", "3"]):
        axiom = content_1_4["axioms"][axiom_num]
        with axiom_cols[idx]:
            with st.container(border=True):
                st.markdown(f"**{t(axiom['title'])}**")
                st.caption(t(axiom['desc']))
                st.latex(axiom['latex'])
                st.markdown("")
                st.markdown(t(axiom['example']), unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # === ROW 2: INTERACTIVE LAB (Controls Left, Chart Right) ===
    st.markdown(f"### {t(content_1_4['interactive']['header'])}")
    
    with st.container(border=True):
        col_ctrl, col_vis = st.columns([1, 1.5], gap="large")
        
        with col_ctrl:
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
                st.markdown(f"- {t(item['label'])}: {item['value']:.2f}")
                fixed_sum += item["value"]
            
            st.markdown("")
            
            # Sliders for each target
            user_values = []
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
            
            # Logic Engine & Feedback
            user_total = sum(user_values)
            
            if mode == "normalization":
                total_prob = fixed_sum + user_total
                gap = 1.0 - total_prob
                if abs(total_prob - 1.0) < 0.001:
                    st.success(t(content_1_4['interactive']['success_msg']))
                elif total_prob > 1.0:
                    st.error(t(content_1_4["interactive"]["error_overflow"]))
                else:
                    st.warning(f"{t(content_1_4['interactive']['error_gap'])} ({gap:.0%} missing)")
                    
            elif mode == "additivity":
                correct_val = scenario.get("correct_val", 0.0)
                if abs(user_total - correct_val) < 0.001:
                    st.success(f"Correct! $P(A \\cup B) = {user_total:.2f}$")
                elif user_total < correct_val:
                    st.warning(t({"de": "Zu klein!", "en": "Too small!"}))
                else:
                    st.error(t({"de": "Zu hoch!", "en": "Too high!"}))
                    
            elif mode == "negativity":
                if user_total == 0.0:
                    st.success(t({"de": "Richtig. Wahrscheinlichkeiten können nicht negativ sein.", "en": "Correct. Probabilities cannot be negative."}))
                elif user_total < 0:
                    st.error(f"Invalid! Negative probability: {user_total:.2f}")
                else:
                    grey_info("Set the error term to 0.")
        
        with col_vis:
            # The Donut Chart
            fig = get_scenario_donut(scenario_key, user_values)
            st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

    # --- EXAM WORKBENCH ---
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    q_id = "q_1_4_logic"
    q_data = get_question("1.4", q_id)
    
    if q_data:
        st.markdown(f"### {t({'de': 'Logik-Check', 'en': 'Logic Check'})}")
        st.caption(t({'de': 'Selbst erstellt', 'en': 'Self-created'}))
        
        with st.container(border=True):
            opt_labels = []
            for o in q_data["options"]:
                if isinstance(o, dict) and "text" in o:
                    opt_labels.append(o["text"])
                else:
                    opt_labels.append(t(o))
            
            render_mcq(
                key_suffix="1_4_exam",
                question_text=t(q_data["question"]),
                options=opt_labels,
                correct_idx=q_data["correct_idx"],
                solution_text_dict=q_data["solution"],
                success_msg_dict={"de": "Korrekt", "en": "Correct"},
                error_msg_dict={"de": "Das stimmt nicht ganz.", "en": "That is not quite right."},
                client=model,
                ai_context="Context: Kolmogorov Axioms of Probability.",
                allow_retry=False,
                course_id="vwl",
                topic_id="1",
                subtopic_id="1.4",
                question_id="q_1_4_logic"
            )
