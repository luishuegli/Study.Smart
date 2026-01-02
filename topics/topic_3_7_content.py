# Topic 3.7: Summary — Random Variables
import streamlit as st
import numpy as np
import plotly.graph_objects as go
from scipy.special import comb
from utils.localization import t
from utils.quiz_helper import render_mcq
from data.exam_questions import get_question
from utils.progress_tracker import track_question_answer, update_local_progress

# ==========================================
# 1. CONTENT DICTIONARY
# ==========================================
content_3_7 = {
    "title": {"de": "3.7 Zusammenfassung", "en": "3.7 Summary"},
    "subtitle": {"de": "Alles Wichtige zu Zufallsvariablen", "en": "Everything Important About Random Variables"},
    
    "cheat_sheet": {
        "header": {"de": "Das Spickzettel", "en": "The Cheat Sheet"},
        "cards": [
            {
                "title": {"de": "CDF → PDF", "en": "CDF → PDF"},
                "formula": r"f(x) = F'(x)",
                "use": {"de": "Ableiten für Dichte", "en": "Differentiate for density"}
            },
            {
                "title": {"de": "PDF → CDF", "en": "PDF → CDF"},
                "formula": r"F(x) = \int_{-\infty}^{x} f(t)\,dt",
                "use": {"de": "Integrieren für Verteilung", "en": "Integrate for distribution"}
            },
            {
                "title": {"de": "E[X] diskret", "en": "E[X] discrete"},
                "formula": r"E[X] = \sum_x x \cdot P(X=x)",
                "use": {"de": "Aus PMF-Tabelle", "en": "From PMF table"}
            },
            {
                "title": {"de": "E[X] stetig", "en": "E[X] continuous"},
                "formula": r"E[X] = \int x \cdot f(x)\,dx",
                "use": {"de": "Aus PDF-Integral", "en": "From PDF integral"}
            },
            {
                "title": {"de": "Varianz", "en": "Variance"},
                "formula": r"Var(X) = E[X^2] - E[X]^2",
                "use": {"de": "Shortcut-Formel!", "en": "Shortcut formula!"}
            },
            {
                "title": {"de": "Standardisierung", "en": "Standardization"},
                "formula": r"Z = \frac{X - \mu}{\sigma}",
                "use": {"de": "Für N(0,1) Tabelle", "en": "For N(0,1) table"}
            }
        ]
    },
    
    "pro_tricks": {
        "header": {"de": "Pro-Tricks", "en": "Pro Tricks"},
        "subtitle": {"de": "Was Top-Studenten wissen", "en": "What Top Students Know"},
        "tricks": [
            {
                "title": {"de": "Varianz-Shortcut", "en": "Variance Shortcut"},
                "wrong": {"de": "E[(X-μ)²] direkt berechnen", "en": "Compute E[(X-μ)²] directly"},
                "right": {"de": "E[X²] - E[X]² verwenden", "en": "Use E[X²] - E[X]²"},
                "reason": {"de": "Viel schneller!", "en": "Much faster!"}
            },
            {
                "title": {"de": "CDF-Sandwich", "en": "CDF Sandwich"},
                "wrong": {"de": "P(a<X≤b) kompliziert integrieren", "en": "Integrate P(a<X≤b) complexly"},
                "right": {"de": "F(b) - F(a)", "en": "F(b) - F(a)"},
                "reason": {"de": "Für diskret UND stetig!", "en": "For discrete AND continuous!"}
            },
            {
                "title": {"de": "Lineare Transformation", "en": "Linear Transform"},
                "wrong": {"de": "Var(aX+b) = a²Var(X) + b", "en": "Var(aX+b) = a²Var(X) + b"},
                "right": {"de": "Var(aX+b) = a²Var(X)", "en": "Var(aX+b) = a²Var(X)"},
                "reason": {"de": "b verschwindet!", "en": "b disappears!"}
            },
            {
                "title": {"de": "Symmetrie-Hack", "en": "Symmetry Hack"},
                "wrong": {"de": "E[X] für symmetrische X berechnen", "en": "Compute E[X] for symmetric X"},
                "right": {"de": "Symmetrisch um 0 → E[X] = 0", "en": "Symmetric around 0 → E[X] = 0"},
                "reason": {"de": "Sofort ablesen!", "en": "Read off instantly!"}
            },
            {
                "title": {"de": "Z-Score Reisepass", "en": "Z-Score Passport"},
                "wrong": {"de": "Für jede Normalverteilung neue Tabelle", "en": "New table for each normal distribution"},
                "right": {"de": "Z berechnen, eine Tabelle!", "en": "Compute Z, one table!"},
                "reason": {"de": "Universal!", "en": "Universal!"}
            }
        ]
    },
    
    "traps": {
        "header": {"de": "Prüfungsfallen", "en": "Exam Traps"},
        "subtitle": {"de": "Diese Fehler vermeiden!", "en": "Avoid These Mistakes!"},
        "items": [
            {
                "trap": {"de": "Gleiche Verteilung = Gleich", "en": "Same Distribution = Equal"},
                "wrong": {"de": "X = Y", "en": "X = Y"},
                "right": {"de": "X und Y haben gleiche Verteilung", "en": "X and Y have same distribution"},
            },
            {
                "trap": {"de": "PDF vergessen zu normieren", "en": "Forgetting to normalize PDF"},
                "wrong": {"de": "∫f(x)dx ≠ 1", "en": "∫f(x)dx ≠ 1"},
                "right": {"de": "Immer prüfen: ∫f(x)dx = 1", "en": "Always check: ∫f(x)dx = 1"},
            },
            {
                "trap": {"de": "Var mit Shift", "en": "Var with Shift"},
                "wrong": {"de": "Var(X+5) = Var(X) + 25", "en": "Var(X+5) = Var(X) + 25"},
                "right": {"de": "Var(X+b) = Var(X)", "en": "Var(X+b) = Var(X)"},
            }
        ]
    },
    
    "interactive": {
        "title": {"de": "Die Symmetrie-Maschine", "en": "The Symmetry Explorer"},
        "desc": {
            "de": "Ruben und Jochen spielen ein faires Münzspiel. Toggle die Overlay-Ansicht!",
            "en": "Ruben and Jochen play a fair coin game. Toggle the overlay view!"
        }
    }
}


def render_subtopic_3_7(model):
    """3.7 Summary — Complete chapter review"""
    
    # --- CSS ---
    st.markdown("""
    <style>
    [data-testid="stHorizontalBlock"] { align-items: stretch !important; }
    [data-testid="column"] { display: flex !important; flex-direction: column !important; }
    [data-testid="column"] > div { flex: 1 !important; }
    h3 { margin-top: 0 !important; }
    </style>
    """, unsafe_allow_html=True)
    
    st.header(t(content_3_7["title"]))
    st.caption(t(content_3_7["subtitle"]))
    st.markdown("---")
    
    # === SECTION 1: CHEAT SHEET ===
    render_cheat_sheet()
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # === SECTION 2: PRO TRICKS ===
    render_pro_tricks()
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # === SECTION 3: EXAM TRAPS ===
    render_exam_traps()
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # === SECTION 4: SYMMETRY EXPLORER ===
    render_symmetry_explorer()
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # === SECTION 5: EXAM PRACTICE ===
    st.markdown(f"### {t({'de': 'Prüfungstraining', 'en': 'Exam Practice'})}")
    
    q_data = get_question("3.7", "hs2024_mc11")
    if q_data:
        with st.container(border=True):
            st.caption(q_data.get("source", ""))
            opts = q_data.get("options", [])
            if opts and isinstance(opts[0], dict):
                option_labels = [t(o) for o in opts]
            else:
                option_labels = opts
            
            render_mcq(
                key_suffix="3_7_mc11",
                question_text=t(q_data["question"]),
                options=option_labels,
                correct_idx=q_data["correct_idx"],
                solution_text_dict=q_data["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Falsch.", "en": "Incorrect."},
                client=model,
                ai_context="Symmetric distributions in fair coin games.",
                course_id="vwl",
                topic_id="3",
                subtopic_id="3.7",
                question_id="hs2024_mc11"
            )


def render_cheat_sheet():
    """Render the formula quick reference cards"""
    cs = content_3_7["cheat_sheet"]
    st.markdown(f"### {t(cs['header'])}")
    
    cards = cs["cards"]
    
    # Row 1: 3 cards
    c1, c2, c3 = st.columns(3, gap="small")
    for col, card in zip([c1, c2, c3], cards[:3]):
        with col:
            with st.container(border=True):
                st.markdown(f"**{t(card['title'])}**")
                st.latex(card['formula'])
                st.caption(t(card['use']))
    
    # Row 2: 3 cards
    c4, c5, c6 = st.columns(3, gap="small")
    for col, card in zip([c4, c5, c6], cards[3:]):
        with col:
            with st.container(border=True):
                st.markdown(f"**{t(card['title'])}**")
                st.latex(card['formula'])
                st.caption(t(card['use']))


def render_pro_tricks():
    """Render the pro tips section"""
    pt = content_3_7["pro_tricks"]
    st.markdown(f"### {t(pt['header'])}")
    st.caption(t(pt['subtitle']))
    
    with st.container(border=True):
        tricks = pt["tricks"]
        
        # Row 1: 3 tricks
        c1, c2, c3 = st.columns(3, gap="small")
        for col, trick in zip([c1, c2, c3], tricks[:3]):
            with col:
                render_trick_card(trick)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Row 2: 2 tricks (centered via padding)
        c4, c5, _ = st.columns([1, 1, 1], gap="small")
        for col, trick in zip([c4, c5], tricks[3:]):
            with col:
                render_trick_card(trick)


def render_trick_card(trick):
    """Render a single pro trick card"""
    st.markdown(f"""
    <div style="background: #f4f4f5; border-radius: 8px; padding: 12px; margin-bottom: 8px;">
        <div style="font-weight: 600; color: #3f3f46; margin-bottom: 8px;">{t(trick['title'])}</div>
        <div style="font-size: 0.85em;">
            <span style="color: #dc2626; text-decoration: line-through;">{t(trick['wrong'])}</span><br>
            <span style="color: #16a34a; font-weight: 500;">{t(trick['right'])}</span>
        </div>
        <div style="font-size: 0.75em; color: #71717a; margin-top: 4px; font-style: italic;">
            {t(trick['reason'])}
        </div>
    </div>
    """, unsafe_allow_html=True)


def render_exam_traps():
    """Render the common exam traps section"""
    traps = content_3_7["traps"]
    st.markdown(f"### {t(traps['header'])}")
    st.caption(t(traps['subtitle']))
    
    with st.container(border=True):
        # Table header
        st.markdown(f"""
        <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 12px; font-weight: 600; margin-bottom: 12px; padding-bottom: 8px; border-bottom: 1px solid #e5e5ea;">
            <div>{t({'de': 'Falle', 'en': 'Trap'})}</div>
            <div style="color: #dc2626;">{t({'de': 'Falsch', 'en': 'Wrong'})}</div>
            <div style="color: #16a34a;">{t({'de': 'Richtig', 'en': 'Right'})}</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Table rows
        for item in traps["items"]:
            st.markdown(f"""
            <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 12px; padding: 8px 0; border-bottom: 1px solid #f4f4f5;">
                <div style="font-weight: 500;">{t(item['trap'])}</div>
                <div style="color: #dc2626; font-family: monospace;">{t(item['wrong'])}</div>
                <div style="color: #16a34a; font-family: monospace;">{t(item['right'])}</div>
            </div>
            """, unsafe_allow_html=True)


def render_symmetry_explorer():
    """Interactive symmetry visualization"""
    inter = content_3_7["interactive"]
    st.markdown(f"### {t(inter['title'])}")
    
    with st.container(border=True):
        st.markdown(t(inter["desc"]))
        st.markdown("---")
        
        # State
        if "sym_n_rounds" not in st.session_state:
            st.session_state.sym_n_rounds = 10
        if "sym_show_overlay" not in st.session_state:
            st.session_state.sym_show_overlay = False
        if "sym_mission_done" not in st.session_state:
            st.session_state.sym_mission_done = False
        
        col_ctrl, col_vis = st.columns([1, 2], gap="large")
        
        with col_ctrl:
            n_rounds = st.slider(
                t({"de": "Runden (n)", "en": "Rounds (n)"}),
                2, 20, st.session_state.sym_n_rounds, 2,
                key="sym_n_rounds"
            )
            
            show_overlay = st.toggle(
                t({"de": "Zeige -X Overlay", "en": "Show -X Overlay"}),
                value=st.session_state.sym_show_overlay,
                key="sym_show_overlay"
            )
            
            if show_overlay:
                if not st.session_state.sym_mission_done:
                    st.balloons()
                    st.session_state.sym_mission_done = True
                    user = st.session_state.get("user")
                    if user:
                        track_question_answer(user["localId"], "vwl", "3", "3.7", "3_7_symmetry_mission", True)
                        update_local_progress("3", "3.7", "3_7_symmetry_mission", True)
                
                st.success(t({"de": "Identisch! X und -X haben dieselbe Verteilung.", "en": "Identical! X and -X have the same distribution."}))
            else:
                st.info(t({"de": "Toggle aktivieren!", "en": "Toggle to reveal!"}))
        
        with col_vis:
            fig = create_symmetry_plot(n_rounds, show_overlay)
            st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
        
        # Pro tip
        st.markdown(f"""
        <div style="background: #f4f4f5; border-radius: 8px; padding: 12px; color: #3f3f46; margin-top: 8px;">
            <strong>Pro Tip:</strong> {t({'de': 'Bei fairen Spielen haben X und -X IMMER dieselbe Verteilung. "Gleiche Verteilung" ≠ "X = Y"!', 'en': 'In fair games, X and -X ALWAYS have the same distribution. "Same distribution" ≠ "X = Y"!'})}
        </div>
        """, unsafe_allow_html=True)


def create_symmetry_plot(n_rounds, show_overlay):
    """Create distribution visualization"""
    values = list(range(-n_rounds, n_rounds + 1, 2))
    probs = []
    for x in values:
        k = (x + n_rounds) // 2
        prob = comb(n_rounds, k, exact=True) * (0.5 ** n_rounds)
        probs.append(prob)
    
    fig = go.Figure()
    
    # X (Ruben) - Blue
    fig.add_trace(go.Bar(
        x=values, y=probs,
        name="X (Ruben)",
        marker_color='#007AFF',
        opacity=0.8, width=1.5
    ))
    
    # -X (Jochen) - Purple overlay
    if show_overlay:
        fig.add_trace(go.Bar(
            x=values, y=probs,
            name="-X (Jochen)",
            marker_color='#AF52DE',
            opacity=0.5, width=1.5
        ))
    
    fig.add_vline(x=0, line_dash="dash", line_color="#6B7280", line_width=1)
    
    fig.update_layout(
        xaxis=dict(title=t({"de": "Gewinn", "en": "Winnings"}), fixedrange=True, showgrid=False),
        yaxis=dict(title="P", fixedrange=True, showgrid=True, gridcolor='#E5E5EA'),
        barmode='overlay',
        height=280,
        margin=dict(l=40, r=20, t=20, b=40),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        legend=dict(orientation="h", y=1.1, x=0.5, xanchor="center")
    )
    
    return fig
