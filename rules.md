# Project Rules (Study.Smart)

## 1. Bilingual Content Mandate
- **All** user-facing text must be bilingual dictionaries `{"de": "...", "en": "..."}`.
- **Critical**: This explicitly includes **MCQ Options**.
    - **Forbidden**: `options = ["Option A", "Option B"]`
    - **Required**: `options = [{"de": "Option A", "en": "Option A"}, ...]`
- Failure to use dictionary structure for options results in the UI failing to switch languages for answers.

## 2. Iconography & Visuals
- **No Emojis**: Use SVG icons or `render_icon`.
- **SVG Integrity**: Ensure `viewBox`, `width`, `height`, and `fill="currentColor"`.

## 3. Mathematical Typesetting
- Use LaTeX for all variables and formulas.
- Fractions within options must use LaTeX (e.g., `1/2` -> `\frac{1}{2}` or clean text `1/2`, but not integer artifacts like `21`).

## 4. Code Standards

### 4.1 No Global CSS
- Use scoped rendering only.

### 4.2 Equal Height Columns (AUTOMATIC)
Side-by-side bordered containers now automatically stretch to equal heights. The fix is global via `load_design_system()` in `styles.py` (Section 3c).

**You don't need to do anything special** — just use:
```python
c1, c2 = st.columns(2)
with c1:
    with st.container(border=True):
        # Short content
with c2:
    with st.container(border=True):
        # Longer content will make both boxes same height
```

**How it works:** The CSS targets `stLayoutWrapper` which by default has `flex-grow: 0` and breaks the height chain. Our fix forces it to grow.

**For formulas of different heights**, use the phantom:
```python
from views.styles import LATEX_PHANTOM
st.latex(formula + LATEX_PHANTOM)  # Reserves space for tall formulas
```

### 4.3 LaTeX in HTML Content
- LaTeX (`$...$`) does **NOT** render inside `st.markdown()` HTML strings
- For LaTeX in custom HTML divs: use `st.latex()` separately, or render the div first, then call `st.latex()`
- Never mix LaTeX with HTML in the same string

### 4.4 Header-Out Protocol (MANDATORY)
- **Section headings MUST be placed OUTSIDE bordered containers**, not inside them.
- The heading introduces the container; the container holds only the content.
- **Correct**:
  ```python
  st.markdown("### The Intuition")
  with st.container(border=True):
      st.markdown(t(content["intuition_text"]))
  ```
- **Forbidden**:
  ```python
  with st.container(border=True):
      st.markdown("### The Intuition")  # ❌ Heading inside!
      st.markdown(t(content["intuition_text"]))
  ```

### 4.5 Verification Checklist (RUN BEFORE COMMIT!)
Before considering any topic file complete, verify:
1. [ ] **Equal heights** - Side-by-side boxes stretch to same height
2. [ ] **Bold renders** - No raw `**text**` visible (use `<strong>` in HTML)
3. [ ] **LaTeX renders** - No raw `$formula$` visible
4. [ ] **Bilingual** - All text uses `t()` function, no mixed "oder/or"
5. [ ] **Syntax OK** - `python3 -m py_compile <file>` passes
6. [ ] **Visual check** - Run `streamlit run app.py` and visually inspect


## 5. Callout Styling (Updated)
- **Trap/Warning Callouts**: Use **Zinc/Grey** palette, not amber.
  - Background: `#f4f4f5` (Zinc-100)
  - Border: `#a1a1aa` (Zinc-400) 
  - Text: `#3f3f46` (Zinc-700)
  - Icon: `#71717a` (Zinc-500)
- **Success States**: Use native Streamlit `st.success()`.
- **Error States**: Use native Streamlit `st.error()`.

## 6. Content Quality & Pedagogy (CRITICAL)

**Goal**: Make learning feel **easy and almost fun**. The student should never need to look anything up or feel confused.

### 6.1 Every Formula Must Have:
- **Intuitive explanation** - What does this calculate? Why does it work?
- **Derivation or breakdown** - Show where it comes from (E[X] = sum of x*P(x))
- **Real-world example** - Concrete application from lectures
- **Parameter meanings** - Not just symbols, but what they represent

### 6.2 "Frag dich" Decision Guides:
- Use `<strong>` HTML tags, NOT `**markdown**` (renders inside HTML divs)
- Keep questions actionable and specific

### 6.3 Pro Tips - Contextual Placement:
- **Place Pro Tips INSIDE the relevant section**, not floating at the bottom
- If a tip relates to a formula, put it right after that formula
- If it helps with a common mistake, put it in the same container as the trap
- Only use a standalone Pro Tip section for general exam strategy

### 6.4 Content Depth Standard:
- **No shallow content** - Every section must add genuine value
- **Derivations > Memorization** - Show the "why" behind formulas
- **Lecture integration** - Use examples and language from the official course material
- **Completeness** - Student should not need to consult other sources

### 6.5 HTML in Content Strings:
- When text will render inside HTML `<div>`, use `<strong>` not `**bold**`
- Always add `unsafe_allow_html=True` to `st.markdown()` for HTML content

### 6.6 The "Stupid Person Check" (MANDATORY Final Step):
**Before marking ANY subtopic complete, ask:**

> "Would the least prepared student in the class be able to understand this topic **completely** from my content alone, without needing to Google anything or ask a friend?"

**If the answer is NO**, you must add:
- More intuition/analogies
- Step-by-step breakdowns
- Parameter explanations
- Worked examples with every calculation shown
- Common mistake warnings

**The content must be SELF-SUFFICIENT.** The student should be able to:
1. Recognize when to use this distribution/formula
2. Understand what each symbol means
3. Apply it to a new problem
4. Avoid common exam traps

**No shortcuts.** If in doubt, add more explanation.
