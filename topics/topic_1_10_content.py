import streamlit as st
from views.styles import render_icon
from utils.localization import t
from utils.quiz_helper import render_mcq, render_tab_progress_css

# ==============================================================================
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
                    "example": {"de": "Würfel 6: 1 Günstige / 6 Mögliche", "en": "Roll 6: 1 Favorable / 6 Possible"}
                },
                {
                    "latex": r"P(S) = 1",
                    "title": {"de": "Normierung", "en": "Normalization"},
                    "intuition": {"de": "Irgendetwas passiert immer (100%).", "en": "Something happens always (100%)."},
                    "example": {"de": "Sonne + Regen + ... = 1", "en": "Sun + Rain + ... = 1"}
                },
                {
                    "latex": r"P(A^c) = 1 - P(A)",
                    "title": {"de": "Gegenwahrscheinlichkeit", "en": "Complement"},
                    "intuition": {"de": "Alles außer A.", "en": "Everything except A."},
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
                    "example": {"de": "Herz oder König? 13 + 4 - 1 (Herz-König)", "en": "Heart or King? 13 + 4 - 1 (King of Hearts)"}
                },
                {
                    "latex": r"P(A|B) = \frac{P(A \cap B)}{P(B)}",
                    "title": {"de": "Bedingte Wsk.", "en": "Conditional Prob."},
                    "intuition": {"de": "Zoom in die Welt B (neuer Nenner).", "en": "Zoom into world B (new denominator)."},
                    "example": {"de": "Von den Rauchern (B), wer hat Krebs (A)?", "en": "Of Smokers (B), who has cancer (A)?"}
                },
                {
                    "latex": r"P(A \cap B) = P(A) \cdot P(B)",
                    "title": {"de": "Unabhängigkeit", "en": "Independence"},
                    "intuition": {"de": "A ist B egal. Information ändert nichts.", "en": "A doesn't care about B. Info changes nothing."},
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
                    "example": {"de": "Defekt von M1 + Defekt von M2...", "en": "Defect from M1 + Defect from M2..."}
                },
                {
                    "latex": r"P(A|B) = \frac{P(B|A)P(A)}{P(B)}",
                    "title": {"de": "Satz von Bayes", "en": "Bayes' Theorem"},
                    "intuition": {"de": "Bedingung umkehren (Inferenz).", "en": "Flip the condition (Inference)."},
                    "example": {"de": "Test positiv -> Krank?", "en": "Test positive -> Sick?"}
                },
                {
                    "latex": r"\text{Prior} \to \text{Posterior}",
                    "title": {"de": "Wissens-Update", "en": "Knowledge Update"},
                    "intuition": {"de": "Heute ist der Posterior von gestern.", "en": "Today is yesterday's posterior."},
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
            {
                "id": "l1", 
                "tab": "Lvl 1",
                "title": {"de": "Level 1: Totale Wahrscheinlichkeit", "en": "Level 1: Total Probability"},
                "q": {"de": "Die Wahrscheinlichkeit für Sonne beträgt 60%. Wenn die Sonne scheint, ist die Laune zu 90% gut. Wenn es regnet (keine Sonne), ist die Laune nur zu 30% gut. Wie hoch ist die Wahrscheinlichkeit für gute Laune insgesamt?",
                      "en": "The probability of sun is 60%. If the sun shines, the mood is 90% good. If it rains (no sun), the mood is only 30% good. What is the total probability of a good mood?"},
                "opts": ["60%", "66%", "54%", "90%"],
                "correct": 1,
                "sol": {"de": "$0.9\\cdot0.6 + 0.3\\cdot0.4 = 0.54 + 0.12 = 0.66$", "en": "$0.9\\cdot0.6 + 0.3\\cdot0.4 = 0.54 + 0.12 = 0.66$"},
                "err": {"de": "Hast du bedacht, dass es auch bei Regen gute Laune geben kann? (Gegenwahrscheinlichkeit von Sonne!)", "en": "Did you consider that mood can be good even when it rains? (Complement of Sun!)"}
            },
            {
                "id": "l2", 
                "tab": "Lvl 2",
                "title": {"de": "Level 2: Bayes Basic", "en": "Level 2: Bayes Basic"},
                "q": {"de": "Maschine M1 produziert 20% aller Teile mit einer Fehlerrate von 5%. Maschine M2 produziert den Rest (80%) mit nur 1% Fehlern. Ein zufällig geprüftes Teil ist defekt. Wie hoch ist die Wahrscheinlichkeit, dass es von Maschine M1 stammt?", 
                      "en": "Machine M1 produces 20% of all parts with a 5% error rate. Machine M2 produces the rest (80%) with only 1% errors. A randomly checked part is defective. What is the probability that it came from Machine M1?"},
                "opts": ["20%", "55.5%", "80%", "5%"],
                "correct": 1,
                "sol": {"de": "P(M1|D) = (0.05*0.2) / 0.018 ≈ 55.5%. Beachte: Obwohl M1 viel weniger produziert, ist sie für die Mehrheit der Fehler verantwortlich!", "en": "P(M1|D) = (0.05*0.2) / 0.018 ≈ 55.5%. Note: Although M1 produces much less, it is responsible for the majority of errors!"},
                "err": {"de": "Nutze Bayes: Prior (Marktanteil) mal Likelihood (Fehlerrate). M1 ist zwar klein, aber unzuverlässig.", "en": "Use Bayes: Prior (Share) times Likelihood (Error Rate). M1 is small but unreliable."}
            },
            {
                "id": "l3", 
                "tab": "Lvl 3",
                "title": {"de": "Level 3: Bayesian Search", "en": "Level 3: Bayesian Search"},
                "q": {"de": "Ein U-Boot versteckt sich in Zone A (40%), B (35%) oder C (25%). Wir suchen Zone A ab, aber finden nichts (obwohl unsere Sensoren das Boot zu 80% finden würden, wenn es dort wäre). Wie hoch ist nun die Wahrscheinlichkeit, dass das Boot doch in Zone A ist?",
                      "en": "A submarine is hiding in Zone A (40%), B (35%), or C (25%). We search Zone A but find nothing (even though our sensors detect it 80% of the time if present). What is the new probability that the boat is actually in Zone A?"},
                "opts": ["8%", "11.8%", "40%", "32%"],
                "correct": 1,
                "sol": {"de": "P(A|¬Fund) = (0.2*0.4) / (0.2*0.4 + 1*0.35 + 1*0.25) ≈ 11.8%", "en": "P(A|¬Found) = (0.2*0.4) / (0.2*0.4 + 1*0.35 + 1*0.25) ≈ 11.8%"},
                "err": {"de": "Der Zähler ist P(in A) * P(nicht gefunden | in A). Der Nenner ist die Summe aller Möglichkeiten, nichts zu finden.", "en": "The numerator is P(in A) * P(not found | in A). The denominator is the sum of all ways to find nothing."}
            },
            {
                "id": "l4", 
                "tab": "Lvl 4",
                "title": {"de": "Level 4: Monty Hall", "en": "Level 4: Monty Hall"},
                "q": {"de": "Du stehst vor 3 Türen. Hinter einer ist ein Gewinn. Du wählst Tür 1. Der Moderator, der weiß, wo der Gewinn ist, öffnet Tür 3 (eine Niete). Er bietet dir an, zu Tür 2 zu wechseln. Solltest du das tun?",
                      "en": "You face 3 doors. Behind one is a prize. You pick Door 1. The host, who knows where the prize is, opens Door 3 (empty). He offers you to switch to Door 2. Should you switch?"},
                "opts": ["33% (Egal)", "66% (Ja, Wechseln)", "50% (Egal)", "25% (Nein, Bleiben)"],
                "correct": 1,
                "sol": {"de": "Ja! Deine Tür 1 hat eine Chance von 1/3. Die anderen beiden Türen haben zusammen 2/3. Da Tür 3 nun offen ist, konzentrieren sich die gesamten 2/3 auf Tür 2.",
                        "en": "Yes! Your Door 1 has a 1/3 chance. The defined 'Other' group has 2/3. Since Door 3 is revealed as empty, the entire 2/3 probability collapses onto Door 2."},
                "err": {"de": "Vergiss nicht: Der Moderator wählt nicht zufällig. Er gibt dir Informationen über die 'Andere' Gruppe.", "en": "Don't forget: The host doesn't choose randomly. He gives you info about the 'Other' group."}
            },
            {
                "id": "l5", 
                "tab": "Lvl 5",
                "title": {"de": "Level 5: Independence", "en": "Level 5: Independence"},
                "q": {"de": "Person A wirft eine Münze und erhält 'Kopf'. Person B wirft eine eigene Münze und erhält 'Zahl'. Beeinflussen sich diese Ereignisse gegenseitig (stochastische Unabhängigkeit)?",
                      "en": "Person A flips a coin and gets 'Heads'. Person B flips their own coin and gets 'Tails'. Do these events match the criteria for stochastic independence?"},
                "opts": ["Nein", "Ja", "Nur bei fairen Münzen", "Nicht entscheidbar"],
                "correct": 1,
                "sol": {"de": "Ja. Das physikalische Ergebnis von Wurf A hat keinen Einfluss auf die Wahrscheinlichkeiten von Wurf B. P(A und B) = P(A)*P(B).", "en": "Yes. The physical result of Flip A has no impact on the probabilities of Flip B. P(A and B) = P(A)*P(B)."},
                "err": {"de": "Überlege kausal: Ändert Wissen über A irgendetwas an deiner Vorhersage für B?", "en": "Think causally: Does knowing A change your prediction for B in any way?"}
            },
            {
                "id": "l6", 
                "tab": "Lvl 6",
                "title": {"de": "Level 6: Combinatorics", "en": "Level 6: Combinatorics"},
                "q": {"de": "In einer Urne sind 3 rote und 2 blaue Kugeln. Du ziehst eine Kugel und legst sie NICHT zurück. Die erste Kugel war rot. Wie hoch ist die Wahrscheinlichkeit, dass die zweite Kugel ebenfalls rot ist?",
                      "en": "An urn contains 3 red and 2 blue balls. You draw one ball and do NOT replace it. The first ball was red. What is the probability that the second ball is also red?"},
                "opts": ["3/5", "2/4 (50%)", "3/4", "2/5"],
                "correct": 1,
                "sol": {"de": "Nach dem ersten Zug (Rot) verbleiben 4 Kugeln in der Urne: 2 Rote und 2 Blaue. Die Chance ist also 2 von 4.", "en": "After the first draw (Red), 4 balls remain: 2 Red and 2 Blue. The chance is therefore 2 out of 4."},
                "err": {"de": "Das 'Gedächtnis' der Urne zählt. Die Gesamtzahl und die roten Kugeln haben sich verringert.", "en": "The 'memory' of the urn matters. Both the total count and the red count decreased."}
            }
        ]
    }
}

# --- HELPER: RENDER BENTO CARD ---
def render_bento_card(title, icon_name, color, items):
    """Renders a visual card for a specific knowledge category."""
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
    
    # 2. Render Each Item as a Full-Width Card
    for item in items:
        with st.container(border=True):
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
<div style="font-size: 0.85rem; color: #666; padding-left: 26px; font-style: italic;">
    Ex: {t(item['example'])}
</div>
                """, unsafe_allow_html=True)

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
