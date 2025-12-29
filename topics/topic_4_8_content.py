# Topic 4.8: Hypergeometric Distribution
import streamlit as st
from utils.localization import t
from utils.quiz_helper import render_mcq
from data.exam_questions import get_question

def render_subtopic_4_8(model):
    """4.8 Hypergeometrische Verteilung"""
    
    st.header(t({"de": "4.8 Hypergeometrische Verteilung", "en": "4.8 Hypergeometric Distribution"}))
    st.markdown("---")
    
    # --- THEORY SECTION ---
    with st.container(border=True):
        st.markdown(f"### {t({'de': 'Theorie', 'en': 'Theory'})}")
        
        st.markdown(t({
            "de": """**Wann verwenden?** Ziehen **ohne Zurücklegen** aus einer endlichen Population.

**Parameter:**
- $N$ = Populationsgrösse
- $M$ = Anzahl "Erfolge" in der Population
- $n$ = Stichprobengrösse

**Wahrscheinlichkeitsfunktion:**""",
            "en": """**When to use?** Drawing **without replacement** from a finite population.

**Parameters:**
- $N$ = Population size
- $M$ = Number of "successes" in population
- $n$ = Sample size

**Probability mass function:**"""
        }))
        
        st.latex(r"P(X = k) = \frac{\binom{M}{k} \cdot \binom{N-M}{n-k}}{\binom{N}{n}}")
        
        st.info(t({
            "de": "**Pro Tip:** Die hypergeometrische Verteilung nähert sich der Binomialverteilung, wenn $N$ sehr gross ist (Faustregel: $n/N < 0.1$).",
            "en": "**Pro Tip:** The hypergeometric distribution approaches the binomial when $N$ is very large (rule of thumb: $n/N < 0.1$)."
        }))
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- EXAM SECTION ---
    st.markdown(f"### {t({'de': 'Prüfungstraining', 'en': 'Exam Practice'})}")
    
    q1 = get_question("4.8", "hypergeom_10_5_3")
    if q1:
        with st.container(border=True):
            st.caption(q1.get("source", ""))
            opts = q1.get("options", [])
            if opts and isinstance(opts[0], dict):
                option_labels = [t(o) for o in opts]
            else:
                option_labels = opts
            
            render_mcq(
                key_suffix="4_8_hypergeom",
                question_text=t(q1["question"]),
                options=option_labels,
                correct_idx=q1["correct_idx"],
                solution_text_dict=q1["solution"],
                success_msg_dict={"de": "Korrekt!", "en": "Correct!"},
                error_msg_dict={"de": "Nicht ganz.", "en": "Not quite."},
                client=model,
                ai_context="Hypergeometric distribution calculation",
                course_id="vwl",
                topic_id="4",
                subtopic_id="4.8",
                question_id="4_8_hypergeom"
            )
