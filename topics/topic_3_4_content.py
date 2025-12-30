import streamlit as st
import plotly.graph_objects as go
import numpy as np
from utils.localization import t
from utils.quiz_helper import render_mcq
from data.exam_questions import get_question

# --- CONTENT DICTIONARY ---
content_3_4 = {
    "title": {
        "de": "3.4 Erwartungswert & Varianz",
        "en": "3.4 Expected Value & Variance"
    },
    "intuition": {
        "title": {"de": "Die Intuition", "en": "The Intuition"},
        "text": {
            "de": "Stell dir eine Wippe vor. Der Erwartungswert $E(X)$ ist genau der Punkt, an dem die Wippe im Gleichgewicht ist. Die Varianz $Var(X)$ misst, wie weit die Gewichte (Wahrscheinlichkeiten) vom Zentrum entfernt liegen. Je weiter außen, desto wackeliger.",
            "en": "Imagine a seesaw. The Expected Value $E(X)$ is exactly the point where the seesaw balances. The Variance $Var(X)$ measures how far the weights (probabilities) are from the center. The further out, the more unstable."
        }
    },
    "interactive": {
        "title": {"de": "Die Wippe", "en": "The Seesaw"},
        "instruction": {
            "de": "Verschiebe das Gewicht bei X=3. Beobachte, wie sich der Schwerpunkt (Erwartungswert) verschiebt.",
            "en": "Move the weight at X=3. Watch how the center of gravity (Expected Value) shifts."
        }
    },
    "definition": {
        "title": {"de": "Die Definitionen", "en": "The Definitions"},
        "e_x": {
            "title": "Erwartungswert E(X)",
            "text": {"de": "Der 'Durchschnitt' auf lange Sicht.", "en": "The 'average' in the long run."},
            "formula": r"E(X) = \sum x \cdot P(X=x)"
        },
        "var_x": {
            "title": "Varianz Var(X)",
            "text": {"de": "Die durchschnittliche quadratische Abweichung vom Zentrum.", "en": "The average squared deviation from the center."},
            "formula": r"Var(X) = E((X - E(X))^2)"
        }
    },
    "pro_tip": {
        "title": {"de": "Profi-Tipp", "en": "Pro Tip"},
        "text": {
            "de": "Für die Varianz gibt es eine schnellere Formel: 'Verschiebungssatz'. Rechne $E(X^2) - (E(X))^2$. Das ist fast immer einfacher als die Definition.",
            "en": "For variance, there is a faster formula: 'Displacement Theorem'. Calculate $E(X^2) - (E(X))^2$. This is almost always easier than the definition."
        }
    },
    "mission": {
        "title": {"de": "Mission: Das faire Spiel", "en": "Mission: The Fair Game"},
        "task": {
            "de": "Ein Spiel kostet 5€ Einsatz. Du wirfst einen Würfel. Bei einer 6 gewinnst du 30€. Ist das Spiel fair ($E(Gewinn) = 0$)?",
            "en": "A game costs 5€ to play. You roll a die. If you roll a 6, you win 30€. Is the game fair ($E(Profit) = 0$)?"
        },
        "options": [
            {"id": "a", "de": "Ja, es ist fair.", "en": "Yes, it is fair."},
            {"id": "b", "de": "Nein, du verlierst durchschnittlich Geld.", "en": "No, you lose money on average."},
            {"id": "c", "de": "Nein, du gewinnst durchschnittlich Geld.", "en": "No, you win money on average."}
        ],
        "correct_id": "a",
        "solution": {
            "de": "Richtig! $E(X) = \frac{1}{6} \cdot 25€ + \frac{5}{6} \cdot (-5€) = 0€$. (Gewinn = Auszahlung - Einsatz)",
            "en": "Correct! $E(X) = \frac{1}{6} \cdot 25€ + \frac{5}{6} \cdot (-5€) = 0€$. (Profit = Payout - Cost)"
        }
    }
}

def render_interactive_balance():
    """Renders the Balance Beam interactive."""

    col_ctrl, col_viz = st.columns([1, 2])

    # State: Weights at positions 1, 2, 3
    # We allow user to change probability mass at position 3
    # P(1) and P(2) adjust

    if "bal_p3" not in st.session_state: st.session_state.bal_p3 = 0.33

    with col_ctrl:
        st.markdown(f"**{t(content_3_4['interactive']['instruction'])}**")

        # Slider for P(X=3)
        p3 = st.slider("P(X=3)", 0.0, 1.0, st.session_state.bal_p3, 0.01)

        # Distribute rest equally to 1 and 2
        rest = 1.0 - p3
        p1 = rest / 2
        p2 = rest / 2

        # Calculate E(X)
        # X values are 1, 2, 3
        ev = 1*p1 + 2*p2 + 3*p3

        # Calculate Variance
        var = p1*(1-ev)**2 + p2*(2-ev)**2 + p3*(3-ev)**2

        st.markdown(f"""
        <div style="margin-top: 20px; padding: 15px; background: #F3F4F6; border-radius: 8px;">
            <div style="display: flex; justify-content: space-between;">
                <div>
                    <div style="color: #6B7280; font-size: 0.8em;">{t({'de': 'Schwerpunkt E(X)', 'en': 'Center E(X)'})}</div>
                    <div style="font-size: 1.8em; font-weight: bold; color: #007AFF;">{ev:.2f}</div>
                </div>
                <div>
                    <div style="color: #6B7280; font-size: 0.8em;">{t({'de': 'Varianz', 'en': 'Variance'})}</div>
                    <div style="font-size: 1.8em; font-weight: bold; color: #EF4444;">{var:.2f}</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col_viz:
        # Visual: A seesaw line from 0 to 4
        # Weights as circles on top
        # Triangle fulcrum at ev

        fig = go.Figure()

        # The Beam
        fig.add_trace(go.Scatter(
            x=[0.5, 3.5], y=[0, 0],
            mode='lines',
            line=dict(color='#374151', width=4),
            hoverinfo='skip'
        ))

        # The Weights (Bubbles)
        # Size proportional to Probability
        x_vals = [1, 2, 3]
        y_vals = [0.2, 0.2, 0.2] # Fixed height above beam
        sizes = [p1*100, p2*100, p3*100] # Scale for visual
        colors = ['#9CA3AF', '#9CA3AF', '#EF4444'] # Gray, Gray, Red (active)

        fig.add_trace(go.Scatter(
            x=x_vals, y=[0.1]*3,
            mode='markers+text',
            marker=dict(size=sizes, color=colors, sizemode='area', sizeref=2.*max(sizes)/(40.**2), sizemin=4),
            text=[f"{p1:.2f}", f"{p2:.2f}", f"{p3:.2f}"],
            textposition="top center",
            name="Weights"
        ))

        # The Fulcrum (Triangle)
        # Draw as a shape
        fig.add_trace(go.Scatter(
            x=[ev], y=[-0.1],
            mode='markers',
            marker=dict(symbol='triangle-up', size=20, color='#007AFF'),
            name='E(X)'
        ))

        # Labels for X axis positions
        fig.add_trace(go.Scatter(
            x=[1, 2, 3], y=[-0.25]*3,
            mode='text',
            text=["1", "2", "3"],
            textfont=dict(size=14, color='black'),
            hoverinfo='skip'
        ))

        fig.update_layout(
            yaxis=dict(range=[-0.5, 0.5], visible=False, fixedrange=True),
            xaxis=dict(range=[0, 4], visible=False, fixedrange=True),
            margin=dict(l=10, r=10, t=20, b=20),
            height=300,
            showlegend=False,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)'
        )

        st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

def render_subtopic_3_4(model):
    """3.4 Erwartungswerte"""
    
    st.header(t(content_3_4["title"]))
    st.markdown("---")
    
    # --- INTUITION ---
    st.markdown(f"### {t(content_3_4['intuition']['title'])}")

    # CSS Equal Height
    st.markdown("""
    <style>
    [data-testid="stHorizontalBlock"] { align-items: stretch !important; }
    [data-testid="column"] { display: flex !important; flex-direction: column !important; }
    [data-testid="column"] > div { flex: 1 !important; }
    </style>
    """, unsafe_allow_html=True)

    col_int, col_play = st.columns([1, 1.6], gap="medium")

    with col_int:
        with st.container(border=True):
            st.markdown(t(content_3_4["intuition"]["text"]))
            st.markdown("<br>", unsafe_allow_html=True)
            st.info(t({"de": "Wo ist das Gleichgewicht?", "en": "Where is the balance?"}))

    with col_play:
        with st.container(border=True):
            render_interactive_balance()

    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- DEFINITION & PRO TIP ---
    col_def, col_pro = st.columns([1, 1], gap="medium")

    with col_def:
        with st.container(border=True):
            st.markdown(f"**{t(content_3_4['definition']['title'])}**")

            # E(X)
            st.markdown(f"**{content_3_4['definition']['e_x']['title']}**")
            st.caption(t(content_3_4['definition']['e_x']['text']))
            st.latex(content_3_4['definition']['e_x']['formula'])

            st.markdown("<hr>", unsafe_allow_html=True)

            # Var(X)
            st.markdown(f"**{content_3_4['definition']['var_x']['title']}**")
            st.caption(t(content_3_4['definition']['var_x']['text']))
            st.latex(content_3_4['definition']['var_x']['formula'])

    with col_pro:
        with st.container(border=True):
            st.markdown(f"**{t(content_3_4['pro_tip']['title'])}**")
            st.warning(t(content_3_4["pro_tip"]["text"]))

    st.markdown("<br><br>", unsafe_allow_html=True)

    # --- MISSION ---
    st.markdown(f"### {t(content_3_4['mission']['title'])}")
    with st.container(border=True):
        render_mcq(
            key_suffix="3_4_mission",
            question_text=t(content_3_4["mission"]["task"]),
            options=[t(o) for o in content_3_4["mission"]["options"]],
            correct_idx=0,
            solution_text_dict=content_3_4["mission"]["solution"],
            success_msg_dict={"de": "Exzellent!", "en": "Excellent!"},
            error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
            client=model,
            ai_context="Expected Value Fair Game",
            course_id="vwl",
            topic_id="3",
            subtopic_id="3.4",
            question_id="3_4_mission"
        )

    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- EXAM SECTION ---
    st.markdown(f"### {t({'de': 'Prüfungstraining', 'en': 'Exam Practice'})}")
    
    # Existing questions
    with st.container(border=True):
        st.caption("HS 2024 Januar, MC #7")
        q1 = get_question("3.4", "hs2024_mc7")
        if q1:
            opts = q1.get("options", [])
            option_labels = [t(o) for o in opts] if opts and isinstance(opts[0], dict) else opts
                
            render_mcq(
                key_suffix="3_4_mc7",
                question_text=t(q1["question"]),
                options=option_labels,
                correct_idx=q1["correct_idx"],
                solution_text_dict=q1["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Falsch.", "en": "Incorrect."},
                client=model,
                ai_context="Expected value of symmetrical PDF",
                course_id="vwl", topic_id="3", subtopic_id="3.4", question_id="3_4_mc7"
            )
            
    st.markdown("<br>", unsafe_allow_html=True)
    
    with st.container(border=True):
        st.caption("HS 2024 Januar, MC #12")
        q2 = get_question("3.4", "hs2024_mc12")
        if q2:
            opts = q2.get("options", [])
            option_labels = [t(o) for o in opts] if opts and isinstance(opts[0], dict) else opts
                
            render_mcq(
                key_suffix="3_4_mc12",
                question_text=t(q2["question"]),
                options=option_labels,
                correct_idx=q2["correct_idx"],
                solution_text_dict=q2["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Falsch.", "en": "Incorrect."},
                client=model,
                ai_context="Expected value, Wald's identity",
                course_id="vwl", topic_id="3", subtopic_id="3.4", question_id="3_4_mc12"
            )
