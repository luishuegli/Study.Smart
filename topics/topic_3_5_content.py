import streamlit as st
import plotly.graph_objects as go
import numpy as np
from views.styles import render_icon
from utils.localization import t
from utils.quiz_helper import render_mcq
from data.exam_questions import get_question
from utils.progress_tracker import track_question_answer, update_local_progress

# --- CONTENT DICTIONARY ---
content_3_5 = {
    "title": {"de": "3.5 Varianz & Standardabweichung", "en": "3.5 Variance & Standard Deviation"},
    "anchor": {"de": "Wie verlässlich ist der Durchschnitt?", "en": "How reliable is the average?"},
    "intro": {
        "text": {
            "de": r"Stell dir zwei Pizzadienste vor. Beide brauchen *im Durchschnitt* 30 Minuten. Aber: 'Pizza A' kommt immer zwischen 29-31 Minuten. 'Pizza B' kommt mal nach 10, mal nach 50 Minuten. Der Durchschnitt ($\mu$) ist gleich, aber das Risiko (Varianz $\sigma^2$) ist völlig anders.",
            "en": r"Imagine two pizza places. Both take *on average* 30 minutes. But: 'Pizza A' always arrives between 29-31 mins. 'Pizza B' arrives sometimes in 10, sometimes in 50 mins. The average ($\mu$) is the same, but the risk (Variance $\sigma^2$) is totally different."
        }
    },
    "playground": {
        "title": {"de": "Der Risiko-Simulator", "en": "The Risk Simulator"},
        "desc": {
            "de": r"Verändere die Streuung ($\sigma$). Der Mittelwert bleibt gleich, aber beobachte, wie 'flach' oder 'spitz' die Kurve wird.",
            "en": r"Change the spread ($\sigma$). The mean stays the same, but watch how 'flat' or 'sharp' the curve becomes."
        },
        "metric_sigma": {"de": r"Standardabweichung ($\sigma$)", "en": r"Standard Deviation ($\sigma$)"}
    },
    "theory": {
        "def_title": {"de": "Definition", "en": "Definition"},
        "def_text": {
            "de": "Die Varianz misst den mittleren quadratischen Abstand vom Erwartungswert. Sie bestraft große Abweichungen extrem.",
            "en": "Variance measures the average squared distance from the expected value. It penalizes large deviations heavily."
        },
        "formula_def": r"V(X) = E[(X - \mu)^2]",
        "formula_calc": r"V(X) = E(X^2) - [E(X)]^2"
    },
    "mission": {
        "title": {"de": "Mission: Der Risiko-Investor", "en": "Mission: The Risk Investor"},
        "briefing": {
            "de": r"Du hast zwei Aktien mit identischer Rendite (5%). Deine Nerven halten aber maximal Schwankungen von $\pm 10\%$ aus. Aktie A ist wild ($\sigma=15\%$), Aktie B ist ruhig ($\sigma=5\%$).",
            "en": r"You have two stocks with identical returns (5%). But your nerves can only handle fluctuations of $\pm 10\%$. Stock A is wild ($\sigma=15\%$), Stock B is calm ($\sigma=5\%$).."
        },
        "task": {
            "de": "Wähle die Aktie, die ruhig genug für deine Nerven ist, und beweise es mit einer Simulation.",
            "en": "Choose the stock that is calm enough for your nerves, and prove it with a simulation."
        },
        "sim_btn": {"de": "10 Jahre simulieren", "en": "Simulate 10 Years"},
        "success": {
            "de": "Gute Wahl! Stabile Rendite ohne Herzinfarkt.",
            "en": "Good choice! Stable returns without a heart attack."
        }
    },
    "pro_tip": {
        "text": {
            "de": "Nutze für Berechnungen fast immer den Verschiebungssatz: $E(X^2) - E(X)^2$. Das ist viel schneller als die Summendefinition!",
            "en": "Almost always use the shortcut formula for calculations: $E(X^2) - E(X)^2$. It's much faster than the sum definition!"
        }
    }
}

def render_subtopic_3_5(model):
    """3.5 Variance - The Pizza/Risk Metaphor"""
    
    # --- CSS INJECTION ---
    st.markdown("""
    <style>
    [data-testid="stHorizontalBlock"] { align-items: stretch !important; }
    
    /* Slider Colors for Risk */
    .stSlider:has([aria-label*="Spread"]) div[data-baseweb="slider"] > div:first-child > div:first-child { background-color: #AF52DE !important; }
    .stSlider:has([aria-label*="Spread"]) div[role="slider"] { border: 2px solid #AF52DE !important; }
    </style>
    """, unsafe_allow_html=True)

    st.header(t(content_3_5["title"]))
    st.markdown(f"**{t(content_3_5['anchor'])}**")
    st.markdown("---")

    # --- INTUITION ---
    with st.container(border=True):
        st.markdown(f"### {render_icon('lightbulb', '#F59E0B')} {t({'de': 'Die Intuition', 'en': 'The Intuition'})}", unsafe_allow_html=True)
        st.markdown(t(content_3_5["intro"]["text"]))
    
    st.markdown("<br>", unsafe_allow_html=True)

    # --- PLAYGROUND: RISK SIMULATOR ---
    st.markdown(f"### {t(content_3_5['playground']['title'])}")
    with st.container(border=True):
        st.caption(t(content_3_5["playground"]["desc"]))

        # Controls
        if "risk_sigma" not in st.session_state: st.session_state.risk_sigma = 1.0

        c_ctrl, c_vis = st.columns([1, 2], gap="large")

        with c_ctrl:
            sigma = st.slider(
                t({"de": "Streuung (Spread)", "en": "Spread"}),
                0.5, 3.0, st.session_state.risk_sigma, 0.1,
                key="risk_slider"
            )
            st.session_state.risk_sigma = sigma

            st.metric(t(content_3_5["playground"]["metric_sigma"]), f"{sigma:.1f}")
            st.metric(t({"de": r"Varianz ($\sigma^2$)", "en": r"Variance ($\sigma^2$)"}), f"{sigma**2:.2f}")

        with c_vis:
            fig = get_risk_chart(sigma)
            st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

    st.markdown("<br>", unsafe_allow_html=True)

    # --- THEORY ---
    c1, c2 = st.columns(2, gap="medium")
    with c1:
        with st.container(border=True):
            st.markdown(f"**{t(content_3_5['theory']['def_title'])}**")
            st.markdown(t(content_3_5["theory"]["def_text"]))
            st.latex(content_3_5["theory"]["formula_def"])
    with c2:
        with st.container(border=True):
            st.markdown(f"**{t({'de': 'Rechen-Trick (Verschiebungssatz)', 'en': 'Calculation Trick (Shortcut)'})}**")
            st.markdown(t(content_3_5['pro_tip']['text'])) # Embedding pro tip here as it explains the formula
            st.latex(content_3_5["theory"]["formula_calc"])

    st.markdown("<br>", unsafe_allow_html=True)

    # --- MISSION: RISK INVESTOR ---
    st.markdown(f"### {t(content_3_5['mission']['title'])}")
    with st.container(border=True):
        st.markdown(t(content_3_5["mission"]["briefing"]))
        st.markdown(f"**{t(content_3_5['mission']['task'])}**")

        if "mission_3_5_done" not in st.session_state: st.session_state.mission_3_5_done = False
        if "stock_sim_data" not in st.session_state: st.session_state.stock_sim_data = None

        # Choice
        stock_choice = st.radio(
            t({"de": "Wähle dein Portfolio", "en": "Choose your Portfolio"}),
            ["Stock A (High Risk)", "Stock B (Low Risk)"],
            horizontal=True
        )

        # Simulation
        if st.button(t(content_3_5["mission"]["sim_btn"])):
            rng = np.random.default_rng()
            # Mean return 5% per year, sigma depends on choice
            mu_ret = 5.0
            sigma_ret = 15.0 if "Stock A" in stock_choice else 5.0

            years = np.arange(1, 11)
            returns = rng.normal(mu_ret, sigma_ret, 10)
            st.session_state.stock_sim_data = (years, returns, stock_choice)

            # Check Win Condition
            # Winning: Choosing Stock B (Low Risk)
            if "Stock B" in stock_choice:
                if not st.session_state.mission_3_5_done:
                    st.balloons()
                    st.session_state.mission_3_5_done = True
                    user = st.session_state.get("user")
                    if user:
                        track_question_answer(user["localId"], "vwl", "3", "3.5", "3_5_mission", True)
                        update_local_progress("3", "3.5", "3_5_mission", True)
                        st.rerun()

        # Results
        if st.session_state.stock_sim_data:
            years, returns, choice_made = st.session_state.stock_sim_data

            c_res_vis, c_res_txt = st.columns([2, 1])

            with c_res_vis:
                # Line chart of returns
                fig_sim = go.Figure()
                fig_sim.add_trace(go.Scatter(
                    x=years, y=returns, mode='lines+markers',
                    line=dict(color='#FF4B4B' if "Stock A" in choice_made else '#34C759', width=3),
                    name=t({"de": "Jahresrendite", "en": "Annual Return"})
                ))
                # Add "Tolerance Band" (+/- 10%)
                fig_sim.add_hrect(y0=-10, y1=10, fillcolor="gray", opacity=0.1, line_width=0, annotation_text=t({"de": "Komfortzone", "en": "Comfort Zone"}))

                fig_sim.update_layout(
                    title=f"{t({'de': 'Simulation', 'en': 'Simulation'})}: {choice_made}",
                    yaxis=dict(title=t({"de": "Rendite (%)", "en": "Return (%)"}), range=[-30, 40]),
                    xaxis=dict(title=t({"de": "Jahr", "en": "Year"})),
                    height=250, margin=dict(t=30, b=20, l=20, r=20)
                )
                st.plotly_chart(fig_sim, use_container_width=True)

            with c_res_txt:
                max_loss = np.min(returns)
                volatility = np.std(returns)

                st.metric(t({"de": "Max. Verlust (pro Jahr)", "en": "Max Drawdown (Yearly)"}), f"{max_loss:.1f}%")
                st.metric(t({"de": "Realisierte Volatilität", "en": "Realized Volatility"}), f"{volatility:.1f}%")

                if st.session_state.mission_3_5_done and "Stock B" in choice_made:
                     st.success(t(content_3_5["mission"]["success"]))
                elif "Stock A" in choice_made:
                    st.error(t({"de": "Zu gefährlich! Du hast die Toleranzgrenze (-10%) wahrscheinlich gerissen.", "en": "Too dangerous! You likely breached the tolerance limit (-10%)."}))


    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- EXAM PRACTICE ---
    st.markdown(f"### {t({'de': 'Prüfungstraining', 'en': 'Exam Practice'})}")
    
    q_data = get_question("3.5", "uebung2_mc8")
    if q_data:
        with st.container(border=True):
            st.caption(q_data.get("source", ""))
            opts = q_data.get("options", [])
            if opts and isinstance(opts[0], dict) and ('de' in opts[0] or 'en' in opts[0]):
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
                ai_context="Variance calculation shortcut formula",
                course_id="vwl", topic_id="3", subtopic_id="3.5", question_id="3_5_mc8"
            )

def get_risk_chart(sigma):
    """Normal distribution with variable sigma."""
    x = np.linspace(-10, 10, 300)
    mu = 0
    y = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma)**2)

    fig = go.Figure()

    # Reference (Sigma=1)
    y_ref = (1 / (1.0 * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - 0) / 1.0)**2)
    fig.add_trace(go.Scatter(x=x, y=y_ref, mode='lines', line=dict(color='gray', width=1, dash='dot'), name="Standard"))

    # Dynamic
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', line=dict(color='#AF52DE', width=3), name="Current"))

    # Shade 1-Sigma Area
    mask = (x >= -sigma) & (x <= sigma)
    fig.add_trace(go.Scatter(
        x=np.concatenate(([x[mask][0]], x[mask], [x[mask][-1]])),
        y=np.concatenate(([0], y[mask], [0])),
        fill='toself', fillcolor='rgba(175, 82, 222, 0.2)', line=dict(width=0), hoverinfo='skip', name="1-Sigma"
    ))

    fig.update_layout(
        xaxis=dict(title="x", range=[-8, 8], fixedrange=True),
        yaxis=dict(visible=False, range=[0, 0.85], fixedrange=True),
        margin=dict(t=20, b=20, l=20, r=20),
        height=250,
        showlegend=False,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )
    return fig
