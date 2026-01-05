# Topic 5.1: Joint Distribution and Marginal Distributions
# EMERGENCY FIX - Matching Topic 4.x patterns exactly
import streamlit as st
from views.styles import inject_equal_height_css
from utils.localization import t
from utils.quiz_helper import render_mcq
from data.exam_questions import get_question

# ==========================================
# CONTENT DICTIONARY
# ==========================================
content_5_1 = {
    "title": {"de": "5.1 Gemeinsame Verteilung und Randverteilungen", "en": "5.1 Joint Distribution and Marginal Distributions"},
    "subtitle": {
        "de": "Wenn zwei Zufallsvariablen zusammen auftreten",
        "en": "When Two Random Variables Appear Together"
    },
    
    # --- FRAG DICH (Decision Guide) ---
    "frag_dich": {
        "header": {"de": "Frag dich: Welche Verteilung brauchst du?", "en": "Ask yourself: Which distribution do you need?"},
        "questions": [
            {"de": "Geht es um <strong>EINE Variable</strong>, andere ignoriert?", "en": "Is it about <strong>ONE variable</strong>, ignoring the other?"},
            {"de": "Brauchst du eine <strong>SPEZIFISCHE (x,y) Kombination</strong>?", "en": "Do you need a <strong>SPECIFIC (x,y) combination</strong>?"},
            {"de": "Musst du eine Zeile/Spalte <strong>SUMMIEREN</strong>?", "en": "Do you need to <strong>SUM</strong> a row/column?"}
        ],
        "conclusion": {"de": "Zeile summieren → f_X | Spalte summieren → f_Y | Zelle → f(x,y)", "en": "Sum row → f_X | Sum column → f_Y | Cell → f(x,y)"}
    },
    
    "exam_essentials": {
        "trap": {
            "de": "Richtung verwechselt: Für $f_X$ summierst du ÜBER alle $Y$ (Zeile). Für $f_Y$ summierst du ÜBER alle $X$ (Spalte).",
            "en": "Direction confused: For $f_X$ you sum ACROSS all $Y$ (row). For $f_Y$ you sum ACROSS all $X$ (column)."
        },
        "tips": [
            {
                "tip": {"de": "Summe aller Wahrscheinlichkeiten = 1", "en": "All probabilities sum to 1"},
                "why": {"de": "Schneller Sanity-Check!", "en": "Quick sanity check!"}
            },
            {
                "tip": {"de": "Gemeinsam → Marginal: JA. Umgekehrt: NEIN", "en": "Joint → Marginal: YES. Reverse: NO"},
                "why": {"de": "Ohne Unabhängigkeit geht's nicht rückwärts.", "en": "Without independence, you can't go backwards."}
            }
        ]
    }
}


def render_subtopic_5_1(model):
    """5.1 Gemeinsame Verteilung und Randverteilungen - EMERGENCY FIX"""
    inject_equal_height_css()
    
    # --- HEADER ---
    st.header(t(content_5_1["title"]))
    st.caption(t(content_5_1["subtitle"]))
    st.markdown("---")
    
    # =========================================
    # SECTION 1: INTUITION - TWO EQUAL HEIGHT CONTAINERS
    # =========================================
    st.markdown(f"### {t({'de': 'Die Intuition', 'en': 'The Intuition'})}")
    
    # Story-based scenario (Stupid Person Rule)
    st.markdown(f"""
<div style="background: #f4f4f5; border-left: 4px solid #a1a1aa; 
            padding: 12px 16px; border-radius: 8px; color: #3f3f46; margin-bottom: 16px;">
<strong>{t({'de': 'Die Geschichte', 'en': 'The Story'})}:</strong><br><br>
{t({'de': 'Du arbeitest in einem Café und erfasst Bestellungen in einer Tabelle:', 
    'en': 'You work at a coffee shop and track orders in a table:'})}<br><br>
• <strong>{t({'de': 'Zeilen', 'en': 'Rows'})}</strong> = {t({'de': 'Kaffee-Grösse (Klein, Mittel, Gross)', 'en': 'Coffee size (Small, Medium, Large)'})}<br>
• <strong>{t({'de': 'Spalten', 'en': 'Columns'})}</strong> = {t({'de': 'Milch-Art (Normal, Hafermilch, Soja)', 'en': 'Milk type (Regular, Oat, Soy)'})}<br>
• <strong>{t({'de': 'Zellen', 'en': 'Cells'})}</strong> = {t({'de': 'Wie viel % der Kunden diese Kombination bestellen', 'en': 'What % of customers order this combination'})}<br><br>
{t({'de': 'Dein Chef stellt dir zwei Arten von Fragen...', 'en': 'Your boss asks you two types of questions...'})}
</div>
""", unsafe_allow_html=True)
    
    # EQUAL HEIGHT CSS for parallel comparison alignment
    st.markdown("""
<style>
[data-testid="stHorizontalBlock"] { align-items: stretch !important; }
[data-testid="column"], [data-testid="stColumn"] { display: flex !important; flex-direction: column !important; }
[data-testid="column"] > div, [data-testid="stColumn"] > div { flex: 1 !important; display: flex !important; flex-direction: column !important; height: 100% !important; }
div[data-testid="stVerticalBlock"], div[data-testid="stVerticalBlockBorderWrapper"] { flex: 1 !important; display: flex !important; flex-direction: column !important; }
</style>
""", unsafe_allow_html=True)
    
    # FORMULA BOXES - Parallel structure for row alignment
    col1, col2 = st.columns(2, gap="medium")
    
    with col1:
        with st.container(border=True):
            st.markdown(f"**{t({'de': 'GEMEINSAM (Joint)', 'en': 'JOINT'})}**")
            # Add phantom subscript to match height of marginal formula
            st.latex(r"f(x,y) = P(X=x \cap Y=y) \vphantom{\sum_y}")
            st.markdown(f"**{t({'de': 'Chef fragt', 'en': 'Boss asks'})}:**")
            st.markdown(t({
                'de': '"Wie viel % bestellen MITTEL + HAFERMILCH?"',
                'en': '"What % order MEDIUM + OAT MILK?"'
            }))
            st.markdown(f"**{t({'de': 'Antwort', 'en': 'Answer'})}:**")
            st.markdown(t({
                'de': 'Finde die EINE Zelle (Zeile + Spalte)',
                'en': 'Find the ONE cell (Row + Column)'
            }))
    
    with col2:
        with st.container(border=True):
            st.markdown(f"**{t({'de': 'MARGINAL (Rand)', 'en': 'MARGINAL'})}**")
            st.latex(r"f_X(x) = \sum_y f(x,y)")
            st.markdown(f"**{t({'de': 'Chef fragt', 'en': 'Boss asks'})}:**")
            st.markdown(t({
                'de': '"Wie viel % bestellen MITTEL?" (egal welche Milch)',
                'en': '"What % order MEDIUM?" (any milk)'
            }))
            st.markdown(f"**{t({'de': 'Antwort', 'en': 'Answer'})}:**")
            st.markdown(t({
                'de': 'Addiere ALLE Zellen der Zeile',
                'en': 'Add ALL cells in the row'
            }))
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # VISUAL COMPARISON - Simple st.image with captions (no containers)
    st.markdown(f"**{t({'de': 'Visueller Vergleich', 'en': 'Visual Comparison'})}:**")
    
    img_col1, img_col2 = st.columns(2, gap="medium")
    with img_col1:
        st.image("assets/topic_5/joint_visual.png", use_container_width=True, caption=t({'de': 'Joint: EINE Zelle', 'en': 'Joint: ONE cell'}))
    with img_col2:
        st.image("assets/topic_5/marginal_visual.png", use_container_width=True, caption=t({'de': 'Marginal: Zeile summieren', 'en': 'Marginal: Sum the row'}))
    
    # =========================================
    # SECTION 2: FRAG DICH - Using Blue Utility
    # =========================================
    from utils.ask_yourself import render_ask_yourself
    render_ask_yourself(
        header=content_5_1['frag_dich']['header'],
        questions=content_5_1['frag_dich']['questions'],
        conclusion=content_5_1['frag_dich']['conclusion']
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # =========================================
    # SECTION 3: INTERACTIVE MISSION (Simple - Stupid Person Rule)
    # =========================================
    st.markdown(f"### {t({'de': 'Übung: Randverteilung berechnen', 'en': 'Exercise: Calculate Marginal'})}")
    
    @st.fragment
    def simple_mission():
        # State
        if "marginal_answer" not in st.session_state:
            st.session_state.marginal_answer = None
        
        with st.container(border=True):
            # Context - why this matters (normal font, not grey caption)
            why_de = 'Stell dir vor: Du hast Umfragedaten mit Alter (X) und Einkommen (Y). Dein Chef fragt: "Wie viel Prozent sind 25-34 Jahre alt?" — Er will NICHT wissen, welches Einkommen sie haben. Das ist eine Randverteilung: Du "vergisst" Y und konzentrierst dich nur auf X.'
            why_en = "Imagine: You have survey data with Age (X) and Income (Y). Your boss asks: 'What percentage are 25-34 years old?' — They don't care about income. That's a marginal: You 'forget' Y and focus only on X."
            
            st.markdown(t({'de': why_de, 'en': why_en}))
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            # Task - bold header with LaTeX formula
            st.markdown(f"**{t({'de': 'Aufgabe', 'en': 'Task'})}:**")
            st.latex(r"f_X(1) = ?")
            st.markdown(t({'de': 'Die Wahrscheinlichkeit, dass X=1 ist (egal welches Y).', 
                'en': 'The probability that X=1 (regardless of Y).'}))
            
            st.markdown("---")
            
            # Hint - just bold text, no grey box
            st.markdown(f"**{t({'de': 'Hinweis', 'en': 'Hint'})}:** {t({'de': 'Addiere alle Werte in der roten Zeile.', 'en': 'Add all values in the red row.'})}")
            
            # Centered table
            st.markdown("""
<div style="display: flex; justify-content: center; margin: 16px 0;">
<table style="border-collapse: collapse; text-align: center; font-size: 1rem;">
<tr style="background: #e5e7eb;">
    <th style="padding: 10px 20px; border: 1px solid #d1d5db;"></th>
    <th style="padding: 10px 20px; border: 1px solid #d1d5db;">Y=1</th>
    <th style="padding: 10px 20px; border: 1px solid #d1d5db;">Y=2</th>
    <th style="padding: 10px 20px; border: 1px solid #d1d5db;">Y=3</th>
</tr>
<tr style="background: rgba(255, 75, 75, 0.15);">
    <td style="padding: 10px 20px; border: 1px solid #d1d5db; font-weight: 600; color: #FF4B4B;">X=1</td>
    <td style="padding: 10px 20px; border: 1px solid #d1d5db; color: #FF4B4B; font-weight: 500;">0.10</td>
    <td style="padding: 10px 20px; border: 1px solid #d1d5db; color: #FF4B4B; font-weight: 500;">0.15</td>
    <td style="padding: 10px 20px; border: 1px solid #d1d5db; color: #FF4B4B; font-weight: 500;">0.05</td>
</tr>
<tr>
    <td style="padding: 10px 20px; border: 1px solid #d1d5db; font-weight: 600; background: #f4f4f5;">X=2</td>
    <td style="padding: 10px 20px; border: 1px solid #d1d5db;">0.20</td>
    <td style="padding: 10px 20px; border: 1px solid #d1d5db;">0.10</td>
    <td style="padding: 10px 20px; border: 1px solid #d1d5db;">0.10</td>
</tr>
<tr>
    <td style="padding: 10px 20px; border: 1px solid #d1d5db; font-weight: 600; background: #f4f4f5;">X=3</td>
    <td style="padding: 10px 20px; border: 1px solid #d1d5db;">0.05</td>
    <td style="padding: 10px 20px; border: 1px solid #d1d5db;">0.15</td>
    <td style="padding: 10px 20px; border: 1px solid #d1d5db;">0.10</td>
</tr>
</table>
</div>
""", unsafe_allow_html=True)
            
            # Step-by-step prompts
            st.markdown(f"**{t({'de': 'Schritt 1', 'en': 'Step 1'})}:** {t({'de': 'Finde die Zeile X=1 (rot markiert)', 'en': 'Find row X=1 (marked red)'})}")
            st.markdown(f"**{t({'de': 'Schritt 2', 'en': 'Step 2'})}:** {t({'de': 'Addiere alle Werte: 0.10 + 0.15 + 0.05 = ?', 'en': 'Add all values: 0.10 + 0.15 + 0.05 = ?'})}")
            
            st.markdown("---")
            
            # Question with LaTeX
            st.markdown(f"**{t({'de': 'Deine Antwort', 'en': 'Your Answer'})}:**")
            st.latex(r"f_X(1) = ?")
            
            answer = st.radio(
                t({"de": "Wähle:", "en": "Choose:"}),
                ["0.20", "0.25", "0.30", "0.35"],
                key="marginal_radio",
                index=None,
                horizontal=True
            )
            
            if answer:
                if answer == "0.30":
                    st.success(t({"de": "Richtig! f_X(1) = 0.10 + 0.15 + 0.05 = 0.30", "en": "Correct! f_X(1) = 0.10 + 0.15 + 0.05 = 0.30"}))
                    # Track progress
                    from utils.progress_tracker import track_question_answer
                    if user := st.session_state.get("user"):
                        track_question_answer(user["localId"], "vwl", "5", "5.1", "marginal_mission", True)
                else:
                    st.error(t({"de": "Summiere die rote Zeile: 0.10 + 0.15 + 0.05 = 0.30", "en": "Sum the red row: 0.10 + 0.15 + 0.05 = 0.30"}))
    
    simple_mission()
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # =========================================
    # SECTION 4: EXAM ESSENTIALS (Utility - matches reference)
    # =========================================
    from utils.exam_essentials import render_exam_essentials
    render_exam_essentials(
        trap=content_5_1['exam_essentials']['trap'],
        tips=content_5_1['exam_essentials']['tips']
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # =========================================
    # SECTION 5: PRÜFUNGSTRAINING (MCQs)
    # =========================================
    st.markdown(f"### {t({'de': 'Prüfungstraining', 'en': 'Exam Practice'})}")
    
    q1 = get_question("5.1", "test3_q4")
    if q1:
        with st.container(border=True):
            st.caption(q1.get("source", ""))
            opts = q1.get("options", [])
            option_labels = [t(o) if isinstance(o, dict) else o for o in opts]
            
            render_mcq(
                key_suffix="5_1_sum",
                question_text=t(q1["question"]),
                options=option_labels,
                correct_idx=q1["correct_idx"],
                solution_text_dict=q1["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
                client=model,
                ai_context="Joint distributions",
                course_id="vwl",
                topic_id="5",
                subtopic_id="5.1",
                question_id="5_1_sum"
            )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    q2 = get_question("5.1", "uebung3_mc5")
    if q2:
        with st.container(border=True):
            st.caption(q2.get("source", ""))
            opts = q2.get("options", [])
            option_labels = [t(o) if isinstance(o, dict) else o for o in opts]
            
            render_mcq(
                key_suffix="5_1_linear",
                question_text=t(q2["question"]),
                options=option_labels,
                correct_idx=q2["correct_idx"],
                solution_text_dict=q2["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
                client=model,
                ai_context="Properties of expectation",
                course_id="vwl",
                topic_id="5",
                subtopic_id="5.1",
                question_id="5_1_linear"
            )
