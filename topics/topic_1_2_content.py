import streamlit as st
import plotly.graph_objects as go
import numpy as np
from views.styles import render_icon
from utils.localization import t
from utils.ai_helper import render_ai_tutor
from utils.quiz_helper import render_mcq, render_tab_progress_css
from data.exam_questions import get_question

# 1. DATA STRUCTURE: BALANCED CONTENT
content_1_2 = {
    "title": {"de": "1.2 Das Rechnen mit Ereignissen", "en": "1.2 Calculating with Events"},
    "theory_header": {"de": "Mengenoperationen", "en": "Set Operations"},
    "theory_intro": {
        "de": "Wir rechnen nicht mit Zahlen, sondern mit Mengen (Ereignissen).",
        "en": "We do not calculate with numbers, but with sets (events)."
    },
    "definitions": {
        "union": {
            "symbol": "A ∪ B",
            "title_de": "Vereinigung",
            "title_en": "Union",
            "def_de": "ODER-Verknüpfung. Das Element ist in $A, B$ oder in beiden.",
            "def_en": "OR Operator. The element is in $A, B$, or in both.",
            "example_de": r"$\text{Wenn } A=\{1,2\} \text{ und } B=\{2,3\}$" + "\n\n" + r"$\rightarrow A \cup B = \{1,2,3\}$",
            "example_en": r"$\text{If } A=\{1,2\} \text{ and } B=\{2,3\}$" + "\n\n" + r"$\rightarrow A \cup B = \{1,2,3\}$"
        },
        "sect": {
            "symbol": "A ∩ B",
            "title_de": "Schnittmenge",
            "title_en": "Intersection",
            "def_de": "UND-Verknüpfung. Das Element muss in $A$ und $B$ sein.",
            "def_en": "AND Operator. The element must be in $A$ and $B$.",
            "example_de": r"$\text{Wenn } A=\{1,2\} \text{ und } B=\{2,3\}$" + "\n\n" + r"$\rightarrow A \cap B = \{2\}$",
            "example_en": r"$\text{If } A=\{1,2\} \text{ and } B=\{2,3\}$" + "\n\n" + r"$\rightarrow A \cap B = \{2\}$"
        },
        "diff": {
            "symbol": "A \\ B",
            "title_de": "Differenz",
            "title_en": "Difference",
            "def_de": "Alles was in $A$ ist, aber nicht in $B$.",
            "def_en": "Everything in $A$, but not in $B$.",
            "example_de": r"$\text{Wenn } A=\{1,2\}, B=\{2,3\}$" + "\n\n" + r"$\rightarrow A \setminus B = \{1\}$",
            "example_en": r"$\text{If } A=\{1,2\}, B=\{2,3\}$" + "\n\n" + r"$\rightarrow A \setminus B = \{1\}$"
        },
        "comp": {
            "symbol": "Ā",
            "title_de": "Komplement",
            "title_en": "Complement",
            "def_de": "Alles im Ereignisraum $S$, was nicht in $A$ liegt.",
            "def_en": "Everything in sample space $S$ that is not in $A$.",
            "example_de": r"$\text{Wenn } S = \{1, 2, 3\} \text{ und } A = \{1\}$" + "\n\n" + r"$\rightarrow \bar{A} = \{2, 3\}$",
            "example_en": r"$\text{If } S = \{1, 2, 3\} \text{ and } A = \{1\}$" + "\n\n" + r"$\rightarrow \bar{A} = \{2, 3\}$"
        }
    },
    "interactive_header": {"de": "Interaktive Visualisierung", "en": "Interactive Visualization"}
}

def get_venn_figure(selection):
    """Generates the Plotly figure for the Venn Diagram."""
    fig = go.Figure()
    
    APPLE_BLUE = "rgba(0, 122, 255, 0.4)"
    
    t_rad = np.linspace(0, 2*np.pi, 200)
    xa = 1 * np.cos(t_rad) - 0.6
    ya = 1 * np.sin(t_rad)
    xb = 1 * np.cos(t_rad) + 0.6
    yb = 1 * np.sin(t_rad)
    
    fig.add_trace(go.Scatter(x=xa, y=ya, mode='lines', line=dict(color='black', width=2), name="A", hoverinfo='skip'))
    fig.add_trace(go.Scatter(x=xb, y=yb, mode='lines', line=dict(color='black', width=2), name="B", hoverinfo='skip'))
    
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
        xaxis=dict(
            visible=False, 
            scaleanchor="y", 
            scaleratio=1, 
            range=[-2.5, 2.5],
            fixedrange=True
        ), 
        yaxis=dict(
            visible=False, 
            range=[-1.8, 1.8],
            fixedrange=True
        ), 
        width=None, # Allow Streamlit to handle width
        height=400, 
        margin=dict(l=0, r=0, t=0, b=0), 
        plot_bgcolor="rgba(0,0,0,0)", 
        paper_bgcolor="rgba(0,0,0,0)", 
        showlegend=False,
        dragmode=False
    )
    fig.add_annotation(x=-0.6, y=0, text="A", showarrow=False, font=dict(size=18, color="black", family="Arial Black"))
    fig.add_annotation(x=0.6, y=0, text="B", showarrow=False, font=dict(size=18, color="black", family="Arial Black"))
    return fig

def render_subtopic_1_2(model):
    st.header(t(content_1_2["title"]))
    st.caption(t(content_1_2["theory_intro"]))
    st.markdown("---")
    
    # --- CSS: FORCE EQUAL HEIGHT COLUMNS ---
    st.markdown("""
    <style>
    /* Force horizontal blocks (rows) to stretch columns to equal height */
    [data-testid="stHorizontalBlock"] {
        align-items: stretch !important;
    }
    
    /* Make columns vertical flex containers (covering both new and old IDs) */
    [data-testid="column"], [data-testid="stColumn"] {
        display: flex !important;
        flex-direction: column !important;
    }

    /* Ensure the direct child of the column (vertical block) takes full height */
    [data-testid="column"] > div, [data-testid="stColumn"] > div {
        flex: 1 !important; 
        display: flex !important;
        flex-direction: column !important;
        height: 100% !important;
    }
    
    /* Target the specific vertical block wrappers to ensure they grow */
    div[data-testid="stVerticalBlock"], 
    div[data-testid="stVerticalBlockBorderWrapper"],
    div[data-testid="stLayoutWrapper"] {
        flex: 1 !important;
        display: flex !important;
        flex-direction: column !important;
    }
    
    /* Ensure internal content of the bordered box also grows */
    div[data-testid="stVerticalBlockBorderWrapper"] > div {
        flex: 1 !important;
        justify_content: space-between !important;
    }

    /* Radio button fix */
    div[role="radiogroup"] {
        width: 100% !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown(f"### {t(content_1_2['theory_header'])}")
    st.markdown("")
    
    # Outer border container
    with st.container(border=True):
        # --- PAIR 1: UNION & INTERSECTION ---
        # UNIFIED CARDS
        c1, c2 = st.columns(2)
        
        # CARD 1: UNION
        with c1:
            with st.container(border=True):
                # Definition
                st.markdown(f"### {content_1_2['definitions']['union']['symbol']}")
                st.caption(t({"de": content_1_2['definitions']['union']["title_de"], "en": content_1_2['definitions']['union']["title_en"]}))
                st.markdown(t({"de": content_1_2['definitions']['union']["def_de"], "en": content_1_2['definitions']['union']["def_en"]}))
                
                # Divider
                st.markdown("---")
                
                # Example
                st.markdown(f"*{t({'de': 'Beispiel', 'en': 'Example'})}:*")
                st.markdown(t({"de": content_1_2['definitions']['union']["example_de"], "en": content_1_2['definitions']['union']["example_en"]}))

        # CARD 2: INTERSECTION
        with c2:
            with st.container(border=True):
                # Definition
                st.markdown(f"### {content_1_2['definitions']['sect']['symbol']}")
                st.caption(t({"de": content_1_2['definitions']['sect']["title_de"], "en": content_1_2['definitions']['sect']["title_en"]}))
                st.markdown(t({"de": content_1_2['definitions']['sect']["def_de"], "en": content_1_2['definitions']['sect']["def_en"]}))
                
                # Divider
                st.markdown("---")
                
                # Example
                st.markdown(f"*{t({'de': 'Beispiel', 'en': 'Example'})}:*")
                st.markdown(t({"de": content_1_2['definitions']['sect']["example_de"], "en": content_1_2['definitions']['sect']["example_en"]}))



        # --- PAIR 2: DIFFERENCE & COMPLEMENT ---
        # UNIFIED CARDS
        c3, c4 = st.columns(2)
        
        # CARD 3: DIFFERENCE
        with c3:
            with st.container(border=True):
                # Definition
                st.markdown(f"### {content_1_2['definitions']['diff']['symbol']}")
                st.caption(t({"de": content_1_2['definitions']['diff']["title_de"], "en": content_1_2['definitions']['diff']["title_en"]}))
                st.markdown(t({"de": content_1_2['definitions']['diff']["def_de"], "en": content_1_2['definitions']['diff']["def_en"]}))
                
                # Divider
                st.markdown("---")
                
                # Example
                st.markdown(f"*{t({'de': 'Beispiel', 'en': 'Example'})}:*")
                st.markdown(t({"de": content_1_2['definitions']['diff']["example_de"], "en": content_1_2['definitions']['diff']["example_en"]}))

        # CARD 4: COMPLEMENT
        with c4:
            with st.container(border=True):
                # Definition
                st.markdown(f"### {content_1_2['definitions']['comp']['symbol']}")
                st.caption(t({"de": content_1_2['definitions']['comp']["title_de"], "en": content_1_2['definitions']['comp']["title_en"]}))
                st.markdown(t({"de": content_1_2['definitions']['comp']["def_de"], "en": content_1_2['definitions']['comp']["def_en"]}))
                
                # Divider
                st.markdown("---")
                
                # Example
                st.markdown(f"*{t({'de': 'Beispiel', 'en': 'Example'})}:*")
                st.markdown(t({"de": content_1_2['definitions']['comp']["example_de"], "en": content_1_2['definitions']['comp']["example_en"]}))
    
    st.markdown("---")
    
    # --- BOTTOM SECTION: INTERACTIVE CONTROLS (LEFT) + DIAGRAM (RIGHT) ---
    st.markdown(f"### {t(content_1_2['interactive_header'])}")
    st.markdown("")
    
    # Wrap in bordered container
    with st.container(border=True):
        col_controls, col_diagram = st.columns([1, 2])
        
        with col_controls:
            st.markdown(f"**{t({'de': 'Wähle Operation:', 'en': 'Select Operation:'})}**")
            st.markdown("")
            
            # Vertical button stack
            op_map = {
                "A": "A",
                "B": "B",
                "A ∪ B": "union",
                "A ∩ B": "sect",
                "A \\ B": "diff",
                "Ā": "comp"
            }
            
            # Load indices from session state or defaults
            if "selected_op_1_2" not in st.session_state:
                st.session_state.selected_op_1_2 = "union"

            for label, key in op_map.items():
                if st.button(
                    label, 
                    key=f"op_btn_{key}",
                    type="primary" if st.session_state.selected_op_1_2 == key else "secondary",
                    use_container_width=True
                ):
                    st.session_state.selected_op_1_2 = key
                    st.rerun()
        
        with col_diagram:
            fig = get_venn_figure(st.session_state.selected_op_1_2)
            st.plotly_chart(fig, use_container_width=False, config={'displayModeBar': False})

    # --- THE EXAM WORKBENCH ---
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown(f"### {t({'de': 'Prüfungstraining: Aufgabe 1.2.1', 'en': 'Exam Practice: Problem 1.2.1'})}")
    st.markdown(f"*{t({'de': 'Statistikskript Aufgabe 1.2.1 (4)', 'en': 'Statistikskript Aufgabe 1.2.1 (4)'})}*")
    st.markdown("")
    
    with st.container(border=True):
        st.markdown(t({'de': r"Werfen von zwei Würfeln ($|S|=36$). Berechnen Sie die Wahrscheinlichkeit der folgenden Ereignisse:", 'en': r"Throwing two dice ($|S|=36$). Calculate the probability of the following events:"}))
        st.markdown("")
        
        # Apply green indicators for answered tabs (only A, B, C for dice problem)
        tab_css = render_tab_progress_css(["A", "B", "C"], "1_2", topic_id="1", subtopic_id="1.2")
        st.markdown(tab_css, unsafe_allow_html=True)
        
        tab_a, tab_b, tab_c = st.tabs(["Event A", "Event B", "Event C"])
        
        def render_exam_workbench(label, q_id, ai_ctx="Topic 1.2: Set operations"):
            q_data = get_question("1.2", q_id)
            if not q_data: return
            
            # Handle bilingual options (dicts with de/en keys)
            opts = q_data.get('options', [])
            if opts and isinstance(opts[0], dict) and ('de' in opts[0] or 'en' in opts[0]):
                option_labels = [t(o) for o in opts]
            else:
                option_labels = opts
            
            render_mcq(
                key_suffix=f"1_2_{label}",
                question_text=t(q_data['question']),
                options=option_labels,
                correct_idx=q_data['correct_idx'],
                solution_text_dict=q_data['solution'],
                success_msg_dict={"de": "Richtig", "en": "Correct"},
                error_msg_dict={"de": "Falsch", "en": "Incorrect"},
                client=model,
                ai_context=f"{ai_ctx}. Question: {q_id}",
                course_id="vwl", topic_id="1", subtopic_id="1.2", question_id=f"1_2_{label}"
            )

        with tab_a: render_exam_workbench("A", "q_1_2_1_a")
        with tab_b: render_exam_workbench("B", "q_1_2_1_b")
        with tab_c: render_exam_workbench("C", "q_1_2_1_c")

    # --- ADDITIONAL EXAM QUESTIONS (Separate Elements) ---
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown(f"### {t({'de': 'Weitere Prüfungsaufgaben', 'en': 'Additional Exam Questions'})}")
    
    # Test 1, Question 2
    with st.container(border=True):
        st.caption("Test 1, Frage 2")
        render_exam_workbench("D", "test1_q2", "Topic 1.2: Set Operations & Probability")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Test 3, Question 1
    with st.container(border=True):
        st.caption("Test 3, Frage 1")
        render_exam_workbench("E", "test3_q1", "Topic 1.2: Complement Rule")