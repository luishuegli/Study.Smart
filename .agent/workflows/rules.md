---
description: Force agent to re-read all rules and context files
---

# Re-Read All Rules

> Use this workflow when the agent seems to have forgotten rules or needs context refresh.

// turbo-all
```
Step 1: view_file .agent/rules/pedagogy.md
Step 2: view_file .agent/rules/design-system.md
Step 3: view_file .agent/rules/layout.md
Step 4: view_file .agent/rules/templates.md
Step 5: view_file .agent/adaptive-learning/synthesis.md
```

---

## After Reading, I MUST Confirm:

### Core Rules (Always Apply)
```
✓ Theory structure: Analogy → Formula → Decoder → Insight
✓ Colors: Blue=#007AFF, Red=#FF4B4B, Purple=#9B59B6, Gray=#6B7280
✓ Spacing: <br> between elements, <br><br> between sections
✓ Grey callouts only (no st.info inside containers)
✓ Headers OUTSIDE containers
✓ Variable Decoder format: $X$ = **Name** — explanation
✓ Key Insight: *The key: [aha moment]*
```

### Pending Rules from synthesis.md (MUST List Each One)
After reading synthesis.md, I will list EVERY pending rule and mark if it applies:

```
Pending Rules I Found:
1. [Rule name] — ✅ Applies / ❌ N/A for this task
2. [Rule name] — ✅ Applies / ❌ N/A for this task
3. [Rule name] — ✅ Applies / ❌ N/A for this task
... (list all)
```

Example:
```
Pending Rules I Found:
1. Intuition OUTSIDE container — ✅ Applies (has theory section)
2. Max 2 columns for formulas — ❌ N/A (no formula grid)
3. No backslash in f-strings — ✅ Applies (using translated text)
4. No inline trap sections — ✅ Applies (using render_exam_essentials())
5. Grey callouts only — ✅ Applies (has callouts)
```

### Mandatory Utilities (Must Use)
```
✓ render_ask_yourself() for Frag Dich
✓ render_exam_essentials() for Exam Essentials  
✓ render_mcq() for MCQs
✓ inject_equal_height_css() if side-by-side
```

---

## If I Don't Confirm All of the Above:

Remind me with: **"Did you actually read the rules? List the pending rules."**
