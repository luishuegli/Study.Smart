---
description: Implementation Rules
---

# Permanent Implementation Rules (Study.Smart)

This document contains **MUST-FOLLOW** rules for all agentic work. These rules are the "Constitution" of the project—ensuring pedagogical brilliance, visual unity, and technical stability.

---

## 1. Iconography & Visuals
- **1.1 Strict Iconography**: **No Emojis** (🚫 🎯 ✅). Use the project's `render_icon(name, color)` helper or Streamlit's native `icon`.
    - *Fallback*: If a specific shape is needed and no icon exists, render a simple SVG using `st.markdown`.
- **1.2 SVG Reliability Protocol**: When rendering custom SVGs via `st.markdown`, you MUST follow this XML standard to prevent rendering failures:
    - `xmlns="http://www.w3.org/2000/svg"` is mandatory.
    - Define a strict `viewBox` (e.g., `viewBox="0 0 24 24"`).
    - Set explicit `width` and `height` in pixels (e.g., `width="24px"`).
    - Use `fill="currentColor"` so icons respect dark/light mode automatically.
- **1.3 Strategic Color**: Use color for **Data Logic**, not decoration.
    - *Rule*: If $P(A)$ is red in the formula, the circle $A$ in the diagram MUST be red.
- **1.4 Language Duality**: Visuals must respect `st.session_state.lang`. NEVER show two languages at once.
- **1.5 Rendering Integrity**:
    - **HTML Safety**: Always use `unsafe_allow_html=True` with `st.markdown`.
    - **No HTML in Components**: `st.slider` and `st.button` labels cannot parse HTML. Use a preceding `st.markdown` label with `label_visibility="collapsed"` on the widget to style it.
    - **LaTeX Safety**: Never nest LaTeX (`$..$`) inside HTML tags within markdown. Use CSS classes on the `div` for styling instead.

---

## 2. Layout & Spacing (The Dashboard Standard)
- **2.1 Equal Height Boxes (The CSS Protocol)**: Side-by-side bordered containers must ALWAYS stretch to equal height. You must inject this exact CSS:
    ```css
    [data-testid="stHorizontalBlock"] { align-items: stretch !important; }
    [data-testid="column"] { display: flex !important; flex-direction: column !important; }
    /* Ensure internal wrappers expand */
    [data-testid="column"] > div { flex: 1 !important; }
    ```
- **2.2 Anti-Overlap & Collision Protocol**:
    - **No Squeezing**: If content risks overlapping (e.g., long labels in 3+ columns), you MUST switch to a **Vertical Layout** or reduce column count. **Better to scroll down than to squint.**
    - **Forced Wrapping**: Apply `white-space: normal !important` to any custom text label inside narrow columns to force line breaks.
    - **Minimum Widths**: Interactive charts must never be placed in columns narrower than `0.4` ratio unless they are simple sparklines.
- **2.3 Bordered Major Parts**: Wrap Theory Cards, Missions, and Workbenches in `st.container(border=True)`.
- **2.4 Hint Placement**: Hints (`st.expander`) must go **AFTER/BELOW** the question text.
- **2.5 Spacing System (Aggressive Whitespace)**:
    - Section Break: `st.markdown("<br><br>", unsafe_allow_html=True)`
    - Element Break: `st.markdown("<br>", unsafe_allow_html=True)`
    - Divider: `st.markdown("---")`
- **2.6 Plotly Geometry Lock**: Any geometric visualization (Venn, Scatter) MUST use `scaleanchor="y"` and `scaleratio=1` in the layout config. This prevents circles from becoming ovals when the window resizes.

---

## 3. Mathematical Notation (LaTeX)
- **3.1 Total LaTeX Policy**: ALL formulas and variables (even simple $x, y$) must be LaTeX.
- **3.2 Typography Consistency**:
    - **Complex**: Use full-line `$$...$$` for fractions, sums, limits.
    - **Simple**: Do NOT wrap entire sentences in LaTeX. Keep words in Markdown (Inter font); only vars in LaTeX.
- **3.3 No Breaking Symbols**: Never break a term like $P(A|B)$ across lines.
    - **Arrow Protocol**: For steps ($A \to B$), place the arrow and result on a **new line** (use `\n\n` or separate `st.latex` calls) to prevent horizontal scroll/overflow.
- **3.4 Contextual Text**: Text inside formulas ("if", "then") must be wrapped in `\text{}`.

---

## 4. Interaction & Live Notation
- **4.1 Direct Manipulation**: No sliders for binary/categorical choices. Use **Pills**, **Toggles**, or **Click-Select**.
- **4.2 Bi-Directional Sync**:
    - **Rule**: Math is the *output* of interaction.
    - **Implementation**: If a user drags a slider ($N=50$), the formula symbol ($P(B)$) must update **instantly**.
- **4.3 The HUD Principle**: Dynamic KPIs go at the **TOP**, flanking the visual.
- **4.4 No Dead Clicks**: If a chart isn't interactive, set `clickmode='none'` to prevent confusing hover effects.

---

## 5. Pedagogy (The "Teacher" Protocol)
- **5.1 The "Intuition First" Rule**: Never present a formula in isolation. Always start with a "Toy Model" (interactive analogy) before the Math.
- **5.2 The "Decoder Ring" Sequence**:
    1. **Anchor**: State the Goal ($P(A \cap B)$).
    2. **Experiment**: Play with the Visual (No math symbols, just shapes).
    3. **Intuition**: Feel the pattern (e.g., "Overlap is double counting").
    4. **Relate**: Label it in plain English ("Mac + iPhone Users").
    5. **Connection**: Show the Formula.
- **5.3 The "Rule of 10"**: Manual counting tasks must use **N ≤ 10** items. Do not test patience.
- **5.4 "Pro Trick"**: Every topic needs a `st.info("Pro Tip")` box containing an exam shortcut/hack.
- **5.5 Concrete-First**: Use natural language labels ("Red Marbles") *before* abstract notation ($A \subset B$).

---

## 6. Progress & Backend
- **6.1 Registry**: New topics MUST be registered in `views/course_overview.py` under `SUBTOPIC_QUESTION_COUNTS`.
- **6.2 Full Cycle Implementation**: Every lesson file must:
    1. **Load**: `progress = get_user_progress()`
    2. **Track**: `track_question_answer(subtopic_id, question_id, is_correct)`
    3. **Update**: `st.session_state["user_progress"] = progress` (Force UI refresh)
- **6.3 Defensive State Initialization**: NEVER access `st.session_state["key"]` directly.
    - *Bad*: `score = st.session_state["score"]` (Crashes on first run).
    - *Good*: `score = st.session_state.get("score", 0)`.

---

## 7. The "Apple" Aesthetic (Form IS Function)
- **7.1 The "Breathing Room" Mandate**: Dense UIs are forbidden. Use aggressive whitespace.
- **7.2 Toolbars over Sidebars**: Controls for a specific chart should be integrated directly above/below that chart (like a toolbar), not floating in a distant sidebar.
- **7.3 Micro-Interactions**: Every action needs feedback.
    - *Bad*: Clicking "Submit" and nothing changes.
    - *Good*: Clicking "Submit" -> Show Success Message -> Update Progress Bar -> Unlock Next Section.
- **7.4 Visual Hierarchy**:
    - **Primary Action**: Solid Color Button (`type="primary"`).
    - **Secondary Action**: Outlined/Ghost Button (`type="secondary"`).
    - **Tertiary**: Text Link.

---

## 8. Development Workflow
- **8.1 Plan First**: Update `implementation_plan.md` before coding.
- **8.2 Lego Block (No Global CSS)**: Global CSS (`<style>`) targeting generic tags (`div`, `p`) is **FORBIDDEN**. Use native Streamlit layouts (`columns`, `containers`).
- **8.3 The "Surgical" Exception**: CSS is allowed ONLY if scoped to a specific widget ID or class.
- **8.4 Atomic Functions (No Monoliths)**: No single function should exceed **50 lines**. Extract logic to `utils/`. View files should only handle display.
- **8.5 Widget Identity**: If you encounter "Duplicate Widget ID" errors, you MUST immediately assign a unique `key=uuid.uuid4()` to the component.
- **8.6 Final Verification**: Before committing, verify:
    1. **SVGs render** (check `viewBox`).
    2. **Layouts stretch** (check CSS).
    3. **Math aligns** (check LaTeX).
    4. **No Overlap** (check narrow widths).