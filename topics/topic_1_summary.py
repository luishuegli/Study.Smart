import streamlit as st
import numpy as np
from views.styles import render_icon
from utils.localization import t
from utils.quiz_helper import render_mcq

# --- CONTENT DICTIONARY ---
content_1_10 = {
    "title": {"de": "1.10 Zusammenfassung & Final Exam", "en": "1.10 Summary & Final Exam"},
    "intro": {"de": "Bevor wir zur Prüfung kommen: Hier ist dein Spickzettel.", "en": "Before the exam: Here is your cheat sheet."},
    "cheat_sheet": {
        "tabs": ["Definitions", "Rules", "Bayes"],
        "def_title": {"de": "Grundbegriffe", "en": "Basic Concepts"},
        "def_content": {
            "de": """
            - **$\Omega$ (Ergebnisraum):** Menge aller möglichen Ausgänge.
            - **$\mathcal{F}$ (Ereignisraum):** Menge aller messbaren Ereignisse.
            - **$P$ (Wahrscheinlichkeitsmaß):** Ordnet jedem Ereignis eine Zahl $[0,1]$ zu.
            - **Laplace:** $P(A) = \\frac{|A|}{|\Omega|}$ (nur bei *gleich wahrscheinlichen* Ausgängen).
            """,
            "en": """
            - **$\Omega$ (Sample Space):** Set of all possible outcomes.
            - **$\mathcal{F}$ (Event Space):** Set of all measurable events.
            - **$P$ (Probability Measure):** Assigns a number $[0,1]$ to every event.
            - **Laplace:** $P(A) = \\frac{|A|}{|\Omega|}$ (only for *equally likely* outcomes).
            """
        },
        "rules_title": {"de": "Rechenregeln", "en": "Calculation Rules"},
        "rules_content": {
            "de": """
            - **Komplement:** $P(A^c) = 1 - P(A)$
            - **Additionssatz:** $P(A \cup B) = P(A) + P(B) - P(A \cap B)$
            - **Bedingte Wsk:** $P(A|B) = \\frac{P(A \cap B)}{P(B)}$
            - **Unabhängigkeit:** $P(A \cap B) = P(A) \cdot P(B)$ (oder $P(A|B) = P(A)$)
            """,
            "en": """
            - **Complement:** $P(A^c) = 1 - P(A)$
            - **Addition Law:** $P(A \cup B) = P(A) + P(B) - P(A \cap B)$
            - **Conditional Prob:** $P(A|B) = \\frac{P(A \cap B)}{P(B)}$
            - **Independence:** $P(A \cap B) = P(A) \cdot P(B)$ (or $P(A|B) = P(A)$)
            """
        },
        "bayes_title": {"de": "Satz von Bayes", "en": "Bayes' Theorem"},
        "bayes_content": {
            "de": """
            - **Totale Wsk:** $P(B) = \sum P(B|A_i)P(A_i)$
            - **Bayes:** $P(A_k|B) = \\frac{P(B|A_k)P(A_k)}{P(B)}$
            - **Update:** Priori $\\to$ Daten $\\to$ Posteriori
            """,
            "en": """
            - **Total Prob:** $P(B) = \sum P(B|A_i)P(A_i)$
            - **Bayes:** $P(A_k|B) = \\frac{P(B|A_k)P(A_k)}{P(B)}$
            - **Update:** Prior $\\to$ Data $\\to$ Posterior
            """
        }
    },
    "exam_title": {"de": "The Final Exam", "en": "The Final Exam"},
    "levels": {
        "1": {"title": "Level 1: Total Probability"},
        "2": {"title": "Level 2: Bayes Basic"},
        "3": {"title": "Level 3: Bayesian Search"},
        "4": {"title": "Level 4: Monty Hall"},
        "5": {"title": "Level 5: Independence Check"},
        "6": {"title": "Level 6: Combinatorics (Urn)"}
    },
    "questions": {
        "l1": {
            "q": {"de": "Wetter: P(Sonne)=0.6. Wenn Sonne: 90% Gute Laune. Wenn Regen: 30% Gute Laune. Wahrscheinlichkeit für Gute Laune?",
                  "en": "Weather: P(Sun)=0.6. If Sun: 90% Good Mood. If Rain: 30% Good Mood. Probability of Good Mood?"},
            "opts": ["60%", "66%", "54%", "90%"],
            "correct_idx": 1,
            "sol": {"de": "$0.9\\cdot0.6 + 0.3\\cdot0.4 = 0.54 + 0.12 = 0.66$", "en": "$0.9\\cdot0.6 + 0.3\\cdot0.4 = 0.54 + 0.12 = 0.66$"},
            "err": {"de": "Hast du den Regen (40%) vergessen?", "en": "Did you forget the rain (40%)?"}
        },
        "l2": {
            "q": {"de": "Qualität: M1 (20% Anteil, 5% Fehler), M2 (80% Anteil, 1% Fehler). Ein Teil ist defekt. Wahrscheinlichkeit, dass es von M1 kommt?", 
                  "en": "Quality: M1 (20% share, 5% error), M2 (80% share, 1% error). Part is defective. Probability it's from M1?"},
            "opts": ["20%", "55.5%", "80%", "5%"],
            "correct_idx": 1,
            "sol": {"de": "P(M1|D) = (0.05*0.2) / 0.018 ≈ 55.5%. Beachte: Obwohl M1 klein ist, macht sie die meisten Fehler!", "en": "P(M1|D) = (0.05*0.2) / 0.018 ≈ 55.5%. Note: Although M1 is small, it makes most errors!"},
            "err": {"de": "Base Rate Fallacy! Die Fehlerquote von M1 ist 5x höher.", "en": "Base Rate Fallacy! M1's error rate is 5x higher."}
        },
        "l3": {
            "q": {"de": "Priors: A=0.2, B=0.3, C=0.5. Suche in C erfolglos. Neue Wahrscheinlichkeit für A?",
                  "en": "Priors: A=0.2, B=0.3, C=0.5. Search in C unsuccessful. New probability for A?"},
            "opts": ["0.2", "0.4", "0.33", "0.5"],
            "correct_idx": 1,
            "sol": {"de": "C fällt weg. A und B verdoppeln sich proportional. A war 0.2, Summe (A+B) = 0.5. P(A|notC) = 0.2/0.5 = 0.4.",
                    "en": "C is gone. A and B double proportionally. A was 0.2, Sum (A+B) = 0.5. P(A|notC) = 0.2/0.5 = 0.4."},
            "err": {"de": "Normiere auf die verbleibende Summe (0.5).", "en": "Normalize to the remaining sum (0.5)."}
        },
        "l4": {
            "q": {"de": "4 Türen. Du wählst Tür 1. Monty öffnet Tür 2 (Ziege). Wechseln? Wie hoch ist die Chance?",
                  "en": "4 Doors. You pick Door 1. Monty opens Door 2 (Goat). Switch? What is the chance?"},
            "opts": ["33% (Egal)", "37.5% (Wechseln)", "50% (Wechseln)", "25% (Bleiben)"],
            "correct_idx": 1,
            "sol": {"de": "Tür 1: 1/4. Rest: 3/4. Monty eliminiert Tür 2. Die 3/4 verteilen sich auf Tür 3 & 4. Jede hat 3/8 = 37.5%.",
                    "en": "Door 1: 1/4. Rest: 3/4. Monty eliminates Door 2. The 3/4 split to Door 3 & 4. Each has 3/8 = 37.5%."},
            "err": {"de": "Die 3/4 der 'Anderen' werden auf weniger Türen konzentriert.", "en": "The 3/4 of the 'Others' concentrate on fewer doors."}
        },
        "l5": {
            "q": {"de": "A wirft Kopf (50%). B wirft Zahl (50%). Sind die Ereignisse unabhängig?",
                  "en": "A flips Heads (50%). B flips Tails (50%). Are the events independent?"},
            "opts": ["Nein", "Ja", "Nur bei fairen Münzen", "Nicht entscheidbar"],
            "correct_idx": 1,
            "sol": {"de": "Ja. Das Ergebnis von A beeinflusst B physikalisch nicht. P(A und B) = P(A)*P(B).", "en": "Yes. A's result does not physically affect B. P(A and B) = P(A)*P(B)."},
            "err": {"de": "Kausalität! Beeinflusst der eine Wurf den anderen?", "en": "Causality! Does one flip affect the other?"}
        },
        "l6": {
            "q": {"de": "Urne mit 3 Roten, 2 Blauen. Ziehen *ohne* Zurücklegen. P(2. Zug Rot | 1. Zug Rot)?",
                  "en": "Urn with 3 Red, 2 Blue. Draw *without* replacement. P(2nd Draw Red | 1st Draw Red)?"},
            "opts": ["3/5", "2/4 (50%)", "3/4", "2/5"],
            "correct_idx": 1,
            "sol": {"de": "Nach 1. Zug Rot sind noch 2 Rote und 2 Blaue übrig. Total 4. Also 2/4 = 0.5.", "en": "After 1st Red, 2 Red and 2 Blue left. Total 4. So 2/4 = 0.5."},
            "err": {"de": "Der Zustand der Urne hat sich geändert (Gedächtnis!).", "en": "The state of the urn has changed (Memory!)."}
        }
    }
}

def render_subtopic_1_summary(model):
    """1.10 Summary & Exam"""
    
    st.header(t(content_1_10["title"]))
    st.caption(t(content_1_10["intro"]))
    
    # --- CHEAT SHEET ---
    st.markdown("### 📝 Cheat Sheet")
    
    with st.container(border=True):
        st.subheader(f"{render_icon('info', color='#555')} {t(content_1_10['cheat_sheet']['def_title'])}")
        st.markdown(t(content_1_10["cheat_sheet"]["def_content"]))
        st.info(t({
            "de": "💡 **Aha-Moment:** In stetigen Räumen (wie der Dartscheibe) haben Punkte keine Fläche. Nur 'Sektoren' haben Gewicht!",
            "en": "💡 **Aha! Moment:** In continuous spaces (like the dartboard), points have no area. Only 'sectors' have weight!"
        }))

    with st.container(border=True):
        st.subheader(f"{render_icon('combine', color='#555')} {t(content_1_10['cheat_sheet']['rules_title'])}")
        st.markdown(t(content_1_10["cheat_sheet"]["rules_content"]))
        st.warning(t({
            "de": "⚠️ **Kardinalfehler:** Vergiss nie $P(A \cap B)$ beim Additionssatz abzuziehen, sonst zählst du die Überschneidung doppelt!",
            "en": "⚠️ **Cardinal Sin:** Never forget to subtract $P(A \cap B)$ in the Addition Law, or you'll count the overlap twice!"
        }))

    with st.container(border=True):
        st.subheader(f"{render_icon('microscope', color='#555')} {t(content_1_10['cheat_sheet']['bayes_title'])}")
        st.markdown(t(content_1_10["cheat_sheet"]["bayes_content"]))
        st.success(t({
            "de": "🔍 **Bayes-Geheimnis:** Neue Daten ändern nicht die Realität, sondern unser Wissen darüber. Update complete.",
            "en": "🔍 **Bayes Secret:** New data doesn't change reality, it changes our knowledge of it. Update complete."
        }))
        
    st.markdown("---")
    
    # --- FINAL EXAM ---
    # --- MISSION BRIEFING ---
    st.info(t({
        "de": "🎯 **Mission Briefing:** Diese Prüfung deckt alle 6 Konzepte von Modul 1 ab. Du brauchst 100% zum Bestehen!",
        "en": "🎯 **Mission Briefing:** This exam covers all 6 concepts of Module 1. You need 100% to pass!"
    }))
    
    levels = ["1", "2", "3", "4", "5", "6"]
    
    # Render all levels
    for lvl in levels:
        q_id = f"l{lvl}"
        q_data = content_1_10["questions"][q_id]
        with st.expander(content_1_10["levels"][lvl]["title"]):
             render_mcq(
                key_suffix=f"1_10_{q_id}",
                question_text=t(q_data["q"]),
                options=q_data["opts"],
                correct_idx=q_data.get("correct_idx", 1),
                solution_text_dict=q_data["sol"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict=q_data["err"],
                model=model,
                ai_context=f"Module 1 Final Exam - Level {lvl}",
                course_id="vwl", topic_id="1", subtopic_id="1.10", question_id=f"exam_{q_id}"
            )

    # Note on Level 5 index: 
    # Opts: ["Ja", "Nein"...]. Correct is Ja (Idx 0). loop uses `correct_idx=1`.
    # I must fix L5 options in the dict above to ["Nein", "Ja"] to match the loop, or pass idx.
    # Actually, better to explicitly pass idx for each.
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button(t({"de": "Prüfung Abgeben 🎉", "en": "Submit Exam 🎉"})):
        st.balloons()

