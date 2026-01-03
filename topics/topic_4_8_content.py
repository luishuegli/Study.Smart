# Topic 4.8: Hypergeometric Distribution - Hypergeometrische Verteilung
# ULTRATHINK ENHANCED VERSION - "Stupid Person Check" Compliant
import streamlit as st
from views.styles import inject_equal_height_css
from utils.localization import t
from utils.quiz_helper import render_mcq
from data.exam_questions import get_question

# ==========================================
# 1. CONTENT DICTIONARY - BILINGUAL (ULTRATHINK)
# ==========================================
content_4_8 = {
    "title": {"de": "4.8 Hypergeometrische Verteilung", "en": "4.8 Hypergeometric Distribution"},
    "subtitle": {"de": "Ziehen ohne Zurücklegen", "en": "Drawing Without Replacement"},
    
    # --- INTUITION HOOK ---
    "intuition": {
        "header": {"de": "Die Intuition", "en": "The Intuition"},
        "text": {
            "de": "Eine Urne mit <strong>roten und weissen Kugeln</strong>. Du ziehst mehrere Kugeln <strong>OHNE Zurücklegen</strong>. Wie viele rote Kugeln wirst du ziehen? Jede Ziehung verändert die Zusammensetzung der Urne — deshalb sind die Züge <strong>abhängig</strong>!",
            "en": "An urn with <strong>red and white balls</strong>. You draw several balls <strong>WITHOUT replacement</strong>. How many red balls will you draw? Each draw changes the composition of the urn — that's why the draws are <strong>dependent</strong>!"
        },
        "key_insight": {
            "de": "Der Schlüssel: 'Ohne Zurücklegen' bedeutet, dass die Wahrscheinlichkeit sich bei jeder Ziehung <strong>ändert</strong>. Deshalb können wir nicht einfach Binomial verwenden!",
            "en": "The key: 'Without replacement' means the probability <strong>changes</strong> with each draw. That's why we can't simply use Binomial!"
        }
    },
    
    # --- FRAG DICH (Decision Guide) ---
    "frag_dich": {
        "header": {"de": "Frag dich: Ist es Hypergeometrisch?", "en": "Ask yourself: Is it Hypergeometric?"},
        "questions": [
            {"de": "Ziehe ich <strong>ohne Zurücklegen</strong>?", "en": "Am I drawing <strong>without replacement</strong>?"},
            {"de": "Ist die Population <strong>endlich</strong> (bekannte Grösse N)?", "en": "Is the population <strong>finite</strong> (known size N)?"},
            {"de": "Zähle ich eine bestimmte <strong>Kategorie</strong> (z.B. 'rote Kugeln')?", "en": "Am I counting a specific <strong>category</strong> (e.g., 'red balls')?"},
            {"de": "Kenne ich, wie viele 'Erfolge' es in der Population gibt (M)?", "en": "Do I know how many 'successes' are in the population (M)?"}
        ],
        "conclusion": {"de": "Alles Ja → Hypergeometrisch!", "en": "All Yes → Hypergeometric!"}
    },
    
    # --- DEFINITION ---
    "definition": {
        "header": {"de": "Definition", "en": "Definition"},
        "text": {
            "de": "Eine Zufallsvariable X heisst <strong>hypergeometrisch verteilt</strong>, wenn sie die Anzahl der 'Erfolge' bei n Ziehungen <strong>ohne Zurücklegen</strong> aus einer Urne mit N Elementen (davon M 'Erfolge') zählt.",
            "en": "A random variable X is called <strong>hypergeometrically distributed</strong> if it counts the number of 'successes' in n draws <strong>without replacement</strong> from an urn with N elements (of which M are 'successes')."
        },
        "notation": r"X \sim \text{Hyp}(N, M, n)"
    },
    
    # --- PARAMETERS WITH MEANING ---
    "parameters": {
        "header": {"de": "Die Parameter verstehen", "en": "Understanding the Parameters"},
        "params": {
            "N": {
                "symbol": "N",
                "name_de": "Gesamtpopulation",
                "name_en": "Total population",
                "meaning_de": "Wie viele Kugeln sind <strong>insgesamt</strong> in der Urne? (Rote + Weisse)",
                "meaning_en": "How many balls are in the urn <strong>in total</strong>? (Red + White)",
                "example_de": "N = 52 (Kartenspiel)",
                "example_en": "N = 52 (deck of cards)"
            },
            "M": {
                "symbol": "M",
                "name_de": "Anzahl 'Erfolge' in Population",
                "name_en": "Number of 'successes' in population",
                "meaning_de": "Wie viele <strong>rote Kugeln</strong> (= die Kategorie, die wir zählen wollen)?",
                "meaning_en": "How many <strong>red balls</strong> (= the category we want to count)?",
                "example_de": "M = 13 (Herz-Karten)",
                "example_en": "M = 13 (heart cards)"
            },
            "n": {
                "symbol": "n",
                "name_de": "Stichprobengrösse",
                "name_en": "Sample size",
                "meaning_de": "Wie viele Kugeln <strong>ziehen</strong> wir insgesamt?",
                "meaning_en": "How many balls do we <strong>draw</strong> in total?",
                "example_de": "n = 5 (5 Karten ziehen)",
                "example_en": "n = 5 (draw 5 cards)"
            }
        }
    },
    
    # --- THE FORMULA WITH BREAKDOWN ---
    "formula": {
        "header": {"de": "Die Formel verstehen", "en": "Understanding the Formula"},
        "pmf": r"P(X = x) = \frac{\binom{M}{x} \cdot \binom{N-M}{n-x}}{\binom{N}{n}}",
        "breakdown": {
            "header": {"de": "Schritt-für-Schritt Erklärung", "en": "Step-by-step Explanation"},
            "numerator1": {
                "formula": r"\binom{M}{x}",
                "de": "Auf wie viele Arten kann ich <strong>x rote Kugeln</strong> aus M roten wählen?",
                "en": "In how many ways can I choose <strong>x red balls</strong> from M red ones?"
            },
            "numerator2": {
                "formula": r"\binom{N-M}{n-x}",
                "de": "Auf wie viele Arten kann ich <strong>die restlichen (n-x) weissen</strong> aus (N-M) weissen wählen?",
                "en": "In how many ways can I choose <strong>the remaining (n-x) white</strong> from (N-M) white ones?"
            },
            "denominator": {
                "formula": r"\binom{N}{n}",
                "de": "Wie viele <strong>Kombinationen insgesamt</strong> gibt es, n Kugeln aus N zu wählen?",
                "en": "How many <strong>total combinations</strong> are there to choose n balls from N?"
            },
            "summary": {
                "de": "<strong>Formel-Logik:</strong> Günstige × Günstige / Alle = (Anzahl Wege, x Rote zu bekommen) × (Anzahl Wege, Rest Weisse zu bekommen) / (Alle möglichen Ziehungen)",
                "en": "<strong>Formula logic:</strong> Favorable × Favorable / All = (Ways to get x red) × (Ways to get remaining white) / (All possible draws)"
            }
        }
    },
    
    # --- MOMENTS WITH INTERPRETATION ---
    "moments": {
        "header": {"de": "Erwartungswert & Varianz", "en": "Expected Value & Variance"},
        "expectation": {
            "title_de": "Erwartungswert",
            "title_en": "Expected Value",
            "formula": r"E[X] = n \cdot \frac{M}{N}",
            "interpretation_de": "Stichprobengrösse × Anteil der 'Erfolge' in der Population. Logisch: Wenn 50% der Kugeln rot sind und ich 10 ziehe, erwarte ich 5 rote.",
            "interpretation_en": "Sample size × proportion of 'successes' in population. Logical: If 50% of balls are red and I draw 10, I expect 5 red ones."
        },
        "variance": {
            "title_de": "Varianz",
            "title_en": "Variance",
            "formula": r"V(X) = n \cdot \frac{M}{N} \cdot \frac{N-M}{N} \cdot \frac{N-n}{N-1}",
            "interpretation_de": "Der letzte Faktor (N-n)/(N-1) heisst <strong>Endlichkeitskorrektur</strong>. Er reduziert die Varianz, weil wir ohne Zurücklegen ziehen!",
            "interpretation_en": "The last factor (N-n)/(N-1) is called <strong>finite population correction</strong>. It reduces variance because we draw without replacement!"
        }
    },
    
    # --- WORKED EXAMPLE ---
    "example_worked": {
        "header": {"de": "Schritt-für-Schritt Beispiel", "en": "Step-by-Step Example"},
        "problem": {
            "de": "Eine Urne enthält <strong>10 Kugeln</strong>: 4 rote und 6 weisse. Du ziehst <strong>3 Kugeln ohne Zurücklegen</strong>. Wie wahrscheinlich ist es, <strong>genau 2 rote</strong> zu ziehen?",
            "en": "An urn contains <strong>10 balls</strong>: 4 red and 6 white. You draw <strong>3 balls without replacement</strong>. What's the probability of drawing <strong>exactly 2 red</strong>?"
        },
        "steps": [
            {
                "label": {"de": "Gegeben", "en": "Given"},
                "latex": r"{\color{#007AFF}N = 10}, \quad {\color{#FF4B4B}M = 4}, \quad {\color{#007AFF}n = 3}, \quad {\color{#FF4B4B}x = 2}",
                "note": {"de": "(Gesamt, Rot, Ziehungen, Gesucht)", "en": "(Total, Red, Draws, Wanted)"}
            },
            {
                "label": {"de": "Zähler Teil 1", "en": "Numerator Part 1"},
                "latex": r"\binom{\color{#FF4B4B}M}{\color{#FF4B4B}x} = \binom{\color{#FF4B4B}4}{\color{#FF4B4B}2} = 6",
                "note": {"de": "Wege, 2 Rote aus 4 zu wählen", "en": "ways to choose 2 red from 4"}
            },
            {
                "label": {"de": "Zähler Teil 2", "en": "Numerator Part 2"},
                "latex": r"\binom{\color{#6B7280}N-M}{\color{#6B7280}n-x} = \binom{\color{#6B7280}6}{\color{#6B7280}1} = 6",
                "note": {"de": "Wege, 1 Weisse aus 6 zu wählen", "en": "ways to choose 1 white from 6"}
            },
            {
                "label": {"de": "Nenner", "en": "Denominator"},
                "latex": r"\binom{\color{#007AFF}N}{\color{#007AFF}n} = \binom{\color{#007AFF}10}{\color{#007AFF}3} = 120",
                "note": {"de": "Alle möglichen Ziehungen", "en": "All possible draws"}
            },
            {
                "label": {"de": "Ergebnis", "en": "Result"},
                "latex": r"P(X=2) = \frac{6 \times 6}{120} = \frac{36}{120} = \mathbf{0.3 = 30\%}",
                "note": None
            }
        ],
        "check": {
            "de": "<strong>Plausibilitäts-Check:</strong> 30% klingt vernünftig — nicht zu hoch (nur 4 von 10 sind rot), nicht zu niedrig (wir ziehen 3).",
            "en": "<strong>Plausibility check:</strong> 30% sounds reasonable — not too high (only 4 of 10 are red), not too low (we draw 3)."
        }
    },
    
    # --- EXAM ESSENTIALS (Merged Trap + Pro Tip) ---
    "exam_essentials": {
        "header": {"de": "Prüfungs-Essentials", "en": "Exam Essentials"},
        "items": [
            {
                "label": {"de": "Falle", "en": "Trap"},
                "title": {"de": "Parameter verwechseln!", "en": "Confusing parameters!"},
                "content": {
                    "de": "N = Gesamtpopulation, M = Erfolge in Population, n = Stichprobe.<br><em>Merke:</em> N (Gross) = alles, M (Mittel) = Erfolge, n (klein) = was wir ziehen",
                    "en": "N = total population, M = successes in population, n = sample.<br><em>Remember:</em> N (big) = everything, M (medium) = successes, n (small) = what we draw"
                },
                "type": "warning"
            },
            {
                "label": {"de": "Signal", "en": "Signal"},
                "title": {"de": "'Ohne Zurücklegen' → Hypergeometrisch", "en": "'Without replacement' → Hypergeometric"},
                "content": {
                    "de": "Das Schlüsselwort! Ohne Zurücklegen = abhängige Ziehungen. Zusammensetzung ändert sich.",
                    "en": "The keyword! Without replacement = dependent draws. Composition changes."
                },
                "type": "tip"
            },
            {
                "label": {"de": "Formel", "en": "Formula"},
                "title": {"de": "(Günstige Rote) × (Günstige Weisse) / (Alle)", "en": "(Favorable red) × (Favorable white) / (All)"},
                "content": {
                    "de": "Wie viele Wege, x Rote UND (n-x) Weisse zu ziehen, geteilt durch alle möglichen Ziehungen.",
                    "en": "How many ways to draw x red AND (n-x) white, divided by all possible draws."
                },
                "type": "tip"
            },
            {
                "label": {"de": "Shortcut", "en": "Shortcut"},
                "title": {"de": "n < 0.05×N → Binomial benutzen", "en": "n < 0.05×N → Use Binomial"},
                "content": {
                    "de": "Bei grosser Population und kleiner Stichprobe ist der Unterschied vernachlässigbar. Spart Zeit!",
                    "en": "With large population and small sample, the difference is negligible. Saves time!"
                },
                "type": "tip"
            }
        ]
    }
}


def render_subtopic_4_8(model):
    """4.8 Hypergeometrische Verteilung - ULTRATHINK Enhanced with Stupid Person Check"""
    inject_equal_height_css()
    
    # --- CSS INJECTION FOR EQUAL HEIGHT (AGGRESSIVE) ---
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
    
    /* Target the vertical block inside columns */
    [data-testid="column"] [data-testid="stVerticalBlock"],
    [data-testid="stColumn"] [data-testid="stVerticalBlock"] {
        flex: 1 !important;
        display: flex !important;
        flex-direction: column !important;
        height: 100% !important;
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
    
    /* Also target any container with border=True */
    .stContainer, [data-testid="stContainer"] {
        height: 100% !important;
        flex: 1 !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # --- HEADER ---
    st.header(t(content_4_8["title"]))
    st.caption(t(content_4_8["subtitle"]))
    st.markdown("---")
    
    # --- INTUITION HOOK ---
    st.markdown(f"### {t(content_4_8['intuition']['header'])}")
    with st.container(border=True):
        st.markdown(t(content_4_8["intuition"]["text"]), unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        key_insight = t(content_4_8["intuition"]["key_insight"])
        st.markdown(f"""
<div style="background: #f4f4f5; border-left: 4px solid #a1a1aa; padding: 12px 16px; border-radius: 8px; color: #3f3f46;">
{key_insight}
</div>
""", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- FRAG DICH: DECISION GUIDE ---
    from utils.ask_yourself import render_ask_yourself
    render_ask_yourself(
        header=content_4_8['frag_dich']['header'],
        questions=content_4_8['frag_dich']['questions'],
        conclusion=content_4_8['frag_dich']['conclusion']
    )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- DEFINITION ---
    st.markdown(f"### {t(content_4_8['definition']['header'])}")
    with st.container(border=True):
        st.markdown(t(content_4_8["definition"]["text"]), unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        st.latex(content_4_8["definition"]["notation"])
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- PARAMETERS ---
    st.markdown(f"### {t(content_4_8['parameters']['header'])}")
    
    cols = st.columns(3, gap="medium")
    for i, (key, param) in enumerate(content_4_8["parameters"]["params"].items()):
        with cols[i]:
            with st.container(border=True):
                st.markdown(f"**{param['symbol']}** — {t({'de': param['name_de'], 'en': param['name_en']})}")
                st.markdown(t({"de": param["meaning_de"], "en": param["meaning_en"]}), unsafe_allow_html=True)
                st.caption(t({"de": param["example_de"], "en": param["example_en"]}))
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- FORMULA WITH BREAKDOWN ---
    st.markdown(f"### {t(content_4_8['formula']['header'])}")
    with st.container(border=True):
        st.latex(content_4_8["formula"]["pmf"])
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(f"**{t(content_4_8['formula']['breakdown']['header'])}**")
        
        breakdown = content_4_8["formula"]["breakdown"]
        
        col_n1, col_n2, col_d = st.columns(3)
        with col_n1:
            st.latex(breakdown["numerator1"]["formula"])
            st.markdown(f"<small style='color:#6b7280;'>{t({'de': breakdown['numerator1']['de'], 'en': breakdown['numerator1']['en']})}</small>", unsafe_allow_html=True)
        with col_n2:
            st.latex(breakdown["numerator2"]["formula"])
            st.markdown(f"<small style='color:#6b7280;'>{t({'de': breakdown['numerator2']['de'], 'en': breakdown['numerator2']['en']})}</small>", unsafe_allow_html=True)
        with col_d:
            st.latex(breakdown["denominator"]["formula"])
            st.markdown(f"<small style='color:#6b7280;'>{t({'de': breakdown['denominator']['de'], 'en': breakdown['denominator']['en']})}</small>", unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        summary_text = t(breakdown["summary"])
        st.markdown(f"""
<div style="background: #f4f4f5; border-left: 4px solid #a1a1aa; padding: 12px 16px; border-radius: 8px; color: #3f3f46;">
{summary_text}
</div>
""", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- MOMENTS ---
    st.markdown(f"### {t(content_4_8['moments']['header'])}")
    
    col_e, col_v = st.columns(2, gap="medium")
    
    with col_e:
        with st.container(border=True):
            st.markdown(f"**{t({'de': content_4_8['moments']['expectation']['title_de'], 'en': content_4_8['moments']['expectation']['title_en']})}**")
            st.latex(content_4_8["moments"]["expectation"]["formula"])
            st.markdown("---")
            st.caption(t({"de": content_4_8["moments"]["expectation"]["interpretation_de"], "en": content_4_8["moments"]["expectation"]["interpretation_en"]}))
    
    with col_v:
        with st.container(border=True):
            st.markdown(f"**{t({'de': content_4_8['moments']['variance']['title_de'], 'en': content_4_8['moments']['variance']['title_en']})}**")
            st.latex(content_4_8["moments"]["variance"]["formula"])
            st.markdown("---")
            st.caption(t({"de": content_4_8["moments"]["variance"]["interpretation_de"], "en": content_4_8["moments"]["variance"]["interpretation_en"]}))
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- WORKED EXAMPLE ---
    st.markdown(f"### {t(content_4_8['example_worked']['header'])}")
    with st.container(border=True):
        
        st.markdown(t(content_4_8['example_worked']['problem']), unsafe_allow_html=True)
        
        st.markdown("---")
        
        for i, step in enumerate(content_4_8["example_worked"]["steps"]):
            if i > 0:
                st.markdown("---")
            st.markdown(f"**{t(step['label'])}:**")
            st.latex(step["latex"])
            if step.get("note"):
                st.caption(t(step["note"]))
        
        st.markdown("---")
        check_text = t(content_4_8['example_worked']['check'])
        st.markdown(f"""
<div style="background-color: #f4f4f5; border-radius: 8px; padding: 12px; border-left: 4px solid #a1a1aa; color: #3f3f46;">
{check_text}
</div>""", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- EXAM ESSENTIALS (Using Utility) ---
    from utils.exam_essentials import render_exam_essentials
    render_exam_essentials(items=content_4_8["exam_essentials"]["items"])
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- EXAM SECTION ---
    st.markdown(f"### {t({'de': 'Prüfungstraining', 'en': 'Exam Practice'})}")
    
    q_data = get_question("4.8", "hypergeom_10_5_3")
    if q_data:
        with st.container(border=True):
            st.caption(q_data.get("source", ""))
            opts = q_data.get("options", [])
            option_labels = [t(o) if isinstance(o, dict) else o for o in opts]
            render_mcq(
                key_suffix="4_8_hyp", question_text=t(q_data["question"]),
                options=option_labels, correct_idx=q_data["correct_idx"],
                solution_text_dict=q_data["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
                client=model, ai_context="Hypergeometric distribution",
                course_id="vwl", topic_id="4", subtopic_id="4.8", question_id="4_8_hyp"
            )
    else:
        with st.container(border=True):
            st.markdown(f"""
<div style="background: #f4f4f5; border-left: 4px solid #a1a1aa; padding: 12px 16px; border-radius: 8px; color: #3f3f46;">
{t({"de": "Keine MCQ-Fragen verfügbar.", "en": "No MCQ questions available."})}
</div>
""", unsafe_allow_html=True)
