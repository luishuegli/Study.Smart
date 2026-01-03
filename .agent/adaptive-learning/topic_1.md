# Adaptive Learning: Topic 1 (Basics of Probability)

> **Purpose:** Log fixes during Topic 1 implementation.
> **Phase:** SYNTHESIZE (complete)
> **Status:** Complete

---

## Fixes Log

### Fix 1: Intuition Section Placement
- **What was wrong:** "Core Idea" / intuition was INSIDE bordered containers
- **What I changed:** Moved intuition OUTSIDE and ABOVE the container using `intuition_box()`
- **Why it matters:** Pedagogy rule: Intuition comes first, before diving into formula details
- **Pattern:** INTUITION-OUTSIDE
- **Files affected:** `topic_1_9_content.py`, all layout utilities

---

### Fix 2: Layout Utility Updates
- **What was wrong:** `single_formula.py`, `formula_breakdown.py` had intuition inside container
- **What I changed:** Refactored both to move intuition outside, added `label` param to `intuition_box()`
- **Why it matters:** Consistent pedagogy pattern across all layouts
- **Pattern:** LAYOUT-INTUITION-OUTSIDE
- **Files affected:** `utils/layouts/single_formula.py`, `utils/layouts/formula_breakdown.py`, `utils/layouts/foundation.py`

---

### Fix 3: Formula Grid Too Narrow
- **What was wrong:** 4-column grid in Topic 1.11 caused LaTeX formulas to be cut off
- **What I changed:** Changed to 2-column layout for formula cards
- **Why it matters:** Formula readability is critical; narrow columns break LaTeX
- **Pattern:** MAX-2-COLUMNS-FOR-FORMULAS
- **Files affected:** `topic_1_11_content.py`

---

### Fix 4: Ask Yourself Added to Summary
- **What was wrong:** Topic 1.11 Summary missing "Ask Yourself" decision bridge
- **What I changed:** Added frag_dich data and render_ask_yourself() call
- **Why it matters:** Every topic needs self-assessment checkpoints
- **Pattern:** FRAG-DICH-MANDATORY
- **Files affected:** `topic_1_11_content.py`

---

### Fix 5: F-string Backslash Error
- **What was wrong:** `W\'keit` in f-string caused Python 3.12+ syntax error
- **What I changed:** Extracted text to variable before embedding in f-string
- **Why it matters:** Python 3.12+ disallows backslashes in f-string expressions
- **Pattern:** NO-BACKSLASH-IN-FSTRING
- **Files affected:** `topic_1_11_content.py`

---

## Summary Statistics

| Category | Count |
|----------|-------|
| Total fixes | 5 |
| Layout fixes | 3 |
| Styling fixes | 1 |
| Pedagogy fixes | 1 |
| Interactive fixes | 0 |

---

## Patterns Emerging

| Pattern | Occurrences | Rule Candidate? |
|---------|-------------|-----------------|
| INTUITION-OUTSIDE | 3 | ✅ YES - Layout rule |
| MAX-2-COLUMNS-FOR-FORMULAS | 1 | ✅ YES - LaTeX readability |
| NO-BACKSLASH-IN-FSTRING | 1 | ✅ YES - Python 3.12+ compat |
| FRAG-DICH-MANDATORY | 1 | Already exists |

---

## Rules to Integrate

1. **Layout Rule Update:** All layout utilities with intuition MUST render it OUTSIDE and ABOVE the container
2. **Formula Column Limit:** Never use more than 2 columns for formula grids (LaTeX needs horizontal space)
3. **Python Compatibility:** Never use backslashes in f-string expressions; extract to variable first

---

## Notes

Topic 1 implementation complete with all pedagogy sections. Key insight: intuition_box should be a standalone element, not nested inside containers. This allows visual separation between "the big idea" and "the details."
