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
                "text_de": "A: „Mindestens ein Würfel zeigt eine Sechs“",
                "text_en": "A: “At least one die shows a six”",
                "sol_de": r"Die Menge der günstigen Fälle ist $\{(1,6), (2,6), ..., (5,6), (6,6), (6,5), ..., (6,1)\}$. Das sind $6+5=11$ Ergebnisse. $$P(A) = \frac{11}{36}$$",
                "sol_en": r"The set of favorable cases is $\{(1,6), (2,6), ..., (5,6), (6,6), (6,5), ..., (6,1)\}$. These are $6+5=11$ outcomes. $$P(A) = \frac{11}{36}$$",
                "answer_key": ["11/36", "0.306", "0.3056", "30.56%"]
            },
            "B": {
                "text_de": "B: „Die Augenzahl beider Würfel ist gleich“",
                "text_en": "B: “The number of spots on both dice is the same”",
                "sol_de": r"Die Paare sind $\{(1,1), (2,2), (3,3), (4,4), (5,5), (6,6)\}$. Das sind 6 Ergebnisse. $$P(B) = \frac{6}{36} = \frac{1}{6}$$",
                "sol_en": r"The pairs are $\{(1,1), (2,2), (3,3), (4,4), (5,5), (6,6)\}$. These are 6 outcomes. $$P(B) = \frac{6}{36} = \frac{1}{6}$$",
                "answer_key": ["1/6", "6/36", "0.167", "16.7%"]
            },
            "C": {
                "text_de": "C: „Beide Würfel zeigen ungerade Zahlen“",
                "text_en": "C: “Both dice show odd numbers”",
                "sol_de": r"Ungerade Zahlen sind $\{1, 3, 5\}$. Es gibt 3 Möglichkeiten für Würfel 1 und 3 Möglichkeiten für Würfel 2. $3 \times 3 = 9$ Ergebnisse. $$P(C) = \frac{9}{36} = \frac{1}{4}$$",
                "sol_en": r"Odd numbers are $\{1, 3, 5\}$. There are 3 possibilities for die 1 and 3 possibilities for die 2. $3 \times 3 = 9$ outcomes. $$P(C) = \frac{9}{36} = \frac{1}{4}$$",
                 "answer_key": ["1/4", "9/36", "0.25", "25%"]
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
    TRANSPARENT = "rgba(0,0,0,0)"
    
    # Generate points for circles
    t_rad = np.linspace(0, 2*np.pi, 200)
    
    # Circle A points
    xa = 1 * np.cos(t_rad) - 0.6
    ya = 1 * np.sin(t_rad)
    
    # Circle B points
    xb = 1 * np.cos(t_rad) + 0.6
    yb = 1 * np.sin(t_rad)
    
    # Base Outlines (Always visible)
    fig.add_trace(go.Scatter(x=xa, y=ya, mode='lines', line=dict(color='black', width=2), name="A", hoverinfo='skip'))
    fig.add_trace(go.Scatter(x=xb, y=yb, mode='lines', line=dict(color='black', width=2), name="B", hoverinfo='skip'))
    
    # --- 2. HIGHLIGHT LOGIC ---
    if selection == "A":
        fig.add_trace(go.Scatter(x=xa, y=ya, fill="toself", fillcolor=APPLE_BLUE, line=dict(width=0), hoverinfo='skip'))
        
    elif selection == "B":
        fig.add_trace(go.Scatter(x=xb, y=yb, fill="toself", fillcolor=APPLE_BLUE, line=dict(width=0), hoverinfo='skip'))
        
    elif selection == "union": # A U B
        fig.add_trace(go.Scatter(x=xa, y=ya, fill="toself", fillcolor=APPLE_BLUE, line=dict(width=0), hoverinfo='skip'))
        fig.add_trace(go.Scatter(x=xb, y=yb, fill="toself", fillcolor=APPLE_BLUE, line=dict(width=0), hoverinfo='skip'))
        
    elif selection == "sect": # A n B (Intersection Lens)
        # Angles for Circle A (Center -0.6): Intersects at x=0 => cos = 0.6 => ~0.927 rad
        phi = np.linspace(-0.927, 0.927, 50) # -53 to 53 deg
        x_lens_a = 1 * np.cos(phi) - 0.6
        y_lens_a = 1 * np.sin(phi)
        
        # Angles for Circle B (Center 0.6): Intersects at x=0 => cos = -0.6 => 2.214 to 4.069 rad
        # We need the arc to the LEFT of x=0.
        theta = np.linspace(2.214, 4.069, 50) 
        x_lens_b = 1 * np.cos(theta) + 0.6
        y_lens_b = 1 * np.sin(theta)
        
        x_poly = np.concatenate([x_lens_a, x_lens_b])
        y_poly = np.concatenate([y_lens_a, y_lens_b])
        
        fig.add_trace(go.Scatter(x=x_poly, y=y_poly, fill="toself", fillcolor=APPLE_BLUE, line=dict(width=0), hoverinfo='skip'))

    elif selection == "diff": # A \ B
        fig.add_trace(go.Scatter(x=xa, y=ya, fill="toself", fillcolor=APPLE_BLUE, line=dict(width=0), hoverinfo='skip'))
        # White out B
        fig.add_trace(go.Scatter(x=xb, y=yb, fill="toself", fillcolor="#FFFFFF", line=dict(width=0), hoverinfo='skip'))
        # Redraw B outline on top
        fig.add_trace(go.Scatter(x=xb, y=yb, mode='lines', line=dict(color='black', width=2), hoverinfo='skip'))

    elif selection == "comp": # Comp A (Not A)
        # Box
        fig.add_trace(go.Scatter(
            x=[-3, 3, 3, -3, -3], 
            y=[-2, -2, 2, 2, -2], 
            fill="toself", 
            fillcolor=APPLE_BLUE, 
            line=dict(width=0), 
            hoverinfo='skip'
        ))
        # White out A
        fig.add_trace(go.Scatter(x=xa, y=ya, fill="toself", fillcolor="#FFFFFF", line=dict(width=0), hoverinfo='skip'))
        # Redraw A outline
        fig.add_trace(go.Scatter(x=xa, y=ya, mode='lines', line=dict(color='black', width=2), hoverinfo='skip'))
        # Redraw B outline
        fig.add_trace(go.Scatter(x=xb, y=yb, mode='lines', line=dict(color='black', width=2), hoverinfo='skip'))

    # Update Layout: FORCE SQUARE
    fig.update_layout(
        xaxis=dict(range=[-2.0, 2.0], visible=False, fixedrange=True),
        yaxis=dict(range=[-2.0, 2.0], visible=False, fixedrange=True),
        width=380,
        height=380,
        margin=dict(l=10, r=10, t=10, b=10),
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        showlegend=False
    )
    
    # Add text labels
    fig.add_annotation(x=-0.6, y=0, text="A", showarrow=False, font=dict(size=20, color="black"))
    fig.add_annotation(x=0.6, y=0, text="B", showarrow=False, font=dict(size=20, color="black"))
    
    return fig

def render_subtopic_1_2(model):
    st.header(t(content_1_2["title"]))
    st.caption(t(content_1_2["theory_intro"]))
    
    st.markdown("---")
    
    # --- THE UNIFIED CAPSULE ---
    with st.container(border=True):
        col_theory, col_vis = st.columns([1.2, 1], gap="large")

        # LEFT: The Content (Definitions)
        with col_theory:
            st.markdown(f"### {t(content_1_2['theory_header'])}")
            
            # Render definitions
            for key, def_data in content_1_2["definitions"].items():
                st.markdown(f"{def_data['title']}")
                st.markdown(t({"de": def_data["text_de"], "en": def_data["text_en"]}))
                st.markdown("---") # Thin separator

        # RIGHT: The Interaction (Visualization)
        with col_vis:
            st.markdown(f"**{t(content_1_2['interactive_header'])}**")
            
            # 1. Horizontal Pills via Radio (Mapped)
            # Keys: A, B, union, sect, diff, comp
            # We need to map the Display Label back to the Key.
            op_map = {
                "A": "A",
                "B": "B", 
                "A ∪ B": "union", 
                "A ∩ B": "sect", 
                "A \\ B": "diff", 
                "Ā": "comp"
            }
            op_options = list(op_map.keys())
            
            selected_label = st.radio(
                "Op", 
                op_options, 
                horizontal=True, 
                label_visibility="collapsed"
            )
            selected_key = op_map[selected_label]
            
            # 2. Square Diagram
            fig = get_venn_figure(selected_key)
            st.plotly_chart(fig, use_container_width=False, config={'displayModeBar': False})

    # --- THE EXAM WORKBENCH ---
    st.markdown("---")
    st.markdown(f"### 📝 {t(content_1_2['exam']['title'])}")
    st.markdown(f"*{content_1_2['exam']['source']}*")
    
    # Container with Divider logic is implied by standard container + css, 
    # but we can use st.container() and put content in it.
    with st.container():
        st.markdown(t(content_1_2["exam"]["question"]))
        
        tab_a, tab_b, tab_c = st.tabs(["Event A", "Event B", "Event C"])
        
        def render_exam_workbench(event_key):
            e_data = content_1_2["exam"]["events"][event_key]
            st.markdown(f"**{t({'de': e_data['text_de'], 'en': e_data['text_en']})}**")
            
            # Grading Logic
            # answer_key list contains valid strings
            user_input = st.text_input(t({"de": "Dein Ergebnis:", "en": "Your Result:"}), key=f"grad_1_2_{event_key}")
            
            is_correct = False
            if user_input:
                # Simple check
                if any(ans in user_input for ans in e_data.get("answer_key", [])):
                    st.success(t({"de": "Richtig!", "en": "Correct!"}))
                    is_correct = True
                else:
                    st.warning(t({"de": "Versuch es noch einmal.", "en": "Try again."}))
            
            # Show Solution Button
            btn_key = f"sol_btn_1_2_{event_key}"
            if f"{btn_key}_state" not in st.session_state:
                st.session_state[f"{btn_key}_state"] = False
                
            if st.button(t({"de": "Lösung zeigen", "en": "Show Solution"}), key=btn_key):
                st.session_state[f"{btn_key}_state"] = not st.session_state[f"{btn_key}_state"]
                
            if st.session_state[f"{btn_key}_state"] or is_correct:
                st.info(t({'de': e_data['sol_de'], 'en': e_data['sol_en']}))
                
                # AI Tutor (Only after solution is revealed)
                st.markdown("---")
                st.caption(t({"de": "Noch Fragen zur Lösung? Frag den AI Tutor.", "en": "Questions about the solution? Ask the AI Tutor."}))
                
                c_ai_1, c_ai_2 = st.columns([3, 1])
                with c_ai_1:
                    ai_q = st.text_area(t({"de": "Deine Frage:", "en": "Your Question:"}), key=f"ai_q_1_2_{event_key}", height=70)
                with c_ai_2:
                    st.markdown("<br>", unsafe_allow_html=True) # Spacer
                    if st.button(t({"de": "Erklären", "en": "Explain"}), key=f"ai_btn_1_2_{event_key}", type="primary"):
                        if model and ai_q:
                            with st.spinner("AI thinking..."):
                                prompt = f"Explain this statistics solution: {e_data['sol_en']} \nUser Question: {ai_q}"
                                try:
                                    response = model.generate_content(prompt)
                                    st.markdown(f"**AI:** {response.text}")
                                except Exception as e:
                                    st.error(f"AI Error: {e}")
                        elif not model:
                            st.error("AI Model not loaded.")

        with tab_a: render_exam_workbench("A")
        with tab_b: render_exam_workbench("B")
        with tab_c: render_exam_workbench("C")
