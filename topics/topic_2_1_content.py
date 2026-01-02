import streamlit as st
import itertools
from views.styles import render_icon, inject_equal_height_css
from utils.localization import t
from utils.quiz_helper import render_mcq
from data.exam_questions import get_question

# --- CONTENT DICTIONARY ---
content_2_1 = {
    "title": {"de": "2.1 Binomialkoeffizient", "en": "2.1 Binomial Coefficient"},
    "anchor": {"de": "Kontext-Check: Zählt die Reihenfolge?", "en": "Context Check: Does Order Matter?"},
    "intro": {
        "de": "Die Mathematik ändert sich je nach **Szenario**. Wähle eine Situation:",
        "en": "The math changes based on the **Scenario**. Choose a situation:"
    },
    "scenarios": {
        "abstract": {
            "label": "Abstract", 
            "items": ["A", "B", "C", "D"],
            "desc": {"de": "Experimentierfeld.", "en": "Playground."}
        },
        "race": {
            "label": "Podium", 
            "items": ["1", "2", "3", "4"],
            "desc": {"de": "Gold ist nicht Silber. <b>Reihenfolge zählt!</b>", "en": "Gold is not Silver. <b>Order Matters!</b>"}
        },
        "lotto": {
            "label": "Lotto", 
            "items": ["1", "2", "3", "4"],
            "desc": {"de": "Die Hand ist gleich, egal wann gezogen. <b>Reihenfolge egal!</b>", "en": "The hand is the same, no matter when drawn. <b>Order Irrelevant!</b>"}
        }
    },
    "cheat_sheet": {
        "title": {"de": "Klausur-Hack: Signalwörter", "en": "Exam Hack: Signal Words"},
        "perm": {"de": "Rangliste, Planen, Code, Anordnen, Warteschlange", "en": "Rank, Schedule, Code, Arrange, Queue"},
        "comb": {"de": "Auswählen, Team, Menge, Gezogen, Lottoprozahl", "en": "Select, Choose, Set, Drawn, Lottery"}
    }
}

# --- VISUAL HELPERS ---
def render_avatar(item, style_type="circle"):
    """Renders a neutral visual item (Ball, Medal, or Letter)."""
    inject_equal_height_css()
    # Design change: Neutral elements, color reserved for variables
    bg = "#f1f5f9" # slate-100
    text_color = "#334155" # slate-700
    border = "1px solid #e2e8f0" # slate-200
    
    if style_type == "medal":
        # Square-ish for podium
        return f"<span style='display:inline-block; width:24px; height:24px; line-height:24px; text-align:center; background:{bg}; color:{text_color}; border:{border}; border-radius:4px; font-weight:bold; margin:0 2px;'>{item}</span>"
    else:
        # Circle for balls/abstract
        return f"<span style='display:inline-block; width:26px; height:26px; line-height:26px; text-align:center; background:{bg}; color:{text_color}; border:{border}; border-radius:50%; font-weight:bold; margin:0 2px;'>{item}</span>"

def render_subtopic_2_1(client):
    c = content_2_1
    
    # --- CSS: LAYOUT & CARDS ---
    st.markdown("""
    <style>
    /* Equal Height Hack */
    [data-testid="column"] { display: flex; flex-direction: column; }
    [data-testid="column"] > div[data-testid="stVerticalBlock"] > div { flex-grow: 1; }
    
    /* Card Container */
    .outcome-card {
        background: white;
        border: 1px solid #e0e0e0;
        border-radius: 8px;
        padding: 10px;
        margin-bottom: 10px;
        box-shadow: 0 1px 2px rgba(0,0,0,0.05);
        transition: all 0.2s;
    }
    
    /* Permutation Row (Valid) */
    .perm-row {
        display: flex; align-items: center; justify-content: space-between;
        padding: 5px 8px;
        margin: 4px 0;
        background: #f8f9fa;
        border-radius: 6px;
        font-family: monospace;
    }
    
    /* Ghost Row (Invalid/Duplicate) */
    .ghost-row {
        display: flex; align-items: center; justify-content: space-between;
        padding: 5px 8px;
        margin: 4px 0;
        background: #fff5f5;
        border: 1px dashed #ffcdd2;
        border-radius: 6px;
        opacity: 0.6;
    }
    .ghost-text {
        text-decoration: line-through;
        color: #e53935;
        font-size: 0.85em;
    }
    
    /* Highlight for Canonical Item */
    .canonical {
        border-left: 4px solid #0068C9;
        background: #e3f2fd;
    }
    </style>
    """, unsafe_allow_html=True)

    # --- HEADER ---
    st.markdown(f"## {t(c['title'])}")
    st.markdown(f"**{t(c['anchor'])}**")
    
    # =========================================================================
    # THEORY SECTION - COMPREHENSIVE PEDAGOGICAL CONTENT
    # =========================================================================
    st.markdown(f"### {t({'de': 'Theorie', 'en': 'Theory'})}")
    
    # --- ROW 1: THE BIG QUESTION ---
    # --- ROW 1: THE BIG QUESTION ---
    st.markdown(f"### {t({'de': 'Zählt die Reihenfolge oder nicht?', 'en': 'Does the order matter or not?'})}")
    with st.container(border=True):
        
        # --- ROW 2: MENTAL MODEL - PODIUM VS LOTTERY ---
        st.markdown(f"**{t({'de': 'Gedächtnisstütze: Podium vs. Lotterie', 'en': 'Memory Hook: Podium vs. Lottery'})}**")
        
        # ROW 1: Titles and Descriptions
        c_perm_t, c_comb_t = st.columns(2, gap="medium")
        with c_perm_t:
            st.markdown(f"<h4>{t({'de': 'Permutation (Podium)', 'en': 'Permutation (Podium)'})}</h4>", unsafe_allow_html=True)
            st.markdown(f"""
<div style="margin-bottom: 12px; color: #334155;">
{t({'de': 'Gold ≠ Silber. Wer <b>WANN</b> ins Ziel kommt, zählt.', 'en': 'Gold ≠ Silver. WHO finishes <b>WHEN</b> matters.'})}
</div>
""", unsafe_allow_html=True)
        with c_comb_t:
            st.markdown(f"<h4>{t({'de': 'Kombination (Lotterie)', 'en': 'Combination (Lottery)'})}</h4>", unsafe_allow_html=True)
            st.markdown(f"""
<div style="margin-bottom: 12px; color: #334155;">
{t({'de': '{3, 7, 12} = {12, 3, 7}. Nur <b>WER</b> gezogen wird, zählt.', 'en': '{3, 7, 12} = {12, 3, 7}. Only <b>WHO</b> is drawn matters.'})}
</div>
""", unsafe_allow_html=True)
            
        # ROW 2: Formulas (Split-Row Grid Protocol - Rule 2.7)
        c_perm_f, c_comb_f = st.columns(2, gap="medium")
        with c_perm_f:
            st.latex(r"P(n, k) = \frac{n!}{\left( n - k \right)!}")
            st.caption(t({"de": "Reihenfolge ist wichtig.", "en": "Order is important."}))
        with c_comb_f:
            st.latex(r"\binom{n}{k} = \frac{n!}{k! \left( n - k \right)!}")
            st.caption(t({"de": "Reihenfolge egal.", "en": "Order irrelevant."}))
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # --- ROW 3: NOTATION ---
        st.markdown(f"**{t({'de': 'Notation (immer zuerst klären!)', 'en': 'Notation (always clarify first!)'})}**")
        
        # Helper for stacked notation
        def notation_card(col, latex, div_id, desc_dict):
             with col:
                st.latex(latex)
                st.markdown(f"<div style='text-align: center; font-size: 0.85em; color: #444; margin-top: -12px;'>{t(desc_dict)}</div>", unsafe_allow_html=True)

        c1, c2, c3, c4 = st.columns(4)
        notation_card(c1, r"n", "not_n", {"de": "Gesamtpool", "en": "Total Pool"})
        notation_card(c2, r"k", "not_k", {"de": "Auswahl", "en": "Selection"})
        notation_card(c3, r"n!", "not_nfac", {"de": "Alle Anordnungen", "en": "Total Arragements"})
        notation_card(c4, r"k!", "not_kfac", {"de": "Auswahl Anordnungen", "en": "Selection Arrangements"})
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # --- ROW 4: THE INTUITION (WHY k!) ---
        st.markdown(f"**{t({'de': 'Warum teilen wir durch $k!$?', 'en': 'Why do we divide by $k!$?'})}**")
        st.markdown(t({
            "de": """Stell dir vor, du wählst ein 3er-Team aus 5 Personen. Wenn du zuerst Anna, dann Ben, dann Clara wählst, ist das **dasselbe Team** wie Ben → Clara → Anna. 
            
Aber die Permutationsformel zählt jede Reihenfolge separat! Für 3 Personen gibt es $3! = 6$ Reihenfolgen. Also müssen wir durch 6 teilen, um die "Geister" (Duplikate) zu entfernen.""",
            "en": """Imagine selecting a team of 3 from 5 people. If you pick Anna first, then Ben, then Clara, that's the **same team** as Ben → Clara → Anna.

But the permutation formula counts each order separately! For 3 people, there are $3! = 6$ orderings. So we divide by 6 to remove the "ghosts" (duplicates)."""
        }))
        
        # --- PRO TIP (Rule 5.4) ---

    
    # --- ROW 5: THE TRAP (COMMON MISTAKE) ---
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"### {t({'de': 'Die Falle: Variation vs. Permutation', 'en': 'The Trap: Variation vs. Permutation'})}")
    with st.container(border=True):
        
        st.markdown(t({
            'de': '<b>Variation mit Wiederholung</b> ($n^k$): Jede Position kann jeden Wert haben (z.B. PIN-Code 1-1-1-1 erlaubt).', 
            'en': '<b>Variation with Repetition</b> ($n^k$): Each position can have any value (e.g., PIN code 1-1-1-1 allowed).'}), unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        st.markdown(t({
            'de': '<b>Permutation ohne Wiederholung</b> ($P(n,k)$): Jedes Element kann nur einmal verwendet werden (z.B. Podiumsplatz).', 
            'en': '<b>Permutation without Repetition</b> ($P(n,k)$): Each element can only be used once (e.g., podium position).'}), unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        st.markdown(t({
            'de': '<b>Frag dich:</b> Kann dieselbe Person/Sache mehrfach vorkommen?', 
            'en': '<b>Ask yourself:</b> Can the same person/thing appear multiple times?'}), unsafe_allow_html=True)

        # --- QUESTION DISSECTOR (Rule: Teach by Example) ---
        st.markdown("<hr style='margin: 16px 0; border: 0; border-top: 1px solid #e5e7eb;'>", unsafe_allow_html=True)
        st.markdown(f"**{t({'de': 'Fragen-Analysator: So erkennst du die Formel', 'en': 'Question Dissector: How to Spot the Formula'})}**")
        
        # Color Legend (compact inline)
        st.markdown("""
<div style="display: flex; gap: 16px; flex-wrap: wrap; font-size: 0.8em; margin-bottom: 12px; color: #64748b;">
    <span><span style="background:#dbeafe; padding:2px 6px; border-radius:4px; color:#1d4ed8;">Given</span> = Data</span>
    <span><span style="background:#fee2e2; padding:2px 6px; border-radius:4px; color:#dc2626;">Target</span> = Find</span>
    <span><span style="background:#dcfce7; padding:2px 6px; border-radius:4px; color:#16a34a;">Signal</span> = Formula Hint</span>
    <span><span style="background:#f4f4f5; padding:2px 6px; border-radius:4px; color:#3f3f46;">→ Formula</span></span>
</div>
        """, unsafe_allow_html=True)
        
        # Tabbed Examples
        tab_perm, tab_comb = st.tabs([t({"de": "Permutation Beispiel", "en": "Permutation Example"}), t({"de": "Kombination Beispiel", "en": "Combination Example"})])
        
        with tab_perm:
            st.markdown(f"""
<div style="background: #fafafa; border-radius: 8px; padding: 12px; line-height: 1.8; font-size: 0.95em;">
<span style="background:#dbeafe; padding:2px 6px; border-radius:4px; color:#1d4ed8;">8 runners</span> compete in a race. 
<span style="background:#fee2e2; padding:2px 6px; border-radius:4px; color:#dc2626;">How many ways</span> can the 
<span style="background:#dbeafe; padding:2px 6px; border-radius:4px; color:#1d4ed8;">top 3 positions</span> be filled 
if there are <span style="background:#dcfce7; padding:2px 6px; border-radius:4px; color:#16a34a;">no ties</span>?
</div>
<div style="margin-top: 8px; font-size: 0.85em;">
<b>📘 Given:</b> $n=8$, $k=3$ &nbsp;|&nbsp; 
<b>🎯 Target:</b> Number of arrangements &nbsp;|&nbsp;
<b>💡 Signal:</b> "positions", "no ties" → Order matters!<br>
<span style="background:#f4f4f5; padding:2px 8px; border-radius:4px; color:#3f3f46; font-weight:600;">→ $P(8,3) = \\frac{{8!}}{{5!}} = 336$</span>
</div>
            """, unsafe_allow_html=True)
        
        with tab_comb:
            st.markdown(f"""
<div style="background: #fafafa; border-radius: 8px; padding: 12px; line-height: 1.8; font-size: 0.95em;">
From <span style="background:#dbeafe; padding:2px 6px; border-radius:4px; color:#1d4ed8;">12 students</span>, 
a <span style="background:#dcfce7; padding:2px 6px; border-radius:4px; color:#16a34a;">committee of 4</span> is 
<span style="background:#dcfce7; padding:2px 6px; border-radius:4px; color:#16a34a;">selected</span>. 
<span style="background:#fee2e2; padding:2px 6px; border-radius:4px; color:#dc2626;">How many different committees</span> are possible?
</div>
<div style="margin-top: 8px; font-size: 0.85em;">
<b>📘 Given:</b> $n=12$, $k=4$ &nbsp;|&nbsp; 
<b>🎯 Target:</b> Number of groups &nbsp;|&nbsp;
<b>💡 Signal:</b> "committee", "selected" → Order irrelevant!<br>
<span style="background:#f4f4f5; padding:2px 8px; border-radius:4px; color:#3f3f46; font-weight:600;">→ $\\binom{{12}}{{4}} = 495$</span>
</div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- SCENARIO ENGINE ---
    with st.container(border=True):
        col_ctrl, col_math = st.columns([1.5, 1], gap="large")
        
        # 1. CONTROLS
        with col_ctrl:
            st.markdown(f"<h4>{t({'de': 'Szenario', 'en': 'Scenario'})}</h4>", unsafe_allow_html=True)
            
            # Map scenarios to icons for display (NOT inside pills, but as context)
            scen_key = st.pills(
                "Scenario",
                options=["abstract", "race", "lotto"],
                format_func=lambda x: c["scenarios"][x]["label"],
                default="abstract",
                selection_mode="single",
                label_visibility="collapsed"
            )
            
            # Display active scenario icon
            icon_map = {"abstract": "shapes", "race": "trophy", "lotto": "ticket"}
            active_icon = render_icon(icon_map.get(scen_key, "shapes"), size=24)
            
            # Logic: Scenario-Lock Protocol
            # We strictly enforce the state based on the scenario to prevent illogical combinations.
            
            is_disabled = False
            toggle_value = st.session_state.get("ignore_order", False)
            
            if scen_key == "race":
                is_disabled = True
                toggle_value = False # Race ALWAYS cares about order
            elif scen_key == "lotto":
                is_disabled = True
                toggle_value = True # Lotto NEVER cares about order
            else:
                # Abstract: Let the user play (Lab Mode)
                is_disabled = False
                # Keep previous state or default to False if not set
                toggle_value = st.session_state.get("ignore_order", False)

            # Update session state immediately to ensure downstream math uses correct value
            st.session_state.ignore_order = toggle_value
            
            # Manual Toggle (Locked for descriptive scenarios)
            st.markdown("<br>", unsafe_allow_html=True)
            is_comb = st.toggle(
                t({"de": "Reihenfolge ignorieren?", "en": "Ignore Order?"}),
                value=toggle_value,
                disabled=is_disabled,
                key="ignore_order_toggle" # Changed key to avoid conflict with manual state set
            )
            
            # Sync toggle back to state if it was interactive
            if not is_disabled:
                st.session_state.ignore_order = is_comb
            
            desc = c["scenarios"][scen_key]["desc"]
            st.markdown(f"<div style='display:flex; align-items:center; gap:8px; margin-top:8px;'>{active_icon} <span>{t(desc)}</span></div>", unsafe_allow_html=True)

        # 2. MATH HUD
        with col_math:
            st.markdown("<h4>Math</h4>", unsafe_allow_html=True)
            
            # Variable Definitions (CRITICAL: Never assume students know notation)
            st.markdown("**Notation:**")
            st.markdown("- $n$ = Total items available")
            st.markdown("- $k$ = Items we select")
            st.markdown("<br>", unsafe_allow_html=True)
            
            n = 4
            k = 2
            
            if is_comb:
                # Combination - Clean, No Colors, Consistent Sizing
                st.latex(r"\binom{4}{2} = \frac{4!}{2! \cdot (4 - 2)!} = 6")
                st.caption(t({"de": "Wir teilen durch 2! (die Ghosts).", "en": "We divide by 2! (the Ghosts)."}))
            else:
                # Permutation - Clean, No Colors
                st.latex(r"P(4, 2) = \frac{4!}{(4 - 2)!} = 12")
                st.caption(t({"de": "Jede Variante zählt.", "en": "Every variation counts."}))

        st.markdown("---")
        
        # 3. THE MULTIVERSE VISUALIZATION
        st.markdown(f"### The Multiverse (n=4, k=2)")
        
        # Prepare Data
        items = c["scenarios"][scen_key]["items"]
        style_type = "medal" if scen_key == "race" else "circle"
        
        # Generate Permutations
        perms = list(itertools.permutations(items, k))
        
        # Group by Set (Canonical)
        groups = {}
        for p in perms:
            key = tuple(sorted(p))
            if key not in groups: groups[key] = []
            groups[key].append(p)
            
        # Grid Layout (3 Columns)
        grid_cols = st.columns(3)
        
        for i, (key, variations) in enumerate(groups.items()):
            c_idx = i % 3
            with grid_cols[c_idx]:
                html = f"<div class='outcome-card'>"
                
                # If Combination: Only show the first as 'Valid', others as 'Ghost'
                # If Permutation: Show all as 'Valid'
                
                for v in variations:
                    # Render Visuals
                    v_html = "".join([render_avatar(x, style_type) for x in v])
                    
                    is_canonical = (v == variations[0]) # Arbitrary 'first' is canonical
                    
                    if not is_comb:
                        # PERM: All are valid
                        html += f"<div class='perm-row'><div>{v_html}</div></div>"
                    else:
                        # COMB: First is valid, others are ghosts
                        if is_canonical:
                            html += f"<div class='perm-row canonical'><div>{v_html}</div><div>{render_icon('check-circle', color='#10b981', size=16)}</div></div>"
                        else:
                            html += f"<div class='ghost-row'><div>{v_html}</div><div class='ghost-text'>{render_icon('ghost', color='#e53935', size=14)} Ghost</div></div>"
                
                html += "</div>"
                st.markdown(html, unsafe_allow_html=True)

    # --- EXAM SECTION ---
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown(f"### {t({'de': 'Prüfungssimulation', 'en': 'Exam Simulation'})}")
    
    # Fetch from Central Repo
    q_id = "q_2_1_scenario_mastery"
    q_data = get_question("2.1", q_id)
    
    if q_data:
        with st.container(border=True):
            # Transform Options (dict list to strings)
            formatted_opts = []
            for o in q_data["options"]:
                if isinstance(o, dict):
                    formatted_opts.append(t(o)) # Localize
                else:
                    formatted_opts.append(str(o))

            render_mcq(
                key_suffix="q_2_1_scen_check",
                question_text=t(q_data["question"]),
                options=formatted_opts,
                correct_idx=q_data["correct_idx"],
                solution_text_dict=q_data["solution"],
                success_msg_dict={"de": "Richtig!", "en": "Correct!"},
                error_msg_dict={"de": "Falsch.", "en": "Incorrect."},
                client=client,
                ai_context="The student is checking their understanding of the scenario-based learning (Abstract vs Podium vs Lotto) and why removing order requires dividing by k!.",
                course_id="vwl",
                topic_id="2",
                subtopic_id="2.1",
                question_id="q_2_1_scenario_mastery"
            )
        

