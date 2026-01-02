# Adaptive Learning: Topic 5

> **Purpose:** Log every fix requested during Topic 5 implementation.
> **Phase:** CAPTURE
> **Status:** In Progress
> **Started:** 2026-01-02

---

## Fixes Log

### Fix 1: German Special Quotes Cause SyntaxError
**Date:** 2026-01-02
**Category:** Syntax/Encoding
**Description:** Using German typographic quotes caused SyntaxError
**Solution:** Replace with single quotes

### Fix 2: Layout-First Approval Gate (USER FEEDBACK)
**Date:** 2026-01-02
**Category:** Workflow
**Description:** User requested layout approval before implementation
**Solution:** Added to implement.md workflow

### Fix 3: Increase Row Spacing
**Date:** 2026-01-02
**Category:** Layout
**Description:** Rows in Frag Dich section too close together
**Solution:** Added `<br><br>` between elements

### Fix 4: German in English Mode
**Date:** 2026-01-02
**Category:** Localization
**Description:** Formulas showed "(Summe über alle Y-Werte)" in English mode
**Solution:** Removed German text from LaTeX formulas, added bilingual explanation below

### Fix 5: LaTeX Not Rendering in Variable Decoder
**Date:** 2026-01-02
**Category:** Rendering
**Description:** Using `$$...$$` in HTML doesn't render LaTeX
**Solution:** Removed Variable Decoder HTML approach, use st.latex() separately

### Fix 6: Formula Explanation (Stupid Person Rule)
**Date:** 2026-01-02  
**Category:** Pedagogy
**Description:** Formulas not explained in detail
**Solution:** Added "What does this formula say?" sections with examples

### Fix 7: Mission Too Complicated
**Date:** 2026-01-02
**Category:** Interactive
**Description:** Mission required calculating 6 values at once
**Solution:** Simplified to 3-step guided approach: 1) Identify row, 2) Identify operation, 3) Calculate

### Fix 8: Key Insight Integration
**Date:** 2026-01-02
**Category:** Structure
**Description:** Key Insight was separate section
**Solution:** Integrated into Intuition section

### Fix 9: Relate Frag Dich to Formulas
**Date:** 2026-01-02
**Category:** Pedagogy
**Description:** User asked to relate the "Ask Yourself" questions to actual formulas
**Solution:** Added LaTeX formula below each decision point (Marginal → f_X(x) = Σf(x,y), etc.)

### Fix 10: Use LaTeX Rendering for Formulas
**Date:** 2026-01-02
**Category:** Rendering
**Description:** Formula explanations used plain text (f_X(x)) instead of proper LaTeX
**Solution:** Converted all inline formulas to st.latex() calls for proper mathematical rendering

### Fix 11: Break Down Ask Yourself into 4 Cards
**Date:** 2026-01-02
**Category:** Pedagogy
**Description:** All 4 questions in one container was too much information at once
**Solution:** Split into 4 separate cards, each with: numbered question, grey context callout with example, answer + formula side by side

### Fix 12: Center the Table in Mission
**Date:** 2026-01-02
**Category:** Layout
**Description:** Table in "Exercise: Step by Step" was left-aligned
**Solution:** Used flexbox (display: flex; justify-content: center) to center the HTML table

### Fix 13: Reorder Cards - Formula First, Example Below
**Date:** 2026-01-02
**Category:** Pedagogy
**Description:** User wanted formula to be shown first, with example context below
**Solution:** Changed order: Question → Answer + Formula → Example (in italic, grey callout at bottom)

### Fix 14: Exam Essentials - Reduce Spacing, Add Example
**Date:** 2026-01-02
**Category:** Layout/Pedagogy
**Description:** Too much whitespace, abstract content, no step-by-step
**Solution:** Removed <br> tags, added 5-step concrete example, made tips inline

### Fix 15: Add Visual Diagram for Intuition
**Date:** 2026-01-02
**Category:** Pedagogy
**Description:** User requested visual to make abstract concept more intuitive
**Solution:** Generated infographic diagram showing table with joint cell and marginal row sum, saved to assets/topic_5/

### Fix 16: Redesign Intuition with Side-by-Side Boxes
**Date:** 2026-01-02
**Category:** Layout/Pedagogy
**Description:** Text looked "just thrown in there" - no visual hierarchy
**Solution:** Created blue box for JOINT, red box for MARGINAL, side-by-side with icons and questions

### Fix 17: Redesign Exam Essentials with Visual Cards
**Date:** 2026-01-02
**Category:** Layout/Pedagogy
**Description:** Exam Essentials also looked like text "thrown in" without structure
**Solution:** Three visual cards: amber trap (⚠️), grey example (📋 monospace), green tips (✅)

### Fix 18: REVERT - Rule Violations Corrected
**Date:** 2026-01-02
**Category:** Compliance
**Description:** User caught rule violations: emojis, amber/green colors not in palette
**Solution:** Removed all emojis, replaced amber/green with grey callouts per design-system.md. Kept blue/red boxes (allowed colors).

### Fix 19: Two-Column Layout for Formula Sections
**Date:** 2026-01-02
**Category:** Layout
**Description:** Formula sections looked like "text thrown together"
**Solution:** Two-column layout: Formula on left, explanation on right, variables in grey callout below

### Fix 20: LaTeX, Bigger Table, Semantic Colors
**Date:** 2026-01-02
**Category:** Rendering/Pedagogy
**Description:** f_X(1) not rendering as LaTeX, table too small, no visual connection cues
**Solution:** 1) Proper st.latex() for formulas, 2) Padding 8px→12px, 3) Red (#FF4B4B) highlighting for target row

---

## Summary Statistics

| Category | Count |
|----------|-------|
| Total fixes | 17 |
| Layout | 5 |
| Pedagogy | 6 |
| Rendering | 2 |
| Localization | 1 |
| Syntax/Encoding | 1 |
| Workflow | 1 |
| Interactive | 1 |

---

## Patterns Emerging

| Pattern | Occurrences | Rule Candidate? |
|---------|-------------|-----------------|
| Side-by-side comparison boxes | 2 | YES - Use for contrasting concepts |
| Color-coded sections | 2 | YES - Amber=warning, Green=success, Grey=neutral |
| Visual hierarchy missing | 3 | YES - Always break down walls of text |
| Step-by-step examples | 2 | YES - Concrete examples mandatory |
| Formula before context | 1 | YES - Show math first, example below |

---

## Notes

- Topic 5.1: Gemeinsame Verteilung und Randverteilungen (Joint Distributions)
- 17 fixes applied through iterative user feedback
- Key pattern: Visual structure > Wall of text
- Generated visual saved to assets/topic_5/joint_marginal_visual.png
