# Adaptive Learning: Topic 9

> **Topic:** Confidence Intervals
> **Subtopics:** 9.1 Concept, 9.2 Derivation, 9.3 Duality, 9.4 Summary
> **Last Updated:** 2026-01-05

---

## Fixes Log

### Session: 2026-01-05 (Topic 9.4 Summary)

#### Fix #1: UNICODE_IN_HTML_CONTEXTS
**Issue:** LaTeX `$\mu_0$`, `$H_0$`, `$\sigma$`, `$\theta$`, `$\alpha$` rendered as raw text (with dollar signs) in grey callouts, MCQ questions, and solutions.

**Root Cause:** `st.markdown(..., unsafe_allow_html=True)` disables LaTeX rendering. All content in:
- Grey callouts (decision_rule, analogy, trap)
- MCQ questions (via `render_mcq` which uses `unsafe_allow_html=True`)
- MCQ solutions (HTML formatted)
- Exam Essentials (tips, trap_rule)

...CANNOT use LaTeX inline math.

**Fix:** Use Unicode symbols instead:
```python
# ❌ WRONG - LaTeX in HTML context
"$\\mu_0$ IM Intervall → $H_0$ NICHT verwerfen"

# ✅ CORRECT - Unicode in HTML context
"μ₀ IM Intervall → H₀ NICHT verwerfen"
```

**Unicode Symbol Reference:**
| LaTeX | Unicode | Description |
|-------|---------|-------------|
| `$\mu$` | μ | Greek mu |
| `$\mu_0$` | μ₀ | Mu with subscript zero |
| `$H_0$` | H₀ | H with subscript zero |
| `$\sigma$` | σ | Greek sigma |
| `$\theta$` | θ | Greek theta |
| `$\alpha$` | α | Greek alpha |
| `$S_n$` | Sₙ | S with subscript n |
| `$\bar{x}$` | x̄ | X with macron (bar) |

#### Fix #2: LEARN_TEST_LEARN_SUMMARY_PATTERN
**Issue:** Summary pages (like 6.3, 9.4) need a specific structure for optimal learning.

**Pattern Applied:**
```
1. Big Picture Hook (Feynman-style analogy)
2. Chunk 1: Concept + Quick Check MCQ
3. Chunk 2: Formulas + Quick Check MCQ  
4. Chunk 3: Duality/Connection + Quick Check MCQ
5. Key Formulas Grid (2x2)
6. Decision Tree (interactive formula selector)
7. Ask Yourself (blue theme)
8. Exam Essentials
9. Official Exam Questions
```

#### Fix #3: SUMMARY_UTILITIES_CHECKLIST
**Utilities used in 9.4 (must use ≥3 different ones):**
- `render_comparison` — σ known vs unknown
- `render_formula_grid` (custom 2x2) — Key formulas
- `render_definition` (inline) — CI formal definition  
- `render_decision_tree` (custom @st.fragment) — Formula selector
- `render_ask_yourself` — Blue Bridge self-check
- `render_exam_essentials` — Tips + Trap

---

## Patterns Applied

### Pattern: Feynman-Style Intuition Hook
```python
"big_picture": {
    "header": {"de": "Das grosse Bild", "en": "The Big Picture"},
    "text": {
        "de": """Du hast gelernt, <strong>mit einem Netz zu fischen, statt mit einem Speer</strong>. 
<strong>Der Speer</strong> (Punktschätzung): Trifft manchmal, verfehlt oft.
<strong>Das Netz</strong> (Konfidenzintervall): Fängt den Fisch in 95% der Würfe.""",
        ...
    }
}
```

### Pattern: Chunk with Embedded MCQ
```python
def render_chunk_concept(model):
    chunk = content_9_4["chunk_concept"]
    st.markdown(f"### {t(chunk['header'])}")
    
    # Definition Card
    with st.container(border=True):
        # ... definition content ...
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Quick Check MCQ (embedded in chunk)
    render_chunk_mcq(chunk["mcq"], "concept", model)
```

### Pattern: Interactive Decision Tree
```python
@st.fragment
def render_formula_decision_tree():
    dt = content_9_4["decision_tree"]
    st.markdown(f"### {t(dt['header'])}")
    
    with st.container(border=True):
        options = dt["root"]["options"]
        option_labels = [t(opt["label"]) for opt in options]
        
        selected = st.radio(
            t({"de": "Wähle:", "en": "Choose:"}),
            options=option_labels,
            key="9_4_decision_tree",
            label_visibility="collapsed"
        )
        
        st.markdown("---")
        
        # Show formula for selected option
        for opt in options:
            if t(opt["label"]) == selected:
                st.latex(opt["result_formula"])
                st.caption(t(opt["result_note"]))
                break
```

---

## Rules Confirmed

| Rule | Status |
|------|--------|
| BLUE_THEME_ASK_YOURSELF_ONLY | ✅ Applied |
| DISPLAY_MATH_ALWAYS_LATEX (for st.latex calls) | ✅ Applied |
| UNICODE_IN_HTML_CONTEXTS | 🆕 NEW RULE |
| BILINGUAL_OPTIONS_STRICT | ✅ Applied |
| HEADERS_OUTSIDE_CONTAINERS | ✅ Applied |
| EQUAL_HEIGHT_CSS | ✅ Applied |

---

## Cross-Topic Patterns

### LATEX_VS_UNICODE Decision Matrix
| Context | Use LaTeX | Use Unicode |
|---------|-----------|-------------|
| `st.latex()` | ✅ | ❌ |
| `st.markdown()` (no HTML) | ✅ | ✅ |
| `st.markdown(..., unsafe_allow_html=True)` | ❌ | ✅ |
| Grey callouts | ❌ | ✅ |
| MCQ questions (render_mcq) | ❌ | ✅ |
| MCQ options (radio labels) | ❌ | ✅ |
| MCQ solutions | ❌ | ✅ |
| Exam Essentials | ❌ | ✅ |
| Worked Example steps | ✅ (st.latex) | ❌ |
