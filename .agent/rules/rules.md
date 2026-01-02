---
trigger: always_on
---

Study.Smart Implementation Rules
The Spirit
This is Brilliant.org meets Apple. Premium, not academic. Every screen should make a student think "this is actually fun to learn from." If it looks like a textbook, you've failed.

Gold Standard References
When implementing, study these files as reference:

Theory structure: topic_4_3_content.py (Poisson) — Analogy, Formula, Decoder, Insight
Interactive mission: 
topic_1_7_content.py
 — Scenario, Goal, Feedback, Completion
MCQ with tabs: 
topic_1_4_content.py
 — Tab progress, bilingual options
Exam Essentials: topic_4_5_content.py — Merged Trap + Tips pattern
Mandatory Elements
Every subtopic MUST have:

☑️ Theory section — Analogy → Formula → Decoder
☑️ At least ONE visual — Chart, diagram, or interactive
☑️ Exam Essentials — Merged Trap + Tips (grey container)
☑️ At least ONE "Frag Dich" — Self-assessment question (grey box)
☑️ At least ONE MCQ — With tracking parameters
MAY have (adds variety):

Interactive mission with completion state
Multiple MCQ tabs
Simulation button (earned after manual play)
Side-by-side comparison visuals
Priority Order
When rules conflict: Pedagogy > Clarity > Aesthetics > Performance

Rule Strictness
[STRICT] — No Creativity Allowed
Color palette (Blue/Red/Gray/Purple)
Spacing values (
,

, ---)
CSS injection (exact code)
Bilingual structure (de/en dictionaries)
MCQ tracking parameters
Container patterns (columns outside, containers inside)
Grey callouts only (no st.info inside containers)
[CREATIVE] — Room for Variety
Analogies and scenarios used
Interactive visualization types
Question phrasing and wording
Order of tips within Exam Essentials
Narrative style of explanations
Sub-Rules (Detailed Documentation)
@design-system.md — Colors, spacing, callouts [STRICT]
@pedagogy.md — Theory, Frag Dich, Exam Essentials [MEDIUM]
@layout.md — Containers, CSS, fragments [STRICT]
@interactive.md — Missions, feedback [CREATIVE]
@templates.md — Copy-paste code skeletons
Adaptive Learning (CRITICAL)
Read @adapt.md before starting any topic.

This system captures every fix you request and turns it into rules:

Phase	When	What
CAPTURE	During implementation	Log fixes to adaptive-learning/topic_X.md
SYNTHESIZE	After topic complete	Identify patterns, propose rules
INTEGRATE	Before next topic	Add new rules to main files
Commands:

"Log this fix" → Add to current topic's adaptive learning file
"Topic X complete, synthesize" → Run synthesis
"Integrate new rules" → Add pending rules to files
The compounding effect:

Topic 1: 15 fixes → Topic 5: 2 fixes → Topic 10: ~20 min implementation
Quick Rules Summary
Visuals
No Emojis (exception: st.button labels)
Semantic colors — Red=selection, Blue=pool
Grey callouts only — #f4f4f5 bg, #a1a1aa border, #3f3f46 text
Layout
Columns outside, containers inside
Headers outside containers
Equal height CSS for side-by-side boxes (see @layout.md)
Content
All LaTeX for math
Bilingual everything — Options MUST be {"de": ..., "en": ...}
Intuition before formula
Backend
Register in SUBTOPIC_QUESTION_COUNTS
Defensive state — st.session_state.get("key", default)