# Topic 7: Descriptive Statistics - Adaptive Learning Log

## Fixes Applied in This Session

### 1. LaTeX Formula Clipping (GLOBAL FIX)
**Issue:** LaTeX formulas (especially fractions) were being cut off at the top across the entire site.
**Root Cause:** Streamlit's parent containers have `overflow: hidden` which clips KaTeX elements.
**Fix:** Added CSS to `views/styles.py`:
```css
.katex, .katex-display, .katex-display > .katex {
    overflow: visible !important;
}
.katex-display {
    padding-top: 4px !important;
    padding-bottom: 2px !important;
}
```
**Rule to Extract:** [ALREADY IN STYLES.PY - GLOBAL]

---

### 2. Mission Element Compaction
**Issue:** Interactive mission element too large, didn't fit on one screen.
**Fixes Applied:**
- Reduced chart height from 400 → 200px
- Removed redundant `<br>` spacers
- Compacted scenario callout padding (12px → 8px)
- Compacted feedback boxes (padding 16px → 8px, font 1.8em → 1.3em)
- Removed color legend (redundant)
- Moved Plotly legend below chart (y=-0.3)

---

### 3. Double Border Removal
**Issue:** Interactive elements wrapped in redundant `st.container(border=True)`.
**Fix:** Removed outer border when inner element already has visual separation.
**Rule:** Mission elements should NOT have outer bordered container.

---

### 4. Slider Color Coding
**Issue:** CEO salary slider not color-coded like other sliders in Topic 1.5.
**Fix:** Added red (#FF4B4B) slider CSS using aria-label selector:
```css
.stSlider:has([aria-label*="CEO"]) div[data-baseweb="slider"] > div:first-child > div:first-child { 
    background-color: #FF4B4B !important; 
}
```
**Rule:** Semantic slider coloring should match the variable's color in formulas.

---

### 5. Sign Formatting in Feedback
**Issue:** Hardcoded `+` prefix caused `+-14 CHF` for negative shifts.
**Fix:** Changed from `+{value:,.0f}` to `{value:+,.0f}` (Python's sign format specifier).
**Rule:** Use `:+,` format for values that can be positive or negative.

---

### 6. Currency: CHF, Not Euros
**Issue:** Worked example used € instead of CHF.
**Fix:** Replace all € with CHF in content.
**Rule:** [STRICT] This is a Swiss project - always use CHF, never €.

---

### 7. HTML Tags Rendering as Text
**Issue:** `<strong>` tags showing instead of bolding.
**Causes:** 
a) Using st.markdown() without `unsafe_allow_html=True`  
b) Mixing HTML with markdown (better to use **bold**)
**Fix:** Added `unsafe_allow_html=True` or converted to markdown `**bold**`.

---

### 8. Exam Essentials Math Without LaTeX
**Issue:** Tips like "K = αn + 1" and "x(K-1)" rendered as plain text.
**Fix:** Convert to proper LaTeX: `$K = \\alpha n + 1$`, `$x_{(K-1)}$`
**RULE TO ADD TO PEDAGOGY.MD:**
```
[STRICT] ALL math in Exam Essentials MUST use LaTeX ($...$)
This includes:
- Variables: $n$, $K$, $\alpha$
- Formulas: $K = \alpha n + 1$
- Subscripts: $x_{(K-1)}$, $x_{(K)}$
- NEVER use plain text like "n-1" or "x(K)" - always LaTeX!
```

---

## Pending Rules to Add to Main Files

1. **pedagogy.md:** Add explicit LaTeX requirement for Exam Essentials math
2. **design-system.md:** Add "CHF only, never €" rule
3. **interactive.md:** Add slider color coding pattern

## Summary
Topic 7.2 now has:
- Compact mission element that fits on screen
- Color-coded CEO salary slider (red = outlier)
- Proper sign formatting (+/-)  
- Legend below chart without overlap
- All math in LaTeX format
- CHF currency throughout

---

## Topic 7.3 (Boxplot) — Fixes Applied

### 9. Slider State Bug (CRITICAL)
**Issue:** Slider jumps back every second move.
**Root Cause:** Using BOTH `value=st.session_state.X` AND `key=Y` AND manual sync creates circular dependency.
**Fix:** Use `key=` only. Streamlit auto-syncs to `st.session_state[key]`.
```python
# ❌ WRONG
val = st.slider("Label", value=st.session_state.X, key="key")
st.session_state.X = val  # CAUSES BUG

# ✅ CORRECT
val = st.slider("Label", value=50, key="key")
# Auto-syncs to st.session_state["key"]
```
**Rule:** [CRITICAL] Add to templates.md

---

### 10. SVG Diagram for Anatomy
**Issue:** Anatomy section was plain text, not visual.
**Fix:** Added labeled SVG boxplot diagram with Q1, Q2, Q3, IQR bracket, outlier.
**Result:** Students see visual + explanations in one container.

---

### 11. Exam Question Formatting
**Issue:** hs2015_prob1 displayed as unreadable wall of text with ASCII art (●●●).
**Fix:** Rewrote with:
- Proper markdown tables for distributions and grades
- Clear Part 1A / Part 1B separation
- Numbered task lists
**Rule:** [STRICT] Multi-part exam questions MUST use markdown tables and `---` dividers.

---

### 12. Problem-Type Question Handling
**Issue:** "No options to select" shown for non-MCQ questions.
**Fix:** Check `type == "problem"` and render with Show Solution button instead of render_mcq.
```python
if q.get("type") == "problem" or not q.get("options"):
    st.markdown(t(q["question"]), unsafe_allow_html=True)
    if st.button("Show Solution"):
        st.markdown(t(q["solution"]))
```
**Rule:** Problem-type questions need different rendering than MCQs.

---

### 13. Spacing Adjustments
- SVG diagram: 160px → 200px height
- Anatomy parts: padding 8/12px → 10/14px
- Scenario: removed double `<br><br>`, now single `<br>`

---

## Topic 7.4 (QQ-Plot) — Fixes Applied

### 14. German Text in LaTeX Formulas (CRITICAL)
**Issue:** German words like "Für", "Punkt", "Ausreisser" appeared in LaTeX even when app was in English mode.
**Root Cause:** Using single `latex` field with German text instead of bilingual support.
**Fix:** Use `latex` (German default) + `latex_en` (English override) fields supported by `render_worked_example`:
```python
{
    "label": {"de": "Schritt 1", "en": "Step 1"},
    "latex": r"\text{Für } k=1: ...",  # German
    "latex_en": r"\text{For } k=1: ...",  # English
    "note": {"de": "...", "en": "..."}
}
```
**Rule:** [CRITICAL] LaTeX with text words MUST have `latex` + `latex_en` pair for bilingual support.

---

### 15. Checkmark Emoji in Options
**Issue:** "Normal Distribution ✓" had checkmark which violates No Emojis rule.
**Fix:** Removed checkmark from all pattern options.
**Rule:** No emojis in option labels.

---

### 16. Interactive Limit
**Issue:** Pattern Detective had infinite rounds, no completion state.
**Fix:** Added `MAX_PATTERNS = 15` limit with completion message and "Play again" button.
**Rule:** All quiz-style interactives should have a finite limit (typically 10-15) with restart option.

---

### 17. Compact Visual Comparison Layout
**Issue:** QQ-Plot vs Histogram comparison section was too tall, didn't fit on screen.
**Fixes Applied:**
- Column ratio [1.5, 1] → [1, 1.5] (more space for buttons)
- Chart height 280px → 200px
- Replaced interpretation boxes with subtitle text
- Moved key insight to single-line caption
- Used black pill buttons (custom HTML) for consistency

---

### 18. Black Pill Buttons
**Issue:** st.pills renders grey buttons, not black like elsewhere in app.
**Fix:** Custom implementation with session state + HTML for selected state:
```python
if is_selected:
    st.markdown(f'<div style="background:#000;color:#fff;...">{opt}</div>', unsafe_allow_html=True)
else:
    if st.button(opt, ...):
        st.session_state.selection = key
        st.rerun(scope="fragment")
```
**Rule:** For black pill buttons matching site style, use custom button group with HTML selected state.

---

## Pending Rules to Add (Topic 7.4)

| Rule | Evidence | Add to File | Status |
|------|----------|-------------|--------|
| **LaTeX + latex_en pair** | Fix #14: German in English mode | design-system.md | ⏳ CRITICAL |
| **Interactive limit (15)** | Fix #16: Infinite rounds | interactive.md | ⏳ Pending |
| **Black pill CSS pattern** | Fix #18: st.pills doesn't match site | templates.md | ⏳ Pending |
| **Compact comparison layout** | Fix #17: Charts max 200px height | layout.md | ⏳ Pending |

---

## Topic 7.5 Fixes (Scatter Plot)

### 19. render_comparison Parameter Name
**Issue:** Called `render_comparison(header=...)` but function expects `title=`.
**Fix:** Changed to `render_comparison(title=...)`.
**Rule:** Check function signatures before calling utilities.

---

### 20. Visual Comparisons Required
**Issue:** render_comparison() produces text-only boxes with just titles — not visually compelling.
**Fix:** Created `univariate_vs_bivariate_visual()` function with side-by-side plots (1D strip vs 2D scatter).
**Rule:** Comparison sections should include visual plots, not just text boxes. Text-only comparisons are insufficient.

---

### 21. HTML Not Allowed in render_worked_example Answer
**Issue:** `<br>` and `<strong>` tags showed as raw text in worked example answer.
**Root Cause:** `render_worked_example()` uses `st.markdown(f"**{t(answer)}**")` WITHOUT `unsafe_allow_html=True`.
**Fix:** Rewrote answer as plain text with em-dash separators instead of HTML.
**Rule:** Worked example answers must be plain text or markdown only — NO HTML tags.

---

### 22. Redundant Translations in Terms
**Issue:** English definition showed "Scatter Plot (Streudiagramm)" — unnecessary German.
**Fix:** English term is just "Scatter Plot".
**Rule:** Only include German translation in English if it's the etymological origin or a commonly-used term.

---

### 23. Definition Cards Need Visuals
**Issue:** Definition card was text-only, abstract without visual context.
**Fix:** Added two-column layout: definition text on left, example scatter plot on right.
**Rule:** Definition sections should include a small example visual when possible.

---

## Pending Rules to Add (Topic 7.5)

| Rule | Evidence | Add to File | Status |
|------|----------|-------------|--------|
| **Visual comparisons required** | Fix #20: Text boxes not enough | layout.md | ⏳ CRITICAL |
| **No HTML in worked_example answers** | Fix #21: HTML renders as text | templates.md | ⏳ CRITICAL |
| **No redundant translations** | Fix #22: Only origin words | design-system.md | ⏳ Pending |
| **Definition + visual pattern** | Fix #23: Side-by-side layout | layout.md | ⏳ Pending |
