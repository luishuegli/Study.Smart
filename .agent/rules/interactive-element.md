---
trigger: always_on
---

---
description: Core principles for all interactive learning elements
---

# Interactive Element Principles

## 1. Purpose-Driven Interaction
- Every interactive element must have a **clear learning purpose**
- The user should understand **what they're trying to discover**
- Completion should be **recognizable** (a goal state exists)

## 2. Narrative Arc
- **Setup**: State the challenge or question
- **Exploration**: User manipulates controls to discover the answer
- **Payoff**: Reward completion with feedback and insight

## 3. Semantic Consistency
- **Colors in visuals should match colors in formulas**
- If a variable appears in both math and chart, use the same color
- Standard semantic mapping: Red = target/selection, Blue = universe/pool

## 4. Feedback Loop
- User actions must produce **immediate visual feedback**
- Progress toward the goal should be **visible**
- Success states deserve **celebration** (balloons, success message)

## 5. Progress Tracking
- Completed missions should be **tracked** for sidebar progress
- Use `st.session_state` to remember completion state

### 6. The "Scenario First" Rule (Mission Context)
- **Every mission MUST start with a real-world scenario** that explains WHY finding this value matters.
- The scenario should be:
  - **Concrete**: "A quality engineer needs to know..." NOT "You might want to find..."
  - **Relatable**: Hospital, factory, sales - things students can picture
  - **Question-based**: End with the business question the math will answer
- **Format**: Blue callout box with `Scenario:` label, placed BEFORE the mission goal
- **Style**: `rgba(0, 122, 255, 0.08)` background, `#007AFF` left border
- **Example**: "A company wants to award bonuses to the top 5% of salespeople. They need to know: What sales value (X) marks the threshold?"

## 7. Reference
See [topic_1_7_content.py](cci:7://file:///Users/luis/Downloads/Study.Smart/topics/topic_1_7_content.py:0:0-0:0) for implementation example.