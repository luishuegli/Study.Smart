# Topic 1.11: Summary — Basics of Probability
import streamlit as st
from views.styles import inject_equal_height_css
from utils.localization import t
from utils.quiz_helper import render_mcq
from data.exam_questions import get_question
from utils.progress_tracker import track_question_answer, update_local_progress

# ==========================================
# 1. CONTENT DICTIONARY
# ==========================================
content_1_11 = {
    "title": {"de": "1.11 Zusammenfassung", "en": "1.11 Summary"},
    "subtitle": {"de": "Grundlagen der Wahrscheinlichkeit auf einen Blick", "en": "Basics of Probability at a Glance"},
    
    "cheat_sheet": {
        "header": {"de": "Das Formel-Kompendium", "en": "The Formula Compendium"},
        "cards": [
            {
                "title": {"de": "Komplement", "en": "Complement"},
                "formula": r"P(A^c) = 1 - P(A)",
                "when": {"de": "'Mindestens eins' = 1 - P(keins)", "en": "'At least one' = 1 - P(none)"}
            },
            {
                "title": {"de": "Addition (allg.)", "en": "Addition (general)"},
                "formula": r"P(A \cup B) = P(A) + P(B) - P(A \cap B)",
                "when": {"de": "Überlappung abziehen!", "en": "Subtract overlap!"}
            },
            {
                "title": {"de": "Addition (disjunkt)", "en": "Addition (disjoint)"},
                "formula": r"P(A \cup B) = P(A) + P(B)",
                "when": {"de": "Nur wenn A∩B = ∅", "en": "Only if A∩B = ∅"}
            },
            {
                "title": {"de": "Bedingte W'keit", "en": "Conditional Prob."},
                "formula": r"P(A|B) = \frac{P(A \cap B)}{P(B)}",
                "when": {"de": "Gegeben B ist eingetreten", "en": "Given B has occurred"}
            },
            {
                "title": {"de": "Unabhängigkeit", "en": "Independence"},
                "formula": r"P(A \cap B) = P(A) \cdot P(B)",
                "when": {"de": "Test: Gilt die Gleichung?", "en": "Test: Does equation hold?"}
            },
            {
                "title": {"de": "Totale W'keit", "en": "Total Probability"},
                "formula": r"P(A) = \sum_i P(A|B_i) \cdot P(B_i)",
                "when": {"de": "Partition in Fälle", "en": "Partition into cases"}
            },
            {
                "title": {"de": "Bayes", "en": "Bayes"},
                "formula": r"P(B|A) = \frac{P(A|B) \cdot P(B)}{P(A)}",
                "when": {"de": "Ursache aus Wirkung", "en": "Cause from effect"}
            }
        ]
    },
    
    "pro_tricks": {
        "header": {"de": "Pro-Tricks", "en": "Pro Tricks"},
        "subtitle": {"de": "Was Top-Studenten wissen", "en": "What Top Students Know"},
        "tricks": [
            {
                "title": {"de": "Komplement-Shortcut", "en": "Complement Shortcut"},
                "tip": {"de": "'Mindestens 1' ist kompliziert? → Berechne 1 - P(keins)!", "en": "'At least 1' is complex? → Compute 1 - P(none)!"}
            },
            {
                "title": {"de": "Disjunkt ≠ Unabhängig", "en": "Disjoint ≠ Independent"},
                "tip": {"de": "Disjunkt (A∩B=∅) bedeutet ABHÄNGIG, nicht unabhängig!", "en": "Disjoint (A∩B=∅) means DEPENDENT, not independent!"}
            },
            {
                "title": {"de": "Der Bayes-Flip", "en": "The Bayes Flip"},
                "tip": {"de": "P(A|B) gegeben? Bayes flippt zu P(B|A)!", "en": "P(A|B) given? Bayes flips to P(B|A)!"}
            },
            {
                "title": {"de": "Baum-Methode", "en": "Tree Method"},
                "tip": {"de": "Mehrstufig? Zeichne einen W'keitsbaum, multipliziere Pfade!", "en": "Multi-stage? Draw probability tree, multiply paths!"}
            }
        ]
    },
    
    "traps": {
        "header": {"de": "Prüfungsfallen", "en": "Exam Traps"},
        "items": [
            {
                "trap": {"de": "Disjunkt = Unabhängig", "en": "Disjoint = Independent"},
                "wrong": {"de": "A∩B=∅ → unabhängig", "en": "A∩B=∅ → independent"},
                "right": {"de": "Disjunkt → abhängig!", "en": "Disjoint → dependent!"}
            },
            {
                "trap": {"de": "Überlappung vergessen", "en": "Forgetting overlap"},
                "wrong": {"de": "P(A∪B) = P(A) + P(B)", "en": "P(A∪B) = P(A) + P(B)"},
                "right": {"de": "- P(A∩B) abziehen!", "en": "Subtract P(A∩B)!"}
            },
            {
                "trap": {"de": "Bayes ohne Total P", "en": "Bayes without Total P"},
                "wrong": {"de": "P(A) direkt einsetzen", "en": "Use P(A) directly"},
                "right": {"de": "P(A) via Totale W'keit!", "en": "P(A) via Total Prob!"}
            }
        ]
    },
    
    "finder": {
        "header": {"de": "Der Formel-Finder", "en": "The Formula Finder"},
        "desc": {"de": "Wähle das Szenario, erhalte die Formel!", "en": "Choose the scenario, get the formula!"},
        "scenarios": {
            "addition": {
                "label": {"de": "A oder B", "en": "A or B"},
                "formula": r"P(A \cup B) = P(A) + P(B) - P(A \cap B)",
                "example": {"de": "König oder Herz? P(K) + P(♥) - P(K♥)", "en": "King or Heart? P(K) + P(♥) - P(K♥)"},
                "color": "#007AFF"
            },
            "conditional": {
                "label": {"de": "A gegeben B", "en": "A given B"},
                "formula": r"P(A|B) = \frac{P(A \cap B)}{P(B)}",
                "example": {"de": "Regenschirm dabei, gegeben es regnet", "en": "Umbrella given it's raining"},
                "color": "#AF52DE"
            },
            "bayes": {
                "label": {"de": "Bayes Flip", "en": "Bayes Flip"},
                "formula": r"P(B|A) = \frac{P(A|B) \cdot P(B)}{P(A)}",
                "example": {"de": "Krankheit gegeben positiver Test", "en": "Disease given positive test"},
                "color": "#FF9500"
            },
            "independence": {
                "label": {"de": "Unabhängig?", "en": "Independent?"},
                "formula": r"P(A \cap B) \stackrel{?}{=} P(A) \cdot P(B)",
                "example": {"de": "Zwei Würfe: 6 dann 6?", "en": "Two rolls: 6 then 6?"},
                "color": "#34C759"
            }
        }
    }
}


def render_subtopic_1_11(model):
    """1.11 Summary — Complete probability review"""
    inject_equal_height_css()
    
    # --- CSS ---
    st.markdown("""
    <style>
    [data-testid="stHorizontalBlock"] { align-items: stretch !important; }
    [data-testid="column"] { display: flex !important; flex-direction: column !important; }
    [data-testid="column"] > div { flex: 1 !important; }
    </style>
    """, unsafe_allow_html=True)
    
    st.header(t(content_1_11["title"]))
    st.caption(t(content_1_11["subtitle"]))
    st.markdown("---")
    
    # === SECTION 1: CHEAT SHEET ===
    render_cheat_sheet()
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # === SECTION 2: PRO TRICKS ===
    render_pro_tricks()
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # === SECTION 3: EXAM TRAPS ===
    render_exam_traps()
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # === SECTION 4: FORMULA FINDER ===
    render_formula_finder()
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # === SECTION 5: EXAM PRACTICE ===
    render_exam_practice(model)


def render_cheat_sheet():
    """Render formula quick reference cards"""
    cs = content_1_11["cheat_sheet"]
    st.markdown(f"### {t(cs['header'])}")
    
    cards = cs["cards"]
    
    # Row 1: 3 cards
    cols = st.columns(3, gap="small")
    for col, card in zip(cols, cards[:3]):
        with col:
            with st.container(border=True):
                st.markdown(f"**{t(card['title'])}**")
                st.latex(card['formula'])
                st.caption(t(card['when']))
    
    # Row 2: 4 cards
    cols2 = st.columns(4, gap="small")
    for col, card in zip(cols2, cards[3:]):
        with col:
            with st.container(border=True):
                st.markdown(f"**{t(card['title'])}**")
                st.latex(card['formula'])
                st.caption(t(card['when']))


def render_pro_tricks():
    """Render pro tips section"""
    pt = content_1_11["pro_tricks"]
    st.markdown(f"### {t(pt['header'])}")
    st.caption(t(pt['subtitle']))
    
    with st.container(border=True):
        tricks = pt["tricks"]
        
        c1, c2 = st.columns(2, gap="medium")
        for col, trick in zip([c1, c2], tricks[:2]):
            with col:
                st.markdown(f"""
                <div style="background: #f4f4f5; border-radius: 8px; padding: 12px; margin-bottom: 8px;">
                    <div style="font-weight: 600; color: #3f3f46; margin-bottom: 6px;">{t(trick['title'])}</div>
                    <div style="font-size: 0.9em; color: #71717a;">{t(trick['tip'])}</div>
                </div>
                """, unsafe_allow_html=True)
        
        c3, c4 = st.columns(2, gap="medium")
        for col, trick in zip([c3, c4], tricks[2:]):
            with col:
                st.markdown(f"""
                <div style="background: #f4f4f5; border-radius: 8px; padding: 12px; margin-bottom: 8px;">
                    <div style="font-weight: 600; color: #3f3f46; margin-bottom: 6px;">{t(trick['title'])}</div>
                    <div style="font-size: 0.9em; color: #71717a;">{t(trick['tip'])}</div>
                </div>
                """, unsafe_allow_html=True)


def render_exam_traps():
    """Render common exam traps"""
    traps = content_1_11["traps"]
    st.markdown(f"### {t(traps['header'])}")
    
    with st.container(border=True):
        # Table header
        st.markdown(f"""
        <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 12px; font-weight: 600; margin-bottom: 12px; padding-bottom: 8px; border-bottom: 1px solid #e5e5ea;">
            <div>{t({'de': 'Falle', 'en': 'Trap'})}</div>
            <div style="color: #dc2626;">{t({'de': 'Falsch', 'en': 'Wrong'})}</div>
            <div style="color: #16a34a;">{t({'de': 'Richtig', 'en': 'Right'})}</div>
        </div>
        """, unsafe_allow_html=True)
        
        for item in traps["items"]:
            st.markdown(f"""
            <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 12px; padding: 8px 0; border-bottom: 1px solid #f4f4f5;">
                <div style="font-weight: 500;">{t(item['trap'])}</div>
                <div style="color: #dc2626; font-family: monospace;">{t(item['wrong'])}</div>
                <div style="color: #16a34a; font-family: monospace;">{t(item['right'])}</div>
            </div>
            """, unsafe_allow_html=True)


def render_formula_finder():
    """Interactive scenario selector for formulas"""
    finder = content_1_11["finder"]
    st.markdown(f"### {t(finder['header'])}")
    
    with st.container(border=True):
        st.markdown(t(finder["desc"]))
        st.markdown("---")
        
        # State
        if "finder_done" not in st.session_state:
            st.session_state.finder_done = False
        
        col_select, col_result = st.columns([1, 1.5], gap="large")
        
        scenarios = finder["scenarios"]
        
        with col_select:
            st.markdown(f"**{t({'de': 'Was suchst du?', 'en': 'What are you looking for?'})}**")
            
            # Pills for scenario selection
            options = [t(s["label"]) for s in scenarios.values()]
            selected = st.pills(
                "scenario",
                options=options,
                key="finder_scenario_pills",
                label_visibility="collapsed"
            )
        
        with col_result:
            if selected:
                # Find matching scenario
                scenario_key = None
                for key, val in scenarios.items():
                    if t(val["label"]) == selected:
                        scenario_key = key
                        break
                
                if scenario_key:
                    scenario = scenarios[scenario_key]
                    color = scenario["color"]
                    
                    # Track mission completion
                    if not st.session_state.finder_done:
                        st.session_state.finder_done = True
                        user = st.session_state.get("user")
                        if user:
                            track_question_answer(user["localId"], "vwl", "1", "1.11", "1_11_finder_mission", True)
                            update_local_progress("1", "1.11", "1_11_finder_mission", True)
                    
                    # Result display
                    st.markdown(f"""
                    <div style="background: {color}20; border: 2px solid {color}; border-radius: 12px; padding: 16px; text-align: center;">
                        <div style="font-weight: 700; font-size: 1.1em; color: {color}; margin-bottom: 8px;">{t(scenario['label'])}</div>
                    </div>
                    """, unsafe_allow_html=True)
                    st.latex(scenario['formula'])
                    st.caption(t(scenario['example']))
            else:
                st.info(t({"de": "Wähle ein Szenario!", "en": "Select a scenario!"}))
        
        # Pro tip
        st.markdown(f"""
        <div style="background: #f4f4f5; border-radius: 8px; padding: 12px; color: #3f3f46; margin-top: 12px;">
            <strong>Pro Tip:</strong> {t({'de': 'Bei Bayes-Aufgaben: Immer zuerst P(A) via Totale W\'keit berechnen!', 'en': 'For Bayes problems: Always compute P(A) via Total Probability first!'})}
        </div>
        """, unsafe_allow_html=True)


def render_exam_practice(model):
    """Render exam practice questions"""
    st.markdown(f"### {t({'de': 'Prüfungstraining', 'en': 'Exam Practice'})}")
    
    question_ids = [
        "hs2024_mc10",
        "uebung1_mc3", "uebung1_mc16",
        "hub_mc1", "hub_mc2", "hub_mc3", "hub_mc4",
        "test1_mc1", "test1_mc2", "test3_mc1"
    ]
    
    for q_id in question_ids:
        q = get_question("1.11", q_id)
        if q:
            # Skip multi-stage problems for now
            if q.get("type") == "multi_stage":
                continue
            
            with st.container(border=True):
                st.caption(q.get("source", ""))
                opts = q.get("options", [])
                if opts and isinstance(opts[0], dict):
                    option_labels = [t(o) for o in opts]
                else:
                    option_labels = opts
                
                render_mcq(
                    key_suffix=f"1_11_{q_id}",
                    question_text=t(q["question"]),
                    options=option_labels,
                    correct_idx=q.get("correct_idx", 0),
                    solution_text_dict=q["solution"],
                    success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                    error_msg_dict={"de": "Falsch.", "en": "Incorrect."},
                    client=model,
                    ai_context=f"Probability fundamentals: {q_id}",
                    course_id="vwl",
                    topic_id="1",
                    subtopic_id="1.11",
                    question_id=q_id
                )
            st.markdown("<br>", unsafe_allow_html=True)
