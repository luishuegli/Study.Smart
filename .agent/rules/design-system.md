---
trigger: always_on
---

description: CSS, colors, and styling [STRICT]
Design System
Code templates: See @templates.md for copy-paste skeletons.

Required Imports
from utils.localization import t           # Translation
from utils.quiz_helper import render_mcq   # MCQ component
from views.styles import render_icon       # Icons (NOT emojis)
[STRICT] Color Palette
Color	Hex	Use
Blue	#007AFF	Pool, Set A, n
Red	#FF4B4B	Selection, Event, k
Purple	#9B59B6	Intersection
Gray	#6B7280	Neutral
Callout colors (Zinc):

Element	Hex
Background	#f4f4f5
Border	#a1a1aa
Text	#3f3f46
Rules:

Colors in visuals MUST match formulas
NO rainbow Plotly defaults
NO decorative colors
[STRICT] Spacing
Context	Code
Section break	st.markdown("<br><br>", unsafe_allow_html=True)
Element break	st.markdown("<br>", unsafe_allow_html=True)
Divider	st.markdown("---")
When:

<br><br> — Theory → Interactive, before Exam
<br> — Between cards in section
--- — After page header
[STRICT] Grey Callout
Use for: Variable Decoder, Key Insight, Frag Dich, Notes

st.markdown(f"""
<div style="background: #f4f4f5; border-left: 4px solid #a1a1aa; 
            padding: 12px 16px; border-radius: 8px; color: #3f3f46;">
<strong>[Label]:</strong><br>
[Content]
</div>
""", unsafe_allow_html=True)
NEVER use inside containers:

st.info()
st.warning()
st.success() (except after correct MCQ answer)
st.error() (except after wrong MCQ answer)
[STRICT] Container Layout
Columns OUTSIDE, containers INSIDE:

c1, c2 = st.columns([1, 1.6])
with c1:
    with st.container(border=True):
        # content
with c2:
    with st.container(border=True):
        # content
Headers OUTSIDE containers:

st.markdown("### Section Title")
with st.container(border=True):
    # content
[STRICT] Equal Height CSS
Inject ONCE per page with side-by-side containers:

st.markdown("""
<style>
[data-testid="stHorizontalBlock"] { align-items: stretch !important; }
[data-testid="column"], [data-testid="stColumn"] { display: flex !important; flex-direction: column !important; }
[data-testid="column"] > div, [data-testid="stColumn"] > div { flex: 1 !important; display: flex !important; flex-direction: column !important; height: 100% !important; }
div[data-testid="stVerticalBlock"], div[data-testid="stVerticalBlockBorderWrapper"] { flex: 1 !important; display: flex !important; flex-direction: column !important; }
</style>
""", unsafe_allow_html=True)
[STRICT] No Emojis
Use 
render_icon()
 for icons
Exception: Emojis OK in st.button() labels only
[STRICT] Bilingual Content
Everything uses dictionaries:

"title": {"de": "Deutsch", "en": "English"}
MCQ options MUST be bilingual:

# WRONG
options = ["A", "B", "C"]
# CORRECT
options = [
    {"id": "a", "de": "Option A", "en": "Option A"},
    {"id": "b", "de": "Option B", "en": "Option B"},
]
[STRICT] MCQ Tracking
Every MCQ needs these parameters:

course_id="vwl",
topic_id="X",
subtopic_id="X.Y",
question_id="unique_id"
Register in SUBTOPIC_QUESTION_COUNTS.

Checklist Before Commit
 Bilingual (de/en) everywhere
 MCQ tracking parameters complete
 SUBTOPIC_QUESTION_COUNTS updated
 Equal height CSS (if side-by-side)
 Headers outside containers
 Grey callouts only
 No emojis (except buttons)
 Colors semantic
 Tested in browser