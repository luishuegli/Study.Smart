# Topic 10.1: Types of Hypotheses (Arten von Hypothesen)
# ULTRATHINK Feynman-style implementation: "Courtroom Analogy"
import streamlit as st
from utils.localization import t
from utils.quiz_helper import render_mcq
from utils.ask_yourself import render_ask_yourself
from utils.exam_essentials import render_exam_essentials
from utils.layouts import render_comparison, render_decision_tree
from utils.layouts.foundation import inject_equal_height_css

# ==============================================================================
# CONTENT DICTIONARY
# ==============================================================================

content_10_1 = {
    "title": {"de": "10.1 Arten von Hypothesen", "en": "10.1 Types of Hypotheses"},
    
    # --- COURTROOM ANALOGY (Intuition) ---
    "intuition": {
        "de": """<strong>Stell dir einen Gerichtssaal vor:</strong><br><br>
• Der Angeklagte gilt als <strong>UNSCHULDIG</strong>, bis das Gegenteil bewiesen ist.<br>
→ Das ist H₀ — der Status Quo (was wir annehmen, bis Beweise dagegen sprechen)<br><br>
• Der Staatsanwalt behauptet, der Angeklagte sei <strong>SCHULDIG</strong>.<br>
→ Das ist H₁ — die Alternative (was wir beweisen wollen)<br><br>
• Wir brauchen <strong>STARKE BEWEISE</strong>, um zu verurteilen (H₀ abzulehnen).<br>
→ Bei schwachen Beweisen sprechen wir frei!<br><br>
<em>Genau so funktioniert ein Hypothesentest.</em>""",
        "en": """<strong>Imagine a courtroom:</strong><br><br>
• The defendant is <strong>INNOCENT</strong> until proven guilty.<br>
→ This is H₀ — the status quo (what we assume until evidence says otherwise)<br><br>
• The prosecutor claims the defendant is <strong>GUILTY</strong>.<br>
→ This is H₁ — the alternative (what we're trying to prove)<br><br>
• We need <strong>STRONG EVIDENCE</strong> to convict (reject H₀).<br>
→ With weak evidence, we must acquit!<br><br>
<em>This is exactly how hypothesis testing works.</em>"""
    },
    
    # --- H₀ vs H₁ COMPARISON ---
    "h0_card": {
        "title": {"de": "H₀ — Nullhypothese", "en": "H₀ — Null Hypothesis"},
        "content": {"de": "Der «Status Quo»", "en": "The «Status Quo»"},
        "details": {
            "de": "• Enthält immer das Gleichheitszeichen (=, ≤, ≥)<br>• Wird beibehalten, ausser Beweise sprechen dagegen<br>• θ ∈ Θ₀",
            "en": "• Always contains the equality (=, ≤, ≥)<br>• Kept unless evidence says otherwise<br>• θ ∈ Θ₀"
        }
    },
    "h1_card": {
        "title": {"de": "H₁ — Alternativhypothese", "en": "H₁ — Alternative Hypothesis"},
        "content": {"de": "Die «Herausforderung»", "en": "The «Challenge»"},
        "details": {
            "de": "• Behauptet etwas Neues oder Anderes<br>• Muss mit starken Beweisen gestützt werden<br>• θ ∈ Θ₁",
            "en": "• Claims something new or different<br>• Must be supported by strong evidence<br>• θ ∈ Θ₁"
        }
    },
    
    # --- SIMPLE vs COMPOSITE ---
    "simple_composite": {
        "simple": {
            "title": {"de": "Einfache Hypothese", "en": "Simple Hypothesis"},
            "formula": r"H_0: \mu = 100",
            "meaning": {"de": "GENAU EIN Wert", "en": "EXACTLY ONE value"},
            "example": {"de": "«Der Mittelwert ist exakt 100»", "en": "«The mean is exactly 100»"}
        },
        "composite": {
            "title": {"de": "Zusammengesetzte Hypothese", "en": "Composite Hypothesis"},
            "formula": r"H_1: \mu \neq 100",
            "meaning": {"de": "MEHRERE Werte möglich", "en": "MULTIPLE values possible"},
            "example": {"de": "«Der Mittelwert ist nicht 100»", "en": "«The mean is not 100»"}
        }
    },
    
    # --- ONE-SIDED vs TWO-SIDED ---
    "sided_hypothesis": {
        "one_sided_right": {
            "title": {"de": "Einseitig (rechts)", "en": "One-sided (right)"},
            "formula": r"H_1: \mu > \mu_0",
            "meaning": {"de": "«grösser als»", "en": "«greater than»"},
            "signal": {"de": "besser, mehr, höher, steigt", "en": "better, more, higher, increases"}
        },
        "one_sided_left": {
            "title": {"de": "Einseitig (links)", "en": "One-sided (left)"},
            "formula": r"H_1: \mu < \mu_0",
            "meaning": {"de": "«kleiner als»", "en": "«less than»"},
            "signal": {"de": "schlechter, weniger, niedriger, sinkt", "en": "worse, less, lower, decreases"}
        },
        "two_sided": {
            "title": {"de": "Zweiseitig", "en": "Two-sided"},
            "formula": r"H_1: \mu \neq \mu_0",
            "meaning": {"de": "«anders als»", "en": "«different from»"},
            "signal": {"de": "unterscheidet sich, ändert sich, ist anders", "en": "differs, changes, is different"}
        }
    },
    
    # --- INTERACTIVE SCENARIOS ---
    "scenarios": [
        {
            "id": "drug",
            "scenario": {
                "de": "Ein Pharmaunternehmen behauptet, ihr neues Medikament senkt den Cholesterinspiegel MEHR als das alte.",
                "en": "A pharmaceutical company claims their new drug lowers cholesterol MORE than the old one."
            },
            "h0": r"H_0: \mu_{\text{new}} = \mu_{\text{old}}",
            "h1": r"H_1: \mu_{\text{new}} > \mu_{\text{old}}",
            "answer_simple_composite": "composite",
            "answer_sided": "one_right",
            "explanation": {
                "de": "«mehr» = Richtung → einseitig rechts. H₁ enthält einen Bereich → zusammengesetzt.",
                "en": "«more» = direction → one-sided right. H₁ contains a range → composite."
            }
        },
        {
            "id": "factory",
            "scenario": {
                "de": "Eine Fabrik testet, ob die durchschnittliche Lebensdauer ihrer Glühbirnen GENAU 1000 Stunden beträgt.",
                "en": "A factory tests whether the average lifespan of their light bulbs is EXACTLY 1000 hours."
            },
            "h0": r"H_0: \mu = 1000",
            "h1": r"H_1: \mu \neq 1000",
            "answer_simple_composite": "simple",
            "answer_sided": "two",
            "explanation": {
                "de": "H₀ ist ein exakter Wert → einfach. «nicht genau» = beide Richtungen → zweiseitig.",
                "en": "H₀ is an exact value → simple. «not exactly» = both directions → two-sided."
            }
        },
        {
            "id": "diet",
            "scenario": {
                "de": "Eine Diät-Studie untersucht, ob Teilnehmer Gewicht VERLIEREN (weniger wiegen als vorher).",
                "en": "A diet study examines whether participants LOSE weight (weigh less than before)."
            },
            "h0": r"H_0: \mu_{\text{after}} = \mu_{\text{before}}",
            "h1": r"H_1: \mu_{\text{after}} < \mu_{\text{before}}",
            "answer_simple_composite": "composite",
            "answer_sided": "one_left",
            "explanation": {
                "de": "«verlieren» = weniger = Richtung nach unten → einseitig links.",
                "en": "«lose» = less = downward direction → one-sided left."
            }
        },
        {
            "id": "salary",
            "scenario": {
                "de": "Ein Unternehmen prüft, ob das DURCHSCHNITTSGEHALT sich vom Branchendurchschnitt UNTERSCHEIDET.",
                "en": "A company checks if the AVERAGE SALARY DIFFERS from the industry average."
            },
            "h0": r"H_0: \mu = \mu_{\text{industry}}",
            "h1": r"H_1: \mu \neq \mu_{\text{industry}}",
            "answer_simple_composite": "simple",
            "answer_sided": "two",
            "explanation": {
                "de": "«unterscheidet sich» ohne Richtung → zweiseitig. H₀ ist exakt → einfach.",
                "en": "«differs» without direction → two-sided. H₀ is exact → simple."
            }
        }
    ],
    
    # --- ASK YOURSELF ---
    "frag_dich": {
        "header": {
            "de": "Frag dich: Kannst du Hypothesen klassifizieren?",
            "en": "Ask yourself: Can you classify hypotheses?"
        },
        "questions": [
            {"de": "«Der Mittelwert ist exakt 170cm» — Einfach oder Zusammengesetzt?", 
             "en": "«The mean is exactly 170cm» — Simple or Composite?"},
            {"de": "«Das neue Medikament wirkt besser» — Einseitig oder Zweiseitig?", 
             "en": "«The new drug works better» — One-sided or Two-sided?"},
            {"de": "«Es gibt einen Unterschied in den Testergebnissen» — Einseitig oder Zweiseitig?", 
             "en": "«There's a difference in test scores» — One-sided or Two-sided?"},
            {"de": "H₀ ist immer das, was wir BEWEISEN wollen — Richtig oder Falsch?", 
             "en": "H₀ is always what we want to PROVE — True or False?"}
        ],
        "conclusion": {
            "de": "Goldene Regel: H₀ = Status Quo, H₁ = Was du beweisen willst",
            "en": "Golden Rule: H₀ = Status Quo, H₁ = What you want to prove"
        }
    },
    
    # --- EXAM ESSENTIALS ---
    "exam_essentials": {
        "trap": {
            "de": "H₁: μ > μ₀ (einseitig) mit H₁: μ ≠ μ₀ (zweiseitig) verwechseln",
            "en": "Confusing H₁: μ > μ₀ (one-sided) with H₁: μ ≠ μ₀ (two-sided)"
        },
        "trap_rule": {
            "de": "«besser/höher/mehr» → EINSEITIG | «unterscheidet sich» → ZWEISEITIG",
            "en": "«better/higher/more» → ONE-SIDED | «differs» → TWO-SIDED"
        },
        "tips": [
            {
                "tip": {"de": "H₀ enthält IMMER das Gleichheitszeichen", "en": "H₀ ALWAYS contains the equality sign"},
                "why": {"de": "Wir brauchen einen exakten Wert, um Wahrscheinlichkeiten zu berechnen.", "en": "We need an exact value to compute probabilities."}
            },
            {
                "tip": {"de": "Lies die Aufgabe genau: Welche Richtung wird behauptet?", "en": "Read carefully: What direction is claimed?"},
                "why": {"de": "Signalwörter wie «grösser», «kleiner», «anders» bestimmen den Test-Typ.", "en": "Signal words like «greater», «less», «different» determine the test type."}
            },
            {
                "tip": {"de": "H₁ ist das, was der Forscher BEWEISEN will", "en": "H₁ is what the researcher wants to PROVE"},
                "why": {"de": "Die «Beweislast» liegt bei H₁, nicht bei H₀.", "en": "The «burden of proof» is on H₁, not H₀."}
            }
        ]
    },
    
    # --- MCQ ---
    "mcq": {
        "question": {
            "de": "Welche der folgenden Aussagen zu Hypothesen ist KORREKT?",
            "en": "Which of the following statements about hypotheses is CORRECT?"
        },
        "options": [
            {"id": "a", "de": "H₀ ist immer einseitig", "en": "H₀ is always one-sided"},
            {"id": "b", "de": "Eine einfache Hypothese enthält genau einen Wert", "en": "A simple hypothesis contains exactly one value"},
            {"id": "c", "de": "H₁: μ ≠ μ₀ ist eine einseitige Hypothese", "en": "H₁: μ ≠ μ₀ is a one-sided hypothesis"},
            {"id": "d", "de": "H₁ enthält immer das Gleichheitszeichen", "en": "H₁ always contains the equality sign"}
        ],
        "correct_id": "b",
        "solution": {
            "de": "<strong>Richtig: (b)</strong><br>Eine einfache Hypothese spezifiziert GENAU EINEN Wert (z.B. H₀: μ = 100).<br><br>(a) ist falsch: H₀ kann ein- oder zweiseitig formuliert werden.<br>(c) ist falsch: μ ≠ μ₀ ist ZWEISEITIG (beide Richtungen).<br>(d) ist falsch: Das Gleichheitszeichen ist in H₀, nicht H₁.",
            "en": "<strong>Correct: (b)</strong><br>A simple hypothesis specifies EXACTLY ONE value (e.g., H₀: μ = 100).<br><br>(a) is wrong: H₀ can be one- or two-sided.<br>(c) is wrong: μ ≠ μ₀ is TWO-SIDED (both directions).<br>(d) is wrong: The equality sign is in H₀, not H₁."
        }
    }
}

# ==============================================================================
# INTERACTIVE HYPOTHESIS CLASSIFIER
# ==============================================================================

@st.fragment
def hypothesis_classifier():
    """Interactive quiz to classify hypothesis types with visual feedback."""
    
    # State initialization
    if "hyp_current_scenario" not in st.session_state:
        st.session_state.hyp_current_scenario = 0
    if "hyp_score" not in st.session_state:
        st.session_state.hyp_score = 0
    if "hyp_answered" not in st.session_state:
        st.session_state.hyp_answered = False
    if "hyp_selection_sc" not in st.session_state:
        st.session_state.hyp_selection_sc = None
    if "hyp_selection_sided" not in st.session_state:
        st.session_state.hyp_selection_sided = None
    
    scenarios = content_10_1["scenarios"]
    current_idx = st.session_state.hyp_current_scenario
    
    # Completion state
    if current_idx >= len(scenarios):
        score = st.session_state.hyp_score
        total = len(scenarios) * 2  # 2 questions per scenario
        
        if score >= total * 0.8:
            st.success(t({"de": f"Ausgezeichnet! {score}/{total} richtig!", "en": f"Excellent! {score}/{total} correct!"}))
        elif score >= total * 0.5:
            st.warning(t({"de": f"Gut gemacht! {score}/{total} richtig.", "en": f"Well done! {score}/{total} correct."}))
        else:
            st.info(t({"de": f"{score}/{total} richtig. Lies die Theorie nochmal!", "en": f"{score}/{total} correct. Review the theory!"}))
        
        if st.button(t({"de": "Nochmal spielen", "en": "Play again"}), key="hyp_restart", use_container_width=True):
            st.session_state.hyp_current_scenario = 0
            st.session_state.hyp_score = 0
            st.session_state.hyp_answered = False
            st.session_state.hyp_selection_sc = None
            st.session_state.hyp_selection_sided = None
            st.rerun(scope="fragment")
        return
    
    scenario = scenarios[current_idx]
    
    # Progress indicator
    st.caption(t({"de": f"Szenario {current_idx + 1} von {len(scenarios)}", 
                  "en": f"Scenario {current_idx + 1} of {len(scenarios)}"}))
    
    # Scenario box with grey styling
    st.markdown(f"""
<div style="background: #f4f4f5; border-left: 4px solid #a1a1aa; 
            padding: 16px 20px; border-radius: 8px; color: #3f3f46; margin-bottom: 16px;">
<strong>{t({"de": "Szenario", "en": "Scenario"})}:</strong><br><br>
{t(scenario["scenario"])}
</div>
""", unsafe_allow_html=True)
    
    # Show the hypotheses
    col_h0, col_h1 = st.columns(2)
    with col_h0:
        st.markdown(f"**H₀:**")
        st.latex(scenario["h0"])
    with col_h1:
        st.markdown(f"**H₁:**")
        st.latex(scenario["h1"])
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    if not st.session_state.hyp_answered:
        # Question 1: Simple vs Composite
        st.markdown(f"**{t({'de': 'Frage 1: Ist H₀ eine...', 'en': 'Question 1: Is H₀ a...'})}**")
        
        sc_cols = st.columns(2)
        with sc_cols[0]:
            if st.button(t({"de": "Einfache Hypothese", "en": "Simple Hypothesis"}), 
                        key="btn_simple", use_container_width=True):
                st.session_state.hyp_selection_sc = "simple"
        with sc_cols[1]:
            if st.button(t({"de": "Zusammengesetzte", "en": "Composite"}), 
                        key="btn_composite", use_container_width=True):
                st.session_state.hyp_selection_sc = "composite"
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Question 2: One-sided vs Two-sided
        st.markdown(f"**{t({'de': 'Frage 2: Ist H₁...', 'en': 'Question 2: Is H₁...'})}**")
        
        sided_cols = st.columns(3)
        with sided_cols[0]:
            if st.button(t({"de": "Einseitig (rechts)", "en": "One-sided (right)"}), 
                        key="btn_one_right", use_container_width=True):
                st.session_state.hyp_selection_sided = "one_right"
        with sided_cols[1]:
            if st.button(t({"de": "Einseitig (links)", "en": "One-sided (left)"}), 
                        key="btn_one_left", use_container_width=True):
                st.session_state.hyp_selection_sided = "one_left"
        with sided_cols[2]:
            if st.button(t({"de": "Zweiseitig", "en": "Two-sided"}), 
                        key="btn_two", use_container_width=True):
                st.session_state.hyp_selection_sided = "two"
        
        # Check if both questions answered
        if st.session_state.hyp_selection_sc and st.session_state.hyp_selection_sided:
            st.session_state.hyp_answered = True
            
            # Calculate score
            if st.session_state.hyp_selection_sc == scenario["answer_simple_composite"]:
                st.session_state.hyp_score += 1
            if st.session_state.hyp_selection_sided == scenario["answer_sided"]:
                st.session_state.hyp_score += 1
            
            st.rerun(scope="fragment")
    
    else:
        # Show results
        user_sc = st.session_state.hyp_selection_sc
        user_sided = st.session_state.hyp_selection_sided
        correct_sc = scenario["answer_simple_composite"]
        correct_sided = scenario["answer_sided"]
        
        # Simple/Composite result
        sc_correct = user_sc == correct_sc
        sided_correct = user_sided == correct_sided
        
        result_cols = st.columns(2)
        with result_cols[0]:
            sc_label = t({"de": "Einfach", "en": "Simple"}) if correct_sc == "simple" else t({"de": "Zusammengesetzt", "en": "Composite"})
            if sc_correct:
                st.markdown(f"""<div style="background: #dcfce7; border: 2px solid #16a34a; border-radius: 8px; padding: 12px; text-align: center;">
<strong style="color: #16a34a;">H₀: {sc_label}</strong>
</div>""", unsafe_allow_html=True)
            else:
                st.markdown(f"""<div style="background: #fee2e2; border: 2px solid #dc2626; border-radius: 8px; padding: 12px; text-align: center;">
<strong style="color: #dc2626;">H₀: {sc_label}</strong>
</div>""", unsafe_allow_html=True)
        
        with result_cols[1]:
            sided_labels = {
                "one_right": t({"de": "Einseitig rechts", "en": "One-sided right"}),
                "one_left": t({"de": "Einseitig links", "en": "One-sided left"}),
                "two": t({"de": "Zweiseitig", "en": "Two-sided"})
            }
            sided_label = sided_labels[correct_sided]
            if sided_correct:
                st.markdown(f"""<div style="background: #dcfce7; border: 2px solid #16a34a; border-radius: 8px; padding: 12px; text-align: center;">
<strong style="color: #16a34a;">H₁: {sided_label}</strong>
</div>""", unsafe_allow_html=True)
            else:
                st.markdown(f"""<div style="background: #fee2e2; border: 2px solid #dc2626; border-radius: 8px; padding: 12px; text-align: center;">
<strong style="color: #dc2626;">H₁: {sided_label}</strong>
</div>""", unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Explanation
        st.markdown(f"""
<div style="background: #f4f4f5; border-left: 4px solid #a1a1aa; 
            padding: 12px 16px; border-radius: 8px; color: #3f3f46;">
<strong>{t({"de": "Erklärung", "en": "Explanation"})}:</strong><br>
{t(scenario["explanation"])}
</div>
""", unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Next scenario button
        if st.button(t({"de": "Nächstes Szenario →", "en": "Next Scenario →"}), 
                    key="btn_next", use_container_width=True, type="primary"):
            st.session_state.hyp_current_scenario += 1
            st.session_state.hyp_answered = False
            st.session_state.hyp_selection_sc = None
            st.session_state.hyp_selection_sided = None
            st.rerun(scope="fragment")


# ==============================================================================
# MAIN RENDER FUNCTION
# ==============================================================================

def render_subtopic_10_1(model):
    """10.1 Arten von Hypothesen — Types of Hypotheses"""
    
    st.header(t(content_10_1["title"]))
    st.markdown("---")
    
    # Inject equal height CSS for side-by-side containers
    inject_equal_height_css()
    
    # ==========================================================================
    # 1. THE COURTROOM ANALOGY (Intuition First)
    # ==========================================================================
    st.markdown(f"### {t({'de': 'Die Kernidee: Der Gerichtssaal', 'en': 'The Core Idea: The Courtroom'})}")
    
    with st.container(border=True):
        st.markdown(t(content_10_1["intuition"]), unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # ==========================================================================
    # 2. H₀ vs H₁ (Side-by-Side Comparison)
    # ==========================================================================
    st.markdown(f"### {t({'de': 'Die zwei Hypothesen', 'en': 'The Two Hypotheses'})}")
    
    col1, col2 = st.columns(2, gap="medium")
    
    with col1:
        with st.container(border=True):
            st.markdown(f"**{t(content_10_1['h0_card']['title'])}**")
            st.markdown(f"*{t(content_10_1['h0_card']['content'])}*")
            st.latex(r"H_0: \theta \in \Theta_0")
            st.markdown("---")
            st.markdown(t(content_10_1['h0_card']['details']), unsafe_allow_html=True)
    
    with col2:
        with st.container(border=True):
            st.markdown(f"**{t(content_10_1['h1_card']['title'])}**")
            st.markdown(f"*{t(content_10_1['h1_card']['content'])}*")
            st.latex(r"H_1: \theta \in \Theta_1")
            st.markdown("---")
            st.markdown(t(content_10_1['h1_card']['details']), unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # ==========================================================================
    # 3. SIMPLE vs COMPOSITE HYPOTHESES
    # ==========================================================================
    st.markdown(f"### {t({'de': 'Einfach vs. Zusammengesetzt', 'en': 'Simple vs. Composite'})}")
    
    simple = content_10_1["simple_composite"]["simple"]
    composite = content_10_1["simple_composite"]["composite"]
    
    col1, col2 = st.columns(2, gap="medium")
    
    with col1:
        with st.container(border=True):
            st.markdown(f"**{t(simple['title'])}**")
            st.latex(simple["formula"])
            st.markdown(f"**{t(simple['meaning'])}**")
            st.caption(t(simple["example"]))
    
    with col2:
        with st.container(border=True):
            st.markdown(f"**{t(composite['title'])}**")
            st.latex(composite["formula"])
            st.markdown(f"**{t(composite['meaning'])}**")
            st.caption(t(composite["example"]))
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # ==========================================================================
    # 4. ONE-SIDED vs TWO-SIDED (Visual Decision Helper)
    # ==========================================================================
    st.markdown(f"### {t({'de': 'Einseitig vs. Zweiseitig', 'en': 'One-Sided vs. Two-Sided'})}")
    
    sided = content_10_1["sided_hypothesis"]
    
    # Create 3 columns for the three types
    col1, col2, col3 = st.columns(3, gap="medium")
    
    with col1:
        with st.container(border=True):
            st.markdown(f"**{t(sided['one_sided_right']['title'])}**")
            st.latex(sided['one_sided_right']['formula'])
            st.markdown(f"*{t(sided['one_sided_right']['meaning'])}*")
            st.markdown("---")
            st.caption(f"{t({'de': 'Signalwörter', 'en': 'Signal words'})}: {t(sided['one_sided_right']['signal'])}")
    
    with col2:
        with st.container(border=True):
            st.markdown(f"**{t(sided['one_sided_left']['title'])}**")
            st.latex(sided['one_sided_left']['formula'])
            st.markdown(f"*{t(sided['one_sided_left']['meaning'])}*")
            st.markdown("---")
            st.caption(f"{t({'de': 'Signalwörter', 'en': 'Signal words'})}: {t(sided['one_sided_left']['signal'])}")
    
    with col3:
        with st.container(border=True):
            st.markdown(f"**{t(sided['two_sided']['title'])}**")
            st.latex(sided['two_sided']['formula'])
            st.markdown(f"*{t(sided['two_sided']['meaning'])}*")
            st.markdown("---")
            st.caption(f"{t({'de': 'Signalwörter', 'en': 'Signal words'})}: {t(sided['two_sided']['signal'])}")
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # ==========================================================================
    # 5. INTERACTIVE HYPOTHESIS CLASSIFIER
    # ==========================================================================
    st.markdown(f"### {t({'de': 'Interaktiv: Hypothesen-Klassifizierer', 'en': 'Interactive: Hypothesis Classifier'})}")
    
    st.markdown(f"""
<div style="background: #f4f4f5; border-left: 4px solid #a1a1aa; 
            padding: 12px 16px; border-radius: 8px; color: #3f3f46; margin-bottom: 16px;">
<strong>{t({"de": "Mission", "en": "Mission"})}:</strong><br>
{t({"de": "Klassifiziere die Hypothesen in jedem Szenario. Ist H₀ einfach oder zusammengesetzt? Ist H₁ einseitig oder zweiseitig?",
    "en": "Classify the hypotheses in each scenario. Is H₀ simple or composite? Is H₁ one-sided or two-sided?"})}
</div>
""", unsafe_allow_html=True)
    
    hypothesis_classifier()
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # ==========================================================================
    # 6. ASK YOURSELF (Frag Dich)
    # ==========================================================================
    render_ask_yourself(
        header=content_10_1["frag_dich"]["header"],
        questions=content_10_1["frag_dich"]["questions"],
        conclusion=content_10_1["frag_dich"]["conclusion"]
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # ==========================================================================
    # 7. EXAM ESSENTIALS
    # ==========================================================================
    render_exam_essentials(
        trap=content_10_1["exam_essentials"]["trap"],
        trap_rule=content_10_1["exam_essentials"]["trap_rule"],
        tips=content_10_1["exam_essentials"]["tips"]
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # ==========================================================================
    # 8. MCQ
    # ==========================================================================
    st.markdown(f"### {t({'de': 'Übung', 'en': 'Exercise'})}")
    
    mcq = content_10_1["mcq"]
    opts = mcq["options"]
    opt_labels = [t({"de": o["de"], "en": o["en"]}) for o in opts]
    correct_idx = next((i for i, o in enumerate(opts) if o["id"] == mcq["correct_id"]), 0)
    
    render_mcq(
        key_suffix="10_1_types",
        question_text=t(mcq["question"]),
        options=opt_labels,
        correct_idx=correct_idx,
        solution_text_dict=mcq["solution"],
        success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
        error_msg_dict={"de": "Falsch.", "en": "Incorrect."},
        client=model,
        ai_context="Topic 10.1: Types of Hypotheses - testing understanding of simple vs composite and one-sided vs two-sided hypotheses",
        course_id="vwl",
        topic_id="10",
        subtopic_id="10.1",
        question_id="10_1_types"
    )
