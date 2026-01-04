# Topic 5.3: Covariance and Correlation Coefficient
# Full implementation following gold standard patterns
import streamlit as st
from views.styles import inject_equal_height_css
from utils.localization import t
from utils.layouts.foundation import grey_info
from utils.quiz_helper import render_mcq
from data.exam_questions import get_question

# ==========================================
# 1. CONTENT DICTIONARY - BILINGUAL
# ==========================================
content_5_3 = {
    "title": {"de": "5.3 Kovarianz und Korrelationskoeffizient", "en": "5.3 Covariance and Correlation Coefficient"},
    "subtitle": {
        "de": "Messen, wie zwei Variablen zusammen schwanken",
        "en": "Measuring how two variables move together"
    },
    
    # --- INTUITION HOOK ---
    "intuition": {
        "header": {"de": "Die Intuition", "en": "The Intuition"},
        "text": {
            "de": "Stell dir vor, du hast zwei Aktien. Steigen sie **zusammen**? Fallen sie **zusammen**? Oder bewegen sie sich **unabhangig**? Die Kovarianz misst genau das: ob zwei Variablen gemeinsam schwanken. Aber sie sagt dir nicht **wie stark** — dafur brauchst du die Korrelation.",
            "en": "Imagine you have two stocks. Do they rise **together**? Fall **together**? Or move **independently**? Covariance measures exactly that: whether two variables fluctuate together. But it doesn't tell you **how strongly** — for that you need correlation."
        }
    },
    
    # --- FRAG DICH (Decision Guide) ---
    "frag_dich": {
        "header": {"de": "Frag dich: Kovarianz oder Korrelation?", "en": "Ask yourself: Covariance or Correlation?"},
        "questions": [
            {"de": "Brauchst du nur die <strong>Richtung</strong> (positiv/negativ)?", "en": "Do you only need the <strong>direction</strong> (positive/negative)?"},
            {"de": "Willst du <strong>vergleichen</strong> zwischen verschiedenen Variablenpaaren?", "en": "Do you want to <strong>compare</strong> between different variable pairs?"},
            {"de": "Interessiert dich die <strong>Starke</strong> des Zusammenhangs?", "en": "Are you interested in the <strong>strength</strong> of the relationship?"}
        ],
        "conclusion": {"de": "Nur Richtung? Cov. Starke oder Vergleich? Korrelation!", "en": "Just direction? Cov. Strength or comparison? Correlation!"}
    },
    
    # --- DEFINITION: COVARIANCE ---
    "definition_cov": {
        "header": {"de": "Die Kovarianz", "en": "The Covariance"},
        "text": {
            "de": "Die Kovarianz misst, ob zwei Variablen **gemeinsam** von ihren Mittelwerten abweichen. Positiv = sie bewegen sich in die gleiche Richtung. Negativ = sie bewegen sich gegeneinander.",
            "en": "Covariance measures whether two variables deviate from their means **together**. Positive = they move in the same direction. Negative = they move against each other."
        },
        "formula_definition": r"\text{Cov}(X,Y) = E\big[(X - \mu_X)(Y - \mu_Y)\big]",
        "formula_shortcut": r"\text{Cov}(X,Y) = E[XY] - E[X] \cdot E[Y]",
        "formula_shortcut_label": {"de": "Verschiebungssatz (einfacher zu rechnen!)", "en": "Shift formula (easier to calculate!)"},
        # VARIABLE DECODER
        "variable_decoder": {
            "header": {"de": "Was bedeutet jedes Symbol?", "en": "What does each symbol mean?"},
            "variables": [
                {
                    "symbol": r"\text{Cov}(X,Y)",
                    "name": {"de": "Kovarianz", "en": "Covariance"},
                    "meaning": {
                        "de": "Eine Zahl, die den **gemeinsamen Trend** von X und Y beschreibt. Kann jeden Wert annehmen — gross, klein, positiv, negativ.",
                        "en": "A number describing the **joint trend** of X and Y. Can be any value — large, small, positive, negative."
                    },
                    "example": {"de": "Cov(Grosse, Gewicht) > 0 (beide steigen zusammen)", "en": "Cov(Height, Weight) > 0 (both increase together)"}
                },
                {
                    "symbol": r"E[(X-\mu_X)(Y-\mu_Y)]",
                    "name": {"de": "Erwartete gemeinsame Abweichung", "en": "Expected joint deviation"},
                    "meaning": {
                        "de": "Fur jedes Paar (x,y): Wie weit ist X vom Mittelwert? Wie weit ist Y? Multipliziere und mittele. **Gleiches Vorzeichen** = positiver Beitrag.",
                        "en": "For each pair (x,y): How far is X from its mean? How far is Y? Multiply and average. **Same sign** = positive contribution."
                    },
                    "example": {"de": "Beide uber Durchschnitt → (+)(+) = + | Beide unter → (-)(-)= +", "en": "Both above average → (+)(+) = + | Both below → (-)(-)= +"}
                },
                {
                    "symbol": r"E[XY] - E[X]E[Y]",
                    "name": {"de": "Verschiebungssatz", "en": "Shift formula"},
                    "meaning": {
                        "de": "Dieselbe Formel, nur umgeschrieben. **Viel einfacher** zu rechnen! Du brauchst nur E[X], E[Y], und E[XY].",
                        "en": "Same formula, just rewritten. **Much easier** to calculate! You only need E[X], E[Y], and E[XY]."
                    },
                    "example": {"de": "Prufungs-Favorit! Weniger Rechenschritte", "en": "Exam favorite! Fewer calculation steps"}
                }
            ]
        }
    },
    
    # --- DEFINITION: CORRELATION ---
    "definition_corr": {
        "header": {"de": "Der Korrelationskoeffizient", "en": "The Correlation Coefficient"},
        "text": {
            "de": "Die Korrelation ist einfach die **normierte** Kovarianz. Durch Division mit den Standardabweichungen wird sie auf den Bereich [-1, +1] skaliert.",
            "en": "Correlation is simply the **normalized** covariance. By dividing by the standard deviations, it's scaled to the range [-1, +1]."
        },
        "formula": r"\rho_{X,Y} = \frac{\text{Cov}(X,Y)}{\sigma_X \cdot \sigma_Y}",
        # VARIABLE DECODER
        "variable_decoder": {
            "header": {"de": "Was bedeutet jedes Symbol?", "en": "What does each symbol mean?"},
            "variables": [
                {
                    "symbol": r"\rho_{X,Y}",
                    "name": {"de": "Korrelationskoeffizient (Rho)", "en": "Correlation coefficient (Rho)"},
                    "meaning": {
                        "de": "Eine Zahl zwischen **-1 und +1**. Je naher an ±1, desto starker der **lineare** Zusammenhang.",
                        "en": "A number between **-1 and +1**. The closer to ±1, the stronger the **linear** relationship."
                    },
                    "example": {"de": "ρ = 0.9 → starker positiver Zusammenhang | ρ = -0.3 → schwacher negativer", "en": "ρ = 0.9 → strong positive | ρ = -0.3 → weak negative"}
                },
                {
                    "symbol": r"\sigma_X, \sigma_Y",
                    "name": {"de": "Standardabweichungen", "en": "Standard deviations"},
                    "meaning": {
                        "de": "Die **Massstabe** fur die Normierung. Ohne sie ware Cov von den Einheiten abhangig (Euro vs. Rappen).",
                        "en": "The **scales** for normalization. Without them, Cov would depend on units (dollars vs. cents)."
                    },
                    "example": {"de": "σ = √Var(X) — die Wurzel der Varianz", "en": "σ = √Var(X) — the square root of variance"}
                }
            ],
            "scale_interpretation": {
                "header": {"de": "Interpretation der Skala", "en": "Scale Interpretation"},
                "values": [
                    {"value": "+1", "meaning_de": "Perfekt positiv — Y = aX + b mit a > 0", "meaning_en": "Perfect positive — Y = aX + b with a > 0"},
                    {"value": "0", "meaning_de": "Kein **linearer** Zusammenhang (aber vielleicht quadratisch!)", "meaning_en": "No **linear** relationship (but maybe quadratic!)"},
                    {"value": "-1", "meaning_de": "Perfekt negativ — Y = aX + b mit a < 0", "meaning_en": "Perfect negative — Y = aX + b with a < 0"}
                ]
            }
        }
    },
    
    # --- EXAM ESSENTIALS ---
    "exam_essentials": {
        "trap": {
            "de": "**Cov = 0 bedeutet NICHT Unabhangigkeit!** Die Kovarianz misst nur **linearen** Zusammenhang. Klassisches Gegenbeispiel: X gleichverteilt auf [-1,1], dann ist Y = X² abhangig von X, aber Cov(X, Y) = 0!",
            "en": "**Cov = 0 does NOT mean independence!** Covariance only measures **linear** relationship. Classic counterexample: X uniform on [-1,1], then Y = X² depends on X, but Cov(X, Y) = 0!"
        },
        "trap_rule": {
            "de": "Unabhangigkeit → Cov = 0. Aber Cov = 0 → NICHT unbedingt unabhangig!",
            "en": "Independence → Cov = 0. But Cov = 0 → NOT necessarily independent!"
        },
        "tips": [
            {
                "tip": {"de": "Verwende den Verschiebungssatz: E[XY] - E[X]E[Y]", "en": "Use the shift formula: E[XY] - E[X]E[Y]"},
                "why": {"de": "Viel weniger Rechnung als die Definitionsformel. Prufungszeit sparen!", "en": "Much less calculation than the definition formula. Save exam time!"}
            },
            {
                "tip": {"de": "Lineare Transformation: Cov(aX, bY) = ab · Cov(X,Y)", "en": "Linear transformation: Cov(aX, bY) = ab · Cov(X,Y)"},
                "why": {"de": "Konstanten verschwinden nicht wie bei Varianz. Sie werden nur multipliziert.", "en": "Constants don't disappear like with variance. They just get multiplied."}
            },
            {
                "tip": {"de": "Korrelation bei linearer Transformation: ρ(aX+b, cY+d) = sign(ac) · ρ(X,Y)", "en": "Correlation under linear transformation: ρ(aX+b, cY+d) = sign(ac) · ρ(X,Y)"},
                "why": {"de": "Additive Konstanten (b, d) andern ρ nicht. Vorzeichen nur wenn a oder c negativ.", "en": "Additive constants (b, d) don't change ρ. Sign only flips if a or c is negative."}
            }
        ]
    }
}


def render_subtopic_5_3(model):
    """5.3 Kovarianz und Korrelationskoeffizient - Full Implementation"""
    inject_equal_height_css()
    
    # --- HEADER ---
    st.header(t(content_5_3["title"]))
    st.caption(t(content_5_3["subtitle"]))
    st.markdown("---")
    
    # --- INTUITION HOOK ---
    st.markdown(f"### {t(content_5_3['intuition']['header'])}")
    with st.container(border=True):
        st.markdown(t(content_5_3["intuition"]["text"]))
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- FRAG DICH: DECISION GUIDE ---
    from utils.ask_yourself import render_ask_yourself
    render_ask_yourself(
        header=content_5_3['frag_dich']['header'],
        questions=content_5_3['frag_dich']['questions'],
        conclusion=content_5_3['frag_dich']['conclusion']
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- DEFINITION: COVARIANCE ---
    cov = content_5_3["definition_cov"]
    st.markdown(f"### {t(cov['header'])}")
    with st.container(border=True):
        st.markdown(t(cov["text"]))
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Main formula
        st.markdown(f"**{t({'de': 'Definition', 'en': 'Definition'})}:**")
        st.latex(cov["formula_definition"])
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Shortcut formula
        st.markdown(f"**{t(cov['formula_shortcut_label'])}:**")
        st.latex(cov["formula_shortcut"])
        
        st.markdown("---")
        
        # --- SYMBOL LEDGER (full-width to prevent formula cutoff) ---
        decoder = cov["variable_decoder"]
        st.markdown(f"**{t(decoder['header'])}**")
        
        for var in decoder["variables"]:
            st.latex(var['symbol'])
            st.markdown(f"**{t(var['name'])}**")
            st.markdown(t(var['meaning']), unsafe_allow_html=True)
            st.caption(t(var['example']))
            st.markdown("---")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- DEFINITION: CORRELATION ---
    corr = content_5_3["definition_corr"]
    st.markdown(f"### {t(corr['header'])}")
    with st.container(border=True):
        st.markdown(t(corr["text"]))
        st.markdown("<br>", unsafe_allow_html=True)
        
        st.latex(corr["formula"])
        
        st.markdown("---")
        
        # --- SYMBOL LEDGER (full-width to prevent formula cutoff) ---
        decoder = corr["variable_decoder"]
        st.markdown(f"**{t(decoder['header'])}**")
        
        for var in decoder["variables"]:
            st.latex(var['symbol'])
            st.markdown(f"**{t(var['name'])}**")
            st.markdown(t(var['meaning']), unsafe_allow_html=True)
            st.caption(t(var['example']))
            st.markdown("---")
        
        # Scale interpretation
        scale = decoder["scale_interpretation"]
        st.markdown(f"**{t(scale['header'])}**")
        for item in scale["values"]:
            st.markdown(f"- **ρ = {item['value']}**: {t({'de': item['meaning_de'], 'en': item['meaning_en']})}")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # =========================================
    # INTERACTIVE MISSION: PORTFOLIO DIVERSIFICATION
    # =========================================
    st.markdown(f"### {t({'de': 'Mission: Portfolio-Diversifikation', 'en': 'Mission: Portfolio Diversification'})}")
    
    @st.fragment
    def portfolio_mission():
        if "portfolio_5_3_completed" not in st.session_state:
            st.session_state.portfolio_5_3_completed = False
        
        # Step 1: Scenario (WHY does this matter?)
        st.markdown(f"""
<div style="background: #f4f4f5; border-left: 4px solid #a1a1aa; 
            padding: 12px 16px; border-radius: 8px; color: #3f3f46;">
<strong>{t({'de': 'Szenario', 'en': 'Scenario'})}:</strong><br>
{t({'de': 'Du bist Fondsmanager und investierst in zwei Aktien (X und Y). Jede hat eine Varianz von 16 — also ziemlich volatil. Dein Ziel: Das Gesamtrisiko deines Portfolios minimieren. Die entscheidende Frage: <strong>Wie hängen die Aktien zusammen?</strong>', 
    'en': "You're a fund manager investing in two stocks (X and Y). Each has variance 16 — pretty volatile. Your goal: Minimize your portfolio's total risk. The key question: <strong>How are the stocks related?</strong>"})}
</div>
""", unsafe_allow_html=True)
        
        # Step 2: Mission statement (WHAT should they do?)
        st.markdown(f"**{t({'de': 'Deine Mission', 'en': 'Your Mission'})}:** {t({'de': 'Finde den ρ-Wert, bei dem das Portfolio-Risiko am kleinsten wird!', 'en': 'Find the ρ value where portfolio risk is lowest!'})}")
        
        with st.container(border=True):
            # Step 3: The formula (HOW does it work?)
            st.markdown(f"**{t({'de': 'Die Formel, die alles erklärt', 'en': 'The Formula That Explains Everything'})}:**")
            st.latex(r"\text{Var}(X + Y) = \underbrace{\sigma_X^2}_{16} + \underbrace{\sigma_Y^2}_{16} + 2 \cdot \underbrace{\rho \cdot \sigma_X \cdot \sigma_Y}_{\text{Cov}(X,Y)}")
            
            st.caption(t({'de': 'Die Kovarianz bestimmt, ob sich Risiken addieren oder aufheben!', 'en': 'The covariance determines whether risks add up or cancel out!'}))
            
            st.markdown("---")
            
            # Step 4: Interactive controls
            rho = st.slider(
                t({"de": "Korrelation ρ zwischen den Aktien", "en": "Correlation ρ between stocks"}),
                min_value=-1.0,
                max_value=1.0,
                value=0.0,
                step=0.1,
                key="portfolio_rho_slider"
            )
            
            # Calculate portfolio variance
            var_x, var_y = 16, 16
            sigma_x, sigma_y = 4, 4
            cov_xy = rho * sigma_x * sigma_y
            portfolio_var = var_x + var_y + 2 * cov_xy
            
            # Step 5: Live calculation display with semantic colors
            # Color coding: Red = high risk, Green = low risk, Blue = neutral
            if portfolio_var >= 48:
                var_color = "#FF4B4B"  # Red - danger/high risk
                risk_label = t({"de": "Hohes Risiko", "en": "High Risk"})
            elif portfolio_var <= 8:
                var_color = "#16a34a"  # Green - safe/low risk
                risk_label = t({"de": "Niedriges Risiko", "en": "Low Risk"})
            else:
                var_color = "#007AFF"  # Blue - neutral
                risk_label = t({"de": "Mittleres Risiko", "en": "Medium Risk"})
            
            cov_color = "#FF4B4B" if cov_xy > 0 else ("#16a34a" if cov_xy < 0 else "#6B7280")
            
            # Display calculations WITHOUT nested containers in columns (prevents formula cutoff)
            st.markdown(f"""
<div style="display: flex; gap: 16px; margin: 12px 0;">
    <div style="flex: 1; padding: 12px; background: #fafafa; border-radius: 8px; border: 1px solid #e5e5e5;">
        <strong style="color: {cov_color};">Cov(X, Y) = {cov_xy:.1f}</strong><br>
        <span style="font-size: 0.9em; color: #6B7280;">ρ × σ_X × σ_Y = {rho:.1f} × 4 × 4</span>
    </div>
    <div style="flex: 1; padding: 12px; background: #fafafa; border-radius: 8px; border: 1px solid #e5e5e5;">
        <strong style="color: {var_color};">Var(X + Y) = {portfolio_var:.1f}</strong><br>
        <span style="font-size: 0.9em; color: #6B7280;">16 + 16 + 2×({cov_xy:.1f})</span>
    </div>
</div>
""", unsafe_allow_html=True)
            
            # Risk indicator bar
            st.markdown(f"""
<div style="background: linear-gradient(to right, #16a34a 0%, #007AFF 50%, #FF4B4B 100%); 
            height: 8px; border-radius: 4px; margin: 8px 0; position: relative;">
    <div style="position: absolute; left: {((portfolio_var) / 64) * 100}%; top: -4px; 
                width: 16px; height: 16px; background: white; border: 2px solid #333; 
                border-radius: 50%; transform: translateX(-50%);"></div>
</div>
<div style="display: flex; justify-content: space-between; font-size: 0.8em; color: #6B7280;">
    <span>0 ({t({'de': 'Min', 'en': 'Min'})})</span>
    <span style="color: {var_color}; font-weight: bold;">{risk_label}</span>
    <span>64 ({t({'de': 'Max', 'en': 'Max'})})</span>
</div>
""", unsafe_allow_html=True)
            
            # Step 6: Feedback based on state
            if rho == -1:
                st.balloons()
                st.success(t({
                    "de": f"🎯 **Mission erfüllt!** Bei ρ = -1 ist Var(X+Y) = {portfolio_var:.0f}!",
                    "en": f"🎯 **Mission Complete!** At ρ = -1, Var(X+Y) = {portfolio_var:.0f}!"
                }))
                
                # Step 7: Connect discovery back to formula
                st.markdown(f"""
<div style="background: rgba(22, 163, 74, 0.1); border-left: 4px solid #16a34a; 
            padding: 12px 16px; border-radius: 8px; color: #3f3f46;">
<strong>{t({'de': 'Was du gerade entdeckt hast', 'en': 'What You Just Discovered'})}:</strong><br><br>
{t({'de': '''In der Formel <strong>Var(X+Y) = σ²_X + σ²_Y + 2·Cov(X,Y)</strong> ist der Kovarianz-Term der Schlüssel:
<br>• <strong style="color: #FF4B4B;">Cov > 0</strong> → Risiken addieren sich (schlecht!)
<br>• <strong style="color: #16a34a;">Cov < 0</strong> → Risiken heben sich auf (Diversifikation!)
<br>• <strong>ρ = -1</strong> → Perfekte Gegenbewegung = Minimales Risiko''',
    'en': '''In the formula <strong>Var(X+Y) = σ²_X + σ²_Y + 2·Cov(X,Y)</strong>, the covariance term is key:
<br>• <strong style="color: #FF4B4B;">Cov > 0</strong> → Risks add up (bad!)
<br>• <strong style="color: #16a34a;">Cov < 0</strong> → Risks cancel out (diversification!)
<br>• <strong>ρ = -1</strong> → Perfect opposite movement = Minimum risk'''})}
</div>
""", unsafe_allow_html=True)
                
                if not st.session_state.portfolio_5_3_completed:
                    st.session_state.portfolio_5_3_completed = True
                    from utils.progress_tracker import track_question_answer, update_local_progress
                    if user := st.session_state.get("user"):
                        update_local_progress("5", "5.3", "5_3_portfolio", True)
                        track_question_answer(user["localId"], "vwl", "5", "5.3", "5_3_portfolio", True)
            
            elif rho == 1:
                st.error(t({
                    "de": f"⚠️ ρ = +1 → Var = {portfolio_var:.0f} — Maximum! Die Aktien schwanken synchron. Versuch's mit negativer Korrelation!",
                    "en": f"⚠️ ρ = +1 → Var = {portfolio_var:.0f} — Maximum! Stocks move in sync. Try negative correlation!"
                }))
            
            elif rho == 0:
                grey_info(t({
                    "de": f"ρ = 0 → Var = {portfolio_var:.0f}. Keine Korrelation = Varianzen addieren sich einfach. Geht das noch besser?",
                    "en": f"ρ = 0 → Var = {portfolio_var:.0f}. No correlation = variances simply add. Can you do better?"
                }))
            
            elif rho < 0:
                grey_info(t({
                    "de": f"ρ = {rho:.1f} → Var = {portfolio_var:.1f}. Gute Richtung! Negative Korrelation senkt das Risiko. Aber es geht noch tiefer...",
                    "en": f"ρ = {rho:.1f} → Var = {portfolio_var:.1f}. Good direction! Negative correlation lowers risk. But you can go lower..."
                }))
            
            else:  # rho > 0
                st.warning(t({
                    "de": f"ρ = {rho:.1f} → Var = {portfolio_var:.1f}. Positive Korrelation erhöht das Risiko! Versuch's in die andere Richtung.",
                    "en": f"ρ = {rho:.1f} → Var = {portfolio_var:.1f}. Positive correlation increases risk! Try the other direction."
                }))
    
    portfolio_mission()
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- EXAM ESSENTIALS ---
    from utils.exam_essentials import render_exam_essentials
    render_exam_essentials(
        trap=content_5_3["exam_essentials"]["trap"],
        trap_rule=content_5_3["exam_essentials"]["trap_rule"],
        tips=content_5_3["exam_essentials"]["tips"]
    )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- EXAM SECTION ---
    st.markdown(f"### {t({'de': 'Prufungstraining', 'en': 'Exam Practice'})}")
    
    # MCQ 1: uebung3_mc1 (Covariance measures)
    q1 = get_question("5.3", "uebung3_mc1")
    if q1:
        with st.container(border=True):
            st.caption(q1.get("source", ""))
            opts = q1.get("options", [])
            option_labels = [t(o) if isinstance(o, dict) else o for o in opts]
            
            render_mcq(
                key_suffix="5_3_cov_def",
                question_text=t(q1["question"]),
                options=option_labels,
                correct_idx=q1["correct_idx"],
                solution_text_dict=q1["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
                client=model,
                ai_context="What covariance measures",
                course_id="vwl",
                topic_id="5",
                subtopic_id="5.3",
                question_id="5_3_cov_def"
            )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # MCQ 2: uebung3_mc9 (Urn correlation)
    q2 = get_question("5.3", "uebung3_mc9")
    if q2:
        with st.container(border=True):
            st.caption(q2.get("source", ""))
            opts = q2.get("options", [])
            option_labels = [t(o) if isinstance(o, dict) else o for o in opts]
            
            render_mcq(
                key_suffix="5_3_urn",
                question_text=t(q2["question"]),
                options=option_labels,
                correct_idx=q2["correct_idx"],
                solution_text_dict=q2["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
                client=model,
                ai_context="Correlation in sampling without replacement",
                course_id="vwl",
                topic_id="5",
                subtopic_id="5.3",
                question_id="5_3_urn"
            )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # MCQ 3: test4_q2 (Correlation calculation)
    q3 = get_question("5.3", "test4_q2")
    if q3:
        with st.container(border=True):
            st.caption(q3.get("source", ""))
            opts = q3.get("options", [])
            option_labels = [t(o) if isinstance(o, dict) else o for o in opts]
            
            render_mcq(
                key_suffix="5_3_calc",
                question_text=t(q3["question"]),
                options=option_labels,
                correct_idx=q3["correct_idx"],
                solution_text_dict=q3["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
                client=model,
                ai_context="Calculating correlation from covariance and variances",
                course_id="vwl",
                topic_id="5",
                subtopic_id="5.3",
                question_id="5_3_calc"
            )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # MCQ 4: test4_q4 (Independence → Covariance = 0)
    q4 = get_question("5.3", "test4_q4")
    if q4:
        with st.container(border=True):
            st.caption(q4.get("source", ""))
            opts = q4.get("options", [])
            option_labels = [t(o) if isinstance(o, dict) else o for o in opts]
            
            render_mcq(
                key_suffix="5_3_indep",
                question_text=t(q4["question"]),
                options=option_labels,
                correct_idx=q4["correct_idx"],
                solution_text_dict=q4["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
                client=model,
                ai_context="Independence implies zero covariance",
                course_id="vwl",
                topic_id="5",
                subtopic_id="5.3",
                question_id="5_3_indep"
            )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # MCQ 5: hs2015_mc1 (E[XY] = E[X]E[Y] equivalence)
    q5 = get_question("5.3", "hs2015_mc1")
    if q5:
        with st.container(border=True):
            st.caption(q5.get("source", ""))
            opts = q5.get("options", [])
            option_labels = [t(o) if isinstance(o, dict) else o for o in opts]
            
            render_mcq(
                key_suffix="5_3_exy",
                question_text=t(q5["question"]),
                options=option_labels,
                correct_idx=q5["correct_idx"],
                solution_text_dict=q5["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
                client=model,
                ai_context="E[XY] = E[X]E[Y] iff uncorrelated",
                course_id="vwl",
                topic_id="5",
                subtopic_id="5.3",
                question_id="5_3_exy"
            )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # MCQ 6: hs2015_mc7 (Linear transformation correlation)
    q6 = get_question("5.3", "hs2015_mc7")
    if q6:
        with st.container(border=True):
            st.caption(q6.get("source", ""))
            opts = q6.get("options", [])
            option_labels = [t(o) if isinstance(o, dict) else o for o in opts]
            
            render_mcq(
                key_suffix="5_3_linear",
                question_text=t(q6["question"]),
                options=option_labels,
                correct_idx=q6["correct_idx"],
                solution_text_dict=q6["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
                client=model,
                ai_context="Correlation under linear transformation",
                course_id="vwl",
                topic_id="5",
                subtopic_id="5.3",
                question_id="5_3_linear"
            )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # MCQ 7: hs2024_mc2 (was already in skeleton but named wrong - keep existing)
    q7 = get_question("5.3", "hs2024_mc2")
    if q7:
        with st.container(border=True):
            st.caption(q7.get("source", ""))
            opts = q7.get("options", [])
            option_labels = [t(o) if isinstance(o, dict) else o for o in opts]
            
            render_mcq(
                key_suffix="5_3_corr_props",
                question_text=t(q7["question"]),
                options=option_labels,
                correct_idx=q7["correct_idx"],
                solution_text_dict=q7["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
                client=model,
                ai_context="Correlation vs Independence properties",
                course_id="vwl",
                topic_id="5",
                subtopic_id="5.3",
                question_id="5_3_corr_props"
            )
