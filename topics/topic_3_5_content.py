import streamlit as st
import numpy as np
import plotly.graph_objects as go
from utils.localization import t
from views.styles import inject_equal_height_css
from utils.quiz_helper import render_mcq
from data.exam_questions import get_question
from utils.progress_tracker import track_question_answer, update_local_progress

# ==========================================
# CONTENT DICTIONARY
# ==========================================
content_3_5 = {
    "title": {"de": "3.5 Varianz", "en": "3.5 Variance"},
    "subtitle": {"de": "Wie breit ist deine Verteilung?", "en": "How spread out is your distribution?"},
    "intuition": {
        "header": {"de": "Die Intuition", "en": "The Intuition"},
        "text": {
            "de": "Stell dir zwei Bogenschützen vor: Beide zielen auf dieselbe Zielscheibe (gleiches μ). Aber Schütze A trifft in einem engen Cluster, Schütze B ist überall verstreut. Die **Varianz** misst genau das: Wie 'eng' oder 'breit' deine Schüsse um das Zentrum liegen.",
            "en": "Imagine two archers: Both aim at the same target (same μ). But Archer A hits in a tight cluster, Archer B is scattered everywhere. **Variance** measures exactly this: How 'tight' or 'spread' your shots are around the center."
        }
    },
    "theory": {
        "def_title": {"de": "Definition", "en": "Definition"},
        "def_text": {"de": "Erwartete quadrierte Abweichung vom Zentrum.", "en": "Expected squared deviation from the center."},
        "shift_title": {"de": "Verschiebungssatz", "en": "The Shortcut"},
        "shift_text": {"de": "Fast immer einfacher zu rechnen!", "en": "Almost always easier to calculate!"},
        "scale_title": {"de": "Skalierung", "en": "Scaling"},
        "scale_text": {"de": "Konstante kommt quadratisch raus!", "en": "Constant comes out squared!"},
        "add_title": {"de": "Verschiebung", "en": "Shifting"},
        "add_text": {"de": "Verschieben ändert die Breite nicht.", "en": "Shifting doesn't change the spread."}
    },
    "mission": {
        "title": {"de": "Mission: Der Scharfschütze", "en": "Mission: The Sharpshooter"},
        "desc": {
            "de": "Passe deine Präzision (σ) an, bis du das **Referenzmuster** triffst. Dein Ziel: **σ = 0.50**",
            "en": "Adjust your precision (σ) until you match the **reference pattern**. Your target: **σ = 0.50**"
        },
        "target_sigma": 0.50
    },
    "pro_tip": {
        "de": "Prüfungs-Hack: Siehst du E[X²] in der Aufgabe? Sofort den Verschiebungssatz anwenden: Var(X) = E[X²] - (E[X])². Das ist fast immer der schnellste Weg!",
        "en": "Exam hack: See E[X²] in the problem? Immediately use the shift formula: Var(X) = E[X²] - (E[X])². This is almost always the fastest approach!"
    }
}


def render_subtopic_3_5(model):
    """3.5 Variance - The Sharpshooter Design"""
    
    inject_equal_height_css()

    st.header(t(content_3_5["title"]))
    st.markdown(t(content_3_5["subtitle"]))
    st.markdown("---")
    
    # --- INTUITION ---
    with st.container(border=True):
        st.markdown(f"### {t(content_3_5['intuition']['header'])}")
        st.markdown(t(content_3_5['intuition']['text']))
    
    st.markdown("<br>", unsafe_allow_html=True)

    # --- SHARPSHOOTER MISSION ---
    render_sharpshooter_mission()

    st.markdown("<br>", unsafe_allow_html=True)

    # --- THEORY CARDS (2x2 Grid) ---
    st.markdown(f"### {t({'de': 'Die Formeln', 'en': 'The Formulas'})}")
    
    # Row 1: Definition + Shortcut
    c1, c2 = st.columns(2, gap="medium")
    with c1:
        with st.container(border=True):
            st.markdown(f"**{t(content_3_5['theory']['def_title'])}**")
            st.caption(t(content_3_5['theory']['def_text']))
            st.latex(r"Var(X) = E[(X - \mu)^2]")
            st.markdown("<br>", unsafe_allow_html=True)
            st.latex(r"\sigma = \sqrt{Var(X)}")
            st.caption(t({"de": "(gleiche Einheit wie X)", "en": "(same unit as X)"}))
    
    with c2:
        with st.container(border=True):
            st.markdown(f"**{t(content_3_5['theory']['shift_title'])}**")
            st.caption(t(content_3_5['theory']['shift_text']))
            st.latex(r"Var(X) = E[X^2] - (E[X])^2")
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown(t({"de": "\"E vom Quadrat minus Quadrat vom E\"", "en": "\"E of square minus square of E\""}))

    st.markdown("<br>", unsafe_allow_html=True)
    
    # Row 2: Scaling + Shifting
    c3, c4 = st.columns(2, gap="medium")
    with c3:
        with st.container(border=True):
            st.markdown(f"**{t(content_3_5['theory']['scale_title'])}**")
            st.caption(t(content_3_5['theory']['scale_text']))
            st.latex(r"Var(aX) = a^2 \cdot Var(X)")
    
    with c4:
        with st.container(border=True):
            st.markdown(f"**{t(content_3_5['theory']['add_title'])}**")
            st.caption(t(content_3_5['theory']['add_text']))
            st.latex(r"Var(X + b) = Var(X)")

    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- PRO TIP ---
    st.markdown(f"""
    <div style="background-color: #f4f4f5; border-radius: 8px; padding: 12px; color: #3f3f46;">
        <strong>Pro Tip:</strong> {t(content_3_5['pro_tip'])}
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # --- EXAM PRACTICE ---
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
                ai_context="Variance calculation",
                course_id="vwl", topic_id="3", subtopic_id="3.5", question_id="3_5_mc8"
            )


def render_sharpshooter_mission():
    """The Sharpshooter: Match the target pattern by adjusting σ"""
    
    st.markdown(f"### {t(content_3_5['mission']['title'])}")
    
    with st.container(border=True):
        st.markdown(t(content_3_5['mission']['desc']))
        st.markdown("---")
        
        # State
        if "sharp_done" not in st.session_state: st.session_state.sharp_done = False
        if "sharp_reset_count" not in st.session_state: st.session_state.sharp_reset_count = 0
        target_sigma = content_3_5['mission']['target_sigma']
        
        # Slider for user's sigma
        user_sigma = st.slider(
            t({"de": "Deine Präzision (σ)", "en": "Your Precision (σ)"}),
            0.1, 1.5, 0.8, 0.05,
            key=f"sharp_sigma_{st.session_state.sharp_reset_count}",
            disabled=st.session_state.sharp_done
        )
        
        # Generate shots using fixed seed for consistency
        np.random.seed(42)
        n_shots = 50
        
        # Reference pattern (target σ = 0.5)
        ref_x = np.random.normal(0, target_sigma, n_shots)
        ref_y = np.random.normal(0, target_sigma, n_shots)
        
        # User's pattern
        np.random.seed(123)
        user_x = np.random.normal(0, user_sigma, n_shots)
        user_y = np.random.normal(0, user_sigma, n_shots)
        
        # Two-column layout for targets
        c_user, c_ref = st.columns(2, gap="medium")
        
        with c_user:
            st.markdown(f"**{t({'de': 'Dein Muster', 'en': 'Your Pattern'})}**")
            fig_user = create_target_chart(user_x, user_y, "#007AFF", user_sigma)
            st.plotly_chart(fig_user, use_container_width=True, config={'displayModeBar': False}, key="user_target")
        
        with c_ref:
            st.markdown(f"**{t({'de': 'Referenz (Ziel)', 'en': 'Reference (Target)'})}**")
            fig_ref = create_target_chart(ref_x, ref_y, "#34C759", target_sigma)
            st.plotly_chart(fig_ref, use_container_width=True, config={'displayModeBar': False}, key="ref_target")
        
        # Stats and feedback
        c_stat1, c_stat2, c_stat3 = st.columns(3)
        
        with c_stat1:
            user_var = user_sigma ** 2
            st.metric(t({"de": "Deine Varianz", "en": "Your Variance"}), f"σ² = {user_var:.2f}")
        
        with c_stat2:
            target_var = target_sigma ** 2
            st.metric(t({"de": "Ziel-Varianz", "en": "Target Variance"}), f"σ² = {target_var:.2f}")
        
        with c_stat3:
            diff = abs(user_sigma - target_sigma)
            if diff < 0.02:  # Must be within ±0.01 of target
                if not st.session_state.sharp_done:
                    st.balloons()
                    st.session_state.sharp_done = True
                    user = st.session_state.get("user")
                    if user:
                        track_question_answer(user["localId"], "vwl", "3", "3.5", "3_5_sharpshooter", True)
                        update_local_progress("3", "3.5", "3_5_sharpshooter", True)
                        st.rerun()
                st.success(t({"de": "Volltreffer!", "en": "Bullseye!"}))
            else:
                if user_sigma < target_sigma:
                    st.info(t({"de": "Zu eng! Mehr streuen.", "en": "Too tight! Spread more."}))
                else:
                    st.info(t({"de": "Zu breit! Präziser zielen.", "en": "Too wide! Aim tighter."}))
        
        if st.session_state.sharp_done:
            if st.button(t({"de": "Nochmal spielen", "en": "Play again"}), key="reset_sharp"):
                st.session_state.sharp_done = False
                st.session_state.sharp_reset_count += 1  # Fresh slider key
                st.rerun()


def create_target_chart(x_vals, y_vals, color, sigma):
    """Create a target (bullseye) scatter chart"""
    
    fig = go.Figure()
    
    # Draw target rings
    for r in [0.5, 1.0, 1.5, 2.0]:
        theta = np.linspace(0, 2*np.pi, 100)
        fig.add_trace(go.Scatter(
            x=r * np.cos(theta), y=r * np.sin(theta),
            mode='lines', line=dict(color='rgba(0,0,0,0.15)', width=1),
            hoverinfo='skip', showlegend=False
        ))
    
    # Bullseye center
    fig.add_trace(go.Scatter(
        x=[0], y=[0], mode='markers',
        marker=dict(size=10, color='#FF3B30', symbol='x'),
        hoverinfo='skip', showlegend=False
    ))
    
    # Shots
    fig.add_trace(go.Scatter(
        x=x_vals, y=y_vals, mode='markers',
        marker=dict(size=8, color=color, opacity=0.7),
        hoverinfo='skip', showlegend=False
    ))
    
    fig.update_layout(
        xaxis=dict(range=[-2.5, 2.5], showgrid=False, zeroline=False, visible=False, 
                   scaleanchor="y", scaleratio=1, fixedrange=True),
        yaxis=dict(range=[-2.5, 2.5], showgrid=False, zeroline=False, visible=False, fixedrange=True),
        height=250,
        margin=dict(l=10, r=10, t=10, b=10),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )
    
    return fig
