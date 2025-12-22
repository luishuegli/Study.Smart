# Content Creation Guide & Design System

## Quick Start Checklist

When creating a new topic, follow this checklist:

- [ ] Create topic file: `topics/topic_X_Y_content.py`
- [ ] Define content dictionary with bilingual strings
- [ ] Add MCQ questions with tracking parameters
- [ ] Update `SUBTOPIC_QUESTION_COUNTS` in `course_overview.py`
- [ ] Use standard spacing and container patterns
- [ ] Test progress tracking

---

## Design System Rules

### 1. Spacing Standards

```python
# Between major sections
st.markdown("<br><br>", unsafe_allow_html=True)

# Between subsections  
st.markdown("<br>", unsafe_allow_html=True)

# Standard section divider
st.markdown("---")
```

**When to use:**
- `<br><br>` - Between theory and interactive sections, before exam workbench
- `<br>` - Between cards/elements within a section
- `---` - After header, between major content blocks

### 2. Container Patterns

```python
# Main content capsule (theory + interactive)
with st.container(border=True):
    # Content here
    pass

# Exam/quiz section
with st.container(border=True):
    render_mcq(...)
```

**Rules:**
- Always use `border=True` for visual consistency
- Theory sections go in bordered containers
- Each MCQ should be in its own bordered container
- Interactive visualizations can be inside or outside containers depending on layout

### 3. Column Layouts

```python
# Theory + Visualization (standard split)
col_theory, col_vis = st.columns([1, 1.6], gap="medium")

# Question + Button
col_content, col_button = st.columns([3, 1])
```

**Standard ratios:**
- Theory/Viz: `[1, 1.6]` - gives more space to interactive elements
- Content/Button: `[3, 1]` - standard for topic cards
- Equal split: `[1, 1]` - for balanced content

### 4. Header Hierarchy

```python
# Topic title (H1)
st.header(t(content["title"]))

# Section headers (H3)
st.markdown(f"### {t(content['section_header'])}")

# Subsection (bold)
st.markdown(f"**{t(content['subsection'])}**")

# Captions
st.caption(t(content['description']))
```

---

## Content Dictionary Template

```python
content_X_Y = {
    "title": {"de": "X.Y Deutscher Titel", "en": "X.Y English Title"},
    
    "theory_header": {"de": "Definitionen", "en": "Definitions"},
    
    "intro": {
        "de": "Deutsche Einleitung...",
        "en": "English introduction..."
    },
    
    "definitions": {
        "concept_1": {
            "title_de": "Konzept 1",
            "title_en": "Concept 1",
            "text_de": "Erklärung...",
            "text_en": "Explanation...",
            "formula": r"P(A) = \frac{x}{y}"  # LaTeX
        }
    },
    
    "exam": {
        "title": {"de": "Übung", "en": "Exercise"},
        "source": "Source citation",
        "question": {
            "de": "Frage?",
            "en": "Question?"
        },
        "options": [
            {"id": "a", "de": "Option A", "en": "Option A"},
            {"id": "b", "de": "Option B", "en": "Option B"}
        ],
        "correct_id": "a",
        "solution": {
            "de": "**Richtig! (a)**<br>Erklärung...",
            "en": "**Correct (a)**<br>Explanation..."
        }
    }
}
```

---

## MCQ Implementation Pattern

```python
# 1. Prepare options
opts = content["exam"]["options"]
opt_labels = [t({"de": o["de"], "en": o["en"]}) for o in opts]

# 2. Find correct index
correct_id = content["exam"]["correct_id"]
correct_idx = next((i for i, o in enumerate(opts) if o["id"] == correct_id), 0)

# 3. Render with tracking
with st.container(border=True):
    render_mcq(
        key_suffix="X_Y_unique_id",
        question_text=t(content["exam"]["question"]),
        options=opt_labels,
        correct_idx=correct_idx,
        solution_text_dict=content["exam"]["solution"],
        success_msg_dict={"de": "Korrekt", "en": "Correct"},
        error_msg_dict={"de": "Falsch", "en": "Incorrect"},
        model=model,
        ai_context="Context: Brief description for AI",
        allow_retry=False,
        # TRACKING PARAMETERS (REQUIRED)
        course_id="vwl",
        topic_id="X",
        subtopic_id="X.Y",
        question_id="unique_question_id"
    )
```

**Question ID naming convention:**
- Single question: `"X_Y_exam"` or `"q_X_Y_concept"`
- Multiple questions: `"X_Y_A"`, `"X_Y_B"`, `"X_Y_C"`
- Descriptive: `"q_1_1_stetig"` (describes what it tests)

---

## Progress Tracking Setup

### Step 1: Add to `course_overview.py`

```python
SUBTOPIC_QUESTION_COUNTS = {
    "1.1": 1,
    "1.2": 3,
    "X.Y": 2,  # ADD YOUR NEW SUBTOPIC
}
```

### Step 2: Use consistent IDs

All `question_id` values in your `render_mcq()` calls must be:
- Unique across the entire course
- Consistent (don't change them later)
- Descriptive enough to identify the question

---

## Standard Render Function Template

```python
def render_subtopic_X_Y(model):
    # --- HEADER ---
    st.header(t(content_X_Y["title"]))
    st.markdown("---")

    # --- THEORY SECTION ---
    with st.container(border=True):
        st.markdown(f"### {t(content_X_Y['theory_header'])}")
        st.markdown(t(content_X_Y["intro"]))
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Theory content here
        # Use columns if needed for theory + visualization
        
    # --- EXAM WORKBENCH ---
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown(f"### {t(content_X_Y['exam']['title'])}")
    st.caption(content_X_Y['exam']['source'])
    
    with st.container(border=True):
        # MCQ implementation here
        pass
```

---

## Reusable Components

### Theory Cards (Stacked)

```python
for concept_key in ["concept_1", "concept_2"]:
    c = content["definitions"][concept_key]
    
    with st.container(border=True):
        st.markdown(f"**{t({'de': c['title_de'], 'en': c['title_en']})}**")
        st.caption(t({'de': c['subtitle_de'], 'en': c['subtitle_en']}))
        st.markdown(t({'de': c['text_de'], 'en': c['text_en']}))
        st.latex(c["formula"])
```

### Tab-based Questions

```python
# Apply green indicators
tab_css = render_tab_progress_css(["A", "B", "C"], "X_Y")
st.markdown(tab_css, unsafe_allow_html=True)

tab_a, tab_b, tab_c = st.tabs(["Question A", "Question B", "Question C"])

with tab_a:
    render_mcq(..., question_id="X_Y_A")
with tab_b:
    render_mcq(..., question_id="X_Y_B")
with tab_c:
    render_mcq(..., question_id="X_Y_C")
```

---

## CSS Utilities

### Remove Header Top Margin

```python
st.markdown("""
    <style>
    h3 { margin-top: 0 !important; padding-top: 0 !important; }
    </style>
""", unsafe_allow_html=True)
```

Use this when aligning headers with bordered containers in columns.

---

## Localization Best Practices

```python
# ✅ GOOD - Separate keys for complex content
"intro": {
    "de": "Deutscher Text...",
    "en": "English text..."
}

# ✅ GOOD - Inline for simple labels
st.button(t({"de": "Klicken", "en": "Click"}))

# ❌ AVOID - Hardcoded strings
st.markdown("This is not translated")

# ✅ GOOD - LaTeX doesn't need translation
"formula": r"P(A) = \frac{1}{6}"
```

---

## File Organization

```
topics/
├── topic_1_content.py       # Subtopic 1.1
├── topic_1_2_content.py     # Subtopic 1.2
├── topic_1_3_content.py     # Subtopic 1.3
├── topic_1_4_content.py     # Subtopic 1.4
└── topic_2_content.py       # New topic
```

**Naming convention:**
- Main topic: `topic_X_content.py` (covers subtopic X.1)
- Additional subtopics: `topic_X_Y_content.py`

---

## Common Patterns Summary

| Element | Code |
|---------|------|
| Section spacing | `st.markdown("<br><br>", unsafe_allow_html=True)` |
| Divider | `st.markdown("---")` |
| Theory container | `with st.container(border=True):` |
| Theory/Viz columns | `st.columns([1, 1.6], gap="medium")` |
| MCQ container | `with st.container(border=True):` |
| Success message | `{"de": "Korrekt", "en": "Correct"}` |
| Error message | `{"de": "Falsch", "en": "Incorrect"}` |

---

## Quick Copy-Paste Templates

### Minimal Topic File

```python
import streamlit as st
from utils.localization import t
from utils.quiz_helper import render_mcq

content_X_Y = {
    "title": {"de": "X.Y Titel", "en": "X.Y Title"},
    # Add content here
}

def render_subtopic_X_Y(model):
    st.header(t(content_X_Y["title"]))
    st.markdown("---")
    
    # Your content here
```

### Single MCQ Question

```python
with st.container(border=True):
    render_mcq(
        key_suffix="X_Y_exam",
        question_text=t({"de": "Frage?", "en": "Question?"}),
        options=["A", "B", "C"],
        correct_idx=0,
        solution_text_dict={"de": "Lösung", "en": "Solution"},
        success_msg_dict={"de": "Korrekt", "en": "Correct"},
        error_msg_dict={"de": "Falsch", "en": "Incorrect"},
        model=model,
        ai_context="Context here",
        course_id="vwl",
        topic_id="X",
        subtopic_id="X.Y",
        question_id="X_Y_exam"
    )
```

---

## Efficiency Tips

1. **Copy existing topic files** as templates - they already have the right structure
2. **Reuse column ratios** - stick to `[1, 1.6]` for theory/viz
3. **Standard spacing** - use the patterns above consistently
4. **Question IDs** - use descriptive names like `"q_2_1_binomial"` instead of generic `"q1"`
5. **Update progress tracking** - don't forget `SUBTOPIC_QUESTION_COUNTS`!

---

## Checklist Before Committing

- [ ] All strings are bilingual (de/en)
- [ ] MCQ questions have tracking parameters
- [ ] Question IDs are unique and descriptive
- [ ] Updated `SUBTOPIC_QUESTION_COUNTS`
- [ ] Containers have `border=True`
- [ ] Standard spacing used (`<br><br>`, `---`)
- [ ] Tested in browser
