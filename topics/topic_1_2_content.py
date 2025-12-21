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
    "exam": {
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
                "sol_en": r"The set of favorable cases is $\{(1,6), (2,6), ..., (5,6), (6,6), (6,5), ..., (6,1)\}$. These are $6+5=11$ outcomes. $$P(A) = \frac{11}{36}$$"
            },
            "B": {
                "text_de": "B: „Die Augenzahl beider Würfel ist gleich“",
                "text_en": "B: “The number of spots on both dice is the same”",
                "sol_de": r"Die Paare sind $\{(1,1), (2,2), (3,3), (4,4), (5,5), (6,6)\}$. Das sind 6 Ergebnisse. $$P(B) = \frac{6}{36} = \frac{1}{6}$$",
                "sol_en": r"The pairs are $\{(1,1), (2,2), (3,3), (4,4), (5,5), (6,6)\}$. These are 6 outcomes. $$P(B) = \frac{6}{36} = \frac{1}{6}$$"
            },
            "C": {
                "text_de": "C: „Beide Würfel zeigen ungerade Zahlen“",
                "text_en": "C: “Both dice show odd numbers”",
                "sol_de": r"Ungerade Zahlen sind $\{1, 3, 5\}$. Es gibt 3 Möglichkeiten für Würfel 1 und 3 Möglichkeiten für Würfel 2. $3 \times 3 = 9$ Ergebnisse. $$P(C) = \frac{9}{36} = \frac{1}{4}$$",
                "sol_en": r"Odd numbers are $\{1, 3, 5\}$. There are 3 possibilities for die 1 and 3 possibilities for die 2. $3 \times 3 = 9$ outcomes. $$P(C) = \frac{9}{36} = \frac{1}{4}$$"
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
    
    # --- 1. DEFINE SHAPES ---
    # We use scatter traces for fills to control hovering and legends better,
    # or shape layers for static outlines.
    
    # Constants
    APPLE_BLUE = "rgba(0, 122, 255, 0.4)"
    APPLE_BLUE_SOLID = "rgba(0, 122, 255, 1.0)"
    TRANSPARENT = "rgba(0,0,0,0)"
    
    # Generate points for circles
    t = np.linspace(0, 2*np.pi, 200)
    
    # Circle A points
    xa = 1 * np.cos(t) - 0.6
    ya = 1 * np.sin(t)
    
    # Circle B points
    xb = 1 * np.cos(t) + 0.6
    yb = 1 * np.sin(t)
    
    # Base Outlines (Always visible)
    fig.add_trace(go.Scatter(x=xa, y=ya, mode='lines', line=dict(color='black', width=2), name="A", hoverinfo='skip'))
    fig.add_trace(go.Scatter(x=xb, y=yb, mode='lines', line=dict(color='black', width=2), name="B", hoverinfo='skip'))
    
    # --- 2. HIGHLIGHT LOGIC ---
    
    if selection == "A":
        # Fill A
        fig.add_trace(go.Scatter(x=xa, y=ya, fill="toself", fillcolor=APPLE_BLUE, line=dict(width=0), hoverinfo='skip'))
        
    elif selection == "B":
        # Fill B
        fig.add_trace(go.Scatter(x=xb, y=yb, fill="toself", fillcolor=APPLE_BLUE, line=dict(width=0), hoverinfo='skip'))
        
    elif selection == "union": # A U B
        # Fill A and Fill B
        # We can just fill both circles.
        fig.add_trace(go.Scatter(x=xa, y=ya, fill="toself", fillcolor=APPLE_BLUE, line=dict(width=0), hoverinfo='skip'))
        fig.add_trace(go.Scatter(x=xb, y=yb, fill="toself", fillcolor=APPLE_BLUE, line=dict(width=0), hoverinfo='skip'))
        
    elif selection == "sect": # A n B (Intersection)
        # Calculate intersection shape (Lens)
        # Left boundary: Arc of B (Right Circle) for x < 0
        # Right boundary: Arc of A (Left Circle) for x > 0
        
        # Angles for Circle A (Center -0.6): Intersects at x=0 => cos = 0.6 => ~53.13 deg
        # We need the arc to the RIGHT of x=0. So from -53 to +53.
        phi = np.linspace(-0.927, 0.927, 50) # -53 to 53 deg
        x_lens_a = 1 * np.cos(phi) - 0.6
        y_lens_a = 1 * np.sin(phi)
        
        # Angles for Circle B (Center 0.6): Intersects at x=0 => cos = -0.6 => ~126.87 deg
        # We need the arc to the LEFT of x=0. So from 127 to 233.
        # 126.87 deg = 2.214 rad.
        # We go from top intersection (approx 127) to bottom (approx 233).
        theta = np.linspace(2.214, 4.069, 50) 
        x_lens_b = 1 * np.cos(theta) + 0.6
        y_lens_b = 1 * np.sin(theta)
        
        # Combine to polygon
        # A goes bottom to top (if linspace - to +). B goes top to bottom (if linspace + to -).
        # Let's order effectively:
        # A arc: -53 to 53 (Bottom to Top)
        # B arc: 127 to 233? Wait. 
        # B center is 0.6. x=0 is left side.
        # Top intersection: (0, 0.8). Bottom: (0, -0.8).
        # Angle for top on B: atan2(0.8, -0.6) = 126.8 deg
        # Angle for bottom on B: atan2(-0.8, -0.6) = -126.8 deg or 233 deg.
        # We need arc from Top to Bottom? Or Bottom to Top?
        # A goes Bottom -> Top. B needs to go Top -> Bottom to close loop.
        
        x_poly = np.concatenate([x_lens_a, x_lens_b])
        y_poly = np.concatenate([y_lens_a, y_lens_b])
        
        fig.add_trace(go.Scatter(x=x_poly, y=y_poly, fill="toself", fillcolor=APPLE_BLUE, line=dict(width=0), hoverinfo='skip'))

    elif selection == "diff": # A \ B
        # Circle A minus Intersection.
        # Or just Fill A, but whiteout B?
        # Better: Polygon A without lens.
        # Arc of A from 53 to 307 (-53). (Large arc)
        # Arc of B from -127 to 127 (Left side of B? No, The boundary is the same arc as intersection but reversed).
        
        # Easier visual trick: Fill A Blue, Fill Intersection White (or Background Color)?
        # Background is white.
        fig.add_trace(go.Scatter(x=xa, y=ya, fill="toself", fillcolor=APPLE_BLUE, line=dict(width=0), hoverinfo='skip'))
        
        # White out B
        # But B outline needs to be visible.
        # Actually, Fill B with WHITE (and opaque).
        fig.add_trace(go.Scatter(x=xb, y=yb, fill="toself", fillcolor="#FFFFFF", line=dict(width=0), hoverinfo='skip'))
        
        # Redraw B outline on top
        fig.add_trace(go.Scatter(x=xb, y=yb, mode='lines', line=dict(color='black', width=2), hoverinfo='skip'))

    elif selection == "comp": # Comp A (Not A)
        # Everything except A.
        # Box from -2 to 2 filled Blue.
        # Circle A filled White.
        
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


    # Layout configs
    fig.update_layout(
        xaxis=dict(range=[-2.5, 2.5], visible=False, fixedrange=True),
        yaxis=dict(range=[-1.5, 1.5], visible=False, fixedrange=True),
        width=400,
        height=300,
        margin=dict(l=0, r=0, t=20, b=0),
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        showlegend=False
    )
    
    # Add text labels
    fig.add_annotation(x=-0.6, y=0, text="A", showarrow=False, font=dict(size=20, color="black"))
    fig.add_annotation(x=0.6, y=0, text="B", showarrow=False, font=dict(size=20, color="black"))
    
    return fig

def render_subtopic_1_2():
    st.header(t(content_1_2["title"]))
    st.caption(t(content_1_2["theory_intro"]))
    
    st.markdown("---")
    
    # 2. THE LAYOUT (Unified Capsule)
    with st.container(border=True):
        st.subheader(t(content_1_2["theory_header"]))
        
        col_theory, col_vis = st.columns([1, 1.5], gap="large")
        
        with col_theory:
            # Operation Selector moved here for logical flow? 
            # Or stick to prompt: "Right (Visual): Selector... Graph"
            # Prompt says Selector is on Right.
            
            # Display Definitions
            for key, val in content_1_2["ops"].items():
                if key in ["A", "B"]: continue # Skip single sets in defs
                
                # Check if this operation is selected to highlight text?
                # Maybe later. For now just list them.
                st.markdown(f"**{val['label']}**: {t({'de': val['desc_de'], 'en': val['desc_en']})}")
                st.markdown("<br>", unsafe_allow_html=True)

        with col_vis:
            # Selector
            op_options = ["A", "B", "union", "sect", "diff", "comp"]
            op_labels = {
                "A": "A",
                "B": "B",
                "union": "A ∪ B",
                "sect": "A ∩ B",
                "diff": "A \\ B",
                "comp": "Ā (Not A)"
            }
            
            selected_op_key = st.radio(
                "Operation",
                op_options,
                format_func=lambda x: op_labels[x],
                horizontal=True,
                label_visibility="collapsed"
            )
            
            # Graph
            fig = get_venn_figure(selected_op_key)
            st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})

    st.markdown("<br>", unsafe_allow_html=True)

    # 4. THE EXAM DRAWER
    with st.expander(t({"de": "📝 Prüfungstraining: Aufgabe 1.2.1", "en": "📝 Exam Practice: Problem 1.2.1"}), expanded=False):
        st.markdown(f"*{content_1_2['exam']['source']}*")
        st.markdown(t(content_1_2["exam"]["question"]))
        
        tab_a, tab_b, tab_c = st.tabs(["Event A", "Event B", "Event C"])
        
        # Helper for Tabs
        def render_exam_tab(event_key):
            e_data = content_1_2["exam"]["events"][event_key]
            st.markdown(f"**{t({'de': e_data['text_de'], 'en': e_data['text_en']})}**")
            
            btn_key = f"sol_btn_1_2_{event_key}"
            if f"{btn_key}_state" not in st.session_state:
                st.session_state[f"{btn_key}_state"] = False
                
            if st.button(t({"de": "Lösung zeigen", "en": "Show Solution"}), key=btn_key):
                st.session_state[f"{btn_key}_state"] = not st.session_state[f"{btn_key}_state"]
                
            if st.session_state[f"{btn_key}_state"]:
                st.info(t({'de': e_data['sol_de'], 'en': e_data['sol_en']}))

        with tab_a: render_exam_tab("A")
        with tab_b: render_exam_tab("B")
        with tab_c: render_exam_tab("C")
