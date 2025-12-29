import streamlit as st
import plotly.graph_objects as go
import numpy as np
from views.styles import render_icon
from utils.localization import t
from utils.quiz_helper import render_mcq
from data.exam_questions import get_question

# --- CONTENT DICTIONARY ---
content_1_6 = {
    "title": {"de": "1.6 Wahrscheinlichkeitsräume", "en": "1.6 Probability Spaces"},
    "theory": {
        "discrete": {
            "title": {"de": "Diskrete Räume", "en": "Discrete Spaces"},
            "text": {
                "de": "Zählbar (1, 2, 3...). Einzelwahrscheinlichkeiten $P(\\omega) > 0$ sind möglich.",
                "en": "Countable (1, 2, 3...). Single probabilities $P(\\omega) > 0$ are possible."
            },
            "formula": r"\sum_{i} P(\omega_i) = 1"
        },
        "continuous": {
            "title": {"de": "Stetige Räume", "en": "Continuous Spaces"},
            "text": {
                "de": "Ein Kontinuum. Die Wahrscheinlichkeit für einen exakten Punkt ist immer 0.",
                "en": "A continuum. The probability of hitting an exact point is always 0."
            },
            "formula": r"P(X = x) = 0"
        }
    },
    "interactive": {
        "mission": {"de": "Das Dart-Paradoxon", "en": "The Dart Paradox"},
        "anchor": {
            "de": "**Deine Mission:** Berechne die Wahrscheinlichkeit, eine bestimmte Zone auf der Dartscheibe zu treffen.",
            "en": "**Your Mission:** Calculate the probability of hitting a specific zone on the dartboard."
        },
        "instruction": {
            "de": "Bewege den Slider, um die Zielzone zu vergrößern oder zu verkleinern.",
            "en": "Move the slider to grow or shrink the target zone."
        },
        "point_label": {"de": "Exakter Punkt", "en": "Exact Point"},
        "area_label": {"de": "Zielbereich", "en": "Target Area"},
        "slider_label": {"de": "Ziel-Radius (%)", "en": "Target Radius (%)"},
        "current_radius": {"de": "Aktueller Radius", "en": "Current Radius"},
        "live_math_title": {"de": "Live-Mathematik", "en": "Live Math"},
        "formula_label": {"de": "Trefferwahrscheinlichkeit", "en": "Hit Probability"},
        "concepts": {
            "no_area": {
                "title": {"de": "Keine Fläche = Keine Chance", "en": "No Area = No Chance"},
                "text": {"de": "Ein Punkt hat keine Breite oder Höhe, also keine 'Masse' in einer stetigen Welt.", "en": "A point has no width or height, so no 'mass' in a continuous world."}
            },
            "intervals": {
                "title": {"de": "Intervalle sind König", "en": "Intervals are King"},
                "text": {"de": "Du kannst keinen einzelnen Moment fangen, aber ein 'Zeitfenster' schon.", "en": "You can't catch a single moment in time, but you can catch a 'window' of time."}
            }
        },
        "pro_trick": {
            "de": "**Pro-Trick:** In stetigen Räumen haben nur Intervalle (Bereiche) eine Wahrscheinlichkeit > 0. Einzelne Punkte haben immer P = 0.",
            "en": "**Pro Trick:** In continuous spaces, only intervals (regions) have probability > 0. Individual points always have P = 0."
        }
    }
}

def render_subtopic_1_6(model):
    """1.6 Probability Spaces - The Dartboard Paradox"""
    
    # FIX: Global CSS to prevent LaTeX cutoff
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
    
    st.header(t(content_1_6["title"]))
    
    # --- THEORY SECTION: Equal Height Columns ---
    # Following Rule #2: Equal Height Boxes Protocol
    st.markdown("""
        <style>
        /* Equal-height theory cards - scoped CSS */
        [data-testid="stHorizontalBlock"] { 
            align-items: stretch !important; 
        }
        [data-testid="column"] { 
            display: flex !important; 
            flex-direction: column !important; 
        }
        [data-testid="stVerticalBlock"],
        [data-testid="stVerticalBlockBorderWrapper"] {
            flex: 1 !important; 
            display: flex !important; 
            flex-direction: column !important;
        }
        </style>
    """, unsafe_allow_html=True)
    
    with st.container(border=True):
        col1, col2 = st.columns(2, gap="medium")
        with col1:
            st.markdown(f"**{t(content_1_6['theory']['discrete']['title'])}**")
            st.caption(t(content_1_6["theory"]["discrete"]["text"]))
            st.latex(content_1_6["theory"]["discrete"]["formula"])
        with col2:
            st.markdown(f"**{t(content_1_6['theory']['continuous']['title'])}**")
            st.caption(t(content_1_6["theory"]["continuous"]["text"]))
            st.latex(content_1_6["theory"]["continuous"]["formula"])
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- SECTION HEADER ---
    st.markdown(f"### {t(content_1_6['interactive']['mission'])}")
    
    # --- THE INTERACTIVE DARTBOARD (DIRECT HIT EDITION) ---
    with st.container(border=True):
        # State Management (0-100 scale)
        if "dart_internal_radius" not in st.session_state:
            st.session_state.dart_internal_radius = 0 # Start at point (0%)

        # 1. NARRATIVE HUD (AGGRESSIVE GUIDANCE)
        # Check state to decide message
        curr_r = st.session_state.dart_internal_radius
        
        if curr_r == 0:
            st.markdown(f"""
<div style="background: #f4f4f5; border-left: 4px solid #71717a; padding: 12px 16px; border-radius: 8px; color: #18181b;">
    <strong>{t({'de': 'Schritt 1:', 'en': 'Step 1:'})}</strong> {t({'de': 'Klicke irgendwo auf die Scheibe, um den ersten Dart zu werfen.', 'en': 'Click anywhere on the board to throw your first dart.'})}
</div>
""", unsafe_allow_html=True)
        elif curr_r < 95:
            st.markdown(f"""
<div style="background: #f4f4f5; border-left: 4px solid #71717a; padding: 12px 16px; border-radius: 8px; color: #18181b;">
    <strong>{t({'de': 'Schritt 2:', 'en': 'Step 2:'})}</strong> {t({'de': 'Super! Du hast eine Fläche erzeugt. Klicke jetzt auf den Rand, um alles abzudecken.', 'en': 'Great! You created an area. Now click the edge to cover everything.'})}
</div>
""", unsafe_allow_html=True)
        else:
            st.balloons()
            st.success(f"**{t({'de': 'Finale:', 'en': 'Final Step:'})}** {t({'de': 'Universum erobert! P=1. Überprüfe die Mathematik unten.', 'en': 'Universe captured! P=1. Check the math below.'})}")
            if user := st.session_state.get("user"):
                from utils.progress_tracker import track_question_answer
                track_question_answer(user["localId"], "vwl", "1", "1.6", "1_6_dart_mission", True)

        st.markdown("<br>", unsafe_allow_html=True)

        # 2. THE INTERACTIVE STAGE
        m1, m2 = st.columns(2)
        
        # Math Logic
        r_float = curr_r / 100.0
        prob_area = r_float ** 2
        
        with m1:
            st.metric(t(content_1_6["interactive"]["point_label"]), "0.000...", help="Probability of hitting a mathematical point")
        with m2:
            st.metric(t(content_1_6["interactive"]["area_label"]), f"{prob_area:.2%}", delta=f"r={curr_r}%")

        # THE BOARD (Direct Manipulation)
        fig = go.Figure()
        
        # Background Board (White/Light)
        fig.add_shape(type="circle", x0=-1, y0=-1, x1=1, y1=1, line_color="#333", line_width=3, fillcolor="#fdfdfd")
        
        # The Dynamic Hit Zone
        if r_float > 0:
            fig.add_shape(
                type="circle",
                x0=-r_float, y0=-r_float, x1=r_float, y1=r_float,
                fillcolor="rgba(255, 75, 75, 0.4)",
                line_color="#FF4B4B",
                line_width=2
            )
            # Center Crosshair
            fig.add_trace(go.Scatter(
                x=[0], y=[0],
                mode='markers',
                marker=dict(symbol='x', color='#FF4B4B', size=12),
                showlegend=False,
                hoverinfo='none'
            ))

        # Invisible Click Layer for Full Coverage Interactability
        # We need to ensure clicks are registered everywhere within the [ -1.1, 1.1 ] range
        # Using a mesh grid of invisible points
        grid_x, grid_y = np.meshgrid(np.linspace(-1.1, 1.1, 25), np.linspace(-1.1, 1.1, 25))
        fig.add_trace(go.Scatter(
            x=grid_x.flatten(), y=grid_y.flatten(),
            mode='markers',
            marker=dict(size=10, color='rgba(0,0,0,0)'),
            hoverinfo='none', showlegend=False
        ))

        fig.update_layout(
            xaxis=dict(visible=False, range=[-1.1, 1.1], fixedrange=True),
            yaxis=dict(visible=False, range=[-1.1, 1.1], fixedrange=True, scaleanchor="x", scaleratio=1),
            margin=dict(l=0, r=0, t=20, b=20),
            height=350,
            clickmode='event+select',
            dragmode=False,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)'
        )

        # Callback to handle selection BEFORE the chart is re-rendered
        def handle_dart_click():
            event = st.session_state.get("dart_direct_hit")
            if event and event["selection"]["points"]:
                pt = event["selection"]["points"][0]
                click_x = pt.get("x", 0)
                click_y = pt.get("y", 0)
                dist = np.sqrt(click_x**2 + click_y**2)
                
                # Map 0.0-1.0+ to 0-100 int
                new_r_int = min(100, max(0, int(dist * 100)))
                st.session_state.dart_internal_radius = new_r_int

        event = st.plotly_chart(fig, on_select=handle_dart_click, selection_mode="points", use_container_width=True, key="dart_direct_hit", config={'displayModeBar': False})

        # 3. LIVE NOTATION (Color Coupled)
        st.divider()
        st.latex(fr"""
            P(\text{{Hit}}) = \frac{{\text{{\color{{#FF4B4B}}{{Target Area}}}}}}{{\text{{Total Board}}}} = 
            \frac{{\pi \cdot \color{{#FF4B4B}}{{{r_float:.2f}}}^2}}{{\pi \cdot 1^2}} = \mathbf{{{prob_area:.4f}}}
        """)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- CONCEPT CHECK MCQ ---
    st.markdown(f"### {t({'de': 'Konzept-Check', 'en': 'Concept Check'})}")
    
    # DYNAMIC EXAM: Reference the user's actual selection
    selected_r_val = f"{r_float:.3f}"
    
    ai_context = f"""
    You are a helpful statistics tutor.
    The student just threw a virtual dart and Selected Radius r = {selected_r_val} ({curr_r}%).
    
    --- STUDENT IS LEARNING THIS THEORY ---
    Topic: Probability Spaces (Discrete vs Continuous)
    
    Key Concepts:
    - **Discrete Spaces**: Countable outcomes (dice, coins). Individual points can have P(ω) > 0.
    - **Continuous Spaces**: Uncountable (time, distance). Individual points always have P(X=x) = 0.
    - **The Paradox**: In continuous spaces, only intervals/regions have non-zero probability.
    
    The student is asked about the probability of hitting EXACTLY their selected radius {selected_r_val}.
    Answer: 0.
    """
    
    # Dynamic Question Text
    q_text = {
        "de": f"In einem stetigen Raum (dein Dartboard), wie groß ist die Wahrscheinlichkeit, exakt deinen Radius $r = {selected_r_val}$ zu treffen?",
        "en": f"In a continuous space (your dartboard), what is the probability of hitting exactly your radius $r = {selected_r_val}$?"
    }
    
    # Dynamic Solution Text
    sol_text = {
        "de": f"""
        **Antwort: 0**
        
        Du hast zwar auf Stelle {selected_r_val} geklickt, aber ein mathematischer Punkt hat keine 'Breite'.
        
        $P(R = {selected_r_val}) = 0$
        
        **Merke:** In stetigen Räumen haben nur *Flächen* (Intervalle) eine Wahrscheinlichkeit > 0.
        """,
        "en": f"""
        **Answer: 0**
        
        You clicked at {selected_r_val}, but a mathematical point has no 'width'.
        
        $P(R = {selected_r_val}) = 0$
        
        **Remember:** In continuous spaces, only *areas* (intervals) have probability > 0.
        """
    }

    q_dart_id = "q_1_6_dart"
    q_data_dart = get_question("1.6", q_dart_id)
    
    if q_data_dart:
        with st.container(border=True):
            render_mcq(
                key_suffix="1_6_mcq",
                question_text=t(q_text),
                options=["0", f"1/{curr_r if curr_r>0 else 100}", "1", f"{r_float:.2f}"],
                correct_idx=0,
                solution_text_dict=sol_text,
                success_msg_dict={"de": "Richtig! In stetigen Räumen ist die Wahrscheinlichkeit für exakte Punkte immer 0.", "en": "Correct! In continuous spaces, the probability of exact points is always 0."},
                error_msg_dict={"de": "Nicht ganz. Denke an die Dartscheibe: Ein einzelner Punkt hat keine Fläche.", "en": "Not quite. Think of the dartboard: A single point has no area."},
                client=model,
                ai_context="Topic 1.6: Continuous probability spaces - dartboard problem",
                allow_retry=False,
                course_id="vwl",
                topic_id="1",
                subtopic_id="1.6",
                question_id="p_single_point"
            )
