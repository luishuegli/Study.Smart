import streamlit as st
import numpy as np
import plotly.graph_objects as go
from views.styles import render_icon, inject_equal_height_css
from utils.localization import t
from utils.layouts.foundation import grey_info
from utils.quiz_helper import render_mcq
from data.exam_questions import get_question

# ==========================================
# 1. CONTENT DICTIONARY
# ==========================================
content_3_2 = {
    "title": {"de": "3.2 Diskrete Zufallsvariablen", "en": "3.2 Discrete Random Variables"},
    "anchor": {
        "header": {"de": "Die Intuition", "en": "The Intuition"},
        "text": {"de": "Stell dir eine digitale Währung vor. Du hast genau 1 Bitcoin (100% Wahrscheinlichkeit). Du musst diesen einen Coin auf verschiedene Wallets (Werte 1, 2, 3...) verteilen. Wenn du mehr in Wallet 1 steckst, MUSS in den anderen weniger sein. Das ist das 'Nullsummenspiel' der Wahrscheinlichkeit.", "en": "Imagine a digital currency. You have exactly 1 Bitcoin (100% probability). You must distribute this single coin across different wallets (Values 1, 2, 3...). If you put more into Wallet 1, there MUST be less in the others. This is the 'zero-sum game' of probability."},
    },
    "theory": {
        "pmf_title": {"de": "Wahrscheinlichkeitsfunktion (PMF)", "en": "Probability Mass Function (PMF)"},
        "pmf_text": {"de": "Ordnet jedem diskreten Wert x eine Wahrscheinlichkeit P(X=x) zu.", "en": "Assigns a probability P(X=x) to each discrete value x."},
        "prop_title": {"de": "Eigenschaften", "en": "Properties"},
        "props": {
            "p1": {"de": "Niemals negativ: $p_k \\geq 0$", "en": "Never negative: $p_k \\geq 0$"},
            "p2": {"de": "Alles muss da sein: $\\sum p_k = 1$", "en": "All accounted for: $\\sum p_k = 1$"}
        },
        "pmf_formula": r"f(x) = P(X=x)",
        "norm_formula": r"\sum_{i} P(X=x_i) = 1"
    },
    "mission1": {
        "title": {"de": "Mission 1: Die Aufwärmübung", "en": "Mission 1: The Warm-Up"},
        "desc": {"de": "Ein Casino beauftragt dich. Konstruiere einen Würfel, bei dem die **6 genau 50%** der Zeit fällt. Die anderen Zahlen (1-5) sollen gleich wahrscheinlich sein.", "en": "A casino hires you. Construct a die where **6 comes up exactly 50%** of the time. The other numbers (1-5) should be equally likely."},
        "target_p6": 0.50,
        "target_others": 0.10
    },
    "mission2": {
        "title": {"de": "Mission 2: Der gezinkte Würfel", "en": "Mission 2: The Loaded Die"},
        "desc": {"de": "Jetzt wird es schwieriger! Die **6** soll genau **40%** der Zeit erscheinen. Die anderen Zahlen teilen sich den Rest gleichmäßig.", "en": "Now it gets harder! **6** should come up exactly **40%** of the time. The other numbers share the rest equally."},
        "target_p6": 0.40,
        "target_others": 0.12
    },
    "pro_tip": {
        "de": "Der 'Kuchen-Trick': Fehlt in der Prüfung ein Wert? Der ganze Kuchen ist 1. Fehlender Wert = 1 - Summe(Rest). Wenn du n-1 Wahrscheinlichkeiten kennst, kennst du automatisch die letzte!",
        "en": "The 'Cake Trick': Missing a value in the exam? The whole cake is 1. Missing value = 1 - Sum(Rest). If you know n-1 probabilities, you automatically know the last one!"
    },
    "frag_dich": {
        "header": {"de": "Frag dich: Diskrete Wahrscheinlichkeit", "en": "Ask yourself: Discrete Probability"},
        "questions": [
            {"de": "Kann P(X=5) negativ sein?", "en": "Can P(X=5) be negative?"},
            {"de": "Was passiert wenn die Summe aller Wahrscheinlichkeiten > 1 ist?", "en": "What happens if the sum of all probabilities > 1?"},
            {"de": "Wenn du 5 von 6 Wahrscheinlichkeiten kennst, wie findest du die 6.?", "en": "If you know 5 out of 6 probabilities, how do you find the 6th?"}
        ],
        "conclusion": {"de": "Der Kuchen ist immer genau 1!", "en": "The cake is always exactly 1!"}
    },
    "exam_essentials": {
        "trap": {
            "de": "Vergessen zu prüfen ob die Summe wirklich 1 ergibt.",
            "en": "Forgetting to check if the sum really equals 1."
        },
        "trap_rule": {
            "de": "**Immer prüfen:** $\\sum P(x) = 1$? Alle Werte $\\geq 0$?",
            "en": "**Always check:** $\\sum P(x) = 1$? All values $\\geq 0$?"
        },
        "tips": [
            {
                "tip": {"de": "Der Kuchen-Trick", "en": "The Cake Trick"},
                "why": {"de": "Fehlender Wert = $1 - \\sum(\\text{Rest})$. Spart Zeit!", "en": "Missing value = $1 - \\sum(\\text{Rest})$. Saves time!"}
            },
            {
                "tip": {"de": "Normierungskonstante $c$ finden", "en": "Finding normalization constant $c$"},
                "why": {"de": "Setze $\\sum f(x) = 1$ und löse nach $c$ auf.", "en": "Set $\\sum f(x) = 1$ and solve for $c$."}
            }
        ]
    }
}

def render_subtopic_3_2(model):
    """3.2 Discrete Random Variables - High-Fidelity Dashboard"""
    
    inject_equal_height_css()

    st.header(t(content_3_2["title"]))
    st.markdown("---")
    
    # --- THEORY SECTION (Following Pedagogy Rules) ---
    
    # 1. THE INTUITION (Header OUTSIDE container)
    st.markdown(f"### {t(content_3_2['anchor']['header'])}")
    with st.container(border=True):
        st.markdown(t(content_3_2["anchor"]["text"]))
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # 2. THE FORMULA + VARIABLE DECODER + KEY INSIGHT
    st.markdown(f"### {t({'de': 'Die Formel', 'en': 'The Formula'})}")
    with st.container(border=True):
        # Formula
        st.latex(content_3_2['theory']['pmf_formula'])
        st.caption(t(content_3_2['theory']['pmf_text']))
        
        st.markdown("---")
        
        # Variable Decoder
        st.markdown(f"**{t({'de': 'Die Variablen erklärt', 'en': 'The Variables Explained'})}:**")
        st.markdown(f"""
• $f(x)$ = **{t({"de": "Wahrscheinlichkeitsfunktion (PMF)", "en": "Probability Mass Function (PMF)"})}** — {t({"de": "Wie wahrscheinlich ist genau dieser Wert?", "en": "How likely is exactly this value?"})}

• $P(X=x)$ = **{t({"de": "Punktwahrscheinlichkeit", "en": "Point Probability"})}** — {t({"de": "Die Chance, dass X genau gleich x ist", "en": "The chance that X equals exactly x"})}

• $x$ = **{t({"de": "Ein möglicher Wert", "en": "A possible value"})}** — {t({"de": "Ein konkretes Ergebnis (z.B. 1, 2, 3...)", "en": "A specific outcome (e.g., 1, 2, 3...)"})}
""")
        
        st.markdown("---")
        
        # Key Insight
        key_insight = t({
            'de': 'Der Schlüssel: Bei diskreten Variablen "klebt" Wahrscheinlichkeit an einzelnen PUNKTEN. Zwischen den Punkten ist NICHTS. Deshalb SUMME, nicht Integral! Und die Summe muss genau 1 sein - wie ein Kuchen.',
            'en': 'The key: For discrete variables, probability "sticks" to individual POINTS. Between points, there\'s NOTHING. That\'s why we SUM, not integrate! And the sum must equal exactly 1 - like a cake.'
        })
        st.markdown(f"*{key_insight}*")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # 3. PROPERTIES (Stupid Person Proof)
    st.markdown(f"### {t(content_3_2['theory']['prop_title'])}")
    with st.container(border=True):
        # Property 1
        st.markdown(f"**1. {t({'de': 'Niemals negativ', 'en': 'Never Negative'})}**")
        st.latex(r"p_k \geq 0")
        prop1_why = t({
            'de': 'Warum? Du kannst keine "-20% Chance" haben, dass etwas passiert. Wahrscheinlichkeiten sind immer 0% oder mehr.',
            'en': 'Why? You can\'t have a "-20% chance" of something happening. Probabilities are always 0% or more.'
        })
        st.markdown(f"*{prop1_why}*")
        
        st.markdown("---")
        
        # Property 2
        st.markdown(f"**2. {t({'de': 'Summe = 1 (Der Kuchen)', 'en': 'Sum = 1 (The Cake)'})}**")
        st.latex(content_3_2['theory']['norm_formula'])
        prop2_why = t({
            'de': 'Warum? Stell dir einen Kuchen vor. Du kannst ihn in Stücke teilen, aber am Ende hast du immer genau 1 ganzen Kuchen - nicht mehr, nicht weniger. 100% Wahrscheinlichkeit wird auf alle möglichen Ergebnisse aufgeteilt.',
            'en': 'Why? Think of a cake. You can slice it into pieces, but in the end you always have exactly 1 whole cake - no more, no less. 100% probability is divided among all possible outcomes.'
        })
        st.markdown(f"*{prop2_why}*")
        
        st.markdown("---")
        
        # Concrete Example
        example_text = t({
            'de': '**Beispiel Würfel:** P(1) + P(2) + P(3) + P(4) + P(5) + P(6) = 1/6 + 1/6 + 1/6 + 1/6 + 1/6 + 1/6 = 1 ✓',
            'en': '**Die Example:** P(1) + P(2) + P(3) + P(4) + P(5) + P(6) = 1/6 + 1/6 + 1/6 + 1/6 + 1/6 + 1/6 = 1 ✓'
        })
        st.markdown(example_text)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # ROW 3: MISSION TABS
    render_missions_3_2()

    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- ASK YOURSELF ---
    from utils.ask_yourself import render_ask_yourself
    render_ask_yourself(
        header=content_3_2["frag_dich"]["header"],
        questions=content_3_2["frag_dich"]["questions"],
        conclusion=content_3_2["frag_dich"]["conclusion"]
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- EXAM ESSENTIALS ---
    from utils.exam_essentials import render_exam_essentials
    render_exam_essentials(
        trap=content_3_2["exam_essentials"]["trap"],
        trap_rule=content_3_2["exam_essentials"]["trap_rule"],
        tips=content_3_2["exam_essentials"]["tips"]
    )

    # EXAM SECTION
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown(f"### {t({'de': 'Prüfungstraining', 'en': 'Exam Practice'})}")
    
    questions = ["uebung2_mc5", "test2_q4"]
    
    for q_key in questions:
        q_data = get_question("3.2", q_key)
        if q_data:
            with st.container(border=True):
                st.caption(q_data.get("source", ""))
                opts = q_data.get("options", [])
                if opts and isinstance(opts[0], dict):
                    option_labels = [t(o) for o in opts]
                else:
                    option_labels = opts

                render_mcq(
                    key_suffix=f"3_2_{q_key}",
                    question_text=t(q_data["question"]),
                    options=option_labels,
                    correct_idx=q_data["correct_idx"],
                    solution_text_dict=q_data["solution"],
                    success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                    error_msg_dict={"de": "Falsch.", "en": "Incorrect."},
                    client=model,
                    ai_context="Discrete Random Variables",
                    course_id="vwl",
                    topic_id="3",
                    subtopic_id="3.2",
                    question_id=f"3_2_{q_key}"
                )
            st.markdown("<br>", unsafe_allow_html=True)


def render_missions_3_2():
    """Two-mission structure: Easy (50%) and Advanced (3x)"""
    
    tab1, tab2 = st.tabs([
        t(content_3_2["mission1"]["title"]),
        t(content_3_2["mission2"]["title"])
    ])
    
    with tab1:
        render_die_mission(
            mission_key="m1",
            desc_dict=content_3_2["mission1"]["desc"],
            target_p6=0.50,
            target_others=0.10,
            tolerance=0.02  # Easy tolerance
        )
    
    with tab2:
        render_die_mission(
            mission_key="m2",
            desc_dict=content_3_2["mission2"]["desc"],
            target_p6=0.375,
            target_others=0.125,
            tolerance=0.015  # Tighter for advanced
        )
    
    # PRO TIP (Below missions)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"""
    <div style="background-color: #f4f4f5; border-radius: 8px; padding: 12px; color: #3f3f46;">
        <strong>Pro Tip:</strong> {t(content_3_2['pro_tip'])}
    </div>
    """, unsafe_allow_html=True)


def render_die_mission(mission_key, desc_dict, target_p6, target_others, tolerance):
    """Reusable die-building mission component"""
    
    # Slider Colors: Blue for P(1-5), Purple for P(6) - matching bar chart colors
    from utils.layouts.foundation import inject_slider_css
    inject_slider_css([
        {"label_contains": "P(1)", "color": "#007AFF"},  # Blue bars
        {"label_contains": "P(6)", "color": "#AF52DE"},  # Purple bar
    ])
    
    with st.container(border=True):
        st.markdown(t(desc_dict))
        st.markdown("---")

        # State keys
        p_others_key = f"miss_3_2_{mission_key}_p_others"
        p6_key = f"miss_3_2_{mission_key}_p6"
        done_key = f"miss_3_2_{mission_key}_done"

        # Initialize state
        if p_others_key not in st.session_state: st.session_state[p_others_key] = 0.10
        if p6_key not in st.session_state: st.session_state[p6_key] = 0.20
        if done_key not in st.session_state: st.session_state[done_key] = False

        # Controls
        c1, c2 = st.columns([1, 2], gap="large")

        with c1:
            st.markdown(f"**{t({'de': 'Einstellungen', 'en': 'Settings'})}**")
            
            p_others = st.slider(
                "P(1) = P(2) = ... = P(5)", 0.0, 0.30,
                st.session_state[p_others_key], 0.01,
                key=p_others_key,
                disabled=st.session_state[done_key]
            )
            
            p6 = st.slider(
                "P(6)", 0.0, 1.0,
                st.session_state[p6_key], 0.01,
                key=p6_key,
                disabled=st.session_state[done_key]
            )
            
            total_prob = 5 * p_others + p6

            # Validation
            is_sum_ok = abs(total_prob - 1.0) < 0.02
            is_p6_ok = abs(p6 - target_p6) < tolerance
            is_others_ok = abs(p_others - target_others) < tolerance

            if is_sum_ok and is_p6_ok and is_others_ok:
                st.success(t({"de": "Mission erfüllt!", "en": "Mission Accomplished!"}))
                if not st.session_state[done_key]:
                    st.balloons()
                    st.session_state[done_key] = True
                    # Track progress
                    from utils.progress_tracker import track_question_answer, update_local_progress
                    user = st.session_state.get("user")
                    if user:
                        track_question_answer(user["localId"], "vwl", "3", "3.2", f"3_2_{mission_key}", True)
                        update_local_progress("3", "3.2", f"3_2_{mission_key}", True)
                        st.rerun()

                if st.button(t({"de": "Mission zurücksetzen", "en": "Reset Mission"}), key=f"reset_{mission_key}"):
                    st.session_state[done_key] = False
                    st.session_state[p_others_key] = 0.10
                    st.session_state[p6_key] = 0.20
                    st.rerun()
            else:
                st.session_state[done_key] = False
                if not is_sum_ok:
                    if total_prob > 1:
                        st.error(f"{t({'de': 'Summe > 100%', 'en': 'Total > 100%'})} ({total_prob:.0%})")
                    else:
                        st.warning(f"{t({'de': 'Summe < 100%', 'en': 'Total < 100%'})} ({total_prob:.0%})")
                elif is_sum_ok:
                    grey_info(t({"de": f"Summe stimmt! Aber überprüfe die Verhältnisse.", "en": f"Sum is correct! But check the ratios."}))

        with c2:
            # Visualization
            x_vals = [1, 2, 3, 4, 5, 6]
            y_vals = [p_others]*5 + [p6]
            colors = ["#007AFF"]*5 + ["#AF52DE"]

            fig = go.Figure()

            fig.add_trace(go.Bar(
                x=x_vals, y=y_vals,
                marker_color=colors,
                text=[f"{v:.0%}" for v in y_vals],
                textposition='auto',
                name="Theoretical"
            ))

            fig.update_layout(
                title=dict(text=f"Total Mass: {total_prob:.0%}", x=0.5),
                xaxis=dict(tickmode='linear', dtick=1, title="Outcome (Die Face)"),
                yaxis=dict(range=[0, 0.6], title="Probability"),
                height=300,
                margin=dict(l=20, r=20, t=40, b=20),
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                showlegend=False
            )
            st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False}, key=f"chart_{mission_key}")
