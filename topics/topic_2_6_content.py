# Topic 2.6: Summary — Elementary Combinatorics
import streamlit as st
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
                "tip": {"de": "$\\binom{n}{k} = \\binom{n}{n-k}$. 3 aus 10 wählen = 7 ausschließen!", "en": "$\\binom{n}{k} = \\binom{n}{n-k}$. Choose 3 from 10 = Exclude 7!"}
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
                "wrong": {"de": "C(n,k) bei Podium", "en": "C(n,k) for podium"},
                "right": {"de": "P(n,k) bei Podium", "en": "P(n,k) for podium"}
            },
            {
                "trap": {"de": "Zurücklegen vergessen", "en": "Forgetting replacement"},
                "wrong": {"de": "P(10,4) für PIN", "en": "P(10,4) for PIN"},
                "right": {"de": "10⁴ für PIN", "en": "10⁴ for PIN"}
            },
            {
                "trap": {"de": "Gruppen doppelt zählen", "en": "Double counting groups"},
                "wrong": {"de": "n·(n-1) für Paare", "en": "n·(n-1) for pairs"},
                "right": {"de": "n·(n-1)/2 für Paare", "en": "n·(n-1)/2 for pairs"}
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
    
    # --- CSS ---
    st.markdown("""
    <style>
    [data-testid="stHorizontalBlock"] { align-items: stretch !important; }
    [data-testid="column"] { display: flex !important; flex-direction: column !important; }
    [data-testid="column"] > div { flex: 1 !important; }
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
    """Render pro tips section"""
    pt = content_2_6["pro_tricks"]
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
    traps = content_2_6["traps"]
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
