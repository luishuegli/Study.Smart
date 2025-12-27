import streamlit as st
import plotly.graph_objects as go
import numpy as np
import pandas as pd
from views.styles import render_icon
from utils.localization import t
from utils.quiz_helper import render_mcq
from utils.progress_tracker import track_question_answer

# --- CONTENT DICTIONARY ---
content_1_9 = {
    "title": {"de": "1.9 Das Bayes-Theorem", "en": "1.9 Bayes' Theorem"},
    "mission": {
        "title": {"de": "Der Medizin-Detektiv", "en": "The Medical Detective"},
        "anchor": {
            "de": "**Deine Mission:** Ein Patient wird positiv getestet. Wie hoch ist die Wahrscheinlichkeit, dass er *wirklich* krank ist?",
            "en": "**Your Mission:** A patient tests positive. What is the probability that they are *really* sick?"
        },
        "instruction": {
            "de": "Gehe durch die 3 Phasen der Diagnose. Beobachte, wie sich die Punkte verändern.",
            "en": "Go through the 3 phases of diagnosis. Watch how the dots change."
        }
    },
    "stages": ["Population", "Virus", "Test", "Filter"],
    "monty": {
        "title": {"de": "2. Das Ziegenproblem (Monty Hall)", "en": "2. The Monty Hall Problem"},
        "intro": {
            "de": "Das berühmteste Rätsel der Wahrscheinlichkeitsrechnung. Es entlarvt unsere falsche Intuition.",
            "en": "The most famous puzzle in probability. It exposes the flaws of our intuition."
        },
        "constraints": {
            "title": {"de": "Die Regeln (Der Host Constraint)", "en": "The Rules (The Host Constraint)"},
            "list": {
                "de": [
                    "1. Monty **MUSS** eine Tür öffnen.",
                    "2. Monty kann **NICHT** deine Tür öffnen.",
                    "3. Monty kann **NICHT** das Auto öffnen.",
                    "4. Monty wählt **ZUFÄLLIG**, wenn er die Wahl hat."
                ],
                "en": [
                    "1. Monty **MUST** open a door.",
                    "2. Monty cannot open **YOUR** door.",
                    "3. Monty cannot open the **CAR** door.",
                    "4. Monty chooses **RANDOMLY** if he has a choice."
                ]
            }
        },
        "intuition_100": {
            "title": {"de": "Der 100-Türen-Trick (Intuition Pump)", "en": "The 100 Doors Trick (Intuition Pump)"},
            "text": {
                "de": """
                Stell dir vor, es gibt **100 Türen**.
                1. Du wählst **Tür 1**. Chance: **1/100**.
                2. Die 'Anderen' (Tür 2-100) haben zusammen **99/100**.
                3. Monty öffnet **98** dieser anderen Türen (alles Ziegen).
                4. Nur **Tür 100** bleibt von den 'Anderen' übrig.
                
                Die 99/100 der 'Anderen' sind nicht verschwunden. Sie haben sich auf Tür 100 konzentriert.
                **Tür 1:** 1/100. **Tür 100:** 99/100. **Wechseln!**
                """,
                "en": """
                Imagine there are **100 doors**.
                1. You pick **Door 1**. Chance: **1/100**.
                2. The 'Others' (Doors 2-100) have a combined **99/100**.
                3. Monty opens **98** of these other doors (all goats).
                4. Only **Door 100** remains closed from the 'Others'.
                
                The 99/100 probability of the 'Others' didn't disappear. It concentrated on **Door 100**.
                **Door 1:** 1/100. **Door 100:** 99/100. **Switch!**
                """
            }
        },
        "anchor": {
             "de": "**Das Dilemma:** Du wählst Tor 1. Monty öffnet Tor 3 (Ziege). Solltest du zu Tor 2 wechseln?",
             "en": "**The Dilemma:** You pick Door 1. Monty opens Door 3 (Goat). Should you switch to Door 2?"
        },
        "sim_btn": {"de": "Simuliere 1000 Runden", "en": "Simulate 1000 Rounds"},
        "matrix_title": {"de": "Warum das funktioniert (Die Matrix)", "en": "Why it works (The Matrix)"}
    },
    "search": {
        "title": {"de": "3. Bayesian Search Theory", "en": "3. Bayesian Search Theory"},
        "story": {
            "de": "**Real-World Power:** Diese Methode wurde genutzt, um das Wrack der *USS Scorpion* und *Air France 447* zu finden.",
            "en": "**Real-World Power:** This method was famously used to locate the *USS Scorpion* and *Air France 447*."
        },
        "instruction": {
            "de": "Das Raster zeigt die Wahrscheinlichkeit, dass sich das Objekt im Sektor befindet. Klicke 'Search', um einen Sektor zu durchsuchen. Ein Misserfolg 'fließt' Wahrscheinlichkeit in die anderen Sektoren.",
            "en": "The grid shows the probability of the object being in a sector. Click 'Search' to scan a sector. A failure causes probability to 'flow' to other sectors."
        }
    },
    "quiz": {
        "title": {"de": "4. Logik-Check: 3 Gefangene", "en": "4. Logic Check: 3 Prisoners"},
        "question": {
            "de": "Drei Gefangene (A, B, C). Einer wird begnadigt. Wärter nennt B als Todeskandidat. Steigt As Chance?",
            "en": "Three prisoners (A, B, C). One is pardoned. Warden names B as executed. Does A's chance increase?"
        },
        "options": {
            "de": ["Ja, auf 50%", "Nein, bleibt 1/3", "Ja, auf 66%", "Nein, sinkt"],
            "en": ["Yes, to 50%", "No, stays 1/3", "Yes, to 66%", "No, decreases"]
        },
        "correct_idx": 1,
        "solution": {
            "de": """
            **Antwort: Nein, bleibt 1/3**
            
            Der Wärter musste einen Namen nennen (B oder C). Dass er B nennt, gibt A keine spezifische Information über sich selbst, da er dies in (fast) jedem Fall tun könnte. Die 'überschüssige' Wahrscheinlichkeit wandert zu C (2/3).
            """,
            "en": """
            **Answer: No, stays 1/3**
            
            The warden had to name someone (B or C). Naming B gives A no specific information about himself, as he could do this in (almost) any case. The 'surplus' probability shifts to C (2/3).
            """
        }
    }
}

def render_subtopic_1_9(model):
    """1.9 Bayes Theorem - Medical Detective & Monty Hall & Bayesian Search"""
    
    # Global CSS for LaTeX visibility
    st.markdown("""
        <style>
        div[data-testid="stMarkdownContainer"] div.katex-display,
        div[data-testid="stMarkdownContainer"] .katex-html {
            overflow: visible !important;
            padding-top: 20px !important;
            padding-bottom: 20px !important;
        }
        /* Force secondary button text to be visible (black) if theme issues exist */
        button[kind="secondary"] p, button[kind="secondary"] div {
            color: #000000 !important;
        }
        /* Also target the span inside button if structure is different */
        button[kind="secondary"] {
            color: #000000 !important;
        }
        </style>
    """, unsafe_allow_html=True)
    
    st.header(t(content_1_9["title"]))
    
    # --- THEORY ---
    st.info(t({"de": "Bayes ist das 'Update' von Wahrscheinlichkeiten durch neue Information.", "en": "Bayes is the 'Update' of probabilities using new information."}))
    st.latex(r"P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}")
    
    st.markdown("<br>", unsafe_allow_html=True)

    # --- PART 1: MEDICAL DETECTIVE (1000 Dots) ---
    # --- PART 1: MEDICAL DETECTIVE (N=16 Intuition) ---
    c_icon_1, c_title_1 = st.columns([0.1, 0.9], gap="small")
    with c_icon_1:
        st.markdown(f"<div style='display:flex; align-items:center; justify-content:center; height:100%;'>{render_icon('microscope', size=24, color='#000000')}</div>", unsafe_allow_html=True)
    with c_title_1:
        st.markdown(f"<h3 style='margin:0; padding-top:4px; color:#000000;'>1. {t(content_1_9['mission']['title'])}</h3>", unsafe_allow_html=True)
    
    with st.container(border=True):
        st.markdown(t(content_1_9["mission"]["anchor"]))
        st.caption(t(content_1_9["mission"]["instruction"]))
        
        # State Management
        if "bayes_stage" not in st.session_state:
            st.session_state.bayes_stage = 0
            
        # Params: N=16 (Strict Pedagogy: "Easy to grasp"), Sick=4 (25%), Healthy=12 (75%)
        # Test: Sensitivity 75% (3/4 detected), Specificity 75% (9/12 correct negative, 3 false alarm)
        # Result: 3 TP, 3 FP -> 50% Precision.
        N = 16
        n_sick = 4
        n_healthy = 12
        TP = 3 
        FN = 1
        TN = 9 
        FP = 3  
        
        # Grid Generation (once)
        if "bayes_dots" not in st.session_state or len(st.session_state.bayes_dots) != N:
            # Create standard grid 4x4
            rows = 4
            cols = 4
            x_list = np.tile(np.arange(cols), rows)
            y_list = np.repeat(np.arange(rows), cols)
            
            # Assign status: First 4 are Sick (3 TP, 1 FN). Next 12 are Healthy (3 FP, 9 TN).
            types = [] 
            for i in range(N):
                if i < 3: types.append('TP')
                elif i < 4: types.append('FN')
                elif i < 7: types.append('FP') # 4,5,6
                else: types.append('TN')
            
            df = pd.DataFrame({'x': x_list, 'y': y_list, 'type': types})
            st.session_state.bayes_dots = df
            
        df = st.session_state.bayes_dots
        
        # STAGE CONTROLS
        c_stages = st.columns(4)
        labels = [
            t({"de": "Start (Priori)", "en": "Start (Prior)"}),
            t({"de": "Virus (Realität)", "en": "Virus (Reality)"}),
            t({"de": "Test (Daten)", "en": "Test (Likelihood)"}),
            t({"de": "Filter (Posteriori)", "en": "Filter (Posterior)"})
        ]
        
        for i, label in enumerate(labels):
            btn_type = "primary" if st.session_state.bayes_stage == i else "secondary"
            if c_stages[i].button(str(i+1) + ". " + label, key=f"bayes_btn_{i}", type=btn_type, use_container_width=True):
                st.session_state.bayes_stage = i
                st.rerun()

        stage = st.session_state.bayes_stage
        
        # DYNAMIC INTUITION CARDS (Aggressive Guidance)
        st.markdown("<br>", unsafe_allow_html=True)
        with st.container(border=True):
            if stage == 0:
                st.info(t({
                    "de": "🎯 **Anker:** Wir starten mit einer Bevölkerung von 16. Aktuell könnte *jeder* krank sein. Wir wissen nichts.",
                    "en": "🎯 **Anchor:** We start with a population of 16. At this point, *anyone* could be sick. We know nothing."
                }))
            
            elif stage == 1:
                st.markdown(t({
                    "de": f"🧬 **Die Wahrheit:** In unserer Welt sind $P(S) = 4/16$ krank. Nur die **{render_icon('circle', '#FF4B4B')} Roten Punkte** sind betroffen.",
                    "en": f"🧬 **The Truth:** In our world, $P(S) = 4/16$ are sick. Only the **{render_icon('circle', '#FF4B4B')} Red Dots** are affected."
                }), unsafe_allow_html=True)
            
            elif stage == 2:
                st.warning(t({
                    "de": "🧪 **Das Testergebnis:** Schau dir die gelben Ränder an! Der Test hat 3 Kranke 'erwischt', aber auch 3 Gesunde 'falsch verdächtigt'.",
                    "en": "🧪 **The Test Result:** Look at the yellow borders! The test 'caught' 3 sick people, but it also 'falsely accused' 3 healthy people."
                }))
                st.latex(r"P(+|S) = 75\% \text{ (Sensitivity)} \quad P(+|H) = 25\% \text{ (False Positive Rate)}")
    
            elif stage == 3:
                st.success(t({
                    "de": "🔍 **Der Filter:** Wir ignorieren alle ohne gelben Rand. Dein neues Universum sind NUR die 6 Personen mit positivem Test.",
                    "en": "🔍 **The Filter:** We ignore everyone without a yellow border. Your new universe is ONLY the 6 people with a positive test."
                }))
                
                # Track progress
                track_question_answer(model, "vwl", "1", "1.9", "1_9_medical_mission", True)
                
                # Pro Tip: Concrete Counts
                c1, c2 = st.columns(2)
                with c1:
                    st.metric(t({"de": "Positive Tests", "en": "Positive Tests"}), "6", help=t({"de": "Alle Punkte mit gelbem Rand", "en": "All dots with yellow border"}))
                with c2:
                    st.metric(t({"de": "Wirklich Krank", "en": "Actually Sick"}), "3", help=t({"de": "Rote Punkte INNERHALB des gelben Rands", "en": "Red dots INSIDE the yellow border"}))
        
        # VISUALIZATION LOGIC
        # Colors:
        # sick_color = Red (#EF4444)
        # healthy_color = Gray (#E5E7EB)
        # pos_test_border = Yellow (#FBBF24)
        
        # We need to map 'type' to color/outline based on STAGE
        
        colors = []
        lines = []
        opacities = []
        
        # Stage 0: All Gray
        if stage == 0:
            colors = ["#9CA3AF"] * N
            lines = [dict(width=0)] * N
            opacities = [0.8] * N
            
        # Stage 1: Virus (Show Truth)
        elif stage == 1:
            for t_type in df['type']:
                if t_type in ['TP', 'FN']: # Sick
                    colors.append("#EF4444")
                else:
                    colors.append("#9CA3AF")
                lines.append(dict(width=0))
                opacities.append(0.8)
                
        # Stage 2: Test (Add Yellow Borders)
        elif stage == 2:
            for t_type in df['type']:
                if t_type in ['TP', 'FN']: # Sick
                    colors.append("#EF4444")
                else:
                    colors.append("#9CA3AF")
                
                # Test logic
                if t_type in ['TP', 'FP']: # Positive Test
                    lines.append(dict(width=2, color="#FBBF24")) # Yellow Border
                else:
                    lines.append(dict(width=0))
                opacities.append(0.8)
                
        # Stage 3: Filter (Posteriori - Fade Negatives)
        elif stage == 3:
            for t_type in df['type']:
                if t_type in ['TP', 'FP']: # Positive Test (Keep Visible)
                    if t_type == 'TP': colors.append("#EF4444")
                    else: colors.append("#9CA3AF")
                    
                    lines.append(dict(width=2, color="#FBBF24"))
                    opacities.append(1.0)
                else: # Negative Test (Fade)
                    if t_type == 'FN': colors.append("#EF4444")
                    else: colors.append("#9CA3AF")
                    lines.append(dict(width=0))
                    opacities.append(0.1)

        # Plotly
        fig = go.Figure()
        
        # TRACE 1: Base Dots (No Borders)
        # Scattergl is efficient but "line" as array is flaky.
        # We just render the dots with their assigned colors.
        
        fig.add_trace(go.Scattergl(
            x=df['x'], y=df['y'],
            mode='markers',
            marker=dict(
                size=35,
                color=colors,
                opacity=opacities,
                line=dict(width=0) # explicit no border for base
            ),
            hoverinfo='none',
            showlegend=False
        ))
        
        # TRACE 2: Highlights (Yellow Borders)
        # If Stage >= 2, we need to show borders for TP/FP (or all? Original logic masked TP/FP).
        # In original logic: 
        #   Stage 2: TP/FP got yellow border. (Sick + HealthyPos)
        #   Stage 3: TP/FP kept yellow border.
        
        if stage >= 2:
            # We want to highlight 'TP' and 'FP' types
            mask_highlight = df['type'].isin(['TP', 'FP'])
            
            # Filter the dataframe to only these points
            df_high = df[mask_highlight]
            
            # The colors are already correct in the base trace.
            # We need an OVERLAY with transparent fill and Yellow Border.
            # BUT: Scattergl marker line width array support is the issue.
            # Here we are drawing specific set, so we can use a single line width/color for ALL in this trace.
            
            fig.add_trace(go.Scattergl(
                x=df_high['x'], y=df_high['y'],
                mode='markers',
                marker=dict(
                    size=35, # Match size
                    color='rgba(0,0,0,0)', # Transparent fill
                    line=dict(width=4, color='#FBBF24'), # Yellow border for all in this trace (thicker for visibility)
                    symbol='circle'
                ),
                hoverinfo='skip',
                showlegend=False
            ))
            
        fig.update_layout(
            xaxis=dict(visible=False, fixedrange=True),
            yaxis=dict(visible=False, fixedrange=True, scaleanchor="x"),
            margin=dict(l=0, r=0, t=10, b=10),
            height=400,
            showlegend=False,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)'
        )
        
        st.plotly_chart(fig, use_container_width=True, config={'staticPlot': True})
        
        # MATH DECODER
        if stage == 3:
            st.markdown(f"### {t({'de':'Die Auflösung', 'en':'The Reveal'})}")
            c_m1, c_m2 = st.columns(2)
            
            label_pos = t({'de': 'Positiv', 'en': 'Positive'})
            label_sick = t({'de': 'Krank', 'en': 'Sick'})
            label_fa = t({'de': 'Falsch Alarm', 'en': 'False Alarm'})
            
            with c_m1:
                st.write(t({"de": "Du siehst nur die gelb umrandeten Punkte:", "en": "You only see the yellow-bordered dots:"}))
                st.latex(fr"\text{{{label_pos}}} = 3 (\text{{{label_sick}}}) + 3 (\text{{{label_fa}}}) = 6")
            with c_m2:
                st.write(t({"de": "Davon sind krank:", "en": "Of those, sick are:"}))
                st.latex(fr"P(\text{{{label_sick}}}|\text{{{label_pos}}}) = \frac{{3}}{{6}} = 50\%")
            st.warning(t({"de": "Trotz 75% genauem Test ist die Chance nur 50%! Schau dir die Punkte an.", 
                          "en": "Despite 75% accuracy, the chance is only 50%! Look at the dots."}))

    st.markdown("---")

    # --- PART 2: MONTY HALL ---
    st.markdown("<br>", unsafe_allow_html=True)
    c_icon_2, c_title_2 = st.columns([0.1, 0.9], gap="small")
    with c_icon_2:
        st.markdown(f"<div style='display:flex; align-items:center; justify-content:center; height:100%;'>{render_icon('door-open', size=24, color='#000000')}</div>", unsafe_allow_html=True)
    with c_title_2:
        st.markdown(f"<h3 style='margin:0; padding-top:4px; color:#000000;'>{t(content_1_9['monty']['title'])}</h3>", unsafe_allow_html=True)
    
    with st.container(border=True):
        st.caption(t(content_1_9["monty"]["intro"]))
        
        # CONSTRAINTS
        st.markdown(f"**{t(content_1_9['monty']['constraints']['title'])}**")
        for rule in t(content_1_9['monty']['constraints']['list']):
            st.markdown(f"- {rule}")
            
        st.markdown("---")
        st.markdown(t(content_1_9["monty"]["anchor"]))
        
        # 100 DOORS INTUITION
        with st.expander(t(content_1_9["monty"]["intuition_100"]["title"])):
            st.markdown(t(content_1_9["monty"]["intuition_100"]["text"]))
        
        if st.button(t(content_1_9["monty"]["sim_btn"]), key="monty_sim"):
            # Simulation
            n_sim = 1000
            wins_switch = 0
            wins_stay = 0
            
            # Simple Monte Carlo
            # Door with Car: Random(3)
            # Choice: Random(3)
            # Stay: Win if Choice == Car (1/3)
            # Switch: Win if Choice != Car (2/3)
            
            # We can just simulate the outcome directly
            cars = np.random.randint(0, 3, n_sim)
            choices = np.random.randint(0, 3, n_sim)
            
            wins_stay = np.sum(cars == choices)
            wins_switch = n_sim - wins_stay
            
            st.session_state.monty_res = (wins_stay, wins_switch)
            
        if "monty_res" in st.session_state:
            stay, switch = st.session_state.monty_res
            
            # Bar Chart
            fig_m = go.Figure()
            fig_m.add_trace(go.Bar(
                x=[t({"de": "Bleiben", "en": "Stay"}), t({"de": "Wechseln", "en": "Switch"})],
                y=[stay, switch],
                marker_color=["#EF4444", "#10B981"],
                text=[f"{stay/10}%", f"{switch/10}%"],
                textposition='auto',
            ))
            fig_m.update_layout(height=250, margin=dict(t=10, b=10))
            st.plotly_chart(fig_m, use_container_width=True)
            
            if switch > stay:
                st.success(t({"de": "Beweis: Wechseln verdoppelt die Chance!", "en": "Proof: Switching doubles your chance!"}))
                
        # MATRIX EXPLANATION
        with st.expander(t(content_1_9["monty"]["matrix_title"])):
            st.markdown(t({
                "de": """
                | Deine Wahl | Auto ist hinter | Monty öffnet | Wechseln gewinnt? |
                |---|---|---|---|
                | **Tür 1** | Tür 1 | Tür 2/3 | Nein (Ziege) |
                | **Tür 1** | Tür 2 | Tür 3 (Zwang!) | **Ja (Auto)** |
                | **Tür 1** | Tür 3 | Tür 2 (Zwang!) | **Ja (Auto)** |
                
                Monty **muss** die Ziege zeigen. Das ist Information.
                """,
                "en": """
                | Your Pick | Car is behind | Monty opens | Switch wins? |
                |---|---|---|---|
                | **Door 1** | Door 1 | Door 2/3 | No (Goat) |
                | **Door 1** | Door 2 | Door 3 (Forced!) | **Yes (Car)** |
                | **Door 1** | Door 3 | Door 2 (Forced!) | **Yes (Car)** |
                
                Monty **must** show the goat. That is information.
                """
            }))

    st.markdown("---")

    # --- PART 3: BAYESIAN SEARCH ---
    st.markdown("<br>", unsafe_allow_html=True)
    c_icon_s, c_title_s = st.columns([0.1, 0.9], gap="small")
    with c_icon_s:
        st.markdown(f"<div style='display:flex; align-items:center; justify-content:center; height:100%;'>{render_icon('search', size=24, color='#000000')}</div>", unsafe_allow_html=True)
    with c_title_s:
        st.markdown(f"<h3 style='margin:0; padding-top:4px; color:#000000;'>{t(content_1_9['search']['title'])}</h3>", unsafe_allow_html=True)

    with st.container(border=True):
        st.markdown(t(content_1_9["search"]["story"]))
        # st.caption(t(content_1_9["search"]["instruction"])) # Replaced by Aggressive Guidance
        
        # INIT SEARCH
        GridSize = 6
        if "search_grid" not in st.session_state:
            # Gaussian Prior centered at 3,3
            x, y = np.meshgrid(np.arange(GridSize), np.arange(GridSize))
            d = np.sqrt((x-2.5)**2 + (y-2.5)**2)
            sigma, mu = 1.5, 0.0
            g = np.exp(-( (d-mu)**2 / ( 2.0 * sigma**2 ) ) )
            st.session_state.search_grid = g / np.sum(g) # Normalize to 1
            st.session_state.search_target = (np.random.randint(0, GridSize), np.random.randint(0, GridSize))
            st.session_state.search_found = False
            st.session_state.search_attempts = 0
            st.session_state.search_msg = ""
            st.session_state.search_last_click = None

        # AGGRESSIVE GUIDANCE HUD
        attempts = st.session_state.get("search_attempts", 0)
        found = st.session_state.search_found
        
        if found:
            st.balloons()
            st.success(t({
                "de": f"🎉 **Gefunden!** Du hast das Objekt nach {attempts} Versuchen lokalisiert.", 
                "en": f"🎉 **Found it!** You located the object after {attempts} attempts."
            }))
        elif attempts == 0:
            st.info(t({
                "de": "🔍 **Deine Mission:** Das Raster zeigt Wahrscheinlichkeiten. Klicke auf den **dunkelsten Sektor** (höchste Chance), um zu suchen.",
                "en": "🔍 **Your Mission:** The grid shows probabilities. Click the **darkest sector** (highest chance) to scan it."
            }))
        else:
            st.warning(t({
                "de": f"📉 **Misserfolg ({attempts}):** Nichts gefunden. Die Wahrscheinlichkeiten haben sich 'verteilt'. Suche weiter im neuen Hotspot!",
                "en": f"📉 **Miss ({attempts}):** Nothing found. Probabilities have 'flowed' elsewhere. Keep hunting the new hotspot!"
            }))

        st.markdown("<br>", unsafe_allow_html=True)

        # RENDER HEATMAP
        grid_data = st.session_state.search_grid
        
        # Annotate values for better clarity? Maybe too cluttered. Let's stick to hover/color.
        # Actually, let's add text for high prob cells? 
        # For now, clean heatmap is best for "Spatial Interaction".
        
        fig_s = go.Figure(data=go.Heatmap(
            z=grid_data,
            x=[chr(65+i) for i in range(GridSize)], # A, B, C...
            y=[str(i+1) for i in range(GridSize)], # 1, 2, 3...
            colorscale='Blues',
            zmin=0, zmax=np.max(grid_data),
            showscale=True,
            hoverongaps=False,
            hovertemplate='%{x}%{y}<br>Prob: %{z:.1%}<extra></extra>'
        ))
        
        # Add a marker for the last clicked spot if it was a miss
        if st.session_state.search_last_click and not found:
             last_c, last_r = st.session_state.search_last_click
             # Convert numeric index back to labels for plotting or just use indices if compatible?
             # Heatmap x/y are strings "A", "1". Plotly handles categorical axis overlap if we match values.
             fig_s.add_trace(go.Scatter(
                 x=[chr(65+last_c)], 
                 y=[str(last_r+1)],
                 mode='markers',
                 marker=dict(symbol='x', color='red', size=15, line=dict(width=2)),
                 showlegend=False,
                 hoverinfo='skip'
             ))

        fig_s.update_layout(
            height=400, 
            margin=dict(t=10, b=10, l=10, r=10),
            xaxis=dict(fixedrange=True, side='top'), # Axis on top like a map
            yaxis=dict(fixedrange=True, autorange='reversed'), # 1 at top convention? Or standard bottom-up? 
            # Standard matrix is typically 1 at top-left. Plotly Heatmap defaults 0 at bottom.
            # Let's keep Y axis standard (1 at bottom) to match school graphs, or reverse for matrix intuition.
            # The previous one used standard (1 at bottom). Let's stick to valid clicking.
            clickmode='event+select',
            dragmode=False
        )
        
        # INTERACTION EVENT
        event = st.plotly_chart(fig_s, on_select="rerun", selection_mode="points", use_container_width=True, key="bayes_search_map", config={'displayModeBar': False})
        
        if event and event["selection"]["points"] and not found:
            pt = event["selection"]["points"][0]
            # Plotly returns x and y coordinates. Since axes are categorical [A,B..] and [1,2..], 
            # pt['x'] might be 'A' or index? selection event usually provides 'point_index' for 1D, or x/y values.
            # For 2D Heatmap, point_index might be flattened index.
            # Safer to rely on x and y values if they are passed.
            
            click_x_val = pt.get("x") # "A" or index
            click_y_val = pt.get("y") # "1" or index
            
            # Robust Parsing for Categorical Axes
            # Plotly selection might return the Category Name (str) OR the index (int/float)
            try:
                # Handle X (Columns A-F)
                if isinstance(click_x_val, str):
                    c_idx = ord(click_x_val) - 65
                else:
                    c_idx = int(click_x_val)
                    
                # Handle Y (Rows 1-6)
                # Note: Y-axis title strings are "1", "2"... 
                if isinstance(click_y_val, str):
                    r_idx = int(click_y_val) - 1
                else:
                    r_idx = int(click_y_val) # If index, Plotly indices usually match the array index 0..N-1
                    # Double check if Heatmap data layout matches this. 
                    # If we passed y=["1","2"], index 0 is "1". So index 0 -> r_idx 0 is correct.
            
                # EXECUTE SEARCH LOGIC
                target = st.session_state.search_target
                st.session_state.search_attempts += 1
                st.session_state.search_last_click = (c_idx, r_idx)
                
                # Detection Prob (Power)
                P_D_given_O = 0.7 
                
                # IS IT THERE?
                is_there = (r_idx == target[1] and c_idx == target[0])
                
                found_now = False
                if is_there:
                    # Roll dice
                    if np.random.random() < P_D_given_O:
                        found_now = True
                        st.session_state.search_found = True
                        track_question_answer(model, "vwl", "1", "1.9", "1_9_search_mission", True)
                
                if not found_now:
                    # BAYES UPDATE
                    prob_k = grid_data[r_idx, c_idx]
                    prob_not_D_given_Ok = 1.0 - P_D_given_O
                    
                    # Numerator for k
                    num_k = prob_not_D_given_Ok * prob_k
                    
                    # Construct unnormalized grid
                    new_grid = grid_data.copy()
                    new_grid[r_idx, c_idx] = num_k 
                    
                    # Normalize
                    st.session_state.search_grid = new_grid / np.sum(new_grid)
                
                st.rerun()
                
            except Exception as e:
                st.error(f"Interaction Error: {e} | X: {click_x_val} ({type(click_x_val)}) Y: {click_y_val} ({type(click_y_val)})")

    st.markdown("---")

    # --- PART 4: CONCEPT CHECK (Three Prisoners) ---
    st.markdown("<br>", unsafe_allow_html=True)
    c_icon_3, c_title_3 = st.columns([0.1, 0.9], gap="small")
    with c_icon_3:
        st.markdown(f"<div style='display:flex; align-items:center; justify-content:center; height:100%;'>{render_icon('check-circle', size=24, color='#000000')}</div>", unsafe_allow_html=True)
    with c_title_3:
        st.markdown(f"<h3 style='margin:0; padding-top:4px; color:#000000;'>{t(content_1_9['quiz']['title'])}</h3>", unsafe_allow_html=True)
    
    with st.container(border=True):
        render_mcq(
            key_suffix="1_9_mcq",
            question_text=t(content_1_9["quiz"]["question"]),
            options=t(content_1_9["quiz"]["options"]),
            correct_idx=content_1_9["quiz"]["correct_idx"],
            solution_text_dict=content_1_9["quiz"]["solution"],
            success_msg_dict={"de": "Exakt.", "en": "Exactly."},
            error_msg_dict={"de": "Überlege: Hat der Wärter eine Wahl?", "en": "Think: Did the warden have a choice?"},
            model=model,
            ai_context="Bayes Theorem / Three Prisoners Problem",
            course_id="vwl", topic_id="1", subtopic_id="1.9", question_id="1_9_prisoners"
        )
