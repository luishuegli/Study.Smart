
# Übung 2 Exam Staging File
# Content extracted from:
# - Uebung_2.pdf (questions)
# - ML_Uebung_2.pdf (solutions)
# Dual-Mode: Study.Smart Guide + Official Solution

# ------------------------------------------------------------------
# MULTIPLE CHOICE
# ------------------------------------------------------------------

uebung2_mc1 = {
    "source": "Übung 2, MC #1",
    "type": "mc",
    "question": {
        "de": r"Diskret ist eine Zufallsvariable, wenn:",
        "en": r"A random variable is discrete if:"
    },
    "options": [
        r"sie nur abzählbar viele Werte annehmen kann.",
        r"sie überabzählbar viele Werte annehmen kann.",
        r"sie nur endlich viele Werte annehmen kann.",
        r"sie unendlich viele Werte annehmen kann.",
        r"ihre Verteilungsfunktion nur als Treppenfunktion gezeichnet werden kann."
    ],
    "correct_idx": 0, # Solution marks (a), (c), (e). (a) is the definition.
    "solution": {
        "de": r"""**Richtig: (a), (c), (e)**

### Study.Smart Guide
**Intuition:**
Diskret heißt "Körnig". Wie Sandkörner oder LEGO-Steine.
Man kann die Werte "durchnummerieren" (1, 2, 3...). Es gibt Lücken dazwischen.
Das Gegenteil ist "Stetig" (wie Wasser oder eine Linie), wo es keine Lücken gibt.

*   (a) Richtig (Definition).
*   (c) Auch richtig (Endlich ist ein Spezialfall von Abzählbar).
*   (e) Richtig. Da die Wahrscheinlichkeit an einzelnen Punkten "klebt", springt die kumulative Kurve (CDF) in Stufen hoch.

---
### Offizielle Lösung
Diskret heißt abzählbar (endlich oder abzählbar unendlich). Die CDF ist eine Treppenfunktion.""",
        "en": r"""**Correct: (a), (c), (e)**

### Study.Smart Guide
**Intuition:**
Discrete means "Grainy" (like integers).
The values are countable. There are gaps.
The CDF looks like a staircase.

---
### Official Solution
Discrete means countable mass points. CDF is a step function."""
    }
}

uebung2_mc2 = {
    "source": "Übung 2, MC #2",
    "type": "mc",
    "question": {
        "de": r"Stetig ist eine Zufallsvariable, wenn:",
        "en": r"A random variable is continuous if:"
    },
    "options": [
        r"sie nur abzählbar viele Werte annehmen kann.",
        r"sie überabzählbar viele Werte annehmen kann.",
        r"sie nur endlich viele Werte annehmen kann.",
        r"sie unendlich viele Werte annehmen kann.",
        r"ihre Verteilungsfunktion nur als Treppenfunktion gezeichnet werden kann."
    ],
    "correct_idx": 1, 
    "solution": {
        "de": r"""**Richtig: (b), (d)**

### Study.Smart Guide
**Intuition:**
Stetig heißt "Fließend". Wie Zeit oder Temperatur.
Zwischen zwei beliebigen Werten gibt es unendlich viele weitere Werte.
Es gibt *überabzählbar* viele Möglichkeiten (wie die reellen Zahlen).

---
### Offizielle Lösung
Stetige ZV können überabzählbar viele Werte annehmen.""",
        "en": r"""**Correct: (b), (d)**

### Study.Smart Guide
**Intuition:**
Continuous means "Fluid". Like time or distance.
Uncountably many values.

---
### Official Solution
Continuous variables take uncountably many values."""
    }
}

uebung2_mc3 = {
    "source": "Übung 2, MC #3",
    "type": "mc",
    "question": {
        "de": r"Der Erwartungswert einer Verteilung:",
        "en": r"The expectation of a distribution:"
    },
    "options": [
        r"ist der Wert, unter dem 50% der Masse liegt (Median).",
        r"ist der erwartete Wert vor dem Experiment.",
        r"ist der Wert, an dem die Dichte maximal ist (Modus).",
        r"ist der Schwerpunkt einer Verteilung.",
        r"ist bei diskreten Verteilungen der wahrscheinlichste Wert."
    ],
    "correct_idx": 3,
    "solution": {
        "de": r"""**Richtig: (b), (d)**

### Study.Smart Guide
**Visualisierung:**
Der Erwartungswert ist der physikalische **Schwerpunkt** (Center of Gravity).
Wenn du die Verteilungskurve aus Pappe ausschneiden würdest, könntest du sie genau an diesem Punkt auf einer Nadelspitze balancieren.

---
### Offizielle Lösung
Schwerpunkt der Verteilung ($E[X]$). Auch als a-priori Erwartung interpretierbar.""",
        "en": r"""**Correct: (b), (d)**

### Study.Smart Guide
**Visual:**
Center of Gravity. The balance point.

---
### Official Solution
Center of gravity."""
    }
}

uebung2_mc4 = {
    "source": "Übung 2, MC #4",
    "type": "mc",
    "question": {
        "de": r"Die Varianz einer diskreten Zufallsvariablen X ist:",
        "en": r"The variance of a discrete random variable X is:"
    },
    "options": [
        r"$\sum (x_i f(x_i) - E[X])^2$",
        r"ein Mass für die Streuung.",
        r"ein Mass für den Schwerpunkt.",
        r"die quadrierte Standardabweichung.",
        r"$\sum x_i^2 f(x_i) - E[X^2]$"
    ],
    "correct_idx": 1,
    "solution": {
        "de": r"""**Richtig: (b), (d)**

### Study.Smart Guide
**Formel-Check:**
*   (a) Falsch. Korrekt wäre: $\sum (x_i - E[X])^2 f(x_i)$. Das $f(x_i)$ gehört nach draußen als Gew중t.
*   (b) Richtig.
*   (d) Richtig ($\sigma^2$).
*   (e) Falsch. Korrekt wäre $E[X^2] - (E[X])^2$ (Verschiebungssatz). Hier stehen die Terme falsch.

---
### Offizielle Lösung
(a) ist falsch geklammert/formuliert. (e) ist Verschiebungssatz falsch. (b) und (d) sind korrekt.""",
        "en": r"""**Correct: (b), (d)**

### Study.Smart Guide
**Analysis:**
(a) Wrong brackets.
(e) Wrong shift formula terms.
(b) and (d) are correct definitions.

---
### Official Solution
Measure of dispersion, squared standard deviation."""
    }
}

uebung2_mc5 = {
    "source": "Übung 2, MC #5",
    "type": "mc",
    "question": {
        "de": r"X diskret. $P(1 \le X < 2)$ ist:",
        "en": r"X discrete. $P(1 \le X < 2)$ is:"
    },
    "options": [
        r"$F(2) - F(1)$",
        r"$F(2) - F(1) - P(X=2)$",
        r"$F(2) - F(1) + P(X=1)$",
        r"$F(2) - F(1) - P(X=2) + P(X=1)$",
        r"$F(2) - F(1) + P(X=2)$"
    ],
    "correct_idx": 3,
    "solution": {
        "de": r"""**Richtig: (d)**

### Study.Smart Guide
**Intuition (Intervall-Logik):**
Wir wollen das Intervall $[1, 2)$. Also alles ab 1 (inklusive) bis knapp vor 2 (exklusive).
$F(2)$ ist alles bis inklusive 2 ($... 1 ... 2$).
$F(1)$ ist alles bis inklusive 1 ($... 1$).
Wenn wir $F(2) - F(1)$ rechnen, bleibt nur das Stück *zwischen* 1 und 2 übrig (exklusiv 1, inklusiv 2).
Wir wollen aber genau das Gegenteil: Inklusiv 1, exklusiv 2.
Also müssen wir $P(X=1)$ wieder dazu addieren und $P(X=2)$ abziehen.

Formel: $F(2) - F(1) - P(X=2) + P(X=1)$.

---
### Offizielle Lösung
$P(1 \le X < 2) = F(2^-) - F(1^-) = (F(2)-P(2)) - (F(1)-P(1))$.<br>$= F(2) - F(1) - P(X=2) + P(X=1)$.""",
        "en": r"""**Correct: (d)**

### Study.Smart Guide
**Intuition:**
We want $[1, 2)$.
$F(b) - F(a)$ usually gives $(a, b]$.
We need to adjust boundaries: Add $P(1)$ back, remove $P(2)$.

---
### Official Solution
Includes 1, excludes 2."""
    }
}

uebung2_mc6 = {
    "source": "Übung 2, MC #6",
    "type": "mc",
    "question": {
        "de": r"Eine Funktion $f(x) \ge 0$ ist eine Dichtefunktion, wenn:",
        "en": r"A function $f(x) \ge 0$ is a PDF if:"
    },
    "options": [
        r"$\sum f(x_i) = 1$.",
        r"$\int_{-\infty}^{\infty} f(x) dx = 1$.",
        r"die Fläche unterhalb gleich 1 ist.",
        r"$F(-\infty)=1$.",
        r"$F(-\infty)=0$ und $F(+\infty)=1$."
    ],
    "correct_idx": 1,
    "solution": {
        "de": r"""**Richtig: (b), (c), (e)**

### Study.Smart Guide
**Definition:**
Eine Dichte muss zwei Dinge erfüllen:
1.  Niemals negativ ($f(x) \ge 0$).
2.  Gesamtfläche ist 1 (Normierung). Das ist Aussage (b) und (c).
(e) bezieht sich auf die Verteilungsfunktion CDF, ist aber auch eine korrekte Eigenschaft, die aus der Dichte folgt.

---
### Offizielle Lösung
Integral ist 1. Entspricht Fläche. CDF Eigenschaften (e).""",
        "en": r"""**Correct: (b), (c), (e)**

### Study.Smart Guide
**Definition:**
Total Area = 1. Non-negative.

---
### Official Solution
Integral equals 1."""
    }
}

uebung2_mc7 = {
    "source": "Übung 2, MC #7",
    "type": "mc",
    "question": {
        "de": r"$f(x) = \frac{1}{2}x^2 - b$ für $1 \le x \le 2$, sonst 0. Für welches $b$ ist dies eine Dichte?",
        "en": r"$f(x) = \frac{1}{2}x^2 - b$ on $[1, 2]$. Find $b$."
    },
    "options": [
        r"$b=1/2$",
        r"$b=1/3$",
        r"$b=1/6$",
        r"$b=1$",
        r"Keine Dichte möglich."
    ],
    "correct_idx": 2,
    "solution": {
        "de": r"""**Richtig: (c)**

### Study.Smart Guide
**Schritt-für-Schritt:**
1.  **Integral berechnen:**
    $\int_1^2 (\frac{1}{2}x^2 - b) dx$.
    Stammfunktion: $[\frac{1}{6}x^3 - bx]_1^2$.
2.  **Grenzen einsetzen:**
    Obergrenze (2): $\frac{8}{6} - 2b$.
    Untergrenze (1): $\frac{1}{6} - b$.
    Differenz: $(\frac{4}{3} - 2b) - (\frac{1}{6} - b) = \frac{8-1}{6} - b = \frac{7}{6} - b$.
3.  **Gleich 1 setzen:**
    $\frac{7}{6} - b = 1 \implies b = \frac{7}{6} - \frac{6}{6} = \frac{1}{6}$.
4.  **Check:** Ist $f(x) \ge 0$?
    $f(1) = 0.5 - 0.16 = 0.33 > 0$. Passt.

---
### Offizielle Lösung
$\int_1^2 (\frac{1}{2}x^2 - b) dx = [\frac{1}{6}x^3 - bx]_1^2 = (\frac{8}{6}-2b) - (\frac{1}{6}-b) = \frac{7}{6} - b = 1 \implies b = 1/6$.<br>Prüfen ob $f(x) \ge 0$: $x^2/2 \ge 1/2 = 3/6 > 1/6$. Ja.""",
        "en": r"""**Correct: (c)**

### Study.Smart Guide
**Step-by-Step:**
1.  Integrate: $[x^3/6 - bx]_1^2$.
2.  Evaluate: $(8/6 - 2b) - (1/6 - b) = 7/6 - b$.
3.  Set to 1: $b = 1/6$.

---
### Official Solution
Integral condition gives $b=1/6$."""
    }
}

uebung2_mc8 = {
    "source": "Übung 2, MC #8",
    "type": "mc",
    "question": {
        "de": r"$f(x) = \frac{1}{18}x$ für $x \in [0, 6]$. Varianz $V(X)$?",
        "en": r"$f(x) = \frac{1}{18}x$ on $[0, 6]$. Variance $V(X)$?"
    },
    "options": [
        r"3",
        r"18",
        r"9",
        r"14/3",
        r"2"
    ],
    "correct_idx": 4,
    "solution": {
        "de": r"""**Richtig: (e)**

### Study.Smart Guide
**Schritt-für-Schritt:**
1.  **Erwartungswert:**
    $E[X] = \int_0^6 x \cdot f(x) dx = \int_0^6 \frac{x^2}{18} dx = [\frac{x^3}{54}]_0^6 = \frac{216}{54} = 4$.
2.  **Zweites Moment:**
    $E[X^2] = \int_0^6 x^2 \cdot f(x) dx = \int_0^6 \frac{x^3}{18} dx = [\frac{x^4}{72}]_0^6 = \frac{1296}{72} = 18$.
3.  **Varianz (Verschiebungssatz):**
    $V(X) = E[X^2] - (E[X])^2 = 18 - 4^2 = 18 - 16 = 2$.

---
### Offizielle Lösung
$E[X] = \int_0^6 x \frac{x}{18} dx = \frac{1}{18} [\frac{x^3}{3}]_0^6 = \frac{216}{54} = 4$.<br>$E[X^2] = \int_0^6 x^2 \frac{x}{18} dx = \frac{1}{18} [\frac{x^4}{4}]_0^6 = \frac{1296}{72} = 18$.<br>$V(X) = 18 - 4^2 = 2$.""",
        "en": r"""**Correct: (e)**

### Study.Smart Guide
**Calculation:**
1.  $E[X] = 4$.
2.  $E[X^2] = 18$.
3.  $V(X) = 18 - 16 = 2$.

---
### Official Solution
$E[X]=4, E[X^2]=18, V(X)=2$."""
    }
}

uebung2_mc9 = {
    "source": "Übung 2, MC #9",
    "type": "mc",
    "question": {
        "de": r"Binomialverteilung beschreibt:",
        "en": r"Binomial distribution describes:"
    },
    "options": [
        r"Erfolg im x-ten Versuch.",
        r"x Erfolge in n Versuchen (mit Zurücklegen).",
        r"x Erfolge in Intervall.",
        r"x Erfolge in n Versuchen (ohne Zurücklegen).",
        r"n Erfolge in x Versuchen."
    ],
    "correct_idx": 1,
    "solution": {
        "de": r"""**Richtig: (b)**

### Study.Smart Guide
**Definition:**
Binomial = **n mal** ziehen **MIT Zurücklegen**.
(Ohne Zurücklegen wäre Hypergeometrisch. Im Intervall wäre Poisson. Erfolg im x-ten Versuch wäre Geometrisch).

---
### Offizielle Lösung
Anzahl Erfolge bei n unabhängigen Bernoulli-Versuchen (Ziehen mit Zurücklegen).""",
        "en": r"""**Correct: (b)**

### Study.Smart Guide
**Definition:**
n trials, independent (with replacement), counting successes.

---
### Official Solution
Successes in n independent trials (with replacement)."""
    }
}

uebung2_mc10 = {
    "source": "Übung 2, MC #10",
    "type": "mc",
    "question": {
        "de": r"Binomialverteilung Approximation:",
        "en": r"Binomial approximation:"
    },
    "options": [
        r"Exponential wenn n > 30.",
        r"Normal wenn $np(1-p) > 9$.",
        r"Normal wenn n > 30, p < 0.1.",
        r"Poisson wenn $np(1-p) > 9$.",
        r"Poisson wenn $n > 30, p \le 0.1$."
    ],
    "correct_idx": 1,
    "solution": {
        "de": r"""**Richtig: (b), (e)**

### Study.Smart Guide
**Faustregeln:**
1.  **Normal-Approximation (Moivre-Laplace):**
    Wenn die Varianz groß genug ist ($\sigma^2 > 9$), ist die Glockenkurve breit genug und nicht "abgeschnitten". (Regel: $npq > 9$).
2.  **Poisson-Approximation:**
    Wenn $n$ riesig und $p$ winzig ist ("Seltene Ereignisse"). Regel: $n>30, p \le 0.1$.

---
### Offizielle Lösung
Faustregeln für Approximation. Normal bei grosser Varianz > 9. Poisson bei seltenen Ereignissen (kleines p, grosses n).""",
        "en": r"""**Correct: (b), (e)**

### Study.Smart Guide
**Rules of Thumb:**
*   Normal: Variance > 9.
*   Poisson: Rare events ($n$ large, $p$ small).

---
### Official Solution
Normal approx (b). Poisson approx (e)."""
    }
}

uebung2_mc11 = {
    "source": "Übung 2, MC #11",
    "type": "mc",
    "question": {
        "de": r"Miguel gewinnt Giro d'Italia mit $p=0.3$. 5 Teilnahmen. Wahrscheinlichkeit mind. 2 Siege?",
        "en": r"Win prob 0.3. 5 attempts. Prob of at least 2 wins?"
    },
    "options": [
        r"0.6398",
        r"0.4718",
        r"0.6",
        r"0.3602",
        r"0.5282"
    ],
    "correct_idx": 1,
    "solution": {
        "de": r"""**Richtig: (b)**

### Study.Smart Guide
**Strategie:**
"Mindestens 2" bedeutet: 2, 3, 4 oder 5.
Einfacher ist das Gegenteil: $1 - (0 \text{ oder } 1)$.

**Rechnung:**
1.  $P(X=0) = \binom{5}{0} 0.3^0 0.7^5 = 1 \cdot 1 \cdot 0.16807$.
2.  $P(X=1) = \binom{5}{1} 0.3^1 0.7^4 = 5 \cdot 0.3 \cdot 0.2401 = 0.36015$.
3.  Summe (0 oder 1): $0.168 + 0.360 = 0.528$.
4.  Gegenwahrscheinlichkeit: $1 - 0.528 = 0.472$.

---
### Offizielle Lösung
$P(0) = 0.7^5 = 0.168$. $P(1) = 5 \cdot 0.3 \cdot 0.7^4 = 0.360$.<br>$1 - 0.168 - 0.360 = 0.472$.""",
        "en": r"""**Correct: (b)**

### Study.Smart Guide
**Calculation:**
Calculate complement (0 or 1 win).
$P(0) \approx 0.168$.
$P(1) \approx 0.360$.
Total compliment = $0.528$.
Result = $1 - 0.528 = 0.472$.

---
### Official Solution
$1 - (P(0)+P(1)) = 0.47178$."""
    }
}

uebung2_mc12 = {
    "source": "Übung 2, MC #12",
    "type": "mc",
    "question": {
        "de": r"Autobatterie Erwartung 10000 km. $P(X > 20000)$? (Annahme Exponential).",
        "en": r"Car battery expected 10000 km. $P(X > 20000)$? (Assume Exponential)."
    },
    "options": [
        r"0.865",
        r"0.607",
        r"0.5",
        r"0.393",
        r"0.135"
    ],
    "correct_idx": 4,
    "solution": {
        "de": r"""**Richtig: (e)**

### Study.Smart Guide
**Intuition:**
Der Mittelwert ist 10.000 (das "Tau" der Lebensdauer).
Wir fragen nach der Wahrscheinlichkeit, dass sie doppelt so lange hält wie der Schnitt (20.000).
Formel für "Überleben": $P(X > x) = e^{-\lambda x}$.
Hier ist $\lambda = 1/10000$.
$P(X > 20000) = e^{-(1/10000) \cdot 20000} = e^{-2} \approx 0.135$.

---
### Offizielle Lösung
Exponentialverteilung $\lambda = 1/10000$.<br>$P(X > 20000) = e^{-\lambda \cdot 20000} = e^{-2} \approx 0.1353$.""",
        "en": r"""**Correct: (e)**

### Study.Smart Guide
**Calculation:**
$\lambda = 1/\mu = 10^{-4}$.
$P(X > 20,000) = e^{-2} \approx 0.135$.

---
### Official Solution
$e^{-2} = 0.135$."""
    }
}

uebung2_mc13 = {
    "source": "Übung 2, MC #13",
    "type": "mc",
    "question": {
        "de": r"$X \sim N(30, 9)$. $P(X < 21)$?",
        "en": r"$X \sim N(30, 9)$. $P(X < 21)$?"
    },
    "options": [
        r"0.9987",
        r"0.8413",
        r"0.1587",
        r"0.00135"
    ],
    "correct_idx": 3,
    "solution": {
        "de": r"""**Richtig: (d)**

### Study.Smart Guide
**Schritt-für-Schritt:**
1.  Stdev $\sigma = \sqrt{9} = 3$.
2.  Z-Score:
    $$Z = \frac{21 - 30}{3} = \frac{-9}{3} = -3$$
3.  Tabelle: Der Wert liegt 3 Standardabweichungen unter dem Mittelwert. (3-Sigma-Regel).
    Das ist extrem selten. $\approx 0.1\%$.
    Genau: $\Phi(-3) \approx 0.0013$.

---
### Offizielle Lösung
$z = \frac{21-30}{3} = -3$.<br>$\Phi(-3) = 1 - \Phi(3) = 1 - 0.99865 = 0.00135$.""",
        "en": r"""**Correct: (d)**

### Study.Smart Guide
**Calculation:**
$Z = -3$. (3 Sigmas away).
Prob $\approx 0.1\%$.

---
### Official Solution
$z=-3$. $\Phi(-3) \approx 0.00135$."""
    }
}

uebung2_mc14 = {
    "source": "Übung 2, MC #14",
    "type": "mc",
    "question": {
        "de": r"$X \sim N(30, 9)$. Finde t so dass $P(X \ge t) = 0.0668$.",
        "en": r"$X \sim N(30, 9)$. Find t s.t. $P(X \ge t) = 0.0668$."
    },
    "options": [
        r"34.5",
        r"33",
        r"31.5",
        r"30"
    ],
    "correct_idx": 0,
    "solution": {
        "de": r"""**Richtig: (a)**

### Study.Smart Guide
**Strategie:**
Wir suchen den "Top 6.68%" Punkt.
Das bedeutet, links davon liegen $1 - 0.0668 = 0.9332$.
1.  Suche $0.9332$ in der Z-Tabelle. $\Rightarrow z \approx 1.5$.
2.  Rück-Transformation:
    $x = \mu + z \cdot \sigma = 30 + 1.5 \cdot 3 = 30 + 4.5 = 34.5$.

---
### Offizielle Lösung
$\Phi(z) = 0.9332$.<br>Tabelle: $z \approx 1.5$.<br>$t = 30 + 1.5 \cdot 3 = 34.5$.""",
        "en": r"""**Correct: (a)**

### Study.Smart Guide
**Calculation:**
Lookup $\Phi(z) = 0.9332$. Found $z=1.5$.
$x = 30 + 1.5(3) = 34.5$.

---
### Official Solution
$z=1.5 \implies t=34.5$."""
    }
}

uebung2_mc15 = {
    "source": "Übung 2, MC #15",
    "type": "mc",
    "question": {
        "de": r"$X \sim N(30, 9)$. Zentrales 95% Intervall?",
        "en": r"$X \sim N(30, 9)$. Central 95% interval?"
    },
    "options": [
        r"29.05 - 30.95",
        r"27.00 - 33.00",
        r"25.05 - 34.95",
        r"24.12 - 35.88"
    ],
    "correct_idx": 3,
    "solution": {
        "de": r"""**Richtig: (d)**

### Study.Smart Guide
**Formel:**
95% Intervall ist definiert durch $\mu \pm 1.96 \sigma$.
$30 \pm 1.96 \cdot 3$.
$30 \pm 5.88$.
$[24.12, 35.88]$.

---
### Offizielle Lösung
$30 \pm 1.96 \cdot 3 = 30 \pm 5.88 = [24.12, 35.88]$.""",
        "en": r"""**Correct: (d)**

### Study.Smart Guide
**Calculation:**
$30 \pm 1.96(3) = 30 \pm 5.88$.

---
### Official Solution
$\mu \pm 1.96\sigma = [24.12, 35.88]$."""
    }
}
