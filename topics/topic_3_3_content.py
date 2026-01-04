import streamlit as st
import plotly.graph_objects as go
import numpy as np
from math import erf, sqrt
from views.styles import render_icon, inject_equal_height_css
from utils.localization import t
from utils.layouts.foundation import grey_info
from utils.quiz_helper import render_mcq
from data.exam_questions import get_question
from utils.progress_tracker import track_question_answer, update_local_progress

# --- CONTENT DICTIONARY ---
content_3_3 = {
    "title": {"de": "3.3 Stetige Zufallsvariablen", "en": "3.3 Continuous Random Variables"},
    "anchor": {"de": "Warum ist die Wahrscheinlichkeit für GENAU diesen Punkt Null?", "en": "Why is the probability of EXACTLY this point zero?"},
    "intro": {
        "text": {
            "de": "Stell dir vor, du hast einen Fruchtsalat (diskret). Du kannst jedes Stück einzeln aufpicken (P > 0). Jetzt wirfst du alles in den Mixer (stetig). Du hast einen Smoothie. Du kannst nicht mehr ein einzelnes 'Apfel-Atom' herausfischen (P=0). Aber du kannst einen Schluck nehmen (Intervall).",
            "en": "Imagine a fruit salad (discrete). You can pick up each piece (P > 0). Now throw it in a blender (continuous). You have a smoothie. You can't fish out a single 'apple atom' anymore (P=0). But you can take a sip (Interval)."
        }
    },
    "playground": {
        "title": {"de": "Der Smoothie-Scanner", "en": "The Smoothie Scanner"},
        "desc": {
            "de": "Verschiebe das Intervall. Die Wahrscheinlichkeit ist die FLÄCHE unter der Kurve (das Integral). Ein einzelner Strich hat keine Breite, also keine Fläche.",
            "en": "Move the interval. Probability is the AREA under the curve (the integral). A single line has no width, thus no area."
        },
        "metric_area": {"de": "Wahrscheinlichkeit (Fläche)", "en": "Probability (Area)"}
    },
    "theory": {
        "def_title": {"de": "Dichtefunktion (PDF)", "en": "Density Function (PDF)"},
        "def_text": {
            "de": "Bei stetigen Variablen reden wir nicht von Wahrscheinlichkeit an einem Punkt, sondern von **Dichte** $f(x)$. Wahrscheinlichkeit entsteht erst durch Integration über eine Breite.",
            "en": "For continuous variables, we don't speak of probability at a point, but of **density** $f(x)$. Probability only exists by integrating over a width."
        },
        "prop_title": {"de": "Eigenschaften", "en": "Properties"},
        "prop_p1": {"de": "1. Gesamte Fläche = 1 (100%)", "en": "1. Total Area = 1 (100%)"},
        "prop_p2": {"de": "2. Einzelpunkte sind unmöglich:", "en": "2. Single points are impossible:"},
        "prop_formula": r"P(X = x) = 0"
    },
    "mission": {
        "title": {"de": "Mission: Der Fabrik-Tycoon", "en": "Mission: The Factory Tycoon"},
        "briefing": {
            "de": r"Du produzierst High-Tech-Bolzen. Kunden zahlen **$10** pro gutem Bolzen (9.8-10.2mm). Jeder Ausschuss (zu klein/groß) kostet dich **$5** Strafe.",
            "en": r"You produce high-tech bolts. Clients pay **$10** per good bolt (9.8-10.2mm). Any defect (too small/big) costs you **$5** in penalty."
        },
        "task": {
            "de": r"Die Maschine streut mit $\sigma=0.2$. Stelle den Mittelwert $\mu$ so ein, dass dein Profit maximiert wird.",
            "en": r"The machine varies with $\sigma=0.2$. Adjust the mean $\mu$ to maximize your profit."
        },
        "sim_btn": {"de": "Produktionslauf starten (100 Bolzen)", "en": "Start Production Run (100 Bolts)"},
        "success": {
            "de": "Profit Maximiert! Du hast die perfekte Einstellung gefunden.",
            "en": "Profit Maximized! You found the perfect setting."
        }
    },
    "pro_tip": {
        "text": {
            "de": "Lass dich nicht täuschen: $f(x)$ kann größer als 1 sein! Nur die Fläche darf nicht größer als 1 sein. Dichte ist wie 'Konzentration', nicht wie Wahrscheinlichkeit.",
            "en": "Don't be fooled: $f(x)$ can be greater than 1! Only the area cannot exceed 1. Density is like 'concentration', not probability."
        }
    },
    "frag_dich": {
        "header": {"de": "Frag dich: Stetige Variablen", "en": "Ask yourself: Continuous Variables"},
        "questions": [
            {"de": "Kann P(X = 5.000) bei einer stetigen Variable > 0 sein?", "en": "Can P(X = 5.000) be > 0 for a continuous variable?"},
            {"de": "Wenn f(3) = 2, ist das ein Problem? (Wahrscheinlichkeit > 100%?)", "en": "If f(3) = 2, is that a problem? (Probability > 100%?)"},
            {"de": "Was ist der Unterschied zwischen f(x) und P(X=x)?", "en": "What's the difference between f(x) and P(X=x)?"}
        ],
        "conclusion": {"de": "f(x) ist DICHTE, nicht Wahrscheinlichkeit! Nur Flächen (Integrale) sind Wahrscheinlichkeiten.", "en": "f(x) is DENSITY, not probability! Only areas (integrals) are probabilities."}
    },
    "exam_essentials": {
        "trap": {
            "de": "Glauben, dass f(x) ≤ 1 sein muss (wie bei diskreten Variablen).",
            "en": "Believing that f(x) must be ≤ 1 (like with discrete variables)."
        },
        "trap_rule": {
            "de": "**Merke:** f(x) ist DICHTE, nicht Wahrscheinlichkeit! f(x) kann 5, 10, 100 sein - nur die FLÄCHE muss 1 sein.",
            "en": "**Remember:** f(x) is DENSITY, not probability! f(x) can be 5, 10, 100 - only the AREA must be 1."
        },
        "tips": [
            {
                "tip": {"de": "Einzelpunkt = 0", "en": "Single point = 0"},
                "why": {"de": "P(X = exakter Wert) = 0, IMMER. Nutze das für Vereinfachungen!", "en": "P(X = exact value) = 0, ALWAYS. Use this for simplifications!"}
            },
            {
                "tip": {"de": "≤ und < sind gleichwertig", "en": "≤ and < are equivalent"},
                "why": {"de": "P(X ≤ 3) = P(X < 3) weil P(X=3) = 0. Spart Rechenzeit!", "en": "P(X ≤ 3) = P(X < 3) because P(X=3) = 0. Saves calculation time!"}
            }
        ]
    }
}

def render_subtopic_3_3(model):
    """3.3 Continuous Random Variables - The Factory Tycoon"""

    inject_equal_height_css()
    
    # Slider Colors for Factory
    st.markdown("""
    <style>
    .stSlider:has([aria-label*="Mean"]) div[data-baseweb="slider"] > div:first-child > div:first-child { background-color: #34C759 !important; }
    .stSlider:has([aria-label*="Mean"]) div[role="slider"] { border: 2px solid #34C759 !important; }
    </style>
    """, unsafe_allow_html=True)

    st.header(t(content_3_3["title"]))
    st.markdown("---")

    # --- INTUITION (Header OUTSIDE container) ---
    st.markdown(f"### {t({'de': 'Die Intuition', 'en': 'The Intuition'})}")
    with st.container(border=True):
        st.markdown(t(content_3_3["intro"]["text"]))
    
    st.markdown("<br>", unsafe_allow_html=True)

    # --- PLAYGROUND: SMOOTHIE SCANNER ---
    st.markdown(f"### {t(content_3_3['playground']['title'])}")
    with st.container(border=True):
        st.caption(t(content_3_3["playground"]["desc"]))

        c_ctrl, c_vis = st.columns([1, 2], gap="large")

        with c_ctrl:
            interval = st.slider(t({"de": "Intervall (a bis b)", "en": "Interval (a to b)"}), -3.0, 3.0, (-0.5, 0.5), 0.1)
            a, b = interval

            p_area = 0.5 * (erf(b/sqrt(2)) - erf(a/sqrt(2)))
            st.metric(t(content_3_3["playground"]["metric_area"]), f"{p_area:.1%}")

            if abs(a - b) < 0.01:
                st.warning(t({"de": "Breite ≈ 0 → Wahrscheinlichkeit ≈ 0", "en": "Width ≈ 0 → Probability ≈ 0"}))

        with c_vis:
            fig = get_pdf_area_chart(a, b)
            st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

    st.markdown("<br>", unsafe_allow_html=True)

    # --- THE FORMULA + VARIABLE DECODER + KEY INSIGHT ---
    st.markdown(f"### {t({'de': 'Die Formel', 'en': 'The Formula'})}")
    with st.container(border=True):
        st.latex(r"P(a \le X \le b) = \int_a^b f(x) \, dx")
        st.caption(t(content_3_3["theory"]["def_text"]))
        
        st.markdown("---")
        
        # Variable Decoder
        st.markdown(f"**{t({'de': 'Die Variablen erklärt', 'en': 'The Variables Explained'})}:**")
        st.markdown(f"""
• $f(x)$ = **{t({"de": "Dichtefunktion (PDF)", "en": "Density Function (PDF)"})}** — {t({"de": "Wie 'konzentriert' ist die Wahrscheinlichkeit bei x? (Kann > 1 sein!)", "en": "How 'concentrated' is probability at x? (Can be > 1!)"})}

• $\\int_a^b$ = **{t({"de": "Das Integral", "en": "The Integral"})}** — {t({"de": "Berechnet die FLÄCHE unter der Kurve von a bis b", "en": "Calculates the AREA under the curve from a to b"})}

• $a, b$ = **{t({"de": "Die Grenzen", "en": "The Bounds"})}** — {t({"de": "Start und Ende des Intervalls (z.B. 9.8mm bis 10.2mm)", "en": "Start and end of the interval (e.g., 9.8mm to 10.2mm)"})}

• $P(a \\le X \\le b)$ = **{t({"de": "Intervall-Wahrscheinlichkeit", "en": "Interval Probability"})}** — {t({"de": "Die Chance, dass X irgendwo zwischen a und b liegt", "en": "The chance that X falls somewhere between a and b"})}
""")
        
        st.markdown("---")
        
        # Key Insight
        key_insight = t({
            'de': 'Der Schlüssel: Ein EINZELNER Punkt hat Wahrscheinlichkeit NULL! Warum? Weil ein Strich keine Breite hat, also keine Fläche. Nur Intervalle (Schlücke vom Smoothie) haben Wahrscheinlichkeit > 0.',
            'en': 'The key: A SINGLE point has ZERO probability! Why? Because a line has no width, thus no area. Only intervals (sips of the smoothie) have probability > 0.'
        })
        st.markdown(f"*{key_insight}*")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- PROPERTIES (Stupid Person Proof) ---
    st.markdown(f"### {t(content_3_3['theory']['prop_title'])}")
    with st.container(border=True):
        # Property 1
        st.markdown(f"**1. {t({'de': 'Gesamte Fläche = 1', 'en': 'Total Area = 1'})}**")
        st.latex(r"\int_{-\infty}^{\infty} f(x) \, dx = 1")
        prop1_why = t({
            'de': '*Warum? Der gesamte Smoothie ist 100%. Die Kurve muss die ganzen 100% irgendwo verteilen.*',
            'en': '*Why? The entire smoothie is 100%. The curve must distribute all 100% somewhere.*'
        })
        st.markdown(prop1_why)
        
        st.markdown("---")
        
        # Property 2
        st.markdown(f"**2. {t({'de': 'Einzelpunkte sind unmöglich', 'en': 'Single Points Are Impossible'})}**")
        st.latex(content_3_3["theory"]["prop_formula"])
        prop2_why = t({
            'de': '*Warum? Stell dir vor, du versuchst GENAU ein Apfel-Atom aus dem Smoothie zu fischen. Das ist physisch unmöglich - du bekommst immer etwas Umgebung mit.*',
            'en': '*Why? Imagine trying to fish out EXACTLY one apple atom from the smoothie. That\'s physically impossible - you always get some surroundings.*'
        })
        st.markdown(prop2_why)

    st.markdown("<br>", unsafe_allow_html=True)

    # --- MISSION: FACTORY TYCOON ---
    st.markdown(f"### {t(content_3_3['mission']['title'])}")
    with st.container(border=True):
        st.markdown(t(content_3_3["mission"]["briefing"]))
        st.markdown(f"**{t(content_3_3['mission']['task'])}**")

        if "eng_mu" not in st.session_state: st.session_state.eng_mu = 9.0
        if "mission_3_3_done" not in st.session_state: st.session_state.mission_3_3_done = False
        if "factory_profit" not in st.session_state: st.session_state.factory_profit = None

        mu = st.slider(
            t({"de": "Maschinen-Einstellung (µ)", "en": "Machine Setting (µ)"}),
            9.0, 11.0, st.session_state.eng_mu, 0.05,
            key="eng_mu_slider"
        )
        st.session_state.eng_mu = mu

        sigma = 0.2
        lower, upper = 9.8, 10.2

        z1 = (lower - mu) / sigma
        z2 = (upper - mu) / sigma
        yield_rate = 0.5 * (erf(z2/sqrt(2)) - erf(z1/sqrt(2)))

        col_m_vis, col_m_res = st.columns([2, 1])

        with col_m_vis:
            fig_eng = get_engineer_chart(mu, sigma, lower, upper)
            st.plotly_chart(fig_eng, use_container_width=True, config={'displayModeBar': False})

        with col_m_res:
            st.metric("Theoretical Yield", f"{yield_rate:.1%}")

            # Simulation
            if st.button(t(content_3_3["mission"]["sim_btn"])):
                rng = np.random.default_rng()
                bolts = rng.normal(mu, sigma, 100)
                good = np.sum((bolts >= lower) & (bolts <= upper))
                bad = 100 - good
                profit = (good * 10) - (bad * 5)
                st.session_state.factory_profit = profit

            if st.session_state.factory_profit is not None:
                st.metric("Last Run Profit", f"${st.session_state.factory_profit}")

            # Win Condition: Target mu=10.0 (+/- 0.06)
            target_mu = 10.0
            if abs(mu - target_mu) < 0.06:
                if not st.session_state.mission_3_3_done:
                    st.balloons()
                    st.session_state.mission_3_3_done = True
                    user = st.session_state.get("user")
                    if user:
                        track_question_answer(user["localId"], "vwl", "3", "3.3", "3_3_mission", True)
                        update_local_progress("3", "3.3", "3_3_mission", True)
                st.success(t(content_3_3["mission"]["success"]))
            else:
                 st.session_state.mission_3_3_done = False
                 if mu < target_mu:
                     grey_info(t({"de": "Zu weit links!", "en": "Too far left!"}))
                 else:
                     grey_info(t({"de": "Zu weit rechts!", "en": "Too far right!"}))

    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- ASK YOURSELF ---
    from utils.ask_yourself import render_ask_yourself
    render_ask_yourself(
        header=content_3_3["frag_dich"]["header"],
        questions=content_3_3["frag_dich"]["questions"],
        conclusion=content_3_3["frag_dich"]["conclusion"]
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- EXAM ESSENTIALS ---
    from utils.exam_essentials import render_exam_essentials
    render_exam_essentials(
        trap=content_3_3["exam_essentials"]["trap"],
        trap_rule=content_3_3["exam_essentials"]["trap_rule"],
        tips=content_3_3["exam_essentials"]["tips"]
    )

    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- EXAM PRACTICE ---
    st.markdown(f"### {t({'de': 'Prüfungstraining', 'en': 'Exam Practice'})}")
    q_data = get_question("3.3", "test2_q3")
    if q_data:
        with st.container(border=True):
            st.caption(q_data.get("source", ""))
            opts = q_data.get("options", [])
            if opts and isinstance(opts[0], dict) and ('de' in opts[0] or 'en' in opts[0]):
                option_labels = [t(o) for o in opts]
            else:
                option_labels = opts
            
            render_mcq(
                key_suffix="3_3_q3",
                question_text=t(q_data["question"]),
                options=option_labels,
                correct_idx=q_data["correct_idx"],
                solution_text_dict=q_data["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
                client=model,
                ai_context="Continuous PDF integration",
                course_id="vwl", topic_id="3", subtopic_id="3.3", question_id="3_3_q3"
            )

def get_pdf_area_chart(a, b):
    x = np.linspace(-3.5, 3.5, 200)
    y = (1 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * x**2)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', line=dict(color='black', width=2), hoverinfo='skip'))
    mask = (x >= a) & (x <= b)
    if np.any(mask):
        fig.add_trace(go.Scatter(
            x=np.concatenate(([x[mask][0]], x[mask], [x[mask][-1]])),
            y=np.concatenate(([0], y[mask], [0])),
            fill='toself', fillcolor='rgba(0, 122, 255, 0.3)', line=dict(width=0), hoverinfo='skip'
        ))
    fig.update_layout(xaxis=dict(title="x", range=[-3.5, 3.5], fixedrange=True), yaxis=dict(title="f(x)", range=[0, 0.45], fixedrange=True), margin=dict(t=20, b=20), height=250, showlegend=False)
    return fig

def get_engineer_chart(mu, sigma, lower, upper):
    x = np.linspace(9.0, 11.0, 300)
    y = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma)**2)
    fig = go.Figure()
    fig.add_vrect(x0=lower, x1=upper, fillcolor="rgba(52, 199, 89, 0.1)", layer="below", line_width=0)
    fig.add_vline(x=lower, line_dash="dash", line_color="green")
    fig.add_vline(x=upper, line_dash="dash", line_color="green")
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', line=dict(color='#34C759', width=3)))
    mask = (x >= lower) & (x <= upper)
    if np.any(mask):
        fig.add_trace(go.Scatter(
            x=np.concatenate(([x[mask][0]], x[mask], [x[mask][-1]])),
            y=np.concatenate(([0], y[mask], [0])),
            fill='toself', fillcolor='rgba(52, 199, 89, 0.4)', line=dict(width=0), hoverinfo='skip'
        ))
    fig.update_layout(xaxis=dict(title="Diameter (mm)", range=[9.0, 11.0], fixedrange=True), yaxis=dict(visible=False, fixedrange=True), margin=dict(t=20, b=20), height=250, showlegend=False)
    return fig
