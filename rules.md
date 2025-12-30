# Project Rules (Study.Smart)

## 1. Bilingual Content Mandate
- **All** user-facing text must be bilingual dictionaries `{"de": "...", "en": "..."}`.
- **Critical**: This explicitly includes **MCQ Options**.
    - **Forbidden**: `options = ["Option A", "Option B"]`
    - **Required**: `options = [{"de": "Option A", "en": "Option A"}, ...]`
- Failure to use dictionary structure for options results in the UI failing to switch languages for answers.

## 2. Iconography & Visuals
- **No Emojis**: Use SVG icons or `render_icon`.
- **SVG Integrity**: Ensure `viewBox`, `width`, `height`, and `fill="currentColor"`.

## 3. Mathematical Typesetting
- Use LaTeX for all variables and formulas.
- Fractions within options must use LaTeX (e.g., `1/2` -> `\frac{1}{2}` or clean text `1/2`, but not integer artifacts like `21`).

## 4. Code Standards
- **No Global CSS**: Use scoped rendering.
- **Equal Height Columns**: Use the CSS injection trick for side-by-side containers.
