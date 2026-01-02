---
trigger: always_on
---

description: Copy-paste code skeletons - fill in, don't recreate
Code Templates
Rule: Copy these skeletons exactly. Only change the [PLACEHOLDER] values.

1. Topic File Structure
import streamlit as st
from utils.localization import t
from utils.quiz_helper import render_mcq
content_[X]_[Y] = {
    "title": {"de": "[Deutscher Titel]", "en": "[English Title]"},
    # Content dictionaries here
}
def render_subtopic_[X]_[Y](model):
    st.header(t(content_[X]_[Y]["title"]))
    st.markdown("---")
    
    # --- THEORY ---
    # See Theory Section template below
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- FRAG DICH ---
    # See Frag Dich template below
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- EXAM ESSENTIALS ---
    # See Exam Essentials template below
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- MCQ ---
    # See MCQ template below
2. Theory Section (The 12-Year-Old Structure)
st.markdown(f"### {t({'de': 'Theorie', 'en': 'Theory'})}")
with st.container(border=True):
    # Step 1: Simple Analogy (Grey Box)
    st.markdown(f"""
<div style="background: #f4f4f5; border-left: 4px solid #a1a1aa; 
            padding: 12px 16px; border-radius: 8px; color: #3f3f46;">
<strong>{t({"de": "Die Kernidee", "en": "The Core Idea"})}:</strong><br>
{t({"de": "[Einfache deutsche Analogie]", "en": "[Simple English analogy]"})}
</div>
""", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Step 2: The Formula
    st.latex(r"[FORMULA HERE]")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Step 3: Variable Decoder (Grey Box)
    st.markdown(f"""
<div style="background: #f4f4f5; border-left: 4px solid #a1a1aa; 
            padding: 12px 16px; border-radius: 8px; color: #3f3f46;">
<strong>{t({"de": "Variablen-Decoder", "en": "Variable Decoder"})}:</strong><br>
$X$ = <strong>[Name]</strong> — [Plain explanation]<br>
$Y$ = <strong>[Name]</strong> — [Plain explanation]
</div>
""", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Step 4: Key Insight (Grey Box)
    st.markdown(f"""
<div style="background: #f4f4f5; border-left: 4px solid #a1a1aa; 
            padding: 12px 16px; border-radius: 8px; color: #3f3f46;">
<strong>{t({"de": "Aha-Moment", "en": "Key Insight"})}:</strong><br>
{t({"de": "[Deutscher Insight]", "en": "[English insight]"})}
</div>
""", unsafe_allow_html=True)
3. Frag Dich (Ask Yourself) Pattern
st.markdown(f"### {t({'de': 'Frag dich', 'en': 'Ask Yourself'})}")
with st.container(border=True):
    st.markdown(f"""
<div style="background: #f4f4f5; border-left: 4px solid #a1a1aa; 
            padding: 12px 16px; border-radius: 8px; color: #3f3f46;">
<strong>{t({"de": "Erkennst du...", "en": "Can you recognize..."})}:</strong><br><br>
• {t({"de": "[Frage 1 auf Deutsch]?", "en": "[Question 1]?"})}<br>
• {t({"de": "[Frage 2 auf Deutsch]?", "en": "[Question 2]?"})}<br>
• {t({"de": "[Frage 3 auf Deutsch]?", "en": "[Question 3]?"})}
</div>
""", unsafe_allow_html=True)
4. Exam Essentials (Merged Trap + Tips)
st.markdown(f"### {t({'de': 'Prüfungs-Essentials', 'en': 'Exam Essentials'})}")
with st.container(border=True):
    # Part 1: The Trap
    st.markdown(f"**{t({'de': 'Die häufigste Falle', 'en': 'The Most Common Trap'})}**")
    st.markdown(f"""
{t({"de": "<strong>[Falle]:</strong> [Beschreibung]<br><br><strong>Regel:</strong> [Regel]", 
    "en": "<strong>[Trap]:</strong> [Description]<br><br><strong>Rule:</strong> [Rule]"})}
""", unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Part 2: Pro Tips
    st.markdown(f"**Pro Tip: {t({'de': 'Prüfungs-Essentials', 'en': 'Exam Essentials'})}:**")
    
    tips = [
        {"tip": {"de": "[Tipp 1]", "en": "[Tip 1]"}, "why": {"de": "[Warum]", "en": "[Why]"}},
        {"tip": {"de": "[Tipp 2]", "en": "[Tip 2]"}, "why": {"de": "[Warum]", "en": "[Why]"}},
    ]
    
    for i, tip_data in enumerate(tips, 1):
        st.markdown(f"**({i}) {t(tip_data['tip'])}**")
        st.markdown(f"*{t({'de': 'Warum', 'en': 'Why'})}?* {t(tip_data['why'])}")
        st.markdown("<br>", unsafe_allow_html=True)
5. MCQ Pattern
opts = [
    {"id": "a", "de": "[Option A Deutsch]", "en": "[Option A English]"},
    {"id": "b", "de": "[Option B Deutsch]", "en": "[Option B English]"},
    {"id": "c", "de": "[Option C Deutsch]", "en": "[Option C English]"},
]
opt_labels = [t({"de": o["de"], "en": o["en"]}) for o in opts]
correct_id = "a"  # Change this
correct_idx = next((i for i, o in enumerate(opts) if o["id"] == correct_id), 0)
st.markdown(f"### {t({'de': 'Übung', 'en': 'Exercise'})}")
st.caption("[Source: HS24 Aufgabe X]")
with st.container(border=True):
    render_mcq(
        key_suffix="[X]_[Y]_exam",
        question_text=t({"de": "[Frage]?", "en": "[Question]?"}),
        options=opt_labels,
        correct_idx=correct_idx,
        solution_text_dict={
            "de": "<strong>Richtig ist ([correct_id])</strong><br>[Erklärung]",
            "en": "<strong>Correct is ([correct_id])</strong><br>[Explanation]"
        },
        success_msg_dict={"de": "Korrekt", "en": "Correct"},
        error_msg_dict={"de": "Falsch", "en": "Incorrect"},
        model=model,
        ai_context="[Context for AI tutor]",
        course_id="vwl",
        topic_id="[X]",
        subtopic_id="[X].[Y]",
        question_id="[X]_[Y]_exam"
    )
6. Grey Callout (Generic)
st.markdown(f"""
<div style="background: #f4f4f5; border-left: 4px solid #a1a1aa; 
            padding: 12px 16px; border-radius: 8px; color: #3f3f46;">
<strong>[Label]:</strong><br>
[Content]
</div>
""", unsafe_allow_html=True)
7. Fragment (For Interactivity)
@st.fragment
def [component_name]():
    if "[state_key]" not in st.session_state:
        st.session_state["[state_key]"] = [default_value]
    
    # Your interactive logic here
    
    if st.button("[Button Text]", key="[unique_key]"):
        st.session_state["[state_key]"] = [new_value]
        st.rerun(scope="fragment")
[component_name]()
8. Equal Height CSS (Inject Once Per Page)
st.markdown("""
<style>
[data-testid="stHorizontalBlock"] { align-items: stretch !important; }
[data-testid="column"], [data-testid="stColumn"] { display: flex !important; flex-direction: column !important; }
[data-testid="column"] > div, [data-testid="stColumn"] > div { flex: 1 !important; display: flex !important; flex-direction: column !important; height: 100% !important; }
div[data-testid="stVerticalBlock"], div[data-testid="stVerticalBlockBorderWrapper"] { flex: 1 !important; display: flex !important; flex-direction: column !important; }
</style>
""", unsafe_allow_html=True)