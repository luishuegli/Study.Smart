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

