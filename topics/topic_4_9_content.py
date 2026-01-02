# Topic 4.9: Summary — Stochastic Models & Distributions
import streamlit as st
from views.styles import inject_equal_height_css
from utils.localization import t
from utils.quiz_helper import render_mcq
from data.exam_questions import get_question

# ==========================================
# 1. CONTENT DICTIONARY
# ==========================================
content_4_9 = {
    "title": {"de": "4.9 Zusammenfassung", "en": "4.9 Summary"},
    "subtitle": {"de": "Alle Verteilungen im Überblick", "en": "All Distributions at a Glance"},
    
    # --- DISTRIBUTION CHEAT SHEET ---
    "cheat_sheet": {
        "header": {"de": "Das Verteilungs-Spickzettel", "en": "The Distribution Cheat Sheet"},
        "discrete": {
            "header": {"de": "Diskrete Verteilungen", "en": "Discrete Distributions"},
            "distributions": [
                {
                    "name": {"de": "Gleichförmig", "en": "Uniform"},
                    "notation": "X ~ Gleich(m)",
                    "pmf": "P(X=xᵢ) = 1/m",
                    "params": "m = Anzahl Ausgänge",
                    "use": {"de": "Fairer Würfel, Lotterie", "en": "Fair die, lottery"}
                },
                {
                    "name": {"de": "Bernoulli", "en": "Bernoulli"},
                    "notation": "X ~ Ber(p)",
                    "pmf": "P(X=1) = p",
                    "params": "p ∈ [0,1]",
                    "use": {"de": "Ein Münzwurf, ja/nein", "en": "One coin flip, yes/no"}
                },
                {
                    "name": {"de": "Binomial", "en": "Binomial"},
                    "notation": "X ~ Bi(n, p)",
                    "pmf": "C(n,x) × pˣ × (1-p)ⁿ⁻ˣ",
                    "params": "n = Versuche, p = Erfolgsrate",
                    "use": {"de": "n Münzwürfe mit Zurücklegen", "en": "n coin flips with replacement"}
                },
                {
                    "name": {"de": "Poisson", "en": "Poisson"},
                    "notation": "X ~ Po(λ)",
                    "pmf": "λˣe⁻λ / x!",
                    "params": "λ = mittlere Rate",
                    "use": {"de": "Seltene Ereignisse (Unfälle, Anrufe)", "en": "Rare events (accidents, calls)"}
                },
                {
                    "name": {"de": "Hypergeometrisch", "en": "Hypergeometric"},
                    "notation": "X ~ Hyp(N, M, n)",
                    "pmf": "C(M,x)×C(N-M,n-x) / C(N,n)",
                    "params": "N=Pop, M=Erfolge, n=Stichprobe",
                    "use": {"de": "Ziehen OHNE Zurücklegen", "en": "Drawing WITHOUT replacement"}
                }
            ]
        },
        "continuous": {
            "header": {"de": "Stetige Verteilungen", "en": "Continuous Distributions"},
            "distributions": [
                {
                    "name": {"de": "Rechteck (Stetig Gleich.)", "en": "Rectangular (Cont. Uniform)"},
                    "notation": "X ~ R(a, b)",
                    "pdf": "f(x) = 1/(b-a)",
                    "params": "a = min, b = max",
                    "use": {"de": "Wartezeit am Bus, Position", "en": "Wait at bus, position"}
                },
                {
                    "name": {"de": "Exponential", "en": "Exponential"},
                    "notation": "X ~ Ex(λ)",
                    "pdf": "f(x) = λe⁻λˣ",
                    "params": "λ = Rate, E[X] = 1/λ",
                    "use": {"de": "Lebensdauer, Wartezeit bis Ereignis", "en": "Lifespan, waiting time until event"}
                },
                {
                    "name": {"de": "Normal", "en": "Normal"},
                    "notation": "X ~ N(μ, σ²)",
                    "pdf": "Glockenform",
                    "params": "μ = Zentrum, σ = Streuung",
                    "use": {"de": "Messfehler, Körpergrösse, IQ", "en": "Measurement error, height, IQ"}
                }
            ]
        }
    },
    
    # --- DECISION TREE ---
    "decision_tree": {
        "header": {"de": "Welche Verteilung?", "en": "Which Distribution?"},
        "subtitle": {"de": "Der Entscheidungsbaum", "en": "The Decision Tree"},
        "rules": [
            {"condition": {"de": "Stetig oder Diskret?", "en": "Continuous or Discrete?"}},
            {"condition": {"de": "Mit oder OHNE Zurücklegen?", "en": "With or WITHOUT replacement?"}},
            {"arrow": "OHNE → Hypergeometrisch"},
            {"condition": {"de": "Wie viele Versuche?", "en": "How many trials?"}},
            {"arrow": "n = 1 → Bernoulli"},
            {"arrow": "n > 1 mit p → Binomial"},
            {"condition": {"de": "Seltene Ereignisse über Zeit?", "en": "Rare events over time?"}},
            {"arrow": "→ Poisson"},
            {"condition": {"de": "Wartezeit bis Ereignis?", "en": "Waiting time until event?"}},
            {"arrow": "→ Exponential"},
            {"condition": {"de": "Alles gleichwahrscheinlich in [a,b]?", "en": "Everything equally likely in [a,b]?"}},
            {"arrow": "→ Rechteck/Rectangular"},
            {"condition": {"de": "Natürlich, symmetrisch, Glockenform?", "en": "Natural, symmetric, bell-shaped?"}},
            {"arrow": "→ Normal"}
        ]
    },
    
    # --- KEY FORMULAS ---
    "key_formulas": {
        "header": {"de": "Die wichtigsten Formeln", "en": "The Key Formulas"},
        "formulas": [
            {"name": "E[X] diskret", "formula": r"\sum_x x \cdot P(X=x)"},
            {"name": "E[X] stetig", "formula": r"\int x \cdot f(x)\,dx"},
            {"name": "Var(X)", "formula": r"E[X^2] - E[X]^2"},
            {"name": "Z-Score", "formula": r"Z = \frac{X - \mu}{\sigma}"}
        ]
    },
    
    # --- PRO TRICKS ---
    "pro_tricks": {
        "header": {"de": "Pro-Tricks", "en": "Pro Tricks"},
        "tricks": [
            {
                "title": {"de": "Binomial vs Hyper", "en": "Binomial vs Hyper"},
                "trigger": {"de": "'Ohne Zurücklegen'", "en": "'Without replacement'"},
                "action": {"de": "Sofort Hypergeometrisch!", "en": "Immediately Hypergeometric!"}
            },
            {
                "title": {"de": "Poisson-Trigger", "en": "Poisson Trigger"},
                "trigger": {"de": "'Im Durchschnitt X pro Zeiteinheit'", "en": "'On average X per time unit'"},
                "action": {"de": "Sofort Poisson mit λ!", "en": "Immediately Poisson with λ!"}
            },
            {
                "title": {"de": "Exponential-Trigger", "en": "Exponential Trigger"},
                "trigger": {"de": "'Wartezeit bis...'", "en": "'Waiting time until...'"},
                "action": {"de": "Exponential mit λ = 1/E[X]", "en": "Exponential with λ = 1/E[X]"}
            },
            {
                "title": {"de": "Normal-Standardisierung", "en": "Normal Standardization"},
                "trigger": {"de": "N(μ, σ²) mit beliebigen Werten", "en": "N(μ, σ²) with any values"},
                "action": {"de": "Z = (X-μ)/σ → Tabelle!", "en": "Z = (X-μ)/σ → Table!"}
            },
            {
                "title": {"de": "1.96 merken!", "en": "Remember 1.96!"},
                "trigger": {"de": "95% Konfidenz", "en": "95% confidence"},
                "action": {"de": "Φ(1.96) ≈ 0.975", "en": "Φ(1.96) ≈ 0.975"}
            }
        ]
    },
    
    # --- COMMON TRAPS ---
    "traps": {
        "header": {"de": "Prüfungsfallen", "en": "Exam Traps"},
        "items": [
            {
                "trap": {"de": "σ vs σ²", "en": "σ vs σ²"},
                "wrong": {"de": "N(100, 25) → σ = 25", "en": "N(100, 25) → σ = 25"},
                "right": {"de": "N(100, 25) → σ² = 25, σ = 5", "en": "N(100, 25) → σ² = 25, σ = 5"}
            },
            {
                "trap": {"de": "λ bei Exponential", "en": "λ with Exponential"},
                "wrong": {"de": "E[X] = λ", "en": "E[X] = λ"},
                "right": {"de": "E[X] = 1/λ", "en": "E[X] = 1/λ"}
            },
            {
                "trap": {"de": "Hyper vs Binomial", "en": "Hyper vs Binomial"},
                "wrong": {"de": "Ohne Zurücklegen → Binomial", "en": "Without replacement → Binomial"},
                "right": {"de": "Ohne Zurücklegen → Hypergeometrisch", "en": "Without replacement → Hypergeometric"}
            },
            {
                "trap": {"de": "Rechteck P(X = x)", "en": "Rectangular P(X = x)"},
                "wrong": {"de": "P(X = 5) berechnen", "en": "Calculate P(X = 5)"},
                "right": {"de": "P(X = x) = 0 für stetige!", "en": "P(X = x) = 0 for continuous!"}
            }
        ]
    }
}


def render_subtopic_4_9(model):
    """4.9 Summary — Complete distributions review"""
    inject_equal_height_css()
    
    # --- CSS ---
    st.markdown("""
    <style>
    [data-testid="stHorizontalBlock"] { align-items: stretch !important; }
    [data-testid="column"] { display: flex !important; flex-direction: column !important; }
    [data-testid="column"] > div { flex: 1 !important; }
    h3 { margin-top: 0 !important; }
    </style>
    """, unsafe_allow_html=True)
    
    st.header(t(content_4_9["title"]))
    st.caption(t(content_4_9["subtitle"]))
    st.markdown("---")
    
    # === SECTION 1: CHEAT SHEET ===
    render_cheat_sheet()
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # === SECTION 2: DECISION TREE ===
    render_decision_tree()
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # === SECTION 3: KEY FORMULAS ===
    render_key_formulas()
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # === SECTION 4: PRO TRICKS ===
    render_pro_tricks()
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # === SECTION 5: TRAPS ===
    render_exam_traps()
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # === SECTION 6: EXAM PRACTICE ===
    st.markdown(f"### {t({'de': 'Prüfungstraining', 'en': 'Exam Practice'})}")
    
    q_ids = ["hs2023_prob3", "uebung2_mc9", "hs2022_mc6"]
    for q_id in q_ids:
        q = get_question("4.9", q_id)
        if q and q.get("type") != "problem":
            with st.container(border=True):
                st.caption(q.get("source", ""))
                opts = q.get("options", [])
                if opts and isinstance(opts[0], dict):
                    option_labels = [t(o) for o in opts]
                else:
                    option_labels = opts
                
                render_mcq(
                    key_suffix=f"4_9_{q_id}",
                    question_text=t(q["question"]),
                    options=option_labels,
                    correct_idx=q["correct_idx"],
                    solution_text_dict=q["solution"],
                    success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                    error_msg_dict={"de": "Falsch.", "en": "Incorrect."},
                    client=model,
                    ai_context=f"Distribution Summary: {q_id}",
                    course_id="vwl",
                    topic_id="4",
                    subtopic_id="4.9",
                    question_id=q_id
                )


def render_cheat_sheet():
    """Render all distributions overview"""
    cs = content_4_9["cheat_sheet"]
    st.markdown(f"### {t(cs['header'])}")
    
    # --- DISCRETE ---
    st.markdown(f"**{t(cs['discrete']['header'])}**")
    
    for dist in cs["discrete"]["distributions"]:
        with st.container(border=True):
            col_name, col_formula, col_use = st.columns([1.5, 2, 1.5])
            with col_name:
                st.markdown(f"**{t(dist['name'])}**")
                st.caption(dist["notation"])
            with col_formula:
                st.code(dist["pmf"], language=None)
                st.caption(dist["params"])
            with col_use:
                st.caption(t(dist["use"]))
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- CONTINUOUS ---
    st.markdown(f"**{t(cs['continuous']['header'])}**")
    
    for dist in cs["continuous"]["distributions"]:
        with st.container(border=True):
            col_name, col_formula, col_use = st.columns([1.5, 2, 1.5])
            with col_name:
                st.markdown(f"**{t(dist['name'])}**")
                st.caption(dist["notation"])
            with col_formula:
                st.code(dist["pdf"], language=None)
                st.caption(dist["params"])
            with col_use:
                st.caption(t(dist["use"]))


def render_decision_tree():
    """Render distribution decision tree"""
    dt = content_4_9["decision_tree"]
    st.markdown(f"### {t(dt['header'])}")
    st.caption(t(dt['subtitle']))
    
    with st.container(border=True):
        decision_html = ""
        for item in dt["rules"]:
            if "condition" in item:
                decision_html += f'<div style="background:#f4f4f5; padding:8px 12px; border-radius:6px; margin:6px 0; font-weight:500;">❓ {t(item["condition"])}</div>'
            elif "arrow" in item:
                decision_html += f'<div style="padding:4px 24px; color:#007AFF; font-family:monospace;">→ {item["arrow"]}</div>'
        
        st.markdown(decision_html, unsafe_allow_html=True)


def render_key_formulas():
    """Render key formulas in a row"""
    kf = content_4_9["key_formulas"]
    st.markdown(f"### {t(kf['header'])}")
    
    cols = st.columns(len(kf["formulas"]))
    for col, f in zip(cols, kf["formulas"]):
        with col:
            with st.container(border=True):
                st.markdown(f"**{f['name']}**")
                st.latex(f["formula"])


def render_pro_tricks():
    """Render pro tricks as trigger-action pairs"""
    pt = content_4_9["pro_tricks"]
    st.markdown(f"### {t(pt['header'])}")
    
    with st.container(border=True):
        for trick in pt["tricks"]:
            st.markdown(f"""
<div style="display:grid; grid-template-columns: 1fr 1.5fr 2fr; gap:12px; padding:8px 0; border-bottom:1px solid #f4f4f5;">
<div style="font-weight:600; color:#3f3f46;">{t(trick['title'])}</div>
<div style="color:#71717a; font-style:italic;">"{t(trick['trigger'])}"</div>
<div style="color:#007AFF; font-weight:500;">{t(trick['action'])}</div>
</div>""", unsafe_allow_html=True)


def render_exam_traps():
    """Render common exam traps"""
    traps = content_4_9["traps"]
    st.markdown(f"### {t(traps['header'])}")
    
    with st.container(border=True):
        # Header
        st.markdown(f"""
<div style="display:grid; grid-template-columns:1fr 1.5fr 1.5fr; gap:12px; font-weight:600; padding-bottom:8px; border-bottom:1px solid #e5e5ea;">
<div>{t({'de': 'Falle', 'en': 'Trap'})}</div>
<div style="color:#dc2626;">{t({'de': 'Falsch', 'en': 'Wrong'})}</div>
<div style="color:#16a34a;">{t({'de': 'Richtig', 'en': 'Right'})}</div>
</div>""", unsafe_allow_html=True)
        
        for item in traps["items"]:
            st.markdown(f"""
<div style="display:grid; grid-template-columns:1fr 1.5fr 1.5fr; gap:12px; padding:8px 0; border-bottom:1px solid #f4f4f5;">
<div style="font-weight:500;">{t(item['trap'])}</div>
<div style="color:#dc2626; font-family:monospace;">{t(item['wrong'])}</div>
<div style="color:#16a34a; font-family:monospace;">{t(item['right'])}</div>
</div>""", unsafe_allow_html=True)
