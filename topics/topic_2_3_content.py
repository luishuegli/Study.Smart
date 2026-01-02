import streamlit as st
from views.styles import render_icon, inject_equal_height_css
from utils.localization import t
from utils.quiz_helper import render_mcq
from data.exam_questions import get_question

# ==============================================================================
# 1. CONTENT DICTIONARY (2.3 ONLY)
# ==============================================================================
content_2_3 = {
    "title": {"de": "2.3 Permutationen (Fakultät)", "en": "2.3 Permutations (Factorial)"},
    "theory_header": {"de": "Das Prinzip der Anordnung", "en": "The Principle of Arrangement"},
    "intro": {
        "de": "Wenn wir **alle** Elemente einer Menge verwenden und die **Reihenfolge zählt**, sprechen wir von einer Permutation (ohne Zurücklegen).",
        "en": "When we use **all** elements of a set and the **order matters**, we speak of a permutation (without replacement)."
    },
    "toy": {
        "title": {"de": "Der Vibe-Check (DJ Deck)", "en": "The Vibe Check (DJ Deck)"},
        "instr": {"de": "Ziehe Tracks in die Playlist. Beobachte, wie deine Optionen schrumpfen.", "en": "Add tracks to the playlist. Watch how your options shrink."},
        "tracks": ["Banger (A)", "Ballad (B)", "Disco (C)"],
        "track_colors": {"Banger (A)": "#EF4444", "Ballad (B)": "#3B82F6", "Disco (C)": "#F59E0B"},
        "slots": [
            {"label_de": "Opener", "label_en": "Opener", "color": "#EF4444"},
            {"label_de": "Bridge", "label_en": "Bridge", "color": "#3B82F6"},
            {"label_de": "Closer", "label_en": "Closer", "color": "#F59E0B"}
        ],
        "reveal": {
            "de": "Jeder Slot verbraucht eine Option. Das ist $n!$ (Fakultät).",
            "en": "Every slot consumes one option. This is $n!$ (Factorial)."
        }
    },
    "exam": {
        "title": {"de": "Prüfungstraining: DVD-Sammlung", "en": "Exam Practice: DVD Collection"},
        "source": "Permutation Practice",
        "scale_viz": {
            "de": "Das Ergebnis $3.04 \\cdot 10^{64}$ ist größer als die Anzahl der Atome in der Milchstraße.",
            "en": "The result $3.04 \\cdot 10^{64}$ is larger than the number of atoms in the Milky Way."
        }
    }
}

# ==============================================================================
# 2. VISUAL COMPONENT: THE CASSETTE TAPE (PURE CSS)
# ==============================================================================
def render_cassette(text, color, is_empty=False, slot_label="", options_left=0):
    """
    Renders a CSS-only Cassette Tape / Slot representation.
    Strictly No Emojis. Uses CSS borders and shadows for premium feel.
    """
    inject_equal_height_css()
    if is_empty:
        # Ghost State (The Receptacle)
        label = t({"de": f"Wähle 1 aus {options_left}", "en": f"Pick 1 of {options_left}"})
        return f"""<div style="height: 54px; border: 2px solid #e5e7eb; border-radius: 12px; background: #f9fafb; display: flex; align-items: center; justify-content: space-between; padding: 0 16px; color: #9ca3af; font-family: 'Inter', sans-serif; margin-bottom: 12px; transition: all 0.3s ease;"><span style="font-weight:600; font-size: 0.85em; text-transform:uppercase; letter-spacing: 0.5px;">{slot_label}</span><span style="background:#e5e7eb; padding: 4px 10px; border-radius: 6px; font-size: 0.8em; color: #6b7280;">{label}</span></div>"""
    else:
        # Filled State (The Physical Media) - Jony Ive Style (Clean, Depth)
        return f"""<div style="height: 54px; border-left: 6px solid {color}; border-radius: 8px; background: white; color: #1f2937; display: flex; align-items: center; justify-content: space-between; padding: 0 16px; margin-bottom: 12px; box-shadow: 0 2px 4px rgba(0,0,0,0.04), 0 1px 2px rgba(0,0,0,0.02); font-family: 'Inter', sans-serif; font-weight: 500; border: 1px solid #e5e7eb; border-left-width: 6px; animation: fadeIn 0.4s cubic-bezier(0.16, 1, 0.3, 1);"><span style="font-size: 1em;">{text}</span><div style="width: 12px; height: 12px; background: {color}; border-radius: 50%; opacity: 0.8; box-shadow: inset 0 1px 2px rgba(0,0,0,0.1);"></div></div>"""

# ==============================================================================
# 3. MAIN RENDERER
# ==============================================================================
def render_subtopic_2_3(client):
    c = content_2_3
    
    # --- CSS: SHARED STYLES ---
    st.markdown("""
        <style>
        .icon-header {
            display: flex !important;
            align-items: center !important;
            gap: 12px !important;
            margin-bottom: 12px !important;
        }
        .icon-header svg {
            flex-shrink: 0 !important;
        </style>
    """, unsafe_allow_html=True)
    
    # --- CSS: LAYOUT STABILITY & ANIMATION ---
    # NOTE: DJ Deck buttons use the .dj-deck-buttons container marker for scoped styling
    st.markdown("""
<style>
[data-testid="stHorizontalBlock"] { align-items: stretch; }
[data-testid="column"] { display: flex; flex-direction: column; }

@keyframes fadeIn { from { opacity: 0; transform: translateY(8px); } to { opacity: 1; transform: translateY(0); } }

/* Scaling fix for icon rendering */
svg { width: 1.5rem; height: 1.5rem; }

/* Tame the Math: Prevent KaTeX from exploding */
.katex { font-size: 1.1em !important; }

/* DJ DECK BUTTONS ONLY - Scoped by container class */
.dj-deck-buttons button {
    height: 54px !important;
    border-radius: 8px !important;
    font-weight: 600 !important;
    font-size: 1rem !important;
}

/* Also style primary buttons in the crate column */
.dj-deck-buttons [data-testid="stButton"] button[kind="primary"] {
    background-color: #1a1a1a !important;
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

    c = content_2_3
    
    # --- HEADER ---
    st.header(t(c["title"]))
    st.markdown("---")
    
    # --- THEORY SECTION ---
    st.markdown(f"### {t(c['theory_header'])}")
    with st.container(border=True):
        col_t1, col_t2 = st.columns([1, 1], gap="medium")
        with col_t1:
            st.markdown(f"**{t({'de': 'Definition', 'en': 'Definition'})}**")
            st.markdown(t({
                "de": "Wenn wir **alle** Elemente einer Menge verwenden und die **Reihenfolge zählt**, sprechen wir von einer Permutation (ohne Zurücklegen).",
                "en": "When we use **all** elements of a set and the **order matters**, we speak of a permutation (without replacement)."
            }))
            
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown(f"**{t({'de': 'Notation', 'en': 'Notation'})}**")
            st.markdown("- $n$ = " + t({"de": "Gesamtzahl der Elemente", "en": "Total number of elements"}))
            st.markdown("- $k$ = " + t({"de": "Anzahl ausgewählter Elemente", "en": "Number of selected elements"}))
            
        with col_t2:
             st.markdown(f"**{t({'de': 'Formeln', 'en': 'Formulas'})}**")
             st.latex(r"P(n, k) = \frac{n!}{(n-k)!}")
             st.caption(t({
                 "de": "Permutation: k Elemente aus n auswählen (Reihenfolge zählt)",
                 "en": "Permutation: select k elements from n (order matters)"
             }))
             
             st.markdown("<br>", unsafe_allow_html=True)
             st.latex(r"P(n, n) = n!")
             st.caption(t({
                 "de": "Spezialfall: Alle n Elemente anordnen",
                 "en": "Special case: arrange all n elements"
             }))
    
    # NEW: Permutations with Repetition (MISSISSIPPI-type problems)
    st.markdown("<br>", unsafe_allow_html=True)
    with st.container(border=True):
        st.markdown(f"**{t({'de': 'Permutation mit Wiederholung', 'en': 'Permutations with Repetition'})}**")
        st.markdown(t({
            "de": "Wenn Elemente **mehrfach vorkommen**, müssen wir die identischen Anordnungen herausdividieren.",
            "en": "When elements **repeat**, we must divide out the identical arrangements."
        }))
        
        col_form, col_ex = st.columns([1, 1], gap="medium")
        
        with col_form:
            st.latex(r"\text{Permutations} = \frac{n!}{n_1! \cdot n_2! \cdots n_k!}")
            st.caption(t({
                "de": "$n_i$ = Anzahl der Wiederholungen pro Element",
                "en": "$n_i$ = count of each repeated element"
            }))
        
        with col_ex:
            st.markdown(f"**{t({'de': 'Klassiker: MISSISSIPPI', 'en': 'Classic: MISSISSIPPI'})}**")
            st.markdown(t({
                "de": "11 Buchstaben: M(1), I(4), S(4), P(2)",
                "en": "11 letters: M(1), I(4), S(4), P(2)"
            }))
            st.latex(r"\frac{11!}{1! \cdot 4! \cdot 4! \cdot 2!} = 34,650")

    st.markdown("<br>", unsafe_allow_html=True)

    # --- INTERACTIVE TOY: THE DJ DECK ---
    with st.container(border=True):
        st.markdown(f"### {t(c['toy']['title'])}")
        st.caption(t(c["toy"]["instr"]))
        
        # State Management
        if "playlist_2_3" not in st.session_state:
            st.session_state.playlist_2_3 = []
            
        current_queue = st.session_state.playlist_2_3
        all_tracks = c["toy"]["tracks"]
        available_tracks = [t for t in all_tracks if t not in current_queue]
        
        # Layout: [Crate (Actions)] | [Queue (Visuals)]
        col_crate, col_queue = st.columns([1, 1.2], gap="large")
        
        # --- LEFT: THE CRATE (ACTION) ---
        with col_crate:
            st.markdown(f"**{t({'de': 'Plattenkiste (Optionen)', 'en': 'Crate (Options)'})}**")
            
            # Start DJ Deck buttons wrapper for scoped styling
            st.markdown('<div class="dj-deck-buttons">', unsafe_allow_html=True)
            
            if not available_tracks and len(current_queue) == 3:
                # Success State
                st.success(t({"de": "Set komplett!", "en": "Set Complete!"}))
                if st.button(t({"de": "Reset Mix", "en": "Reset Mix"}), type="secondary", use_container_width=True):
                    st.session_state.playlist_2_3 = []
                    st.rerun()
            else:
                # Render Available Buttons
                for track in available_tracks:
                    # Pure text button, no emoji, per Premium feel
                    if st.button(f"{track}", key=f"btn_{track}", use_container_width=True, type="primary"):
                        st.session_state.playlist_2_3.append(track)
                        st.rerun()
                
                left_count = len(available_tracks)
                st.caption(f"{left_count} {t({'de': 'Tracks übrig', 'en': 'tracks remaining'})}")
            
            # End DJ Deck buttons wrapper
            st.markdown('</div>', unsafe_allow_html=True)

        # --- RIGHT: THE QUEUE (VISUAL) ---
        with col_queue:
            st.markdown(f"**{t({'de': 'Die Playlist (Reihenfolge)', 'en': 'The Playlist (Order)'})}**")
            
            slots = c["toy"]["slots"]
            
            for i in range(3):
                # Localize label
                label_key = "label_de" if st.session_state.lang == "de" else "label_en"
                slot_label = slots[i][label_key]
                options_remaining = 3 - i
                
                if i < len(current_queue):
                    # Filled: Show the Cassette
                    track_name = current_queue[i]
                    color = c["toy"]["track_colors"].get(track_name, "#333")
                    html = render_cassette(track_name, color, is_empty=False)
                else:
                    # Empty: Show the Ghost Receptacle
                    html = render_cassette("", "#ccc", is_empty=True, slot_label=slot_label, options_left=options_remaining)
                
                st.markdown(html, unsafe_allow_html=True)

        # --- MATH HUD (FOOTER) ---
        st.markdown("---")
        
        step = len(current_queue)
        
        # Helper to generate Dynamic LaTeX Color String
        def fmt_num(val, idx):
            # Active color matches the slot color logic (just use bold for simplicity or specific colors)
            if idx == step: return f"\\color{{#EF4444}}{{\\mathbf{{{val}}}}}" 
            if idx < step: return f"{val}" 
            return f"\\color{{#ccc}}{{{val}}}" 
            
        n1 = fmt_num(3, 0)
        n2 = fmt_num(2, 1)
        n3 = fmt_num(1, 2)
        
        c_math, c_txt = st.columns([1, 1.5], vertical_alignment="center")
        with c_math:
            st.latex(rf"N = {n1} \times {n2} \times {n3} = 6")
        with c_txt:
            if step == 3:
                st.info(t(c["toy"]["reveal"]))
            else:
                st.caption(t({"de": "Jeder Song, den du wählst, wird Teil der Formel.", "en": "Every song you pick becomes part of the formula."}))

    # --- EXAM SECTION ---
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown(f"### {t(c['exam']['title'])}")
    st.caption(c["exam"]["source"])
    
    with st.container(border=True):
        q_data = get_question("2.3", "dvd_collection")
        
        # Translate options
        opts = q_data.get("options", [])
        if opts and isinstance(opts[0], dict):
            option_labels = [t(o) for o in opts]
        else:
            option_labels = opts
        
        render_mcq(
            key_suffix="2_3_dvd",
            question_text=t(q_data["question"]),
            options=option_labels,
            correct_idx=q_data["correct_idx"],
            solution_text_dict=q_data["solution"],
            success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
            error_msg_dict={"de": "Falsch.", "en": "Incorrect."},
            client=client,
            ai_context="Topic: Permutations without replacement (Factorial). Problem: 50 DVDs in 50 Cases.",
            course_id="stats_hsg",
            topic_id="2",
            subtopic_id="2.3",
            question_id="q_2_3_dvd"
        )
        
        # --- SCALE VISUALIZATION (THE SHELF) ---
        # A visual bridge between the toy (3) and the exam (50)
        if st.toggle(t({"de": "Visualisierung (Größenordnung)", "en": "Visualize Scale"})):
            st.markdown(f"""
<div style="
margin-top: 10px;
padding: 20px;
background: #f9fafb;
border-radius: 12px;
border: 1px solid #e5e7eb;
overflow-x: auto;
">
<div style="font-size:0.8em; color:#6b7280; margin-bottom:12px; text-transform:uppercase; letter-spacing:1px; font-weight:600;">The Factorial Chain (n=50)</div>
<div style="display: flex; gap: 8px; align-items: flex-end; justify-content: flex-start; font-family: 'Menlo', monospace; height: 40px;">
<div style="text-align:center;"><span style="color:#EF4444; font-weight:bold; font-size:1.2em;">50</span></div>
<span style="color:#9ca3af; padding-bottom: 4px;">×</span>
<div style="text-align:center;"><span style="color:#3B82F6; font-weight:bold; font-size:1.1em;">49</span></div>
<span style="color:#9ca3af; padding-bottom: 4px;">×</span>
<div style="text-align:center;"><span style="color:#F59E0B; font-weight:bold; font-size:1.1em;">48</span></div>
<span style="color:#d1d5db; margin: 0 10px; padding-bottom: 4px;">... × ...</span>
<div style="text-align:center;"><span style="color:#6b7280; font-weight:bold;">1</span></div>
</div>
<div style="text-align: left; margin-top: 16px; font-size: 0.95em; color: #374151; border-top: 1px dashed #d1d5db; padding-top: 12px;">
Result: <b>3.04 × 10⁶⁴</b> <span style="color: #6b7280; font-style: italic; margin-left:8px;">&mdash; {t(c['exam']['scale_viz'])}</span>
</div>
</div>
""", unsafe_allow_html=True)

    # --- ADDITIONAL EXAM QUESTIONS ---
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown(f"### {t({'de': 'Weitere Prüfungsaufgaben', 'en': 'Additional Exam Questions'})}")
    
    def render_perm_q(q_id, key_suffix, question_key, source_caption):
        q_data = get_question("2.3", q_id)
        if not q_data:
            st.warning(f"Question {q_id} not found")
            return
        
        opts = q_data.get("options", [])
        if opts and isinstance(opts[0], dict):
            option_labels = [t(o) for o in opts]
        else:
            option_labels = opts
        
        with st.container(border=True):
            st.caption(source_caption)
            render_mcq(
                key_suffix=key_suffix,
                question_text=t(q_data['question']),
                options=option_labels,
                correct_idx=q_data['correct_idx'],
                solution_text_dict=q_data['solution'],
                success_msg_dict={"de": "Richtig!", "en": "Correct!"},
                error_msg_dict={"de": "Falsch.", "en": "Incorrect."},
                client=client,
                ai_context=f"Topic 2.3: Permutations. Question: {q_id}",
                course_id="vwl", topic_id="2", subtopic_id="2.3", question_id=question_key
            )
    
    render_perm_q("test1_q3", "2_3_test1_q3", "2_3_test1_q3", "Test 1, Frage 3")
    st.markdown("<br>", unsafe_allow_html=True)
    render_perm_q("hs2015_mc4", "2_3_hs2015_mc4", "2_3_hs2015_mc4", "HS 2015 Januar, MC #4 (Schliessfach)")
