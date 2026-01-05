# Topic 8 Adaptive Learning Notes

## Topic 8.1: Intuitive Heuristic Approaches for Estimators

### Fixes Applied

#### 1. LaTeX in HTML Divs - DOES NOT WORK
**Issue**: Using `$...$` syntax in HTML `<div>` elements does not render LaTeX.
**Fix**: Use `st.latex()` instead, or put math inside `st.container(border=True)`.
```python
# WRONG - LaTeX won't render
st.markdown(f"<div>$\\hat{{\\mu}} = ...$</div>", unsafe_allow_html=True)

# CORRECT - Use st.latex()
st.latex(r"\hat{\mu} = ...")
```

#### 2. Intuition Box Should Be White, Not Grey
**Issue**: User expected "Intuition" section to use white container with border, not grey callout.
**Fix**: Use `st.container(border=True)` for Intuition sections:
```python
st.markdown("### Intuition")
with st.container(border=True):
    st.markdown(t(content["intuition"]), unsafe_allow_html=True)
```

#### 3. Vertical Centering in Side-by-Side Columns
**Issue**: Symbol (θ̂) not vertically centered with adjacent content.
**Fix**: Use explicit top/bottom padding to push content down:
```python
<div style="padding: 100px 0 40px 0;">  # More top than bottom
```

#### 4. Interactive Should Show Chart from Start
**Issue**: Chart only appeared after 3 rounds, felt arbitrary.
**Fix**: Always show empty chart with fixed axes, add data as rounds are played:
```python
fig = go.Figure()
if len(history) >= 1:
    # Add traces
fig.update_layout(xaxis=dict(range=[0, 20]), yaxis=dict(range=[0, 15]))
st.plotly_chart(fig)  # Always show, even if empty
```

#### 5. Interactive Should Show Full Calculation
**Issue**: Results felt "arbitrary" - didn't show X₁, X₂ values used.
**Fix**: Track last round and show calculation breakdown:
```python
st.session_state.sd_last = {"x1": x1, "x2": x2, "a": est_a, "b": est_b, ...}
# Then show:
st.latex(fr"\frac{{{x1:.1f} + {x2:.1f}}}{{2}} = {est_a:.1f}")
```

#### 6. Dynamic Chart Axes
**Issue**: Fixed x-axis range `[0, 20]` cut off data when user played 300+ rounds.
**Fix**: Make axes dynamic, with minimum for empty chart:
```python
xaxis=dict(range=[0, max(20, len(history) + 5)])  # Expands with data
```

#### 6. Relatable Scenario
**Issue**: Abstract "μ = 50" not intuitive for students.
**Fix**: Use relatable scenario - "pizza delivery time" with friends guessing.

#### 7. Intuitive Explanation of WHY
**Issue**: "A wins 55%" doesn't explain why.
**Fix**: Add explanation: "If you weight one friend more, you're taking a risk - what if that friend is wrong?"

### New Rules Identified

1. **INTUITION_WHITE_CONTAINER**: Intuition sections use `st.container(border=True)`, not grey callouts
2. **INTERACTIVE_EMPTY_CHART**: Show empty chart from start, add data as interaction happens
3. **INTERACTIVE_SHOW_CALCULATION**: Show actual values and calculation breakdown, not just results
4. **RELATABLE_SCENARIOS**: Use everyday examples (pizza delivery, friends guessing)
5. **EXPLAIN_THE_WHY**: Success messages should explain WHY, not just state the result

### Components Used
- `inject_equal_height_css()` - Side-by-side containers
- `render_worked_example()` - Student heights example
- `render_ask_yourself()` - Frag Dich section
- `render_exam_essentials()` - Trap + Tips
- `render_mcq()` - Exam practice
- `@st.fragment` - Interactive isolation
- `go.Figure()` with `st.plotly_chart()` - Running average chart
