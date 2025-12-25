# Permanent Implementation Rules (Study.Smart)

This document contains MUST-FOLLOW rules for all agentic work on the Study.Smart project. These rules ensure pedagogical quality, visual consistency, and technical integrity.

---

## 1. Iconography & Visuals
- **Strict Iconography Rule**: Do not use Emojis. Wherever an icon is needed (e.g., inside the Legend or Control labels), use the project's `render_icon(name, color)` helper or Streamlit's native `icon` parameter. If a specific shape (Circle/Square) is needed and no icon exists, render a simple SVG shape using `st.markdown`.
- **Strategic Color Use**: Use colors to aid intuition, not just for decoration.
    - *Example (Topic 1.5)*: Using specific colors to identify which circle in a Venn diagram corresponds to which data point.
- **Visual Legends**: Include a clear legend for complex diagrams (multi-colored, multi-shaped) if it helps student comprehension. Labels should be bilingual.
- **Language Duality**: Graphics and interactive elements MUST respect the current language mode (`st.session_state.lang`). NEVER display two languages simultaneously in a diagram if a toggle is available.
- **Rendering Integrity**:
    - **Always use `unsafe_allow_html=True`** in `st.markdown` whenever `render_icon` or HTML tags are involved.
    - **No HTML in Component Labels**: Streamlit components (like `st.slider`, `st.button`) do not support HTML in their labels. If a label requires styling (e.g., `nowrap`), use a preceding `st.markdown` with `unsafe_allow_html=True` and set `label_visibility="collapsed"` on the component.
    - **LaTeX Stability**: Avoid nesting LaTeX (e.g., `$P(A)$`) inside HTML tags (like `<div>`) within `st.markdown`, as it often fails to parse. Instead, use a CSS class on the `div` to apply styles (like `nowrap`) while keeping the LaTeX as raw markdown.
    - **Markdown Bold Stability**: Markdown bold (`**text**`) MUST NOT wrap multi-line blocks with nested newlines or double-newlines. Streamlit's markdown parser often fails to render these as bold and displays literal stars instead. Always bold lines or paragraphs individually.

---

## 2. Layout & Spacing
- **Equal Height Boxes**: Side-by-side bordered containers (`st.container(border=True)`) must ALWAYS have equal height (stretched). This requires a specific CSS protocol:
    1. Set `align-items: stretch !important` on `[data-testid="stHorizontalBlock"]`.
    2. Set `display: flex !important` and `flex-direction: column !important` on `[data-testid="column"]`.
    3. Ensure all internal wrappers (`stVerticalBlock`, `stVerticalBlockBorderWrapper`, `stLayoutWrapper`) have `flex: 1 !important`.
    4. Set `justify-content: space-between !important` (or `flex-start` with spacers) on the inner div of the bordered wrapper to distribute content.
- **Bordered Major Parts**: Wrap all major UI sections (Theory Cards, Interactive Missions, Exam Workbenches) in `st.container(border=True)` to create a clean, modern "dashboard" look.
- **No Text Overlap**: Avoid using `white-space: nowrap` on long labels within narrow containers (e.g., small columns). This causes text to bleed out and overlap. Prioritize wrapping or shortening the label.
- **Hint Placement**: Optional hints (expanders) MUST always be placed AFTER/BELOW the question text, never before. This ensures the student reads the problem first.
- **LaTeX Typography Consistency**: 
    - **Mandatory Full-Line LaTeX**: Use only for lines containing **complex notation** (fractions, square roots, summation, limits) to ensure perfect vertical alignment and font consistency.
    - **Forbidden Full-Line LaTeX**: Do NOT wrap entire sentences in LaTeX if they only contain simple variables (e.g., $A, B$) and natural language. Keep the text in standard markdown (Inter font).
    - **"No Numbers" Heuristic**: If a sentence contains no numeric values (0-9) or complex operators, it should almost always remain in standard markdown.
- **HUD Metric Consistency**: Use standard CSS classes (like `.nowrap-label`) ONLY for very short metrics (e.g., $P(A)$) that are guaranteed to fit.
- **Consistent Spacing**:
    - Between major sections: `st.markdown("<br><br>", unsafe_allow_html=True)`
    - Between elements: `st.markdown("<br>", unsafe_allow_html=True)`
    - Major dividers: `st.markdown("---")`
    - Distances must be uniform across the entire site.
- **Interactive Representation (Visuals)**: For custom interactive visuals (charts, legends, simulations), rigid margin rules do NOT apply. Priority is **Nice Placement** and **Conflict Avoidance**. Visuals should "float" naturally without overlapping borders or neighboring elements, but do not need to adhere to standard text spacing grids if it harms the aesthetic.
- **Natural Layout Principle (Apple-Like)**: Interactive layouts should prioritize **Natural Flow** and **Whitespace** over rigid grids/columns. Controls should act as "Toolbars" integrated with the visual (e.g., centered pills above/below a chart), rather than being isolated in sidebars. Avoid "Box-in-Box" layouts; let elements breathe.

---

## 3. Mathematical Notation (LaTeX)
- **Total LaTeX Policy**: EVERY formula and mathematical expression must be in LaTeX format.
- **No Breaking Symbols**: Mathematical notation and symbols (e.g., $(\Omega)$ or $P(A|B)$) MUST NOT be broken across lines. 
    - **Smart Arrow Wrapping**: For long examples involving transitions (e.g., "If $A=\{...\} \rightarrow B=\{...\}$"), always place the arrow and the result on a **new line** to avoid horizontal overflow. **Implementation**: Use a double newline (`\n\n`) or separate strings for different `st.markdown`/`st.latex` calls to ensure the line break is respected by the renderer.
    - **Cramming Avoidance**: Use newlines (`\n`) or separate `st.latex` blocks instead of cramming multiple definitions into a single line.
- **Contextual Text**: Supporting text for formulas (e.g., "wenn S={...}", "dann", "für alle") must also be included inside the LaTeX block or consistently formatted to match.
    - *Example*: `st.latex(r"\text{Sei } A = \{1, 2, 3\}")` instead of "Sei A = {1, 2, 3}".
    - *Example*: `st.latex(r"\text{Sei } A = \{1, 2, 3\}")` instead of "Sei A = {1, 2, 3}".

---

## 4. The Principle of Direct Manipulation & Live Notation
- **No Arbitrary Abstractions**: Direct Manipulation is King. Never use a slider (0-100) to represent a binary or categorical state change (like removing a group). Use Toggles, Pills (`st.pills`), or Click-Select to mimic the physical action of "discarding" or "selecting".
- **True Direct Interaction**: The Graphic *IS* the Interface. When possible, users should interact directly with the visualization (e.g., clicking data points to filter them).
- **The Apple Layout Principle (Unity of Control & Content)**:
    - **Don't Stack; Integrate**: Interactive visuals must follow a HUD (Heads Up Display) hierarchy, not a blog post format.
    - **Metrics First**: Place dynamic KPIs (Key Performance Indicators) at the TOP, flanking the central visual or formula.
    - **Live Color Mapping**: If a visual element is Red, its corresponding number in the formula must be `\color{red}{Number}`.
    - **No Dead Interaction**: Disable chart clicking (`clickmode='none'`) if it provides no pedagogical value or causes lag/ghosting. Offload control to tactile inputs like Pills.
- **Action-to-Notation Coupling**: Mathematical notation is not a static label; it is a dynamic output. When the user changes the physical state (e.g., filters data), the mathematical symbol must update **instantly** to reflect that change (e.g., $\Omega \to B$).

---

## 5. Progress Tracking & Backend
- **Mandatory Registration**: Every new topic and subtopic MUST be registered in `views/course_overview.py` under `SUBTOPIC_QUESTION_COUNTS`.
- **Full Backend Integration**: Every lesson implementation must include:
    1. Loading `user_progress` via `get_user_progress`.
    2. Tracking every question submission via `track_question_answer`.
    3. Updating the local `st.session_state["user_progress"]` for immediate UI feedback.
- **Progress Hierarchy**:
    - **Subtopic (Sidebar)**: Show an SVG checkmark icon if all questions/missions are complete. Otherwise, show progress fraction (e.g., `(1/3)`).
    - **Topic Overview**: Aggregate subtopic percentages into a topic-level progress bar.
    - **Course Overview**: Aggregate topic-level progress into a total course completion percentage.

---

## 5. Pedagogy & UX
- **Intentional Design**: Every theory card and interactive element must be designed to make complex concepts intuitive and "fun."
- **MCQ Standard**: Always use `utils/quiz_helper.py` (`render_mcq`) for multiple-choice questions to ensure layout consistency.
- **Intuition Over Repetition (The "Rule of 10")**: Interactive elements requiring manual user input (like counting items) must be kept strictly minimal (N ≤ 10). The goal is to spark intuition, not test patience. If a concept can be proven with 5 items, do not use 50. Large datasets should be automated; small datasets should be manual.
- **The Decoder Ring Protocol**: Interactive elements must follow a 5-step pedagogical sequence:
    1. *The Anchor (The Math)*: Start with the formal goal/question (e.g., "Calculate $P(A|B)$"). This validates student anxiety and sets the destination.
    2. *Experiment (The Toy)*: Interaction with a visual system without math symbols (e.g., "Filter Shapes").
    3. *Intuition (The Feeling)*: Create a visceral sense of the concept (e.g., fading shapes = "shrinking world").
    4. *Relate (The Concept)*: Connect actions to plain-English (e.g., "How many circles are left?" vs "Denominator").
    5. *Connection (The Reveal)*: Map the discoveries back to the notation in Step 1 (e.g., "The $P(B)$ is your count of circles").
    - **The "Intuitive Transition" Loop**: The flow must playfully transition a student from:
        1. **Experimenting** (Touching the toy) -> 
        2. **Understanding** (Seeing the pattern) -> 
        3. **Relating** (Connecting to words) -> 
        4. **Notation** (Seeing the math).
    - **Framing as a Problem**: Interactive elements should always be framed as a specific problem the user needs to solve (e.g., "Find the Code"), rather than just an open sandbox. Guidance is mandatory.
- **Concrete-First Visuals**: Use natural language in legends and labels first. 
    - *Required*: "Red Circles", "Target Area", "Total Population". 
    - *Forbidden*: Abstract terms like "Group $A \cap B$" or "Subset $X$" before the concept is Relat-ed.
- **Live Notation Mandate**: Formulas in interactives must be Dynamic UI Components.
    - Static LaTeX is banned in interactive sections.
    - *Bi-Directional Sync*: If a slider changes (e.g., $N=30$), the formula symbol ($P(B)$) must update with the number or highlight in sync. Math is the *output* of the simulation, not the instruction.
- **Dual Language**: All text (including labels, buttons, and error messages) MUST be bilingual using the `t()` helper. Do not forget to translate mathematical connecting words ("if", "then").

---

## 6. Development Workflow
- **Plan First**: Always update the `implementation_plan.md` before making changes.
- **Small Commits**: Commit changes logically with descriptive messages.
- **Rule Verification**: Before finishing ANY task, explicitly verify that all permanent rules (Iconography, Layout, LaTeX, Progress) have been followed.
- **Checklist**: Always run through the "Checklist Before Committing" in `design_system.md`.

---

## 7. The "Lego Block" Mandate (Zero Global CSS)
- **Strict Prohibition**: You are FORBIDDEN from writing global CSS blocks (e.g., style tag at the top of the file) that target generic classes like `[data-testid="column"]` or `div`. 
    - *Reason*: This breaks the entire app's layout.
- **Native Layouts Only**: You must achieve 100% of the layout using Native Streamlit Containers:
    - Use `st.columns()` for horizontal alignment.
    - Use `st.container(border=True)` for grouping.
    - Use `st.expander()` for hiding details.
- **The "Surgical" Exception**: You may use CSS only if targeting a specific widget via a scoped selector (like centering `st.pills`), and it must be strictly scoped.
- **Accept Imperfection**: If native Streamlit cannot do it (e.g., "move this button 3px up"), DO NOT DO IT. Change the design instead. It is better to have a clean, standard layout than a broken custom one.
