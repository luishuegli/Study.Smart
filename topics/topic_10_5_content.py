# Topic 10.5: Summary — Hypothesis Testing Complete
# THE FINAL MASTERPIECE: "You've Become a Statistician"
#
# This is the LAST topic in the entire course. The student leaves thinking:
# "Wow, I've never taken a course so intuitive yet so fun, yet so specific."
import streamlit as st
from utils.localization import t
from utils.quiz_helper import render_mcq
from utils.ask_yourself import render_ask_yourself
from utils.exam_essentials import render_exam_essentials
from views.styles import inject_equal_height_css

# ==============================================================================
# CONTENT DICTIONARY - BILINGUAL
# ==============================================================================

content_10_5 = {
    "title": {"de": "10.5 Zusammenfassung", "en": "10.5 Summary"},
    "subtitle": {"de": "Hypothesentests im Überblick — Du hast es geschafft!", 
                 "en": "Hypothesis Testing Overview — You Made It!"},
    
    # --- THE BIG PICTURE CELEBRATION ---
    "celebration": {
        "de": """<strong>Von Würfeln zu Entscheidungen, die zählen</strong><br><br>
Du hast mit Wahrscheinlichkeiten angefangen — Münzwürfe, Kartenziehen, einfache Experimente.<br><br>
Dann kamen die Verteilungen — Binomial, Poisson, Normal — die Muster hinter dem Zufall.<br><br>
Mit den Schätzern hast du gelernt, aus Stichproben die Wahrheit zu erschliessen.<br><br>
Und jetzt? Jetzt kannst du <strong>Behauptungen testen</strong>. Wie ein Richter, ein Türsteher, ein Talentjuror — 
du weisst, wann die Beweise stark genug sind, um eine Entscheidung zu treffen.<br><br>
<em>Das ist Statistik. Willkommen im Club.</em>""",
        "en": """<strong>From dice rolls to decisions that matter</strong><br><br>
You started with probabilities — coin flips, card draws, simple experiments.<br><br>
Then came distributions — Binomial, Poisson, Normal — the patterns behind randomness.<br><br>
With estimators, you learned to infer truth from samples.<br><br>
And now? Now you can <strong>test claims</strong>. Like a judge, a bouncer, a talent show judge — 
you know when the evidence is strong enough to make a decision.<br><br>
<em>This is statistics. Welcome to the club.</em>"""
    },
    
    # --- THE 4 JOURNEY CARDS ---
    "journey_cards": [
        {
            "topic": "10.1",
            "title": {"de": "H₀ vs H₁", "en": "H₀ vs H₁"},
            "analogy": {"de": "Der Gerichtssaal", "en": "The Courtroom"},
            "key": {"de": "H₀ = unschuldig bis...", "en": "H₀ = innocent until..."}
        },
        {
            "topic": "10.2",
            "title": {"de": "T vs c", "en": "T vs c"},
            "analogy": {"de": "Der Türsteher", "en": "The Bouncer"},
            "key": {"de": "T aus Daten, c aus Tabelle", "en": "T from data, c from table"}
        },
        {
            "topic": "10.3",
            "title": {"de": "α vs β", "en": "α vs β"},
            "analogy": {"de": "Der Rauchmelder", "en": "The Smoke Detector"},
            "key": {"de": "Fehlalarm vs Brand verschlafen", "en": "False alarm vs Missed fire"}
        },
        {
            "topic": "10.4",
            "title": {"de": "p vs α", "en": "p vs α"},
            "analogy": {"de": "Der Beweis-Meter", "en": "The Evidence Meter"},
            "key": {"de": "p < α → Ablehnen!", "en": "p < α → Reject!"}
        }
    ],
    
    # --- MCQ 1: Analogy Matching ---
    "mcq_analogy": {
        "question": {
            "de": "«Ein Stichprobenergebnis ist wie ein Ausweis, und der kritische Wert ist die Altersgrenze.» — Welches Konzept beschreibt diese Analogie?",
            "en": "«A sample result is like an ID, and the critical value is the age limit.» — Which concept does this analogy describe?"
        },
        "options": [
            {"id": "a", "de": "Der p-Wert", "en": "The p-value"},
            {"id": "b", "de": "Typ-I vs Typ-II Fehler", "en": "Type I vs Type II Error"},
            {"id": "c", "de": "Kritischer Bereich und Teststatistik", "en": "Critical Region and Test Statistic"},
            {"id": "d", "de": "Nullhypothese vs Alternativhypothese", "en": "Null vs Alternative Hypothesis"}
        ],
        "correct_id": "c",
        "solution": {
            "de": "<strong>Richtig: (c) Kritischer Bereich und Teststatistik</strong><br><br>Die Türsteher-Analogie aus 10.2! Der «Ausweis» ist deine Teststatistik T (berechnet aus Daten), die «Altersgrenze» ist der kritische Wert c (aus der Tabelle).",
            "en": "<strong>Correct: (c) Critical Region and Test Statistic</strong><br><br>The bouncer analogy from 10.2! The «ID» is your test statistic T (calculated from data), the «age limit» is the critical value c (from the table)."
        }
    },
    
    # --- THE 5-STEP RECIPE ---
    "recipe": {
        "header": {"de": "Das Rezept: Jeder Z-Test in 5 Schritten", "en": "The Recipe: Every Z-Test in 5 Steps"},
        "steps": [
            {
                "number": "1",
                "title": {"de": "Hypothesen aufstellen", "en": "State Hypotheses"},
                "content": {"de": "$H_0$: $\\mu = \\mu_0$ (Status Quo)<br>$H_1$: $\\mu \\neq \\mu_0$ oder $\\mu > \\mu_0$ oder $\\mu < \\mu_0$", 
                           "en": "$H_0$: $\\mu = \\mu_0$ (Status Quo)<br>$H_1$: $\\mu \\neq \\mu_0$ or $\\mu > \\mu_0$ or $\\mu < \\mu_0$"},
                "tip": {"de": "$H_0$ enthält IMMER $=$", "en": "$H_0$ ALWAYS contains $=$"}
            },
            {
                "number": "2",
                "title": {"de": "Signifikanzniveau wählen", "en": "Choose Significance Level"},
                "content": {"de": "$\\alpha = 5\\%$ (typisch), $1\\%$, oder $10\\%$", "en": "$\\alpha = 5\\%$ (typical), $1\\%$, or $10\\%$"},
                "tip": {"de": "Kleineres $\\alpha$ = strengerer Test", "en": "Smaller $\\alpha$ = stricter test"}
            },
            {
                "number": "3",
                "title": {"de": "Teststatistik berechnen", "en": "Calculate Test Statistic"},
                "formula": r"T = \frac{\bar{X} - \mu_0}{\sigma / \sqrt{n}}",
                "tip": {"de": "T kommt aus DEINEN DATEN", "en": "T comes from YOUR DATA"}
            },
            {
                "number": "4",
                "title": {"de": "Kritischen Wert oder p-Wert finden", "en": "Find Critical Value or p-Value"},
                "content": {"de": "Zweiseitig: $c = z_{1-\\alpha/2}$<br>Einseitig: $c = z_{1-\\alpha}$", 
                           "en": "Two-sided: $c = z_{1-\\alpha/2}$<br>One-sided: $c = z_{1-\\alpha}$"},
                "tip": {"de": "$c$ kommt aus der TABELLE", "en": "$c$ comes from the TABLE"}
            },
            {
                "number": "5",
                "title": {"de": "Entscheiden", "en": "Decide"},
                "content": {"de": "$|T| > c$ → $H_0$ ablehnen<br>$p < \\alpha$ → $H_0$ ablehnen", 
                           "en": "$|T| > c$ → Reject $H_0$<br>$p < \\alpha$ → Reject $H_0$"},
                "tip": {"de": "Beide Methoden = gleiches Ergebnis!", "en": "Both methods = same result!"}
            }
        ]
    },
    
    # --- MCQ 2: Step Order ---
    "mcq_steps": {
        "question": {
            "de": "In welcher Reihenfolge führst du einen Hypothesentest durch?",
            "en": "In what order do you perform a hypothesis test?"
        },
        "options": [
            {"id": "a", "de": "T berechnen → α wählen → Hypothesen → Entscheiden", 
             "en": "Calculate T → Choose α → Hypotheses → Decide"},
            {"id": "b", "de": "Hypothesen → α wählen → T berechnen → c/p finden → Entscheiden", 
             "en": "Hypotheses → Choose α → Calculate T → Find c/p → Decide"},
            {"id": "c", "de": "α wählen → Entscheiden → T berechnen → Hypothesen", 
             "en": "Choose α → Decide → Calculate T → Hypotheses"},
            {"id": "d", "de": "p-Wert finden → Hypothesen → α = 5% immer", 
             "en": "Find p-value → Hypotheses → α = 5% always"}
        ],
        "correct_id": "b",
        "solution": {
            "de": "<strong>Richtig: (b)</strong><br><br>Die korrekte Reihenfolge:<br>1. Hypothesen aufstellen (H₀, H₁)<br>2. α wählen (BEVOR du Daten anschaust!)<br>3. Teststatistik T berechnen<br>4. Kritischen Wert c oder p-Wert finden<br>5. Entscheiden",
            "en": "<strong>Correct: (b)</strong><br><br>The correct order:<br>1. State hypotheses (H₀, H₁)<br>2. Choose α (BEFORE looking at data!)<br>3. Calculate test statistic T<br>4. Find critical value c or p-value<br>5. Decide"
        }
    },
    
    # --- THE ERROR MATRIX ---
    "error_matrix": {
        "header": {"de": "Die Entscheidungsmatrix", "en": "The Decision Matrix"},
        "reality_true": {"de": "Realität: H₀ ist WAHR", "en": "Reality: H₀ is TRUE"},
        "reality_false": {"de": "Realität: H₀ ist FALSCH", "en": "Reality: H₀ is FALSE"},
        "decision_reject": {"de": "Entscheidung: H₀ ablehnen", "en": "Decision: Reject H₀"},
        "decision_keep": {"de": "Entscheidung: H₀ nicht ablehnen", "en": "Decision: Don't reject H₀"},
        "type1": {"de": "Typ-I-Fehler (α)", "en": "Type I Error (α)"},
        "type1_desc": {"de": "Fehlalarm!", "en": "False alarm!"},
        "type2": {"de": "Typ-II-Fehler (β)", "en": "Type II Error (β)"},
        "type2_desc": {"de": "Brand verschlafen!", "en": "Missed fire!"},
        "correct1": {"de": "Korrekt!", "en": "Correct!"},
        "correct2": {"de": "Korrekt!", "en": "Correct!"},
        "power": {"de": "Power = 1 - β", "en": "Power = 1 - β"}
    },
    
    # --- KEY FORMULAS ---
    "key_formulas": {
        "header": {"de": "Formel-Cheatsheet", "en": "Formula Cheatsheet"},
        "formulas": [
            {
                "name": {"de": "Z-Statistik", "en": "Z-Statistic"},
                "formula": r"Z = \frac{\bar{X} - \mu_0}{\sigma / \sqrt{n}}"
            },
            {
                "name": {"de": "p-Wert Entscheidung", "en": "p-Value Decision"},
                "formula": r"p < \alpha \Rightarrow \text{Reject } H_0"
            },
            {
                "name": {"de": "Power (Güte)", "en": "Power"},
                "formula": r"\text{Power} = 1 - \beta"
            },
            {
                "name": {"de": "Kritischer Wert (zweiseitig)", "en": "Critical Value (two-sided)"},
                "formula": r"c = z_{1-\alpha/2}"
            }
        ]
    },
    
    # --- MCQ 3: Formula Recognition ---
    "mcq_formula": {
        "question": {
            "de": "Die Power eines Tests beträgt 0.85. Was ist β?",
            "en": "The power of a test is 0.85. What is β?"
        },
        "options": [
            {"id": "a", "de": "0.85", "en": "0.85"},
            {"id": "b", "de": "0.15", "en": "0.15"},
            {"id": "c", "de": "0.05", "en": "0.05"},
            {"id": "d", "de": "Kann nicht berechnet werden", "en": "Cannot be calculated"}
        ],
        "correct_id": "b",
        "solution": {
            "de": "<strong>Richtig: (b) 0.15</strong><br><br>Power = 1 - β<br>0.85 = 1 - β<br>β = 1 - 0.85 = 0.15<br><br>β ist die Wahrscheinlichkeit eines Typ-II-Fehlers (echten Effekt verpassen).",
            "en": "<strong>Correct: (b) 0.15</strong><br><br>Power = 1 - β<br>0.85 = 1 - β<br>β = 1 - 0.85 = 0.15<br><br>β is the probability of a Type II Error (missing a real effect)."
        }
    },
    
    # --- ASK YOURSELF ---
    "frag_dich": {
        "header": {
            "de": "Frag dich: Bist du prüfungsbereit?",
            "en": "Ask yourself: Are you exam-ready?"
        },
        "questions": [
            {"de": "Was ist der Unterschied zwischen T (Teststatistik) und c (kritischer Wert)?",
             "en": "What's the difference between T (test statistic) and c (critical value)?"},
            {"de": "Wann benutzt du einen einseitigen, wann einen zweiseitigen Test?",
             "en": "When do you use one-sided vs two-sided test?"},
            {"de": "Was passiert mit α und β wenn du n erhöhst?",
             "en": "What happens to α and β when you increase n?"},
            {"de": "Was bedeutet «H₀ nicht ablehnen» — ist H₀ dann bewiesen?",
             "en": "What does «don't reject H₀» mean — is H₀ then proven?"},
            {"de": "p = 0.03 bei α = 0.05 — Was ist deine Entscheidung?",
             "en": "p = 0.03 with α = 0.05 — What's your decision?"}
        ],
        "conclusion": {
            "de": "Wenn du alle 5 Fragen beantworten kannst, bist du bereit für jede Prüfungsaufgabe zu Hypothesentests!",
            "en": "If you can answer all 5 questions, you're ready for any exam question on hypothesis testing!"
        }
    },
    
    # --- EXAM ESSENTIALS ---
    "exam_essentials": {
        "trap": {
            "de": "«p = 0.03 bedeutet, dass H₀ mit 3% Wahrscheinlichkeit wahr ist»",
            "en": "«p = 0.03 means H₀ is 3% likely to be true»"
        },
        "trap_rule": {
            "de": "FALSCH! Der p-Wert ist die Wahrscheinlichkeit, solche DATEN zu sehen, WENN H₀ wahr wäre — nicht umgekehrt!",
            "en": "WRONG! The p-value is the probability of seeing such DATA IF H₀ were true — not the other way around!"
        },
        "tips": [
            {
                "tip": {"de": "«H₀ nicht ablehnen» ≠ «H₀ ist wahr»", 
                        "en": "«Don't reject H₀» ≠ «H₀ is true»"},
                "why": {"de": "Es heisst nur: zu wenig Beweis gegen H₀. Vielleicht ist n zu klein!", 
                        "en": "It only means: insufficient evidence against H₀. Maybe n is too small!"}
            },
            {
                "tip": {"de": "Bei zweiseitigen Tests: α aufteilen! Jeder Rand bekommt $\\alpha/2$", 
                        "en": "For two-sided tests: split α! Each tail gets $\\alpha/2$"},
                "why": {"de": "Bei α = 5% zweiseitig: je 2.5% links und rechts.", 
                        "en": "At α = 5% two-sided: 2.5% left and right each."}
            },
            {
                "tip": {"de": "T kommt aus den DATEN, c kommt aus der TABELLE", 
                        "en": "T comes from DATA, c comes from TABLE"},
                "why": {"de": "Die häufigste Verwechslung in Prüfungen!", 
                        "en": "The most common confusion in exams!"}
            },
            {
                "tip": {"de": "Power ≥ 80% ist das Ziel — sonst ist dein Test zu schwach", 
                        "en": "Power ≥ 80% is the goal — otherwise your test is too weak"},
                "why": {"de": "Niedrige Power = viele echte Effekte werden verpasst.", 
                        "en": "Low power = many real effects are missed."}
            },
            {
                "tip": {"de": "Grösseres n verbessert BEIDES: α bleibt konstant, β sinkt", 
                        "en": "Larger n improves BOTH: α stays constant, β decreases"},
                "why": {"de": "Der einzige Weg, den α-β Trade-off zu umgehen!", 
                        "en": "The only way to escape the α-β trade-off!"}
            }
        ]
    },
    
    # --- FINAL BOSS MCQ ---
    "mcq_final": {
        "question": {
            "de": """Ein Qualitätsingenieur testet, ob die durchschnittliche Füllmenge μ = 500ml ist. 
Er verwendet α = 5% (zweiseitig), berechnet T = 2.1, und findet c = 1.96.
Welche Aussage ist KORREKT?""",
            "en": """A quality engineer tests if the average fill amount μ = 500ml.
He uses α = 5% (two-sided), calculates T = 2.1, and finds c = 1.96.
Which statement is CORRECT?"""
        },
        "options": [
            {"id": "a", 
             "de": "H₀ nicht ablehnen, da T < 2.0", 
             "en": "Don't reject H₀, since T < 2.0"},
            {"id": "b", 
             "de": "H₀ ablehnen, da |T| = 2.1 > 1.96 = c", 
             "en": "Reject H₀, since |T| = 2.1 > 1.96 = c"},
            {"id": "c", 
             "de": "H₀ ablehnen, da T positiv ist", 
             "en": "Reject H₀, since T is positive"},
            {"id": "d", 
             "de": "Mehr Informationen nötig (Stichprobengrösse n)", 
             "en": "More information needed (sample size n)"}
        ],
        "correct_id": "b",
        "solution": {
            "de": """<strong>Richtig: (b) H₀ ablehnen, da |T| = 2.1 > 1.96 = c</strong><br><br>
<strong>Die Logik:</strong><br>
• Zweiseitiger Test → Wir vergleichen |T| mit c<br>
• |T| = |2.1| = 2.1<br>
• c = 1.96 (kritischer Wert bei α/2 = 2.5% pro Seite)<br>
• 2.1 > 1.96 → T fällt in den Ablehnbereich<br><br>
<strong>Konklusion:</strong> Es gibt genügend Beweis, um H₀ abzulehnen. Die Füllmenge unterscheidet sich signifikant von 500ml.""",
            "en": """<strong>Correct: (b) Reject H₀, since |T| = 2.1 > 1.96 = c</strong><br><br>
<strong>The logic:</strong><br>
• Two-sided test → We compare |T| with c<br>
• |T| = |2.1| = 2.1<br>
• c = 1.96 (critical value at α/2 = 2.5% per tail)<br>
• 2.1 > 1.96 → T falls in the rejection region<br><br>
<strong>Conclusion:</strong> There's sufficient evidence to reject H₀. The fill amount significantly differs from 500ml."""
        }
    }
}


# ==============================================================================
# RENDER FUNCTIONS
# ==============================================================================

def render_journey_cards():
    """Render the 4 journey cards showing progress through Topic 10."""
    cards = content_10_5["journey_cards"]
    cols = st.columns(4, gap="small")
    
    for col, card in zip(cols, cards):
        with col:
            st.markdown(f"""
<div style="background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%); 
            border: 2px solid #e2e8f0; border-radius: 12px; padding: 14px; 
            text-align: center; height: 100%;">
    <div style="font-size: 0.75em; color: #94a3b8; margin-bottom: 4px;">{card['topic']}</div>
    <div style="font-weight: 700; font-size: 1.1em; color: #1e293b;">{t(card['title'])}</div>
    <div style="color: #64748b; font-size: 0.85em; margin: 6px 0; font-style: italic;">«{t(card['analogy'])}»</div>
    <div style="color: #475569; font-size: 0.8em; margin-top: 8px;">{t(card['key'])}</div>
</div>
""", unsafe_allow_html=True)


def render_recipe_steps():
    """Render the 5-step hypothesis testing recipe."""
    recipe = content_10_5["recipe"]
    
    st.markdown(f"### {t(recipe['header'])}")
    
    with st.container(border=True):
        for i, step in enumerate(recipe["steps"]):
            if i > 0:
                st.markdown("---")
            
            # Step header
            st.markdown(f"**{step['number']}. {t(step['title'])}**")
            
            # Content or formula
            if "formula" in step:
                st.latex(step["formula"])
            else:
                st.markdown(t(step["content"]), unsafe_allow_html=True)
            
            # Tip
            st.caption(t(step['tip']))


def render_error_matrix():
    """Render the 2x2 error decision matrix."""
    matrix = content_10_5["error_matrix"]
    
    st.markdown(f"### {t(matrix['header'])}")
    
    # Custom HTML for the 2x2 matrix with semantic colors
    st.markdown(f"""
<div style="display: grid; grid-template-columns: 1fr 1fr; grid-template-rows: auto 1fr 1fr; gap: 0; max-width: 100%;">
    <div style="background: #f1f5f9; padding: 12px; text-align: center; border: 1px solid #e2e8f0; font-weight: 600;">{t(matrix['reality_true'])}</div>
    <div style="background: #f1f5f9; padding: 12px; text-align: center; border: 1px solid #e2e8f0; font-weight: 600;">{t(matrix['reality_false'])}</div>
    <div style="background: #fee2e2; padding: 16px; text-align: center; border: 2px solid #fecaca;"><div style="font-weight: 700; color: #dc2626;">{t(matrix['type1'])}</div><div style="color: #b91c1c; font-size: 0.9em;">{t(matrix['type1_desc'])}</div></div>
    <div style="background: #dcfce7; padding: 16px; text-align: center; border: 2px solid #bbf7d0;"><div style="font-weight: 700; color: #16a34a;">{t(matrix['correct1'])}</div><div style="color: #15803d; font-size: 0.9em;">{t(matrix['power'])}</div></div>
    <div style="background: #dcfce7; padding: 16px; text-align: center; border: 2px solid #bbf7d0;"><div style="font-weight: 700; color: #16a34a;">{t(matrix['correct2'])}</div></div>
    <div style="background: #ffedd5; padding: 16px; text-align: center; border: 2px solid #fed7aa;"><div style="font-weight: 700; color: #ea580c;">{t(matrix['type2'])}</div><div style="color: #c2410c; font-size: 0.9em;">{t(matrix['type2_desc'])}</div></div>
</div>
<div style="display: flex; margin-top: 8px; gap: 8px;">
    <div style="flex: 1; text-align: center; color: #64748b; font-size: 0.85em;">{t(matrix['decision_reject'])}</div>
    <div style="flex: 1; text-align: center; color: #64748b; font-size: 0.85em;">{t(matrix['decision_keep'])}</div>
</div>
""", unsafe_allow_html=True)


def render_formula_cheatsheet():
    """Render the key formulas in a 2x2 grid."""
    formulas = content_10_5["key_formulas"]
    
    st.markdown(f"### {t(formulas['header'])}")
    
    # 2x2 grid
    row1 = st.columns(2, gap="medium")
    row2 = st.columns(2, gap="medium")
    
    for i, (col, formula) in enumerate(zip(row1 + row2, formulas["formulas"])):
        with col:
            with st.container(border=True):
                st.markdown(f"**{t(formula['name'])}**")
                st.latex(formula["formula"])


def render_mcq_block(mcq_key, key_suffix, model):
    """Render an MCQ from the content dictionary."""
    mcq = content_10_5[mcq_key]
    opts = mcq["options"]
    opt_labels = [t({"de": o["de"], "en": o["en"]}) for o in opts]
    correct_idx = next((i for i, o in enumerate(opts) if o["id"] == mcq["correct_id"]), 0)
    
    with st.container(border=True):
        st.markdown(f"**{t({'de': 'Schnell-Check', 'en': 'Quick Check'})}**")
        render_mcq(
            key_suffix=key_suffix,
            question_text=t(mcq["question"]),
            options=opt_labels,
            correct_idx=correct_idx,
            solution_text_dict=mcq["solution"],
            success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
            error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
            client=model,
            ai_context=f"Topic 10.5 Summary: {key_suffix}",
            course_id="vwl",
            topic_id="10",
            subtopic_id="10.5",
            question_id=key_suffix
        )


# ==============================================================================
# MAIN RENDER FUNCTION
# ==============================================================================

def render_subtopic_10_5(model):
    """10.5 Zusammenfassung — The Final Masterpiece"""
    
    # Inject equal height CSS
    inject_equal_height_css()
    
    # Header
    st.header(t(content_10_5["title"]))
    st.caption(t(content_10_5["subtitle"]))
    st.markdown("---")
    
    # ==========================================================================
    # 1. THE CELEBRATION (Big Picture)
    # ==========================================================================
    st.markdown(f"### {t({'de': 'Die Reise', 'en': 'The Journey'})}")
    
    with st.container(border=True):
        st.markdown(t(content_10_5["celebration"]), unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # ==========================================================================
    # 2. THE 4 JOURNEY CARDS
    # ==========================================================================
    render_journey_cards()
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # MCQ 1: Analogy Matching
    render_mcq_block("mcq_analogy", "10_5_analogy", model)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # ==========================================================================
    # 3. THE 5-STEP RECIPE
    # ==========================================================================
    render_recipe_steps()
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # MCQ 2: Step Order
    render_mcq_block("mcq_steps", "10_5_steps", model)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # ==========================================================================
    # 4. THE ERROR MATRIX
    # ==========================================================================
    render_error_matrix()
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # ==========================================================================
    # 5. KEY FORMULAS CHEATSHEET
    # ==========================================================================
    render_formula_cheatsheet()
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # MCQ 3: Formula Recognition
    render_mcq_block("mcq_formula", "10_5_formula", model)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # ==========================================================================
    # 6. ASK YOURSELF
    # ==========================================================================
    render_ask_yourself(
        header=content_10_5["frag_dich"]["header"],
        questions=content_10_5["frag_dich"]["questions"],
        conclusion=content_10_5["frag_dich"]["conclusion"]
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # ==========================================================================
    # 7. EXAM ESSENTIALS
    # ==========================================================================
    render_exam_essentials(
        trap=content_10_5["exam_essentials"]["trap"],
        trap_rule=content_10_5["exam_essentials"]["trap_rule"],
        tips=content_10_5["exam_essentials"]["tips"]
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # ==========================================================================
    # 8. THE FINAL BOSS MCQ
    # ==========================================================================
    st.markdown(f"### {t({'de': 'Die ultimative Prüfungsaufgabe', 'en': 'The Ultimate Exam Question'})}")
    
    mcq = content_10_5["mcq_final"]
    opts = mcq["options"]
    opt_labels = [t({"de": o["de"], "en": o["en"]}) for o in opts]
    correct_idx = next((i for i, o in enumerate(opts) if o["id"] == mcq["correct_id"]), 0)
    
    with st.container(border=True):
        render_mcq(
            key_suffix="10_5_final",
            question_text=t(mcq["question"]),
            options=opt_labels,
            correct_idx=correct_idx,
            solution_text_dict=mcq["solution"],
            success_msg_dict={"de": "Perfekt! Du bist bereit!", "en": "Perfect! You're ready!"},
            error_msg_dict={"de": "Fast! Lies die Lösung.", "en": "Almost! Read the solution."},
            client=model,
            ai_context="Topic 10.5 Final Boss: Comprehensive hypothesis testing workflow question",
            course_id="vwl",
            topic_id="10",
            subtopic_id="10.5",
            question_id="10_5_final_boss"
        )
