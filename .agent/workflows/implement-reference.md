---
description: Code examples and reference snippets for topic implementation
---

# Implementation Code Reference

> **This file contains code snippets referenced by implement.md**

---

## Required Imports (COPY EXACTLY)

```python
from utils.localization import t
from utils.quiz_helper import render_mcq
from utils.ask_yourself import render_ask_yourself
from utils.exam_essentials import render_exam_essentials
from utils.worked_example import render_worked_example
from views.styles import render_icon, inject_equal_height_css
```

## Layout Utilities

```python
from utils.layouts import (
    render_single_formula,      # Single formula intro
    render_comparison,          # Side-by-side comparison
    render_formula_grid,        # Multi-formula grid (2x2)
    render_steps,               # Step-by-step process
    render_formula_breakdown,   # Deep dive into formula
    render_definition,          # Definition card
    render_decision_tree,       # Decision tree
)
from utils.layouts.foundation import (
    grey_callout, intuition_box, variable_decoder, key_insight
)
```

## Utility Usage Examples

### Ask Yourself
```python
render_ask_yourself(
    header=content["frag_dich"]["header"],  # REQUIRED!
    questions=content["frag_dich"]["questions"],
    conclusion=content["frag_dich"]["conclusion"]
)
```

### Exam Essentials
```python
render_exam_essentials(
    trap=content["exam_essentials"]["trap"],
    trap_rule=content["exam_essentials"]["trap_rule"],
    tips=content["exam_essentials"]["tips"]
)
```

### Worked Example (with Semantic Colors)
```python
# COLOR ROLES: Blue=#007AFF (params), Red=#FF4B4B (target), Green=#16a34a (prob), Purple=#9B59B6 (transformed)
render_worked_example(
    header={"de": "Schritt-für-Schritt", "en": "Step-by-Step"},
    problem={"de": "...", "en": "..."},
    steps=[
        {"label": {"de": "Gegeben", "en": "Given"}, "latex": r"{\color{#007AFF}\lambda = 4}", "note": {"de": "Rate", "en": "Rate"}},
        {"label": {"de": "Formel", "en": "Formula"}, "latex": r"P(X = {\color{#FF4B4B}6}) = ...", "note": None},
    ],
    answer={"de": "...", "en": "..."}
)
```

### MCQ Tracking
```python
render_mcq(
    key_suffix="X_Y_name",
    question_text=t(q["question"]),
    options=option_labels,
    correct_idx=q["correct_idx"],
    solution_text_dict=q["solution"],
    success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
    error_msg_dict={"de": "Falsch.", "en": "Incorrect."},
    client=model,
    ai_context="...",
    course_id="vwl",
    topic_id="X",
    subtopic_id="X.Y",
    question_id="unique_id"
)
```

### Backend Registration
```python
# In views/course_overview.py
SUBTOPIC_QUESTION_COUNTS = {
    "X.Y": N,  # Number of MCQs in this subtopic
}
```

## Frag Dich Manual HTML (if not using utility)
```python
st.markdown(f'''
<div style="background: #f4f4f5; border-left: 4px solid #a1a1aa; 
            padding: 12px 16px; border-radius: 8px; color: #3f3f46;">
<strong>{t({"de": "Erkennst du...", "en": "Can you recognize..."})}:</strong><br><br>
• Question 1?<br>• Question 2?<br>• Question 3?
</div>
''', unsafe_allow_html=True)
```

## Exam Essentials Manual HTML (if not using utility)
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
