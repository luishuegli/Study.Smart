import streamlit as st
import plotly.graph_objects as go
import numpy as np
from views.styles import render_icon, inject_equal_height_css
from utils.localization import t
from utils.ai_helper import render_ai_tutor
from utils.quiz_helper import render_mcq
from data.exam_questions import get_question

# 1. DATA STRUCTURE
content_1_5 = {
    "title": {"de": "1.5 Wichtige Regeln (Additionssatz)", "en": "1.5 Important Rules (Addition Law)"},
    "intro": {
        "header": {"de": "Die Intuition", "en": "The Intuition"},
        "text": {"de": "Stell dir Gästelisten für zwei Partys vor. Wenn 10 Leute auf beiden Listen stehen, darfst du sie nicht doppelt zählen. Du musst die 'Überlappung' einmal abziehen, um die wahre Gesamtzahl zu erhalten.", "en": "Think of guest lists for two parties. If 10 people are on both lists, you'd count them twice if you just added the totals. To get the true count, you must subtract that 'overlap' once."}
    },
    "rules": {
        "comp": {
            "title": {"de": "1. Komplement", "en": "1. Complement"},
            "text": {"de": "Die Wahrscheinlichkeit, dass A *nicht* eintritt.", "en": "The probability that A does *not* occur."},
            "latex": r"P(\bar{A}) = 1 - P(A)"
        },
        "union": {
            "title": {"de": "2. Der Additionssatz", "en": "2. General Addition Rule"},
            "text": {"de": "Für beliebige Ereignisse. Wir müssen die Schnittmenge abziehen.", "en": "For any events. We must subtract the intersection."},
            "latex": r"P(A \cup B) = P(A) + P(B) - P(A \cap B)"
        },
        "diff": {
            "title": {"de": "3. Differenzregel", "en": "3. Difference Rule"},
            "text": {"de": "Das Ereignis 'A ohne B' (Theorem 4).", "en": "The event 'A without B' (Theorem 4)."},
            "latex": r"P(A \setminus B) = P(A) - P(A \cap B)"
        },
        "mono": {
            "title": {"de": "4. Monotonie", "en": "4. Monotonicity"},
            "text": {"de": "Wenn A ein Teil von B ist, kann P(A) nicht größer sein (Theorem 6).", "en": "If A is part of B, P(A) cannot be larger (Theorem 6)."},
            "latex": r"A \subseteq B \Rightarrow P(A) \leq P(B)"
        }
    },
    "interactive": {
        "header": {"de": "Der Überlappungs-Simulator", "en": "The Overlap Simulator"},
        "desc": {"de": "Beobachte, wie die Gesamtreichweite (Union) sinkt, wenn die Überlappung steigt.", "en": "Watch how Total Reach (Union) drops as overlap increases."},
        "metric_label": {"de": "Gesamtreichweite (Union)", "en": "Total Reach (Union)"},
        "tip": {"de": "Profi-Tipp: Die Schnittmenge kann niemals größer sein als die kleinste Einzelgruppe. Du kannst nicht mehr 'Beide' haben als du überhaupt iPhone-Nutzer hast!", "en": "Pro Tip: The intersection can never be larger than the smallest individual group. You can't have more 'Both' than you have iPhone users!"},
        # NEW: The "Mission" Context
        "mission_title": {"de": "Deine Mission: Der Markt-Analyst", "en": "Your Mission: The Market Analyst"},
        "mission_text": {
            "de": "Wir wissen: **60%** haben ein iPhone ($P(A)$) und **40%** ein MacBook ($P(B)$). Die Marktforschung sagt, dass **80%** der Leute *mindestens eines* der Geräte besitzen ($A \\cup B$).\n\n**Aufgabe:** Stelle die Slider für A und B ein. Finde dann die **Schnittmenge**, damit die Gesamtreichweite genau **0.80** beträgt.",
            "en": "We know: **60%** have an iPhone ($P(A)$) and **40%** a MacBook ($P(B)$). Market research says **80%** own *at least one* device ($A \\cup B$).\n\n**Task:** Set sliders A and B. Then find the correct **Overlap** so the Total Reach equals exactly **0.80**."
        }
    }
}

def render_subtopic_1_5(model):
    """1.5 Wichtige Regeln (Additionssatz) - High-Fidelity Dashboard"""
    inject_equal_height_css()
    
    # --- STEP 0: THE ULTRA-ROBUST EQUAL HEIGHT PROTOCOL (Ported from 1.2) ---
    st.markdown("""
    <style>
    /* Force horizontal blocks (rows) to stretch columns to equal height */
    [data-testid="stHorizontalBlock"] {
        align-items: stretch !important;
    }
    
    /* Make columns vertical flex containers */
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
    
    /* Ensure internal content of the bordered box also grows and distributes */
    div[data-testid="stVerticalBlockBorderWrapper"] > div {
        flex: 1 !important;
        display: flex !important;
        flex-direction: column !important;
        justify-content: space-between !important;
    }
    </style>
    """, unsafe_allow_html=True)

    st.header(t(content_1_5["title"]))
    st.markdown(t({"de": "Wie addiert man Wahrscheinlichkeiten korrekt, ohne doppelt zu zählen?", "en": "How to add probabilities correctly without double counting?"}))
    
    # ROW 1: THE INTUITION (Full Width)
    st.markdown(f"### {t(content_1_5['intro']['header'])}")
    st.markdown(t(content_1_5["intro"]["text"]))
    
    st.markdown("<br>", unsafe_allow_html=True)

    # ROW 2: THE RULES (Side-by-Side with Equal Height)
    c1, c2 = st.columns(2, gap="medium")
    
    with c1:
        with st.container(border=True):
            st.markdown(f"**{t(content_1_5['rules']['comp']['title'])}**")
            st.caption(t(content_1_5['rules']['comp']['text']))
            
            rule_c1, rule_c2 = st.columns([1, 1])
            with rule_c1:
                st.latex(content_1_5['rules']['comp']['latex'])
            with rule_c2:
                fig_comp = get_complement_figure()
                st.plotly_chart(fig_comp, use_container_width=True, config={'displayModeBar': False})
                st.markdown(f"""
                <div style="font-size: 11px; color: #86868b; line-height: 1.4;">
                    <span style="display: inline-block; margin-right: 8px;"><b>S</b> = {t({'de': 'Ereignisraum (Alles)', 'en': 'Sample Space (All)'})}</span><br>
                    <span style="display: inline-block;"><b>Aᶜ</b> = {t({'de': 'Komplement (Alles außer A)', 'en': 'Complement (Not A)'})}</span>
                </div>
                """, unsafe_allow_html=True)
                
    with c2:
        with st.container(border=True):
            st.markdown(f"**{t(content_1_5['rules']['union']['title'])}**")
            st.caption(t(content_1_5['rules']['union']['text']))
            st.markdown("<br>", unsafe_allow_html=True)
            st.latex(content_1_5['rules']['union']['latex'])
            # Explicit min-height balance
            st.markdown("<div style='height: 80px;'></div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    
    # ROW 2B: ADDITIONAL RULES (Difference + Monotonicity from slides)
    c3, c4 = st.columns(2, gap="medium")
    
    with c3:
        with st.container(border=True):
            st.markdown(f"**{t(content_1_5['rules']['diff']['title'])}**")
            st.caption(t(content_1_5['rules']['diff']['text']))
            st.latex(content_1_5['rules']['diff']['latex'])
            st.caption(t({"de": "Nützlich für 'A aber nicht B' Szenarien", "en": "Useful for 'A but not B' scenarios"}))
    
    with c4:
        with st.container(border=True):
            st.markdown(f"**{t(content_1_5['rules']['mono']['title'])}**")
            st.caption(t(content_1_5['rules']['mono']['text']))
            st.latex(content_1_5['rules']['mono']['latex'])
            st.caption(t({"de": "Teil einer Menge hat nie größere W'keit", "en": "Part of a set never has larger probability"}))

    st.markdown("<br>", unsafe_allow_html=True)

    # ROW 3: THE SIMULATOR (Consecutive Playground and Mission)
    render_simulator_1_5()

    # EXAM SECTION
    # EXAM SECTION
    st.markdown("<br>", unsafe_allow_html=True)
    
    q_id = "q_1_5_add"
    q_data = get_question("1.5", q_id)
    
    if q_data:
        st.markdown(f"### {t({'de': 'Prüfungstraining: HS2022 (MC 5)', 'en': 'Exam Practice: HS2022 (MC 5)'})}")
        
        # Translate options properly
        translated_options = [t(opt) for opt in q_data["options"]]
        
        # Fix escaped newlines in question text
        question_text = t(q_data["question"]).replace("\\n\\n", "<br><br>").replace("\\n", "<br>")
        
        with st.container(border=True):
             render_mcq(
                key_suffix="1_5_q1",
                question_text=question_text,
                options=translated_options,
                correct_idx=q_data["correct_idx"],
                solution_text_dict=q_data["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Falsch. Schau dir den Lösungsweg an.", "en": "Incorrect. Check the solution steps."},
                client=model,
                hint_text_dict=q_data.get("hint"),
                ai_context="Addition rule and conditional probability calculation.",
                course_id="vwl",
                topic_id="1",
                subtopic_id="1.5",
                question_id="1_5_q1"
            )

def render_simulator_1_5():
    """
    10/10 Dual-Mode Simulator with Refined Crash-Proofing and Notation.
    Vertical layout: Playground first, then Mission. No emojis.
    """
    
    # --- CSS: SCOPED SLIDER COLORS (using utility) ---
    from utils.layouts.foundation import inject_slider_css
    inject_slider_css([
        {"label_contains": "iPhone", "color": "#007AFF"},     # Blue
        {"label_contains": "Mac", "color": "#AF52DE"},        # Purple
        {"label_contains": "P(A and B)", "color": "#5856D6"}, # Indigo
        {"label_contains": "Overlap", "color": "#5856D6"},    # Indigo
    ])

    # ==========================================
    # SECTION 1: PLAYGROUND (Free Mode)
    # ==========================================
    st.markdown(f"### Playground")
    with st.container(border=True):
        st.caption("Experiment freely. The Overlap slider automatically adapts.")
        
        c1, c2, c3 = st.columns(3)
        with c1:
            val_a_p = st.slider("P(A) iPhone", 0.0, 1.0, 0.5, key="play_a")
        with c2:
            val_b_p = st.slider("P(B) MacBook", 0.0, 1.0, 0.5, key="play_b")
        with c3:
            # Relative Slider (0-100% of valid range)
            limit_upper = min(val_a_p, val_b_p)
            limit_lower = max(0.0, val_a_p + val_b_p - 1.0 + 0.0001)
            
            t_rel = st.slider("P(A and B) Position (Min ↔ Max)", 0.0, 1.0, 0.5, key="play_t")
            val_i_p = limit_lower + t_rel * (limit_upper - limit_lower)
            
            st.caption(f"P(A and B) = **{val_i_p:.2f}**")

        union_p = val_a_p + val_b_p - val_i_p
        fig_p = get_venn_diagram(val_a_p, val_b_p, val_i_p)
        st.plotly_chart(fig_p, use_container_width=True, key="fig_playground", config={'displayModeBar': False})
        
        st.latex(rf"\textcolor{{#007AFF}}{{{val_a_p:.2f}}} + \textcolor{{#AF52DE}}{{{val_b_p:.2f}}} - \mathbf{{{val_i_p:.2f}}} = {union_p:.2f}")

    st.markdown("<br>", unsafe_allow_html=True)

    # ==========================================
    # SECTION 2: THE MISSION (Strict Mode - Bulletproof)
    # ==========================================
    st.markdown(f"### Mission: Market Analyst")
    with st.container(border=True):
        # 1. Briefing
        st.markdown(t(content_1_5['interactive']['mission_text']))
        st.markdown("---")

        # 2. State Initialization
        # We use explicit initialization and NEVER delete keys to avoid sync issues
        if "miss_a" not in st.session_state: st.session_state.miss_a = 0.3
        if "miss_b" not in st.session_state: st.session_state.miss_b = 0.3
        if "miss_i" not in st.session_state: st.session_state.miss_i = 0.0
        if "balloons_done" not in st.session_state: st.session_state.balloons_done = False

        target_a = 0.60
        target_b = 0.40
        target_union = 0.80
        
        # We use a slightly more generous epsilon for slider noise
        def is_close(val, target): return abs(val - target) < 0.015

        # 3. Logic: Determine current step based on state
        a_set = is_close(st.session_state.miss_a, target_a)
        b_set = is_close(st.session_state.miss_b, target_b)
        
        step = 1
        if a_set: step = 2
        if a_set and b_set: step = 3

        # 4. Control Panel
        col_ctrl, col_vis = st.columns([1, 1.5], gap="large")

        with col_ctrl:
            st.markdown("#### Control Panel")

            # --- STEP 1: IPHONE DATA ---
            if step == 1:
                st.markdown(f"""
                <div style="background-color: rgba(0, 122, 255, 0.08); border: 1px solid rgba(0, 122, 255, 0.1); border-radius: 8px; padding: 12px; color: #007AFF; font-size: 14px; margin-bottom: 16px;">
                    <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 8px;">
                        {render_icon('file-text')} <strong>Data Point A:</strong>
                    </div>
                    Market research indicates that <b>60%</b> of the target demographic owns an <b>iPhone</b>.<br><br>
                    Input this value into the model below. {render_icon('arrow-right')}
                </div>
                """, unsafe_allow_html=True)
            
            lab_a = "P(A) iPhone (Data Locked)" if a_set else "Input P(A) iPhone Data"
            val_a = st.slider(
                lab_a, 0.0, 1.0, 
                value=st.session_state.miss_a, 
                step=0.01,
                key="miss_a", 
                disabled=(step > 1)
            )

            # --- STEP 2: MACBOOK DATA ---
            if step == 2:
                st.markdown(f"""
                <div style="background-color: rgba(0, 122, 255, 0.08); border: 1px solid rgba(0, 122, 255, 0.1); border-radius: 8px; padding: 12px; color: #007AFF; font-size: 14px; margin-bottom: 16px;">
                    <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 8px;">
                        {render_icon('file-text')} <strong>Data Point B:</strong>
                    </div>
                    The report also states that <b>40%</b> of the demographic owns a <b>MacBook</b>.<br><br>
                    Input this value into the model. {render_icon('arrow-right')}
                </div>
                """, unsafe_allow_html=True)
            
            lab_b = "P(B) MacBook (Data Locked)" if b_set else ("Input P(B) MacBook Data" if step == 2 else "P(B) MacBook (Waiting)")
            val_b = st.slider(
                lab_b, 0.0, 1.0, 
                value=st.session_state.miss_b, 
                step=0.01,
                key="miss_b", 
                disabled=(step != 2)
            )

            # --- STEP 3: THE ANALYSIS (INTERSECTION) ---
            # Pre-calculate solution state for alerts (Fix NameError)
            is_solved = is_close(val_a + val_b - st.session_state.miss_i, target_union) and step == 3

            # Crash Protection Logic (Safety Valve)
            math_lim_up = min(val_a, val_b)
            math_lim_lo = max(0.0, val_a + val_b - 1.0)
            
            if step != 3:
                slider_min, slider_max = 0.0, 1.0
            else:
                slider_min = float(math_lim_lo)
                slider_max = float(math_lim_up)
                if slider_max <= slider_min: slider_max = slider_min + 0.05
                
                # Bounds Fix
                if st.session_state.miss_i < slider_min: st.session_state.miss_i = slider_min
                if st.session_state.miss_i > slider_max: st.session_state.miss_i = slider_max

                # Narrative Prompt for Step 3
                if not is_solved:
                    # Heuristic: If value is 0.0 (start), show instruction. Else show discrepancy.
                    if st.session_state.miss_i == 0.0:
                         st.markdown(f"""
                        <div style="background-color: rgba(0, 122, 255, 0.08); border: 1px solid rgba(0, 122, 255, 0.1); border-radius: 8px; padding: 12px; color: #007AFF; font-size: 14px; margin-bottom: 16px;">
                            <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 8px;">
                                {render_icon('activity')} <strong>Calibration Required:</strong>
                            </div>
                            The model needs calibration. Find the correct <b>Overlap</b> to match the survey total (0.80).<br><br>
                            Adjust the slider below. {render_icon('arrow-right')}
                        </div>
                        """, unsafe_allow_html=True)
                    else:
                        st.markdown(f"""
                        <div style="background-color: rgba(255, 149, 0, 0.08); border: 1px solid rgba(255, 149, 0, 0.1); border-radius: 8px; padding: 12px; color: #FF9500; font-size: 14px; margin-bottom: 16px;">
                            <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 8px;">
                                {render_icon('alert-triangle')} <strong>Discrepancy Detected:</strong>
                            </div>
                            The calculated Total Reach does not match the survey data (<b>0.80</b>).<br><br>
                            <b>Calibrate</b> the overlap to align the model. {render_icon('arrow-right')}
                        </div>
                        """, unsafe_allow_html=True)

            lab_i = "P(A and B) Model Calibrated" if is_solved else ("Calibrate Overlap P(A and B)" if step == 3 else "Overlap (Locked)")
            
            val_i = st.slider(
                lab_i, 
                slider_min, 
                slider_max, 
                value=st.session_state.miss_i, 
                step=0.01,
                key="miss_i", 
                disabled=(step != 3)
            )

        with col_vis:
            # 5. Visuals & HUD
            curr_un = val_a + val_b - val_i
            fig = get_venn_diagram(val_a, val_b, val_i)
            st.plotly_chart(fig, use_container_width=True, key="fig_mission", config={'displayModeBar': False})
            
            st.metric("Total Reach (Target: 0.80)", f"{curr_un:.2f}")
            
            # Feedback Logic
            if step < 3:
                st.markdown(f"""
                <div style="background-color: rgba(0, 122, 255, 0.08); border: 1px solid rgba(0, 122, 255, 0.1); border-radius: 8px; padding: 12px; color: #007AFF; font-size: 14px; text-align: center;">
                    Step {step}: Configure the market shares first.
                </div>
                """, unsafe_allow_html=True)
            elif is_solved:
                st.markdown("""
                <div style="background-color: rgba(52, 199, 89, 0.15); border: 1px solid #34C759; border-radius: 8px; padding: 10px; color: #34C759; font-weight: bold; text-align: center;">
                    PERFECT MATCH <br> <span style="font-size: 0.8em; font-weight: normal;">Mission Accomplished</span>
                </div>
                """, unsafe_allow_html=True)
                
                if not st.session_state.get("balloons_done"):
                    st.balloons()
                    st.session_state.balloons_done = True
                    
                    # Update progress correctly (Local + Firestore)
                    from utils.progress_tracker import track_question_answer, update_local_progress
                    user = st.session_state.get("user")
                    if user:
                        user_id = user["localId"]
                        # 1. Update Firestore
                        track_question_answer(user_id, "vwl", "1", "1.5", "1_5_mission", True)
                        # 2. Update Local Session State (UI Sync)
                        update_local_progress("1", "1.5", "1_5_mission", True)
                        
                        # 3. Trigger Rerun to update sidebar immediately
                        st.rerun()
            else:
                st.session_state.balloons_done = False
                diff = curr_un - target_union
                msg = "Reach is too High. Increase P(A and B) overlap." if diff > 0 else "Reach is too Low. Decrease P(A and B) overlap."
                st.markdown(f"""
                <div style="background-color: rgba(255, 149, 0, 0.08); border: 1px solid rgba(255, 149, 0, 0.1); border-radius: 8px; padding: 12px; color: #FF9500; font-size: 14px; text-align: center;">
                    {msg}
                </div>
                """, unsafe_allow_html=True)
                
        # --- NARRATIVE CONCLUSION (Full Width) ---
        if is_solved:
            st.markdown(f"""
            <div style="background-color: rgba(245, 245, 247, 1.0); border: 1px solid rgba(0,0,0,0.05); border-radius: 12px; padding: 16px; margin-top: 24px; color: #1D1D1F;">
                <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 8px;">
                    {render_icon('beaker')} <strong>Analyst's Insight: The Hidden 20%</strong>
                </div>
                <div style="font-size: 14px; line-height: 1.5; opacity: 0.9;">
                    Notice what happened: <b>60%</b> (iPhone) + <b>40%</b> (Mac) = <b>100%</b>.<br>
                    But the survey said only <b>80%</b> of people own at least one device.<br><br>
                    Where did the missing <b>20%</b> go? They are the people who own <b>both</b>! By setting the Overlap to 0.20, you "found" the double-counted group that was inflating the total. This is the power of the formula:
                    <br><br>
                    <div style="text-align: center; font-weight: 600; font-family: 'Source Sans Pro', sans-serif;">
                        P(A ∪ B) = P(A) + P(B) - P(A ∩ B)
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("<br><br>", unsafe_allow_html=True)
            
            def reset_mission():
                st.session_state.miss_a = 0.3
                st.session_state.miss_b = 0.3
                st.session_state.miss_i = 0.0
                st.session_state.balloons_done = False
            
            st.button("Restart Mission", on_click=reset_mission)

    # ROW 4: THE PRO TIP (Footer - outside the simulator box for breathing room)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(t(content_1_5["interactive"]["tip"]))

def get_venn_diagram(prob_a, prob_b, prob_i):
    """
    Generates a Venn diagram where circles slide along the X-axis.
    Aspect Ratio is LOCKED to prevent squishing.
    """
    # 1. Calculate Radii (Area = Probability -> r = sqrt(P/pi))
    # We scale up by 2.5 to make them look good on the chart
    scale = 2.5
    ra = np.sqrt(prob_a / np.pi) * scale if prob_a > 0 else 0
    rb = np.sqrt(prob_b / np.pi) * scale if prob_b > 0 else 0
    
    # 2. Calculate Distance (The Sliding Rail)
    # Min overlap (0) -> Distance is sum of radii (touching)
    # Max overlap (min set) -> Distance is diff of radii (concentric)
    
    max_possible_overlap = min(prob_a, prob_b)
    
    # Avoid division by zero
    if max_possible_overlap == 0:
        ratio = 0
    else:
        ratio = prob_i / max_possible_overlap
        
    # Linear Interpolation creates a "fast-slow" visual disconnect.
    # We use a simple power curve to smooth the approach.
    ease_t = ratio 
    
    # Easing function (Quadratic Ease-In-Out) makes it feel more "physical"
    if ease_t < 0.5:
        smoothed_ratio = 2 * ease_t * ease_t
    else:
        smoothed_ratio = -1 + (4 - 2 * ease_t) * ease_t
        
    # Apply smoothed ratio to distance
    dist_touching = ra + rb
    dist_inside = abs(ra - rb)
    d = dist_touching - (dist_touching - dist_inside) * smoothed_ratio
    
    # 3. Centers (Slide along X-axis, centered at 0)
    # Circle A moves left, Circle B moves right
    cx_a = -d / 2
    cx_b = +d / 2
    
    # 4. Build Figure
    fig = go.Figure()
    
    # Circle A (iPhone - Blue)
    if prob_a > 0:
        fig.add_shape(type="circle",
            xref="x", yref="y",
            x0=cx_a - ra, y0=-ra, x1=cx_a + ra, y1=ra,
            fillcolor="#007AFF", opacity=0.5, line_color="#007AFF"
        )
    
    # Circle B (MacBook - Purple)
    if prob_b > 0:
        fig.add_shape(type="circle",
            xref="x", yref="y",
            x0=cx_b - rb, y0=-rb, x1=cx_b + rb, y1=rb,
            fillcolor="#AF52DE", opacity=0.5, line_color="#AF52DE"
        )
    
    # Add Text Labels (Centered on circles)
    labels = []
    x_pos = []
    if prob_a > 0:
        labels.append(f"<b>{t({'de': 'iPhone', 'en': 'iPhone'})}</b>")
        x_pos.append(cx_a)
    if prob_b > 0:
        labels.append(f"<b>{t({'de': 'Mac', 'en': 'Mac'})}</b>")
        x_pos.append(cx_b)

    if labels:
        fig.add_trace(go.Scatter(
            x=x_pos, 
            y=[0] * len(labels),
            text=labels,
            mode="text",
            textfont=dict(color="white", size=14, family="Arial Black"),
            hoverinfo='skip'
        ))

    # 5. THE ANTI-SQUISH LOCK
    fig.update_layout(
        xaxis=dict(
            visible=False, 
            scaleanchor="y", 
            scaleratio=1, 
            range=[-3.5, 3.5], # Tightened rail
            fixedrange=True
        ),
        yaxis=dict(
            visible=False, 
            range=[-1.8, 1.8], # Tightened height
            fixedrange=True
        ),
        margin=dict(l=0, r=0, t=0, b=0),
        height=300, # Reduced height for better visibility
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        showlegend=False,
        dragmode=False
    )
    
    return fig

def get_complement_figure():
    """Generates a simple Venn diagram for a complement."""
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=[-2.5, 2.5, 2.5, -2.5, -2.5],
        y=[-1.8, -1.8, 1.8, 1.8, -1.8],
        fill="toself",
        fillcolor="rgba(0, 122, 255, 0.15)",
        line=dict(color="black", width=2),
        name="S",
        hoverinfo='skip',
        mode='lines'
    ))

    theta = np.linspace(0, 2*np.pi, 100)
    r = 1.0
    fig.add_trace(go.Scatter(
        x=r * np.cos(theta),
        y=r * np.sin(theta),
        fill="toself",
        fillcolor="white",
        line=dict(color="black", width=2),
        name="A",
        showlegend=False,
        hoverinfo='skip',
        mode='lines'
    ))

    fig.add_annotation(x=0, y=0, text="A", showarrow=False, font=dict(size=14))
    fig.add_annotation(x=2, y=1.5, text="S", showarrow=False, font=dict(size=14))
    fig.add_annotation(x=-1.5, y=1.5, text="Aᶜ", showarrow=False, font=dict(size=18, color="#007AFF"))

    fig.update_layout(
        xaxis=dict(range=[-2.6, 2.6], visible=False),
        yaxis=dict(range=[-1.9, 1.9], visible=False),
        showlegend=False,
        width=180,
        height=120,
        margin=dict(l=0, r=0, t=0, b=0),
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)"
    )
    
    return fig

    fig.update_layout(
        xaxis=dict(range=[-2.6, 2.6], visible=False),
        yaxis=dict(range=[-1.9, 1.9], visible=False),
        showlegend=False,
        width=180,
        height=120,
        margin=dict(l=0, r=0, t=0, b=0),
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)"
    )
    
    return fig
