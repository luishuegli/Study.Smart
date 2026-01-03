# Adaptive Learning: Synthesis

> **Purpose:** Track patterns across topics and pending rules to integrate.
> **Updated:** 2026-01-03

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

### From Topic 4
| Rule | Evidence | Add to File | Status |
|------|----------|-------------|--------|
| Grey callouts only | Fixes #2, #5, #7 | design-system.md | ⏳ Pending |
| Headers outside containers | Fixes #1, #3 | layout.md | ✅ Integrated |

---

## Cross-Topic Patterns

_Same issue appearing across multiple topics = CRITICAL rule._

| Pattern | Topics | Severity | Rule? |
|---------|--------|----------|-------|
| Intuition inside containers | T1, T2 | CRITICAL | ⏳ NEW - Layout utilities updated |
| Colored callouts inside containers | T3, T4 | HIGH | ✅ Added |
| Equal height CSS missing | T1, T2, T3 | CRITICAL | ✅ Added |
| Inline custom HTML for traps | T2 | MEDIUM | ⏳ NEW - Use utilities |
| Formula columns too narrow | T1 | MEDIUM | ⏳ NEW - Max 2 columns |

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

### Topic 4 Synthesis
- **Completed:** [Date]
- **Total fixes:** X
- **New rules created:** Y
- **Key learnings:** [Summary]

### Topic 3 Synthesis
- **Completed:** [Date]
- **Total fixes:** X
- **New rules created:** Y
- **Key learnings:** [Summary]

---

## Rule Evolution Tracker

_Track how rules improve over time._

| Rule | Version | Origin | Refinements |
|------|---------|--------|-------------|
| Intuition-outside | v1 | Topic 1, Fix #1 | Added to all layout utilities |
| Grey callouts | v1 | Topic 4, Fix #2 | - |
| Header-out protocol | v2 | Topic 2, refined in T4 | Added edge cases |
| Max formula columns | v1 | Topic 1, Fix #3 | - |

---

## Metrics

| Metric | T1 | T2 | T3 | T4 | T5 | Trend |
|--------|----|----|----|----|----|----|
| Fixes needed | 5 | 2 | - | - | - | ↓ |
| Implementation time | - | - | - | - | - | ↓ |
| Rules added | 3 | 1 | - | - | - | ↑ |
