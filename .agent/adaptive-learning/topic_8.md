# Topic 8 Adaptive Learning Notes

## Topic 8.1: Intuitive Heuristic Approaches for Estimators

### Fixes Applied

#### 1. LaTeX in HTML Divs - DOES NOT WORK
**Issue**: Using `$...$` syntax in HTML `<div>` elements does not render LaTeX.
**Fix**: Use `st.latex()` instead, or put math inside `st.container(border=True)`.
```python
# WRONG - LaTeX won't render
st.markdown(f"<div>$\\hat{{\\mu}} = ...$</div>", unsafe_allow_html=True)

# CORRECT - Use st.latex()
st.latex(r"\hat{\mu} = ...")
```

#### 2. Intuition Box Should Be White, Not Grey
**Issue**: User expected "Intuition" section to use white container with border, not grey callout.
**Fix**: Use `st.container(border=True)` for Intuition sections:
```python
st.markdown("### Intuition")
with st.container(border=True):
    st.markdown(t(content["intuition"]), unsafe_allow_html=True)
```

#### 3. Vertical Centering in Side-by-Side Columns
**Issue**: Symbol (θ̂) not vertically centered with adjacent content.
**Fix**: Use explicit top/bottom padding to push content down:
```python
<div style="padding: 100px 0 40px 0;">  # More top than bottom
```

#### 4. Interactive Should Show Chart from Start
**Issue**: Chart only appeared after 3 rounds, felt arbitrary.
**Fix**: Always show empty chart with fixed axes, add data as rounds are played:
```python
fig = go.Figure()
if len(history) >= 1:
    # Add traces
fig.update_layout(xaxis=dict(range=[0, 20]), yaxis=dict(range=[0, 15]))
st.plotly_chart(fig)  # Always show, even if empty
```

#### 5. Interactive Should Show Full Calculation
**Issue**: Results felt "arbitrary" - didn't show X₁, X₂ values used.
**Fix**: Track last round and show calculation breakdown:
```python
st.session_state.sd_last = {"x1": x1, "x2": x2, "a": est_a, "b": est_b, ...}
# Then show:
st.latex(fr"\frac{{{x1:.1f} + {x2:.1f}}}{{2}} = {est_a:.1f}")
```

#### 6. Dynamic Chart Axes
**Issue**: Fixed x-axis range `[0, 20]` cut off data when user played 300+ rounds.
**Fix**: Make axes dynamic, with minimum for empty chart:
```python
xaxis=dict(range=[0, max(20, len(history) + 5)])  # Expands with data
```

#### 6. Relatable Scenario
**Issue**: Abstract "μ = 50" not intuitive for students.
**Fix**: Use relatable scenario - "pizza delivery time" with friends guessing.

#### 7. Intuitive Explanation of WHY
**Issue**: "A wins 55%" doesn't explain why.
**Fix**: Add explanation: "If you weight one friend more, you're taking a risk - what if that friend is wrong?"

### New Rules Identified

1. **INTUITION_WHITE_CONTAINER**: Intuition sections use `st.container(border=True)`, not grey callouts
2. **INTERACTIVE_EMPTY_CHART**: Show empty chart from start, add data as interaction happens
3. **INTERACTIVE_SHOW_CALCULATION**: Show actual values and calculation breakdown, not just results
4. **RELATABLE_SCENARIOS**: Use everyday examples (pizza delivery, friends guessing)
5. **EXPLAIN_THE_WHY**: Success messages should explain WHY, not just state the result

### Components Used
- `inject_equal_height_css()` - Side-by-side containers
- `render_worked_example()` - Student heights example
- `render_ask_yourself()` - Frag Dich section
- `render_exam_essentials()` - Trap + Tips
- `render_mcq()` - Exam practice
- `@st.fragment` - Interactive isolation
- `go.Figure()` with `st.plotly_chart()` - Running average chart

---

## Topic 8.2: Properties of Point Estimators

### Fixes Applied

#### 1. render_definition() API
**Issue**: Called with `definition=...` keyword argument.
**Fix**: Use `formal=...` instead — that's the correct parameter name.
```python
# WRONG
render_definition(term=..., definition=...)

# CORRECT
render_definition(term=..., formal=...)
```

#### 2. render_comparison() API
**Issue**: Used `header` and `description` keys in left/right dicts.
**Fix**: Use `title` and `insight` keys instead.
```python
# WRONG
left={"header": {...}, "description": {...}}

# CORRECT
left={"title": {...}, "insight": {...}}
```

#### 3. grey_callout() vs grey_info()
**Issue**: `grey_callout(label, content)` requires 2 arguments, called with 1.
**Fix**: Use `grey_info(content)` for single-argument grey boxes.
```python
# WRONG - grey_callout takes 2 args
grey_callout(t({...}))

# CORRECT - grey_info takes 1 arg
grey_info(t({...}))
```

### New Rules Identified

1. **API_CHECK_BEFORE_USE**: Always verify utility function signatures before use (view the .py file)
2. **GREY_INFO_FOR_SINGLE_ARG**: Use `grey_info()` for single content; `grey_callout()` for label+content

#### 4. Slider Jumping Bug (CRITICAL)
**Issue**: Slider jumps back to original value every second use.
**Cause**: Writing to session_state AFTER reading the slider value.
**Fix**: Use `on_change` callback pattern:
```python
# WRONG - Causes jumping bug
n = st.slider(..., value=st.session_state.n, key="slider")
st.session_state.n = n  # BUG: Overwrites after read!

# CORRECT - on_change callback
def update_value():
    st.session_state.my_value = st.session_state._slider_temp

st.slider(..., value=st.session_state.my_value, key="_slider_temp", on_change=update_value)
n = st.session_state.my_value
```
**Rule**: SLIDER_ON_CHANGE_PATTERN - Never write to state after reading slider. Use temp key + callback.

#### 5. Floating Grey Elements
**Issue**: Grey callouts (key_insight, tip boxes) floating outside containers look disconnected.
**Fix**: Include inside parent container using `---` dividers:
```python
with st.container(border=True):
    # Main content...
    st.markdown("---")
    st.markdown(f"**Key Insight:** {insight}")
    st.markdown("---")
    st.markdown(f"**Tip:** {tip}")
```
**Rule**: CONTAINED_GREY_ELEMENTS - Grey callouts should be inside a container unless standalone.

### Components Used
- `render_definition()` - Formal definitions with formulas
- `render_comparison()` - Side-by-side variance comparison
- `render_ask_yourself()` - Frag Dich section
- `render_exam_essentials()` - Tips + Trap
- `grey_info()` - Scenario boxes
- `key_insight()` - Aha-moment boxes
- `@st.fragment` - Both interactive elements isolated
- `go.Figure()` with `st.plotly_chart()` - Consistency distribution + Error chart

#### 6. Blue Slider Styling (Default Red Override)
**Issue**: Streamlit sliders have red/pink default styling. User requested blue semantic color.
**Fix**: Inject scoped CSS to override slider track and thumb colors:
```python
st.markdown("""
<style>
.stSlider div[data-baseweb="slider"] > div:first-child > div:first-child { background-color: #007AFF !important; }
.stSlider div[role="slider"] { background-color: #FFFFFF !important; border: 2px solid #007AFF !important; }
</style>
""", unsafe_allow_html=True)
```
**Rule**: BLUE_SLIDER_DEFAULT - All sliders should be blue unless semantically different (e.g., red for outlier).

---

## Topic 8 Global Fixes (Session 2026-01-05)

### Exam Essentials LaTeX Consistency
**Scope**: All topics with exam_essentials sections
**Issue**: Plain text math like "Cov = 0" instead of LaTeX `$\text{Cov} = 0$`
**Files Fixed**:
- topic_5_5_content.py - "Cov = 0" → `$\text{Cov} = 0$` in trap and trap_rule
- All other topics already had LaTeX (verified)

**Rule**: EXAM_ESSENTIALS_LATEX_STRICT - ALL math in exam_essentials (trap, trap_rule, tips) MUST use LaTeX notation.

---

## Topic 8.3: Methods for Constructing Estimators

### Implementation Summary

Successfully implemented Topic 8.3 with maximum clarity approach - "Two Methods, One Goal" theme.

### Fixes Applied

#### 1. render_steps API Mismatch
**Issue**: Used `header`, `title`, `content` keys - API expects `title`, `action`, `explanation`.
**Fix**: Updated data structure to match API:
```python
# WRONG
{"title": {"de": "Schritt 1...", "en": "Step 1..."}, "content": {...}}

# CORRECT
{"action": {"de": "Erwartungswert aufschreiben", "en": "Write the expected value"}, "explanation": {...}}
```

#### 2. render_formula_breakdown API Mismatch
**Issue**: Used `header`, `intuition`, `symbol` - API expects `title`, `story`, `formula`.
**Fix**: Updated parameter names and parts structure:
```python
# WRONG - parts
{"symbol": r"L(\theta)", "name": {...}, "description": {...}}

# CORRECT - parts
{"formula": r"L(\theta)", "name": {...}, "explanation": {...}}
```

#### 3. render_decision_tree API Mismatch
**Issue**: Used complex `nodes`/`edges` graph structure - API expects simple `decisions` list.
**Fix**: Converted to IF/THEN format:
```python
# WRONG
{"nodes": [...], "edges": [...]}

# CORRECT
{"decisions": [
    {"condition": {...}, "result": {...}},
    {"condition": {...}, "result": {...}, "highlight": True}  # Optional
]}
```

#### 4. render_comparison API Mismatch
**Issue**: Used `header` and tried to pass formulas as separate args.
**Fix**: Use `title`, include formula in left/right dicts:
```python
# CORRECT
left_data = {"title": {...}, "insight": {...}, "formula": r"..."}
render_comparison(title=..., left=left_data, right=right_data)
```

### New Rules Identified

1. **API_VERIFICATION_MANDATORY**: Before using ANY utility, read the actual .py file to verify the exact API signature
2. **STEPS_ACTION_EXPLANATION**: `render_steps` uses `action` and `explanation`, NOT `title` and `content`
3. **FORMULA_BREAKDOWN_STORY**: `render_formula_breakdown` uses `story` for intuition, `formula` in parts (not `symbol`)
4. **DECISION_TREE_SIMPLE**: `render_decision_tree` uses flat `decisions` list, NOT graph `nodes`/`edges`

### Components Used
- `render_comparison()` - MOM vs MLE side-by-side
- `render_steps()` - Both MOM and MLE procedures (×2)
- `render_formula_breakdown()` - Likelihood function explanation
- `render_worked_example()` - Poisson MOM example
- `render_decision_tree()` - Method selection guide
- `render_ask_yourself()` - Frag Dich section
- `render_exam_essentials()` - Tips + Trap
- `@st.fragment` - Method Detective quiz
- Interactive quiz with 5 rounds, state management

### Quiz Fixes (Session 2)

#### 5. LaTeX in Quiz Snippets
**Issue**: Quiz snippets showed plain text math like "E[X] = 1/λ" instead of LaTeX.
**Fix**: Restructure quiz questions to separate text, latex, and context:
```python
# WRONG - Plain text math
{"snippet": {"de": "E[X] = 1/λ. Setze X̄ = 1/λ, also λ̂ = 2.", ...}}

# CORRECT - Proper LaTeX
{
    "text": {"de": "Gegeben:", "en": "Given:"},
    "latex": r"E[X] = \frac{1}{\lambda}, \quad \bar{X} = 0.5 \implies \hat{\lambda} = 2",
    "context": {"de": "Setze Stichprobenmittel = Erwartungswert", "en": "Set sample mean = expected value"}
}
```
**Rule**: QUIZ_LATEX_SEPARATE - Separate LaTeX from prose in quiz questions for proper rendering.

#### 6. Pill Button Consistency
**Issue**: Buttons turned rectangular after clicking (Streamlit default).
**Fix**: Inject scoped CSS for pill buttons AND use matching border-radius in result HTML:
```python
# CSS for buttons
st.markdown("""
<style>
.stButton > button {
    border-radius: 20px !important;
    padding: 8px 24px !important;
}
</style>
""", unsafe_allow_html=True)

# HTML for result pills (matching radius)
st.markdown(f"""<div style="border-radius: 20px; padding: 10px 24px;">...</div>""")
```
**Rule**: PILL_BUTTON_CONSISTENCY - Both st.button CSS and result HTML must use same border-radius.

#### 7. Decision Tree Checkmark Removal
**Issue**: Decision tree `highlight=True` items showed a checkmark "✓" which was inconsistent.
**Fix**: Removed checkmark from `decision_tree.py`, now just uses bold and exclamation:
```python
# BEFORE
st.markdown(f"**IF** {if_text} → **{then_text}** ✓")

# AFTER
st.markdown(f"**IF** {if_text} → **{then_text}!**")
```
**Rule**: NO_EMOJI_IN_UTILITIES - Utility components should not add emojis/symbols.

#### 8. Feedback Box Consolidation
**Issue**: Feedback with LaTeX was split into multiple green boxes (disjointed).
**Fix**: Use `st.success()`/`st.error()` for unified styling, display LaTeX separately below:
```python
# Build full text
explanation_text = t(q["explanation"])
if "explanation_suffix" in q:
    explanation_text += " ... " + t(q["explanation_suffix"])

# Single unified box
st.success(explanation_text)

# LaTeX below (if present)
if "explanation_latex" in q:
    st.latex(q["explanation_latex"])
```
**Rule**: UNIFIED_FEEDBACK_BOX - Don't split feedback into multiple colored boxes.

---

## Topic 8.4: Maximum Likelihood Estimation (MLE)

### Fixes Applied

#### 1. Bilingual Option Consistency in Exam Questions
**Issue**: English mode exam questions showing German text ("Richtig", "Falsch", "und", "Erwartungstreu", "Varianz ist")
**Fix**: Fixed all German-only terms in `data/exam_questions.py`:
```python
# WRONG
{"de": "Nur a", "en": "Nur a"}

# CORRECT
{"de": "Nur a", "en": "Only a"}
```
**Terms fixed**: Richtig→True, Falsch→False, und→and, Erwartungstreu→Unbiased, Varianz ist→Variance is

**Rule**: BILINGUAL_OPTIONS_STRICT - Every option dict MUST have proper translations for both de/en.

#### 2. Literal `<br>` Tags in Problem Renderer
**Issue**: `<br>` appearing as literal text in problem descriptions and solutions
**Cause**: `st.markdown()` calls missing `unsafe_allow_html=True`
**Fix**: Added `unsafe_allow_html=True` to all markdown calls in `utils/problem_renderer.py`:
```python
# WRONG
st.markdown(t(stem_text))

# CORRECT
st.markdown(t(stem_text), unsafe_allow_html=True)
```
**Files fixed**:
- `problem_renderer.py` lines 31, 76-79, 103, 127, 164

**Rule**: PROBLEM_RENDERER_HTML_SAFE - All st.markdown in problem_renderer must have unsafe_allow_html=True.

#### 3. Ask Yourself LaTeX in HTML Context
**Issue**: LaTeX `$\hat{\theta}$` rendering as literal text in `render_ask_yourself()` blue box
**Cause**: LaTeX doesn't render inside HTML divs
**Fix**: Use Unicode symbols instead of LaTeX in question content:
```python
# WRONG - Won't render
{"de": "Was bedeutet $\\hat{\\theta}$ vs $\\theta$?", "en": "..."}

# CORRECT - Unicode works
{"de": "Was bedeutet **θ̂ vs θ**?", "en": "What does **θ̂ vs θ** mean?"}
```
**Rule**: ASK_YOURSELF_NO_LATEX - Use Unicode (θ̂, μ, σ) instead of LaTeX in ask_yourself questions.

#### 4. Display Math Centering (Piecewise Functions)
**Issue**: `$$...$$` blocks rendering as inline math (left-aligned) instead of centered display math
**Cause**: Markdown parser not recognizing block math despite blank lines
**Fix**: Wrap display math in centered div:
```python
# WRONG - Left-aligned inline
$$f_X(x) = \begin{cases} ... \end{cases}$$

# CORRECT - Forced center
<div style="text-align: center; margin: 16px 0;">

$$f_X(x) = \begin{cases} ... \end{cases}$$

</div>
```
**Rule**: CENTERED_DISPLAY_MATH - Wrap `$$...$$` blocks in `<div style="text-align: center; margin: 16px 0;">` for reliable centering.

#### 5. Piecewise Function Formatting
**Issue**: Cramped inline display of piecewise functions in exam problems
**Fix**: Added proper spacing with bold headers, line breaks, and horizontal rules:
```python
# CORRECT structure
**Problem 5 (15 Points)**

**Part 5A (7 Points)**

Consider the following probability density function:

<div style="text-align: center; margin: 16px 0;">
$$f_X(x) = ...$$
</div>

---

**Part 5B (8 Points)**
...
```
**Rule**: PROBLEM_VISUAL_STRUCTURE - Use bold headers, line breaks, and centered divs for multi-part problems.

### Global CSS Added

#### Display Math Centering (views/styles.py)
```css
.katex-display {
    text-align: center !important;
}
[data-testid="stMarkdownContainer"] .katex-display {
    margin-left: auto !important;
    margin-right: auto !important;
}
```

### Components Used
- `render_multi_stage_problem()` - Multi-part exam problems
- `render_open_question()` - Open-ended questions
- `render_ask_yourself()` - Frag Dich (with Unicode symbols)
- `render_exam_essentials()` - Tips + Trap
- Various exam questions from `data/exam_questions.py`

### New Rules Summary

| Rule | Description |
|------|-------------|
| BILINGUAL_OPTIONS_STRICT | All option dicts must have proper de/en translations |
| PROBLEM_RENDERER_HTML_SAFE | problem_renderer markdown needs unsafe_allow_html=True |
| ASK_YOURSELF_NO_LATEX | Use Unicode (θ̂, μ) not LaTeX in ask_yourself |
| CENTERED_DISPLAY_MATH | Wrap `$$` blocks in centered div for reliable centering |
| PROBLEM_VISUAL_STRUCTURE | Bold headers + line breaks + centered divs for problems |
