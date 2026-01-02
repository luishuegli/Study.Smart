import streamlit as st
from math import factorial
from utils.localization import t
from utils.quiz_helper import render_mcq
from data.exam_questions import get_question
from views.styles import render_icon, inject_equal_height_css

# --- CONTENT DICTIONARY (BILINGUAL) ---
content_2_5 = {
    "title": {"de": "2.5 Variationen (mit Wiederholung)", "en": "2.5 Variations (With Replacement)"},
    
    "intro": {
        "de": "Bei Variationen mit Wiederholung kann jedes Element mehrfach gewählt werden – der Pool schrumpft nie.",
        "en": "With variations with replacement, each element can be chosen multiple times – the pool never shrinks."
    },
    
    "context_anchor": {
        "de": """**Sicherheitsfrage: Warum sind 4-stellige PINs sicher?**

Deine Bank nutzt 4-stellige PINs. Ziffern: 0-9 (10 Möglichkeiten pro Stelle).

Jemand versucht, deinen PIN zu erraten:
- Versuch 1: 0000
- Versuch 2: 0001
- Versuch 3: 0002
- ...

**Wie viele Versuche braucht man, um ALLE Möglichkeiten durchzuprobieren?**

Das beantwortet Abschnitt 2.5.""",
        "en": """**Security Question: Why are 4-digit PINs secure?**

Your bank uses 4-digit PINs. Digits: 0-9 (10 choices per position).

Someone's trying to brute-force your PIN:
- Try 1: 0000
- Try 2: 0001
- Try 3: 0002
- ...

**How many tries until they've tried ALL possibilities?**

This is what Section 2.5 answers."""
    },
    
    "key_insight": {
        "de": """**Der Schlüssel:** Jede Ziffernposition ist UNABHÄNGIG.
- Position 1: kann 0-9 sein (10 Möglichkeiten)
- Position 2: IMMER NOCH 0-9 (10 Möglichkeiten) ← Pool schrumpft NICHT!
- Position 3: IMMER NOCH 0-9 (10 Möglichkeiten)
- Position 4: IMMER NOCH 0-9 (10 Möglichkeiten)

Das ist **MIT WIEDERHOLUNG** (with replacement).""",
        "en": """**The Key Insight:** Each digit position is INDEPENDENT.
- Position 1: can be 0-9 (10 choices)
- Position 2: STILL 0-9 (10 choices) ← Pool doesn't shrink!
- Position 3: STILL 0-9 (10 choices)
- Position 4: STILL 0-9 (10 choices)

This is **WITH REPLACEMENT**."""
    },
    
    "contrast_title": {"de": "Kontrast: 2.3 vs. 2.5", "en": "Contrast: 2.3 vs. 2.5"},
    
    "formula": {
        "title": {"de": "Variationen mit Wiederholung", "en": "Variations With Replacement"},
        "latex": r"n^{k}",
        "intuition": {"de": "Unbegrenzter Vorrat. Nichts wird 'verbraucht'.", "en": "Infinite supply. Nothing gets 'used up'."},
        "example": {"de": "iPhone-PIN: 4 Ziffern, je 0-9", "en": "iPhone passcode: 4 digits, each 0-9"},
        "pro_tip": {"de": "Kannst du dasselbe zweimal wählen? JA → n^k", "en": "Can you pick the same thing twice? YES → n^k"}
    },
    
    "interactive_title": {"de": "PIN-Baukasten", "en": "PIN Builder"},
    "interactive_instr": {
        "de": "Baue einen 4-stelligen PIN. Beobachte: Der verfügbare Pool BLEIBT bei 10 – auch nach jeder Auswahl!",
        "en": "Build a 4-digit PIN. Watch: The available pool STAYS at 10 – even after each selection!"
    },
    
    "security_title": {"de": "Praxisanwendung: PIN-Sicherheit", "en": "Real-World Application: PIN Security"},
    
    "exam": {
        "title": {"de": "Prüfungstraining", "en": "Exam Practice"},
        "source": "Variation with Replacement Practice"
    }
}

# --- MAIN RENDERING FUNCTION ---
def render_subtopic_2_5(model):
    """Renders Section 2.5: Variations (With Replacement)"""
    inject_equal_height_css()
    
    # --- HEADER ---
    st.header(t(content_2_5["title"]))
    st.markdown("---")
    
    # --- CONTEXT ANCHOR ---
    with st.container(border=True):
        st.markdown(t(content_2_5["context_anchor"]))
        
        st.markdown("<hr style='margin: 16px 0; border: 0; border-top: 1.5px solid #f3f4f6;'>", unsafe_allow_html=True)
        
        st.markdown(f"""
<div style="background: #f4f4f5; border-left: 3px solid #71717a; padding: 12px; border-radius: 6px; color: #3f3f46;">
{t(content_2_5["key_insight"])}
</div>
""", unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- CONTRAST: 2.3 vs 2.5 ---
    with st.container(border=True):
        st.markdown(f"### {t(content_2_5['contrast_title'])}")
        
        col_23, col_25 = st.columns([1, 1], gap="large")
        
        with col_23:
            st.markdown(f"**2.3: {t({'de': 'OHNE Wiederholung', 'en': 'WITHOUT Replacement'})}**")
            st.markdown(f"""
<div style="background: #f4f4f5; border-radius: 8px; padding: 16px;">
<b>{t({"de": "Szenario:", "en": "Scenario:"})}</b> {t({"de": "Playlist aus 3 Songs", "en": "Playlist of 3 songs"})}<br>
<b>{t({"de": "Songs:", "en": "Songs:"})}</b> {{A, B, C}}<br><br>
{t({"de": "Kann Song A zweimal vorkommen?", "en": "Can song A appear twice?"})} <b>{t({"de": "NEIN", "en": "NO"})}</b><br><br>
• {t({"de": "Position 1: 3 Optionen", "en": "Position 1: 3 options"})}<br>
• {t({"de": "Position 2: 2 Optionen (einer weg!)", "en": "Position 2: 2 options (one gone!)"})}<br>
• {t({"de": "Position 3: 1 Option (zwei weg!)", "en": "Position 3: 1 option (two gone!)"})}<br><br>
<b>{t({"de": "Pool schrumpft: 3→2→1", "en": "Pool shrinks: 3→2→1"})}</b>
</div>
""", unsafe_allow_html=True)
            st.latex(r"P(n,k) = \frac{n!}{(n-k)!}")
            st.latex(r"3 \times 2 \times 1 = 6")
        
        with col_25:
            st.markdown(f"**2.5: {t({'de': 'MIT Wiederholung', 'en': 'WITH Replacement'})}**")
            st.markdown(f"""
<div style="background: #f4f4f5; border-radius: 8px; padding: 16px;">
<b>{t({"de": "Szenario:", "en": "Scenario:"})}</b> {t({"de": "3-stelliger PIN", "en": "3-digit PIN"})}<br>
<b>{t({"de": "Ziffern:", "en": "Digits:"})}</b> {{0-9}}<br><br>
{t({"de": "Kann Ziffer 5 zweimal vorkommen?", "en": "Can digit 5 appear twice?"})} <b>{t({"de": "JA", "en": "YES"})}</b><br><br>
• {t({"de": "Position 1: 10 Optionen", "en": "Position 1: 10 options"})}<br>
• {t({"de": "Position 2: 10 Optionen (nichts weg!)", "en": "Position 2: 10 options (nothing gone!)"})}<br>
• {t({"de": "Position 3: 10 Optionen (nichts weg!)", "en": "Position 3: 10 options (nothing gone!)"})}<br><br>
<b>{t({"de": "Pool bleibt: 10→10→10", "en": "Pool stays: 10→10→10"})}</b>
</div>
""", unsafe_allow_html=True)
            st.latex(r"n^k")
            st.latex(r"10 \times 10 \times 10 = 1000")
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- INTERACTIVE: PIN BUILDER ---
    with st.container(border=True):
        st.markdown(f"### {t(content_2_5['interactive_title'])}")
        st.caption(t(content_2_5['interactive_instr']))
        
        # State initialization (Rule 6.3)
        if "pin_2_5" not in st.session_state:
            st.session_state.pin_2_5 = []
        
        digits = list(range(10))
        
        col_build, col_viz = st.columns([1.5, 1.5], gap="large")
        
        with col_build:
            st.markdown(f"**{t({'de': 'Ziffern-Pool (immer 0-9)', 'en': 'Digit Pool (always 0-9)'})}**")
            
            cols = st.columns(5)
            for idx, digit in enumerate(digits):
                col_idx = idx % 5
                # Highlight if already used (to show it's STILL available!)
                is_used = digit in st.session_state.pin_2_5
                btn_type = "primary" if is_used else "secondary"
                
                with cols[col_idx]:
                    if st.button(str(digit), key=f"digit_2_5_{digit}_{len(st.session_state.pin_2_5)}", 
                               type=btn_type, use_container_width=True):
                        if len(st.session_state.pin_2_5) < 4:
                            st.session_state.pin_2_5.append(digit)
                            st.rerun()
            
            if is_used:
                st.caption(t({
                    "de": "Hervorgehobene Ziffern wurden bereits verwendet – aber sind IMMER NOCH verfügbar!",
                    "en": "Highlighted digits were already used – but are STILL available!"
                }))
        
        with col_viz:
            st.markdown(f"**{t({'de': 'Pool-Grösse nach jedem Schritt', 'en': 'Pool Size After Each Step'})}**")
            
            if len(st.session_state.pin_2_5) == 0:
                st.info(t({"de": "Pool: 10/10 (alle verfügbar)", "en": "Pool: 10/10 (all available)"}))
            else:
                pin_str = "".join(map(str, st.session_state.pin_2_5))
                st.markdown(f"**{t({'de': 'Aktueller PIN:', 'en': 'Current PIN:'})}** `{pin_str}`")
                
                # Show pool size at each step
                for i in range(len(st.session_state.pin_2_5)):
                    st.success(f"{t({'de': 'Nach Ziffer', 'en': 'After digit'})} {i+1}: Pool = 10 ← {t({'de': 'immer noch 10!', 'en': 'still 10!'})}")
                
                if len(st.session_state.pin_2_5) == 4:
                    st.markdown("<hr style='margin: 16px 0; border: 0; border-top: 1.5px solid #f3f4f6;'>", unsafe_allow_html=True)
                    st.markdown(f"""
**{t({"de": "Vergleich zu 2.3 (Playlist):", "en": "Compare to 2.3 (Playlist):"})}**
- {t({"de": "Dort wäre der Pool: 10→9→8→7", "en": "There, pool would be: 10→9→8→7"})}
- {t({"de": "Hier ist der Pool: 10→10→10→10", "en": "Here, pool is: 10→10→10→10"})}

**{t({"de": "Warum?", "en": "Why?"})}** {t({"de": "Jede Ziffer ist unabhängig. Gewählte kommen zurück!", "en": "Each digit is independent. Chosen ones come back!"})}
""")
        
        st.markdown("<hr style='margin: 20px 0; border: 0; border-top: 1.5px solid #f3f4f6;'>", unsafe_allow_html=True)
        
        # Live math display
        k = len(st.session_state.pin_2_5) if len(st.session_state.pin_2_5) > 0 else 4
        result = 10 ** k
        
        col_formula, col_compare = st.columns([1, 1], gap="medium")
        
        with col_formula:
            st.latex(rf"10^{{{k}}} = {result:,}".replace(",", "'"))
            st.caption(t({
                "de": f"Mit Wiederholung: {result:,} mögliche {k}-stellige PINs".replace(",", "'"),
                "en": f"With replacement: {result:,} possible {k}-digit PINs"
            }))
        
        with col_compare:
            if k > 0:
                without_replacement = 1
                for i in range(k):
                    without_replacement *= (10 - i)
                st.latex(rf"10 \times 9 \times ... = {without_replacement:,}".replace(",", "'"))
                st.caption(t({
                    "de": f"Ohne Wiederholung wären es nur {without_replacement:,}".replace(",", "'"),
                    "en": f"Without replacement it would be only {without_replacement:,}"
                }))
        
        # Reset button
        if len(st.session_state.pin_2_5) > 0:
            if st.button(t({"de": "Neuen PIN bauen", "en": "Build New PIN"}), key="reset_pin_2_5"):
                st.session_state.pin_2_5 = []
                st.rerun()
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- SECURITY APPLICATION ---
    with st.container(border=True):
        st.markdown(f"### {t(content_2_5['security_title'])}")
        
        col_calc, col_insight = st.columns([1, 1.2], gap="large")
        
        with col_calc:
            st.markdown(f"**{t({'de': 'Dein 4-stelliger PIN:', 'en': 'Your 4-digit PIN:'})}**")
            st.latex(r"10^4 = 10'000")
            st.markdown(t({"de": "Durchschnittl. Versuche (50%): 5'000", "en": "Average attempts (50%): 5,000"}))
            st.markdown(t({"de": "Bei 1 Versuch/Sek: **83 Minuten**", "en": "At 1 try/sec: **83 minutes**"}))
        
        with col_insight:
            st.markdown(f"**{t({'de': 'Was, wenn Ziffern einzigartig sein müssten?', 'en': 'What if digits had to be unique?'})}**")
            st.markdown(f"""
<div style="background: #f4f4f5; border-radius: 8px; padding: 16px;">
<b>P(10,4) = 10 × 9 × 8 × 7 = 5'040</b><br><br>
{t({"de": "50% Chance: 2'520 Versuche", "en": "50% chance: 2,520 tries"})}<br>
{t({"de": "Bei 1/Sek: 42 Minuten", "en": "At 1/sec: 42 minutes"})}<br><br>
<b>{t({"de": "SCHNELLER zu knacken!", "en": "FASTER to brute-force!"})}</b>
</div>
""", unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        st.markdown(f"""
<div style="background: #f4f4f5; border-left: 3px solid #71717a; padding: 24px 20px; border-radius: 6px; font-size: 0.9rem; color: #3f3f46;">
<strong>Pro Tip:</strong> {t({
    "de": "Banken nutzen MIT Wiederholung (10⁴ = 10'000) weil es SICHERER ist als ohne (5'040)!",
    "en": "Banks use WITH replacement (10⁴ = 10,000) because it's MORE SECURE than without (5,040)!"
})}
</div>
""", unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- FORMULA COMPASS ---
    with st.container(border=True):
        st.markdown(f"### {t({'de': 'Formel-Kompass', 'en': 'Formula Compass'})}")
        
        col_formula, col_explain = st.columns([1, 1.2], gap="medium")
        
        with col_formula:
            st.markdown(f"**{t(content_2_5['formula']['title'])}**")
            st.latex(content_2_5['formula']['latex'])
        
        with col_explain:
            st.markdown(f"""
<div style="font-size: 0.95rem; color: #333; margin-bottom: 8px; display: flex; align-items: start; gap: 8px;">
    <span style="color: #666; margin-top: 2px;">{render_icon('lightbulb', size=16)}</span>
    <span>{t(content_2_5['formula']['intuition'])}</span>
</div>
<div style="font-size: 0.85rem; color: #666; padding-left: 26px; font-style: italic; margin-bottom: 12px;">
    Ex: {t(content_2_5['formula']['example'])}
</div>
<div style="background: #f4f4f5; border-left: 3px solid #71717a; padding: 24px 20px; border-radius: 6px; font-size: 0.9rem; color: #3f3f46;">
    <strong>Pro Tip:</strong> {t(content_2_5['formula']['pro_tip'])}
</div>
            """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- EXAM SECTION ---
    st.markdown(f"### {t(content_2_5['exam']['title'])}")
    st.caption(t(content_2_5['exam']['source']))
    
    with st.container(border=True):
        q_data = get_question("2.5", "coin_toss_seq")
        
        # Translate options
        opts = q_data.get("options", [])
        if opts and isinstance(opts[0], dict):
            option_labels = [t(o) for o in opts]
        else:
            option_labels = opts
        
        render_mcq(
            key_suffix="2_5_coin",
            question_text=t(q_data["question"]),
            options=option_labels,
            correct_idx=q_data["correct_idx"],
            solution_text_dict=q_data["solution"],
            success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
            error_msg_dict={"de": "Noch nicht ganz...", "en": "Not quite..."},
            client=model,
            ai_context="Variations with Replacement: Coin flip 2^4",
            hint_text_dict={"de": r"$$n^k$$", "en": r"$$n^k$$"},
            course_id="vwl",
            topic_id="2",
            subtopic_id="2.5",
            question_id="q_2_5_coin"
        )

