# Topic 2.6: Summary — Elementary Combinatorics
import streamlit as st
from views.styles import inject_equal_height_css
from utils.localization import t
from utils.quiz_helper import render_mcq
from data.exam_questions import get_question
from utils.progress_tracker import track_question_answer, update_local_progress

# ==========================================
# 1. CONTENT DICTIONARY
# ==========================================
content_2_6 = {
    "title": {"de": "2.6 Zusammenfassung", "en": "2.6 Summary"},
    "subtitle": {"de": "Elementare Kombinatorik auf einen Blick", "en": "Elementary Combinatorics at a Glance"},
    
    "cheat_sheet": {
        "header": {"de": "Das Entscheidungs-Kompendium", "en": "The Decision Compendium"},
        "cards": [
            {
                "title": {"de": "Permutation (alle n)", "en": "Permutation (all n)"},
                "formula": r"n!",
                "when": {"de": "Alle anordnen", "en": "Arrange ALL"},
                "example": {"de": "5 Bücher in Regal", "en": "5 books on shelf"}
            },
            {
                "title": {"de": "Permutation (k aus n)", "en": "Permutation (k from n)"},
                "formula": r"\frac{n!}{(n-k)!}",
                "when": {"de": "Reihenfolge wichtig", "en": "Order matters"},
                "example": {"de": "Podium 1-2-3", "en": "Podium 1-2-3"}
            },
            {
                "title": {"de": "Kombination", "en": "Combination"},
                "formula": r"\binom{n}{k} = \frac{n!}{k!(n-k)!}",
                "when": {"de": "Reihenfolge egal", "en": "Order doesn't matter"},
                "example": {"de": "Team auswählen", "en": "Choosing a team"}
            },
            {
                "title": {"de": "Variation mit Zurücklegen", "en": "Variation w/ Replacement"},
                "formula": r"n^k",
                "when": {"de": "Mit Wiederholung", "en": "With repetition"},
                "example": {"de": "PIN-Code (0-9)", "en": "PIN code (0-9)"}
            }
        ]
    },
    
    "pro_tricks": {
        "header": {"de": "Pro-Tricks", "en": "Pro Tricks"},
        "subtitle": {"de": "Was Top-Studenten wissen", "en": "What Top Students Know"},
        "tricks": [
            {
                "title": {"de": "Der Order-Test", "en": "The Order Test"},
                "tip": {"de": "Reihenfolge wichtig? → Permutation. Egal? → Kombination.", "en": "Order matters? → Permutation. Doesn't? → Combination."}
            },
            {
                "title": {"de": "Multiplikationsprinzip", "en": "Multiplication Principle"},
                "tip": {"de": "Mehrere Stufen? → Multipliziere die Anzahlen!", "en": "Multiple stages? → Multiply the counts!"}
            },
            {
                "title": {"de": "Symmetrie-Trick", "en": "Symmetry Trick"},
                "tip_text": {"de": "3 aus 10 wählen = 7 ausschließen!", "en": "Choose 3 from 10 = Exclude 7!"},
                "formula": r"\binom{n}{k} = \binom{n}{n-k}"
            },
            {
                "title": {"de": "Der Divisions-Hack", "en": "The Division Hack"},
                "tip": {"de": "Doppelt gezählt? → Durch Anzahl der Anordnungen teilen!", "en": "Double counted? → Divide by number of arrangements!"}
            }
        ]
    },
    
    "traps": {
        "header": {"de": "Prüfungsfallen", "en": "Exam Traps"},
        "items": [
            {
                "trap": {"de": "P vs C verwechseln", "en": "Confusing P vs C"},
                "wrong_formula": r"C(n,k)",
                "wrong_context": {"de": "bei Podium", "en": "for podium"},
                "right_formula": r"P(n,k)",
                "right_context": {"de": "bei Podium", "en": "for podium"}
            },
            {
                "trap": {"de": "Zurücklegen vergessen", "en": "Forgetting replacement"},
                "wrong_formula": r"P(10,4)",
                "wrong_context": {"de": "für PIN", "en": "for PIN"},
                "right_formula": r"10^4",
                "right_context": {"de": "für PIN", "en": "for PIN"}
            },
            {
                "trap": {"de": "Gruppen doppelt zählen", "en": "Double counting groups"},
                "wrong_formula": r"n \cdot (n-1)",
                "wrong_context": {"de": "für Paare", "en": "for pairs"},
                "right_formula": r"\frac{n \cdot (n-1)}{2}",
                "right_context": {"de": "für Paare", "en": "for pairs"}
            }
        ]
    },
    
    "compass": {
        "header": {"de": "Der Zähl-Kompass", "en": "The Counting Compass"},
        "desc": {"de": "Beantworte zwei Fragen, finde die richtige Formel!", "en": "Answer two questions, find the right formula!"},
        "q1": {"de": "Ist die Reihenfolge wichtig?", "en": "Does order matter?"},
        "q2": {"de": "Mit Zurücklegen (Wiederholung)?", "en": "With replacement (repetition)?"}
    }
}


def render_subtopic_2_6(model):
    """2.6 Summary — Complete combinatorics review"""
    inject_equal_height_css()
    
    # --- CSS: Equal height (AGGRESSIVE) ---
    st.markdown("""
    <style>
    /* Force horizontal blocks to stretch children */
    [data-testid="stHorizontalBlock"] {
        align-items: stretch !important;
        display: flex !important;
    }
    
    /* Make columns flex containers that fill height */
    [data-testid="column"], [data-testid="stColumn"] {
        display: flex !important;
        flex-direction: column !important;
        flex: 1 !important;
    }
    
    /* All direct children should expand */
    [data-testid="column"] > div,
    [data-testid="stColumn"] > div {
        flex: 1 !important; 
        display: flex !important;
        flex-direction: column !important;
        height: 100% !important;
        min-height: 100% !important;
    }
    
    /* Target the border wrapper specifically */
    [data-testid="column"] [data-testid="stVerticalBlockBorderWrapper"],
    [data-testid="stColumn"] [data-testid="stVerticalBlockBorderWrapper"] {
        flex: 1 !important;
        height: 100% !important;
        min-height: 100% !important;
        display: flex !important;
        flex-direction: column !important;
    }
    
    /* And its child */
    [data-testid="stVerticalBlockBorderWrapper"] > div {
        flex: 1 !important;
        height: 100% !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.header(t(content_2_6["title"]))
    st.caption(t(content_2_6["subtitle"]))
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
    
    # === SECTION 4: COUNTING COMPASS ===
    render_counting_compass()
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # === SECTION 5: EXAM PRACTICE ===
    st.markdown(f"### {t({'de': 'Prüfungstraining', 'en': 'Exam Practice'})}")
    
    question_ids = ["test1_mc3", "test2_mc1"]
    
    for q_id in question_ids:
        q = get_question("2.6", q_id)
        if q:
            with st.container(border=True):
                st.caption(q.get("source", ""))
                opts = q.get("options", [])
                if opts and isinstance(opts[0], dict):
                    option_labels = [t(o) for o in opts]
                else:
                    option_labels = opts
                
                render_mcq(
                    key_suffix=f"2_6_{q_id}",
                    question_text=t(q["question"]),
                    options=option_labels,
                    correct_idx=q["correct_idx"],
                    solution_text_dict=q["solution"],
                    success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                    error_msg_dict={"de": "Falsch.", "en": "Incorrect."},
                    client=model,
                    ai_context=f"Combinatorics: {q_id}",
                    course_id="vwl",
                    topic_id="2",
                    subtopic_id="2.6",
                    question_id=q_id
                )
            st.markdown("<br>", unsafe_allow_html=True)


def render_cheat_sheet():
    """Render formula quick reference cards"""
    cs = content_2_6["cheat_sheet"]
    st.markdown(f"### {t(cs['header'])}")
    
    cards = cs["cards"]
    
    # 2 rows of 2 cards (cleaner for combinatorics)
    c1, c2 = st.columns(2, gap="medium")
    for col, card in zip([c1, c2], cards[:2]):
        with col:
            with st.container(border=True):
                st.markdown(f"**{t(card['title'])}**")
                st.latex(card['formula'])
                st.caption(f"{t(card['when'])} — *{t(card['example'])}*")
    
    c3, c4 = st.columns(2, gap="medium")
    for col, card in zip([c3, c4], cards[2:]):
        with col:
            with st.container(border=True):
                st.markdown(f"**{t(card['title'])}**")
                st.latex(card['formula'])
                st.caption(f"{t(card['when'])} — *{t(card['example'])}*")


def render_pro_tricks():
    """Render pro tips section - using native Streamlit for equal height"""
    pt = content_2_6["pro_tricks"]
    st.markdown(f"### {t(pt['header'])}")
    st.caption(t(pt['subtitle']))
    
    tricks = pt["tricks"]
    
    # Row 1
    c1, c2 = st.columns(2, gap="medium")
    for col, trick in zip([c1, c2], tricks[:2]):
        with col:
            with st.container(border=True):
                st.markdown(f"**{t(trick['title'])}**")
                st.markdown(t(trick['tip']), unsafe_allow_html=True)
    
    # Row 2
    c3, c4 = st.columns(2, gap="medium")
    for col, trick in zip([c3, c4], tricks[2:]):
        with col:
            with st.container(border=True):
                st.markdown(f"**{t(trick['title'])}**")
                # Handle formula separately if present
                if "formula" in trick:
                    st.latex(trick["formula"])
                    st.markdown(t(trick.get("tip_text", trick.get("tip", {}))), unsafe_allow_html=True)
                else:
                    st.markdown(t(trick['tip']), unsafe_allow_html=True)


def render_exam_traps():
    """Render common exam traps with proper LaTeX"""
    traps = content_2_6["traps"]
    st.markdown(f"### {t(traps['header'])}")
    
    with st.container(border=True):
        # Header row
        col_trap, col_wrong, col_right = st.columns(3)
        with col_trap:
            st.markdown(f"**{t({'de': 'Falle', 'en': 'Trap'})}**")
        with col_wrong:
            st.markdown(f"<span style='color:#dc2626; font-weight:600;'>{t({'de': 'Falsch', 'en': 'Wrong'})}</span>", unsafe_allow_html=True)
        with col_right:
            st.markdown(f"<span style='color:#16a34a; font-weight:600;'>{t({'de': 'Richtig', 'en': 'Right'})}</span>", unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Each trap row
        for item in traps["items"]:
            col_trap, col_wrong, col_right = st.columns(3)
            with col_trap:
                st.markdown(f"**{t(item['trap'])}**")
            with col_wrong:
                st.latex(f"\\color{{red}}{{{item['wrong_formula']}}}")
                st.caption(t(item['wrong_context']))
            with col_right:
                st.latex(f"\\color{{green}}{{{item['right_formula']}}}")
                st.caption(t(item['right_context']))


def render_counting_compass():
    """Interactive decision tree for choosing the right formula"""
    compass = content_2_6["compass"]
    st.markdown(f"### {t(compass['header'])}")
    
    with st.container(border=True):
        st.markdown(t(compass["desc"]))
        st.markdown("---")
        
        # State
        if "compass_order" not in st.session_state:
            st.session_state.compass_order = None
        if "compass_replace" not in st.session_state:
            st.session_state.compass_replace = None
        if "compass_done" not in st.session_state:
            st.session_state.compass_done = False
        
        col_q, col_result = st.columns([1, 1.5], gap="large")
        
        with col_q:
            # Question 1: Order matters?
            st.markdown(f"**{t(compass['q1'])}**")
            order = st.pills(
                "order", 
                options=[t({"de": "Ja", "en": "Yes"}), t({"de": "Nein", "en": "No"})],
                key="compass_order_pills",
                label_visibility="collapsed"
            )
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            # Question 2: With replacement?
            st.markdown(f"**{t(compass['q2'])}**")
            replace = st.pills(
                "replace",
                options=[t({"de": "Ja", "en": "Yes"}), t({"de": "Nein", "en": "No"})],
                key="compass_replace_pills",
                label_visibility="collapsed"
            )
        
        with col_result:
            # Determine result based on selections
            yes_label = t({"de": "Ja", "en": "Yes"})
            no_label = t({"de": "Nein", "en": "No"})
            
            if order and replace:
                order_yes = (order == yes_label)
                replace_yes = (replace == yes_label)
                
                if order_yes and replace_yes:
                    # Order + Replacement = Variation with replacement
                    formula = r"n^k"
                    name = t({"de": "Variation mit Zurücklegen", "en": "Variation with Replacement"})
                    example = t({"de": "PIN-Code: 10⁴ = 10,000", "en": "PIN code: 10⁴ = 10,000"})
                    color = "#007AFF"
                elif order_yes and not replace_yes:
                    # Order + No replacement = Permutation
                    formula = r"\frac{n!}{(n-k)!}"
                    name = t({"de": "Permutation", "en": "Permutation"})
                    example = t({"de": "Podium: P(10,3) = 720", "en": "Podium: P(10,3) = 720"})
                    color = "#AF52DE"
                elif not order_yes and replace_yes:
                    # No order + Replacement = Combination with replacement
                    formula = r"\binom{n+k-1}{k}"
                    name = t({"de": "Kombination mit Zurücklegen", "en": "Combination with Replacement"})
                    example = t({"de": "Süßigkeiten wählen", "en": "Choosing candies"})
                    color = "#FF9500"
                else:
                    # No order + No replacement = Combination
                    formula = r"\binom{n}{k}"
                    name = t({"de": "Kombination", "en": "Combination"})
                    example = t({"de": "Team: C(10,3) = 120", "en": "Team: C(10,3) = 120"})
                    color = "#34C759"
                
                # Track mission completion
                if not st.session_state.compass_done:
                    st.session_state.compass_done = True
                    user = st.session_state.get("user")
                    if user:
                        track_question_answer(user["localId"], "vwl", "2", "2.6", "2_6_compass_mission", True)
                        update_local_progress("2", "2.6", "2_6_compass_mission", True)
                
                # Result display
                st.markdown(f"""
                <div style="background: {color}20; border: 2px solid {color}; border-radius: 12px; padding: 20px; text-align: center;">
                    <div style="font-weight: 700; font-size: 1.2em; color: {color}; margin-bottom: 12px;">{name}</div>
                </div>
                """, unsafe_allow_html=True)
                st.latex(formula)
                st.caption(example)
            else:
                st.info(t({"de": "Beantworte beide Fragen!", "en": "Answer both questions!"}))
        
        # Pro tip
        st.markdown(f"""
        <div style="background: #f4f4f5; border-radius: 8px; padding: 12px; color: #3f3f46; margin-top: 12px;">
            <strong>Pro Tip:</strong> {t({'de': 'Frag dich immer: "Ist ABC ≠ CBA?" Wenn ja → Reihenfolge wichtig!', 'en': 'Always ask: "Is ABC ≠ CBA?" If yes → Order matters!'})}
        </div>
        """, unsafe_allow_html=True)
