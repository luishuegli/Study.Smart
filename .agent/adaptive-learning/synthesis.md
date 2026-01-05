# Adaptive Learning: Synthesis

> **Purpose:** Track patterns across topics and pending rules to integrate.
> **Updated:** 2026-01-05

---

## Pending Rules (Not Yet Integrated)

_Rules that have been identified but not yet added to rule files._

### From Topic 1 (NEW)
| Rule | Evidence | Add to File | Status |
|------|----------|-------------|--------|
| **Intuition OUTSIDE container** | Fix #1: intuition was buried inside bordered containers | layout.md, all layout utilities | ⏳ CRITICAL |
| **Max 2 columns for formulas** | Fix #3: 4-column grid caused LaTeX cutoff | layout.md | ⏳ Pending |
| **No backslash in f-strings** | Fix #5: Python 3.12+ compatibility | implement.md (DO NOT section) | ✅ Integrated |

### From Topic 2 (NEW)
| Rule | Evidence | Add to File | Status |
|------|----------|-------------|--------|
| **No inline trap sections** | Fix #1: Use render_exam_essentials(), not custom HTML | pedagogy.md | ⏳ Pending |

### From Topic 5
| Rule | Evidence | Add to File | Status |
|------|----------|-------------|--------|
| **Layout-First Approval Gate** | User feedback: must show layout before implementing | implement.md (workflow) | ⏳ CRITICAL |
| No special Unicode quotes | German `„"` caused SyntaxError | design-system.md | ⏳ Pending |
| **Semantic Colors in Missions** | Fix #45: Red=risk, Green=safe, Blue=neutral | interactive.md | ✅ DOCUMENTED |
| **Never Nest Containers in Columns** | Fix #45: Causes formula cutoff | layout.md | ✅ DOCUMENTED |
| **Mission Statement First** | Fix #45: Goal BEFORE interaction | interactive.md | ✅ DOCUMENTED |
| **Discovery Debrief** | Fix #45: Explain what student learned at completion | interactive.md | ✅ DOCUMENTED |

### From Topic 3 (NEW)
| Rule | Evidence | Add to File | Status |
|------|----------|-------------|--------|
| **Decoder-in-Card (uses `---` separators)** | Fix #7, #10: Gold standard is Topic 1.6. Variable Decoder is INSIDE the card container, separated by `---` lines, NOT nested divs | pedagogy.md, layout.md | ⏳ CRITICAL |
| **Summary pages = same structure** | Fix #7: Summary pages (3.7) follow same Intuition→Theory→AskYourself→Interactive→ExamEssentials→MCQ order | pedagogy.md | ⏳ Pending |
| **@st.fragment on ALL interactives** | Fix #8, #9: Every interactive function needs `@st.fragment` decorator | layout.md | ⏳ CRITICAL |
| **Green reserved for success only** | Fix #9: Don't use `#34C759` for reference/target visuals, use Gray `#6B7280` | design-system.md | ⏳ Pending |

### From Topic 7 (NEW - Slider State Bug)
| Rule | Evidence | Add to File | Status |
|------|----------|-------------|--------|
| **SLIDER KEY-ONLY PATTERN** | Fix #1 Topic 7.3: Using BOTH `value=st.session_state.X` AND `key=Y` AND manual sync causes jump-back bug | interactive.md, templates.md | ⏳ **CRITICAL** |

### From Topic 7.5 (NEW - Scatter Plot)
| Rule | Evidence | Add to File | Status |
|------|----------|-------------|--------|
| **Visual comparisons required** | Fix #20: render_comparison() text-only boxes insufficient | layout.md | ⏳ **CRITICAL** |
| **No HTML in worked_example answers** | Fix #21: `<br>`, `<strong>` render as raw text | templates.md | ⏳ **CRITICAL** |
| **No redundant translations** | Fix #22: English should not show "(Streudiagramm)" | design-system.md | ⏳ Pending |
| **Definition + visual pattern** | Fix #23: Use 2-column layout with example plot | layout.md | ⏳ Pending |

**🚨 SLIDER STATE BUG - ROOT CAUSE & FIX:**

When a Streamlit slider has a `key=`, it automatically syncs to `st.session_state[key]`. Creating a SEPARATE state variable causes circular dependency:

```python
# ❌ WRONG PATTERN (causes slider jump-back every 2nd move)
if "slider_value" not in st.session_state:
    st.session_state.slider_value = 50

val = st.slider("Label", value=st.session_state.slider_value, key="slider_key")
st.session_state.slider_value = val  # ← CAUSES BUG!

# ✅ CORRECT PATTERN (use key auto-sync only)
val = st.slider("Label", min_value=0, max_value=100, value=50, key="slider_key")
# Streamlit auto-syncs to st.session_state["slider_key"] - no manual work needed!
```

### From Topic 7.3 (NEW - Additional Rules)
| Rule | Evidence | Add to File | Status |
|------|----------|-------------|--------|
| **PROBLEM-TYPE QUESTION HANDLING** | Fix #12: Non-MCQ questions showed "No options to select" | quiz_helper.py, topic templates | ⏳ CRITICAL |
| **EXAM QUESTION TABLES** | Fix #11: Multi-part exam questions must use markdown tables, not ASCII art | exam_questions.py | ⏳ Pending |

**Problem-Type Questions:**
```python
# Check question type before rendering
if q.get("type") == "problem" or not q.get("options"):
    st.markdown(t(q["question"]), unsafe_allow_html=True)
    if st.button("Show Solution"):
        st.markdown(t(q["solution"]))
else:
    render_mcq(...)  # Only for actual MCQs
```

### From Topic 4
| Rule | Evidence | Add to File | Status |
|------|----------|-------------|--------|
| Grey callouts only | Fixes #2, #5, #7 | design-system.md | ⏳ Pending |
| Headers outside containers | Fixes #1, #3 | layout.md | ✅ Integrated |

### From Topic 5.4 (NEW)
| Rule | Evidence | Add to File | Status |
|------|----------|-------------|--------|
| **Connection Coloring (Trace Values)** | User feedback: Colors should show where SAME value appears again, not categorize by type. Each distinct value gets its own color throughout. | design-system.md | ⏳ CRITICAL |
| **No emojis in decision trees** | Emoji ⭐ in decision tree violates No Emojis rule | decision_tree.py | ✅ Fixed |
| **Color the question too** | Given values in problem statement should use same colors as in solution steps | worked_example.py | ⏳ Pending |

### From Topic 8 (NEW - 2026-01-05)
| Rule | Evidence | Add to File | Status |
|------|----------|-------------|--------|
| **INTUITION_WHITE_CONTAINER** | User feedback: Intuition sections should use `st.container(border=True)`, NOT grey callouts | pedagogy.md, layout.md | ⏳ CRITICAL |
| **INTERACTIVE_EMPTY_CHART** | Fix #4: Show empty chart from start, add data lines as interaction happens | interactive.md | ⏳ Pending |
| **INTERACTIVE_SHOW_CALCULATION** | Fix #5: Show actual X₁, X₂ values and calculation breakdown, not just results | interactive.md | ⏳ CRITICAL |
| **RELATABLE_SCENARIOS** | Fix #6: Use everyday examples (pizza delivery, friends guessing) instead of abstract μ = 50 | pedagogy.md | ⏳ Pending |
| **EXPLAIN_THE_WHY** | Fix #7: Success messages should explain WHY the pattern works, not just state "A wins 55%" | interactive.md | ⏳ CRITICAL |
| **NO_LATEX_IN_HTML** | Confirmed again: `$...$` in HTML divs does not render. Use `st.latex()` | layout.md | ✅ DOCUMENTED (Topic 6) |
| **VERTICAL_CENTER_EQUAL_PADDING** | Fix #8: When centering content vertically in side-by-side columns, use EQUAL padding on top and bottom | layout.md | ⏳ Pending |
| **DYNAMIC_CHART_AXES** | Fix #9: Don't hardcode chart axis ranges - use `max(min_range, data_length + buffer)` to expand with data | interactive.md | ⏳ Pending |

**Vertical Centering in Side-by-Side Columns:**

When you have two columns where one has content (text, tables) and the other has a centered element (symbol, icon, chart):

```python
# ❌ WRONG - Unequal padding causes misalignment
<div style="padding: 100px 0 40px 0;">  # More top than bottom = too low
<div style="padding: 40px 0 100px 0;">  # More bottom than top = too high

# ✅ CORRECT - Equal padding for perfect vertical center
<div style="display: flex; flex-direction: column; justify-content: center; 
            align-items: center; padding: 70px 0;">
    <span style="font-size: 5em;">θ̂</span>
    <em>theta-hat</em>
</div>
```

**Key insight:** The padding value should be roughly half the height difference between your content and the adjacent column's content.

**Intuition Container Pattern:**
```python
# ❌ WRONG - Grey callout
st.markdown(f"""
<div style="background: #f4f4f5; border-left: 4px solid #a1a1aa; ...">
{content}
</div>
""", unsafe_allow_html=True)

# ✅ CORRECT - White container with border
st.markdown("### Intuition")
with st.container(border=True):
    st.markdown(t(content), unsafe_allow_html=True)
```

**Interactive Calculation Breakdown Pattern:**
```python
# Track last round details
st.session_state.sd_last = {"x1": x1, "x2": x2, "a": est_a, "b": est_b, ...}

# Show the story
with st.container(border=True):
    st.markdown(f"Friend 1 says **{lr['x1']:.1f}** min, Friend 2 says **{lr['x2']:.1f}** min")
    st.latex(fr"\frac{{{lr['x1']:.1f} + {lr['x2']:.1f}}}{{2}} = {lr['a']:.1f}")
    st.caption(f"Error: |{lr['a']:.1f} - 50| = **{lr['err_a']:.1f}**")
```

**Connection Coloring Specification:**

> **Purpose:** Colors trace the SAME value across steps, showing where numbers come from.

**How it works:**
1. Assign each DISTINCT given value its own color
2. When that value appears in later steps, use the SAME color
3. Intermediate results get new colors
4. Final answer is always GREEN

**Example (Portfolio Variance):**
```
PROBLEM: σ²_X = 100, σ²_Y = 64, ρ = 0.5. Find Var(X+Y)?

GIVEN:
  σ²_X = {blue}100      σ²_Y = {red}64       ρ = {purple}0.5

CALCULATE COV:
  Cov = {purple}0.5 · √{blue}100 · √{red}64 = {purple}0.5 · 10 · 8 = {gray}40

APPLY FORMULA:
  Var(X+Y) = {blue}100 + {red}64 + 2·{gray}40 = {green}244
```

**Color Palette:**
| Role | Color | Hex | Notes |
|------|-------|-----|-------|
| Value A | Blue | #007AFF | First given value |
| Value B | Red | #FF4B4B | Second given value |
| Value C | Purple | #9B59B6 | Third given value |
| Intermediate | Gray | #6B7280 | Computed values (reused later) |
| Final Answer | Green | #16a34a | Always green |

**Anti-pattern:** DON'T use same color for different values just because they're "inputs".

### From Topic 6 (UPDATED 2026-01-04)
| Rule | Evidence | Add to File | Status |
|------|----------|-------------|--------|
| **Bilingual Formula Dicts** | Fix #2: German words in LaTeX formulas | design-system.md | ⏳ CRITICAL |
| **Slider State Pattern** | Fix #3: value+key+sync causes ping-pong | troubleshooting.md | ⏳ CRITICAL |
| **Inline Symbol Decoder** | Fix #5, #8: Consolidate symbol explanations into CLT expander | pedagogy.md | ⏳ Pending |
| **No LaTeX in HTML divs** | Fix #1: st.markdown doesn't render LaTeX inside HTML | layout.md | ⏳ CRITICAL |
| **HTML Cannot Wrap st Elements** | T6.2 Fix #1: Opening `<div>` and closing `</div>` in separate st.markdown() don't wrap elements between | layout.md | ⏳ CRITICAL |
| **Slider CSS Requires Visible Labels** | T6.2 Fix #4-5: `label_visibility="collapsed"` breaks CSS targeting via `[aria-label*="..."]` | interactive.md | ⏳ Pending |
| **Slider Semantic Coloring (1.5 Pattern)** | T6.2 Fix #4: Use `.stSlider:has([aria-label*="X"])` CSS selector pattern | interactive.md | ⏳ Pending |
| **Formula Values Stay Black** | T6.2 Fix #6: Semantic coloring = slider-to-label, not slider-to-formula | design-system.md | ⏳ Pending |
| **Bilingual trap_formula** | T6.2 Fix #3: trap_formula with text like "FALSCH!" must be bilingual dict | pedagogy.md | ⏳ Pending |
| **Multi-line LaTeX Aligned** | T6.2 Fix #7: Use `\\begin{aligned}` for long formulas in narrow columns | layout.md | ⏳ Pending |
| **why_formula for Tips** | T6.2 Fix #9: Tips with math need `why_formula` field for proper LaTeX rendering | pedagogy.md | ⏳ Pending |

**Bilingual Formula Pattern:**
```python
# WRONG
"formula": r"\text{Summe: } E = n\mu"

# CORRECT
"formula": {"de": r"\text{Summe: } E = n\mu", "en": r"\text{Sum: } E = n\mu"}
```

**Slider State Pattern:**
```python
# WRONG - causes ping-pong revert
n = st.slider("n", value=st.session_state.n, key="slider")
st.session_state.n = n

# CORRECT - let Streamlit manage
n = st.slider("n", value=5, key="slider")  # value=initial only
```

---

## Cross-Topic Patterns

_Same issue appearing across multiple topics = CRITICAL rule._

| Pattern | Topics | Severity | Rule? |
|---------|--------|----------|-------|
| Intuition inside containers | T1, T2 | CRITICAL | ⏳ NEW - Layout utilities updated |
| Colored callouts inside containers | T3, T4 | HIGH | ✅ Added |
| Equal height CSS missing | T1, T2, T3 | CRITICAL | ✅ Added |
| Inline custom HTML for traps | T2 | MEDIUM | ⏳ NEW - Use utilities |
| Formula columns too narrow | T1, T5.3 | MEDIUM | ⏳ NEW - Max 2 columns |
| **Decoder separated from formula** | T3 | HIGH | ⏳ NEW - Use `---` separators |
| **Missing @st.fragment** | T3 (3.5, 3.6) | HIGH | ⏳ NEW - Decorator mandatory |
| **Nested containers in columns** | T5.3 | HIGH | ⏳ NEW - Use HTML flexbox instead |
| **German in LaTeX formulas** | T5.5, T6.1, T6.2 | HIGH | ✅ Fixed - Use bilingual dicts |
| **Slider value/key conflict** | T6.1 | HIGH | ✅ Fixed - Use key only |
| **Emojis in feedback widgets** | T6.1 | HIGH | ✅ Fixed - Absolute No Emojis v2 |
| **Semantic color without legend** | T6.1 | HIGH | ✅ Fixed - Add visible legend |
| **LaTeX in raw HTML** | T6.1, T7.6 | HIGH | ✅ Fixed - Use Unicode or st.latex() |
| **HTML divs spanning st elements** | T6.2 | HIGH | ✅ Fixed - Use st.container + CSS |
| **Slider CSS with hidden labels** | T6.2 | HIGH | ✅ Fixed - Use visible labels |
| **Formula values colored** | T6.2 | MEDIUM | ✅ Fixed - Values stay black |
| **Double border on interactives** | T7.2, T7.6 | HIGH | ✅ Fixed - Remove outer st.container() |

---

## Historical Log

### Topic 1 Synthesis
- **Completed:** 2026-01-03
- **Total fixes:** 5
- **New rules created:** 3 (intuition-outside, max-2-cols, no-backslash)
- **Key learnings:** Intuition is the "hook" - it must stand alone visually, not be buried inside details. Layout utilities updated to enforce this.

### Topic 2 Synthesis
- **Completed:** 2026-01-03 (in progress)
- **Total fixes:** 2
- **New rules created:** 1 (no inline traps)
- **Key learnings:** Old inline HTML sections must be replaced with standardized utilities. The "Question Dissector" pattern could be a future utility.

### Topic 3 Synthesis
- **Completed:** 2026-01-03 ✅
- **Total fixes:** 10
- **New rules created:** 4 (decoder-in-card, summary-structure, fragment-mandatory, green-reserved)
- **Key learnings:**
  1. **Formula Card Structure:** Title → Intuition (italic) → Formula → `---` → Variables (bullets) → `---` → Insight (italic). All within ONE container, NO nested divs/callouts.
  2. **Summary pages = regular structure:** Even summary pages (3.7) follow Intuition→Theory→AskYourself→Interactive→ExamEssentials→MCQ order.
  3. **@st.fragment mandatory:** Every interactive function MUST have `@st.fragment` decorator for smooth UX.
  4. **Green reserved:** `#34C759` only for success feedback, not for reference visuals.

### Topic 4 Synthesis
- **Completed:** 2026-01-02 ✅
- **Total fixes:** 8
- **New rules created:** 2 (grey-callouts-only, header-out-protocol)
- **Key learnings:** Consistent styling with grey callouts only. Headers must be outside containers.

### Topic 5 Synthesis
- **Completed:** 2026-01-03 ✅
- **Total fixes:** 12
- **New rules created:** 3 (connection-coloring, scenario-first, discovery-debrief)
- **Key learnings:** Connection Coloring traces values across steps. Nested containers in columns cause formula cutoff.

### Topic 6 Synthesis
- **Completed:** 2026-01-04 ✅ (6.2 added)
- **Total fixes:** 15 (6.1) + 12 (6.2) = 27
- **New rules created:** 11 (bilingual-formulas, slider-state, inline-decoder, no-latex-in-html, semantic-legend, emojis-in-widgets, html-subscript, slider-css-pattern, html-wrap-impossible, aligned-latex, why-formula-tips)
- **Key learnings:**
  1. **Bilingual Formulas:** Any LaTeX with text words MUST be a `{"de": ..., "en": ...}` dict
  2. **Slider State:** Never use `value=session_state.x` + `key="x"` + manual sync - causes ping-pong
  3. **Inline Symbol Decoder:** Use simple inline format for symbol/variable explanations
  4. **No LaTeX in HTML:** Use separate `st.latex()` calls, not inline in HTML divs
  5. **Semantic Color Legend:** If color changes have meaning, MUST add visible legend
  6. **HTML Subscript:** In raw HTML contexts (like render_ask_yourself), use `X<sub>i</sub>` not `$X_i$`
  7. **T6.2: HTML divs can't wrap st elements** - Use st.container + CSS override instead
  8. **T6.2: Slider CSS needs visible labels** - `[aria-label*="..."]` only works with visible labels
  9. **T6.2: Semantic coloring = slider-to-label** - Formula values stay BLACK

---

## Rule Evolution Tracker

_Track how rules improve over time._

| Rule | Version | Origin | Refinements |
|------|---------|--------|-------------|
| Intuition-outside | v1 | Topic 1, Fix #1 | Added to all layout utilities |
| Grey callouts | v1 | Topic 4, Fix #2 | - |
| Header-out protocol | v2 | Topic 2, refined in T4 | Added edge cases |
| Max formula columns | v1 | Topic 1, Fix #3 | - |
| **Decoder-in-Card** | v1 | Topic 3, Fix #7 | Uses `---` separators, matches Topic 1.6 |
| **Fragment-mandatory** | v1 | Topic 3, Fix #8 | All interactives need `@st.fragment` |

---

## Metrics

| Metric | T1 | T2 | T3 | T4 | T5 | Trend |
|--------|----|----|----|----|----|-------|
| Fixes needed | 5 | 2 | 10 | - | 45 | ↑ (complex topic) |
| Implementation time | - | - | - | - | - | ↓ |
| Rules added | 3 | 1 | 4 | - | 4 | ↑ |

---

## Topic 5.3 Synthesis
- **Completed:** 2026-01-03
- **Total fixes:** 1 (session) + 44 prior = 45
- **New rules created:** 4 (semantic-colors, no-nested-containers, mission-first, discovery-debrief)
- **Key learnings:**
  1. **Semantic Colors in Missions:** Red = danger/high risk, Green = safe/low risk, Blue = neutral. Colors must reinforce meaning.
  2. **Never nest st.container() inside st.columns():** Causes formula cutoff. Use HTML flexbox instead.
  3. **Mission Statement First:** Goal appears BEFORE the interactive, not at the bottom.
  4. **Discovery Debrief:** After mission completion, explain what the student learned and relate back to the formula.

## Topic 5.4 Synthesis
- **Completed:** 2026-01-03
- **Total fixes:** 6
- **New rules created:** 3 (connection-coloring, color-question-too, ≥3-utilities-mandate)
- **Key learnings:**
  1. **Connection Coloring (CRITICAL):** Colors trace SAME value across steps - each distinct value gets its own persistent color. Anti-pattern: Don't color different values the same just because they're "inputs".
  2. **Color the Question Too:** Given values in problem statement should use same colors as in solution steps for full traceability.
  3. **≥3 Utilities Mandate:** Every subtopic must use at least 3 different layout utilities (excluding ask_yourself and exam_essentials). Updated `implement.md` workflow.
  4. **No Emojis in Utilities:** Removed ⭐ from decision_tree.py, replaced with ✓.
  
**Files modified:**
- `topic_5_4_content.py` — Full implementation with Connection Coloring
- `decision_tree.py` — Emoji removal
- `implement.md` — Added utility selection checklist
- `exam_questions.py` — Fixed English translations for hs2015_mc6

## Topic 5.5 Synthesis
- **Completed:** 2026-01-03
- **Total fixes:** 6
- **New rules created:** 3 (absolute-no-emojis, no-help-tooltips, examples-use-arrow)
- **Key learnings:**
  1. **Absolute No Emojis (STRICT):** Emojis like 📌 and 💡 are NOT allowed, even in captions. The only exception remains `st.button()` labels. Use plain text or `→` arrow for examples.
  2. **No Help Tooltips:** Do NOT use `help=` parameter in `st.markdown()`. It creates question mark icons that clutter the UI. Show the information directly instead via `st.caption()`.
  3. **Examples with Arrow:** When showing "when" and "example" for formulas, use plain caption for "when" and prefix examples with `→` (arrow) instead of emojis.
  
**Rule Integration:**

### From Topic 5.5 (NEW)
| Rule | Evidence | Add to File | Status |
|------|----------|-------------|--------|
| **Absolute No Emojis** | Fixed 📌💡 in captions | design-system.md | ⏳ CRITICAL |
| **No Help Tooltips** | Fixed help= in st.markdown | design-system.md | ⏳ Pending |
| **Examples with Arrow** | Use → prefix | design-system.md | ⏳ Pending |
| **LaTeX Must Be Language-Agnostic** | German text appeared in English mode | design-system.md | ⏳ CRITICAL |

**Files modified:**
- `topic_5_5_content.py` — Learn-Test-Learn summary with ULTRATHINK, fixed emojis/tooltips/LaTeX
- `exam_essentials.py` — Added `tip_formula` and `why_formula` support

---

## Design System Rule Clarification

### No Emoji Rule — Expanded (JAN 2026)

**Before (v1):**
> No emojis. Exception: Emojis OK in st.button() labels only.

**After (v2 — STRICT):**
> **NO EMOJIS ANYWHERE** except st.button() labels.
> 
> Specifically prohibited:
> - 📌 💡 ⭐ ❓ or ANY emoji in `st.caption()`
> - Emojis in grey callout HTML
> - Emojis in st.info/warning/error (already banned)
> - `help=` parameter in st.markdown (creates ? icon)
> 
> **Allowed alternatives:**
> - Plain text labels
> - `→` arrow for examples/flow
> - `•` bullets for lists
> - `ℹ️` ONLY in st.button() label

### LaTeX Language-Agnostic Rule (JAN 2026)

> **LaTeX formulas must NEVER contain language-specific text.**
> 
> **Problem:** Using `\text{Zeile}` in LaTeX shows German even when app is in English mode.
> 
> **Solution:** Keep formulas purely mathematical. Move any explanatory text to bilingual `why` fields:
> 
> ```python
> # WRONG - German appears in English mode
> "why_formula": r"f_X \text{ (Zeile)}, \quad f_Y \text{ (Spalte)}"
> 
> # CORRECT - Bilingual text in why field
> "why": {"de": "f_X → Zeile, f_Y → Spalte", "en": "f_X → row, f_Y → column"}
> ```
> 
> **Exception:** Universal math terms like `\text{Cov}`, `\text{Var}` are OK.


---

## Topic 7 Synthesis
- **Completed:** 2026-01-05 ✅
- **Total fixes:** 26 (across 7.1-7.6)
- **New rules created:** 8 (exam-essentials-latex, chf-only, slider-semantic-color, mission-compaction, feedback-sign-format, no-double-border, no-latex-in-html, unicode-for-callouts)
- **Key learnings:**
  1. **Exam Essentials LaTeX (STRICT):** ALL math in tips/traps MUST use LaTeX ($...$), including variables ($n$), formulas ($K = \alpha n + 1$), and subscripts ($x_{(K-1)}$). NEVER use plain text like "n-1" or "x(K)".
  2. **CHF Currency Only:** This is a Swiss project - always use CHF, never €.
  3. **Slider Semantic Coloring:** Use CSS `.stSlider:has([aria-label*="X"])` pattern to color-code sliders matching semantic meaning (e.g., red #FF4B4B for outliers).
  4. **Mission Compaction:** For missions to fit on screen: chart height ≤220px, padding 8px, remove `<br>` spacers, legend below chart (y=-0.3).
  5. **Feedback Sign Format:** Use Python's `:+,.0f` format for values that can be positive/negative, NOT hardcoded `+` prefix (causes `+-14`).
  6. **No Double Border (CRITICAL):** Interactive elements (radios, sliders, pills) should NOT have outer `st.container(border=True)`. Remove the container wrapper entirely.
  7. **No LaTeX in HTML Grey Callouts:** Streamlit doesn't render LaTeX inside `st.markdown(..., unsafe_allow_html=True)`. Use Unicode subscripts (Q₁, x₍ₖ₎) or separate `st.latex()` calls.
  8. **Multipart Question Formatting:** Use markdown tables, `---` dividers, bold headers for multi-stage exam questions.

### From Topic 7 (NEW - 2026-01-04)
| Rule | Evidence | Add to File | Status |
|------|----------|-------------|--------|
| **Exam Essentials LaTeX** | "K = αn + 1" rendered as plain text | pedagogy.md | ⏳ CRITICAL |
| **CHF Only** | € appeared in worked example | design-system.md | ⏳ Pending |
| **Slider Semantic Color** | CEO slider should be red (outlier) | interactive.md | ⏳ Pending |
| **Plotly Legend Below Chart** | Legend overlapped with chart title | interactive.md | ⏳ Pending |
| **Feedback Sign Format** | Use `:+,.0f` not `+{value}` | design-system.md | ⏳ Pending |
| **KaTeX Overflow Fix** | Formulas clipped at top globally | styles.py | ✅ Integrated |

### From Topic 7.4 (NEW - 2026-01-04)
| Rule | Evidence | Add to File | Status |
|------|----------|-------------|--------|
| **LaTeX + latex_en pair** | "Für k=1" showed in English mode | design-system.md | ⏳ CRITICAL |
| **Interactive Finite Limit** | Pattern Detective had infinite rounds | interactive.md | ⏳ Pending |
| **Black Pill CSS Pattern** | st.pills renders grey, not black | templates.md | ⏳ Pending |
| **Compact Chart Height (200px)** | Comparison didn't fit on screen | layout.md | ⏳ Pending |
| **No Checkmarks in Options** | "Normal ✓" violates no-emoji rule | design-system.md | ✅ Fixed |

### From Topic 7.6 (NEW - 2026-01-05)
| Rule | Evidence | Add to File | Status |
|------|----------|-------------|--------|
| **No Double Border on Interactives** | Tool wizard had outer border + radio borders | layout.md | ⏳ CRITICAL |
| **No LaTeX in HTML Grey Callouts** | `$Q_1 - 1.5 \cdot \text{IQR}$` showed as raw text | layout.md | ⏳ CRITICAL |
| **Unicode Subscripts for Callouts** | Use Q₁ Q₃ x₍ₖ₎ instead of $Q_1$ etc. | design-system.md | ⏳ Pending |

---

## Proposed Rule Integrations (Topic 7 Complete)

### 1. design-system.md — Add LaTeX Bilingual Section

```markdown
[STRICT] Bilingual LaTeX Formulas
Any LaTeX with text words (e.g., `\text{For}`, `\text{Point}`) MUST use bilingual support:

Option A: Separate keys in data dicts
```python
{
    "latex": r"\text{Für } k=1...",     # German default
    "latex_en": r"\text{For } k=1...",  # English override
}
```

Option B: Pure math (no text) — preferred when possible
```python
"latex": r"k=1: \quad F^{-1}(\ldots)"  # No language-specific text
```

Universal terms like `\text{Cov}`, `\text{Var}` are OK in any language.
```

### 2. interactive.md — Add Quiz Limit Pattern

```markdown
[STRICT] Quiz-Style Interactive Limits
All quiz/detective/pattern-matching games MUST have:
- Finite limit: `MAX_ROUNDS = 15` (or 10 for simpler games)
- Completion state: Show final score and restart option
- Progress indicator: `Score: X/Y`

Pattern:
```python
MAX_ROUNDS = 15
if st.session_state.round >= MAX_ROUNDS:
    st.success(f"Complete! Score: {score}/{MAX_ROUNDS}")
    if st.button("Play again"):
        st.session_state.round = 0; st.rerun(scope="fragment")
    return
```
```

### 3. templates.md — Add Black Pill Button Pattern

```markdown
[PATTERN] Black Pill Button Group
For site-consistent pill selection (black when selected):

```python
btn_cols = st.columns(len(options))
for col, opt, key in zip(btn_cols, options, keys):
    with col:
        if st.session_state.selection == key:
            st.markdown(f'''<div style="background:#000;color:#fff;
                padding:8px 16px;border-radius:20px;text-align:center;
                font-weight:500;font-size:0.9em;">{opt}</div>''', 
                unsafe_allow_html=True)
        else:
            if st.button(opt, key=f"pill_{key}", use_container_width=True):
                st.session_state.selection = key
                st.rerun(scope="fragment")
```
```

### 4. layout.md — Add Compact Comparison Pattern

```markdown
[PATTERN] Compact Visual Comparison
For side-by-side chart comparisons on a single screen:
- Chart height: max 200px
- Column ratio: Give more space to controls ([1, 1.5] not [1.5, 1])
- No interpretation boxes — use subtitle text
- Key insight: Single-line caption
```

### 5. layout.md — Add No Double Border Rule

```markdown
[STRICT] No Double Border on Interactive Elements
Interactive elements (radios, sliders, pill buttons) should NOT have outer `st.container(border=True)`.

The inner elements already provide visual separation. Adding an outer border:
- Creates ugly double-border effect
- Wastes screen space
- Reduces content area

Pattern:
```python
# ❌ WRONG - creates double border
with st.container(border=True):
    st.radio(...)

# ✅ CORRECT - no wrapper OR use st.container() without border
st.radio(...)
# OR
with st.container():  # No border parameter
    st.radio(...)
```
```

### 6. design-system.md — Add Unicode for Grey Callouts

```markdown
[STRICT] Unicode Math in Grey Callouts
LaTeX does NOT render inside HTML grey callouts (`st.markdown(..., unsafe_allow_html=True)`).

Use Unicode subscripts/superscripts instead:
- Subscripts: ₀₁₂₃₄₅₆₇₈₉ₐₑₓₙₖ₍₎
- Superscripts: ⁰¹²³⁴⁵⁶⁷⁸⁹
- Math: × · − ± √ ∞ ≈ ≠ ≤ ≥ → ∑ ∏
- Floor/ceiling: ⌊ ⌋ ⌈ ⌉

Examples:
- Q₁ − 1.5·IQR (not $Q_1 - 1.5 \cdot \text{IQR}$)
- x₍ₖ₎ (not $x_{(k)}$)
- σ² (not $\sigma^2$)
```

