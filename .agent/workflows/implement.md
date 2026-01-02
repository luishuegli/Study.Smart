---
description: Complete workflow for implementing a new topic/subtopic
trigger: /implement or "implement topic X.Y"
---

# Topic Implementation Workflow

> **Spirit:** This is Brilliant.org meets Apple. Every screen should make a student think "this is actually fun to learn from."

---

## Pre-Flight Checks (Before Starting)

```
□ Read @rules.md for mandatory elements
□ Read @adaptive-learning/synthesis.md for pending rules
□ Identify gold standard: Which existing topic is most similar?
□ Create adaptive-learning/topic_[X].md to log fixes
□ Open browser preview for real-time testing
```

---

## Adaptive Learning Integration

### BEFORE Implementation
1. Read `@adaptive-learning/synthesis.md` for pending rules
2. Check if similar topics had frequent fixes → apply those patterns proactively
3. Create `adaptive-learning/topic_[X].md` using template

### DURING Implementation (Real-Time Logging)
Every time the user requests a fix:
```markdown
### Fix [N]: [Title]
- **Phase:** [Which phase: Theory/Interactive/etc.]
- **What was wrong:** [Issue]
- **What I changed:** [Fix]
- **Pattern:** [Potential rule if repeats]
```

**Log triggers:**
- User says "change this", "fix this", "make it X instead"
- User rejects a design choice
- User provides styling feedback
- User corrects content/wording

### AFTER Implementation (Synthesis)
When user says "Topic complete":
1. Count fixes by phase
2. Identify patterns (3+ = rule)
3. Propose additions to rule files

### The Compounding Effect

```
Topic 1: 15 fixes → lots of learning
Topic 3: 8 fixes → patterns emerging  
Topic 5: 3 fixes → rules stabilizing
Topic 10: 0-1 fixes → near-perfect implementation
```

### Integration Points Per Phase

| Phase | What to log |
|-------|-------------|
| Theory | Formula formatting, decoder style, analogy quality |
| Exam Audit | Question selection criteria, solution format |
| Interactive | Interaction type preferences, scenario styles |
| Frag Dich | Question phrasing, styling |
| Exam Essentials | Trap format, tip numbering |
| QA | Layout issues, CSS problems |

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

### 3.3 Variable Decoder (Grey Box)
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
□ Theory structure matches Topic 4.3 (gold standard)
□ Interactive variety maintained (not repetitive)
□ Exam Essentials format consistent
```

---

## Post-Implementation: Synthesis Workflow

### Step 1: User Triggers Synthesis
```
User: "Topic X complete, synthesize"
```

### Step 2: Agent Reviews Fix Log
Read `adaptive-learning/topic_[X].md` and count:
```
Phase             | Fix Count
------------------|----------
Theory            | ?
Interactive       | ?
Exam Questions    | ?
Styling/Layout    | ?
```

### Step 3: Apply Graduation Logic

| Frequency | Action |
|-----------|--------|
| 1 fix | Note only (don't generalize) |
| 2 fixes same issue | Flag as potential pattern |
| 3+ fixes same issue | **MUST become a rule** |
| Cross-topic repeat | **CRITICAL rule** → add to main rules.md |

### Step 4: Propose New Rules
For each graduated pattern, write:
```markdown
**Proposed Rule:**
- Text: "[Exact rule wording]"
- Add to: [design-system.md / pedagogy.md / etc.]
- Evidence: Fixes #X, #Y, #Z from Topic N
```

### Step 5: Update Synthesis File
Add to `adaptive-learning/synthesis.md`:
```markdown
## Topic [X] Synthesis
- **Date:** [Date]
- **Total fixes:** [N]
- **New rules proposed:** [List]
- **Key learnings:** [Summary]
```

### Step 6: Integration Before Next Topic
Before starting Topic X+1:
1. Read synthesis.md for pending rules
2. Add approved rules to rule files
3. Mark as "✅ Integrated" in synthesis.md

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
