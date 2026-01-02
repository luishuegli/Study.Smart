# Topic 5.1: Joint Distribution and Marginal Distributions
# FIXED VERSION - Addressing all user feedback
import streamlit as st
from views.styles import inject_equal_height_css
from utils.localization import t
from utils.quiz_helper import render_mcq
from data.exam_questions import get_question

# ==========================================
# CONTENT DICTIONARY - FULLY BILINGUAL
# ==========================================
content_5_1 = {
    "title": {"de": "5.1 Gemeinsame Verteilung und Randverteilungen", "en": "5.1 Joint Distribution and Marginal Distributions"},
    "subtitle": {
        "de": "Wenn zwei Zufallsvariablen zusammen auftreten",
        "en": "When Two Random Variables Appear Together"
    },
    
    # --- INTUITION HOOK (Structured for Visual Layout) ---
    "intuition": {
        "header": {"de": "Die Intuition", "en": "The Intuition"},
        "intro": {
            "de": "Stell dir eine **Excel-Tabelle** vor — jede Zelle ist eine Wahrscheinlichkeit.",
            "en": "Think of an **Excel spreadsheet** — each cell is a probability."
        },
        "joint": {
            "title": {"de": "GEMEINSAM", "en": "JOINT"},
            "definition": {"de": "= EINE bestimmte Zelle", "en": "= ONE specific cell"},
            "question": {"de": "Was ist P(X=1 UND Y=2)?", "en": "What's P(X=1 AND Y=2)?"}
        },
        "marginal": {
            "title": {"de": "MARGINAL", "en": "MARGINAL"},
            "definition": {"de": "= Zeilen-/Spaltensumme", "en": "= Row/Column TOTAL"},
            "question": {"de": "Was ist P(X=1), egal was Y?", "en": "What's P(X=1), regardless of Y?"}
        },
        "insight": {
            "de": "Marginal 'vergisst' — du summierst Y weg und verlierst dessen Info.",
            "en": "Marginal 'forgets' — you sum away Y and lose its info."
        }
    },
    
    # --- FRAG DICH (Decision Guide) with Context ---
    "frag_dich": {
        "header": {"de": "Frag dich", "en": "Ask Yourself"},
        "intro": {"de": "Erkennst du die richtige Verteilung?", "en": "Can you identify the right distribution?"},
        "questions": [
            {
                "q": {"de": "Geht es um EINE Variable, wobei die andere ignoriert wird?", "en": "Is it about ONE variable, ignoring the other?"},
                "context": {
                    "de": "Beispiel: 'Wie wahrscheinlich ist es, dass ein Student BWL studiert?' — Du fragst nur nach dem Studienfach, das Alter ist egal.",
                    "en": "Example: 'How likely is it that a student studies Business?' — You only ask about the major, the age doesn't matter."
                },
                "a": {"de": "Randverteilung", "en": "Marginal"},
                "formula": r"f_X(x) = \sum_y f(x,y)"
            },
            {
                "q": {"de": "Geht es um eine SPEZIFISCHE (x,y) Kombination?", "en": "Is it about a SPECIFIC (x,y) combination?"},
                "context": {
                    "de": "Beispiel: 'Wie wahrscheinlich ist es, dass jemand 20 Jahre alt ist UND BWL studiert?' — Du willst genau diese eine Kombination.",
                    "en": "Example: 'How likely is someone to be 20 years old AND study Business?' — You want exactly this one combination."
                },
                "a": {"de": "Gemeinsame Verteilung", "en": "Joint distribution"},
                "formula": r"f(x, y) = P(X=x \cap Y=y)"
            },
            {
                "q": {"de": "Musst du eine Zeile oder Spalte SUMMIEREN?", "en": "Do you need to SUM a row or column?"},
                "context": {
                    "de": "Du hast eine Tabelle und sollst die Randverteilung berechnen? Addiere alle Werte einer Zeile (für f_X) oder Spalte (für f_Y).",
                    "en": "You have a table and need to compute the marginal? Add up all values in a row (for f_X) or column (for f_Y)."
                },
                "a": {"de": "Marginal berechnen", "en": "Computing marginal"},
                "formula": r"f_X(x) = \sum_j f(x, y_j)"
            },
            {
                "q": {"de": "Ist der Definitionsbereich ein RECHTECK?", "en": "Is the support region a RECTANGLE?"},
                "context": {
                    "de": "Wenn X und Y unabhängig sind, kann man die gemeinsame Verteilung als Produkt schreiben. Ein rechteckiger Bereich ist ein Hinweis!",
                    "en": "If X and Y are independent, you can write the joint as a product. A rectangular region is a hint!"
                },
                "a": {"de": "Könnte unabhängig sein!", "en": "Might be independent!"},
                "formula": r"f(x,y) = f_X(x) \cdot f_Y(y)"
            }
        ]
    },
    
    # --- EXAM ESSENTIALS with Step-by-Step Example ---
    "exam_essentials": {
        "header": {"de": "Prüfungs-Essentials", "en": "Exam Essentials"},
        "trap": {
            "title": {"de": "Die häufigste Falle", "en": "The Most Common Trap"},
            "content": {
                "de": "<strong>Richtung verwechselt:</strong> Für f_X summierst du ÜBER alle Y (Zeile). Für f_Y summierst du ÜBER alle X (Spalte).",
                "en": "<strong>Direction confused:</strong> For f_X you sum ACROSS all Y (row). For f_Y you sum ACROSS all X (column)."
            }
        },
        "example": {
            "title": {"de": "Konkretes Beispiel", "en": "Concrete Example"},
            "steps": [
                {"de": "Gegeben: f(1,1)=0.1, f(1,2)=0.2, f(1,3)=0.15", "en": "Given: f(1,1)=0.1, f(1,2)=0.2, f(1,3)=0.15"},
                {"de": "Gesucht: f_X(1) = Wahrscheinlichkeit dass X=1", "en": "Find: f_X(1) = Probability that X=1"},
                {"de": "Schritt: Summiere ALLE Y-Werte für X=1", "en": "Step: Sum ALL Y values for X=1"},
                {"de": "Rechnung: 0.1 + 0.2 + 0.15 = 0.45", "en": "Calculation: 0.1 + 0.2 + 0.15 = 0.45"},
                {"de": "Ergebnis: f_X(1) = 0.45", "en": "Result: f_X(1) = 0.45"}
            ]
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
    """5.1 Gemeinsame Verteilung und Randverteilungen - FIXED VERSION"""
    inject_equal_height_css()
    
    # --- HEADER ---
    st.header(t(content_5_1["title"]))
    st.caption(t(content_5_1["subtitle"]))
    st.markdown("---")
    
    # --- INTUITION HOOK (Side-by-Side Boxes - Blue/Red per rules) ---
    st.markdown(f"### {t(content_5_1['intuition']['header'])}")
    with st.container(border=True):
        # Intro text
        st.markdown(t(content_5_1["intuition"]["intro"]))
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Side-by-side boxes for Joint vs Marginal (Blue/Red per color palette)
        col_joint, col_marginal = st.columns(2)
        
        with col_joint:
            st.markdown(f"""
<div style="background: rgba(0, 122, 255, 0.1); border: 2px solid #007AFF; 
            border-radius: 8px; padding: 16px; text-align: center;">
<strong style="color: #007AFF; font-size: 1.1rem;">{t(content_5_1['intuition']['joint']['title'])}</strong><br>
<span>{t(content_5_1['intuition']['joint']['definition'])}</span><br><br>
<em style="color: #555;">"{t(content_5_1['intuition']['joint']['question'])}"</em>
</div>
""", unsafe_allow_html=True)
        
        with col_marginal:
            st.markdown(f"""
<div style="background: rgba(255, 75, 75, 0.1); border: 2px solid #FF4B4B; 
            border-radius: 8px; padding: 16px; text-align: center;">
<strong style="color: #FF4B4B; font-size: 1.1rem;">{t(content_5_1['intuition']['marginal']['title'])}</strong><br>
<span>{t(content_5_1['intuition']['marginal']['definition'])}</span><br><br>
<em style="color: #555;">"{t(content_5_1['intuition']['marginal']['question'])}"</em>
</div>
""", unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Visual diagram - smaller size
        st.image("assets/topic_5/joint_marginal_visual.png", 
                 caption=t({"de": "Joint = einzelne Zelle, Marginal = Zeilen-/Spaltensumme", 
                           "en": "Joint = single cell, Marginal = row/column sum"}),
                 width=450)
        
        # Key Insight - Grey callout (per rules)
        st.markdown(f"""
<div style="background: #f4f4f5; border-left: 4px solid #a1a1aa; 
            padding: 12px 16px; border-radius: 8px; color: #3f3f46;">
<strong>{t({"de": "Aha-Moment", "en": "Key Insight"})}:</strong> {t(content_5_1['intuition']['insight'])}
</div>
""", unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- FRAG DICH: 4 SEPARATE DECISION CARDS ---
    st.markdown(f"### {t(content_5_1['frag_dich']['header'])}")
    st.markdown(f"*{t(content_5_1['frag_dich']['intro'])}*")
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Each question gets its own container with context
    for i, q_data in enumerate(content_5_1['frag_dich']['questions']):
        with st.container(border=True):
            # Question as header
            st.markdown(f"**{i+1}. {t(q_data['q'])}**")
            st.markdown("<br>", unsafe_allow_html=True)
            
            # Answer and formula FIRST (formula prominent)
            col_ans, col_form = st.columns([1, 2])
            with col_ans:
                st.markdown(f"**→ {t(q_data['a'])}**")
            with col_form:
                st.latex(q_data['formula'])
            
            # Context/example BELOW in grey callout
            st.markdown(f"""
<div style="background: #f4f4f5; border-left: 4px solid #a1a1aa; 
            padding: 10px 14px; border-radius: 6px; color: #3f3f46; margin-top: 12px;">
<em>{t(q_data['context'])}</em>
</div>
""", unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- FORMULAS WITH DETAILED EXPLANATION ---
    st.markdown(f"### {t({'de': 'Die Formeln im Detail', 'en': 'The Formulas in Detail'})}")
    
    # JOINT DISTRIBUTION - Two-column layout
    with st.container(border=True):
        st.markdown(f"**{t({'de': 'Gemeinsame Verteilung (Joint)', 'en': 'Joint Distribution'})}**")
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Two columns: Formula | Explanation
        col_formula, col_explain = st.columns([1, 1.5])
        
        with col_formula:
            st.latex(r"f(x, y) = P(X = x \cap Y = y)")
        
        with col_explain:
            st.markdown(t({
                "de": "**Was sagt diese Formel?**\n\nWahrscheinlichkeit, dass **BEIDE** Ereignisse gleichzeitig eintreten.\n\n**Beispiel:** P(25-34 Jahre UND mittleres Einkommen)",
                "en": "**What does this formula say?**\n\nProbability that **BOTH** events happen at the same time.\n\n**Example:** P(25-34 years AND medium income)"
            }))
        
        # Variables in grey callout below
        st.markdown(f"""
<div style="background: #f4f4f5; border-left: 4px solid #a1a1aa; 
            padding: 12px 16px; border-radius: 8px; color: #3f3f46; margin-top: 12px;">
<strong>{t({"de": "Variablen", "en": "Variables"})}:</strong> 
$f(x,y)$ = {t({"de": "Wahrscheinlichkeit der Kombination", "en": "Probability of combination"})} · 
$X=x$ = {t({"de": "erste Variable", "en": "first variable"})} · 
$Y=y$ = {t({"de": "zweite Variable", "en": "second variable"})} · 
$\\cap$ = AND
</div>
""", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # MARGINAL DISTRIBUTION
    with st.container(border=True):
        st.markdown(f"**{t({'de': 'Randverteilung (Marginal)', 'en': 'Marginal Distribution'})}**")
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Two columns: Formulas | Explanation
        col_formula, col_explain = st.columns([1, 1.5])
        
        with col_formula:
            st.latex(r"f_X(x) = \sum_y f(x, y)")
            st.latex(r"f_Y(y) = \sum_x f(x, y)")
        
        with col_explain:
            st.markdown(t({
                "de": "**Was sagt diese Formel?**\n\n'Vergisst' die andere Variable. Addiere alle Zellen einer Zeile oder Spalte.\n\n**Beispiel:** P(25-34 Jahre), egal welches Einkommen → Zeilensumme",
                "en": "**What does this formula say?**\n\n'Forgets' the other variable. Add up all cells in a row or column.\n\n**Example:** P(25-34 years), regardless of income → Row sum"
            }))
        
        # Variables in grey callout below
        st.markdown(f"""
<div style="background: #f4f4f5; border-left: 4px solid #a1a1aa; 
            padding: 12px 16px; border-radius: 8px; color: #3f3f46; margin-top: 12px;">
<strong>{t({"de": "Variablen", "en": "Variables"})}:</strong> 
$f_X(x)$ = {t({"de": "Zeilensumme (summiere über Y)", "en": "Row sum (sum over Y)"})} · 
$f_Y(y)$ = {t({"de": "Spaltensumme (summiere über X)", "en": "Column sum (sum over X)"})}
</div>
""", unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- GUIDED MISSION: Step by Step (Stupid Person Rule) ---
    st.markdown(f"### {t({'de': 'Übung: Schritt für Schritt', 'en': 'Exercise: Step by Step'})}")
    
    @st.fragment
    def guided_mission():
        # Initialize state
        if "mission_step" not in st.session_state:
            st.session_state.mission_step = 1
            st.session_state.user_row_sum = 0.0
            st.session_state.mission_complete = False
        
        with st.container(border=True):
            # Scenario (per interactive.md rules) - with LaTeX
            st.markdown(f"""
<div style="background: #f4f4f5; border-left: 4px solid #a1a1aa; 
            padding: 12px 16px; border-radius: 8px; color: #3f3f46;">
<strong>{t({'de': 'Szenario', 'en': 'Scenario'})}:</strong><br>
{t({'de': 'Du hast eine Tabelle mit Wahrscheinlichkeiten. Wir berechnen gemeinsam die Randverteilung', 
    'en': 'You have a table of probabilities. We will calculate the marginal distribution'})} $f_X(1)$ {t({'de': 'für die erste Zeile.', 'en': 'for the first row.'})}
</div>
""", unsafe_allow_html=True)
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            # Simple 3-column table (values visible, no scrolling)
            table_data = [[0.10, 0.15, 0.05], [0.20, 0.10, 0.10], [0.05, 0.15, 0.10]]
            
            st.markdown(f"**{t({'de': 'Die Tabelle:', 'en': 'The Table:'})}**")
            
            # Centered HTML table - BIGGER with semantic colors (Red = target row)
            st.markdown("""
<div style="display: flex; justify-content: center; margin: 16px 0;">
<table style="border-collapse: collapse; text-align: center; font-size: 1.1rem;">
<tr style="background: #e5e7eb;">
    <th style="padding: 12px 24px; border: 1px solid #d1d5db;"></th>
    <th style="padding: 12px 24px; border: 1px solid #d1d5db;">Y=1</th>
    <th style="padding: 12px 24px; border: 1px solid #d1d5db;">Y=2</th>
    <th style="padding: 12px 24px; border: 1px solid #d1d5db;">Y=3</th>
</tr>
<tr style="background: rgba(255, 75, 75, 0.15);">
    <td style="padding: 12px 24px; border: 1px solid #d1d5db; font-weight: 600; color: #FF4B4B;">X=1</td>
    <td style="padding: 12px 24px; border: 1px solid #d1d5db; color: #FF4B4B; font-weight: 500;">0.10</td>
    <td style="padding: 12px 24px; border: 1px solid #d1d5db; color: #FF4B4B; font-weight: 500;">0.15</td>
    <td style="padding: 12px 24px; border: 1px solid #d1d5db; color: #FF4B4B; font-weight: 500;">0.05</td>
</tr>
<tr>
    <td style="padding: 12px 24px; border: 1px solid #d1d5db; font-weight: 600; background: #f4f4f5;">X=2</td>
    <td style="padding: 12px 24px; border: 1px solid #d1d5db;">0.20</td>
    <td style="padding: 12px 24px; border: 1px solid #d1d5db;">0.10</td>
    <td style="padding: 12px 24px; border: 1px solid #d1d5db;">0.10</td>
</tr>
<tr>
    <td style="padding: 12px 24px; border: 1px solid #d1d5db; font-weight: 600; background: #f4f4f5;">X=3</td>
    <td style="padding: 12px 24px; border: 1px solid #d1d5db;">0.05</td>
    <td style="padding: 12px 24px; border: 1px solid #d1d5db;">0.15</td>
    <td style="padding: 12px 24px; border: 1px solid #d1d5db;">0.10</td>
</tr>
</table>
</div>
""", unsafe_allow_html=True)
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            # STEP-BY-STEP GUIDED APPROACH
            step = st.session_state.mission_step
            
            if step == 1:
                st.markdown(f"**{t({'de': 'Schritt 1: Verstehe die Aufgabe', 'en': 'Step 1: Understand the Task'})}**")
                st.markdown(t({
                    "de": "Wir wollen",
                    "en": "We want to calculate"
                }), unsafe_allow_html=True)
                st.latex(r"f_X(1)")
                st.markdown(t({
                    "de": "— die Wahrscheinlichkeit, dass X=1 ist, **egal welchen Wert Y hat**.",
                    "en": "— the probability that X=1, **regardless of what value Y has**."
                }))
                st.markdown("<br>", unsafe_allow_html=True)
                st.markdown(t({
                    "de": "**Frage:** Welche Zeile müssen wir betrachten?",
                    "en": "**Question:** Which row do we need to look at?"
                }))
                
                answer = st.radio(
                    t({"de": "Wähle:", "en": "Choose:"}),
                    [t({"de": "Zeile X=1", "en": "Row X=1"}), 
                     t({"de": "Zeile X=2", "en": "Row X=2"}),
                     t({"de": "Zeile X=3", "en": "Row X=3"})],
                    key="step1_answer",
                    index=None
                )
                
                if answer == t({"de": "Zeile X=1", "en": "Row X=1"}):
                    st.success(t({"de": "Richtig! Wir schauen uns Zeile X=1 an.", "en": "Correct! We look at row X=1."}))
                    if st.button(t({"de": "Weiter zu Schritt 2", "en": "Continue to Step 2"}), key="to_step2"):
                        st.session_state.mission_step = 2
                        st.rerun(scope="fragment")
                elif answer:
                    st.error(t({"de": "Da X=1 ist, müssen wir Zeile X=1 betrachten.", "en": "Since X=1, we need to look at row X=1."}))
            
            elif step == 2:
                st.markdown(f"**{t({'de': 'Schritt 2: Identifiziere die Werte', 'en': 'Step 2: Identify the Values'})}**")
                st.markdown(t({
                    "de": "In Zeile X=1 stehen die Werte: **0.10, 0.15, 0.05**",
                    "en": "Row X=1 contains the values: **0.10, 0.15, 0.05**"
                }))
                st.markdown("<br>", unsafe_allow_html=True)
                st.markdown(t({
                    "de": "**Frage:** Was müssen wir mit diesen Werten tun?",
                    "en": "**Question:** What do we need to do with these values?"
                }))
                
                answer = st.radio(
                    t({"de": "Wähle:", "en": "Choose:"}),
                    [t({"de": "Addieren", "en": "Add them"}), 
                     t({"de": "Multiplizieren", "en": "Multiply them"}),
                     t({"de": "Subtrahieren", "en": "Subtract them"})],
                    key="step2_answer",
                    index=None
                )
                
                if answer == t({"de": "Addieren", "en": "Add them"}):
                    st.success(t({"de": "Richtig! Wir addieren alle Werte der Zeile.", "en": "Correct! We add all values in the row."}))
                    if st.button(t({"de": "Weiter zu Schritt 3", "en": "Continue to Step 3"}), key="to_step3"):
                        st.session_state.mission_step = 3
                        st.rerun(scope="fragment")
                elif answer:
                    st.error(t({"de": "Für die Randverteilung addieren wir!", "en": "For marginal distribution, we add!"}))
            
            elif step == 3:
                st.markdown(f"**{t({'de': 'Schritt 3: Berechne', 'en': 'Step 3: Calculate'})}**")
                st.markdown(t({
                    "de": "0.10 + 0.15 + 0.05 = ?",
                    "en": "0.10 + 0.15 + 0.05 = ?"
                }))
                st.markdown("<br>", unsafe_allow_html=True)
                
                user_answer = st.number_input(
                    t({"de": "Deine Antwort:", "en": "Your answer:"}),
                    min_value=0.0, max_value=1.0, step=0.01,
                    value=0.0,
                    key="step3_answer"
                )
                
                if st.button(t({"de": "Prüfen", "en": "Check"}), key="check_step3"):
                    if abs(user_answer - 0.30) < 0.01:
                        st.success(t({"de": "Perfekt! f_X(1) = 0.30", "en": "Perfect! f_X(1) = 0.30"}))
                        st.balloons()
                        st.session_state.mission_complete = True
                        
                        # Track progress
                        from utils.progress_tracker import track_question_answer
                        if user := st.session_state.get("user"):
                            track_question_answer(user["localId"], "vwl", "5", "5.1", "marginal_mission", True)
                    else:
                        st.error(t({"de": "Rechne nochmal: 0.10 + 0.15 + 0.05 = ?", "en": "Calculate again: 0.10 + 0.15 + 0.05 = ?"}))
            
            if st.session_state.mission_complete:
                st.markdown("<br>", unsafe_allow_html=True)
                st.markdown(f"""
<div style="background: #dcfce7; border-left: 4px solid #22c55e; 
            padding: 12px 16px; border-radius: 8px; color: #166534;">
<strong>{t({'de': 'Mission erfolgreich!', 'en': 'Mission Complete!'})}:</strong><br>
{t({'de': 'Du hast die Randverteilung f_X(1) = 0.30 berechnet. Das Prinzip ist immer gleich: Zeile oder Spalte summieren!', 
    'en': 'You calculated the marginal distribution f_X(1) = 0.30. The principle is always the same: sum the row or column!'})}
</div>
""", unsafe_allow_html=True)
                
                # Reset button
                if st.button(t({"de": "Nochmal üben", "en": "Practice again"}), key="reset_mission"):
                    st.session_state.mission_step = 1
                    st.session_state.mission_complete = False
                    st.rerun(scope="fragment")
    
    guided_mission()
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- EXAM ESSENTIALS (Grey callouts per rules) ---
    st.markdown(f"### {t(content_5_1['exam_essentials']['header'])}")
    with st.container(border=True):
        # Trap - Grey callout
        st.markdown(f"""
<div style="background: #f4f4f5; border-left: 4px solid #a1a1aa; 
            padding: 12px 16px; border-radius: 8px; color: #3f3f46;">
<strong>{t(content_5_1['exam_essentials']['trap']['title'])}:</strong> {t(content_5_1["exam_essentials"]["trap"]["content"])}
</div>
""", unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Step-by-step example - Grey callout
        st.markdown(f"**{t(content_5_1['exam_essentials']['example']['title'])}**")
        st.markdown(f"""
<div style="background: #f4f4f5; border-left: 4px solid #a1a1aa; 
            padding: 12px 16px; border-radius: 8px; color: #3f3f46;">
{"<br>".join([f"<strong>{i}.</strong> {t(step)}" for i, step in enumerate(content_5_1['exam_essentials']['example']['steps'], 1)])}
</div>
""", unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Tips - Grey callout
        st.markdown(f"""
<div style="background: #f4f4f5; border-left: 4px solid #a1a1aa; 
            padding: 12px 16px; border-radius: 8px; color: #3f3f46;">
<strong>{t({'de': 'Pro Tipps', 'en': 'Pro Tips'})}:</strong><br>
{"<br>".join([f"({i}) <strong>{t(tip_data['tip'])}</strong> — <em>{t(tip_data['why'])}</em>" for i, tip_data in enumerate(content_5_1['exam_essentials']['tips'], 1)])}
</div>
""", unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- EXAM SECTION ---
    st.markdown(f"### {t({'de': 'Prüfungstraining', 'en': 'Exam Practice'})}")
    
    # MCQ 1: test3_q4 (E[X+Y])
    q1 = get_question("5.1", "test3_q4")
    if q1:
        with st.container(border=True):
            st.caption(q1.get("source", ""))
            opts = q1.get("options", [])
            if opts and isinstance(opts[0], dict):
                option_labels = [t(o) for o in opts]
            else:
                option_labels = opts
            
            render_mcq(
                key_suffix="5_1_sum",
                question_text=t(q1["question"]),
                options=option_labels,
                correct_idx=q1["correct_idx"],
                solution_text_dict=q1["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
                client=model,
                ai_context="Linearity of expectation in joint distributions",
                course_id="vwl",
                topic_id="5",
                subtopic_id="5.1",
                question_id="5_1_sum"
            )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # MCQ 2: uebung3_mc5 (Expectation operator)
    q2 = get_question("5.1", "uebung3_mc5")
    if q2:
        with st.container(border=True):
            st.caption(q2.get("source", ""))
            opts = q2.get("options", [])
            if opts and isinstance(opts[0], dict):
                option_labels = [t(o) for o in opts]
            else:
                option_labels = opts
            
            render_mcq(
                key_suffix="5_1_linear",
                question_text=t(q2["question"]),
                options=option_labels,
                correct_idx=q2["correct_idx"],
                solution_text_dict=q2["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
                client=model,
                ai_context="Properties of expectation operator",
                course_id="vwl",
                topic_id="5",
                subtopic_id="5.1",
                question_id="5_1_linear"
            )
