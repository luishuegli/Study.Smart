# VWL-Brilliant Course Configuration - Notation Bible

# General Notation
LATEX_EXPECTED_VALUE = r"E[X]"
LATEX_VARIANCE = r"V(X)"
LATEX_STD_DEV = r"\sigma_X"
LATEX_PROBABILITY = r"P(A)"

# Descriptive Statistics (Slides 302-303)
LATEX_QUARTILE_1 = r"Q_1"
LATEX_QUARTILE_2 = r"Q_2"
LATEX_QUARTILE_3 = r"Q_3"
LATEX_IQR = r"IQA"  # Interquartilsabstand
LATEX_MEDIAN = r"Q_2"

# Discrete Distributions (Slides 187-194)
# Binomial distribution mass function: f_Bi(x; p, n)
LATEX_BINOMIAL_MASS = r"f_{Bi}(x; p, n)"
LATEX_BINOMIAL_FORMULA = r"\binom{n}{x} \cdot p^x \cdot (1-p)^{n-x}"
LATEX_PARAM_N = r"n"
LATEX_PARAM_P = r"p"

# Continuous Distributions (Slide 210)
# Normal distribution density: f_N(x; mu, sigma^2)
LATEX_NORMAL_DENSITY = r"f_N(x; \mu, \sigma^2)"
LATEX_NORMAL_FORMULA = r"\frac{1}{\sqrt{2\pi\sigma^2}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}"
LATEX_PARAM_MU = r"\mu"
LATEX_PARAM_SIGMA2 = r"\sigma^2"

# Hypothesis Testing (Slide 390)
LATEX_NULL_HYPOTHESIS = r"H_0"
LATEX_ALT_HYPOTHESIS = r"H_1"
LATEX_ALPHA = r"\alpha"
LATEX_BETA = r"\beta"
LATEX_SIGNIFICANCE_LEVEL = r"\alpha"
LATEX_POWER_FUNCTION = r"G(\mu)"  # Gütefunktion

# Conceptual Explanations for Beginners
NOTATION_EXPLANATIONS = {
    LATEX_EXPECTED_VALUE: "The 'theoretical average' of a random variable.",
    LATEX_VARIANCE: "Measures the squared deviation from the mean – how 'spread out' the values are.",
    LATEX_STD_DEV: "The average distance from the mean, in the original units of the data.",
    LATEX_QUARTILE_1: "The 25% mark: 25% of the data is below this value.",
    LATEX_QUARTILE_2: "The Median: The exact middle of the dataset (50% mark).",
    LATEX_QUARTILE_3: "The 75% mark: 75% of the data is below this value.",
    LATEX_IQR: "The range of the middle 50% of the data. High IQR means high uncertainty.",
    LATEX_BINOMIAL_MASS: "Calculates the probability of getting exactly 'x' successes in 'n' trials.",
    LATEX_NORMAL_DENSITY: "The 'Bell Curve' – models naturally occurring phenomena like heights or errors.",
    LATEX_PARAM_N: "The number of trials or observations.",
    LATEX_PARAM_P: "The probability of success in a single trial.",
    LATEX_PARAM_MU: "The center of the bell curve (the mean).",
    LATEX_PARAM_SIGMA2: "How wide or narrow the bell curve is (the variance).",
    LATEX_NULL_HYPOTHESIS: "The 'status quo' or the default assumption we try to challenge.",
    LATEX_ALT_HYPOTHESIS: "The alternative we suspect might be true.",
}

# Style & Formatting
ST_THEME_COLOR = "#6366f1"
