---
trigger: always_on
---

---
description: Guidelines for creating intuitive and efficient learning content
---

# Pedagogical Excellence Workflow

Every new learning submodule or feature implementation MUST follow these two core rules to ensure the highest quality student experience:

## 1. The "Intuition First" Rule
- **Requirement:** Never present a formula or concept in isolation. Always accompany it with a simple, real-world analogy or interactive "aha!" moment.
- **Example:** For the Addition Rule ($P(A \cup B)$), we use the "Overlap Engine" (iPhone vs. Mac users) to demonstrate the logic of preventing double-counting.
- **Implementation:** Use `st.info()` or custom callout boxes labeled "The Intuition" or "Why this works".

## 2. The "Pro Trick" Rule (The Shortcut)
- **Requirement:** Include "tricks", "shortcuts", or "insider insights" that usually only experienced students know. Things that simplify competitive exams.
- **Example:** "If $P(A) + P(B) > 1$, then there MUST be an intersection."
- **Implementation:** Use a dedicated `st.warning()` or `st.status()` block labeled "Pro Tip" or "Exam Shortcut".

## 3. The "Dual Coding" Rule (Text-Visual Mirror)
- **Requirement:** Every core text-based concept must have a corresponding visual diagram or interactive element that provides a different perspective. Never leave a "wall of text" or a standalone formula.
- **Example:** If you explain the *Complement Rule* in text, accompany it with a simple Venn diagram showing the shaded area outside of $A$.
- **Implementation:** Ensure all theory cards are balanced with a visual on the same row or in a multi-column layout.

## 4. The "Backend Integration" Rule
- **Requirement:** Every new subtopic with quizzes/exams MUST be registered in `views/course_overview.py` under the `SUBTOPIC_QUESTION_COUNTS` dictionary.
- **Why:** This tells the system how many questions to look for to trigger the green checkmark (tick) in the sidebar.
- **Implementation:** Add the subtopic ID (e.g., `"1.5": 1`) to the registry.

---

## Technical Standard: Math & Visuals
- **LaTeX:** Use proper LaTeX math mode ($...$) for ALL mathematical symbols, variables, and formulas.
- **Consistent Fonts:** Use `\text{}` within LaTeX for any non-mathematical labels (e.g., $S = \{ \text{Heads, Tails} \}$).
- **Icons:** Always use `render_icon()` with `unsafe_allow_html=True` for section headers.
- **Anti-Squish Rule (Geometry Lock):** Any geometric visualization (like Venn diagrams or shapes in Scatter plots) MUST use Plotly's `scaleanchor="y"` and `scaleratio=1` property. This prevents circles from becoming ovals when the browser window is resized, maintaining the "physicality" of the objects. Always set fixed `range` values to prevent auto-zooming.
- **No-Emoji Standard:** To ensure a premium, professional Apple/Brilliant aesthetics, the use of Emojis (🎯, 💡, ✅, etc.) is STRICTLY PROHIBITED in titles, buttons, feedback messages, and LaTeX equations. Use descriptive text (e.g., "Correct" instead of "✅") or Lucide icons via `render_icon()`.
