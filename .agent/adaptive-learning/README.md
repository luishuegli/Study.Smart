# Adaptive Learning: User Guide

## Quick Commands

| When | Say This | What Happens |
|------|----------|--------------|
| Start new topic | `@[/implement] section 6.3` | Agent reads all rules + starts implementation |
| Refresh rules mid-session | `@[/rules]` | Agent re-reads all rule files |
| Mid-work fix | Just say "fix this" or "change that" | Agent logs fix automatically |
| After topic done | "Topic X complete, synthesize" | Agent reviews logs → proposes rules |
| Before next topic | "Integrate pending rules" | Agent adds approved rules to rule files |

---

## The Workflow

### 1. Starting a New Section (Fresh Chat)

```
You: @[/implement] section 6.3
```

Agent automatically:
1. Reads `pedagogy.md`, `synthesis.md`, `topic_[previous].md`
2. Checks pending rules to apply
3. Starts implementation with all context

### 2. During Implementation (Automatic)

When you say things like:
- "fix this"
- "that's wrong"
- "not stupid-person-proof"
- "change the layout"

Agent automatically logs to `adaptive-learning/topic_[X].md`:
```markdown
### Fix 1: Missing header argument
- **What was wrong:** render_ask_yourself() called without header
- **What I changed:** Added header parameter
- **Pattern:** Required-Parameter-Check
- **Files:** topic_3_2_content.py
```

**You don't need to ask for logging — it happens automatically.**

### 3. After Topic Complete (Optional)

```
You: Topic 6 complete, synthesize
```

Agent:
1. Reads `adaptive-learning/topic_6.md` 
2. Counts fixes by category
3. Identifies patterns (2+ same issue = rule candidate)
4. Proposes new rules

### 4. Before Next Topic

```
You: Integrate pending rules
```

Agent:
1. Reads `synthesis.md` for pending rules
2. Adds them to `pedagogy.md`, `design-system.md`, etc.
3. Marks as "✅ Integrated" in synthesis

---

## File Structure

```
.agent/
├── workflows/
│   └── implement.md          # Main workflow (use /implement)
├── rules/
│   ├── pedagogy.md           # Teaching rules
│   ├── design-system.md      # Colors, spacing, callouts
│   ├── layout.md             # Container patterns, CSS
│   └── templates.md          # Copy-paste code
└── adaptive-learning/
    ├── synthesis.md          # Pending rules, cross-topic patterns
    ├── topic_1.md            # Fix logs for Topic 1
    ├── topic_2.md            # Fix logs for Topic 2
    └── ...
```

---

## The Compounding Effect

```
Topic 1:  15 fixes → lots of learning
Topic 3:   8 fixes → patterns emerging  
Topic 5:   3 fixes → rules stabilizing
Topic 10:  0-1 fixes → near-perfect implementation
```

Each fix becomes a rule. Rules prevent future mistakes. By Topic 10, agents implement sections with minimal corrections.

---

## Tips

1. **Always start fresh chat** for new implementations (full context)
2. **Be specific** when pointing out issues ("header missing" vs "fix this")
3. **Let fixes accumulate** — synthesis works better with more data
4. **Review synthesis.md** periodically to approve pending rules
