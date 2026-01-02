---
trigger: always_on
---

description: Missions, scenarios, and feedback [CREATIVE with structure]
Interactive Elements
The Goal
Every interactive element should produce an "aha!" moment. The student discovers the concept through doing, not reading.

[STRICT] Mandatory Structure
Every interactive element MUST have:

Scenario — Real-world context (grey callout)
Goal — What the student is trying to find
Interaction — Controls to manipulate
Feedback — Immediate visual response
Completion — Recognizable success state
[STRICT] Scenario First Pattern
Before showing the mission goal, provide context:

st.markdown(f"""
<div style="background: #f4f4f5; border-left: 4px solid #a1a1aa; 
            padding: 12px 16px; border-radius: 8px; color: #3f3f46;">
<strong>{t({"de": "Szenario", "en": "Scenario"})}:</strong><br>
{t({"de": "[Konkretes deutsches Szenario]", 
    "en": "[Concrete English scenario]"})}
</div>
""", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
st.markdown(f"**{t({'de': 'Mission', 'en': 'Mission'})}:** [What to find]")
Scenario requirements:

Concrete: "A quality engineer needs to know..."
Relatable: Factory, hospital, sales
Question-based: End with the business question
[STRICT] Fragment Isolation
ALL interactive components use @st.fragment:

@st.fragment
def mission_component():
    # State initialization
    if "state_key" not in st.session_state:
        st.session_state.state_key = default
    
    # Interaction logic
    
    if success_condition:
        st.success("Mission Complete!")
        st.rerun(scope="fragment")
mission_component()
Benefits:

Only fragment reruns, not whole page
Faster interaction
No scroll jumping
[STRICT] Feedback Requirements
Immediate: Every action produces visible change
Progress visible: How close to goal?
Success celebrated: st.success() + optional st.balloons()
[CREATIVE] Interaction Types
You may use ANY of these (variety encouraged):

Type	When to use	Example
Slider	Continuous values	Find λ where P(X=0)=0.05
Click grid	Discrete selection	Pick 3 cards from deck
Pills/Radio	Category choice	"With replacement?"
Button sequence	Multi-step	Monty Hall doors
Drag (limited)	Ordering	Arrange events
[CREATIVE] Completion Patterns
Single-answer mission:

if abs(user_value - target) < tolerance:
    st.success("Found it!")
    st.session_state.mission_complete = True
Exploration mission (no single answer):

if games_played >= 5:
    st.success("You've discovered the pattern!")
Simulation unlock (Earned-Sim pattern):

if manual_games >= 2:
    if st.button("Simulate 1000 Games"):
        # Run simulation
[STRICT] Semantic Consistency
Colors in visuals MUST match formulas:

If $P(A)$ is red in math, circle A is red in diagram
If slider controls λ, λ in formula updates
[STRICT] No Dead Clicks
Non-interactive charts:

fig.update_layout(clickmode='none', hovermode=False)
[STRICT] Control Placement
[Controls: sliders, buttons, pills]
        ↓
[Visualization: chart, grid, diagram]
        ↓
[Result: dynamic formula, feedback]
[CREATIVE] Scenario Bank
Good scenarios by distribution:

Distribution	Scenario
Poisson	Calls per hour, defects per batch
Binomial	Pass/fail tests, coin flips
Normal	Heights, test scores, sales
Bayes	Medical tests, spam filters
Rules for scenarios:

One scenario per concept
Consistent throughout the section
Concrete, not abstract
Cohesion vs Variety
SAME everywhere (cohesion):

Scenario-first pattern
Grey callout styling
Fragment isolation
Feedback on every action
Control → Visual → Result flow
DIFFERENT per topic (variety):

Specific scenario content
Interaction type (slider vs click vs pills)
Completion condition
Number of steps