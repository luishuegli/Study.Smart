---
description: Complete workflow for implementing a new topic/subtopic
---

// turbo-all

# Topic Implementation Workflow

> **Spirit:** Brilliant.org meets Apple. Make students think "this is fun to learn from."

---

## Pre-Flight Checks (MANDATORY — NO EXCEPTIONS)

> **Every rule file AND all utilities MUST be read before implementing a new topic.**

```
// turbo
1. view_file .agent/rules/rules.md
// turbo
2. view_file .agent/rules/pedagogy.md
// turbo
3. view_file .agent/rules/design-system.md
// turbo
4. view_file .agent/rules/layout.md
// turbo
5. view_file .agent/rules/interactive.md
// turbo
6. view_file .agent/rules/templates.md
// turbo
7. view_file .agent/adaptive-learning/synthesis.md
// turbo
8. view_file .agent/adaptive-learning/topic_[previous].md (if exists)
// turbo
9. view_file utils/layouts/__init__.py (UTILITY INDEX)
// turbo
10. view_file_outline utils/worked_example.py
// turbo
11. view_file_outline utils/ask_yourself.py
// turbo
12. view_file_outline utils/exam_essentials.py
```

**Confirm:** ✓ All rule files read | ✓ All utils scanned | ✓ Pending rules from synthesis

---

## Gold Standard References (USE SPARINGLY)

> **⚠️ Each topic's content is UNIQUE. Gold standards are starting points, NOT templates.**

- Topics 1+2 show possible patterns — **adapt, don't copy**
- What worked in one section may be wrong for another
- Always prioritize the **actual content and pedagogy** over matching examples

---

## MANDATORY Utilities (USE THESE — DON'T REINVENT)

> **Before writing ANY custom HTML or layout code, check if a utility exists.**

### Core Imports (Always)
```python
from utils.localization import t
from utils.quiz_helper import render_mcq
from utils.ask_yourself import render_ask_yourself
from utils.exam_essentials import render_exam_essentials
from utils.worked_example import render_worked_example
```

### Layout Utilities (EVALUATE EACH ONE)
```python
from utils.layouts import (
    render_single_formula,     # A: Formula + Intuition + Decoder
    render_comparison,         # B: Side-by-side (e.g., Joint vs Marginal)
    render_formula_grid,       # C: Multiple formulas in grid (MAX 2 cols!)
    render_steps,              # D: Step-by-step process
    render_formula_breakdown,  # E: Deep dive into formula parts
    render_definition,         # G: Definition card
    render_decision_tree,      # H: Decision flow
)
from utils.layouts.foundation import (
    grey_callout,             # Standard grey info box
    intuition_box,            # Opening intuition hook
    variable_decoder,         # Symbol explanations
    key_insight,              # "Aha!" moment box
    inject_equal_height_css,  # For side-by-side containers
)
```

### ⚠️ MANDATORY Utility Selection Checklist

**Before Phase 3, explicitly evaluate EACH utility below. Answer YES/NO/NA for each:**

| Utility | Question to Ask | Answer |
|---------|-----------------|--------|
| `render_single_formula` | Does this topic introduce ONE key formula? | |
| `render_comparison` | Are there TWO concepts to compare/contrast? | |
| `render_formula_grid` | Are there 3+ related formulas (cheat sheet)? | |
| `render_formula_breakdown` | Is there a complex formula needing part-by-part explanation? | |
| `render_definition` | Is there a key term needing formal definition? | |
| `render_decision_tree` | Is there a "which method/formula to use" decision? | |
| `render_steps` | Is there a procedure/algorithm to explain? | |
| `render_worked_example` | Is there a numerical example to walk through? | |

**RULE:** You MUST use AT LEAST 3 different utilities per subtopic (excluding ask_yourself and exam_essentials which are always required).

### Utility Selection Guide

| Content Type | Use This Utility |
|--------------|------------------|
| **One formula + intuition + decoder** | `render_single_formula` |
| **Compare two concepts** (Cov vs Corr, E vs Var, Joint vs Marginal) | `render_comparison` |
| **Multiple related formulas** (cheat sheet, formula summary) | `render_formula_grid` |
| **Complex formula breakdown** (Binomial PMF, Hypergeometric) | `render_formula_breakdown` |
| **Definition of term** (Independence, Random Variable) | `render_definition` |
| **Which method to choose** (distribution selection, test selection) | `render_decision_tree` |
| **Step-by-step procedure** (Bayes, Hypothesis testing) | `render_steps` |
| **Numerical worked example** (calculation with answer) | `render_worked_example` |
| **Self-check questions** | `render_ask_yourself` (ALWAYS) |
| **Exam tips + trap** | `render_exam_essentials` (ALWAYS) |

**RULE:** If you find yourself writing raw HTML for a layout that looks like one of these utilities, STOP and use the utility instead.

---

## Adaptive Learning

**Before:** Read synthesis.md for pending rules
**During:** Log fixes automatically when user corrects something
**Format:** `### Fix N: Title` → What was wrong → What I changed → Pattern → Files

---

## Phase 1: THEORY EXTRACTION

**Sources (ALWAYS READ FIRST):**
- `data/All_Theory/course_theory.txt` — Official lecture content
- `data/All_Theory/handwritten_Statistikskript_VWL_HS2025.pdf` — Visual reference for formatting

**Extract:** Formulas, variables+meanings, conditions, misconceptions

**Gate:** □ LaTeX formulas □ All variables □ Bilingual

---

## Phase 2: EXAM QUESTION AUDIT

**Source:** `data/exam_questions.py` — Questions already allocated to subtopics

**Process:**
1. Check existing MCQs in subtopic — does each one TEST this exact theory?
2. If mismatch → reallocate or flag
3. If no question closely tests the core insight → CREATE new question

**Create New:** Test core insight, 2-3 min answerable, plausible distractors

**Gate:** □ ≥1 MCQ closely tests theory □ Bilingual options

---

## Phase 3: 12-YEAR-OLD THEORY

**Structure (in order):**
1. **Simple Analogy** (grey box, no math, end with "This is what [formula] calculates")
2. **The Formula** (clean LaTeX)
3. **Variable Decoder** ($X$ = **Name** — explanation)
4. **Key Insight** (grey box, the "aha!" moment)

**Gate:** □ 12-y-o could explain □ Every symbol defined □ No naked formulas

---

## Phase 4: INTERACTIVE (PROPOSE 4 OPTIONS)

> **ALWAYS propose 4 different interactive element options before implementing.**

**Process:**
1. Identify core insight hard to grasp from text
2. Check Topics 1+2 for variety — AVOID repetition
3. **PROPOSE 4 OPTIONS** with: Type, Scenario, Mission, Rough Layout
4. Wait for user to select best option
5. Implement selected option

**Types:** Slider (continuous), Click grid (discrete), Pills (category), Button sequence (multi-step), Simulation (probability)

**Gate:** □ @st.fragment □ Different from last 3 topics □ Concrete scenario □ Completion state

---

## MANDATORY: Full Page Layout Preview

> **Every implementation plan MUST include a complete ASCII mockup of the page structure.**

**Purpose:** User can visualize the ENTIRE layout before any code is written.

**Format:** Use ASCII boxes, lines, and indentation to show:
- All section headers (### Title)
- Container boundaries (borders, columns)
- Rough content placement (formulas, text, controls)
- Component names (render_comparison, render_steps, etc.)

**Example:**
```
Header: Topic Title
Subtitle: One-liner

────────────────────────────────────────────

### 1. INTUITION
Grey box - NO math symbols
"Simple analogy..."

────────────────────────────────────────────

### 2. THEORY
┌─────────────────────────┐    ┌─────────────────────────┐
│ **Concept A**           │    │ **Concept B**           │
│ Formula                 │    │ Formula                 │
│ Explanation             │    │ Explanation             │
└─────────────────────────┘    └─────────────────────────┘
(render_comparison)

────────────────────────────────────────────

### 3. INTERACTIVE
[Controls] → [Visualization] → [Result]
(@st.fragment)

...
```

**RULE:** The plan is INCOMPLETE without this layout preview.

---

## Phase 5: FRAG DICH

**Question types:** "Is this X or Y?", "What distribution for [signal]?", "Why can't we use [alternative]?"

**Use:** `render_ask_yourself(header, questions, conclusion)`

**Gate:** □ 3-5 questions □ Tests recognition □ Bilingual

---

## Phase 6: EXAM ESSENTIALS

**Structure:**
- **Trap:** #1 mistake + rule to avoid
- **Tips:** Numbered, each with "Why?" explanation

**Use:** `render_exam_essentials(trap, trap_rule, tips)`

**Gate:** □ Real #1 mistake □ Class A tips □ Grey container

---

## Phase 7: BACKEND

```python
SUBTOPIC_QUESTION_COUNTS = {"X.Y": N}
```

All MCQs need: course_id, topic_id, subtopic_id, question_id

**Gate:** □ Counts updated □ Tracking params □ Unique IDs

---

## Phase 8: FINAL QA

**Browser:** □ No errors □ Equal height □ Interactive works □ MCQ tracks
**Code:** □ No emojis □ Grey callouts □ Headers outside containers □ Bilingual □ @st.fragment
**Cohesion:** □ Theory follows pedagogy □ Interactive variety □ Utils used

---

## Summary Topics: Learn-Test-Learn

> For overview topics (like 4.9), use chunked layout.

**Flow:** Chunk→Cards→MCQ | Chunk→Cards→MCQ | Key Formulas→Ask Yourself→Exam Essentials

**Compact Card:** Name (bold) | Notation (mono) | One-liner (when to use)

**Ref:** `topic_4_9_content.py`

---

## Mandatory Elements

```
☑️ Theory (Analogy→Formula→Decoder→Insight)
☑️ ≥3 layout utilities used (not counting ask_yourself/exam_essentials)
☑️ ≥1 visual/interactive with @st.fragment
☑️ Frag Dich (render_ask_yourself)
☑️ Exam Essentials (render_exam_essentials)
☑️ ≥1 MCQ with tracking
☑️ SUBTOPIC_QUESTION_COUNTS
```

**Utility Examples per Topic Type:**

| Topic Type | Suggested Utilities |
|------------|---------------------|
| **Formula introduction** | `render_single_formula` + `render_worked_example` + `render_definition` |
| **Two-concept comparison** | `render_comparison` + `render_decision_tree` + `render_worked_example` |
| **Complex formula** | `render_formula_breakdown` + `render_steps` + `render_worked_example` |
| **Distribution overview** | `render_formula_grid` + `render_decision_tree` + `render_comparison` |

