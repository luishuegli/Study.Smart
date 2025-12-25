import streamlit as st
import plotly.graph_objects as go
import numpy as np
from utils.localization import t
from views.styles import render_icon
from utils.localization import t
from utils.ai_helper import render_ai_tutor
from utils.quiz_helper import render_mcq
import random

# 1. THE CONTENT DICTIONARY (Rosetta Stone Protocol)
content_1_3 = {
    "title": {"de": "1.3 Der Wahrscheinlichkeitsbegriff", "en": "1.3 The Concept of Probability"},
    "theory_header": {"de": "Definitionen", "en": "Definitions"},
    "intro": {
        "de": "Was bedeutet 'Wahrscheinlichkeit' eigentlich? Es gibt zwei Sichtweisen:",
        "en": "What does 'probability' actually mean? There are two perspectives:"
    },
    "definitions": {
        "laplace": {
            "title_de": "1. Laplace (Klassisch)",
            "title_en": "1. Laplace (Classical)",
            "subtitle_de": "Das 'faire' Prinzip",
            "subtitle_en": "The 'Fair' Principle",
            "text_de": "Wenn der Ereignisraum endlich ist und alle Ergebnisse **gleich wahrscheinlich** sind.",
            "text_en": "When the sample space is finite and all outcomes are **equally likely**.",
            # FORMULA LOCALIZED
            "formula_de": r"P(A) = \frac{|A|}{|S|} = \frac{\text{Günstig}}{\text{Möglich}}",
            "formula_en": r"P(A) = \frac{|A|}{|S|} = \frac{\text{Favorable}}{\text{Possible}}"
        },
        "freq": {
            "title_de": "2. Frequentistisch (Statistisch)",
            "title_en": "2. Frequentist (Statistical)",
            "subtitle_de": "Das 'Experimentator'-Prinzip",
            "subtitle_en": "The 'Experimenter' Principle",
            "text_de": "Wahrscheinlichkeit ist der Grenzwert der relativen Häufigkeit bei unendlicher Wiederholung.",
            "text_en": "Probability is the limit of relative frequency over infinite repetitions.",
            "formula": r"P(A) = \lim_{n \to \infty} \frac{k}{n}"
        }
    },
    "vis_header": {"de": "Gesetz der großen Zahlen", "en": "Law of Large Numbers"},
    "vis_desc": {
        "de": "Simuliere Würfelwürfe. Beobachte, wie sich die Balken der theoretischen Linie (16.7%) annähern.",
        "en": "Simulate dice rolls. Watch how the bars converge to the theoretical line (16.7%)."
    },
    "vis_note": {
        "de": "**Beachte:** Bei wenigen Würfen schwanken die Balken stark. Erst bei sehr vielen Würfen ($n \\to \\infty$) stabilisiert sich die Verteilung.",
        "en": "**Note:** With few rolls, the bars fluctuate wildly. Only with many rolls ($n \\to \\infty$) does the distribution stabilize."
    },
    "exam": {
        "title": {"de": "Konzept-Check", "en": "Concept Check"},
        "source": "Selbst erstellt / Self-created",
        "question": {
            "de": r"**$\text{Wann darf man die Laplace-Formel } P(A) = \frac{g}{m} \text{ verwenden?}$**",
            "en": r"**$\text{When are you allowed to use the Laplace formula } P(A) = \frac{g}{m}?$**"
        },
        "options": [
            {"id": "a", "de": "Immer.", "en": "Always."},
            {"id": "b", "de": "Nur bei unendlich vielen Ergebnissen.", "en": "Only with infinite outcomes."},
            {"id": "c", "de": "Nur wenn der Ereignisraum endlich ist und alle Elementarereignisse gleich wahrscheinlich sind.", "en": "Only if the sample space is finite and all elementary events are equally likely."},
            {"id": "d", "de": "Nur wenn man empirische Daten hat.", "en": "Only if you have empirical data."}
        ],
        "correct_id": "c",
        "solution": {
            "de": "**Richtig! (c)**<br>Das 'Indifferenzprinzip' ist entscheidend. Bei einem gezinkten Würfel (ungleiche Wahrscheinlichkeiten) funktioniert Laplace nicht.",
            "en": "**Correct (c)**<br>The 'Principle of Indifference' is crucial. Laplace does not work for loaded dice (unequal probabilities)."
        }
    }
}

def update_rolls(n):
    """Simulate n rolls and update session state."""
    if "rolls_1_3" not in st.session_state:
        st.session_state.rolls_1_3 = {i: 0 for i in range(1, 7)}
        st.session_state.total_rolls_1_3 = 0
    
    new_rolls = np.random.randint(1, 7, size=n)
    for roll in new_rolls:
        st.session_state.rolls_1_3[roll] += 1
    
    st.session_state.total_rolls_1_3 += n

def reset_rolls():
    """Reset the simulation."""
    st.session_state.rolls_1_3 = {i: 0 for i in range(1, 7)}
    st.session_state.total_rolls_1_3 = 0

def get_freq_chart():
    """Generate the Plotly bar chart for relative frequencies."""
    
    # Calculate frequencies
    total = st.session_state.total_rolls_1_3
    if total > 0:
        y_data = [st.session_state.rolls_1_3[i] / total for i in range(1, 7)]
    else:
        y_data = [0] * 6
    
    x_data = list(range(1, 7))
    
    # DISTINCT COLORS PALETTE (Apple-ish)
    colors = [
        "rgba(255, 59, 48, 0.7)",   # Red
        "rgba(255, 149, 0, 0.7)",   # Orange
        "rgba(255, 204, 0, 0.7)",   # Yellow
        "rgba(52, 199, 89, 0.7)",   # Green
        "rgba(0, 199, 190, 0.7)",   # Teal
        "rgba(0, 122, 255, 0.7)"    # Blue
    ]
    border_colors = [c.replace("0.7", "1.0") for c in colors]
    
    fig = go.Figure()
    
    # 1. The Bars (Actual Data)
    fig.add_trace(go.Bar(
        x=x_data,
        y=y_data,
        name=t({"de": "Häufigkeit", "en": "Frequency"}),
        marker_color=colors, 
        marker_line_color=border_colors,
        marker_line_width=1.5
    ))
    
    # 2. The Theoretical Line (1/6 = 0.16666...)
    fig.add_shape(
        type="line",
        x0=0.5, y0=1/6, x1=6.5, y1=1/6,
        line=dict(color="black", width=2, dash="dash"),
    )
    
    # Annotation for the line
    fig.add_annotation(
        x=6.5, y=1/6,
        xref="x", yref="y",
        text="16.7%",
        showarrow=False,
        yshift=10,
        font=dict(color="black", size=10)
    )

    # Layout Styling
    fig.update_layout(
        xaxis=dict(
            tickmode='linear', 
            tick0=1, 
            dtick=1, 
            showgrid=False,
            title=t({"de": "Würfelaugen", "en": "Dice Face"})
        ),
        yaxis=dict(
            range=[0, 1.05], 
            showgrid=False,
            visible=True,
            title=t({"de": "Relative Anteile", "en": "Relative Proportion"})
        ),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=10, r=10, t=30, b=10),
        height=350,
        showlegend=False,
        title=dict(
            text=f"n = {total}",
            x=0.5,
            xanchor='center',
            font=dict(size=14)
        )
    )
    
    if total > 0:
        max_val = max(y_data)
        upper_limit = max(max_val, 0.2) * 1.2 
        upper_limit = min(upper_limit, 1.0)
        fig.update_layout(yaxis_range=[0, upper_limit])

    return fig

def render_subtopic_1_3(model):
    # Initialize State
    if "rolls_1_3" not in st.session_state:
        reset_rolls()

    # --- HEADER ---
    st.header(t(content_1_3["title"]))
    st.markdown("---")

    # --- UNIFIED CAPSULE ---
    with st.container(border=True):
        
        # 1. Full Width Intro (Fixes "Horizontal Width" issue)
        st.markdown(f"### {t(content_1_3['theory_header'])}")
        st.markdown(t(content_1_3["intro"]))
        st.markdown("<br>", unsafe_allow_html=True)

        # 2. Columns (Left: Cards, Right: Sim)
        # With wider page, we can balance this better: [1, 1.6]
        col_theory, col_vis = st.columns([1, 1.6], gap="medium")
        
        # --- LEFT: THEORY CARDS ---
        with col_theory:
            # Card 1: Laplace
            with st.container(border=True):
                c = content_1_3["definitions"]["laplace"]
                st.markdown(f"**{t({'de': c['title_de'], 'en': c['title_en']})}**")
                st.caption(t({'de': c['subtitle_de'], 'en': c['subtitle_en']}))
                st.markdown(t({'de': c['text_de'], 'en': c['text_en']}))
                
                # Check for localized formula key
                f_key = "formula_de" if st.session_state.lang == 'de' else "formula_en"
                st.latex(c.get(f_key, c.get("formula", ""))) # Fallback

            st.markdown("<br>", unsafe_allow_html=True)

            # Card 2: Frequentist
            with st.container(border=True):
                c = content_1_3["definitions"]["freq"]
                st.markdown(f"**{t({'de': c['title_de'], 'en': c['title_en']})}**")
                st.caption(t({'de': c['subtitle_de'], 'en': c['subtitle_en']}))
                st.markdown(t({'de': c['text_de'], 'en': c['text_en']}))
                st.latex(c["formula"]) # No localization needed for this one

        # --- RIGHT: VISUALIZATION ---
        with col_vis:
            # Force alignment with CSS hack to remove top margin of the header so it aligns with the card border
            st.markdown("""
                <style>
                h3 { margin-top: 0 !important; padding-top: 0 !important; }
                </style>
            """, unsafe_allow_html=True)
            
            st.markdown(f"### {t(content_1_3['vis_header'])}")
            st.caption(t(content_1_3["vis_desc"]))
            
            # Controls: Equal width now to prevent squeezes
            c1, c2, c3, c4 = st.columns(4) 
            with c1:
                # FIX: st.button does not support SVG/HTML in label. Use text.
                if st.button(t({"de": "Reset", "en": "Reset"}), key="reset_1_3", type="secondary", use_container_width=True):
                    reset_rolls()
                    st.rerun()
            with c2:
                if st.button("+1", key="add_1_1_3", type="primary", use_container_width=True):
                    update_rolls(1)
                    st.rerun()
            with c3:
                if st.button("+10", key="add_10_1_3", type="primary", use_container_width=True):
                    update_rolls(10)
                    st.rerun()
            with c4:
                if st.button("+100", key="add_100_1_3", type="primary", use_container_width=True):
                    update_rolls(100)
                    st.rerun()
            
            # Chart
            fig = get_freq_chart()
            st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
            
            # Additional Note (No Emoji)
            st.info(t(content_1_3["vis_note"]))

    # --- EXAM WORKBENCH ---
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown(f"### {t(content_1_3['exam']['title'])}")
    st.caption(content_1_3['exam']['source'])
    
    with st.container(border=True):
        # Prepare Options
        opts = content_1_3["exam"]["options"]
        opt_labels = [t({"de": o["de"], "en": o["en"]}) for o in opts]
        
        # Calculate correct index
        correct_id = content_1_3["exam"]["correct_id"]
        correct_idx = next((i for i, o in enumerate(opts) if o["id"] == correct_id), 0)
        
        render_mcq(
            key_suffix="1_3_exam",
            question_text=t(content_1_3["exam"]["question"]),
            options=opt_labels,
            correct_idx=correct_idx,
            solution_text_dict=content_1_3["exam"]["solution"],
            success_msg_dict={"de": "Korrekt", "en": "Correct"},
            error_msg_dict={"de": "Das stimmt nicht ganz.", "en": "That is not quite right."},
            model=model,
            ai_context="Context: Probability definitions (Laplace vs Frequentist).",
            allow_retry=False,
            course_id="vwl",
            topic_id="1",
            subtopic_id="1.3",
            question_id="1_3_exam"
        )
