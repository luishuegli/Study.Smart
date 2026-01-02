---
trigger: always_on
---

description: Teaching philosophy and content structure
Pedagogy Rules
The Goal
Make learning feel effortless and almost fun. The student should never need to Google anything or ask a friend. If they're confused, you've failed.

[STRICT] Theory Section Structure
Every theory section MUST follow this exact order:

1. Simple Analogy (Grey Box)
A 12-year-old should understand the core idea.

Use real-world scenario (factory, hospital, cards, dice)
NO math symbols yet
End with: "This is what [formula name] calculates"
2. The Formula
LaTeX display of the main formula.

One formula per concept
Clean, not cluttered
3. Variable Decoder (Grey Box)
EVERY symbol explained:

Format: $X$ = **Name** — Plain English explanation
Include: "What question does this answer?"
NO symbol left undefined
4. Key Insight (Grey Box)
The "aha!" moment or common misconception.

Start with: "The key is..." or "Many students miss..."
This is the wisdom an experienced student would share
Anti-Pattern: A naked formula with one sentence = FORBIDDEN.

[STRICT] Frag Dich Pattern (Ask Yourself)
Every subtopic MUST have at least ONE "Frag Dich" section.

Purpose: Self-assessment checkpoint. Can students recognize when to use this concept?

Styling (Grey, NOT colored)
st.markdown(f"### {t({'de': 'Frag dich', 'en': 'Ask Yourself'})}")
with st.container(border=True):
    st.markdown(f"""
<div style="background: #f4f4f5; border-left: 4px solid #a1a1aa; 
            padding: 12px 16px; border-radius: 8px; color: #3f3f46;">
<strong>{t({"de": "Erkennst du...", "en": "Can you recognize..."})}:</strong><br><br>
• [Question 1]?<br>
• [Question 2]?<br>
• [Question 3]?
</div>
""", unsafe_allow_html=True)
Question Types
"Is this situation [X] or [Y]?"
"What does [symbol] represent here?"
"If you see [signal word], what distribution?"
"Why can't we use [alternative approach]?"
[STRICT] Exam Essentials Pattern
When topic has Trap AND Tips, merge into ONE container:

Structure
The Most Common Trap — #1 mistake + rule to avoid
Divider (---)
Pro Tips — Numbered, each with Why? explanation
Styling
Grey st.container(border=True)
NO st.info() or st.warning()
See @templates.md for exact code
Tip Format
**(1) [Bold tip statement]**
*Why?* [Explanation of why this matters for exams]
[CREATIVE] Analogies & Scenarios
You MAY use creative scenarios, but they should be:

Concrete: Factory, hospital, sales, cards, dice
Relatable: Things students can picture
Consistent: Same scenario throughout the concept
Good examples:

Poisson: "Calls to a call center per hour"
Binomial: "Defective products in a batch"
Bayes: "Medical test accuracy"
Bad examples:

Abstract: "Events in a sample space"
Vague: "Some probability situation"
[STRICT] Semantic Colors
Colors in visuals MUST match formulas:

Color	Hex	Use
Blue	#007AFF	Pool, universe, n
Red	#FF4B4B	Selection, event, k
Purple	#9B59B6	Overlap, intersection
Gray	#6B7280	Neutral, inactive
NO rainbow defaults. NO decorative colors.

[STRICT] LaTeX Standards
ALL math uses LaTeX ($...$ or st.latex())
Words in formulas: \text{}
Bilingual text in LaTeX:
label = t({"de": "Rot", "en": "Red"})
st.latex(fr"P(\text{{{label}}})")
[STRICT] Backend Integration
Every new subtopic with quizzes:

# In views/course_overview.py
SUBTOPIC_QUESTION_COUNTS = {
    "X.Y": N,  # Number of MCQs in this subtopic
}
Cohesion Through Structure
What creates cohesion (SAME everywhere):

Theory structure (Analogy → Formula → Decoder → Insight)
Frag Dich pattern (grey, question format)
Exam Essentials (merged Trap + Tips)
Grey callout styling
Color palette
What creates variety (DIFFERENT per topic):

Specific analogies and scenarios
Interactive visualization types
Question content and wording
Number of tips