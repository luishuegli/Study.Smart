# Topic 5.2: Conditional Distributions and Stochastic Independence
# Refactored to match gold standard patterns from topic_4_3_content.py and topic_1_7_content.py
import streamlit as st
import plotly.graph_objects as go
from views.styles import inject_equal_height_css
from utils.localization import t
from utils.quiz_helper import render_mcq
from data.exam_questions import get_question

# ==========================================
# 1. CONTENT DICTIONARY - BILINGUAL (GOLD STANDARD FORMAT)
# ==========================================
content_5_2 = {
    "title": {"de": "5.2 Bedingte Verteilungen und stochastische Unabhängigkeit", "en": "5.2 Conditional Distributions and Stochastic Independence"},
    "subtitle": {
        "de": "Was passiert, wenn du schon etwas weisst?",
        "en": "What happens when you already know something?"
    },
    
    # --- INTUITION HOOK ---
    "intuition": {
        "header": {"de": "Die Intuition", "en": "The Intuition"},
        "text": {
            "de": "Stell dir vor, du kennst das Ergebnis **einer** Zufallsvariable. Ändert das, was du über die **andere** weisst? Wenn ja: **bedingte Verteilung**. Wenn nein: **Unabhängigkeit**.",
            "en": "Imagine you know the outcome of **one** random variable. Does that change what you know about the **other**? If yes: **conditional distribution**. If no: **independence**."
        }
    },
    
    # --- FRAG DICH (Decision Guide) ---
    "frag_dich": {
        "header": {"de": "Frag dich: Welche Situation liegt vor?", "en": "Ask yourself: What situation is this?"},
        "questions": [
            {"de": "Brauchst du P(X) **GEGEBEN** du hast Y beobachtet?", "en": "Do you need P(X) **GIVEN** you observed Y?"},
            {"de": "Ist Information über Y **nützlich** für die Vorhersage von X?", "en": "Is information about Y **useful** for predicting X?"},
            {"de": "Kann die gemeinsame Dichte als **Produkt** der Randdichten geschrieben werden?", "en": "Can the joint density be written as the **product** of marginals?"}
        ],
        "conclusion": {"de": "Produkt der Marginalen = Unabhängig | Sonst = Bedingte Verteilung nutzen", "en": "Product of marginals = Independent | Otherwise = Use conditional distribution"}
    },
    
    # --- DEFINITION (Conditional Distribution) ---
    "definition_conditional": {
        "header": {"de": "Die bedingte Verteilung", "en": "The Conditional Distribution"},
        "text": {
            "de": "Die bedingte Verteilung von X gegeben Y=y gibt die Wahrscheinlichkeit von X an, **nachdem** du Y=y beobachtet hast.",
            "en": "The conditional distribution of X given Y=y specifies the probability of X **after** observing Y=y."
        },
        "formula_discrete": r"f_{X|Y}(x|y) = \frac{f_{X,Y}(x,y)}{f_Y(y)}",
        "formula_continuous": r"f_{X|Y}(x|y) = \frac{f(x,y)}{f_Y(y)}",
        # VARIABLE DECODER - "Stupid Person Rule" applied (like 4.3)
        "variable_decoder": {
            "header": {"de": "Was bedeutet jedes Symbol?", "en": "What does each symbol mean?"},
            "variables": [
                {
                    "symbol": r"f_{X|Y}(x|y)",
                    "name": {"de": "Bedingte Massenfunktion/Dichte", "en": "Conditional Mass/Density Function"},
                    "meaning": {
                        "de": "Die Wahrscheinlichkeit dass X=x ist, **gegeben** du weisst schon Y=y. Der Strich '|' bedeutet 'unter der Bedingung'.",
                        "en": "The probability that X=x, **given** you already know Y=y. The bar '|' means 'conditional on'."
                    },
                    "example": {"de": "P(Erfolg | Training absolviert) — Erfolgswahrscheinlichkeit für Trainierte", "en": "P(Success | Training done) — success rate for trained people"}
                },
                {
                    "symbol": r"f_{X,Y}(x,y)",
                    "name": {"de": "Gemeinsame Verteilung", "en": "Joint Distribution"},
                    "meaning": {
                        "de": "Die Wahrscheinlichkeit, dass BEIDE Ereignisse gleichzeitig auftreten: X=x UND Y=y.",
                        "en": "The probability that BOTH events occur simultaneously: X=x AND Y=y."
                    },
                    "example": {"de": "P(Gross UND Blond) — beides zusammen", "en": "P(Tall AND Blonde) — both together"}
                },
                {
                    "symbol": r"f_Y(y)",
                    "name": {"de": "Randverteilung von Y", "en": "Marginal Distribution of Y"},
                    "meaning": {
                        "de": "Die Wahrscheinlichkeit von Y=y **insgesamt**, also über alle möglichen X summiert/integriert. Der Nenner **normiert** auf die Bedingung.",
                        "en": "The probability of Y=y **overall**, summed/integrated over all possible X. The denominator **normalizes** to the condition."
                    },
                    "example": {"de": "P(Training absolviert) — egal wie der Ausgang war", "en": "P(Training done) — regardless of outcome"}
                }
            ],
            "full_reading": {
                "de": "**Lies die Formel so:**<br>'Die Wahrscheinlichkeit von X gegeben Y ist gleich der gemeinsamen Wahrscheinlichkeit geteilt durch die Randwahrscheinlichkeit der Bedingung.'",
                "en": "**Read the formula as:**<br>'The probability of X given Y equals the joint probability divided by the marginal probability of the condition.'"
            }
        }
    },
    
    # --- DEFINITION (Independence) ---
    "definition_independence": {
        "header": {"de": "Stochastische Unabhängigkeit", "en": "Stochastic Independence"},
        "text": {
            "de": "Zwei Zufallsvariablen X und Y sind **stochastisch unabhängig**, wenn Information über Y nichts über X verrät — und umgekehrt.",
            "en": "Two random variables X and Y are **stochastically independent** when information about Y reveals nothing about X — and vice versa."
        },
        "formula": r"f_{X,Y}(x,y) = f_X(x) \cdot f_Y(y) \quad \forall (x,y)",
        "variable_decoder": {
            "header": {"de": "Was bedeutet jedes Symbol?", "en": "What does each symbol mean?"},
            "variables": [
                {
                    "symbol": r"f_{X,Y}(x,y)",
                    "name": {"de": "Gemeinsame Verteilung", "en": "Joint Distribution"},
                    "meaning": {
                        "de": "Bei Unabhängigkeit kann man diese EINFACH berechnen: einfach die beiden Einzelwahrscheinlichkeiten multiplizieren!",
                        "en": "With independence, you can EASILY calculate this: just multiply the two individual probabilities!"
                    },
                    "example": {"de": "P(Münze zeigt Kopf UND Würfel zeigt 6) = 0.5 × 1/6", "en": "P(Coin shows Heads AND Die shows 6) = 0.5 × 1/6"}
                },
                {
                    "symbol": r"\forall (x,y)",
                    "name": {"de": "'Für alle'", "en": "'For all'"},
                    "meaning": {
                        "de": "Die Gleichung muss für **JEDE** Kombination (x,y) gelten — nicht nur für einige! Wenn auch nur EINE Zelle nicht passt = abhängig.",
                        "en": "The equation must hold for **EVERY** combination (x,y) — not just some! If even ONE cell doesn't match = dependent."
                    },
                    "example": {"de": "Prüfe alle 4 Zellen einer 2×2 Tabelle", "en": "Check all 4 cells of a 2×2 table"}
                }
            ],
            "key_implication": {
                "de": "**Folgerung:** Bei Unabhängigkeit ist die bedingte Verteilung GLEICH der Randverteilung: $f_{X|Y}(x|y) = f_X(x)$. Der 'Filter' Y ändert nichts!",
                "en": "**Implication:** With independence, the conditional distribution EQUALS the marginal: $f_{X|Y}(x|y) = f_X(x)$. The 'filter' Y changes nothing!"
            }
        }
    },
    
    # --- WORKED EXAMPLE (Step-by-Step like 4.3) ---
    "example_worked": {
        "header": {"de": "Schritt-für-Schritt: Bedingte Wahrscheinlichkeit", "en": "Step-by-Step: Conditional Probability"},
        "problem": {
            "de": "Aus der Vorlesung (Beispiel 5.2.1): Drei Münzwürfe. X = Anzahl Köpfe beim 1. Wurf (0 oder 1). Y = Gesamtanzahl Köpfe. Berechne $P(X=1 \\mid Y=1)$.",
            "en": "From the lecture (Example 5.2.1): Three coin flips. X = heads on 1st flip (0 or 1). Y = total heads. Calculate $P(X=1 \\mid Y=1)$."
        },
        "steps": [
            {
                "label": {"de": "Gegeben aus Tabelle", "en": "Given from Table"},
                "latex": r"{\color{#9B59B6}f(1,1) = \frac{1}{8}}, \quad {\color{#007AFF}f_Y(1) = \frac{3}{8}}",
                "note": {"de": "(Joint: X=1 UND Y=1) (Marginal: Y=1 insgesamt)", "en": "(Joint: X=1 AND Y=1) (Marginal: Y=1 overall)"}
            },
            {
                "label": {"de": "Formel anwenden", "en": "Apply Formula"},
                "latex": r"f_{X|Y}({\color{#FF4B4B}1}|1) = \frac{f(1,1)}{f_Y(1)} = \frac{{\color{#9B59B6}1/8}}{{\color{#007AFF}3/8}}",
                "note": {"de": "Bedingte = Joint / Marginal der Bedingung", "en": "Conditional = Joint / Marginal of condition"}
            },
            {
                "label": {"de": "Rechnen", "en": "Calculate"},
                "latex": r"= \frac{1/8}{3/8} = \frac{1}{8} \times \frac{8}{3} = {\color{#16a34a}\frac{1}{3}}",
                "note": {"de": "Bruch dividieren = mit Kehrwert multiplizieren", "en": "Divide by fraction = multiply by reciprocal"}
            }
        ],
        "answer": {
            "de": "Die Wahrscheinlichkeit ist $\\frac{1}{3} \\approx 33.3\\%$",
            "en": "The probability is $\\frac{1}{3} \\approx 33.3\\%$"
        },
        "check": {
            "de": "**Plausibilitäts-Check:** Alle bedingten Wsk f(x|Y=1) müssen sich zu 1 summieren. Hier: f(0|1) + f(1|1) = 2/3 + 1/3 = 1 ✓",
            "en": "**Plausibility Check:** All conditional probs f(x|Y=1) must sum to 1. Here: f(0|1) + f(1|1) = 2/3 + 1/3 = 1 ✓"
        }
    },
    
    # --- EXAM ESSENTIALS ---
    "exam_essentials": {
        "header": {"de": "Prüfungs-Essentials", "en": "Exam Essentials"},
        "items": [
            {
                "label": {"de": "Falle", "en": "Trap"},
                "title": {"de": "Cov = 0 ≠ Unabhängigkeit!", "en": "Cov = 0 ≠ Independence!"},
                "content": {
                    "de": "Korrelation misst nur **linearen** Zusammenhang. X und Y können stark abhängig sein (z.B. Y = X²) mit Cov(X,Y) = 0!",
                    "en": "Correlation only measures **linear** relationship. X and Y can be strongly dependent (e.g., Y = X²) with Cov(X,Y) = 0!"
                },
                "type": "warning"
            },
            {
                "label": {"de": "Regel", "en": "Rule"},
                "title": {"de": "Rechteckiger Träger → gutes Zeichen", "en": "Rectangular Support → good sign"},
                "content": {
                    "de": "Bei Unabhängigkeit ist der Träger (wo f(x,y) > 0) immer **ein Rechteck**. Dreieck oder andere Form → fast immer abhängig!",
                    "en": "With independence, support (where f(x,y) > 0) is always **a rectangle**. Triangle or other shape → almost always dependent!"
                },
                "type": "tip"
            },
            {
                "label": {"de": "Tipp", "en": "Tip"},
                "title": {"de": "E[XY] = E[X]·E[Y] braucht nur Unkorreliertheit", "en": "E[XY] = E[X]·E[Y] only needs uncorrelatedness"},
                "content": {
                    "de": "Diese Eigenschaft gilt schon wenn Cov = 0, nicht erst bei Unabhängigkeit. Unabhängigkeit ist **stärker**.",
                    "en": "This property holds when Cov = 0, not only for independence. Independence is **stronger**."
                },
                "type": "tip"
            }
        ]
    }
}


def render_subtopic_5_2(model):
    """5.2 Bedingte Verteilungen und stochastische Unabhängigkeit - GOLD STANDARD VERSION"""
    inject_equal_height_css()
    
    # --- HEADER ---
    st.header(t(content_5_2["title"]))
    st.caption(t(content_5_2["subtitle"]))
    st.markdown("---")
    
    # --- INTUITION HOOK ---
    st.markdown(f"### {t(content_5_2['intuition']['header'])}")
    with st.container(border=True):
        st.markdown(t(content_5_2["intuition"]["text"]))
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- FRAG DICH: DECISION GUIDE ---
    from utils.ask_yourself import render_ask_yourself
    render_ask_yourself(
        header=content_5_2['frag_dich']['header'],
        questions=content_5_2['frag_dich']['questions'],
        conclusion=content_5_2['frag_dich']['conclusion']
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- DEFINITION: CONDITIONAL (with integrated Symbol Ledger - like 4.3) ---
    cond = content_5_2["definition_conditional"]
    st.markdown(f"### {t(cond['header'])}")
    with st.container(border=True):
        st.markdown(t(cond["text"]))
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Show both discrete and continuous formulas
        col_disc, col_cont = st.columns(2, gap="medium")
        with col_disc:
            st.caption(t({"de": "Diskret", "en": "Discrete"}))
            st.latex(cond["formula_discrete"])
        with col_cont:
            st.caption(t({"de": "Stetig", "en": "Continuous"}))
            st.latex(cond["formula_continuous"])
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # --- INTEGRATED SYMBOL LEDGER (inside same container) ---
        decoder = cond["variable_decoder"]
        st.markdown(f"**{t(decoder['header'])}**")
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Render each variable using native Streamlit layout for proper LaTeX
        for i, var in enumerate(decoder["variables"]):
            col_sym, col_content = st.columns([1, 4])
            with col_sym:
                st.latex(var['symbol'])
            with col_content:
                st.markdown(f"**{t(var['name'])}**")
                st.markdown(t(var['meaning']), unsafe_allow_html=True)
                st.caption(t(var['example']))
            st.markdown("---")
        
        # Full reading summary at the bottom
        st.markdown(f"""
<div style="background: #f4f4f5; border-radius: 8px; padding: 14px;">
    <div style="color: #3f3f46; line-height: 1.5;">{t(decoder['full_reading'])}</div>
</div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- DEFINITION: INDEPENDENCE (with integrated Symbol Ledger) ---
    indep = content_5_2["definition_independence"]
    st.markdown(f"### {t(indep['header'])}")
    with st.container(border=True):
        st.markdown(t(indep["text"]))
        st.markdown("<br>", unsafe_allow_html=True)
        st.latex(indep["formula"])
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # --- INTEGRATED SYMBOL LEDGER ---
        decoder = indep["variable_decoder"]
        st.markdown(f"**{t(decoder['header'])}**")
        st.markdown("<br>", unsafe_allow_html=True)
        
        for i, var in enumerate(decoder["variables"]):
            col_sym, col_content = st.columns([1, 4])
            with col_sym:
                st.latex(var['symbol'])
            with col_content:
                st.markdown(f"**{t(var['name'])}**")
                st.markdown(t(var['meaning']), unsafe_allow_html=True)
                st.caption(t(var['example']))
            st.markdown("---")
        
        # Key implication callout
        st.markdown(t(decoder['key_implication']))
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- WORKED EXAMPLE (Like 4.3) ---
    ex = content_5_2["example_worked"]
    st.markdown(f"### {t(ex['header'])}")
    with st.container(border=True):
        st.markdown(t(ex['problem']), unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Steps with proper LaTeX and plain labels
        for i, step in enumerate(ex["steps"]):
            if i > 0:
                st.markdown("---")
            
            st.markdown(f"**{t(step['label'])}:**")
            st.latex(step["latex"])
            
            if step.get("note"):
                st.caption(t(step["note"]))
        
        st.markdown("---")
        st.markdown(f"**{t(ex['answer'])}**")
        
        st.markdown("<br>", unsafe_allow_html=True)
        # Plausibility check callout
        st.markdown(f"""
        <div style="background-color: #f4f4f5; border-radius: 8px; padding: 12px; border-left: 4px solid #a1a1aa; color: #3f3f46;">
            {t(ex['check'])}
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # =========================================
    # INTERACTIVE MISSION: INDEPENDENCE CHECKER (Like 1.7)
    # =========================================
    st.markdown(f"### {t({'de': 'Interaktive Übung: Münzwurf (Beispiel 5.2.1)', 'en': 'Interactive Exercise: Coin Toss (Example 5.2.1)'})}")
    
    @st.fragment
    def coin_toss_mission():
        if "coin_mission_5_2_completed" not in st.session_state:
            st.session_state.coin_mission_5_2_completed = False
        
        # Scenario callout
        st.markdown(f"""
<div style="background: #f4f4f5; border-left: 4px solid #a1a1aa; 
            padding: 12px 16px; border-radius: 8px; color: #3f3f46; margin-bottom: 16px;">
<strong>{t({'de': 'Das Szenario', 'en': 'The Scenario'})}</strong><br>
{t({'de': 'Drei faire Münzwürfe. X = Köpfe beim 1. Wurf (0 oder 1). Y = Gesamte Köpfe (0, 1, 2, oder 3).', 
    'en': 'Three fair coin flips. X = heads on 1st flip (0 or 1). Y = total heads (0, 1, 2, or 3).'})}
</div>
""", unsafe_allow_html=True)
        
        with st.container(border=True):
            st.markdown(f"**{t({'de': 'Gemeinsame Wahrscheinlichkeitstabelle', 'en': 'Joint Probability Table'})}**")
            
            # The actual joint probability table from Beispiel 5.2.1 - rendered as HTML
            st.markdown("""
<div style="display: flex; justify-content: center; margin: 16px 0; overflow-x: auto;">
<table style="border-collapse: collapse; text-align: center; font-size: 0.9rem;">
<tr style="background: #e5e7eb;">
    <th style="padding: 8px 14px; border: 1px solid #d1d5db;"></th>
    <th style="padding: 8px 14px; border: 1px solid #d1d5db;">Y=0</th>
    <th style="padding: 8px 14px; border: 1px solid #d1d5db; background: rgba(0, 122, 255, 0.15);">Y=1</th>
    <th style="padding: 8px 14px; border: 1px solid #d1d5db;">Y=2</th>
    <th style="padding: 8px 14px; border: 1px solid #d1d5db;">Y=3</th>
    <th style="padding: 8px 14px; border: 1px solid #d1d5db; background: #f4f4f5;">f<sub>X</sub></th>
</tr>
<tr>
    <td style="padding: 8px 14px; border: 1px solid #d1d5db; font-weight: 600; background: #f4f4f5;">X=0</td>
    <td style="padding: 8px 14px; border: 1px solid #d1d5db;">1/8</td>
    <td style="padding: 8px 14px; border: 1px solid #d1d5db; background: rgba(0, 122, 255, 0.08);">1/4</td>
    <td style="padding: 8px 14px; border: 1px solid #d1d5db;">1/8</td>
    <td style="padding: 8px 14px; border: 1px solid #d1d5db;">0</td>
    <td style="padding: 8px 14px; border: 1px solid #d1d5db; background: #f4f4f5;">1/2</td>
</tr>
<tr style="background: rgba(255, 75, 75, 0.08);">
    <td style="padding: 8px 14px; border: 1px solid #d1d5db; font-weight: 600; color: #FF4B4B; background: #f4f4f5;">X=1</td>
    <td style="padding: 8px 14px; border: 1px solid #d1d5db;">0</td>
    <td style="padding: 8px 14px; border: 1px solid #d1d5db; background: rgba(155, 89, 182, 0.25); font-weight: 600; color: #9B59B6;">1/8</td>
    <td style="padding: 8px 14px; border: 1px solid #d1d5db;">1/4</td>
    <td style="padding: 8px 14px; border: 1px solid #d1d5db;">1/8</td>
    <td style="padding: 8px 14px; border: 1px solid #d1d5db; background: #f4f4f5;">1/2</td>
</tr>
<tr style="background: #f4f4f5;">
    <td style="padding: 8px 14px; border: 1px solid #d1d5db; font-weight: 600;">f<sub>Y</sub></td>
    <td style="padding: 8px 14px; border: 1px solid #d1d5db;">1/8</td>
    <td style="padding: 8px 14px; border: 1px solid #d1d5db; background: rgba(0, 122, 255, 0.15); font-weight: 600; color: #007AFF;">3/8</td>
    <td style="padding: 8px 14px; border: 1px solid #d1d5db;">3/8</td>
    <td style="padding: 8px 14px; border: 1px solid #d1d5db;">1/8</td>
    <td style="padding: 8px 14px; border: 1px solid #d1d5db;">1</td>
</tr>
</table>
</div>
""", unsafe_allow_html=True)
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            # Color key
            st.caption(t({
                "de": "Farbcode: 🟣 = f(1,1), 🔵 = f_Y(1) (die Bedingung)",
                "en": "Color code: 🟣 = f(1,1), 🔵 = f_Y(1) (the condition)"
            }))
            
            st.markdown("---")
            
            # Question
            st.markdown(f"**{t({'de': 'Deine Aufgabe', 'en': 'Your Task'})}:** {t({'de': 'Berechne P(X=1 | Y=1)', 'en': 'Calculate P(X=1 | Y=1)'})}")
            
            st.latex(r"P(X=1 \mid Y=1) = \frac{f(1,1)}{f_Y(1)} = \frac{{\color{#9B59B6}1/8}}{{\color{#007AFF}3/8}} = \; ?")
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            answer = st.radio(
                t({"de": "Wähle die richtige Antwort:", "en": "Choose the correct answer:"}),
                ["1/4", "1/3", "1/2", "2/3"],
                key="coin_mission_5_2_radio",
                index=None,
                horizontal=True
            )
            
            if answer:
                if answer == "1/3":
                    st.balloons()
                    st.success(t({
                        "de": "**Richtig!** (1/8) ÷ (3/8) = (1/8) × (8/3) = 1/3",
                        "en": "**Correct!** (1/8) ÷ (3/8) = (1/8) × (8/3) = 1/3"
                    }))
                    
                    # Mastery card
                    st.markdown("<br>", unsafe_allow_html=True)
                    st.markdown(f"""
<div style="background: #f4f4f5; border-left: 4px solid #16a34a; padding: 12px 16px; border-radius: 8px; color: #3f3f46;">
<strong>{t({'de': 'Was du gelernt hast:', 'en': 'What you learned:'})}</strong><br>
{t({'de': 'Das Universum schrumpft! Von 8 möglichen Ergebnissen sind nur noch 3 relevant (die mit Y=1). Davon hat genau 1 auch X=1.', 
    'en': 'The universe shrinks! Of 8 possible outcomes, only 3 are relevant (those with Y=1). Of those, exactly 1 also has X=1.'})}
</div>
""", unsafe_allow_html=True)
                    
                    # Track progress
                    if not st.session_state.coin_mission_5_2_completed:
                        st.session_state.coin_mission_5_2_completed = True
                        from utils.progress_tracker import track_question_answer, update_local_progress
                        if user := st.session_state.get("user"):
                            update_local_progress("5", "5.2", "5_2_coin_mission", True)
                            track_question_answer(user["localId"], "vwl", "5", "5.2", "5_2_coin_mission", True)
                else:
                    st.error(t({
                        "de": "**Nicht ganz.** Tipp: Bruch dividieren = mit Kehrwert multiplizieren. (1/8) ÷ (3/8) = ?",
                        "en": "**Not quite.** Tip: Divide by fraction = multiply by reciprocal. (1/8) ÷ (3/8) = ?"
                    }))
    
    coin_toss_mission()
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- EXAM ESSENTIALS ---
    from utils.exam_essentials import render_exam_essentials
    render_exam_essentials(items=content_5_2["exam_essentials"]["items"])
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- EXAM SECTION ---
    st.markdown(f"### {t({'de': 'Prüfungstraining', 'en': 'Exam Practice'})}")
    
    # MCQ 1: hs2023_mc9 (Cov calculation)
    q1 = get_question("5.2", "hs2023_mc9")
    if q1:
        with st.container(border=True):
            st.caption(q1.get("source", ""))
            opts = q1.get("options", [])
            option_labels = [t(o) if isinstance(o, dict) else o for o in opts]
            
            render_mcq(
                key_suffix="5_2_cov",
                question_text=t(q1["question"]),
                options=option_labels,
                correct_idx=q1["correct_idx"],
                solution_text_dict=q1["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
                client=model,
                ai_context="Covariance calculation with linear transformation",
                course_id="vwl",
                topic_id="5",
                subtopic_id="5.2",
                question_id="5_2_cov"
            )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # MCQ 2: test3_q5 (Var(X-Y))
    q2 = get_question("5.2", "test3_q5")
    if q2:
        with st.container(border=True):
            st.caption(q2.get("source", ""))
            opts = q2.get("options", [])
            option_labels = [t(o) if isinstance(o, dict) else o for o in opts]
            
            render_mcq(
                key_suffix="5_2_vardiff",
                question_text=t(q2["question"]),
                options=option_labels,
                correct_idx=q2["correct_idx"],
                solution_text_dict=q2["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
                client=model,
                ai_context="Variance of difference of independent variables",
                course_id="vwl",
                topic_id="5",
                subtopic_id="5.2",
                question_id="5_2_vardiff"
            )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # MCQ 3: uebung3_mc7 (Var(aX+b))
    q3 = get_question("5.2", "uebung3_mc7")
    if q3:
        with st.container(border=True):
            st.caption(q3.get("source", ""))
            opts = q3.get("options", [])
            option_labels = [t(o) if isinstance(o, dict) else o for o in opts]
            
            render_mcq(
                key_suffix="5_2_varscale",
                question_text=t(q3["question"]),
                options=option_labels,
                correct_idx=q3["correct_idx"],
                solution_text_dict=q3["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
                client=model,
                ai_context="Variance of linear transformation",
                course_id="vwl",
                topic_id="5",
                subtopic_id="5.2",
                question_id="5_2_varscale"
            )
