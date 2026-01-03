---
trigger: always_on
---

description: Container patterns and CSS [STRICT]
Layout Rules
All layout rules are [STRICT]. No creativity allowed.

[STRICT] Container Layout Rule
Columns OUTSIDE, containers INSIDE:

# CORRECT
c1, c2 = st.columns([1, 1.6])
with c1:
    with st.container(border=True):
        st.markdown("Content")
with c2:
    with st.container(border=True):
        st.markdown("Content")
# WRONG - Breaks equal height
with st.container(border=True):
    c1, c2 = st.columns(2)
[STRICT] Header-Out Protocol
Headers (###) go OUTSIDE bordered containers:

# CORRECT
st.markdown("### Section Title")
with st.container(border=True):
    st.markdown("Content")
# WRONG
with st.container(border=True):
    st.markdown("### Section Title")
[STRICT] No Nested Borders
Never use st.info(), st.warning() inside containers:

# WRONG
with st.container(border=True):
    st.info("Note")
# CORRECT - Use grey div
with st.container(border=True):
    st.markdown(f"""
<div style="background: #f4f4f5; border-left: 4px solid #a1a1aa; 
            padding: 12px 16px; border-radius: 8px; color: #3f3f46;">
{content}
</div>
""", unsafe_allow_html=True)
[STRICT] Equal Height CSS
Inject ONCE per page with side-by-side containers:

st.markdown("""
<style>
[data-testid="stHorizontalBlock"] { align-items: stretch !important; }
[data-testid="column"], [data-testid="stColumn"] { 
    display: flex !important; 
    flex-direction: column !important; 
}
[data-testid="column"] > div, [data-testid="stColumn"] > div { 
    flex: 1 !important; 
    display: flex !important; 
    flex-direction: column !important; 
    height: 100% !important; 
}
div[data-testid="stVerticalBlock"], 
div[data-testid="stVerticalBlockBorderWrapper"] { 
    flex: 1 !important; 
    display: flex !important; 
    flex-direction: column !important; 
}
</style>
""", unsafe_allow_html=True)
Critical selectors:

stHorizontalBlock — Forces row to stretch
stVerticalBlock — For content blocks
stVerticalBlockBorderWrapper — For bordered containers
[STRICT] Spacing
Context	Code
Section break	st.markdown("<br><br>", unsafe_allow_html=True)
Element break	st.markdown("<br>", unsafe_allow_html=True)
Divider	st.markdown("---")
When to use:

<br><br> — Theory → Interactive, before Exam
<br> — Between cards in section
--- — After page header
[STRICT] Column Ratios
# Theory + Visualization
st.columns([1, 1.6], gap="medium")
# Content + Button
st.columns([3, 1])
# Equal split
st.columns([1, 1])
[STRICT] Fragment Isolation
ALL interactive components use @st.fragment:

@st.fragment
def component():
    if st.button("Click", key="btn"):
        st.session_state.value += 1
        st.rerun(scope="fragment")  # Only this fragment reruns
component()
[STRICT] Anti-Overlap Protocol
If content risks overlapping:

Switch to vertical layout
Reduce column count
Never put charts in columns narrower than 0.4
Rule: Better to scroll than to squint.

[STRICT] Plotly Geometry Lock
Prevent circles becoming ovals:

fig.update_layout(
    xaxis=dict(scaleanchor="y", scaleratio=1),
    yaxis=dict(scaleanchor="x", scaleratio=1),
)
[STRICT] CSS Scoping
Only scoped CSS allowed:

# ALLOWED - data-testid
[data-testid="stHorizontalBlock"] { ... }
# FORBIDDEN - generic tags
div { margin: 0; }
[STRICT] No Dead Clicks
Non-interactive charts:

fig.update_layout(clickmode='none', hovermode=False)

[STRICT] Max 2 Columns for Formulas
LaTeX formulas get cut off in narrow columns. NEVER use more than 2 columns for formula grids:

# WRONG - Formulas will be cut off/scrollable
c1, c2, c3 = st.columns(3)  # Too narrow!

# CORRECT - Adequate width for LaTeX
c1, c2 = st.columns(2, gap="medium")

[STRICT] Formula Card Structure (Gold Standard: Topic 1.6)
Formula cards use `---` separators, NOT nested containers:

```python
with st.container(border=True):
    # 1. Title (bold)
    st.markdown(f"**{t(title)}**")
    
    # 2. Intuition (italic, NO math)
    st.markdown(f"*{t(intuition)}*")
    
    # 3. Formula (prominent)
    st.latex(formula)
    
    # --- Variable Decoder ---
    st.markdown("---")
    st.markdown("**Variables:**")
    for v in variables:
        st.markdown(f"• ${v['symbol']}$ = **{name}** — {desc}")
    
    # --- Insight ---
    st.markdown("---")
    st.markdown(f"*{t(insight)}*")