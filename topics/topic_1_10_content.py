import streamlit as st
from views.styles import render_icon, inject_equal_height_css
from utils.localization import t
from utils.quiz_helper import render_mcq, render_tab_progress_css

from utils.quiz_helper import render_mcq, render_tab_progress_css
from data.exam_questions import get_question
# 1. CONTENT DICTIONARY
# ==============================================================================
content_1_10 = {
    "title": {"de": "1.10 Zusammenfassung & Final Exam", "en": "1.10 Summary & Final Exam"},
    "intro": {"de": "Dein Wissens-Dashboard. Alles auf einen Blick.", "en": "Your Knowledge Dashboard. Everything at a glance."},
    
    # CHEAT SHEET: RICH CONTENT
    "cheat_sheet": {
        "col1": {
            "title": {"de": "Die Basis", "en": "The Basics"},
            "icon": "box",
            "color": "#007AFF", # Apple Blue
            "items": [
                {
                    "latex": r"P(A) = \frac{|A|}{|\Omega|}",
                    "title": {"de": "Laplace (Gleichverteilung)", "en": "Laplace (Equally Likely)"},
                    "intuition": {"de": "Günstige durch Mögliche.", "en": "Favorable over Possible."},
                    "pro_tip": {"de": "Funktioniert NUR bei Gleichverteilung. Gezinkter Würfel? Laplace versagt.", "en": "Only works when all outcomes are equally likely. Loaded dice? Laplace fails."},
                    "example": {"de": "Würfel 6: 1 Günstige / 6 Mögliche", "en": "Roll 6: 1 Favorable / 6 Possible"}
                },
                {
                    "latex": r"P(S) = 1",
                    "title": {"de": "Normierung", "en": "Normalization"},
                    "intuition": {"de": "Irgendetwas passiert immer (100%).", "en": "Something happens always (100%)."},
                    "pro_tip": {"de": "Prüfe deine Arbeit: Wenn die Summe ≠ 1, hast du einen Fehler gemacht.", "en": "Use this to check your work: if probabilities don't sum to 1, you made an error."},
                    "example": {"de": "Sonne + Regen + ... = 1", "en": "Sun + Rain + ... = 1"}
                },
                {
                    "latex": r"P(A^c) = 1 - P(A)",
                    "title": {"de": "Gegenwahrscheinlichkeit", "en": "Complement"},
                    "intuition": {"de": "Alles außer A.", "en": "Everything except A."},
                    "pro_tip": {"de": "Der Trick für 'mindestens eins': 1 − P(keins) ist fast immer einfacher.", "en": "The shortcut for 'at least one' problems: 1 − P(none) is almost always easier."},
                    "example": {"de": "Nicht 6 = 1 - (1/6) = 5/6", "en": "Not 6 = 1 - (1/6) = 5/6"}
                }
            ]
        },
        "col2": {
            "title": {"de": "Die Werkzeuge", "en": "The Tools"},
            "icon": "tool",
            "color": "#FF9500", # Apple Orange
            "items": [
                {
                    "latex": r"P(A \cup B) = P(A) + P(B) - P(A \cap B)",
                    "title": {"de": "Additionssatz", "en": "Addition Law"},
                    "intuition": {"de": "Addieren, aber Schnitt nicht doppelt zählen.", "en": "Add, but don't double count overlap."},
                    "pro_tip": {"de": "Wenn P(A) + P(B) > 1, MÜSSEN sich A und B überschneiden.", "en": "If P(A) + P(B) > 1, then A and B MUST overlap. Impossible to avoid intersection."},
                    "example": {"de": "Herz oder König? 13 + 4 - 1 (Herz-König)", "en": "Heart or King? 13 + 4 - 1 (King of Hearts)"}
                },
                {
                    "latex": r"P(A|B) = \frac{P(A \cap B)}{P(B)}",
                    "title": {"de": "Bedingte Wsk.", "en": "Conditional Prob."},
                    "intuition": {"de": "Zoom in die Welt B (neuer Nenner).", "en": "Zoom into world B (new denominator)."},
                    "pro_tip": {"de": "Der Nenner schrumpft! Du filterst das Universum. Denke: 'Gegeben dass ich schon in B bin...'", "en": "The denominator shrinks! You're filtering the universe. Think: 'Given I'm already in B...'"},
                    "example": {"de": "Von den Rauchern (B), wer hat Krebs (A)?", "en": "Of Smokers (B), who has cancer (A)?"}
                },
                {
                    "latex": r"P(A \cap B) = P(A) \cdot P(B)",
                    "title": {"de": "Unabhängigkeit", "en": "Independence"},
                    "intuition": {"de": "A ist B egal. Information ändert nichts.", "en": "A doesn't care about B. Info changes nothing."},
                    "pro_tip": {"de": "Selten im echten Leben. Wenn du dir IRGENDEINEN Zusammenhang vorstellen kannst, sind sie wahrscheinlich NICHT unabhängig.", "en": "Rare in real life. If you can imagine ANY mechanism linking A and B, they're probably NOT independent."},
                    "example": {"de": "Münze (Kopf) und Würfel (6).", "en": "Coin (Head) and Die (6)."}
                }
            ]
        },
        "col3": {
            "title": {"de": "Die Inferenz (Bayes)", "en": "The Inference (Bayes)"},
            "icon": "git-merge", # Flow icon
            "color": "#AF52DE", # Apple Purple
            "items": [
                {
                    "latex": r"P(B) = \sum P(B|A_i)P(A_i)",
                    "title": {"de": "Totale Wahrscheinlichkeit", "en": "Total Probability"},
                    "intuition": {"de": "Summe aller Pfade, die zu B führen.", "en": "Sum of all paths leading to B."},
                    "pro_tip": {"de": "Die 'Baumdiagramm'-Formel. Zerlege in Fälle, gewichte nach Wahrscheinlichkeit, summiere.", "en": "The 'tree diagram' formula. Split by cases, weight by their probability, add up."},
                    "example": {"de": "Defekt von M1 + Defekt von M2...", "en": "Defect from M1 + Defect from M2..."}
                },
                {
                    "latex": r"P(A|B) = \frac{P(B|A)P(A)}{P(B)}",
                    "title": {"de": "Satz von Bayes", "en": "Bayes' Theorem"},
                    "intuition": {"de": "Bedingung umkehren (Inferenz).", "en": "Flip the condition (Inference)."},
                    "pro_tip": {"de": "Ärzte irren hier oft. Positiver Test ≠ hohe Krankheitswahrscheinlichkeit, wenn die Krankheit selten ist (Base-Rate-Neglect).", "en": "Doctors get this wrong. A positive test ≠ high chance of disease if the disease is rare (base rate neglect)."},
                    "example": {"de": "Test positiv -> Krank?", "en": "Test positive -> Sick?"}
                },
                {
                    "latex": r"\text{Prior} \to \text{Posterior}",
                    "title": {"de": "Wissens-Update", "en": "Knowledge Update"},
                    "intuition": {"de": "Heute ist der Posterior von gestern.", "en": "Today is yesterday's posterior."},
                    "pro_tip": {"de": "Bayesianisches Lernen: Jede neue Evidenz aktualisiert deinen Glauben. Nie von Null anfangen.", "en": "Bayesian learning: each new piece of evidence updates your belief. Never start from scratch."},
                    "example": {"de": "Suche im Meer: Keine Fund -> Wsk sinkt.", "en": "Search at sea: No find -> Prob drops."}
                }
            ]
        }
    },
    
    # EXAM: LEVELS
    "exam": {
        "header": {"de": "The Final Exam", "en": "The Final Exam"},
        "desc": {"de": "Beweise deine statistische Intuition. 6 Level.", "en": "Prove your statistical intuition. 6 Levels."},
        "levels": [
            {"id": "l1", "tab": "Lvl 1", "title": {"de": "Level 1: Totale Wahrscheinlichkeit", "en": "Level 1: Total Probability"}},
            {"id": "l2", "tab": "Lvl 2", "title": {"de": "Level 2: Bayes Basic", "en": "Level 2: Bayes Basic"}},
            {"id": "l3", "tab": "Lvl 3", "title": {"de": "Level 3: Bayesian Search", "en": "Level 3: Bayesian Search"}},
            {"id": "l4", "tab": "Lvl 4", "title": {"de": "Level 4: Monty Hall", "en": "Level 4: Monty Hall"}},
            {"id": "l5", "tab": "Lvl 5", "title": {"de": "Level 5: Independence", "en": "Level 5: Independence"}},
            {"id": "l6", "tab": "Lvl 6", "title": {"de": "Level 6: Combinatorics", "en": "Level 6: Combinatorics"}}
        ]
    }
}

# --- HELPER: RENDER BENTO CARD ---
def render_bento_card(title, icon_name, color, items):
    """Renders a visual card for a specific knowledge category."""
    inject_equal_height_css()
    # We use a native container with a border as the base
    with st.container(border=True):
        # Header with Icon
        col_icon, col_title = st.columns([1, 5])
        with col_icon:
            st.markdown(f"<div style='color:{color}'>{render_icon(icon_name, size=24)}</div>", unsafe_allow_html=True)
        with col_title:
            st.markdown(f"<h4 style='margin:0; padding:0; color:{color}'>{title}</h4>", unsafe_allow_html=True)
        
        st.markdown(f"<hr style='margin: 8px 0; border-top: 2px solid {color}20;'>", unsafe_allow_html=True)
        
        # Items Loop
        for item in items:
            st.markdown(f'''
            <div style="margin-bottom: 16px;">
                <div style="font-weight: 600; font-size: 0.9em; margin-bottom: 4px;">{t(item['title'])}</div>
                <div style="margin-bottom: 8px;">{t(item['latex'])}</div>
                <div style="font-size: 0.85em; color: #444; margin-bottom: 2px; border-left: 2px solid {color}40; padding-left: 8px;">
                    <i>Intuition:</i> {t(item['intuition'])}
                </div>
                <div style="font-size: 0.8em; color: #666; margin-left: 10px;">
                    Example: {t(item['example'])}
                </div>
            </div>
            ''', unsafe_allow_html=True) # Direct markdown render for clearer control

            # We replace st.latex with the markdown latex for tighter integration above to avoid spacing issues,
            # but actually st.latex is safer for rendering. Let's revert to separate calls but with tight logic.
            # Actually, let's keep it simple: Title -> Latex -> Intuition/Ex.
            
            # Since I put latex in the markdown f-string above, I need to make sure I don't double render.
            # Wait, item['latex'] is a string. If I put it in markdown it needs $...$.
            # The previous code used st.latex(item['latex']).
            
            # Let's clean up the loop to be robust:
            # st.markdown(f"**{t(item['title'])}**")
            # st.latex(item['latex'])
            # st.caption(...)

# --- HELPER: RENDER SWIMLANE (VERTICAL STACK) ---
def render_swimlane(title, icon_name, items):
    """Renders a section with each item as a full-width horizontal card (formula left, explanation right)."""
    
    # 1. Section Header
    st.markdown(f"""
    <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 16px; margin-top: 32px;">
        <div style="display:flex; align-items:center; color: #111;">{render_icon(icon_name, size=28)}</div>
        <h3 style="margin:0; padding:0; color: #111; font-weight: 700;">{title}</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # 2. Unified Category Container
    with st.container(border=True):
        for i, item in enumerate(items):
            col_formula, col_explain = st.columns([1.2, 1], gap="large")
            
            with col_formula:
                st.markdown(f"**{t(item['title'])}**")
                st.latex(item['latex'])
            
            with col_explain:
                st.markdown(f"""
<div style="font-size: 0.95rem; color: #333; margin-bottom: 8px; display: flex; align-items: start; gap: 8px;">
    <span style="color: #666; margin-top: 2px;">{render_icon('lightbulb', size=16)}</span>
    <span>{t(item['intuition'])}</span>
</div>
<div style="font-size: 0.85rem; color: #666; padding-left: 26px; font-style: italic; margin-bottom: 12px;">
    Ex: {t(item['example'])}
</div>
<div style="background: #f4f4f5; border-left: 3px solid #71717a; padding: 8px 12px; border-radius: 6px; font-size: 0.85rem; color: #3f3f46;">
    <strong>Pro Tip:</strong> {t(item.get('pro_tip', {'de': '', 'en': ''}))}
</div>
                """, unsafe_allow_html=True)
            
            # Add separator between items (but not after the last one)
            if i < len(items) - 1:
                st.markdown("<hr style='margin: 24px 0; border: 0; border-top: 1.5px solid #f3f4f6;'>", unsafe_allow_html=True)
        
        # Bottom Margin Mandate: Ensure last Pro Tip doesn't collide with border
        st.markdown("<div style='margin-bottom: 12px;'></div>", unsafe_allow_html=True)

# --- HELPER: RENDER EXAM LEVEL ---
def render_level(lvl, model):
    """Secondary helper to render a specific exam level."""
    from utils.quiz_helper import shuffle_options
    
    st.markdown(f"**{t(lvl['title'])}**")
    
    # Fetch from Central
    q_data = get_question("1.10", lvl["id"])
    if not q_data:
        st.error(f"Question {lvl['id']} not found.")
        return

    # Translate bilingual options
    # In Central Repo 1.10, options are list of strings for l1, l3, l6...
    # BUT for l2, 1.10 uses list of DICTS?
    # Let's check l2 in Step 2856.
    # l2 options: [{"de": "20%", "en": "20%"}, ...]
    # l1 options: ["1/8", "3/8", ...]
    # So we need to handle both cases.
    
    raw_opts = q_data["options"]
    translated_opts = []
    for o in raw_opts:
        if isinstance(o, dict):
            translated_opts.append(t(o))
        else:
            translated_opts.append(o)

    correct_idx = q_data["correct_idx"]
    
    # Shuffle with stable seed based on level ID (deterministic per question)
    seed = hash(lvl['id']) % 10000  # Stable seed
    shuffled_opts, new_correct_idx = shuffle_options(translated_opts, correct_idx, seed)
    
    render_mcq(
        key_suffix=f"exam_{lvl['id']}",
        question_text=t(q_data["question"]),
        options=shuffled_opts,
        correct_idx=new_correct_idx,
        solution_text_dict=q_data["solution"],
        success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
        error_msg_dict={"de": "Noch nicht ganz...", "en": "Not quite..."},
        # hint_text_dict=q_data.get("hint", None), # Central question might not have explicit hint field matching 'err'
        # The 'err' field in original file was a Hint/Error message.
        # In central file, some have 'err' or just solution?
        # 1.10 l1 has 'err'...? No, Step 2856 shows only solution.
        # So we lose the specific error hint?
        # Unless I add it to central file.
        # But I am not asked to modify central file anymore.
        # I'll omit hint_text_dict if not present.
        client=model,
        ai_context=f"Final Exam Level: {t(lvl['title'])}",
        course_id="vwl",
        topic_id="1",
        subtopic_id="1.10",
        question_id=f"1_10_{lvl['id']}"
    )

# ==============================================================================
# 3. MAIN RENDERER
# ==============================================================================
def render_subtopic_1_10(model):
    """1.10 Summary & Exam - The Horizontal Swimlane Design"""
    
    st.header(t(content_1_10["title"]))
    st.caption(t(content_1_10["intro"]))
    st.markdown("---")

    # --- CSS: EQUAL HEIGHT FOR CARDS WITHIN ROWS ---
    # We still need the equal height logic for the items *within* each swimlane row
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
    
    /* Ensure internal content of the bordered box also grows */
    div[data-testid="stVerticalBlockBorderWrapper"] > div {
        flex: 1 !important;
        justify_content: space-between !important; /* Distribute content vertically */
    }

    h4 { font-weight: 600 !important; }
    </style>
    """, unsafe_allow_html=True)

    # 1. SWIMLANE 1: BASICS
    d = content_1_10["cheat_sheet"]["col1"]
    render_swimlane(t(d["title"]), d["icon"], d["items"])
    
    # 2. SWIMLANE 2: TOOLS
    d = content_1_10["cheat_sheet"]["col2"]
    render_swimlane(t(d["title"]), d["icon"], d["items"])
    
    # 3. SWIMLANE 3: INFERENCE
    d = content_1_10["cheat_sheet"]["col3"]
    render_swimlane(t(d["title"]), d["icon"], d["items"])

    st.markdown("<br><br>", unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # 2. THE EXAM (Tabbed Interface)
    st.markdown(f"### {t(content_1_10['exam']['header'])}")
    st.caption(t(content_1_10["exam"]["desc"]))
    
    # Generate tabs from level data
    levels = content_1_10["exam"]["levels"]
    tab_labels = [l["tab"] for l in levels]
    
    # Progress Indicators for Tabs
    tab_css = render_tab_progress_css(
        [l["id"] for l in levels], 
        key_prefix="1_10", 
        topic_id="1", 
        subtopic_id="1.10"
    )
    st.markdown(tab_css, unsafe_allow_html=True)
    
    # Render Tabs
    tabs = st.tabs(tab_labels)
    
    for i, tab in enumerate(tabs):
        with tab:
            with st.container(border=True):
                render_level(levels[i], model)

    # 3. GLOBAL SUBMIT
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Optional Celebration Logic
    if st.button(t({"de": "Prüfung abschließen", "en": "Finish Exam"}), type="primary"):
        st.balloons()
        st.success(t({"de": "Modul 1 Abgeschlossen! Herzlichen Glückwunsch.", "en": "Module 1 Completed! Congratulations."}))
