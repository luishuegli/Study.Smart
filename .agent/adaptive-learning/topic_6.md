# Topic 6 Adaptive Learning Log

## Topic 6.1: Der zentrale Grenzwertsatz (CLT)
**Date:** 2026-01-03

---

## Fixes Applied (15 Total)

### 1. LaTeX in HTML Doesn't Render
**Problem:** `$S_n \approx N(...)$` inside HTML div showed raw LaTeX  
**Solution:** Use `st.latex()` outside the HTML, not inline  
**Rule:** Never put LaTeX inside HTML divs - use separate st.latex() calls

### 2. German Words in LaTeX Formulas
**Problem:** Hardcoded "und", "oder", "Summe", "Mittelwert" in formulas  
**Solution:** Make formulas bilingual dicts: `{"de": r"...", "en": r"..."}`  
**Rule:** LaTeX formulas with text MUST be bilingual dicts, not raw strings

### 3. Slider Ping-Pong Revert Issue
**Problem:** Slider reverted every second interaction  
**Cause:** Setting both `value=st.session_state.xxx` AND `key="xxx"` creates conflict  
**Solution:** Use `key` only, let Streamlit manage state. Set `value` only for initial default  
**Rule:** Never do `value=session_state.X` + `key="X"` + manual sync simultaneously

### 4. Emoji in Expander (v2 Violation)
**Problem:** Used emoji in expander label  
**Solution:** Remove emoji  
**Rule:** Absolute No Emojis (v2) - even in expanders

### 5. Duplicate Variable Decoder
**Problem:** Symbol explanations shown in 2 places (CLT expander + separate section)  
**Solution:** Consolidate into single expander inside CLT theorem box  
**Rule:** Single source of truth for symbol definitions

### 6. i.i.d. Section Too Abstract
**Problem:** Definition was formal, not intuitive  
**Solution:** ULTRATHINK "Stupid Person Rule" - analogy, conditions, why it matters  
**Rule:** Every definition needs: Analogy → Conditions → Why It Matters

### 7. Steps Without LaTeX
**Problem:** Mathematical terms showed as plain Unicode  
**Solution:** Add `formula` field to steps, render with st.latex()  
**Rule:** All math notation must use LaTeX, even in procedural steps

### 8. Inline Expander for Symbol Decoder
**Pattern:** Put symbol decoder inside theorem box as collapsible expander  
**Rule:** Complex formulas need inline symbol decoder (expander)

### 9. Syntax Error from Replacement
**Problem:** Literal newline character in code replacement  
**Solution:** Fixed the malformed line

### 10. Slider Not Updating Visualization
**Problem:** After fixing ping-pong, visualization used stale session_state values  
**Solution:** Use `n_value` directly from slider return, not session_state  
**Rule:** When using key-only pattern, read widget return value directly

### 11. Symbol/Variable Alignment
**Problem:** In expander, LaTeX symbol and text description were vertically misaligned  
**Solution:** Use inline format: `$X_i$ = **Name** — Description`  
**Rule:** For simple symbol-description pairs, use inline markdown, not columns

### 12. Semantic Color Legend Missing
**Problem:** Histogram color changed (red→purple→green) but meaning wasn't explained  
**Solution:** Added 3-column legend below chart explaining n thresholds  
**Rule:** If color has semantic meaning, MUST have visible legend

### 13. Emojis in Feedback Messages
**Problem:** Emojis in st.warning/info/success messages  
**Solution:** Remove all emojis  
**Rule:** Absolute No Emojis (v2) - includes all st. feedback widgets

### 14. "Symbol" → "Variable" Terminology
**Problem:** Expander said "What does each symbol mean?"  
**Solution:** Changed to "What does each variable mean?"  
**Rule:** Use "variable" for mathematical variables

### 15. LaTeX in Ask Yourself Utility
**Problem:** `$X_i$` showed as literal text in render_ask_yourself  
**Cause:** Utility renders as raw HTML where LaTeX doesn't work  
**Solution:** Use HTML subscript: `X<sub>i</sub>` instead  
**Rule:** In raw HTML contexts, use HTML formatting, not LaTeX

---

## Topic 6.2: De Moivre-Laplace (Continuity Correction)
**Date:** 2026-01-04

---

## Fixes Applied (12 Total)

### 1. HTML Divs Cannot Wrap Streamlit Elements
**Problem:** Opening `<div>` in one st.markdown() and closing `</div>` in another doesn't wrap intermediate elements  
**Cause:** Each st.markdown() is a separate DOM element - HTML doesn't span across  
**Solution:** Use `st.container(border=True)` with CSS override for custom borders  
**Rule:** To wrap Streamlit elements with custom styling, use st.container + CSS, not raw HTML divs

### 2. Ask Yourself Blue Border Pattern
**Problem:** Wanted blue border around Ask Yourself but content fell outside  
**Solution:** Use `st.container(border=True)` then inject scoped CSS to change border color  
**Code Pattern:**
```python
with st.container(border=True):
    st.markdown("**1.** Question with $LaTeX$...")
    # Blue button inside
    st.markdown('<div style="background: #007AFF...">Conclusion</div>', ...)
```

### 3. Bilingual trap_formula
**Problem:** "FALSCH!" showing in English version  
**Solution:** Make trap_formula a bilingual dict  
**Code:** `"trap_formula": {"de": r"...\text{FALSCH!}", "en": r"...\text{WRONG!}"}`  
**Rule:** ANY text in LaTeX formulas must be bilingual

### 4. Colored Slider CSS Pattern
**Problem:** CSS selectors not matching sliders  
**Cause:** Using `label:contains()` which doesn't work; using `label_visibility="collapsed"` hides aria-label  
**Solution:** Use visible labels with descriptive text, target via `[aria-label*="..."]`  
**Code Pattern:**
```css
.stSlider:has([aria-label*="n ="]) div[data-baseweb="slider"] > div:first-child > div:first-child { 
    background-color: #007AFF !important; 
}
.stSlider:has([aria-label*="n ="]) div[role="slider"] { 
    background-color: #FFFFFF !important; 
    border: 2px solid #007AFF !important; 
}
```

### 5. Slider Labels Enable CSS Targeting
**Problem:** `label_visibility="collapsed"` removed aria-label, breaking CSS  
**Solution:** Use visible labels like "n = Sample Size", "p = Probability"  
**Rule:** Slider labels must be visible for CSS semantic coloring to work

### 6. Formula Values Stay Black
**Problem:** Colored formula values (using `\color{red}`) was excessive  
**Solution:** Only sliders are colored; formula values remain black  
**Rule:** Semantic coloring = slider-to-label connection, not slider-to-formula

### 7. Multi-line LaTeX with Aligned Environment
**Problem:** Long formulas cut off in narrow columns  
**Solution:** Use `\begin{aligned}` environment  
**Code:**
```python
"formula": r"\begin{aligned} &P(X \geq 60) \\ &\approx P(...) \\ &= P(Z \geq 2.0) \end{aligned}"
```

### 8. Mnemonic Table Pattern
**Problem:** Verbose explanation of correction direction confusing  
**Solution:** Replace with compact mnemonic table  
**Pattern:** One-liner + simple 2-column table showing the rule

### 9. Exam Tips why_formula
**Problem:** Plain text showing math symbols instead of LaTeX  
**Solution:** Add `why_formula` field to tips that need LaTeX  
**Code:** `"why_formula": r"P(X \geq k) \to k - 0.5 \quad | \quad P(X \leq k) \to k + 0.5"`

### 10. EXACT Formula Full Display
**Problem:** EXACT binomial row was too compact, missing formula  
**Solution:** Add full binomial summation formula  
**Code:** `\sum_{i=k}^{n} \binom{n}{i} p^i (1-p)^{n-i}`

### 11. Remove Unused Color Legends
**Problem:** Color legend for WITHOUT/WITH/EXACT was redundant after removing formula colors  
**Solution:** Remove legend since sliders now have colored labels directly

### 12. UND vs AND in Validity Check
**Problem:** German "UND" showing in English mode  
**Solution:** Use bilingual `t({'de': 'UND', 'en': 'AND'})` in inline math context

---

## Key Patterns (Updated for 6.2)

### st.container + CSS for Custom Borders
```python
# For Ask Yourself blue border
with st.container(border=True):
    st.markdown("**1.** Question with $P(X \geq k)$?")
    st.markdown('<div style="background: #007AFF; ...">Conclusion</div>', ...)
```

### Slider Semantic Coloring (Topic 1.5 Pattern)
```css
/* Track color */
.stSlider:has([aria-label*="n ="]) div[data-baseweb="slider"] > div:first-child > div:first-child { 
    background-color: #007AFF !important; 
}
/* Thumb border */
.stSlider:has([aria-label*="n ="]) div[role="slider"] { 
    background-color: #FFFFFF !important; 
    border: 2px solid #007AFF !important; 
}
```

### Bilingual Formula with Text
```python
"trap_formula": {
    "de": r"Z = \frac{X - np}{\sigma} \quad \text{FALSCH!}",
    "en": r"Z = \frac{X - np}{\sigma} \quad \text{WRONG!}"
}
```

### Multi-line LaTeX (Aligned)
```python
r"\begin{aligned} &P(X \geq 60) \\ &\approx P\left(Z \geq \frac{60-50}{5}\right) \\ &= P(Z \geq 2.0) \end{aligned}"
```
