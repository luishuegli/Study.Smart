# Topic 4.9: Summary — Stochastic Models & Distributions
# ULTRATHINK REDESIGN: Compact Cards + Learn-Test-Learn Flow
import streamlit as st
from views.styles import inject_equal_height_css
from utils.localization import t
from utils.quiz_helper import render_mcq
from utils.ask_yourself import render_ask_yourself
from utils.exam_essentials import render_exam_essentials
from data.exam_questions import get_question

# ==========================================
# 1. CONTENT DICTIONARY - CHUNKED BY CONCEPT
# ==========================================
content_4_9 = {
    "title": {"de": "4.9 Zusammenfassung", "en": "4.9 Summary"},
    "subtitle": {"de": "Alle Verteilungen im Überblick", "en": "All Distributions at a Glance"},
    
    # --- CHAPTER INTUITION ---
    "intuition": {
        "header": {"de": "Die Intuition", "en": "The Intuition"},
        "text": {
            "de": "In diesem Kapitel hast du die **Familie der Verteilungen** kennengelernt — von diskret (Binomial, Poisson, Hypergeometrisch) bis stetig (Normal, Exponential, Rechteck). Diese Zusammenfassung zeigt dir, **wann du welche Verteilung benutzt** und die häufigsten Prüfungsfallen.",
            "en": "This chapter introduced you to the **family of distributions** — from discrete (Binomial, Poisson, Hypergeometric) to continuous (Normal, Exponential, Rectangular). This summary shows you **when to use which distribution** and the most common exam traps."
        }
    },
    
    # === CHUNK 1: COUNTING DISTRIBUTIONS ===
    "chunk_counting": {
        "header": {"de": "Zähl-Verteilungen", "en": "Counting Distributions"},
        "cards": [
            {"name": "Bernoulli", "notation": "X ~ Ber(p)", "oneliner": {"de": "Ein Versuch", "en": "One trial"}},
            {"name": "Binomial", "notation": "X ~ Bi(n, p)", "oneliner": {"de": "n Versuche, MIT Zurücklegen", "en": "n trials, WITH replacement"}},
            {"name": {"de": "Gleichförmig", "en": "Uniform"}, "notation": "X ~ Gleich(m)", "oneliner": {"de": "Alle m gleich wahrscheinlich", "en": "All m equally likely"}}
        ],
        "mcq": {
            "question": {"de": "Du wirfst eine Münze 10 Mal und zählst Köpfe. Welche Verteilung?", "en": "You flip a coin 10 times and count heads. Which distribution?"},
            "options": [
                {"de": "Bernoulli", "en": "Bernoulli"},
                {"de": "Binomial", "en": "Binomial"},
                {"de": "Poisson", "en": "Poisson"}
            ],
            "correct_idx": 1,
            "solution": {"de": "Binomial! n = 10 Versuche, jeder mit p = 0.5. Bernoulli wäre nur EIN Wurf.", "en": "Binomial! n = 10 trials, each with p = 0.5. Bernoulli would be just ONE flip."}
        }
    },
    
    # === CHUNK 2: RATE-BASED DISTRIBUTIONS ===
    "chunk_rates": {
        "header": {"de": "Raten-Verteilungen", "en": "Rate-Based Distributions"},
        "cards": [
            {"name": "Poisson", "notation": "X ~ Po(λ)", "oneliner": {"de": "Ereignisse pro Zeiteinheit", "en": "Events per time unit"}},
            {"name": {"de": "Hypergeometrisch", "en": "Hypergeometric"}, "notation": "X ~ Hyp(N,M,n)", "oneliner": {"de": "OHNE Zurücklegen", "en": "WITHOUT replacement"}}
        ],
        "mcq": {
            "question": {"de": "'Eine Loskiste mit 100 Losen, 20 Gewinne. Du ziehst 5 ohne Zurücklegen.' — Welche Verteilung?", "en": "'A lottery box with 100 tickets, 20 winners. You draw 5 without replacement.' — Which distribution?"},
            "options": [
                {"de": "Binomial", "en": "Binomial"},
                {"de": "Hypergeometrisch", "en": "Hypergeometric"},
                {"de": "Poisson", "en": "Poisson"}
            ],
            "correct_idx": 1,
            "solution": {"de": "Hypergeometrisch! 'Ohne Zurücklegen' = H. Mit Zurücklegen wäre Binomial.", "en": "Hypergeometric! 'Without replacement' = H. With replacement would be Binomial."}
        }
    },
    
    # === CHUNK 3: CONTINUOUS DISTRIBUTIONS ===
    "chunk_continuous": {
        "header": {"de": "Stetige Verteilungen", "en": "Continuous Distributions"},
        "cards": [
            {"name": {"de": "Rechteck", "en": "Rectangular"}, "notation": "X ~ R(a,b)", "oneliner": {"de": "Überall gleich in [a,b]", "en": "Equal everywhere in [a,b]"}},
            {"name": "Exponential", "notation": "X ~ Ex(λ)", "oneliner": {"de": "Wartezeit bis Ereignis", "en": "Time until event"}},
            {"name": "Normal", "notation": "X ~ N(μ,σ²)", "oneliner": {"de": "Glockenform, natürlich", "en": "Bell curve, natural"}}
        ],
        "mcq": {
            "question": {"de": "'Die durchschnittliche Lebensdauer einer Maschine beträgt 5000 Stunden.' — Welche Verteilung für die Lebensdauer?", "en": "'The average lifespan of a machine is 5000 hours.' — Which distribution for lifespan?"},
            "options": [
                {"de": "Normal", "en": "Normal"},
                {"de": "Exponential", "en": "Exponential"},
                {"de": "Rechteck", "en": "Rectangular"}
            ],
            "correct_idx": 1,
            "solution": {"de": "Exponential! 'Lebensdauer/Wartezeit bis...' = klassisches Exponential-Signal. E[X] = 1/λ.", "en": "Exponential! 'Lifespan/time until...' = classic Exponential signal. E[X] = 1/λ."}
        }
    },
    
    # === KEY FORMULAS ===
    "key_formulas": {
        "header": {"de": "Die wichtigsten Formeln", "en": "The Key Formulas"},
        "formulas": [
            {"name": "E[X] diskret", "formula": r"\sum_x x \cdot P(X=x)"},
            {"name": "E[X] stetig", "formula": r"\int x \cdot f(x)\,dx"},
            {"name": "Var(X)", "formula": r"E[X^2] - E[X]^2"},
            {"name": "Z-Score", "formula": r"Z = \frac{X - \mu}{\sigma}"}
        ]
    },
    
    # === ASK YOURSELF ===
    "ask_yourself": {
        "header": {"de": "Frag dich selbst", "en": "Ask Yourself"},
        "questions": [
            {"de": "Kannst du alle Verteilungen an ihren Signalwörtern erkennen?", "en": "Can you recognize all distributions by their signal words?"},
            {"de": "Wann benutzt du Binomial vs. Hypergeometrisch?", "en": "When do you use Binomial vs. Hypergeometric?"},
            {"de": "Was ist der Unterschied zwischen λ bei Poisson und Exponential?", "en": "What's the difference between λ in Poisson vs. Exponential?"},
            {"de": "Wie standardisierst du N(μ,σ²) zu N(0,1)?", "en": "How do you standardize N(μ,σ²) to N(0,1)?"}
        ],
        "conclusion": {
            "de": "Wenn du diese Fragen beantworten kannst, bist du bereit für Verteilungs-Aufgaben!",
            "en": "If you can answer these, you're ready for distribution problems!"
        }
    },
    
    # === EXAM ESSENTIALS ===
    "exam_essentials": {
        "tips": [
            {
                "tip": {"de": "'Ohne Zurücklegen' = Sofort Hypergeometrisch", "en": "'Without replacement' = Immediately Hypergeometric"},
                "why": {"de": "Binomial funktioniert nur MIT Zurücklegen!", "en": "Binomial only works WITH replacement!"}
            },
            {
                "tip": {"de": "'Im Durchschnitt X pro Zeiteinheit' = Poisson", "en": "'On average X per time unit' = Poisson"},
                "why": {"de": "Das Signalwort für die Poisson-Verteilung.", "en": "The signal word for Poisson distribution."}
            },
            {
                "tip": {"de": "N(100, 25) → σ² = 25, σ = 5 (NICHT σ = 25!)", "en": "N(100, 25) → σ² = 25, σ = 5 (NOT σ = 25!)"},
                "why": {"de": "Der zweite Parameter ist IMMER die Varianz, nicht σ!", "en": "The second parameter is ALWAYS variance, not σ!"}
            },
            {
                "tip": {"de": "E[X] bei Exponential = 1/λ (nicht λ!)", "en": "E[X] for Exponential = 1/λ (not λ!)"},
                "why": {"de": "Bei Poisson ist λ der Mittelwert, bei Exponential ist es 1/λ.", "en": "For Poisson λ is the mean, for Exponential it's 1/λ."}
            },
            {
                "tip": {"de": "P(X = x) = 0 für ALLE stetigen Verteilungen", "en": "P(X = x) = 0 for ALL continuous distributions"},
                "why": {"de": "Nur Intervalle haben Wahrscheinlichkeit > 0.", "en": "Only intervals have probability > 0."}
            }
        ],
        "trap": {
            "de": "<strong>σ vs σ² Verwirrung:</strong> N(μ, σ²) hat σ² als Parameter! Bei N(100, 25) ist σ = 5, NICHT 25.",
            "en": "<strong>σ vs σ² Confusion:</strong> N(μ, σ²) has σ² as parameter! For N(100, 25), σ = 5, NOT 25."
        },
        "trap_rule": {
            "de": "Immer prüfen: Steht der Parameter für σ oder σ²?",
            "en": "Always check: Does the parameter represent σ or σ²?"
        }
    }
}


def render_subtopic_4_9(model):
    """4.9 Summary — ULTRATHINK Learn-Test-Learn Flow"""
    inject_equal_height_css()
    
    # --- CSS for compact cards ---
    st.markdown("""
    <style>
    [data-testid="stHorizontalBlock"] { align-items: stretch !important; }
    [data-testid="column"] { display: flex !important; flex-direction: column !important; }
    [data-testid="column"] > div { flex: 1 !important; }
    .compact-card {
        background: #f9fafb;
        border: 1px solid #e5e7eb;
        border-radius: 10px;
        padding: 14px;
        text-align: center;
        height: 100%;
    }
    .compact-card .name { font-weight: 700; font-size: 1.05em; margin-bottom: 4px; }
    .compact-card .notation { color: #6b7280; font-family: monospace; font-size: 0.9em; }
    .compact-card .oneliner { color: #374151; font-size: 0.85em; margin-top: 6px; }
    </style>
    """, unsafe_allow_html=True)
    
    st.header(t(content_4_9["title"]))
    st.caption(t(content_4_9["subtitle"]))
    st.markdown("---")
    
    # === CHUNK 1: COUNTING DISTRIBUTIONS ===
    render_chunk(content_4_9["chunk_counting"], "counting", model)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # === CHUNK 2: RATE-BASED DISTRIBUTIONS ===
    render_chunk(content_4_9["chunk_rates"], "rates", model)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # === CHUNK 3: CONTINUOUS DISTRIBUTIONS ===
    render_chunk(content_4_9["chunk_continuous"], "continuous", model)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # === KEY FORMULAS ===
    render_key_formulas()
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # === ASK YOURSELF ===
    render_ask_yourself(
        header=content_4_9["ask_yourself"]["header"],
        questions=content_4_9["ask_yourself"]["questions"],
        conclusion=content_4_9["ask_yourself"]["conclusion"]
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # === EXAM ESSENTIALS ===
    render_exam_essentials(
        tips=content_4_9["exam_essentials"]["tips"],
        trap=content_4_9["exam_essentials"]["trap"],
        trap_rule=content_4_9["exam_essentials"]["trap_rule"]
    )


def render_chunk(chunk, chunk_id, model):
    """Render a chunk: header + compact cards + MCQ"""
    st.markdown(f"### {t(chunk['header'])}")
    
    # Compact cards in a row
    cols = st.columns(len(chunk["cards"]))
    for col, card in zip(cols, chunk["cards"]):
        with col:
            name = t(card["name"]) if isinstance(card["name"], dict) else card["name"]
            oneliner = t(card["oneliner"])
            st.markdown(f"""
            <div class="compact-card">
                <div class="name">{name}</div>
                <div class="notation">{card['notation']}</div>
                <div class="oneliner">{oneliner}</div>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # MCQ immediately after
    mcq = chunk["mcq"]
    opts = [t(o) for o in mcq["options"]]
    
    with st.container(border=True):
        st.markdown(f"🧠 **{t({'de': 'Schnell-Check', 'en': 'Quick Check'})}**")
        render_mcq(
            key_suffix=f"4_9_{chunk_id}",
            question_text=t(mcq["question"]),
            options=opts,
            correct_idx=mcq["correct_idx"],
            solution_text_dict=mcq["solution"],
            success_msg_dict={"de": "Richtig!", "en": "Correct!"},
            error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
            client=model,
            ai_context=f"Distribution summary: {chunk_id} distributions",
            course_id="vwl",
            topic_id="4",
            subtopic_id="4.9",
            question_id=f"4_9_quick_{chunk_id}"
        )


def render_key_formulas():
    """Render key formulas in a compact row"""
    kf = content_4_9["key_formulas"]
    st.markdown(f"### {t(kf['header'])}")
    
    cols = st.columns(len(kf["formulas"]))
    for col, f in zip(cols, kf["formulas"]):
        with col:
            with st.container(border=True):
                st.markdown(f"**{f['name']}**")
                st.latex(f["formula"])
