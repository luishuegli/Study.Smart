import streamlit as st
import plotly.graph_objects as go
import numpy as np
from views.styles import render_icon
from utils.localization import t

# 1. DATA STRUCTURE: THE BILINGUAL CONTENT
content_1_2 = {
    "title": {"de": "1.2 Das Rechnen mit Ereignissen", "en": "1.2 Calculating with Events"},
    "theory_header": {"de": "Mengenoperationen", "en": "Set Operations"},
    "theory_intro": {
        "de": "Wir rechnen nicht mit Zahlen, sondern mit Mengen (Ereignissen).",
        "en": "We do not calculate with numbers, but with sets (events)."
    },
    "ops": {
        "A": {"label": "A", "desc_de": "Ereignis A", "desc_en": "Event A"},
        "B": {"label": "B", "desc_de": "Ereignis B", "desc_en": "Event B"},
        "union": {"label": "A ∪ B", "desc_de": "Vereinigung (ODER)", "desc_en": "Union (OR)"},
        "sect":  {"label": "A ∩ B", "desc_de": "Schnittmenge (UND)", "desc_en": "Intersection (AND)"},
        "diff":  {"label": "A \\ B", "desc_de": "Differenz (A ohne B)", "desc_en": "Difference (A without B)"},
        "comp":  {"label": "Ā", "desc_de": "Komplement (Nicht A)", "desc_en": "Complement (Not A)"}
    },
     "definitions": {
        "union": {
            "title": "A ∪ B (Union / Vereinigung)",
            "text_de": "**ODER-Verknüpfung.** Das Element ist in A, in B oder in beiden.",
            "text_en": "**OR Operator.** The element is in A, in B, or in both."
        },
        "sect": {
            "title": "A ∩ B (Intersection / Schnitt)",
            "text_de": "**UND-Verknüpfung.** Das Element muss in A **und** gleichzeitig in B sein.",
            "text_en": "**AND Operator.** The element must be in A **and** simultaneously in B."
        },
        "diff": {
            "title": "A \\ B (Difference / Differenz)",
            "text_de": "Alles was in A ist, aber **nicht** in B.",
            "text_en": "Everything in A, but **not** in B."
        },
        "comp": {
            "title": "Ā (Complement / Komplement)",
            "text_de": "Alles im Ereignisraum S, was **nicht** in A liegt.",
            "text_en": "Everything in sample space S that is **not** in A."
        }
    },
    "interactive_header": {"de": "Interaktive Visualisierung", "en": "Interactive Visualization"},
    "exam": {
        "title": {"de": "Prüfungstraining: Aufgabe 1.2.1", "en": "Exam Practice: Problem 1.2.1"},
        "source": "Statistikskript Aufgabe 1.2.1 (4)",
        "question": {
            "de": r"Werfen von zwei Würfeln ($|S|=36$). Berechnen Sie die Wahrscheinlichkeit der folgenden Ereignisse:",
            "en": r"Throwing two dice ($|S|=36$). Calculate the probability of the following events:"
        },
        "events": {
            "A": {
                "text_de": "A: 'Mindestens ein Würfel zeigt eine Sechs'",
                "text_en": "A: 'At least one die shows a six'",
                "sol_de": r"Die Menge der günstigen Fälle ist $\{(1,6), (2,6), ..., (5,6), (6,6), (6,5), ..., (6,1)\}$. Das sind $6+5=11$ Ergebnisse. $$P(A) = \frac{11}{36}$$",
                "sol_en": r"The set of favorable cases is $\{(1,6), (2,6), ..., (5,6), (6,6), (6,5), ..., (6,1)\}$. These are $6+5=11$ outcomes. $$P(A) = \frac{11}{36}$$",
                "options": ["1/6", "11/36", "5/18", "1/2"],
                "correct_opt": "11/36"
            },
            "B": {
                "text_de": "B: 'Die Augenzahl beider Würfel ist gleich'",
                "text_en": "B: 'The number of spots on both dice is the same'",
                "sol_de": r"Die Paare sind $\{(1,1), (2,2), (3,3), (4,4), (5,5), (6,6)\}$. Das sind 6 Ergebnisse. $$P(B) = \frac{6}{36} = \frac{1}{6}$$",
                "sol_en": r"The pairs are $\{(1,1), (2,2), (3,3), (4,4), (5,5), (6,6)\}$. These are 6 outcomes. $$P(B) = \frac{6}{36} = \frac{1}{6}$$",
                "options": ["1/36", "1/6", "1/12", "1/2"],
                "correct_opt": "1/6"
            },
            "C": {
                "text_de": "C: 'Beide Würfel zeigen ungerade Zahlen'",
                "text_en": "C: 'Both dice show odd numbers'",
                "sol_de": r"Ungerade Zahlen sind $\{1, 3, 5\}$. Es gibt 3 Möglichkeiten für Würfel 1 und 3 Möglichkeiten für Würfel 2. $3 \times 3 = 9$ Ergebnisse. $$P(C) = \frac{9}{36} = \frac{1}{4}$$",
                "sol_en": r"Odd numbers are $\{1, 3, 5\}$. There are 3 possibilities for die 1 and 3 possibilities for die 2. $3 \times 3 = 9$ outcomes. $$P(C) = \frac{9}{36} = \frac{1}{4}$$",
                 "options": ["1/6", "1/4", "1/3", "1/2"],
                 "correct_opt": "1/4"
            }
        }
    }
}

def get_venn_figure(selection):
    """
    Generates the Plotly figure for the Venn Diagram.
    Circle A: (-0.6, 0), r=1
    Circle B: (0.6, 0), r=1
    """
    fig = go.Figure()
    
    # Constants
    APPLE_BLUE = "rgba(0, 122, 255, 0.4)"
    
    # Generate points for circles
    t_rad = np.linspace(0, 2*np.pi, 200)
    xa = 1 * np.cos(t_rad) - 0.6
    ya = 1 * np.sin(t_rad)
    xb = 1 * np.cos(t_rad) + 0.6
    yb = 1 * np.sin(t_rad)
    
    # Base Outlines (Always visible)
    fig.add_trace(go.Scatter(x=xa, y=ya, mode='lines', line=dict(color='black', width=2), name="A", hoverinfo='skip'))
    fig.add_trace(go.Scatter(x=xb, y=yb, mode='lines', line=dict(color='black', width=2), name="B", hoverinfo='skip'))
    
    # Highlight Logic
    if selection == "A":
        fig.add_trace(go.Scatter(x=xa, y=ya, fill="toself", fillcolor=APPLE_BLUE, line=dict(width=0), hoverinfo='skip'))
    elif selection == "B":
        fig.add_trace(go.Scatter(x=xb, y=yb, fill="toself", fillcolor=APPLE_BLUE, line=dict(width=0), hoverinfo='skip'))
    elif selection == "union":
        fig.add_trace(go.Scatter(x=xa, y=ya, fill="toself", fillcolor=APPLE_BLUE, line=dict(width=0), hoverinfo='skip'))
        fig.add_trace(go.Scatter(x=xb, y=yb, fill="toself", fillcolor=APPLE_BLUE, line=dict(width=0), hoverinfo='skip'))
    elif selection == "sect":
        phi = np.linspace(-0.927, 0.927, 50)
        x_lens_a = 1 * np.cos(phi) - 0.6
        y_lens_a = 1 * np.sin(phi)
        theta = np.linspace(2.214, 4.069, 50) 
        x_lens_b = 1 * np.cos(theta) + 0.6
        y_lens_b = 1 * np.sin(theta)
        x_poly = np.concatenate([x_lens_a, x_lens_b])
        y_poly = np.concatenate([y_lens_a, y_lens_b])
        fig.add_trace(go.Scatter(x=x_poly, y=y_poly, fill="toself", fillcolor=APPLE_BLUE, line=dict(width=0), hoverinfo='skip'))
    elif selection == "diff":
        fig.add_trace(go.Scatter(x=xa, y=ya, fill="toself", fillcolor=APPLE_BLUE, line=dict(width=0), hoverinfo='skip'))
        fig.add_trace(go.Scatter(x=xb, y=yb, fill="toself", fillcolor="#FFFFFF", line=dict(width=0), hoverinfo='skip'))
        fig.add_trace(go.Scatter(x=xb, y=yb, mode='lines', line=dict(color='black', width=2), hoverinfo='skip'))
    elif selection == "comp":
        fig.add_trace(go.Scatter(x=[-3, 3, 3, -3, -3], y=[-2, -2, 2, 2, -2], fill="toself", fillcolor=APPLE_BLUE, line=dict(width=0), hoverinfo='skip'))
        fig.add_trace(go.Scatter(x=xa, y=ya, fill="toself", fillcolor="#FFFFFF", line=dict(width=0), hoverinfo='skip'))
        fig.add_trace(go.Scatter(x=xa, y=ya, mode='lines', line=dict(color='black', width=2), hoverinfo='skip'))
        fig.add_trace(go.Scatter(x=xb, y=yb, mode='lines', line=dict(color='black', width=2), hoverinfo='skip'))

    fig.update_layout(
        xaxis=dict(range=[-2.0, 2.0], visible=False), 
        yaxis=dict(range=[-2.0, 2.0], visible=False), 
        width=450, 
        height=450, 
        margin=dict(l=10, r=10, t=10, b=10), 
        plot_bgcolor="rgba(0,0,0,0)", 
        paper_bgcolor="rgba(0,0,0,0)", 
        showlegend=False
    )
    fig.add_annotation(x=-0.6, y=0, text="A", showarrow=False, font=dict(size=20, color="black"))
    fig.add_annotation(x=0.6, y=0, text="B", showarrow=False, font=dict(size=20, color="black"))
    return fig

def render_subtopic_1_2(model):
    st.header(t(content_1_2["title"]))
    st.caption(t(content_1_2["theory_intro"]))
    st.markdown("---")
    
    # --- THE UNIFIED CAPSULE (Improved Spacing) ---
    with st.container(border=True):
        col_theory, col_vis = st.columns([1, 1.3], gap="large")
        
        with col_theory:
            st.markdown(f"### {t(content_1_2['theory_header'])}")
            st.markdown("")  # Breathing room
            
            # Render definitions with better spacing
            for key, def_data in content_1_2["definitions"].items():
                st.markdown(f"**{def_data['title']}**")
                st.markdown(t({"de": def_data["text_de"], "en": def_data["text_en"]}))
                st.markdown("")  # Space between definitions instead of divider
                st.markdown("")  # Extra space for clarity

        with col_vis:
            st.markdown(f"**{t(content_1_2['interactive_header'])}**")
            st.markdown("")  # Breathing room
            
            # Horizontal Pills via Radio
            op_map = {"A": "A", "B": "B", "A ∪ B": "union", "A ∩ B": "sect", "A \\ B": "diff", "Ā": "comp"}
            selected_label = st.radio(
                "Op", 
                list(op_map.keys()), 
                horizontal=True, 
                label_visibility="collapsed"
            )
            
            st.markdown("")  # Space before diagram
            
            # Square Diagram (Larger for better visibility)
            fig = get_venn_figure(op_map[selected_label])
            st.plotly_chart(fig, use_container_width=False, config={'displayModeBar': False})

    # --- THE EXAM WORKBENCH ---
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown(f"### {t(content_1_2['exam']['title'])}")
    st.markdown(f"*{content_1_2['exam']['source']}*")
    st.markdown("")  # Space before container
    
    with st.container(border=True):
        st.markdown(t(content_1_2["exam"]["question"]))
        st.markdown("")  # Space before tabs
        
        tab_a, tab_b, tab_c = st.tabs(["Event A", "Event B", "Event C"])
        
        def render_exam_workbench(event_key):
            e_data = content_1_2["exam"]["events"][event_key]
            st.markdown(f"**{t({'de': e_data['text_de'], 'en': e_data['text_en']})}**")
            st.markdown("")  # Space before MCQ
            
            # Multiple Choice Input
            radio_key = f"mcq_1_2_{event_key}"
            user_selection = st.radio(
                t({"de": "Wähle:", "en": "Select:"}),
                e_data["options"],
                key=radio_key,
                index=None,
            )
            
            # Check correctness
            if user_selection:
                if user_selection == e_data["correct_opt"]:
                    st.success(t({"de": "Richtig!", "en": "Correct!"}))
                else:
                    st.error(t({"de": "Falsch.", "en": "Incorrect."}))
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            # Show Solution Button
            btn_key = f"sol_btn_1_2_{event_key}"
            if f"{btn_key}_state" not in st.session_state:
                st.session_state[f"{btn_key}_state"] = False
                
            if st.button(t({"de": "Lösung zeigen", "en": "Show Solution"}), key=btn_key):
                st.session_state[f"{btn_key}_state"] = not st.session_state[f"{btn_key}_state"]
                
            if st.session_state[f"{btn_key}_state"]:
                st.markdown("")  # Space before solution
                
                # Nested Box for Solution
                with st.container(border=True):
                    st.info(t({'de': e_data['sol_de'], 'en': e_data['sol_en']}))
                    
                    st.markdown("---")
                    st.caption(t({"de": "AI Tutor:", "en": "AI Tutor:"}))
                    
                    c_ai_1, c_ai_2 = st.columns([4, 1])
                    with c_ai_1:
                        ai_q = st.text_input(
                            t({"de": "Frage:", "en": "Question:"}), 
                            key=f"ai_q_1_2_{event_key}", 
                            placeholder=t({"de": "Was ist unklar?", "en": "What is unclear?"}),
                            label_visibility="collapsed"
                        )
                    with c_ai_2:
                        if st.button(t({"de": "Ask", "en": "Ask"}), key=f"ai_btn_1_2_{event_key}", type="primary", use_container_width=True):
                            if model and ai_q:
                                with st.spinner("..."):
                                    prompt = f"Explain this statistics solution: {e_data['sol_en']} \nUser Question: {ai_q}"
                                    try:
                                        response = model.generate_content(prompt)
                                        st.markdown(f"**AI:** {response.text}")
                                    except Exception as e:
                                        st.error(f"Error: {e}")
                            elif not model:
                                st.error("Model unavailable")

        with tab_a: render_exam_workbench("A")
        with tab_b: render_exam_workbench("B")
        with tab_c: render_exam_workbench("C")
