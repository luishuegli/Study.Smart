import streamlit as st
import re
from views.styles import render_icon
from utils.localization import t
from utils.quiz_helper import render_mcq

# --- CONTENT DICTIONARY ---
content_2_2 = {
    "title": {"de": "2.2 Das Fundamentalprinzip", "en": "2.2 The Fundamental Principle"},
    "anchor": {"de": "Problem: Der Kleiderschrank ist voll. Aber wie viele Outfits kannst du wirklich erstellen?", "en": "Problem: The closet is full. But how many unique outfits can you create?"},
    "toy_instr": {"de": "Mission: Kombiniere Hemden und Hosen. Beobachte, wie das Gitter wächst.", "en": "Mission: Combine shirts and pants. Watch the grid grow."},
    "items": {
        "shirts": ["Red", "Blue", "Green", "Yellow"],
        "pants": ["Jeans", "Chinos", "Shorts"]
    },
    "colors": {
        "Red": "#EF4444", "Blue": "#3B82F6", "Green": "#10B981", "Yellow": "#F59E0B",
        "Jeans": "#1E3A8A", "Chinos": "#D97706", "Shorts": "#9CA3AF"
    },
    "math_reveal": {
        "de": "Intuitiv: Für jedes der **{n_s}** Hemden gibt es **{n_p}** Hosen-Optionen.", 
        "en": "Intuition: For each of the **{n_s}** shirts, there are **{n_p}** pants options."
    },
    "relate": {
        "de": "Das ist das **Fundamentalprinzip**: Unabhängige Entscheidungen werden **multipliziert**.",
        "en": "This is the **Fundamental Principle**: Independent choices are **multiplied**."
    },
    "exam_q": {
        "q": {"de": "In einem Verein mit 10 Mitgliedern (4 Frauen und 6 Herren) soll nun ein Vorstand bestehend aus zwei Damen und zwei Herren gebildet werden. Wie viele Möglichkeiten gibt es?", 
              "en": "In a club with 10 members (4 women and 6 men), a board consisting of two women and two men is to be formed. How many possibilities are there?"},
        "opts": ["90", "25", "210", "60"],
        "sol": {"de": "<div style='margin-bottom:16px;'>Formel: $\\binom{n}{k} = \\frac{n!}{k!(n-k)!}$</div><div style='margin-bottom:12px;'>Frauen: $\\binom{4}{2} = 6$<br>Männer: $\\binom{6}{2} = 15$</div><div>Fundamentalprinzip: $6 \\cdot 15 = 90$</div>", 
                "en": "<div style='margin-bottom:16px;'>Formula: $\\binom{n}{k} = \\frac{n!}{k!(n-k)!}$</div><div style='margin-bottom:12px;'>Women: $\\binom{4}{2} = 6$<br>Men: $\\binom{6}{2} = 15$</div><div>Principle: $6 \\cdot 15 = 90$</div>"}
    }
}

# --- VISUAL HELPERS ---
def render_clothing_stack(shirt_name, pant_name, colors):
    """
    Renders a premium stacked visual of Shirt + Pants using pure CSS (No Emojis).
    Design: Flat design with subtle border boxing for depth.
    """
    s_col = colors.get(shirt_name, "#ccc")
    p_col = colors.get(pant_name, "#666")
    
    return f"""<div style="display:flex; flex-direction:column; align-items:center; margin: 4px;">
        <div style="width:34px; height:24px; background:{s_col}; border-radius: 6px 6px 2px 2px; border:1px solid rgba(0,0,0,0.05); box-shadow: inset 0 -2px 0 rgba(0,0,0,0.1);" title="{shirt_name}"></div>
        <div style="width:30px; height:32px; background:{p_col}; border-radius: 0 0 6px 6px; border:1px solid rgba(0,0,0,0.05); margin-top:-2px; z-index:2;" title="{pant_name}"></div>
    </div>""".replace("\n", "")

def get_committee_matrix_html(rows=6, cols=15):
    """Generates the HTML for the 6x15 Committee Matrix Grid."""
    total = rows * cols
    
    # Generate cells
    cells = ""
    for r in range(rows):
        for c in range(cols):
            cells += f"<div class='matrix-cell' title='Option {r*cols + c + 1}'></div>"
            
    # Aggressive cleanup: remove leading spaces from every line
    def clean(s):
        return re.sub(r'^\s+', '', s, flags=re.MULTILINE)

    css = clean(f"""
    <style>
    .matrix-container {{
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 8px;
        padding: 16px;
        background: #f8f9fa;
        border-radius: 12px;
        border: 1px solid #e0e0e0;
    }}
    .matrix-grid {{
        display: grid;
        grid-template-columns: repeat({cols}, 1fr);
        gap: 3px;
        width: 100%;
        max-width: 600px;
    }}
    .matrix-cell {{
        aspect-ratio: 1;
        background-color: #E0E7FF;
        border: 1px solid #C7D2FE;
        border-radius: 2px;
        transition: all 0.1s ease;
        cursor: pointer;
    }}
    .matrix-cell:hover {{
        background-color: #4F46E5;
        border-color: #3730A3;
        transform: scale(1.3);
        z-index: 10;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }}
    .matrix-axis-label {{
        font-family: monospace;
        font-size: 0.8em;
        color: #666;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
    }}
    </style>
    """)
    
    html = clean(f"""
    <div class="matrix-container">
        <!-- Top Label -->
        <div class="matrix-axis-label" style="color:#1E88E5;">
            ← {cols} Men-Pairs (Columns) →
        </div>
        
        <div style="display:flex; width:100%; justify-content:center; align-items:center; gap:8px;">
            <!-- Left Label -->
            <div class="matrix-axis-label" style="writing-mode: vertical-lr; text-orientation: mixed; transform: rotate(180deg); color:#E53935;">
                ← {rows} Women-Pairs (Rows) →
            </div>
            
            <!-- The Grid -->
            <div class="matrix-grid">
                {cells}
            </div>
        </div>
        
        <!-- Bottom KPI -->
        <div style="margin-top:8px; font-family:monospace; font-weight:bold; color:#333;">
            Area = <span style="color:#E53935;">{rows}</span> × <span style="color:#1E88E5;">{cols}</span> = <span style="color:#10B981;">{total}</span>
        </div>
    </div>
    """)
    
    return css + html

def render_subtopic_2_2(client):
    c = content_2_2
    
    st.markdown(f"## {t(c['title'])}")
    st.markdown(f"**{t(c['anchor'])}**")

    # =========================================================================
    # THEORY SECTION - COMPREHENSIVE PEDAGOGICAL CONTENT
    # =========================================================================
    st.markdown(f"### {t({'de': 'Theorie: Das Multiplikationsprinzip', 'en': 'Theory: The Multiplication Principle'})}")
    
    with st.container(border=True):
        # --- ROW 1: THE KEY INSIGHT ---
        st.markdown(f"""
<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 12px; padding: 20px; border-left: 4px solid #10b981; margin-bottom: 16px;">
    <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 8px;">
        <div style="background: #ecfdf5; padding: 6px; border-radius: 50%; display: flex; align-items: center; justify-content: center;">{render_icon('zap', size=18, color='#10b981')}</div>
        <div style="font-size: 0.85em; text-transform: uppercase; letter-spacing: 1px; font-weight: 600; color: #10b981;">{t({'de': 'Die goldene Regel', 'en': 'The Golden Rule'})}</div>
    </div>
    <div style="display: flex; gap: 40px; align-items: center;">
        <div>
            <div style="font-size: 1.2em; font-weight: 700; color: #1e293b;">{t({'de': 'UND', 'en': 'AND'})}</div>
            <div style="font-size: 0.9em; color: #64748b;">{t({'de': 'Entscheidungs-Kette', 'en': 'Choice Chain'})}</div>
            <div style="font-size: 1.5em; font-weight: 800; color: #10b981; margin-top: 4px;">&times;</div>
        </div>
        <div style="width: 1px; height: 40px; background: #e2e8f0;"></div>
        <div>
            <div style="font-size: 1.2em; font-weight: 700; color: #1e293b;">{t({'de': 'ODER', 'en': 'OR'})}</div>
            <div style="font-size: 0.9em; color: #64748b;">{t({'de': 'Alternativen', 'en': 'Alternatives'})}</div>
            <div style="font-size: 1.5em; font-weight: 800; color: #64748b; margin-top: 4px;">+</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
        
        # --- ROW 2: MENTAL MODEL - NARRATIVE & FORMULA ---
        # Adjusted weights to 1:1 for better symmetry
        col_text, col_form = st.columns([1, 1], gap="large")
        
        with col_text:
            st.markdown(f"#### {t({'de': 'Das Gedankenmodell', 'en': 'The Mental Model'})}")
            # Subtle background and padding to even out the visual weight with the Formula box
            st.markdown(f"""
<div style="background: #fafafa; border-radius: 12px; padding: 16px; border: 1px solid #f1f5f9; min-height: 200px;">
<p style="margin-top: 0; font-weight: 500; color: #475569;">{t({'de': 'Stell dir vor, du stehst an einer Weggabelung:', 'en': 'Imagine standing at a fork in the road:'})}</p>
<ol style="margin-bottom: 0; color: #1e293b;">
<li><b>{t({'de': 'Entscheidung 1:', 'en': 'Decision 1:'})}</b> {t({'de': 'Du wählst ein Hemd', 'en': 'You pick a shirt'})} (<span style="color:#007AFF; font-weight:600;">3 options</span>)</li>
<li><b>{t({'de': 'Für JEDES Hemd:', 'en': 'For EACH shirt:'})}</b> {t({'de': 'Du wählst eine Hose', 'en': 'You pick pants'})} (<span style="color:#FF4B4B; font-weight:600;">4 options</span>)</li>
</ol>
<div style="margin-top: 16px; padding-top: 12px; border-top: 1px dashed #e2e8f0; font-size: 0.95em;">
{t({'de': 'Anzahl der Pfade', 'en': 'Number of paths'})} = <span style="color:#007AFF; font-weight:600;">3</span> × <span style="color:#FF4B4B; font-weight:600;">4</span> = <b>12</b>
</div>
</div>
""", unsafe_allow_html=True)
            
        with col_form:
            st.markdown(f"#### {t({'de': 'Die Formel', 'en': 'The Formula'})}")
            
            # Use a container to match the height and styling of the left side
            with st.container(border=True):
                st.latex(r"N = \color{#007AFF}{n}_1 \cdot \color{#FF4B4B}{n}_2 \cdot \dots \cdot n_k")
                
                # --- PARAMETER SPEC LIST (Rounded & Natural) ---
                def render_spec_row(label, desc, color="#64748b"):
                    return f"""<div style="display: flex; align-items: center; gap: 12px; padding: 10px 12px; background: #fafafa; border-radius: 8px; margin-bottom: 6px;"><div style="min-width: 40px; font-family: serif; font-size: 1.1em; font-weight: 600; color: {color}; text-align: center;">{label}</div><div style="font-size: 0.9em; color: #475569;">{desc}</div></div>"""

                st.markdown(f"""
<div style="margin-top: 12px; border-top: 1px dashed #e2e8f0; padding-top: 12px;">
{render_spec_row("$k$", t({"de": "Anzahl Entscheidungen", "en": "Number of selection steps"}))}
{render_spec_row("$n_1$", t({"de": "Optionen bei Schritt 1", "en": "Options at step 1"}), color="#007AFF")}
{render_spec_row("$n_2$", t({"de": "Optionen bei Schritt 2", "en": "Options at step 2"}), color="#FF4B4B")}
<div style="display: flex; align-items: center; gap: 12px; padding: 10px 12px; background: #ecfdf5; border-radius: 8px; margin-top: 10px; border: 1px solid #d1fae5;">
<div style="min-width: 40px; font-family: serif; font-size: 1.1em; font-weight: 800; color: #10B981; text-align: center;">$N$</div>
<div style="font-size: 0.9em; font-weight: 600; color: #064e3b;">{t({"de": "Ergebnis", "en": "Result"})}</div>
</div>
</div>
""", unsafe_allow_html=True)

        # --- ROW 3: FULL WIDTH DECISION TREE ---
        st.markdown("<br>", unsafe_allow_html=True)
        # --- SVG DECISION TREE (Show, Don't Tell) ---
        # CRITICAL: NO INDENTATION AT ALL OR MARKDOWN WILL RENDER AS CODE BLOCK
        tree_svg = f"""
<div style="margin: 16px 0; background: #fafafa; border-radius: 12px; padding: 24px; border: 1px solid #f1f5f9;">
<svg viewBox="0 0 500 150" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
<!-- Root -->
<circle cx="40" cy="75" r="5" fill="#334155" />
<text x="38" y="90" font-size="10" text-anchor="middle" fill="#64748b">Start</text>
<!-- Shirt Branches (n1=3) -->
<line x1="40" y1="75" x2="150" y2="25" stroke="#cbd5e1" stroke-width="2" />
<circle cx="150" cy="25" r="5" fill="#007AFF" />
<line x1="40" y1="75" x2="150" y2="75" stroke="#cbd5e1" stroke-width="2" />
<circle cx="150" cy="75" r="5" fill="#007AFF" />
<line x1="40" y1="75" x2="150" y2="125" stroke="#cbd5e1" stroke-width="2" />
<circle cx="150" cy="125" r="5" fill="#007AFF" />
<text x="150" y="15" font-size="10" text-anchor="middle" font-weight="600" fill="#007AFF">n₁ = 3</text>
<!-- Pants Branches (n2=4 per shirt) -->
<line x1="150" y1="25" x2="300" y2="5" stroke="#f1f5f9" stroke-width="1.5" />
<line x1="150" y1="25" x2="300" y2="15" stroke="#f1f5f9" stroke-width="1.5" />
<line x1="150" y1="25" x2="300" y2="35" stroke="#f1f5f9" stroke-width="1.5" />
<line x1="150" y1="25" x2="300" y2="45" stroke="#f1f5f9" stroke-width="1.5" />
<line x1="150" y1="75" x2="300" y2="55" stroke="#f1f5f9" stroke-width="1.5" />
<line x1="150" y1="75" x2="300" y2="65" stroke="#f1f5f9" stroke-width="1.5" />
<line x1="150" y1="75" x2="300" y2="85" stroke="#f1f5f9" stroke-width="1.5" />
<line x1="150" y1="75" x2="300" y2="95" stroke="#f1f5f9" stroke-width="1.5" />
<line x1="150" y1="125" x2="300" y2="105" stroke="#f1f5f9" stroke-width="1.5" />
<line x1="150" y1="125" x2="300" y2="115" stroke="#f1f5f9" stroke-width="1.5" />
<line x1="150" y1="125" x2="300" y2="135" stroke="#f1f5f9" stroke-width="1.5" />
<line x1="150" y1="125" x2="300" y2="145" stroke="#f1f5f9" stroke-width="1.5" />
<g fill="#FF4B4B">
<circle cx="300" cy="5" r="3" /><circle cx="300" cy="15" r="3" /><circle cx="300" cy="35" r="3" /><circle cx="300" cy="45" r="3" />
<circle cx="300" cy="55" r="3" /><circle cx="300" cy="65" r="3" /><circle cx="300" cy="85" r="3" /><circle cx="300" cy="95" r="3" />
<circle cx="300" cy="105" r="3" /><circle cx="300" cy="115" r="3" /><circle cx="300" cy="135" r="3" /><circle cx="300" cy="145" r="3" />
</g>
<text x="300" y="155" font-size="10" text-anchor="middle" font-weight="600" fill="#FF4B4B">n₂ = 4</text>
<rect x="360" y="55" width="120" height="40" rx="8" fill="#ecfdf5" stroke="#10B981" stroke-width="1" />
<text x="420" y="80" font-size="14" font-weight="800" text-anchor="middle" fill="#10B981">Total = 12</text>
</svg>
</div>
"""
        st.markdown(tree_svg, unsafe_allow_html=True)
    
    # --- ROW 3: THE TRAP ---
    st.markdown("<br>", unsafe_allow_html=True)
    with st.container(border=True):
        st.markdown(f"""
<div style="display: flex; align-items: center; gap: 8px; margin-bottom: 8px;">
{render_icon('info', size=18, color='#3b82f6')} 
<span style="font-weight: 600; color: #1e293b;">{t({'de': 'Die Falle: Unabhängigkeit prüfen!', 'en': 'The Trap: Check Independence!'})}</span>
</div>
""", unsafe_allow_html=True)

        st.markdown(t({
            'de': 'Das Multiplikationsprinzip gilt <b>nur für unabhängige Entscheidungen</b>.', 
            'en': 'The multiplication principle <b>only works for independent choices</b>.'}), unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown(t({
            'de': '<b>Unabhängig:</b> Hemd wählen UND Hose wählen (Hemd beeinflusst Hosen-Optionen nicht)', 
            'en': "<b>Independent:</b> Choose shirt AND choose pants (shirt doesn't affect pants options)"}), unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown(t({
            'de': '<b>NICHT unabhängig:</b> "Wähle 2 Personen aus 5" ≠ 5 × 4 (das wäre Overcounting!)', 
            'en': '<b>NOT independent:</b> "Choose 2 people from 5" ≠ 5 × 4 (that\'s overcounting!)'}), unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown(f"<b>{t({'de': 'Faustregel:', 'en': 'Rule of thumb:'})}</b> " + t({'de': 'Wenn die erste Wahl die zweite beeinflusst → prüfe genau!', 'en': 'If the first choice affects the second → check carefully!'}))

        # --- INTEGRATED DECISION GUIDE (Rounded List Strategy) ---
        st.markdown("<hr style='margin: 20px 0; border: 0; border-top: 1px dashed #e2e8f0;'>", unsafe_allow_html=True)
        st.markdown(f"**{t({'de': 'Entscheidungshilfe: Wann welche Formel?', 'en': 'Decision Guide: When to Use What?'})}**")
        
        def render_guide_row(situation, formula, is_primary=False):
            bg = "#f8fafc" if not is_primary else "#eff6ff"
            border = "1px solid #e2e8f0" if not is_primary else "1px solid #bfdbfe"
            return f"""<div style="display: flex; justify-content: space-between; align-items: center; padding: 12px 16px; background: {bg}; border: {border}; border-radius: 10px; margin-bottom: 8px;"><div style="font-size: 0.95em; color: #1e293b; font-weight: 500;">{situation}</div><div style="font-family: serif; font-size: 1.1em; font-weight: 600; color: {'#2563eb' if is_primary else '#475569'};">{formula}</div></div>"""

        row1_text = t({"de": "Unabhängige Entscheidungen (Hemd UND Hose)", "en": "Independent choices (shirt AND pants)"})
        row1_formula = "$N = n_1 \cdot n_2$"
        row2_text = t({"de": "Auswahl ohne Reihenfolge (Team bilden)", "en": "Selection without order (form a team)"})
        row2_formula = "$\\binom{n}{k}$"
        row3_text = t({"de": "Auswahl mit Reihenfolge (Podium)", "en": "Selection with order (podium)"})
        row3_formula = "$P(n,k)$"
        row4_text = t({"de": "Mit Wiederholung (PIN-Code)", "en": "With repetition (PIN code)"})
        row4_formula = "$n^k$"

        st.markdown(f"""
<div style="margin-top: 12px;">
{render_guide_row(row1_text, row1_formula, is_primary=True)}
{render_guide_row(row2_text, row2_formula)}
{render_guide_row(row3_text, row3_formula)}
{render_guide_row(row4_text, row4_formula)}
</div>
""", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)

    # --- THE INTERACTIVE MATRIX ---
    with st.container(border=True):
        col_head, _ = st.columns([2, 1])
        with col_head:
            st.markdown(f"### {t({'de': 'Der Outfit-Konfigurator', 'en': 'The Outfit Configurator'})}")
        
        # 1. Split Layout: Inputs (Builder) | Visual (Matrix)
        col_inp, col_vis = st.columns([1, 2], gap="large")
        
        with col_inp:
            st.caption(t(c["toy_instr"]))
            st.markdown("<br>", unsafe_allow_html=True)
            
            # --- BUILDER INTERFACE (Pills) ---
            # Shirts (Rows)
            st.markdown(f"**{t({'de': 'Hemden', 'en': 'Shirts'})}** ($n_1$)")
            
            # Fix Double-Click: Explicit State Init
            if "pills_shirts" not in st.session_state:
                st.session_state.pills_shirts = ["Red", "Blue"]
                
            # Fix Double-Click/No-Update: Use callbacks to force rerun on change
            def on_change_handler():
                pass # Streamlit triggers rerun automatically on change, but passing this ensures event binding

            sel_shirts = st.pills("Shirts", c["items"]["shirts"], selection_mode="multi", key="pills_shirts", label_visibility="collapsed", on_change=on_change_handler)
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            # Pants (Cols)
            st.markdown(f"**{t({'de': 'Hosen', 'en': 'Pants'})}** ($n_2$)")
            
            if "pills_pants" not in st.session_state:
                st.session_state.pills_pants = ["Jeans"]
                
            sel_pants = st.pills("Pants", c["items"]["pants"], selection_mode="multi", key="pills_pants", label_visibility="collapsed", on_change=on_change_handler)
            
            # Defensive Defaults
            if not sel_shirts: sel_shirts = []
            if not sel_pants: sel_pants = []

            # Live Notation (Dynamic Formula)
            n_s = len(sel_shirts)
            n_p = len(sel_pants)
            total = n_s * n_p
            
            st.markdown("<br><hr style='margin:10px 0; border-top: 1px solid #eee;'>", unsafe_allow_html=True)
            st.markdown(f"""
<div style="
background: #F8F9FA; 
border-radius: 12px; 
padding: 16px; 
border: 1px solid #E0E0E0;
text-align: center;
font-family: 'Inter', sans-serif;
">
<div style="font-size: 0.85em; color: #666; margin-bottom: 8px; font-weight: 500;">LIVE MATH</div>
<div style="display: flex; align-items: center; justify-content: center; gap: 8px; font-size: 1.4em; font-weight: 600;">
<div style="color: #007AFF;" title="n1 (Shirts)">{n_s}</div>
<div style="color: #ccc;">×</div>
<div style="color: #FF4B4B;" title="n2 (Pants)">{n_p}</div>
<div style="color: #ccc;">=</div>
<div style="color: #10B981;">{total}</div>
</div>
<div style="
margin-top: 8px; 
font-size: 0.8em; 
color: #888; 
border-top: 1px solid #eee; 
padding-top: 6px;
">
Total (N) = <span style="color:#007AFF;">n₁</span> · <span style="color:#FF4B4B;">n₂</span>
</div>
</div>
""", unsafe_allow_html=True)
            
            # Relate (Connection)
            if total > 0:
                relate_msg = t(c["relate"])
                # Use columns to ensure Markdown renders correctly (HTML block kills Markdown parsing)
                c_ico, c_txt = st.columns([0.15, 0.85], gap="small")
                with c_ico:
                    st.markdown(f"<div style='margin-top:2px;'>{render_icon('lightbulb')}</div>", unsafe_allow_html=True)
                with c_txt:
                    st.markdown(relate_msg)

        with col_vis:
            # --- THE VISUAL GRID (Proof) ---
            if total > 0:
                # Dynamic CSS Grid: The layout itself is the math lesson.
                # Columns = n_pants. Rows = n_shirts.
                st.markdown(f"""
<style>
.visual-stage {{
display: flex;
justify-content: center;
align-items: center;
min-height: 450px; /* Adaptive height to match left column */
width: 100%;
}}
.wardrobe-grid {{
display: grid;
grid-template-columns: repeat({max(1, n_p)}, 120px);
justify-content: center;
gap: 12px;
padding: 12px;
/* Removed border and background for cleaner look */
}}
.wardrobe-item {{
background: white; border: 1px solid #e0e0e0; border-radius: 8px;
display: flex; justify-content: center; align-items: center; padding: 12px;
aspect-ratio: 1 / 1;
box-shadow: 0 1px 2px rgba(0,0,0,0.03);
transition: transform 0.2s ease, box-shadow 0.2s ease;
}}
.wardrobe-item:hover {{ 
transform: translateY(-2px) scale(1.02); 
box-shadow: 0 4px 8px rgba(0,0,0,0.08); 
border-color: #3B82F6; 
}}
</style>
""", unsafe_allow_html=True)
                
                # Render Grid Items wrapped in Stage
                grid_html = "<div class='visual-stage'><div class='wardrobe-grid'>"
                for shirt in sel_shirts:
                    for pant in sel_pants:
                        icon = render_clothing_stack(shirt, pant, c['colors'])
                        grid_html += f"<div class='wardrobe-item'>{icon}</div>"
                grid_html += "</div></div>"
                
                st.markdown(grid_html, unsafe_allow_html=True)
                st.caption(t(c["math_reveal"]))
            else:
                # Empty State
                st.info(t({"de": "Wähle mindestens ein Hemd und eine Hose.", "en": "Select at least one shirt and pants."}))

    # --- EXAM SECTION ---
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown(f"### {t({'de': 'Prüfungstraining', 'en': 'Exam Practice'})}")
    
    with st.container(border=True):
        render_mcq(
            key_suffix="2_2_exam", 
            question_text=t(c["exam_q"]["q"]), 
            options=c["exam_q"]["opts"], 
            correct_idx=0, # 90
            solution_text_dict=c["exam_q"]["sol"], 
            success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
            error_msg_dict={"de": "Falsch.", "en": "Incorrect."}, 
            client=client, 
            ai_context="The user is learning the Fundamental Counting Principle. The problem involves combining choices (women, men) using multiplication.",
            course_id="vwl", topic_id="2", subtopic_id="2.2", question_id="q_2_2_club"
        )
        
        # Visual Solution: The "Slot Machine"
        if st.toggle(t({"de": "Lösung visualisieren", "en": "Visualize Solution"})):
            # The Committee Matrix (6x15 Grid)
            # Safe HTML Header to prevent SVG issues
            st.markdown(f"""
<div style="display:flex; align-items:center; gap:8px; margin-bottom:4px;">
{render_icon('layout-grid')}
<h4 style="margin:0; padding:0;">The Committee Matrix</h4>
</div>
""", unsafe_allow_html=True)
            
            st.caption(t({
                "de": "Jede Zelle ist ein möglicher Vorstand. 6 Zeilen (Frauen-Paare) × 15 Spalten (Männer-Paare).",
                "en": "Every cell is a possible board. 6 Rows (Women-Pairs) × 15 Columns (Men-Pairs)."
            }))
            
            # Use helper to generate HTML (avoids indentation issues)
            # Function internally handles dedent
            matrix_html = get_committee_matrix_html(rows=6, cols=15)
            st.markdown(matrix_html, unsafe_allow_html=True)
