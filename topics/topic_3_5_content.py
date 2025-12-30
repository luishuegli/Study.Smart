import streamlit as st
import plotly.graph_objects as go
import numpy as np
import scipy.stats as stats
from utils.localization import t
from utils.quiz_helper import render_mcq
from data.exam_questions import get_question

# --- CONTENT DICTIONARY ---
content_3_5 = {
    "title": {
        "de": "3.5 Varianz & Standardabweichung",
        "en": "3.5 Variance & Standard Deviation"
    },
    "intuition": {
        "title": {"de": "Die Intuition", "en": "The Intuition"},
        "text": {
            "de": "Stell dir zwei Bogenschützen vor. Beide treffen im **Durchschnitt** genau die Mitte (Erwartungswert ist gleich). Aber Schütze A streut seine Pfeile über die ganze Scheibe (hohe Varianz), während Schütze B immer fast denselben Punkt trifft (niedrige Varianz). Varianz misst die **Verlässlichkeit**.",
            "en": "Imagine two archers. Both hit the **center** on average (Expected Value is equal). But Archer A scatters arrows all over the target (High Variance), while Archer B always hits nearly the same spot (Low Variance). Variance measures **reliability**."
        }
    },
    "interactive": {
        "title": {"de": "Der Präzisions-Tuner", "en": "The Precision Tuner"},
        "instruction": {
            "de": "Reduziere die Standardabweichung $\sigma$. Beobachte, wie sich die 'Treffer' bündeln.",
            "en": "Reduce the standard deviation $\sigma$. Watch how the 'hits' cluster together."
        }
    },
    "definition": {
        "title": {"de": "Die Definition", "en": "The Definition"},
        "text": {
            "de": "Die Varianz ist der durchschnittliche **quadrierte** Abstand vom Zentrum. Wir quadrieren, damit sich Minus und Plus nicht aufheben.",
            "en": "Variance is the average **squared** distance from the center. We square it so minuses and pluses don't cancel each other out."
        },
        "formula": r"Var(X) = E((X - \mu)^2)"
    },
    "pro_tip": {
        "title": {"de": "Profi-Tipp", "en": "Pro Tip"},
        "text": {
            "de": "Varianz hat komische Einheiten (z.B. 'Quadrat-Euro'). Deshalb nutzen wir meist die **Standardabweichung** $\sigma = \sqrt{Var(X)}$. Sie hat dieselbe Einheit wie die Daten (z.B. 'Euro').",
            "en": "Variance has weird units (e.g., 'Square Euros'). That's why we usually use the **Standard Deviation** $\sigma = \sqrt{Var(X)}$. It has the same unit as the data (e.g., 'Euros')."
        }
    },
    "mission": {
        "title": {"de": "Mission: Der 95%-Auftrag", "en": "Mission: The 95% Job"},
        "task": {
            "de": "Du produzierst Schrauben mit Sollwert 10mm. Dein Kunde verlangt, dass **95%** aller Schrauben im Bereich $10 \pm 2$mm liegen. Wie groß darf deine Standardabweichung höchstens sein? (Faustregel: 95% liegen in $\pm 2\sigma$)",
            "en": "You produce screws with a target of 10mm. Your customer requires that **95%** of all screws are within $10 \pm 2$mm. What is the maximum standard deviation allowed? (Rule of thumb: 95% are within $\pm 2\sigma$)"
        },
        "options": [
            {"id": "a", "de": "1.0 mm", "en": "1.0 mm"},
            {"id": "b", "de": "2.0 mm", "en": "2.0 mm"},
            {"id": "c", "de": "0.5 mm", "en": "0.5 mm"}
        ],
        "correct_id": "a",
        "solution": {
            "de": "Richtig! Wenn $2\sigma = 2$mm, dann ist $\sigma = 1$mm.",
            "en": "Correct! If $2\sigma = 2$mm, then $\sigma = 1$mm."
        }
    }
}

def render_interactive_variance():
    """Renders the Archer/Precision visualization."""

    col_ctrl, col_viz = st.columns([1, 2])

    with col_ctrl:
        st.markdown(f"**{t(content_3_5['interactive']['instruction'])}**")

        # Slider for Sigma
        # We start with High Variance
        if "var_sigma" not in st.session_state: st.session_state.var_sigma = 2.0

        sigma = st.slider("Standard Deviation (σ)", 0.1, 3.0, st.session_state.var_sigma, 0.1)
        st.session_state.var_sigma = sigma

        # Metric
        # Calculate % within [-1, 1] just for info
        prob_inside = stats.norm.cdf(1, scale=sigma) - stats.norm.cdf(-1, scale=sigma)

        st.markdown(f"""
        <div style="margin-top: 20px; padding: 15px; background: #F3F4F6; border-radius: 8px; text-align: center;">
            <div style="color: #6B7280; font-size: 0.8em; text-transform: uppercase;">
                {t({'de': 'Streuung', 'en': 'Spread'})} (Var = σ²)
            </div>
            <div style="font-size: 2em; font-weight: bold; color: #EF4444;">
                {sigma**2:.2f}
            </div>
            <div style="margin-top: 5px; font-size: 0.8em; color: #374151;">
                {t({'de': 'Treffer im Zentrum', 'en': 'Hits in Center'})} (±1): <b>{prob_inside*100:.0f}%</b>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col_viz:
        # Visual: A Target (Concentric Circles) + Scatter Plot of Hits

        fig = go.Figure()

        # 1. Target Rings
        # 1-Sigma Ring (68%)
        # 2-Sigma Ring (95%)
        # But for the visual to be fixed, we draw fixed rings at 1, 2, 3 units.
        # And the POINTS move based on sigma.

        # Ring 3 (Outer)
        fig.add_shape(type="circle", x0=-3, y0=-3, x1=3, y1=3, line_color="lightgray")
        # Ring 2
        fig.add_shape(type="circle", x0=-2, y0=-2, x1=2, y1=2, line_color="gray")
        # Ring 1 (Bullseye Area)
        fig.add_shape(type="circle", x0=-1, y0=-1, x1=1, y1=1, line_color="#EF4444", line_width=2)

        # 2. Simulated Hits
        # Generate 100 random points centered at 0 with scale=sigma
        # We use a fixed seed so they "move" deterministically when sigma changes?
        # Actually random is better for "Shot" feel, but "fixed seed dependent on sigma" makes it smooth?
        # Let's try regenerating to show randomness.

        np.random.seed(42) # Fixed seed for stable pattern logic
        # But we want them to expand/contract.
        # So we generate Normalized(0,1) and multiply by sigma.

        raw_x = np.random.normal(0, 1, 100)
        raw_y = np.random.normal(0, 1, 100)

        x_hits = raw_x * sigma
        y_hits = raw_y * sigma

        fig.add_trace(go.Scatter(
            x=x_hits, y=y_hits,
            mode='markers',
            marker=dict(color='#007AFF', size=8, opacity=0.6),
            name='Hits'
        ))

        # Layout
        fig.update_layout(
            xaxis=dict(range=[-4, 4], visible=False, fixedrange=True, scaleanchor="y", scaleratio=1),
            yaxis=dict(range=[-4, 4], visible=False, fixedrange=True),
            margin=dict(l=10, r=10, t=10, b=10),
            height=300,
            showlegend=False,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            shapes=[
                dict(type="line", x0=-4, y0=0, x1=4, y1=0, line=dict(color="rgba(0,0,0,0.1)")),
                dict(type="line", x0=0, y0=-4, x1=0, y1=4, line=dict(color="rgba(0,0,0,0.1)"))
            ]
        )

        st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

def render_subtopic_3_5(model):
    """3.5 Varianz"""
    
    st.header(t(content_3_5["title"]))
    st.markdown("---")
    
    # --- INTUITION ---
    st.markdown(f"### {t(content_3_5['intuition']['title'])}")

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
            st.markdown(t(content_3_5["intuition"]["text"]))
            st.markdown("<br>", unsafe_allow_html=True)
            st.info(t({"de": "Präzision = Geringe Varianz", "en": "Precision = Low Variance"}))

    with col_play:
        with st.container(border=True):
            render_interactive_variance()

    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- DEFINITION & PRO TIP ---
    col_def, col_pro = st.columns([1, 1], gap="medium")

    with col_def:
        with st.container(border=True):
            st.markdown(f"**{t(content_3_5['definition']['title'])}**")
            st.markdown(t(content_3_5["definition"]["text"]))
            st.latex(content_3_5["definition"]["formula"])

    with col_pro:
        with st.container(border=True):
            st.markdown(f"**{t(content_3_5['pro_tip']['title'])}**")
            st.warning(t(content_3_5["pro_tip"]["text"]))

    st.markdown("<br><br>", unsafe_allow_html=True)

    # --- MISSION ---
    st.markdown(f"### {t(content_3_5['mission']['title'])}")
    with st.container(border=True):
        render_mcq(
            key_suffix="3_5_mission",
            question_text=t(content_3_5["mission"]["task"]),
            options=[t(o) for o in content_3_5["mission"]["options"]],
            correct_idx=0,
            solution_text_dict=content_3_5["mission"]["solution"],
            success_msg_dict={"de": "Exzellent!", "en": "Excellent!"},
            error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
            client=model,
            ai_context="Variance 95% Rule",
            course_id="vwl",
            topic_id="3",
            subtopic_id="3.5",
            question_id="3_5_mission"
        )

    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- EXAM SECTION ---
    st.markdown(f"### {t({'de': 'Prüfungstraining', 'en': 'Exam Practice'})}")
    
    q_data = get_question("3.5", "uebung2_mc8")
    if q_data:
        with st.container(border=True):
            st.caption(q_data.get("source", ""))
            
            opts = q_data.get("options", [])
            if opts and isinstance(opts[0], dict):
                option_labels = [t(o) for o in opts]
            else:
                option_labels = opts
            
            render_mcq(
                key_suffix="3_5_mc8",
                question_text=t(q_data["question"]),
                options=option_labels,
                correct_idx=q_data["correct_idx"],
                solution_text_dict=q_data["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
                client=model,
                ai_context="Calculation of Variance from PDF",
                course_id="vwl",
                topic_id="3",
                subtopic_id="3.5",
                question_id="3_5_mc8"
            )
