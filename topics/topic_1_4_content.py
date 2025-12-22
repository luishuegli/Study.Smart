import streamlit as st
import plotly.graph_objects as go
from utils.localization import t
from views.styles import render_icon

# 1. THE CONTENT DICTIONARY (Rosetta Stone Protocol)
content_1_4 = {
    "title": {"de": "1.4 Axiomatik der Wahrscheinlichkeitstheorie", "en": "1.4 Axioms of Probability Theory"},
    "theory_header": {"de": "Die 3 Kolmogorow-Axiome", "en": "The 3 Kolmogorov Axioms"},
    "intro": {
        "de": "Damit Mathematik funktioniert, müssen diese drei 'Goldenen Regeln' immer gelten:",
        "en": "For mathematics to work, these three 'Golden Rules' must always apply:"
    },
    "axioms": {
        "1": {
            "title": {"de": "1. Nicht-Negativität", "en": "1. Non-Negativity"},
            "desc": {"de": "Eine Wahrscheinlichkeit ist nie kleiner als 0.", "en": "A probability is never less than 0."},
            "latex": r"P(A) \ge 0"
        },
        "2": {
            "title": {"de": "2. Normierung", "en": "2. Normalization"},
            "desc": {"de": "Die Wahrscheinlichkeit des gesamten Ereignisraums ist 100%.", "en": "The probability of the entire sample space is 100%."},
            "latex": r"P(S) = 1"
        },
        "3": {
            "title": {"de": "3. Additivität", "en": "3. Additivity"},
            "desc": {"de": "Für disjunkte (getrennte) Ereignisse addieren sich die Wahrscheinlichkeiten.", "en": "For disjoint (separate) events, probabilities add up."},
            "latex": r"P(A \cup B) = P(A) + P(B)"
        }
    },
    "interactive": {
        "header": {"de": "Der Wahrscheinlichkeits-Kuchen", "en": "The Probability Cake"},
        "desc": {"de": "Baue den Ereignisraum $S$. Versuche, mehr als 100% hinzuzufügen.", "en": "Build the sample space $S$. Try to add more than 100%."},
        "label_add": {"de": "Ereignis hinzufügen", "en": "Add Event"},
        "err_overflow": {"de": "Fehler: Verletzung von Axiom 2! Summe > 1.", "en": "Error: Violation of Axiom 2! Sum > 1."}
    },
    "exam": {
        "title": {"de": "Logik-Check", "en": "Logic Check"},
        "source": "Selbst erstellt / Self-created",
        "question": {
            "de": r"Welche der folgenden Wahrscheinlichkeitszuweisungen ist ungültig? ($S = \{e_1, e_2, e_3\}$)",
            "en": r"Which of the following probability assignments is invalid? ($S = \{e_1, e_2, e_3\}$)"
        },
        "options": [
            {"id": "a", "text": "P(e₁)=0.3, P(e₂)=0.3, P(e₃)=0.4"},
            {"id": "b", "text": "P(e₁)=0.5, P(e₂)=0.5, P(e₃)=0"},
            {"id": "c", "text": "P(e₁)=0.6, P(e₂)=-0.1, P(e₃)=0.5"}
        ],
        "correct_id": "c",
        "solution": {
            "de": "**Richtig! (c)**<br>Wahrscheinlichkeiten können nicht negativ sein. Dies verletzt **Axiom 1**.",
            "en": "**Correct! (c)**<br>Probabilities cannot be negative. This violates **Axiom 1**."
        }
    }
}

def init_cake_state():
    """Initialize the probability cake state."""
    if "cake_slices_1_4" not in st.session_state:
        st.session_state.cake_slices_1_4 = [{'name': 'A', 'value': 0.2}]
    if "slice_counter" not in st.session_state:
        st.session_state.slice_counter = 1  # Start at 1 (B is next)

def get_next_slice_name():
    """Generate next slice name (B, C, D, ...)."""
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    name = letters[st.session_state.slice_counter % 26]
    st.session_state.slice_counter += 1
    return name

def reset_cake():
    """Reset the probability cake to initial state."""
    st.session_state.cake_slices_1_4 = [{'name': 'A', 'value': 0.2}]
    st.session_state.slice_counter = 1

def get_probability_donut():
    """Generate the Plotly donut chart for probability cake with bold visuals and center HUD."""
    slices = st.session_state.cake_slices_1_4
    current_sum = sum(s['value'] for s in slices)
    remaining = 1.0 - current_sum
    
    # Build data
    labels = [s['name'] for s in slices]
    values = [s['value'] for s in slices]
    
    # Apple System Colors + distinct Grey for Empty
    colors = ['#007AFF', '#AF52DE', '#FF9500', '#34C759', '#FF2D55']
    color_map = {slice['name']: colors[i % len(colors)] for i, slice in enumerate(slices)}
    
    # Add dummy "Empty" slice if needed
    if remaining > 0.0001:
        labels.append('Empty (S)')
        values.append(remaining)
        color_map["Empty (S)"] = '#F0F2F6'  # Grey for empty
    
    # Build color list in order
    slice_colors = [color_map[l] for l in labels]
    
    fig = go.Figure(data=[go.Pie(
        labels=labels,
        values=values,
        hole=0.5,  # Larger hole for the HUD
        marker=dict(
            colors=slice_colors,
            line=dict(color='#FFFFFF', width=2)
        ),
        textinfo='label+percent',
        # BOLD TYPOGRAPHY FIX
        textfont=dict(
            family="Arial Black, sans-serif",
            size=15,
            color="white"
        ),
        hoverinfo='label+value',
        sort=False
    )])
    
    # THE CENTER HUD (The "Intuitive" Link)
    center_text = f"<b>Σ = {current_sum:.2f}</b>"
    center_color = "black"
    
    if current_sum >= 0.999:
        center_text = "<b>100%<br>VALID</b>"
        center_color = "#34C759"  # Apple Green
    
    fig.update_layout(
        annotations=[dict(
            text=center_text,
            x=0.5,
            y=0.5,
            font_size=20,
            font_color=center_color,
            showarrow=False
        )],
        showlegend=False,
        margin=dict(l=10, r=10, t=10, b=10),
        height=350,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    
    return fig

def render_subtopic_1_4(model):
    # Initialize State
    init_cake_state()

    # --- HEADER ---
    st.header(t(content_1_4["title"]))
    st.markdown("---")

    # --- UNIFIED CAPSULE ---
    with st.container(border=True):
        
        # 1. Full Width Intro
        st.markdown(f"### {render_icon('book-open')} {t(content_1_4['theory_header'])}", unsafe_allow_html=True)
        st.markdown(t(content_1_4["intro"]))
        st.markdown("<br>", unsafe_allow_html=True)

        # 2. Columns (Left: Axiom Cards, Right: Probability Cake)
        col_theory, col_vis = st.columns([1, 1.2], gap="large")
        
        # --- LEFT: THE 3 AXIOM CARDS (STACKED) ---
        with col_theory:
            for axiom_num in ["1", "2", "3"]:
                axiom = content_1_4["axioms"][axiom_num]
                
                with st.container(border=True):
                    st.markdown(f"**{t(axiom['title'])}**")
                    st.caption(t(axiom['desc']))
                    st.latex(axiom['latex'])
                
                # Spacing between cards
                if axiom_num != "3":
                    st.markdown("")

        # --- RIGHT: PROBABILITY CAKE VALIDATOR ---
        with col_vis:
            # Force alignment
            st.markdown("""
                <style>
                h3 { margin-top: 0 !important; padding-top: 0 !important; }
                </style>
            """, unsafe_allow_html=True)
            
            st.markdown(f"### {render_icon('pie-chart')} {t(content_1_4['interactive']['header'])}", unsafe_allow_html=True)
            st.caption(t(content_1_4["interactive"]["desc"]))
            
            # Calculate current state
            current_sum = sum(s['value'] for s in st.session_state.cake_slices_1_4)
            remaining = 1.0 - current_sum
            
            # Input Controls (3 columns: Input, Add, Auto-Fill)
            c1, c2, c3 = st.columns([1.5, 1, 1])
            
            with c1:
                new_value = st.number_input(
                    "Probability",
                    min_value=0.01,
                    max_value=1.0,
                    value=0.1,
                    step=0.05,
                    label_visibility="collapsed",
                    key="prob_input_1_4"
                )
            
            with c2:
                if st.button(t(content_1_4["interactive"]["label_add"]), key="add_slice_1_4", type="primary", use_container_width=True):
                    # VALIDATION: Check Axiom 2
                    if current_sum + new_value > 1.0001:
                        st.error(t(content_1_4["interactive"]["err_overflow"]))
                    else:
                        # Add slice
                        new_name = get_next_slice_name()
                        st.session_state.cake_slices_1_4.append({'name': new_name, 'value': new_value})
                        st.rerun()
            
            with c3:
                # Auto-Fill button (only show if there's remaining space)
                if remaining > 0.0001:
                    if st.button("Auto-Fill", key="autofill_1_4", type="secondary", use_container_width=True, help="Instantly satisfy Axiom 2"):
                        new_name = get_next_slice_name()
                        st.session_state.cake_slices_1_4.append({'name': 'Rest', 'value': remaining})
                        st.rerun()
            
            # The Donut Chart
            fig = get_probability_donut()
            st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
            
            # Reset Button
            if st.button("Reset", key="reset_cake_1_4", type="secondary", use_container_width=True):
                reset_cake()
                st.rerun()

    # --- EXAM WORKBENCH ---
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown(f"### {render_icon('clipboard-list')} {t(content_1_4['exam']['title'])}", unsafe_allow_html=True)
    st.caption(content_1_4['exam']['source'])
    
    with st.container(border=True):
        st.markdown(t(content_1_4["exam"]["question"]))
        
        # Options
        opts = content_1_4["exam"]["options"]
        opt_labels = [o["text"] for o in opts]
        
        # Radio with instant feedback
        radio_key = "mcq_1_4"
        user_selection = st.radio(
            "Selection", 
            options=opt_labels, 
            index=None, 
            key=radio_key,
            label_visibility="collapsed"
        )
        
        # Instant feedback when selection is made
        if user_selection:
            selected_idx = opt_labels.index(user_selection)
            selected_id = opts[selected_idx]["id"]
            
            if selected_id == content_1_4["exam"]["correct_id"]:
                st.success(t({"de": "Korrekt!", "en": "Correct!"}))
                st.session_state.show_sol_1_4 = True
            else:
                st.error(t({"de": "Das stimmt nicht ganz.", "en": "That is not quite right."}))
        
        # Solution (only show if correct answer was selected)
        if st.session_state.get("show_sol_1_4", False):
            st.markdown("---")
            # Fix: Use unsafe_allow_html=True to render HTML tags properly
            sol_text = t(content_1_4["exam"]["solution"])
            st.markdown(sol_text, unsafe_allow_html=True)
            
            # AI Tutor
            st.markdown("---")
            st.caption(f"{render_icon('bot')} AI Tutor", unsafe_allow_html=True)
            
            # AI Response Area (appears above input)
            if "ai_response_1_4" in st.session_state:
                st.markdown(f"**AI:** {st.session_state['ai_response_1_4']}")
                st.markdown("---")
            
            # Input and Button
            c_ai_1, c_ai_2 = st.columns([4, 1])
            with c_ai_1:
                ai_q = st.text_input(
                    t({"de": "Frage:", "en": "Question:"}), 
                    key="ai_q_1_4", 
                    placeholder=t({"de": "Was ist unklar?", "en": "What is unclear?"}),
                    label_visibility="collapsed"
                )
            with c_ai_2:
                if st.button("Ask", key="ai_btn_1_4", type="primary", use_container_width=True):
                    if model and ai_q:
                        with st.spinner("..."):
                            prompt = f"Context: Kolmogorov Axioms of Probability. User Question: {ai_q}"
                            try:
                                response = model.generate_content(prompt)
                                st.session_state["ai_response_1_4"] = response.text
                                st.rerun()
                            except Exception as e:
                                st.error(f"Error: {e}")
                    elif not model:
                        st.error("Model unavailable")
