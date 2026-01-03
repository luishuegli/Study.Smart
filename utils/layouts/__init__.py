"""
Layout Utilities
================
10+1 reusable theory section layouts.
See layout_system_design.md for full specification.

Usage:
    from utils.layouts import render_single_formula  # Layout A
    from utils.layouts import render_comparison      # Layout B
    from utils.layouts import render_formula_grid    # Layout C
    from utils.layouts import render_steps           # Layout D
    from utils.layouts import render_formula_breakdown  # Layout E
    from utils.layouts import render_definition      # Layout G
    from utils.layouts import render_decision_tree   # Layout H
    from utils.layouts.foundation import grey_callout, variable_decoder, key_insight  # Layout K helpers
"""

# Layout A: Single Formula Introduction
from utils.layouts.single_formula import render_single_formula

# Layout B: Side-by-Side Comparison
from utils.layouts.comparison import render_comparison

# Layout C: Multi-Formula Grid
from utils.layouts.formula_grid import render_formula_grid

# Layout D: Step-by-Step Process
from utils.layouts.steps import render_steps

# Layout E: Formula Breakdown (Deep Dive)
from utils.layouts.formula_breakdown import render_formula_breakdown

# Layout G: Definition Card
from utils.layouts.definition import render_definition

# Layout H: Decision Tree
from utils.layouts.decision_tree import render_decision_tree

# Layout K: Foundation utilities (exported for custom layouts)
from utils.layouts.foundation import (
    grey_callout,
    intuition_box,
    variable_decoder,
    key_insight,
    inject_equal_height_css,
    COLORS,
    STANDARD_BORDER,
    STANDARD_RADIUS
)
