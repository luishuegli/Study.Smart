---
description: Complete workflow for implementing a new topic/subtopic
---

// turbo-all

# Topic Implementation Workflow

> **Spirit:** This is Brilliant.org meets Apple. Every screen should make a student think "this is actually fun to learn from."

---

## Pre-Flight Checks (MANDATORY - Execute These Commands)

> **DO NOT SKIP.** These are commands to run, not suggestions.

```
Step 1: view_file .agent/rules/pedagogy.md (lines 1-70)
Step 2: view_file .agent/adaptive-learning/synthesis.md
Step 3: view_file .agent/adaptive-learning/topic_[previous].md (if exists)
```

After reading files, confirm:
```
✓ I reviewed pedagogy.md - Theory structure: Analogy → Formula → Decoder → Insight
✓ I reviewed synthesis.md - Pending rules to apply: [list each one]
✓ I know the gold standard topics: Topics 1+2 (interactive elements + variety)
✓ I checked utils/layouts/ for available layout utilities
```

---

## MANDATORY Utilities (Use These, Don't Reinvent)

> **ALWAYS use existing utilities for consistent styling.** Never write inline HTML for these.

```python
# Required imports for EVERY topic file
from utils.localization import t                    # Translation
from utils.quiz_helper import render_mcq            # MCQ component
from utils.ask_yourself import render_ask_yourself  # Ask Yourself section
from utils.exam_essentials import render_exam_essentials  # Exam Essentials
from views.styles import render_icon, inject_equal_height_css  # Styling
```

### Layout Utilities (USE FOR NEW SECTIONS)

> **For brand new sections**, use the pre-built layouts from `utils/layouts/` instead of writing custom HTML.

```python
from utils.layouts import (
    render_single_formula,      # Layout A: Single formula intro
    render_comparison,          # Layout B: Side-by-side comparison
    render_formula_grid,        # Layout C: Multi-formula grid (2x2)
    render_steps,               # Layout D: Step-by-step process
    render_formula_breakdown,   # Layout E: Deep dive into formula
    render_definition,          # Layout G: Definition card
    render_decision_tree,       # Layout H: Decision tree
)
from utils.layouts.foundation import (
    grey_callout,               # Grey callout box
    intuition_box,              # Intuition section
    variable_decoder,           # Variable decoder section
    key_insight,                # Key insight section
)
```

**When to use layouts:**
- **New topic from scratch** → Use layouts for consistency
- **Filling gaps in existing topic** → Follow existing patterns in that file
- **Refactoring** → Migrate to layouts when touching that code

### Usage:
```python
# Ask Yourself (Frag Dich) - HEADER IS REQUIRED!
render_ask_yourself(
    header=content["frag_dich"]["header"],  # REQUIRED!
    questions=content["frag_dich"]["questions"],
    conclusion=content["frag_dich"]["conclusion"]
)

# Exam Essentials
render_exam_essentials(
    trap=content["exam_essentials"]["trap"],
    trap_rule=content["exam_essentials"]["trap_rule"],
    tips=content["exam_essentials"]["tips"]
)
```

**DO NOT:**
- Write inline `<div style="background: #f4f4f5...">` for Ask Yourself
- Write custom HTML for Exam Essentials
- Create new styling patterns
- **Use backslash escapes (\' or \") inside f-strings** (Python 3.12+ syntax error!)

---

## Adaptive Learning Integration

### BEFORE Implementation
1. Read `@adaptive-learning/synthesis.md` for pending rules
2. Check if similar topics had frequent fixes → apply those patterns proactively
3. Create `adaptive-learning/topic_[X].md` if it doesn't exist

### DURING Implementation (AUTOMATIC Real-Time Logging)

> **NO MANUAL TRIGGER NEEDED.** Log fixes AS THEY HAPPEN.

**When to log (automatically, don't ask):**
- User says "fix this", "change this", "wrong", "not stupid-person-proof"
- User points out an error or requests a change
- I make a mistake and correct it
- User rejects a design choice

**Log format (add to topic_[X].md immediately):**
```markdown
### Fix [N]: [Short Title]
- **What was wrong:** [Issue]
- **What I changed:** [Fix]
- **Pattern:** [Potential rule name]
- **Files:** [affected files]
```

### NO MANUAL SYNTHESIS STEP
- Logging happens in real-time, not at the end
- When moving to next topic, just start - no "synthesize" command needed
- Rules emerge naturally from accumulated logs

### The Compounding Effect

```
Topic 1: 15 fixes → lots of learning
Topic 3: 8 fixes → patterns emerging  
Topic 5: 3 fixes → rules stabilizing
Topic 10: 0-1 fixes → near-perfect implementation
```

### What to Log Per Phase

| Phase | What to log |
|-------|-------------|
| Theory | Formula formatting, decoder style, analogy quality, Stupid Person Rule violations |
| Interactive | Interaction type preferences, scenario styles |
| Exam Essentials | Trap format, tip clarity |
| Layout | CSS issues, container problems, spacing |

---

## Phase 1: THEORY EXTRACTION

**Sources:**
- `data/All_Theory/course_theory.txt`
- `data/All_Theory/handwritten_Statistikskript_VWL_HS2025.pdf`

**Extract:**
1. Main formula(s) for this subtopic
2. All variables and their meanings
3. Key conditions/assumptions
4. Common misconceptions (for trap section later)

**Output:** Draft theory content in content dictionary

**Quality Gate:**
```
□ All formulas in LaTeX
□ Every variable identified
□ Bilingual (de/en) prepared
```

---

## Phase 2: EXAM QUESTION AUDIT

**Sources:**
- `data/exam_questions.py`
- `exam_data.py`
- `data/exams/*.pdf`

**Process:**

```
1. Search for questions testing this specific theory
2. For each candidate question:
   - Does it TEST the core concept? (not just mention it)
   - Is it at appropriate difficulty?
   - Is it self-contained? (doesn't need other topics)
3. If match found → use it
4. If partial match → adapt it
5. If no match → CREATE new question
```

**Creating New Questions:**
- Must test the CORE insight, not edge cases
- Should be answerable in 2-3 minutes
- Include plausible distractors
- Write solution with step-by-step reasoning

**Quality Gate:**
```
□ At least 1 MCQ identified/created
□ Question tests the exact theory (not adjacent topic)
□ Bilingual options prepared
```

---

## Phase 3: 12-YEAR-OLD THEORY SECTION

**Structure (MANDATORY ORDER):**

### 3.1 Simple Analogy (Grey Box)
- Use real-world scenario (factory, hospital, cards, dice)
- NO math symbols yet
- End with: "This is what [formula] calculates"

**Test:** Would a 12-year-old understand the core idea?

### 3.2 The Formula
- Clean LaTeX display
- One formula per concept

### 3.3 Variable Decoder 
For EACH variable:
```
$X$ = **Name** — Plain English explanation
```

**Must answer:**
- What does this measure?
- What are typical values?
- What happens when it changes?

### 3.4 Key Insight (Grey Box)
- The "aha!" moment
- Common misconception to avoid
- The wisdom an experienced student would share

**Quality Gate:**
```
□ 12-year-old could explain the concept
□ Every formula symbol defined
□ No naked formulas without context
```

---

## Phase 4: INTERACTIVE ELEMENT

**Process:**

1. **Identify the core insight** that's hard to grasp from text
2. **Check existing topics** for interaction variety:
   - What types already exist? (sliders, grids, buttons)
   - What scenarios already used? (factory, hospital, cards)
   - AVOID repetition
3. **Design interaction:**
   - Scenario first (grey box)
   - Clear mission/goal
   - Immediate feedback
   - Completion state

**Interaction Types (vary across topics):**
| Type | Best for |
|------|----------|
| Slider | Continuous values, "find the X" |
| Click grid | Discrete selection, combinations |
| Pills/Radio | Category choices |
| Button sequence | Multi-step processes |
| Simulation | Probability convergence |

**Quality Gate:**
```
□ Uses @st.fragment for instant feedback
□ Different from last 3 topics' interactions
□ Scenario is concrete and relatable
□ Clear completion state
```

---

## Phase 5: FRAG DICH (Ask Yourself)

**Purpose:** Self-assessment checkpoint

**Question Types:**
- "Is this situation [X] or [Y]?"
- "What distribution when you see [signal word]?"
- "What does [symbol] represent here?"
- "Why can't we use [alternative]?"

**Requirements:**
- 3-5 questions
- Grey callout styling
- Bilingual

```python
st.markdown(f"### {t({'de': 'Frag dich', 'en': 'Ask Yourself'})}")
with st.container(border=True):
    st.markdown(f"""
<div style="background: #f4f4f5; border-left: 4px solid #a1a1aa; 
            padding: 12px 16px; border-radius: 8px; color: #3f3f46;">
<strong>{t({"de": "Erkennst du...", "en": "Can you recognize..."})}:</strong><br><br>
• Question 1?<br>
• Question 2?<br>
• Question 3?
</div>
""", unsafe_allow_html=True)
```

**Quality Gate:**
```
□ Tests recognition, not recall
□ Would help student on exam
□ Grey styling applied
```

---

## Phase 6: EXAM ESSENTIALS (Merged Trap + Tips)

**Structure:**

### 6.1 The Most Common Trap
- What's the #1 mistake students make?
- What's the rule to avoid it?

### 6.2 Pro Tips (Numbered)
- Shortcuts that save time on exams
- Each with *Why?* explanation
- Insider knowledge an experienced student would share

**Sources for tips:**
- Common errors from graded exams
- Efficiency tricks for calculations
- Pattern recognition shortcuts

```python
st.markdown("### Exam Essentials")
with st.container(border=True):
    st.markdown("**The Most Common Trap**")
    st.markdown("...")
    st.markdown("---")
    st.markdown("**Pro Tip: Exam essentials:**")
    st.markdown("**(1) [Tip]**")
    st.markdown("*Why?* [Explanation]")
```

**Quality Gate:**
```
□ Trap is the REAL #1 mistake (not generic)
□ Tips are CLASS A (would actually help on exam)
□ Grey container, no colored callouts
```

---

## Phase 7: BACKEND INTEGRATION

```python
# In views/course_overview.py
SUBTOPIC_QUESTION_COUNTS = {
    "X.Y": N,  # Number of MCQs in this subtopic
}
```

**MCQ Tracking:**
```python
render_mcq(
    ...,
    course_id="vwl",
    topic_id="X",
    subtopic_id="X.Y",
    question_id="unique_id"
)
```

**Quality Gate:**
```
□ SUBTOPIC_QUESTION_COUNTS updated
□ All MCQs have tracking parameters
□ Question IDs unique
```

---

## Phase 8: FINAL QA

### Browser Testing
```
□ Load the page - no errors in console
□ Side-by-side boxes equal height
□ Interactive element responds correctly
□ MCQ submits and tracks
□ Success/error feedback works
□ Looks good on different window widths
```

### Code Review
```
□ No emojis (except st.button)
□ Grey callouts only (no st.info inside containers)
□ Headers outside containers
□ All content bilingual
□ @st.fragment for interactivity
```

### Cohesion Check
```
□ Theory structure follows pedagogy rules
□ Interactive variety maintained (check Topics 1+2 as reference)
□ Exam Essentials format consistent
□ Layout utilities used where applicable
```

---

## Quick Reference: Mandatory Elements

```
Every subtopic MUST have:
☑️ Theory (Analogy → Formula → Decoder → Insight)
☑️ At least 1 visual or interactive
☑️ Frag Dich section
☑️ Exam Essentials (merged Trap + Tips)
☑️ At least 1 MCQ with tracking
☑️ Registered in SUBTOPIC_QUESTION_COUNTS
```

---

## Time Estimate

| Phase | First Topics | After 5+ Topics |
|-------|--------------|-----------------|
| Theory extraction | 15 min | 8 min |
| Exam question audit | 10 min | 5 min |
| Theory section | 20 min | 10 min |
| Interactive element | 25 min | 12 min |
| Frag Dich | 5 min | 3 min |
| Exam Essentials | 10 min | 5 min |
| Backend + QA | 10 min | 5 min |
| **TOTAL** | **~95 min** | **~48 min** |

With adaptive learning, expect ~20 min by Topic 10.