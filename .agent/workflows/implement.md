---
description: Complete workflow for implementing a new topic/subtopic
---

// turbo-all

# Topic Implementation Workflow

> **Spirit:** Brilliant.org meets Apple. Make students think "this is fun to learn from."

---

## Pre-Flight Checks (MANDATORY — NO EXCEPTIONS)

> **Every rule file MUST be read before implementing a new topic.**

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
```

**Confirm:** ✓ All rule files read | ✓ Pending rules from synthesis | ✓ Theory structure clear

---

## Gold Standard References (USE SPARINGLY)

> **⚠️ Each topic's content is UNIQUE. Gold standards are starting points, NOT templates.**

- Topics 1+2 show possible patterns — **adapt, don't copy**
- What worked in one section may be wrong for another
- Always prioritize the **actual content and pedagogy** over matching examples

---

## MANDATORY Utilities

> **See `.agent/workflows/implement-reference.md` for full code snippets.**

**Always import:** `t`, `render_mcq`, `render_ask_yourself`, `render_exam_essentials`, `render_worked_example`

**Layout utilities:** `render_single_formula`, `render_comparison`, `render_formula_grid`, `render_definition`, `grey_callout`, `intuition_box`, `variable_decoder`, `key_insight`

**Rules:** Use utils, don't write inline HTML. No backslash escapes in f-strings.

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
☑️ ≥1 visual/interactive
☑️ Frag Dich
☑️ Exam Essentials
☑️ ≥1 MCQ with tracking
☑️ SUBTOPIC_QUESTION_COUNTS
```
