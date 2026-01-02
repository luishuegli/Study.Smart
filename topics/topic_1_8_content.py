import streamlit as st
import plotly.graph_objects as go
import numpy as np
from views.styles import render_icon, inject_equal_height_css
from utils.localization import t
from utils.quiz_helper import render_mcq
from utils.progress_tracker import track_question_answer
from data.exam_questions import get_question

# --- CONTENT DICTIONARY ---
content_1_8 = {
    "title": {"de": "1.8 Totale Wahrscheinlichkeit", "en": "1.8 Total Probability"},
    "mission": {
        "title": {"de": "Die Fabrik der Unsicherheit", "en": "The Factory of Uncertainty"},
        "anchor": {
            "de": "**Deine Mission:** Du bist Qualitätsmanager. Berechne die *gesamte* Defektquote deiner Fabrik, die von 3 verschiedenen Zulieferern abhängt.",
            "en": "**Your Mission:** You are the Quality Manager. Calculate the *total* defect rate of your factory, which depends on 3 different suppliers."
        },
        "instruction": {
            "de": "Stelle Marktanteile (Breite) und Defektraten (Höhe) ein. Beobachte, wie sich der 'Turm der Fehler' zusammensetzt.",
            "en": "Adjust market shares (width) and defect rates (height). Watch how the 'Tower of Errors' is built."
        }
    },
    "theory_cards": {
        "partition": {
            "title": {"de": "Die Partition", "en": "The Partition"},
            "text": {"de": "Zerlege das Problem in disjunkte Teile $B_i$ (Zulieferer), die zusammen 100% ergeben.", "en": "Break the problem into disjoint parts $B_i$ (Suppliers) that sum to 100%."},
            "formula": r"\sum P(B_i) = 1"
        },
        "total_prob": {
            "title": {"de": "Totale Wahrscheinlichkeit", "en": "Total Probability"},
            "text": {"de": "Die Summe der gewichteten Einzelwahrscheinlichkeiten.", "en": "The sum of the weighted individual probabilities."},
            "formula": r"P(A) = \sum P(A|B_i) \cdot P(B_i)"
        }
    },
    "bridge": {
        "title": {"de": "System-Zuverlässigkeit", "en": "System Reliability"},
        "intro": {
            "de": "**Ingenieurs-Challenge:** Ein Brückensystem lässt sich nicht einfach in Serie/Parallel zerlegen. Wir nutzen den 'Keystone'-Trick ($K$).",
            "en": "**Engineering Challenge:** A bridge system cannot be simply completely decomposed into series/parallel. We use the 'Keystone' trick ($K$)."
        },
        "instruction": {
            "de": "Wähle den Zustand des Keystone-Bauteils K, um das wahre System zu vereinfachen.",
            "en": "Choose the state of Keystone component K to simplify the true system."
        }
    },
    "quiz": {
        "title": {"de": "Konzept-Check", "en": "Concept Check"}
    }
}

def render_subtopic_1_8(model):
    """1.8 Total Probability - The Factory & The Bridge"""
    inject_equal_height_css()
    
    # Global CSS for LaTeX visibility
    st.markdown("""
        <style>
        div[data-testid="stMarkdownContainer"] div.katex-display,
        div[data-testid="stMarkdownContainer"] .katex-html {
            overflow: visible !important;
            padding-top: 20px !important;
            padding-bottom: 20px !important;
        }
        </style>
    """, unsafe_allow_html=True)
    
    st.header(t(content_1_8["title"]))
    
    # --- THEORY CARDS ---
    # Equal Height Protocol
    st.markdown("""
        <style>
        [data-testid="stHorizontalBlock"] { align-items: stretch !important; }
        [data-testid="column"] { display: flex !important; flex-direction: column !important; }
        [data-testid="stVerticalBlock"], [data-testid="stVerticalBlockBorderWrapper"] { flex: 1 !important; }
        </style>
    """, unsafe_allow_html=True)
    
    with st.container(border=True):
        # ROW 1: Titles and Descriptions
        c1, c2 = st.columns(2, gap="medium")
        with c1:
            st.markdown(f"**{t(content_1_8['theory_cards']['partition']['title'])}**")
            st.caption(t(content_1_8["theory_cards"]["partition"]["text"]))
        with c2:
            st.markdown(f"**{t(content_1_8['theory_cards']['total_prob']['title'])}**")
            st.caption(t(content_1_8["theory_cards"]["total_prob"]["text"]))
            
        # ROW 2: Formulas (Split-Row Grid Protocol - Rule 2.7)
        f1, f2 = st.columns(2, gap="medium")
        with f1:
            st.latex(content_1_8["theory_cards"]["partition"]["formula"])
        with f2:
            st.latex(content_1_8["theory_cards"]["total_prob"]["formula"])
            
    st.markdown("<br>", unsafe_allow_html=True)

    # --- PART 1: THE FACTORY (Interactive Visualizer) ---
    # --- PART 1: THE FACTORY (Interactive Visualizer) ---
    # --- PART 1: THE FACTORY (Interactive Visualizer) ---
    st.markdown(f"### {t(content_1_8['mission']['title'])}")
    
    # --- CSS: SCOPED SLIDER COLORS FOR 1.8 (REFINED) ---
    st.markdown("""
    <style>
    /* 1. Alpha (Blue) */
    .stSlider:has([aria-label="Alpha"]) div[data-baseweb="slider"] > div:first-child > div:first-child { background-color: #60A5FA !important; }
    .stSlider:has([aria-label="Alpha"]) div[role="slider"] { background-color: #FFFFFF !important; border: 2px solid #60A5FA !important; }
    .stSlider:has([aria-label="Alpha"]) div[data-testid="stMarkdownContainer"] > p { color: #60A5FA !important; } 

    /* 2. Beta (Green) */
    .stSlider:has([aria-label="Beta"]) div[data-baseweb="slider"] > div:first-child > div:first-child { background-color: #34D399 !important; }
    .stSlider:has([aria-label="Beta"]) div[role="slider"] { background-color: #FFFFFF !important; border: 2px solid #34D399 !important; }
    
    /* 3. Defect Alpha (Blue) */
    .stSlider:has([aria-label="Defect Alpha"]) div[data-baseweb="slider"] > div:first-child > div:first-child { background-color: #60A5FA !important; }
    .stSlider:has([aria-label="Defect Alpha"]) div[role="slider"] { background-color: #FFFFFF !important; border: 2px solid #60A5FA !important; }

    /* 4. Defect Beta (Green) */
    .stSlider:has([aria-label="Defect Beta"]) div[data-baseweb="slider"] > div:first-child > div:first-child { background-color: #34D399 !important; }
    .stSlider:has([aria-label="Defect Beta"]) div[role="slider"] { background-color: #FFFFFF !important; border: 2px solid #34D399 !important; }

    /* 5. Defect Gamma (Amber) */
    .stSlider:has([aria-label="Defect Gamma"]) div[data-baseweb="slider"] > div:first-child > div:first-child { background-color: #FBBF24 !important; }
    .stSlider:has([aria-label="Defect Gamma"]) div[role="slider"] { background-color: #FFFFFF !important; border: 2px solid #FBBF24 !important; }
    
    /* Global Slider Label/Value Tweak */
    /* Try to force the value label to be colored text on transparent bg */
    /* Note: This is a best-effort guess at Streamlit's internal DOM for value labels */
    div[data-baseweb="slider"] > div > div > div[role="slider"] + div {
        background-color: transparent !important;
        color: inherit !important; /* Inherit from parent which we might set */
        font-weight: bold !important;
    }
    </style>
    """, unsafe_allow_html=True)

    with st.container(border=True):
        # 1. NARRATIVE HUD (AGGRESSIVE GUIDANCE)
        # We check if sliders are still at default or if success is reached
        pa_val = st.session_state.get("slider_1_8_pa", 30)
        defa_val = st.session_state.get("slider_1_8_defa", 5)
        
        # Calculate result for HUD
        p_a, p_b = st.session_state.get("slider_1_8_pa", 30), st.session_state.get("slider_1_8_pb", 50)
        p_c = 100 - p_a - p_b
        da, db, dc = st.session_state.get("slider_1_8_defa", 5), st.session_state.get("slider_1_8_defb", 20), st.session_state.get("slider_1_8_defc", 50)
        res = (p_a/100 * da/100 + p_b/100 * db/100 + p_c/100 * dc/100) * 100
        
        if pa_val == 30 and defa_val == 5: # Defaults
             st.info(t({
                 "de": "**Schritt 1:** Passe die **Marktanteile** (Priors) an. Wer produziert am meisten?",
                 "en": "**Step 1:** Adjust the **Market Shares** (Priors). Who produced the most?"
             }))
        elif res >= 2.0:
            st.warning(t({
                "de": "**Schritt 2:** Die Defektrate ist zu hoch! Optimiere die **Fehlerraten**, um unter das Ziel von 2.0% zu kommen.",
                "en": "**Step 2:** The defect rate is too high! Optimize the **Defect Rates** to get under the 2.0% target."
            }))
        else:
            st.balloons()
            st.success(t({
                "de": "**Mission erfüllt!** Du hast die totale Wahrscheinlichkeit durch kluge Partitionierung unter das Limit gedrückt.",
                "en": "**Mission Accomplished!** You pushed the total probability under the limit through smart partitioning."
            }))
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # 2. EXPERIMENT (Bordered Supplier Cards)
        col_ctrl, col_vis = st.columns([1, 1], gap="medium")
        
        with col_ctrl:
            # Callbacks to enforce A + B <= 100
            def update_alpha():
                if st.session_state.slider_1_8_pa + st.session_state.slider_1_8_pb > 100:
                    st.session_state.slider_1_8_pb = 100 - st.session_state.slider_1_8_pa
            
            def update_beta():
                if st.session_state.slider_1_8_pa + st.session_state.slider_1_8_pb > 100:
                    st.session_state.slider_1_8_pa = 100 - st.session_state.slider_1_8_pb
            
            # --- SUPPLIER CARDS (Color-coded) ---
            # Alpha Card (Blue)
            st.markdown("""
<div style="border: 2px solid #60A5FA; border-radius: 8px; padding: 10px; margin-bottom: 8px; background: rgba(96,165,250,0.05);">
<div style="font-weight: 600; color: #60A5FA; margin-bottom: 4px;">Alpha Inc.</div>
</div>
            """, unsafe_allow_html=True)
            alpha_s, alpha_d = st.columns(2)
            with alpha_s:
                st.caption("Share (Bar Width)")
                p_a = st.slider("Alpha", 0, 100, 30, key="slider_1_8_pa", label_visibility="collapsed", on_change=update_alpha)
            with alpha_d:
                st.caption("Defect Rate (Bar Height)")
                def_a = st.slider("Defect Alpha", 0, 100, 5, key="slider_1_8_defa", label_visibility="collapsed")
            
            # Beta Card (Green)
            st.markdown("""
<div style="border: 2px solid #34D399; border-radius: 8px; padding: 10px; margin-bottom: 8px; background: rgba(52,211,153,0.05);">
<div style="font-weight: 600; color: #34D399; margin-bottom: 4px;">Beta Corp.</div>
</div>
            """, unsafe_allow_html=True)
            beta_s, beta_d = st.columns(2)
            with beta_s:
                st.caption("Share (Bar Width)")
                p_b = st.slider("Beta", 0, 100, 50, key="slider_1_8_pb", label_visibility="collapsed", on_change=update_beta)
            with beta_d:
                st.caption("Defect Rate (Bar Height)")
                def_b = st.slider("Defect Beta", 0, 100, 20, key="slider_1_8_defb", label_visibility="collapsed")
            
            # Gamma Card (Amber)
            p_c = 100 - p_a - p_b
            st.markdown(f"""
<div style="border: 2px solid #FBBF24; border-radius: 8px; padding: 10px; margin-bottom: 8px; background: rgba(251,191,36,0.05);">
<div style="font-weight: 600; color: #FBBF24; margin-bottom: 4px;">Gamma Ltd. — {p_c}% (Residual)</div>
</div>
            """, unsafe_allow_html=True)
            gamma_d_col, _ = st.columns([1, 1])
            with gamma_d_col:
                st.caption("Defect Rate (Bar Height)")
                def_c = st.slider("Defect Gamma", 0, 100, 50, key="slider_1_8_defc", label_visibility="collapsed")
            
            # Target
            target_val = 2.0

        # 3. VISUALIZATION
        with col_vis:
            # Prepare Data
            # Widths = Market Share, Heights = 100 (Background), Fill = Defect Rate
            
            fig = go.Figure()
            
            # X-positions (cumulative to allow side-by-side blocks)
            # We model them as bars centered at specific points
            
            # Helper to add a supplier block
            def add_block(name, color, hatch_color, x_start, width, defect_pct):
                if width <= 0: return
                x_center = x_start + width/2
                
                # Full Block (The Supplier's Total Output)
                fig.add_trace(go.Bar(
                    x=[x_center], y=[100], width=[width],
                    name=f"{name} (Total)",
                    marker=dict(color=color, opacity=0.3, line=dict(width=0)),
                    showlegend=False, hoverinfo="skip"
                ))
                
                # Defective Part (The weighted contribution)
                defect_height = defect_pct # Height relative to 100 scale? No, relative to the block?
                # Actually, visually we want the height to represent rate (0-100%).
                # The AREA represents probability.
                
                fig.add_trace(go.Bar(
                    x=[x_center], y=[defect_pct], width=[width],
                    name=f"{name} (Defect)",
                    marker=dict(color=hatch_color, pattern=dict(shape="/")),
                    text=f"{defect_pct}%", textposition="auto",
                    hoverinfo="text+name"
                ))
            
            # Colors
            c_alpha = "#60A5FA" # Blue
            c_beta = "#34D399"  # Green
            c_gamma = "#FBBF24" # Amber
            c_defect = "#EF4444" # Red hatching
            
            # Add Supplier Blocks
            # Note: Bar charts in plotly align x-axis. Since widths vary, we need careful positioning.
            # Using offset based logic.
            
            # Alpha
            add_block("Alpha", c_alpha, c_defect, 0, p_a, def_a)
            # Beta
            add_block("Beta", c_beta, c_defect, p_a, p_b, def_b)
            # Gamma
            add_block("Gamma", c_gamma, c_defect, p_a + p_b, p_c, def_c)
            
            # Total Calculation
            total_defect_pct = (p_a/100 * def_a/100 + p_b/100 * def_b/100 + p_c/100 * def_c/100) * 100
            
            # The "Result" Tower (Total Probability)
            # Visualizing it as a separate bar on the right?
            # Let's add it at x=120 (gap)
            
            fig.add_trace(go.Bar(
                x=[120], y=[total_defect_pct], width=[20],
                name="Total Defect",
                marker=dict(color=c_defect),
                text=f"{total_defect_pct:.1f}%", textposition="outside"
            ))
            
            # Layout
            fig.update_layout(
                title=t({"de": "Marktstruktur & Fehlerrate", "en": "Market Structure & Defect Rate"}),
                xaxis=dict(range=[0, 140], showticklabels=False, title=t({"de": "Marktanteil (Partition)", "en": "Market Share (Partition)"})),
                yaxis=dict(range=[0, 100], title=t({"de": "Defektrate (%)", "en": "Defect Rate (%)"})),
                barmode="overlay", # We manually positioned them
                height=300,
                margin=dict(l=20, r=20, t=40, b=20),
                showlegend=False
            )
            
            st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
            
            # --- FORMULA IN ACTION (Integrated directly under chart) ---
            st.markdown(f"**{t({'de': 'Die Formel in Aktion', 'en': 'The Formula in Action'})}**")
            
            # Color-coded live formula
            # Color-coded live formula
            # P(D) = P(D|A)P(A) + ...
            line1 = r"\small \color{#EF4444}{P(D)} = "
            term_a = fr"\color{{#60A5FA}}{{ {def_a}\% \cdot {p_a}\% }} + "
            term_b = fr"\color{{#34D399}}{{ {def_b}\% \cdot {p_b}\% }} + "
            term_c = fr"\color{{#FBBF24}}{{ {def_c}\% \cdot {p_c}\% }}"
            
            # Numerical
            val_a = (def_a/100) * (p_a/100)
            val_b = (def_b/100) * (p_b/100)
            val_c = (def_c/100) * (p_c/100)
            total = val_a + val_b + val_c
            
            # Result in RED to match P(D)
            line3 = fr"= \color{{#EF4444}}{{ \mathbf{{ {total:.4f} }} \text{{ ({total*100:.2f}\%) }} }}"
            
            # Single line display with negative margin override (HTML Injection)
            # We use an explicit div to pull the content left and ensure it fits.
            # IMPORTANT: Blank lines are required for Markdown to process $$ inside HTML.
            st.markdown(rf"""
            <div style="margin-left: -60px; margin-right: -60px; text-align: center; overflow-x: visible;">

            $${line1 + term_a + term_b + term_c + line3}$$

            </div>
            """, unsafe_allow_html=True)
            
            # CHECK TARGET
            if total_defect_pct < target_val:
                st.success(f"{t({'de': 'ZIEL ERREICHT!', 'en': 'TARGET REACHED!'})} ({total_defect_pct:.1f}% < {target_val}%)")
                if user := st.session_state.get("user"):
                    track_question_answer(user["localId"], "vwl", "1", "1.8", "1_8_mission", True)
            else:
                st.warning(f"{t({'de': 'Ziel verfehlt.', 'en': 'Target missed.'})} ({total_defect_pct:.1f}% > {target_val}%)")
            
            st.caption(t({
                "de": "Insight: Großer Balken x Kleine Rate = Großer Einfluss.",
                "en": "Insight: Big Bar x Small Rate = Big Impact."
            }))

    st.markdown("---")
    
    # --- PART 2: THE BRIDGE (System Reliability) ---
    # --- PART 2: THE BRIDGE (System Reliability) ---
    st.markdown("<br>", unsafe_allow_html=True)
    # --- PART 2: THE BRIDGE (System Reliability) ---
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"### {t(content_1_8['bridge']['title'])}")
    
    with st.container(border=True):
        st.markdown(t(content_1_8["bridge"]["intro"]))
        st.caption(t(content_1_8["bridge"]["instruction"]))
        
        # Interactive Schematic using Graphviz or clean SVG is hard to layout perfectly in Python without external lib.
        # We will use a simplified Plotly representation of nodes and edges.
        
        # KEYSTONE TOGGLE
        keystone_state = st.radio(
            t({"de": "Zustand von Bauteil K", "en": "State of Component K"}),
            ["Working (Success)", "Broken (Fail)"],
            horizontal=True,
            index=0
        )
        
        k_works = (keystone_state == "Working (Success)")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Plotly Diagram
        # Nodes: S (Start), E (End), 1, 2, 3, 4, K (Middle)
        # Layout: S(0,1), 1(1,2), 2(1,0), K(2,1), 3(3,2), 4(3,0), E(4,1)
        
        fig_bridge = go.Figure()
        
        # Colors
        c_work = "#10B981"
        c_broken = "#EF4444"
        c_k = c_work if k_works else c_broken
        k_symbol = "circle" if k_works else "x"
        
        # Edges (Standard)
        # If K is working, it's a short circuit (line). If broken, it's open (no line).
        
        # Defining logical connectivity based on K state
        # Coordinates
        pos = {
            "S": (0, 1), "E": (4, 1),
            "1": (1, 2), "2": (1, 0),
            "3": (3, 2), "4": (3, 0),
            "K": (2, 1)
        }
        
        # Draw Components (Fixed 1,2,3,4) - assume active for visualization
        # In a real calc we'd need probs. Here we just show decomposition.
        
        # Fixed Edges: S->1, S->2, 3->E, 4->E
        edges = [("S", "1"), ("S", "2"), ("3", "E"), ("4", "E")]
        
        # Edges involving K
        # 1->K, 2->K, K->3, K->4 ? No, Bridge is usually:
        # S->1->3->E (Top path)
        # S->2->4->E (Bottom path)
        # 1->K->4 (Cross) ? 
        # Standard Bridge: 1(TopL), 2(BotL), 3(TopR), 4(BotR), K(Bridge 1-4 or 1-2?)
        # Let's assume Wheatstone Bridge topology:
        # Path A: S -> N1 -> N2 -> E
        # Path B: S -> N3 -> N4 -> E
        # K connects N1 and N3.
        
        # Let's refine for visual clarity:
        # Nodes: S(0,1), TopMid(2,2), BotMid(2,0), E(4,1) -> This is simpler parallel.
        # Wheatstone: S(0,1) -> T1(1,2) -> T2(3,2) -> E(4,1)
        #                    -> B1(1,0) -> B2(3,0) -> E(4,1)
        #                    K connects T1 and B2? Or T1 and B1? 
        # Usually K connects the midpoints. Let's say T1(Top) and B1(Bot).
        
        # Let's use specific coordinates for Wheatstone
        # 1(TopLeft), 2(BotLeft), 3(TopRight), 4(BotRight), 5(Keystone)
        
        # If K works (Short): 1 and 2 are parallel, 3 and 4 are parallel. The two blocks are in series.
        # If K fails (Open): (1+3) is series, (2+4) is series. The two branches are parallel.
        
        # Simplified Vis depending on state
        
        if k_works:
            st.markdown(f"**{t({'de': 'Fall 1: K funktioniert (Kurzschluss)', 'en': 'Case 1: K Works (Short Circuit)'})}**")
            st.latex(r"System = (1 \parallel 2) \cap (3 \parallel 4)")
            st.caption(t({"de": "1 und 2 sind parallel geschaltet. 3 und 4 sind parallel geschaltet. Die Blöcke sind in Serie.", "en": "1 and 2 are in parallel. 3 and 4 are in parallel. The blocks are in series."}))
        else:
            st.markdown(f"**{t({'de': 'Fall 2: K defekt (Unterbrechung)', 'en': 'Case 2: K Broken (Open Circuit)'})}**")
            st.latex(r"System = (1 \cap 3) \parallel (2 \cap 4)")
            st.caption(t({"de": "Oberer Pfad (1-3) und unterer Pfad (2-4) sind parallel.", "en": "Top path (1-3) and bottom path (2-4) are in parallel."}))

    st.markdown("<br>", unsafe_allow_html=True)
    # --- PART 3: EXAM WORKBENCH ---
    st.markdown(f"### {t({'de': 'Prüfungstraining', 'en': 'Exam Practice'})}")
    
    def render_exam_q(q_id, key_suffix, question_key, source_caption):
        q_data = get_question("1.8", q_id)
        if not q_data:
            st.warning(f"Question {q_id} not found in QUESTIONS_1_8")
            return
        
        opts = q_data.get("options", [])
        # Handle both string lists and dict lists
        if opts and isinstance(opts[0], dict):
            option_labels = [t(o) for o in opts]
        else:
            option_labels = opts
        
        with st.container(border=True):
            st.caption(source_caption)
            render_mcq(
                key_suffix=key_suffix,
                question_text=t(q_data['question']),
                options=option_labels,
                correct_idx=q_data['correct_idx'],
                solution_text_dict=q_data['solution'],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Falsch.", "en": "Incorrect."},
                client=model,
                ai_context=f"Topic 1.8: Total Probability & Bayes. Question: {q_id}",
                course_id="vwl", topic_id="1", subtopic_id="1.8", question_id=question_key
            )
    
    render_exam_q("uebung1_prob_factory", "1_8_factory", "1_8_factory", t({"de": "Fabrik-Frage", "en": "Factory Question"}))
    st.markdown("<br>", unsafe_allow_html=True)
    render_exam_q("hs2022_mc2", "1_8_bayes_coins", "1_8_bayes_coins", "HS 2022 Januar, MC #2 (Bayes)")
    st.markdown("<br>", unsafe_allow_html=True)
    render_exam_q("hs2022_mc1", "1_8_game_theory", "1_8_game_theory", "HS 2022 Januar, MC #1 (Geometric Series)")
