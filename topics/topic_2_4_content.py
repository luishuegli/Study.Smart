import streamlit as st
from math import factorial
from utils.localization import t
from utils.layouts.foundation import grey_info
from utils.quiz_helper import render_mcq
from data.exam_questions import get_question
from data.exam_questions import get_question
from views.styles import render_icon, inject_equal_height_css

# --- CONTENT DICTIONARY (BILINGUAL) ---
content_2_4 = {
    "title": {"de": "2.4 Kombinationen (Auswahl ohne Reihenfolge)", "en": "2.4 Combinations (Selection Without Order)"},
    
    "intro": {
        "de": "Bei Kombinationen zählt nur WER ausgewählt wird, nicht in welcher Reihenfolge.",
        "en": "In combinations, only WHO is selected matters, not the order of selection."
    },
    
    "context_anchor": {
        "de": """**Zurück zum Konzertkomitee:**

Wir wählen 3 Musiker für ein Komitee aus 5 Kandidaten: Alice, Bob, Charlie, Diana, Ethan.

**Die entscheidende Frage:** 
- Ist {Alice, Bob, Charlie} dasselbe Komitee wie {Charlie, Bob, Alice}?
- **JA!** Es sind dieselben drei Personen – nur in anderer Reihenfolge genannt.

Das ist der Kern von **Kombinationen**: Die Reihenfolge der Auswahl spielt keine Rolle.""",
        "en": """**Back to the Concert Committee:**

We're selecting 3 musicians for a committee from 5 candidates: Alice, Bob, Charlie, Diana, Ethan.

**The key question:** 
- Is {Alice, Bob, Charlie} the same committee as {Charlie, Bob, Alice}?
- **YES!** They're the same three people – just named in different order.

This is the essence of **Combinations**: The order of selection doesn't matter."""
    },
    
    "worked_example_title": {"de": "Durchgerechnetes Beispiel: Warum durch k! teilen?", "en": "Worked Example: Why Divide by k!?"},
    
    "formula": {
        "title": {"de": "Kombinationsformel", "en": "Combination Formula"},
        "latex": r"C(n, k) = \binom{n}{k} = \frac{n!}{k! \cdot (n - k)!}",
        "intuition": {"de": "Teamfoto: Egal wer wo steht.", "en": "Team photo: nobody cares who stands where."},
        "example": {"de": "Lotto: 6 aus 49 Zahlen", "en": "Lottery: Pick 6 from 49 numbers"},
        "pro_tip": {"de": "Würde Tauschen das Ergebnis ändern? NEIN → Teile durch k!", "en": "Would swapping change the outcome? NO → Divide by k!"}
    },
    
    "interactive_title": {"de": "Komitee-Baukasten", "en": "Committee Builder"},
    "interactive_instr": {
        "de": "Wähle genau 3 Musiker aus. Beobachte: Egal in welcher Reihenfolge du klickst – das System sortiert automatisch!",
        "en": "Select exactly 3 musicians. Notice: No matter what order you click – the system auto-sorts!"
    },
    
    "contrast_title": {"de": "Kontrast: Permutation vs. Kombination", "en": "Contrast: Permutation vs. Combination"},
    
    "exam": {
        "title": {"de": "Prüfungstraining", "en": "Exam Practice"},
        "source": "Combination Practice"
    },
    
    # --- FRAG DICH (Ask Yourself) ---
    "frag_dich": {
        "header": {"de": "Frag dich: Kombination oder Permutation?", "en": "Ask yourself: Combination or Permutation?"},
        "questions": [
            {"de": "Wärst du <strong>verärgert</strong>, wenn die Reihenfolge sich ändert?", "en": "Would you be <strong>upset</strong> if the order changed?"},
            {"de": "Ist es ein <strong>Team</strong> (egal wo jeder steht) oder ein <strong>Podium</strong> (Gold ≠ Silber)?", "en": "Is it a <strong>team</strong> (doesn't matter where people stand) or a <strong>podium</strong> (Gold ≠ Silver)?"},
            {"de": "Enthält das Ergebnis <strong>geschweifte Klammern</strong> {A,B,C} oder eine <strong>Sequenz</strong> (A→B→C)?", "en": "Does the result have <strong>curly braces</strong> {A,B,C} or a <strong>sequence</strong> (A→B→C)?"}
        ],
        "conclusion": {"de": "Nicht verärgert / Team / Klammern → Kombination (÷ k!).", "en": "Not upset / Team / Braces → Combination (÷ k!)."}
    },
    
    # --- EXAM ESSENTIALS ---
    "exam_essentials": {
        "trap": {
            "de": "Kombinations-Formel verwenden, wenn Reihenfolge <strong>doch</strong> zählt! Du verlierst Punkte, wenn du bei Podium-Problemen durch k! teilst.",
            "en": "Using Combination formula when order <strong>does</strong> matter! You lose points if you divide by k! on podium problems."
        },
        "trap_rule": {
            "de": "Frag dich: Ist {A,B} = {B,A}? JA → Kombination. NEIN → Permutation!",
            "en": "Ask yourself: Is {A,B} = {B,A}? YES → Combination. NO → Permutation!"
        },
        "tips": [
            {
                "tip": {"de": "Kombination = Permutation ÷ k!", "en": "Combination = Permutation ÷ k!"},
                "why": {"de": "Wir entfernen die k! 'Geister' (identische Gruppen in anderer Reihenfolge).", "en": "We remove the k! 'ghosts' (identical groups in different orders)."}
            },
            {
                "tip": {"de": "Signalwörter: 'Team', 'Gruppe', 'Menge', 'wählen'", "en": "Signal words: 'team', 'group', 'set', 'choose'"},
                "why": {"de": "Diese Wörter deuten auf 'keine Reihenfolge' hin → Kombination.", "en": "These words suggest 'no order' → Combination."}
            },
            {
                "tip": {"de": "Immer das Beispiel durchdenken!", "en": "Always think through the example!"},
                "why": {"de": "Tausche zwei Elemente. Wenn das Ergebnis gleich bleibt → Kombination.", "en": "Swap two elements. If the result stays the same → Combination."}
            }
        ]
    }
}

# --- MAIN RENDERING FUNCTION ---
def render_subtopic_2_4(model):
    """Renders Section 2.4: Combinations (Selection Without Order)"""
    inject_equal_height_css()
    
    # --- HEADER ---
    st.header(t(content_2_4["title"]))
    st.markdown("---")
    
    # --- THEORY SECTION (Following Pedagogy Rules) ---
    
    # 1. THE INTUITION (Outside container)
    st.markdown(f"### {t({'de': 'Die Intuition', 'en': 'The Intuition'})}")
    with st.container(border=True):
        st.markdown(t({
            "de": "Stell dir vor, du wählst 3 Freunde für ein Lotto-Syndikat. Es ist egal, ob du zuerst Anna, dann Ben, dann Clara wählst oder Ben → Clara → Anna. Am Ende ist es **dieselbe Gruppe**. Bei Kombinationen zählt nur WER drin ist, nicht WANN sie gewählt wurden.",
            "en": "Imagine picking 3 friends for a lottery syndicate. It doesn't matter if you pick Anna first, then Ben, then Clara - or Ben → Clara → Anna. In the end, it's the **same group**. With combinations, only WHO is in matters, not WHEN they were picked."
        }))
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # 2. THE FORMULA + VARIABLE DECODER + KEY INSIGHT (Single container)
    st.markdown(f"### {t({'de': 'Die Formel', 'en': 'The Formula'})}")
    with st.container(border=True):
        # Formula
        st.latex(r"C(n,k) = \binom{n}{k} = \frac{n!}{k!(n-k)!}")
        st.caption(t({"de": "Kombination: k Elemente aus n auswählen (Reihenfolge egal)", "en": "Combination: select k elements from n (order irrelevant)"}))
        
        st.markdown("---")
        
        # Variable Decoder
        st.markdown(f"**{t({'de': 'Die Variablen erklärt', 'en': 'The Variables Explained'})}:**")
        st.markdown(f"""
• $n$ = **{t({"de": "Pool", "en": "Pool"})}** — {t({"de": "Wie viele Elemente stehen zur Verfügung?", "en": "How many elements are available?"})}

• $k$ = **{t({"de": "Auswahl", "en": "Selection"})}** — {t({"de": "Wie viele wählen wir aus?", "en": "How many do we choose?"})}

• $k!$ = **{t({"de": "Die Geister", "en": "The Ghosts"})}** — {t({"de": "Wie viele 'Duplikate' entstehen durch verschiedene Reihenfolgen?", "en": "How many 'duplicates' arise from different orderings?"})}

• $\\binom{{n}}{{k}}$ = **{t({"de": "Binomialkoeffizient", "en": "Binomial Coefficient"})}** — {t({"de": "'n über k' - die Anzahl einzigartiger Gruppen", "en": "'n choose k' - the number of unique groups"})}
""")
        
        st.markdown("---")
        
        # Key Insight
        st.markdown(f"*{t({'de': 'Der Schlüssel: Kombination = Permutation ÷ k! Die k! Geister sind identische Gruppen, die in verschiedener Reihenfolge gewählt wurden. Wir teilen sie heraus!', 'en': 'The key: Combination = Permutation ÷ k! The k! ghosts are identical groups picked in different orders. We divide them out!'})}*")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- CONTEXT ANCHOR (Now just a scenario introduction) ---
    with st.container(border=True):
        st.markdown(t(content_2_4["context_anchor"]))
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- WORKED EXAMPLE: WHY DIVIDE BY K! ---
    with st.container(border=True):
        st.markdown(f"### {t(content_2_4['worked_example_title'])}")
        
        # --- STEP 1 ---
        col1_theory, col1_math = st.columns([1.4, 1], gap="large", vertical_alignment="center")
        with col1_theory:
            st.markdown(f"**{t({'de': 'Schritt 1: Wenn Reihenfolge zählen würde', 'en': 'Step 1: If order mattered'})}**")
            st.markdown(f"""
<div style="background: #f4f4f5; border-left: 3px solid #71717a; padding: 12px; border-radius: 6px; color: #3f3f46;">
{t({"de": "Wähle 2 aus {{A, B, C}}. Mit Reihenfolge wären das:",
    "en": "Pick 2 from {{A, B, C}}. With order, these would be:"})}
<br><br>
A→B, B→A, A→C, C→A, B→C, C→B = <b>6 {t({"de": "Ergebnisse", "en": "results"})}</b>
<br><br>
{t({"de": "Formel: P(3,2) = 3 × 2 = 6", "en": "Formula: P(3,2) = 3 × 2 = 6"})}
</div>
""", unsafe_allow_html=True)
        with col1_math:
            st.latex(r"P(3,2) = \frac{3!}{(3-2)!} = \frac{6}{1} = 6")
        
        st.markdown("---")
        
        # --- STEP 2 ---
        col2_theory, col2_math = st.columns([1.4, 1], gap="large", vertical_alignment="center")
        with col2_theory:
            st.markdown(f"**{t({'de': 'Schritt 2: Bemerke die Duplikate', 'en': 'Step 2: Notice the duplicates'})}**")
            st.markdown(f"""
<div style="background: #f4f4f5; border-left: 3px solid #71717a; padding: 12px; border-radius: 6px; color: #3f3f46;">
{t({"de": "Aber für ein KOMITEE sind diese GLEICH:", "en": "But for a COMMITTEE, these are THE SAME:"})}
<br><br>
{{A, B}} = {{B, A}} → {t({"de": "Beide beschreiben dieselbe 2er-Gruppe!", "en": "Both describe the same 2-person group!"})}
<br><br>
{t({"de": "Jedes Paar wurde 2! = 2 mal gezählt.", "en": "Each pair was counted 2! = 2 times."})}
</div>
""", unsafe_allow_html=True)
        with col2_math:
            st.latex(r"k! = 2! = 2")
        
        st.markdown("---")
        
        # --- STEP 3 ---
        col3_theory, col3_math = st.columns([1.4, 1], gap="large", vertical_alignment="center")
        with col3_theory:
            st.markdown(f"**{t({'de': 'Schritt 3: Teile durch k!', 'en': 'Step 3: Divide by k!'})}**")
            st.markdown(f"""
<div style="background: #f4f4f5; border-left: 3px solid #71717a; padding: 12px; border-radius: 6px; color: #3f3f46;">
6 ÷ 2! = 6 ÷ 2 = <b>3</b> {t({"de": "einzigartige Komitees", "en": "unique committees"})}
<br><br>
{{A, B}}, {{A, C}}, {{B, C}}
</div>
""", unsafe_allow_html=True)
        with col3_math:
            st.latex(r"C(3,2) = \frac{P(3,2)}{k!} = \frac{6}{2} = 3")
            st.markdown("<br>", unsafe_allow_html=True)
            st.latex(r"C(n,k) = \frac{n!}{k!(n-k)!}")
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- INTERACTIVE: COMMITTEE BUILDER ---
    with st.container(border=True):
        st.markdown(f"### {t(content_2_4['interactive_title'])}")
        st.caption(t(content_2_4['interactive_instr']))
        
        # State initialization (Rule 6.3)
        if "committee_2_4" not in st.session_state:
            st.session_state.committee_2_4 = []
        
        musicians = ["Alice", "Bob", "Charlie", "Diana", "Ethan"]
        
        col_select, col_display = st.columns([1.5, 1.5], gap="large")
        
        with col_select:
            st.markdown(f"**{t({'de': 'Verfügbare Musiker', 'en': 'Available Musicians'})}**")
            
            cols = st.columns(3)
            for idx, musician in enumerate(musicians):
                col_idx = idx % 3
                is_selected = musician in st.session_state.committee_2_4
                btn_type = "primary" if is_selected else "secondary"
                
                with cols[col_idx]:
                    if st.button(musician, key=f"musician_2_4_{musician}", type=btn_type, use_container_width=True):
                        if is_selected:
                            st.session_state.committee_2_4.remove(musician)
                        elif len(st.session_state.committee_2_4) < 3:
                            st.session_state.committee_2_4.append(musician)
                        st.rerun()
        
        with col_display:
            st.markdown(f"**{t({'de': 'Dein Komitee', 'en': 'Your Committee'})}**")
            
            # Auto-sort to prove order doesn't matter
            sorted_committee = sorted(st.session_state.committee_2_4)
            
            if len(st.session_state.committee_2_4) == 0:
                grey_info(t({"de": "Wähle 3 Musiker aus...", "en": "Select 3 musicians..."}))
            else:
                selection_order = " → ".join(st.session_state.committee_2_4)
                sorted_order = ", ".join(sorted_committee)
                
                st.markdown(f"""
**{t({"de": "Klick-Reihenfolge:", "en": "Click order:"})}**  
`{selection_order}`

**{t({"de": "Komitee (sortiert):", "en": "Committee (sorted):"})}**  
`{{{sorted_order}}}`
""")
                
                if len(st.session_state.committee_2_4) == 3:
                    st.success(t({
                        "de": "Egal in welcher Reihenfolge du geklickt hast – es ist DASSELBE Komitee!",
                        "en": "No matter what order you clicked – it's the SAME committee!"
                    }))
        
        st.markdown("<hr style='margin: 20px 0; border: 0; border-top: 1.5px solid #f3f4f6;'>", unsafe_allow_html=True)
        
        # Live math display
        n = 5
        k = len(st.session_state.committee_2_4) if len(st.session_state.committee_2_4) > 0 else 3
        
        if k > 0:
            c_result = factorial(n) // (factorial(k) * factorial(n - k))
            st.latex(rf"C({n}, {k}) = \frac{{{n}!}}{{{k}! \cdot {n-k}!}} = {c_result}")
            st.caption(t({
                "de": f"Es gibt genau {c_result} verschiedene {k}er-Komitees aus 5 Musikern.",
                "en": f"There are exactly {c_result} different {k}-person committees from 5 musicians."
            }))
        
        # Reset button
        if len(st.session_state.committee_2_4) > 0:
            if st.button(t({"de": "Zurücksetzen", "en": "Reset"}), key="reset_committee_2_4"):
                st.session_state.committee_2_4 = []
                st.rerun()
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- CONTRAST TABLE ---
    with st.container(border=True):
        st.markdown(f"### {t(content_2_4['contrast_title'])}")
        
        col_perm, col_comb = st.columns([1, 1], gap="large")
        
        with col_perm:
            st.markdown(f"**{t({'de': 'Permutation (2.3)', 'en': 'Permutation (2.3)'})}**")
            st.latex(r"P(n,k) = \frac{n!}{(n-k)!}")
            st.markdown(f"""
<div style="background: #f4f4f5; border-radius: 8px; padding: 16px;">
<b>{t({"de": "Reihenfolge ZÄHLT", "en": "Order MATTERS"})}</b><br><br>
{t({"de": "Beispiel: Podiumsplätze", "en": "Example: Podium places"})}<br>
{t({"de": "Gold-Silber-Bronze ≠ Bronze-Silber-Gold", "en": "Gold-Silver-Bronze ≠ Bronze-Silver-Gold"})}<br><br>
<b>{t({"de": "Test:", "en": "Test:"})}</b> {t({"de": "Wärst du sauer, wenn getauscht wird?", "en": "Would you be upset if positions swap?"})}<br>
→ {t({"de": "JA", "en": "YES"})} = Permutation
</div>
""", unsafe_allow_html=True)
        
        with col_comb:
            st.markdown(f"**{t({'de': 'Kombination (2.4)', 'en': 'Combination (2.4)'})}**")
            st.latex(r"C(n,k) = \frac{n!}{k!(n-k)!}")
            st.markdown(f"""
<div style="background: #f4f4f5; border-radius: 8px; padding: 16px;">
<b>{t({"de": "Reihenfolge EGAL", "en": "Order DOESN'T MATTER"})}</b><br><br>
{t({"de": "Beispiel: Teamauswahl", "en": "Example: Team selection"})}<br>
{{Alice, Bob}} = {{Bob, Alice}}<br><br>
<b>{t({"de": "Test:", "en": "Test:"})}</b> {t({"de": "Würde Tauschen etwas ändern?", "en": "Would swapping change anything?"})}<br>
→ {t({"de": "NEIN", "en": "NO"})} = {t({"de": "Kombination", "en": "Combination"})}
</div>
""", unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # -- FORMULA COMPASS (like 2.2) ---
    with st.container(border=True):
        st.markdown(f"### {t({'de': 'Formel-Kompass', 'en': 'Formula Compass'})}")
        
        col_formula, col_explain = st.columns([1, 1.2], gap="medium")
        
        with col_formula:
            st.markdown(f"**{t(content_2_4['formula']['title'])}**")
            st.latex(content_2_4['formula']['latex'])
        
        with col_explain:
            st.markdown(f"""
<div style="font-size: 0.95rem; color: #333; margin-bottom: 8px; display: flex; align-items: start; gap: 8px;">
    <span style="color: #666; margin-top: 2px;">{render_icon('lightbulb', size=16)}</span>
    <span>{t(content_2_4['formula']['intuition'])}</span>
</div>
<div style="font-size: 0.85rem; color: #666; padding-left: 26px; font-style: italic; margin-bottom: 12px;">
    Ex: {t(content_2_4['formula']['example'])}
</div>
<div style="background: #f4f4f5; border-left: 3px solid #71717a; padding: 24px 20px; border-radius: 6px; font-size: 0.9rem; color: #3f3f46;">
    <strong>Pro Tip:</strong> {t(content_2_4['formula']['pro_tip'])}
</div>
            """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- FRAG DICH (Ask Yourself) ---
    from utils.ask_yourself import render_ask_yourself
    render_ask_yourself(
        header=content_2_4["frag_dich"]["header"],
        questions=content_2_4["frag_dich"]["questions"],
        conclusion=content_2_4["frag_dich"]["conclusion"]
    )
    
    # --- EXAM ESSENTIALS ---
    st.markdown("<br><br>", unsafe_allow_html=True)
    from utils.exam_essentials import render_exam_essentials
    render_exam_essentials(
        trap=content_2_4["exam_essentials"]["trap"],
        trap_rule=content_2_4["exam_essentials"]["trap_rule"],
        tips=content_2_4["exam_essentials"]["tips"]
    )

    # --- EXAM SECTION ---
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown(f"### {t(content_2_4['exam']['title'])}")
    st.caption(t(content_2_4['exam']['source']))
    
    with st.container(border=True):
        q_data = get_question("2.4", "lottery")
        # Prepare options (handle dict/string)
        lottery_options = q_data["options"]
        if lottery_options and isinstance(lottery_options[0], dict):
            lottery_labels = [t(o) for o in lottery_options]
        else:
            lottery_labels = lottery_options

        render_mcq(
            key_suffix="2_4_lottery",
            question_text=t(q_data["question"]),
            options=lottery_labels,
            correct_idx=q_data["correct_idx"],
            solution_text_dict=q_data["solution"],
            success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
            error_msg_dict={"de": "Noch nicht ganz...", "en": "Not quite..."},
            client=model,
            ai_context="Combinations: Lottery problem C(49,6)",
            hint_text_dict={"de": r"$$C(n,k) = \frac{n!}{k!(n-k)!}$$", "en": r"$$C(n,k) = \frac{n!}{k!(n-k)!}$$"},
            course_id="vwl",
            topic_id="2",
            subtopic_id="2.4",
            question_id="q_2_4_lottery"
        )
    
    # --- ADDITIONAL EXAM QUESTION ---
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown(f"### {t({'de': 'Weitere Prüfungsaufgabe', 'en': 'Additional Exam Question'})}")
    
    with st.container(border=True):
        st.caption("Test 2, Frage 1 (Vorstand)")
        q_data_2 = get_question("2.4", "test2_q1")
        if q_data_2:
            opts = q_data_2.get("options", [])
            if opts and isinstance(opts[0], dict):
                option_labels = [t(o) for o in opts]
            else:
                option_labels = opts
            
            render_mcq(
                key_suffix="2_4_test2_q1",
                question_text=t(q_data_2["question"]),
                options=option_labels,
                correct_idx=q_data_2["correct_idx"],
                solution_text_dict=q_data_2["solution"],
                success_msg_dict={"de": "Richtig!", "en": "Correct!"},
                error_msg_dict={"de": "Falsch.", "en": "Incorrect."},
                client=model,
                ai_context="Combinations: Club board selection problem",
                course_id="vwl",
                topic_id="2",
                subtopic_id="2.4",
                question_id="2_4_test2_q1"
            )
