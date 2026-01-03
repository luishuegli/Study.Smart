import streamlit as st
import plotly.graph_objects as go
import numpy as np
import pandas as pd
from views.styles import render_icon, inject_equal_height_css
from utils.localization import t
from utils.localization import t
from utils.quiz_helper import render_mcq
from utils.progress_tracker import track_question_answer
from data.exam_questions import get_question

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
        "origin": {
            "title": {"de": "Die Ursprungsgeschichte (1990)", "en": "The Origin Story (1990)"},
            "text": {
                "de": """<strong>New York, 1990:</strong> Marilyn vos Savant (höchster IQ der Welt) veröffentlichte dieses Rätsel im <em>Parade Magazine</em>. Ihre Antwort: <strong>"Wechseln verdoppelt die Gewinnchance."</strong><br><br>Die Reaktion? Tausende Briefe, viele von Mathematik-PhDs, die sie beschimpften: <em>"Sie haben einen Fehler gemacht... als Mathematiker bin ich entsetzt!"</em><br><br>Warum irrten sich so viele Experten? Weil sie den Kontext ignorierten.""",
                "en": """<strong>New York, 1990:</strong> Marilyn vos Savant (highest IQ record) published this puzzle in <em>Parade Magazine</em>. Her answer: <strong>"Switching doubles your chance."</strong><br><br>The reaction? Thousands of letters, many from Math PhDs, calling her wrong: <em>"You made a mistake... as a mathematician I am appalled!"</em><br><br>Why did so many experts get it wrong? Because they ignored the context."""
            }
        },
        "constraints": {
            "title": {"de": "Das Spiel-Setup (Kontext ist alles)", "en": "The Game Setup (Context is King)"},
            "intro": {"de": "Du bist in einer Game Show. Der Host ist Monty Hall.", "en": "You are on a Game Show. The host is Monty Hall."},
            "list": {
                "de": [
                    "1. **Drei Türen:** Hinter einer ist ein **Auto** (Gewinn), hinter zwei sind **Ziegen** (Nieten).",
                    "2. **Deine Wahl:** Du wählst eine Tür (z.B. Tür 1).",
                    "3. **Montys Zwang:** Monty (der weiß, wo das Auto ist) **MUSS** eine andere Tür öffnen, hinter der eine **Ziege** steht.",
                    "4. **Das Angebot:** Monty fragt dich: *'Möchtest du zu der verbleibenden Tür wechseln?'*"
                ],
                "en": [
                    "1. **Three Doors:** Behind one is a **Car** (Win), behind two are **Goats** (Loss).",
                    "2. **Your Choice:** You pick a door (e.g., Door 1).",
                    "3. **Monty's Constraint:** Monty (who knows where the car is) **MUST** open another door revealing a **Goat**.",
                    "4. **The Offer:** Monty asks: *'Do you want to switch to the remaining door?'*"
                ]
            }
        },
        "intuition_100": {
            "title": {"de": "Der 50-Türen-Trick (Intuition Pump)", "en": "The 50 Doors Trick (Intuition Pump)"},
            "text": {
                "de": """Stell dir vor, es gibt <strong>50 Türen</strong>.<br><br>1. Du wählst <strong>Tür 1</strong>. Chance: <strong>1/50 (2%)</strong>.<br>2. Die 'Anderen' (Tür 2-50) haben zusammen <strong>49/50 (98%)</strong>.<br>3. Monty öffnet <strong>48</strong> dieser anderen Türen (alles Ziegen).<br>4. Nur <strong>Tür 50</strong> bleibt von den 'Anderen' übrig.<br><br><strong>Warum 48 Türen?</strong> Monty öffnet IMMER alle Ziegen-Türen ausser einer. Die 98% Wahrscheinlichkeit der 'Anderen' verschwinden nicht - sie konzentrieren sich auf die EINE überlebende Tür!<br><br><strong>Ergebnis:</strong> Tür 1 = 2%, Tür 50 = 98%. <strong>Wechseln!</strong>""",
                "en": """Imagine there are <strong>50 doors</strong>.<br><br>1. You pick <strong>Door 1</strong>. Chance: <strong>1/50 (2%)</strong>.<br>2. The 'Others' (Doors 2-50) have a combined <strong>49/50 (98%)</strong>.<br>3. Monty opens <strong>48</strong> of these other doors (all goats).<br>4. Only <strong>Door 50</strong> remains closed from the 'Others'.<br><br><strong>Why 48 doors?</strong> Monty ALWAYS opens all goat doors except one. The 98% probability of the 'Others' doesn't disappear - it CONCENTRATES on the ONE surviving door!<br><br><strong>Result:</strong> Door 1 = 2%, Door 50 = 98%. <strong>Switch!</strong>"""
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
        "title": {"de": "4. Logik-Check: 3 Gefangene", "en": "4. Logic Check: 3 Prisoners"}
    },
    
    # --- FRAG DICH (Ask Yourself) ---
    "frag_dich": {
        "header": {"de": "Frag dich: Bayes oder Totale Wahrscheinlichkeit?", "en": "Ask yourself: Bayes or Total Probability?"},
        "questions": [
            {"de": "Habe ich einen <strong>Prior</strong> (was ich VORHER glaube)?", "en": "Do I have a <strong>prior</strong> (what I believe BEFORE)?"},
            {"de": "Bekomme ich <strong>neue Evidenz</strong> (z.B. Testergebnis)?", "en": "Do I get <strong>new evidence</strong> (e.g., test result)?"},
            {"de": "Muss ich <strong>rückwärts</strong> rechnen (Effekt → Ursache)?", "en": "Do I need to calculate <strong>backwards</strong> (effect → cause)?"},
            {"de": "Kenne ich $P(B|A)$ aber brauche $P(A|B)$?", "en": "Do I know $P(B|A)$ but need $P(A|B)$?"}
        ],
        "conclusion": {"de": "Alle JA? → Bayes! Vorwärts (Ursache → Effekt)? → Totale Wahrscheinlichkeit.", "en": "All YES? → Bayes! Forward (cause → effect)? → Total Probability."}
    },
    
    # --- EXAM ESSENTIALS ---
    "exam_essentials": {
        "trap": {
            "de": "Base Rate Fallacy! Ein positiver Test bedeutet NICHT automatisch 'wahrscheinlich krank' — es hängt von der <strong>Seltenheit der Krankheit</strong> ab.",
            "en": "Base Rate Fallacy! A positive test does NOT automatically mean 'probably sick' — it depends on the <strong>rarity of the disease</strong>."
        },
        "trap_rule": {
            "de": "Faustregel: Je seltener die Krankheit (Prior), desto mehr falsch-positive überschwemmen die wahr-positiven.",
            "en": "Rule of thumb: The rarer the disease (prior), the more false positives swamp the true positives."
        },
        "tips": [
            {
                "tip": {"de": "Prior × Likelihood ÷ Normalizer = Posterior", "en": "Prior × Likelihood ÷ Normalizer = Posterior"},
                "why": {"de": "Die Bayes-Formel in Worten: $P(A|B) = \\frac{P(B|A) \\cdot P(A)}{P(B)}$", "en": "The Bayes formula in words: $P(A|B) = \\frac{P(B|A) \\cdot P(A)}{P(B)}$"}
            },
            {
                "tip": {"de": "Monty Hall: Wechseln verdoppelt die Gewinnchance!", "en": "Monty Hall: Switching doubles your chance!"},
                "why": {"de": "Du gewinnst durch Wechseln immer dann, wenn du anfangs FALSCH lagst (2/3 Chance).", "en": "You win by switching whenever you were WRONG initially (2/3 chance)."}
            },
            {
                "tip": {"de": "P(B) oft mit Totaler Wahrscheinlichkeit berechnen", "en": "P(B) often calculated with Total Probability"},
                "why": {"de": "$P(B) = P(B|A) \\cdot P(A) + P(B|\\neg A) \\cdot P(\\neg A)$ — alle Pfade summieren.", "en": "$P(B) = P(B|A) \\cdot P(A) + P(B|\\neg A) \\cdot P(\\neg A)$ — sum all paths."}
            }
        ]
    }
}

def render_subtopic_1_9(model):
    """1.9 Bayes Theorem - Medical Detective & Monty Hall & Bayesian Search"""
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
    st.markdown("---")
    
    # --- THEORY: BAYES THEOREM (Stupid Person Rule Applied) ---
    # Header OUTSIDE container (Header-Out Protocol)
    st.markdown(f"### {t({'de': 'Das Bayes-Theorem', 'en': 'Bayes Theorem'})}")
    
    # Intuition OUTSIDE and ABOVE container
    from utils.layouts.foundation import intuition_box
    intuition_box({
        "de": "Du glaubst etwas über die Welt (z.B. 'Ich bin wahrscheinlich gesund'). Dann bekommst du neue Information (z.B. 'Der Test war positiv!'). Bayes sagt dir, wie du deine Meinung UPDATE sollst.",
        "en": "You believe something about the world (e.g., 'I'm probably healthy'). Then you get new information (e.g., 'The test was positive!'). Bayes tells you how to UPDATE your belief."
    })
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    with st.container(border=True):
        # The Formula
        st.latex(r"P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}")
        
        st.markdown("---")
        
        # Variable Decoder (The Critical Part)
        st.markdown(f"**{t({'de': 'Die Variablen erklärt', 'en': 'The Variables Explained'})}:**")
        st.markdown(f"""
• $P(A)$ = **{t({"de": "Prior", "en": "Prior"})}** — {t({"de": "Was du VORHER glaubst", "en": "What you believe BEFORE"})}

• $P(B|A)$ = **{t({"de": "Likelihood", "en": "Likelihood"})}** — {t({"de": "Wie gut ist der Beweis?", "en": "How good is the evidence?"})}

• $P(B)$ = **{t({"de": "Normalisierung", "en": "Normalizer"})}** — {t({"de": "Wie oft sehen wir diesen Beweis überhaupt?", "en": "How often do we see this evidence at all?"})}

• $P(A|B)$ = **{t({"de": "Posterior", "en": "Posterior"})}** — {t({"de": "Deine NEUE Überzeugung", "en": "Your NEW belief"})}
""")
        
        st.markdown("---")
        
        # The Key Insight
        st.markdown(f"*{t({'de': 'Ein positiver Test bedeutet NICHT automatisch, dass du krank bist! Es hängt davon ab, wie SELTEN die Krankheit ist (Prior) und wie GUT der Test ist (Likelihood).', 'en': 'A positive test does NOT automatically mean you are sick! It depends on how RARE the disease is (Prior) and how GOOD the test is (Likelihood).'})}*")
    
    st.markdown("<br>", unsafe_allow_html=True)

    # --- PART 1: MEDICAL DETECTIVE (1000 Dots) ---
    # --- PART 1: MEDICAL DETECTIVE (N=16 Intuition) ---
    st.markdown(f"### 1. {t(content_1_9['mission']['title'])}")
    
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
                    "de": "**Anker:** Wir starten mit einer Bevölkerung von 16. Aktuell könnte *jeder* krank sein. Wir wissen nichts.",
                    "en": "**Anchor:** We start with a population of 16. At this point, *anyone* could be sick. We know nothing."
                }))
            
            elif stage == 1:
                st.markdown(t({
                    "de": f"**Die Wahrheit:** In unserer Welt sind $P(S) = 4/16$ krank. Nur die **{render_icon('circle', color='#FF4B4B')} Roten Punkte** sind betroffen.",
                    "en": f"**The Truth:** In our world, $P(S) = 4/16$ are sick. Only the **{render_icon('circle', color='#FF4B4B')} Red Dots** are affected."
                }), unsafe_allow_html=True)
            
            elif stage == 2:
                st.warning(t({
                    "de": "**Das Testergebnis:** Schau dir die gelben Ränder an! Der Test hat 3 Kranke 'erwischt', aber auch 3 Gesunde 'falsch verdächtigt'.",
                    "en": "**The Test Result:** Look at the yellow borders! The test 'caught' 3 sick people, but it also 'falsely accused' 3 healthy people."
                }))
                st.latex(r"P(+|S) = 75\% \text{ (Sensitivity)} \quad P(+|H) = 25\% \text{ (False Positive Rate)}")
    
            elif stage == 3:
                st.success(t({
                    "de": "**Der Filter:** Wir ignorieren alle ohne gelben Rand. Dein neues Universum sind NUR die 6 Personen mit positivem Test.",
                    "en": "**The Filter:** We ignore everyone without a yellow border. Your new universe is ONLY the 6 people with a positive test."
                }))
                
                if user := st.session_state.get("user"):
                    track_question_answer(user["localId"], "vwl", "1", "1.9", "1_9_medical_mission", True)
                
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
    st.markdown(f"### {t(content_1_9['monty']['title'])}")
    st.caption(t(content_1_9["monty"]["intro"]))
    
    # =========================================================================
    # SECTION 1: THE SETUP (Collapsible)
    # =========================================================================
    with st.expander(t({"de": "Die Geschichte & Regeln", "en": "The Story & Rules"}), expanded=False):
        # Origin Story
        st.markdown(f"#### {t(content_1_9['monty']['origin']['title'])}")
        st.markdown(f"""
<div style="background: #f4f4f5; border-left: 4px solid #a1a1aa; padding: 12px 16px; border-radius: 8px; color: #3f3f46;">
{t(content_1_9["monty"]["origin"]["text"])}
</div>
""", unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Game Setup
        st.markdown(f"#### {t(content_1_9['monty']['constraints']['title'])}")
        st.markdown(t(content_1_9["monty"]["constraints"]["intro"]))
        for rule in t(content_1_9['monty']['constraints']['list']):
            st.markdown(f"- {rule}")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # 50 Doors Intuition
        st.markdown(f"#### {t(content_1_9['monty']['intuition_100']['title'])}")
        st.markdown(f"""
<div style="background: #f4f4f5; border-left: 4px solid #a1a1aa; padding: 12px 16px; border-radius: 8px; color: #3f3f46; box-sizing: border-box; word-wrap: break-word; overflow-wrap: break-word;">
{t(content_1_9["monty"]["intuition_100"]["text"])}
</div>
""", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # =========================================================================
    # SECTION 2: THE LAB (Main Focus - Game + Live Stats)
    # =========================================================================
    st.markdown(f"#### {t({'de': 'Das Experiment', 'en': 'The Experiment'})}")
    
    with st.container(border=True):
        
        @st.fragment
        def monty_hall_lab():
            import random
            
            # Initialize unified state
            if "mh" not in st.session_state:
                st.session_state.mh = {
                    "game": {
                        "car": random.randint(0, 2),
                        "phase": "PICK",
                        "user_pick": None,
                        "monty_reveal": None,
                    },
                    "stats": {
                        "games_played": 0,
                        "stay_wins": 0,
                        "stay_losses": 0,
                        "switch_wins": 0,
                        "switch_losses": 0,
                    }
                }
            
            g = st.session_state.mh["game"]
            stats = st.session_state.mh["stats"]
            
            # Door labels
            door_labels = [
                t({"de": "Tür 1", "en": "Door 1"}),
                t({"de": "Tür 2", "en": "Door 2"}),
                t({"de": "Tür 3", "en": "Door 3"})
            ]
            
            # --- GAME DOORS ---
            d1, d2, d3 = st.columns(3, gap="small")
            
            for i, col in enumerate([d1, d2, d3]):
                with col:
                    if g["phase"] == "PICK":
                        label = f"🚪 {door_labels[i]}"
                        btn_type = "secondary"
                        disabled = False
                    elif g["phase"] == "REVEALED":
                        if i == g["monty_reveal"]:
                            label = f"🐐 {door_labels[i]}"
                            btn_type = "secondary"
                            disabled = True
                        elif i == g["user_pick"]:
                            label = f"🚪 {door_labels[i]} ✓"
                            btn_type = "primary"
                            disabled = True
                        else:
                            label = f"🚪 {door_labels[i]}"
                            btn_type = "secondary"
                            disabled = True
                    else:  # RESULT
                        if i == g["car"]:
                            label = f"🚗 {door_labels[i]}"
                            btn_type = "primary" if g.get("won") else "secondary"
                        else:
                            label = f"🐐 {door_labels[i]}"
                            btn_type = "secondary"
                        disabled = True
                    
                    if st.button(label, key=f"mh_door_{i}", use_container_width=True, 
                                type=btn_type, disabled=disabled):
                        if g["phase"] == "PICK":
                            g["user_pick"] = i
                            goat_doors = [d for d in range(3) if d != i and d != g["car"]]
                            g["monty_reveal"] = random.choice(goat_doors)
                            g["phase"] = "REVEALED"
                            st.rerun(scope="fragment")
            
            # --- STAY/SWITCH BUTTONS ---
            if g["phase"] == "REVEALED":
                st.markdown("<br>", unsafe_allow_html=True)
                st.markdown(f"**{t({'de': 'Monty zeigt eine Ziege! Was tust du?', 'en': 'Monty reveals a goat! What do you do?'})}**")
                
                remaining_door = [d for d in range(3) if d != g["user_pick"] and d != g["monty_reveal"]][0]
                
                b1, b2 = st.columns(2)
                with b1:
                    if st.button(t({"de": "Bleiben", "en": "Stay"}), key="mh_stay", 
                                use_container_width=True, type="secondary"):
                        won = g["user_pick"] == g["car"]
                        g["won"] = won
                        g["choice"] = "STAY"
                        g["phase"] = "RESULT"
                        stats["games_played"] += 1
                        if won:
                            stats["stay_wins"] += 1
                        else:
                            stats["stay_losses"] += 1
                        st.rerun(scope="fragment")
                with b2:
                    if st.button(t({"de": "Wechseln", "en": "Switch"}), key="mh_switch", 
                                use_container_width=True, type="primary"):
                        won = remaining_door == g["car"]
                        g["won"] = won
                        g["choice"] = "SWITCH"
                        g["phase"] = "RESULT"
                        stats["games_played"] += 1
                        if won:
                            stats["switch_wins"] += 1
                        else:
                            stats["switch_losses"] += 1
                        st.rerun(scope="fragment")
            
            # --- RESULT + NEXT GAME ---
            if g["phase"] == "RESULT":
                st.markdown("<br>", unsafe_allow_html=True)
                if g["won"]:
                    st.success(t({"de": "Gewonnen! Du hast das Auto!", "en": "You won! You got the car!"}))
                else:
                    st.error(t({"de": "Verloren. Du hast eine Ziege.", "en": "You lost. You got a goat."}))
                
                if st.button(t({"de": "Nächstes Spiel", "en": "Next Game"}), key="mh_next"):
                    st.session_state.mh["game"] = {
                        "car": random.randint(0, 2),
                        "phase": "PICK",
                        "user_pick": None,
                        "monty_reveal": None,
                    }
                    st.rerun(scope="fragment")
            
            # --- LIVE STATS ---
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown("---")
            
            total_stay = stats["stay_wins"] + stats["stay_losses"]
            total_switch = stats["switch_wins"] + stats["switch_losses"]
            total = stats["games_played"]
            
            stay_pct = (stats["stay_wins"] / total_stay * 100) if total_stay > 0 else 0
            switch_pct = (stats["switch_wins"] / total_switch * 100) if total_switch > 0 else 0
            
            st.markdown(f"**{t({'de': 'Deine Ergebnisse', 'en': 'Your Results'})}** ({total} {t({'de': 'Spiele', 'en': 'games'})})")
            
            c1, c2 = st.columns(2)
            with c1:
                st.markdown(f"""
<div style="background: #f4f4f5; border-radius: 8px; padding: 12px; text-align: center;">
    <div style="font-size: 1.5rem; font-weight: 700; color: #3f3f46;">{stay_pct:.0f}%</div>
    <div style="font-size: 0.85rem; color: #71717a;">{t({"de": "Bleiben gewinnt", "en": "Stay Wins"})}</div>
    <div style="font-size: 0.75rem; color: #a1a1aa;">{stats["stay_wins"]}/{total_stay}</div>
</div>
""", unsafe_allow_html=True)
            with c2:
                st.markdown(f"""
<div style="background: #f4f4f5; border-radius: 8px; padding: 12px; text-align: center;">
    <div style="font-size: 1.5rem; font-weight: 700; color: #3f3f46;">{switch_pct:.0f}%</div>
    <div style="font-size: 0.85rem; color: #71717a;">{t({"de": "Wechseln gewinnt", "en": "Switch Wins"})}</div>
    <div style="font-size: 0.75rem; color: #a1a1aa;">{stats["switch_wins"]}/{total_switch}</div>
</div>
""", unsafe_allow_html=True)
            
            # --- FAST FORWARD BUTTON (unlocks after 2 games) ---
            if total >= 2:
                st.markdown("<br>", unsafe_allow_html=True)
                st.caption(t({"de": "Simuliert 1000 Spiele mit zufälliger Wahl, dann Stay vs Switch", 
                              "en": "Simulates 1000 games with random pick, then Stay vs Switch"}))
                if st.button(t({"de": "1000 Spiele simulieren", "en": "Simulate 1000 Games"}), 
                            key="mh_fast_forward", use_container_width=True, type="primary"):
                    # Run simulation
                    cars = np.random.randint(0, 3, 1000)
                    choices = np.random.randint(0, 3, 1000)
                    sim_stay_wins = np.sum(cars == choices)
                    sim_switch_wins = 1000 - sim_stay_wins
                    
                    # Add to existing stats
                    stats["stay_wins"] += sim_stay_wins
                    stats["stay_losses"] += (1000 - sim_stay_wins)
                    stats["switch_wins"] += sim_switch_wins
                    stats["switch_losses"] += (1000 - sim_switch_wins)
                    stats["games_played"] += 1000
                    
                    st.rerun(scope="fragment")
                
                if total >= 100:
                    st.success(t({"de": "Beweis: Wechseln verdoppelt die Gewinnchance!", 
                                  "en": "Proof: Switching doubles your chance!"}))
        
        # Render the lab
        monty_hall_lab()
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # =========================================================================
    # 50 DOORS INTUITION PUMP (Interactive)
    # =========================================================================
    st.markdown(f"#### {t({'de': 'Der 50-Türen-Trick', 'en': 'The 50 Doors Trick'})}")
    st.caption(t({"de": "Warum Wechseln so offensichtlich richtig ist, wenn man es grösser denkt", 
                  "en": "Why switching is obviously correct when you scale it up"}))
    
    with st.container(border=True):
        
        @st.fragment
        def fifty_doors_demo():
            import random
            
            N_DOORS = 50
            
            # Initialize state
            if "fd" not in st.session_state:
                st.session_state.fd = {
                    "phase": "PICK",  # PICK, ELIMINATED, FINAL
                    "car": random.randint(0, N_DOORS - 1),
                    "user_pick": None,
                    "eliminated": [],
                    "survivor": None
                }
            
            fd = st.session_state.fd
            
            # --- PHASE: PICK ---
            if fd["phase"] == "PICK":
                st.markdown(f"**{t({'de': 'Wähle eine Tür (1-50):', 'en': 'Pick a door (1-50):'})}**")
                
                # Show 50 doors as a grid (5 columns x 10 rows - wider buttons)
                for row in range(10):
                    cols = st.columns(5)
                    for col_idx, col in enumerate(cols):
                        door_num = row * 5 + col_idx
                        with col:
                            if st.button(f"{door_num + 1}", key=f"fd_door_{door_num}", 
                                        use_container_width=True):
                                fd["user_pick"] = door_num
                                # Determine survivor (the one door Monty leaves from "Others")
                                if fd["car"] == door_num:
                                    # User picked the car - survivor is random other door
                                    others = [d for d in range(N_DOORS) if d != door_num]
                                    fd["survivor"] = random.choice(others)
                                else:
                                    # User didn't pick car - survivor IS the car
                                    fd["survivor"] = fd["car"]
                                # Eliminate all others except user pick and survivor
                                fd["eliminated"] = [d for d in range(N_DOORS) 
                                                   if d != door_num and d != fd["survivor"]]
                                fd["phase"] = "ELIMINATED"
                                st.rerun(scope="fragment")
            
            # --- PHASE: ELIMINATED ---
            elif fd["phase"] == "ELIMINATED":
                st.markdown(f"**{t({'de': 'Monty öffnet 48 Türen...', 'en': 'Monty opens 48 doors...'})}**")
                
                # Show doors with eliminated ones as goats
                for row in range(10):
                    cols = st.columns(5)
                    for col_idx, col in enumerate(cols):
                        door_num = row * 5 + col_idx
                        with col:
                            if door_num == fd["user_pick"]:
                                st.markdown(f"<div style='background: #18181b; color: white; padding: 8px; border-radius: 6px; text-align: center; font-weight: bold;'>{door_num + 1}</div>", unsafe_allow_html=True)
                            elif door_num == fd["survivor"]:
                                st.markdown(f"<div style='background: #f4f4f5; padding: 8px; border-radius: 6px; text-align: center; font-weight: bold; border: 2px solid #18181b;'>{door_num + 1}</div>", unsafe_allow_html=True)
                            else:
                                st.markdown(f"<div style='background: #fecaca; color: #991b1b; padding: 8px; border-radius: 6px; text-align: center; font-size: 0.75rem;'>🐐</div>", unsafe_allow_html=True)
                
                st.markdown("<br>", unsafe_allow_html=True)
                
                # Show the choice
                user_door = fd["user_pick"] + 1
                survivor_door = fd["survivor"] + 1
                
                st.markdown(f"""
<div style="background: #f4f4f5; padding: 16px; border-radius: 8px;">
<strong>{t({"de": "Die Situation:", "en": "The Situation:"})}</strong><br><br>
{t({"de": f"Deine Tür ({user_door}): 1/50 = <strong>2%</strong>", "en": f"Your Door ({user_door}): 1/50 = <strong>2%</strong>"})}
<br>
{t({"de": f"Die Überlebende ({survivor_door}): 49/50 = <strong>98%</strong>", "en": f"The Survivor ({survivor_door}): 49/50 = <strong>98%</strong>"})}
<br><br>
<strong>{t({"de": "Die 98% sind nicht verschwunden - sie haben sich auf EINE Tür konzentriert!", "en": "The 98% didn't disappear - they CONCENTRATED on ONE door!"})}</strong>
</div>
""", unsafe_allow_html=True)
                
                st.markdown("<br>", unsafe_allow_html=True)
                
                c1, c2 = st.columns(2)
                with c1:
                    if st.button(t({"de": "Bleiben", "en": "Stay"}), key="fd_stay", use_container_width=True):
                        fd["choice"] = "STAY"
                        fd["won"] = fd["user_pick"] == fd["car"]
                        fd["phase"] = "FINAL"
                        st.rerun(scope="fragment")
                with c2:
                    if st.button(t({"de": "Wechseln", "en": "Switch"}), key="fd_switch", 
                                use_container_width=True, type="primary"):
                        fd["choice"] = "SWITCH"
                        fd["won"] = fd["survivor"] == fd["car"]
                        fd["phase"] = "FINAL"
                        st.rerun(scope="fragment")
            
            # --- PHASE: FINAL ---
            elif fd["phase"] == "FINAL":
                if fd["won"]:
                    st.success(t({"de": "Gewonnen! Du hast das Auto!", "en": "You won! You got the car!"}))
                else:
                    st.error(t({"de": "Verloren. Du hast eine Ziege.", "en": "You lost. You got a goat."}))
                
                car_door = fd["car"] + 1
                st.markdown(f"*{t({'de': f'Das Auto war hinter Tür {car_door}.', 'en': f'The car was behind Door {car_door}.'})}*")
                
                if st.button(t({"de": "Nochmal spielen", "en": "Play Again"}), key="fd_reset"):
                    st.session_state.fd = {
                        "phase": "PICK",
                        "car": random.randint(0, N_DOORS - 1),
                        "user_pick": None,
                        "eliminated": [],
                        "survivor": None
                    }
                    st.rerun(scope="fragment")
        
        fifty_doors_demo()
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # =========================================================================
    # SECTION 3: THE PROOF (Expander)
    # =========================================================================
    with st.expander(t(content_1_9['monty']['matrix_title'])):
        st.markdown(t({
            "de": """
| Deine Wahl | Auto ist hinter | Monty öffnet | Wechseln gewinnt? |
|---|---|---|---|
| **Tür 1** | Tür 1 | Tür 2/3 | Nein (Ziege) |
| **Tür 1** | Tür 2 | Tür 3 (Zwang!) | **Ja (Auto)** |
| **Tür 1** | Tür 3 | Tür 2 (Zwang!) | **Ja (Auto)** |

**Die Logik:** Wenn du bleibst, musst du von Anfang an richtig liegen (Chance 1/3). Wenn du wechselst, gewinnst du immer dann, wenn du anfangs *falsch* lagst (Chance 2/3).
            """,
            "en": """
| Your Pick | Car is behind | Monty opens | Switch wins? |
|---|---|---|---|
| **Door 1** | Door 1 | Door 2/3 | No (Goat) |
| **Door 1** | Door 2 | Door 3 (Forced!) | **Yes (Car)** |
| **Door 1** | Door 3 | Door 2 (Forced!) | **Yes (Car)** |

**The Logic:** If you stay, you must be right from the start (1/3 chance). If you switch, you win whenever you were *wrong* initially (2/3 chance).
            """
        }))

    st.markdown("---")

    # --- PART 3: BAYESIAN SEARCH ---
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"### {t(content_1_9['search']['title'])}")

    with st.container(border=True):
        st.markdown(t(content_1_9["search"]["story"]))
        
        # INIT SEARCH (Smaller grid for faster gameplay)
        GridSize = 4
        if "search_grid" not in st.session_state:
            # Gaussian Prior centered at center of grid
            x, y = np.meshgrid(np.arange(GridSize), np.arange(GridSize))
            center = (GridSize - 1) / 2
            d = np.sqrt((x-center)**2 + (y-center)**2)
            sigma, mu = 1.0, 0.0
            g = np.exp(-( (d-mu)**2 / ( 2.0 * sigma**2 ) ) )
            st.session_state.search_grid = g / np.sum(g) # Normalize to 1
            # Fix: Target must be generated based on the probability distribution!
            # Flatten grid and sample index
            flat_probs = st.session_state.search_grid.flatten()
            flat_idx = np.random.choice(len(flat_probs), p=flat_probs)
            t_r, t_c = divmod(flat_idx, GridSize)
            st.session_state.search_target = (t_c, t_r)
            st.session_state.search_found = False
            st.session_state.search_attempts = 0
            st.session_state.search_msg = ""
            st.session_state.search_last_click = None
            st.session_state.search_history = [] # List of (r, c) misses

        # AGGRESSIVE GUIDANCE HUD
        attempts = st.session_state.get("search_attempts", 0)
        found = st.session_state.search_found
        
        if found:
            st.balloons()
            
            # Simplified Success UI (User Request: "Clean up layout")
            st.success(t({
                "de": f"**Gefunden!** Du hast das Objekt nach {attempts} Versuchen lokalisiert.\n\nDa unser Sensor jetzt 'perfekt' ist (100% Detection), hast du systematisch alle leeren Sektoren eliminiert. Das ist die Extremform von Bayes: P(Ort|Miss) = 0.", 
                "en": f"**Found it!** You located the object after {attempts} attempts.\n\nSince our sensor is now 'perfect' (100% detection), you systematically eliminated all empty sectors. This is the extreme form of Bayes: P(Location|Miss) = 0."
            }))
        elif attempts == 0:
            st.info(t({
                "de": "**Deine Mission:** Das Raster zeigt Wahrscheinlichkeiten. Klicke auf den **dunkelsten Sektor** (höchste Chance), um zu suchen.",
                "en": "**Your Mission:** The grid shows probabilities. Click the **darkest sector** (highest chance) to scan it."
            }))
        else:
            # Pedagogical Feedback: Explain the "Water Flow"
            last_click = st.session_state.search_history[-1] if st.session_state.search_history else None
            coord_str = f"{chr(65+last_click[0])}{last_click[1]+1}" if last_click else "?"
            
            st.warning(f"**Miss at {coord_str}:** {t({'de': 'Nichts gefunden.', 'en': 'Nothing found.'})}")
            
            # The "Aha!" Moment Visualization
            c_narrative, c_math = st.columns([0.7, 0.3])
            with c_narrative:
                st.caption(t({
                    "de": "**Was ist gerade passiert?** Da du dort *nichts* gefunden hast, ist es *unwahrscheinlicher*, dass das Objekt dort ist. Diese 'verlorene' Wahrscheinlichkeit verschwindet nicht – sie **fließt** wie Wasser auf die anderen Zellen.",
                    "en": "**What happened?** Since you found *nothing* there, it's now *less likely* to be there. This 'lost' probability doesn't vanish—it **flows** like water to the other cells."
                }))
            with c_math:
                st.metric(
                    label="Probability Shift", 
                    value="Distributed", 
                    delta="Spread to neighbors"
                )

        st.markdown("<br>", unsafe_allow_html=True)

        # RENDER: HYBRID APPROACH
        # 1. Heatmap for perfect seamless visuals
        # 2. Transparent Scatter layer for reliable clicks
        
        grid_data = st.session_state.search_grid
        
        # Prepare Plot Data
        # If found, we want the target cell to be "White" (0 probability visually) 
        # so the ship pops out, similar to how X's are on white.
        plot_grid = grid_data.copy()
        if found:
             t_c, t_r = st.session_state.search_target
             plot_grid[t_r, t_c] = 0.0
        
        # Prepare data for scatter layer
        x_coords = []
        y_coords = []
        hover_texts = []
        
        for row in range(GridSize):
            for col in range(GridSize):
                x_coords.append(chr(65 + col))  # A, B, C...
                y_coords.append(str(row + 1))    # 1, 2, 3...
                prob_val = grid_data[row, col]
                hover_texts.append(f"{chr(65+col)}{row+1}<br>Prob: {prob_val:.1%}")
        
        fig_s = go.Figure()
        
        # TRACE 0: Visual Heatmap (Background)
        fig_s.add_trace(go.Heatmap(
            z=plot_grid,
            x=[chr(65+i) for i in range(GridSize)],
            y=[str(i+1) for i in range(GridSize)],
            colorscale='Blues',
            zmin=0, zmax=np.max(grid_data),
            showscale=True,
            hoverongaps=False,
            hoverinfo='skip' # Handled by scatter
        ))
        
        # TRACE 1: Invisible Clickable Layer (Foreground)
        fig_s.add_trace(go.Scatter(
            x=x_coords,
            y=y_coords,
            mode='markers',
            marker=dict(
                size=60, # Large enough to be easily clickable
                color='rgba(0,0,0,0)', # Invisible
                symbol='square',
            ),
            text=hover_texts,
            hovertemplate='%{text}<extra></extra>',
            showlegend=False
        ))
        
        import base64

        # TRACE 2: Miss Markers (X)
        for m_c, m_r in st.session_state.search_history:
            fig_s.add_trace(go.Scatter(
                x=[chr(65+m_c)], 
                y=[str(m_r+1)],
                mode='markers',
                marker=dict(symbol='x', color='red', size=20, line=dict(width=3)),
                showlegend=False,
                hoverinfo='skip'
            ))

        # TRACE 3: FOUND SHIP (If found)
        if found:
            t_c, t_r = st.session_state.search_target
            
            # Black Ship SVG, slightly smaller
            ship_svg = """<svg xmlns="http://www.w3.org/2000/svg" width="60" height="60" viewBox="0 0 24 24" fill="none" stroke="#000000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 21c.6.5 1.2 1 2.5 1 2.5 0 2.5-2 5-2 1.3 0 1.9.5 2.5 1 .6.5 1.2 1 2.5 1 2.5 0 2.5-2 5-2 1.3 0 1.9.5 2.5 1"/><path d="M19.38 20A11.6 11.6 0 0 0 21 14l-9-4-9 4c0 2.9.9 5.8 2.5 8"/><path d="M10 10V4a2 2 0 0 1 2-2a2 2 0 0 1 2 2v6"/><polyline points="14 7 8 7"/></svg>"""
            
            b64_ship = base64.b64encode(ship_svg.encode('utf-8')).decode("utf-8")
            ship_uri = f"data:image/svg+xml;base64,{b64_ship}"
            
            # Add image overlay
            fig_s.add_layout_image(
                dict(
                    source=ship_uri,
                    xref="x",
                    yref="y",
                    x=chr(65+t_c),
                    y=str(t_r+1),
                    sizex=0.7, # Smaller
                    sizey=0.7,
                    xanchor="center",
                    yanchor="middle",
                    layer="above"
                )
            )

        fig_s.update_layout(
            height=400,
            width=500, # Constrain width to help aspect ratio
            margin=dict(t=30, b=10, l=10, r=10),
            xaxis=dict(
                fixedrange=True, 
                side='top',
                title=None
            ),
            yaxis=dict(
                fixedrange=True, 
                autorange='reversed',
                scaleanchor='x', # Force square aspect ratio
                scaleratio=1,
                title=None
            ),
            clickmode='event+select',
            plot_bgcolor='rgba(0,0,0,0)',
            showlegend=False
        )
        
        # INTERACTION EVENT
        event = st.plotly_chart(fig_s, on_select="rerun", selection_mode="points", use_container_width=True, key="bayes_search_map", config={'displayModeBar': False})
        
        if event and event.get("selection") and event["selection"].get("points") and not found:
            clicked_point = event["selection"]["points"][0]
            
            # HANDLE CLICKS
            # Note: Clicks might register on Trace 0 (Heatmap) or Trace 1 (Scatter) depending on Plotly version quirks.
            # We standardize by calculating index from x/y if possible, or using point_index from Scatter.
            
            # Fallback to point_index which is ROBUST for this grid
            # Trace 1 is the Scatter layer
            if clicked_point.get("curve_number") == 1:
                point_idx = clicked_point.get("point_index")
                if point_idx is not None:
                    c_idx = point_idx % GridSize
                    r_idx = point_idx // GridSize

            if c_idx is not None and r_idx is not None:
                try:
                    # EXECUTE SEARCH LOGIC
                    target = st.session_state.search_target
                    st.session_state.search_attempts += 1
                    
                    # Detection Prob (Power) - 100% (Elimination) to avoid user frustration
                    # Teacher Mode: "Sensor is perfect now"
                    P_D_given_O = 1.0 
                    
                    # IS IT THERE?
                    is_there = (r_idx == target[1] and c_idx == target[0])
                    
                    found_now = False
                    if is_there:
                        # 100% Detection if it's there
                        if np.random.random() < P_D_given_O:
                            found_now = True
                            st.session_state.search_found = True
                            if user := st.session_state.get("user"):
                                track_question_answer(user["localId"], "vwl", "1", "1.9", "1_9_search_mission", True)
                    
                    if not found_now:
                        # BAYES UPDATE (ELIMINATION)
                        # P(Miss | ObjectThere) = 0.0 (Impossible with 100% sensor)
                        # P(Miss | ObjectNotThere) = 1.0
                        
                        prob_k = grid_data[r_idx, c_idx]
                        prob_not_D_given_Ok = 1.0 - P_D_given_O # 0.0
                        
                        num_k = prob_not_D_given_Ok * prob_k # Becomes 0.0
                        
                        new_grid = grid_data.copy()
                        new_grid[r_idx, c_idx] = num_k 
                        
                        # Normalize
                        if np.sum(new_grid) > 0:
                            st.session_state.search_grid = new_grid / np.sum(new_grid)
                        
                        if (c_idx, r_idx) not in st.session_state.search_history:
                            st.session_state.search_history.append((c_idx, r_idx))
                    
                    st.rerun()
                    
                except Exception as e:
                    st.error(f"Error: {e}")

    st.markdown("---")




    # --- PART 4: CONCEPT CHECK (Three Prisoners) ---
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"### {t(content_1_9['quiz']['title'])}")
    
    with st.container(border=True):
        q_data = get_question("1.9", "three_prisoners")
        
        # Handle bilingual options
        opts = q_data.get("options", [])
        if opts and isinstance(opts[0], dict) and ('de' in opts[0] or 'en' in opts[0]):
            option_labels = [t(o) for o in opts]
        else:
            option_labels = opts
        
        render_mcq(
            key_suffix="1_9_mcq",
            question_text=t(q_data["question"]),
            options=option_labels,
            correct_idx=q_data["correct_idx"],
            solution_text_dict=q_data["solution"],
            success_msg_dict={"de": "Exakt.", "en": "Exactly."},
            error_msg_dict={"de": "Überlege: Hat der Wärter eine Wahl?", "en": "Think: Did the warden have a choice?"},
            client=model,
            ai_context="Bayes Theorem / Three Prisoners Problem",
            course_id="vwl", topic_id="1", subtopic_id="1.9", question_id="1_9_prisoners"
        )
    
    # --- FRAG DICH (Ask Yourself) ---
    st.markdown("<br><br>", unsafe_allow_html=True)
    from utils.ask_yourself import render_ask_yourself
    render_ask_yourself(
        header=content_1_9["frag_dich"]["header"],
        questions=content_1_9["frag_dich"]["questions"],
        conclusion=content_1_9["frag_dich"]["conclusion"]
    )
    
    # --- EXAM ESSENTIALS ---
    st.markdown("<br><br>", unsafe_allow_html=True)
    from utils.exam_essentials import render_exam_essentials
    render_exam_essentials(
        trap=content_1_9["exam_essentials"]["trap"],
        trap_rule=content_1_9["exam_essentials"]["trap_rule"],
        tips=content_1_9["exam_essentials"]["tips"]
    )
    
    # --- EXAM WORKBENCH ---
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown(f"### {t({'de': 'Prüfungstraining', 'en': 'Exam Practice'})}")
    
    with st.container(border=True):
        q_data = get_question("1.9", "hs2024_mc6")
        if q_data:
            # Handle bilingual options if needed
            opts = q_data.get("options", [])
            if opts and isinstance(opts[0], dict):
                 option_labels = [t(o) for o in opts]
            else:
                 option_labels = opts
            
            render_mcq(
                key_suffix="1_9_hs2024_mc6",
                question_text=t(q_data["question"]),
                options=option_labels,
                correct_idx=q_data["correct_idx"],
                solution_text_dict=q_data["solution"],
                success_msg_dict={"de": "Richtig!", "en": "Correct!"},
                error_msg_dict={"de": "Falsch.", "en": "Incorrect."},
                client=model,
                ai_context="Conditional Probability / Total Probability",
                hint_text_dict=q_data.get("hint"),
                course_id="vwl", topic_id="1", subtopic_id="1.9", question_id="1_9_hs2024_mc6"
            )
