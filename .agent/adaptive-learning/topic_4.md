# Topic 4 Adaptive Learning Log

**Date:** 2026-01-03
**Topic:** 4 - Stochastic Models (Distributions)

---

## Fixes Applied

### 1. `st.info()` → Grey Callout (7 files)
**Issue:** `st.info()` creates blue callout boxes that clash when nested inside `st.container(border=True)`.
**Rule:** Use grey HTML divs for static informational callouts inside bordered containers.

**Files Fixed:**
- `topic_4_1_content.py` — "No MCQ" message
- `topic_4_2_content.py` — "Bernoulli tested in Binomial" message
- `topic_4_4_content.py` — "No MCQ" message
- `topic_4_5_content.py` — "Why rectangular" + "No MCQ"
- `topic_4_6_content.py` — "Same λ" + "No MCQ"
- `topic_4_7_content.py` — Z-transform meaning + "No MCQ"
- `topic_4_8_content.py` — Key insight + "No MCQ"

**Exception:** `st.info()` OK inside interactive missions (dynamic feedback).

---

### 2. `st.caption()` Doesn't Render HTML
**Issue:** `st.caption()` shows `<strong>` tags as raw text.
**Fix:** Use `st.markdown()` with `unsafe_allow_html=True` and `<small>` styling.

**File:** `topic_4_8_content.py` — Formula breakdown section

---

### 3. Colorful Step Boxes → Plain LaTeX
**Issue:** Worked examples used colorful boxes (blue, green, yellow, red) for step labels. Looks cluttered.
**Fix:** Simple bold text labels + proper LaTeX formulas.

**File:** `topic_4_8_content.py` — Step-by-Step Example section

**Before:**
```python
step_colors = {"Parameter": ("#dbeafe", "#1d4ed8"), ...}
st.markdown(f'<div style="background:{bg}...">{label}</div>')
st.markdown(content_text)  # Plain text with C(M,x)
```

**After:**
```python
st.markdown(f"**{t(step['label'])}:**")
st.latex(step["latex"])  # Proper LaTeX: \binom{M}{x}
st.caption(t(step["note"]))
```

---

### 4. `render_exam_essentials` HTML Rendering
**Issue:** Utility didn't render HTML in content (showed raw `<br>` and `<em>` tags).
**Fix:** Added `unsafe_allow_html=True` to all content markdown calls.

**File:** `utils/exam_essentials.py`

---

### 5. Semantic Colored LaTeX in Worked Examples
**Issue:** Math in worked examples used plain black numbers, making it hard to map formula parts to variables.
**Fix:** Use LaTeX `\color{#HEX}` commands to color numbers based on their meaning. Colors carry through all steps (Given → Find → Formula → Calculation).

**Universal Color Mapping:**
| Color | Hex | Meaning |
|-------|-----|---------|
| Blue | #007AFF | n, N, λ, μ, a, b (parameters / pool size) |
| Red | #FF4B4B | k, x, specific query values |
| Green | #16a34a | p, σ (probability / std dev) |
| Purple | #9B59B6 | z-score (intermediate transformed value) |
| Gray | #6B7280 | N-M, n-x (the "other" category) |

**Files Refactored:**
- `topic_4_3_content.py` (Binomial): n=blue, k=red, p=green
- `topic_4_4_content.py` (Poisson): λ=blue, x=red
- `topic_4_5_content.py` (Rectangular): a,b=blue, query=red
- `topic_4_6_content.py` (Exponential): λ/E[X]=blue, x=red
- `topic_4_7_content.py` (Normal): μ=blue, σ=green, x=red, z=purple
- `topic_4_8_content.py` (Hypergeometric): N,n=blue, M,x=red, N-M=gray

**Key Pattern:** Colors flow from "Given" step through to "Formula" step, creating visual traceability.

**LaTeX Example:**
```latex
\binom{\color{#007AFF}12}{\color{#FF4B4B}5} \times {\color{#16a34a}0.35}^{\color{#FF4B4B}5}
```

---

## Pending Rules to Integrate

| Rule | Description | Priority |
|------|-------------|----------|
| Grey Callout Only | No `st.info/warning` inside containers | HIGH |
| HTML in Captions | Use `st.markdown` with styling, not `st.caption` | MEDIUM |
| LaTeX for Math | Use `st.latex()` not plain text for formulas | HIGH |
| Plain Step Labels | No colorful boxes in worked examples | LOW |

---

## Cross-Topic Patterns

These fixes likely apply to other topics:
- [ ] Check all `st.caption()` calls with HTML content
- [ ] Check all `st.success()` calls inside containers
- [ ] Check all worked examples for plain-text math
