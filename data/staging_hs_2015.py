
"""
HS 2015 Exam Questions Staging File
Extracted and Translated (Dual Mode: Study.Smart Guide + Official)
"""

HS_2015_STAGING = {
    # --- MULTIPLE CHOICE (40 Punkte Total, 4 Punkte each) ---
    
    "hs2015_mc1": {
        "source": "HS 2015, MC 1 (4 Punkte)",
        "type": "mc",
        "question": {
            "de": r"Es seien $X, Y$ zwei stetige Zufallsvariablen. Welche der folgenden Aussagen ist immer korrekt?",
            "en": r"Let $X, Y$ be two continuous random variables. Which of the following statements is always correct?"
        },
        "options": [
            {"de": r"Wenn die Randdichten $f_X(x)$ und $f_Y(y)$ bekannt sind, können wir daraus die gemeinsame Dichte $f_{X,Y}(x, y)$ berechnen.", 
             "en": r"If the marginal densities $f_X(x)$ and $f_Y(y)$ are known, we can calculate the joint density $f_{X,Y}(x, y)$ from them."},
            {"de": r"$X$ und $Y$ sind unabhängig dann und nur dann wenn $\text{Cov}(X, Y) = 0$.", 
             "en": r"$X$ and $Y$ are independent if and only if $\text{Cov}(X, Y) = 0$."},
            {"de": r"$f_{Y|X}(y|x) = f_{X|Y}(x|y)$.", 
             "en": r"$f_{Y|X}(y|x) = f_{X|Y}(x|y)$."},
            {"de": r"$\text{Cov}(X, Y) = 0$ dann und nur dann wenn $E[XY] = E[X]E[Y]$.", 
             "en": r"$\text{Cov}(X, Y) = 0$ if and only if $E[XY] = E[X]E[Y]$."}
        ],
        "correct_idx": 3,
        "solution": {
            "de": r"""**Richtig: (d)**

### Study.Smart Guide
**Intuition:**
Dies ist die exakte Definition von "unkorreliert".
Kovarianz misst, wie sehr zwei Variablen *gemeinsam* variieren ($E[XY]$), verglichen damit, wie sie *einzeln* variieren würden, wenn sie nichts miteinander zu tun hätten ($E[X]E[Y]$). Wenn diese Differenz 0 ist, sind sie unkorreliert.

**Schritt-für-Schritt:**
1.  Formel für Kovarianz:
    $$\text{Cov}(X,Y) = E[XY] - E[X]E[Y]$$
2.  Setze Cov = 0:
    $$0 = E[XY] - E[X]E[Y]$$
3.  Umformen:
    $$E[XY] = E[X]E[Y]$$
    Dies ist also äquivalent.

---
### Offizielle Lösung
$\text{Cov}(X,Y) = E[XY] - E[X]E[Y]$. Wenn dies 0 ist, folgt direkt $E[XY] = E[X]E[Y]$. (b) ist falsch, da Unkorreliertheit $\nRightarrow$ Unabhängigkeit.""",
            "en": r"""**Correct: (d)**

### Study.Smart Guide
**Intuition:**
This is the definition of "uncorrelated".
Covariance compares the expected joint movement ($E[XY]$) to the product of individual expectations ($E[X]E[Y]$). If they are equal, covariance is zero.

**Step-by-Step:**
1.  Covariance Formula:
    $$\text{Cov}(X,Y) = E[XY] - E[X]E[Y]$$
2.  Set Cov = 0:
    $$0 = E[XY] - E[X]E[Y]$$
3.  Rearrange:
    $$E[XY] = E[X]E[Y]$$

---
### Official Solution
$\text{Cov}(X,Y) = E[XY] - E[X]E[Y]$. If this is 0, it directly follows that $E[XY] = E[X]E[Y]$. (b) is false, as uncorrelated $\nRightarrow$ independent."""
        }
    },

    "hs2015_mc2": {
        "source": "HS 2015, MC 2 (4 Punkte)",
        "type": "mc",
        "question": {
            "de": r"Sei $X$ eine stetige Zufallsvariable mit kumulativer Verteilungsfunktion $F(x)$. Welche der folgenden Aussagen ist FALSCH?",
            "en": r"Let $X$ be a continuous random variable with cumulative distribution function $F(x)$. Which of the following statements is FALSE?"
        },
        "options": [
            {"de": r"$P(a \le X \le b) = \int_a^b F(x)dx$", 
             "en": r"$P(a \le X \le b) = \int_a^b F(x)dx$"},
            {"de": r"Wenn $X$ normalverteilt ist, dann gilt $E[X] = \text{Median}(X)$.", 
             "en": r"If $X$ is normally distributed, then $E[X] = \text{Median}(X)$."},
            {"de": r"Wenn $X$ uniform verteilt ist auf $[0, 1]$, dann ist $F(x)$ linear für $x \in [0, 1]$.", 
             "en": r"If $X$ is uniformly distributed on $[0, 1]$, then $F(x)$ is linear for $x \in [0, 1]$."},
            {"de": r"Wenn $X$ uniform verteilt ist, dann gilt $E[X] = \text{Median}(X)$.", 
             "en": r"If $X$ is uniformly distributed, then $E[X] = \text{Median}(X)$."}
        ],
        "correct_idx": 0,
        "solution": {
            "de": r"""**Richtig: (a) ist FALSCH**

### Study.Smart Guide
**Die Falle:**
Wahrscheinlichkeit ist die Fläche unter der **Dichte** $f(x)$, nicht unter der *Verteilungsfunktion* $F(x)$.
Die Verteilungsfunktion $F(x)$ gibt bereits die Fläche an! Man muss sie nicht nochmal integrieren, sondern nur subtrahieren.

**Schritt-für-Schritt:**
Korrekt wäre:
$$P(a \le X \le b) = \int_a^b f(x) dx$$
ODER
$$P(a \le X \le b) = F(b) - F(a)$$
Die Aussage (a) vermischt beides.

---
### Offizielle Lösung
Die Wahrscheinlichkeit berechnet sich aus dem Integral der **Dichte** $f(x)$, nicht der Verteilungsfunktion $F(x)$. Korrekt wäre $P(a \le X \le b) = F(b) - F(a)$.""",
            "en": r"""**Correct: (a) is FALSE**

### Study.Smart Guide
**The Trap:**
Probability is the area under the **Density** $f(x)$, not the *CDF* $F(x)$.
Since $F(x)$ is already the integral, you subtract values, not integrate again.

**Correction:**
Should be:
$$P(a \le X \le b) = F(b) - F(a)$$

---
### Official Solution
Probability is calculated from the integral of the **density** $f(x)$, not the distribution function $F(x)$. Correct would be $P(a \le X \le b) = F(b) - F(a)$."""
        }
    },

    "hs2015_mc3": {
        "source": "HS 2015, MC 3 (4 Punkte)",
        "type": "mc",
        "question": {
            "de": r"Es seien $X$ und $Y$ zwei normal verteilte Zufallsvariablen mit $\mu_X = 1, \sigma_X^2 = 4, \mu_Y = 0$ und $\sigma_Y^2 = 1$. Mit $\Phi(\cdot)$ bezeichnen wir die Verteilungsfunktion der Standardnormalverteilung. Welche der folgenden Aussagen ist FALSCH?",
            "en": r"Let $X$ and $Y$ be two normally distributed random variables with $\mu_X = 1, \sigma_X^2 = 4, \mu_Y = 0$ and $\sigma_Y^2 = 1$. Let $\Phi(\cdot)$ denote the CDF of the standard normal distribution. Which of the following statements is FALSE?"
        },
        "options": [
            {"de": r"$P(\frac{X-1}{2} \le y) = \Phi(y)$", "en": r"$P(\frac{X-1}{2} \le y) = \Phi(y)$"},
            {"de": r"$\Phi^{-1}(0.91) = 0.8186$ (laut Tabelle/Kontext, tatsächlich umgekehrt)", "en": r"$\Phi^{-1}(0.91) = 0.8186$ (according to table/context, actually reserved)"},
            {"de": r"$E[2X - 3Y] = -1$", "en": r"$E[2X - 3Y] = -1$"},
            {"de": r"$\Phi(-1) = P(Y \ge 1)$", "en": r"$\Phi(-1) = P(Y \ge 1)$"}
        ],
        "correct_idx": 2,
        "solution": {
            "de": r"""**Richtig: (c) ist FALSCH**

### Study.Smart Guide
**Intuition:**
Der Erwartungswert ist linear. Wir können die Faktoren einfach vor das E ziehen und einsetzen.

**Rechnung:**
1.  Formel: $E[2X - 3Y] = 2E[X] - 3E[Y]$
2.  Einsetzen: $2(1) - 3(0)$
3.  Ergebnis: $2 - 0 = 2$.
4.  Die Behauptung ist "-1", also falsch.

---
### Offizielle Lösung
$E[2X - 3Y] = 2E[X] - 3E[Y] = 2(1) - 3(0) = 2$. Die Aussage behauptet $-1$.""",
            "en": r"""**Correct: (c) is FALSE**

### Study.Smart Guide
**Calculation:**
1.  Linearity: $E[2X - 3Y] = 2E[X] - 3E[Y]$
2.  Substitute: $2(1) - 3(0) = 2$.
3.  Statement claims -1, so it is false.

---
### Official Solution
$E[2X - 3Y] = 2E[X] - 3E[Y] = 2(1) - 3(0) = 2$. The statement claims $-1$."""
        }
    },

    "hs2015_mc4": {
        "source": "HS 2015, MC 4 (4 Punkte)",
        "type": "mc",
        "question": {
            "de": r"Herr Meyer hat seinen Schlüssel-Code vergessen (4 Stellen). Ziffern 3, 5, 7 kommen vor, eine Ziffer ist doppelt. Wieviele Codes?",
            "en": r"Lost key code (4 digits). Digits 3, 5, 7 appear, one digit is doubled. How many codes?"
        },
        "options": [
            {"de": "12", "en": "12"},
            {"de": "24", "en": "24"},
            {"de": "36", "en": "36"},
            {"de": "72", "en": "72"}
        ],
        "correct_idx": 2,
        "solution": {
            "de": r"""**Richtig: 36**

### Study.Smart Guide
**Intuition:**
Ein zweistufiger Prozess:
1.  Welche Ziffer kommt doppelt vor? (3, 5 oder 7?)
2.  Wie viele Möglichkeiten, diese 4 Ziffern (z.B. 3,3,5,7) anzuordnen?

**Schritt-für-Schritt:**
1.  **Auswahl der doppelten Ziffer:**
    Es gibt 3 Kandidaten (3, 5, 7). $\Rightarrow 3$ Möglichkeiten.
    (Nehmen wir an, die 3 ist doppelt. Unser Set ist {3, 3, 5, 7}).
2.  **Anordnung (Permutation mit Wiederholung):**
    Wir ordnen 4 Ziffern an, wobei eine 2-mal vorkommt.
    $$\frac{n!}{k_1! \cdot k_2! \cdot ...} = \frac{4!}{2! \cdot 1! \cdot 1!} = \frac{24}{2} = 12$$
3.  **Kombination:**
    $3 \text{ Szenarien} \cdot 12 \text{ Anordnungen} = 36$.

---
### Offizielle Lösung
Ziffern: $\{3, 5, 7\}$. Eine Ziffer muss doppelt vorkommen. <br>1. Wahl der doppelten Ziffer: $\binom{3}{1} = 3$ Möglichkeiten.<br>2. Anordnung von 4 Ziffern (z.B. 3,3,5,7): $\frac{4!}{2!1!1!} = \frac{24}{2} = 12$.<br>Total: $3 \cdot 12 = 36$.""",
            "en": r"""**Correct: 36**

### Study.Smart Guide
**Step-by-Step:**
1.  **Choose the Doubled Digit:**
    Could be 3, 5, or 7. (3 options).
    Suppose we picked 3. We now have {3, 3, 5, 7}.
2.  **Arrange the Digits:**
    Permutation of 4 items with 2 identical:
    $$\frac{4!}{2!} = \frac{24}{2} = 12$$
3.  **Total:**
    $3 \times 12 = 36$.

---
### Official Solution
Digits: $\{3, 5, 7\}$. One digit must appear twice. <br>1. Choose the doubled digit: $\binom{3}{1} = 3$ options.<br>2. Arrange 4 digits (e.g., 3,3,5,7): $\frac{4!}{2!1!1!} = \frac{24}{2} = 12$.<br>Total: $3 \cdot 12 = 36$."""
        }
    },

    "hs2015_mc5": {
        "source": "HS 2015, MC 5 (4 Punkte)",
        "type": "mc",
        "question": {
            "de": r"Es sei $X$ eine diskrete Zufallsvariable mit einer Wahrscheinlichkeitsmassenfunktion der Form $f(x) = \frac{x+4}{c}$ für $x = 1, \dots, 5$ (0 sonst). Für welchen Wert von $c$ ist $f(x)$ eine Wahrscheinlichkeitsmassenfunktion?",
            "en": r"Let $X$ be a discrete random variable with a probability mass function of the form $f(x) = \frac{x+4}{c}$ for $x = 1, \dots, 5$ (0 otherwise). For which value of $c$ is $f(x)$ a probability mass function?"
        },
        "options": [
            {"de": "c = 20", "en": "c = 20"},
            {"de": "c = 25", "en": "c = 25"},
            {"de": "c = 30", "en": "c = 30"},
            {"de": "c = 35", "en": "c = 35"}
        ],
        "correct_idx": 3,
        "solution": {
            "de": r"""**Richtig: c = 35**

### Study.Smart Guide
**Intuition:**
Die Summe aller Wahrscheinlichkeiten muss immer genau 1 ergeben (100%).

**Schritt-für-Schritt:**
1.  Summiere alle Zähler für $x=1,2,3,4,5$:
    $$(1+4) + (2+4) + (3+4) + (4+4) + (5+4)$$
    $$= 5 + 6 + 7 + 8 + 9 = 35$$
2.  Normierungsbedingung:
    $$\frac{35}{c} = 1$$
3.  Lösung:
    $$c = 35$$

---
### Offizielle Lösung
Summe der Wahrscheinlichkeiten muss 1 sein: $\sum_{x=1}^5 \frac{x+4}{c} = 1$.<br>Zähler-Summe: $(1+4)+(2+4)+(3+4)+(4+4)+(5+4) = 5+6+7+8+9 = 35$.<br>Also $35/c = 1 \Rightarrow c=35$.""",
            "en": r"""**Correct: c = 35**

### Study.Smart Guide
**Step-by-Step:**
1.  Sum of numerators for $x=1$ to $5$:
    $$5 + 6 + 7 + 8 + 9 = 35$$
2.  Condition: Sum / c = 1.
3.  Therefore $c = 35$.

---
### Official Solution
Sum of probabilities must match 1: $\sum_{x=1}^5 \frac{x+4}{c} = 1$.<br>Numerator sum: $(1+4)+(2+4)+(3+4)+(4+4)+(5+4) = 5+6+7+8+9 = 35$.<br>Thus $35/c = 1 \Rightarrow c=35$."""
        }
    },

    "hs2015_mc6": {
        "source": "HS 2015, MC 6 (4 Punkte)",
        "type": "mc",
        "question": {
            "de": r"Es seien $X_i, i = 1, \dots, n$ Zufallsvariablen. Betrachten Sie:<br>1) $\text{Var}(\sum X_i) = \sum \text{Var}(X_i)$<br>2) $\sum \text{Var}(X_i) = n \cdot \text{Var}(X_j)$<br>Welche Aussage ist korrekt?",
            "en": r"Let $X_i, i = 1, \dots, n$ be random variables. Consider:<br>1) $\text{Var}(\sum X_i) = \sum \text{Var}(X_i)$<br>2) $\sum \text{Var}(X_i) = n \cdot \text{Var}(X_j)$<br>Which statement is correct?"
        },
        "options": [
            {"de": "Hinreichend für 1: Identisch verteilt. Hinreichend für 2: Unabhängig.", "en": "Sufficient for 1: Identically distributed. Sufficient for 2: Independent."},
            {"de": "Hinreichend für 1: Unabhängig. Hinreichend für 2: Identisch verteilt.", "en": "Sufficient for 1: Independent. Sufficient for 2: Identically distributed."},
            {"de": "Beide gelten immer, auch bei Abhängigkeit.", "en": "Both always hold, even with dependency."},
            {"de": "Beide gelten immer, auch bei nicht-identischer Verteilung.", "en": "Both always hold, even with non-identical distribution."}
        ],
        "correct_idx": 1,
        "solution": {
            "de": r"""**Richtig: (b)**

### Study.Smart Guide
**Intuition:**
1.  **Gleichung 1 (Summe der Varianzen):** Das ist die Formel von Bienaymé. Sie gilt nur, wenn es keine Interaktion (Kovarianz) zwischen den Variablen gibt. Sie müssen also **unabhängig** (unkorreliert) sein.
2.  **Gleichung 2 (n mal Varianz):** Das bedeutet einfach, dass jede Variable die gleiche Varianz hat. Sie müssen also **identisch verteilt** sein.

---
### Offizielle Lösung
Gleichung 1 (Bienaymé) gilt, wenn die Variablen **unabhängig** (oder zumindest unkorreliert) sind.<br>Gleichung 2 gilt, wenn alle Varianzen gleich sind, also wenn sie **identisch verteilt** sind.""",
            "en": r"""**Correct: (b)**

### Study.Smart Guide
**Intuition:**
1.  **Eq 1 (Sum of Variances):** Requires zero covariance, i.e., **Independence**.
2.  **Eq 2 (n times Variance):** Requires all variances to be equal, i.e., **Identically Distributed**.

---
### Official Solution
Equation 1 (Bienaymé) holds if variables are **independent** (or at least uncorrelated).<br>Equation 2 holds if all variances are equal, i.e., if they are **identically distributed**."""
        }
    },

    "hs2015_mc7": {
        "source": "HS 2015, MC 7 (4 Punkte)",
        "type": "mc",
        "question": {
            "de": r"Es seien $X, Y$ und $Z$ drei Zufallsvariablen wobei $Y = 3X + 2$ und $Z = 2X - 3$. Welche Aussage ist korrekt?",
            "en": r"Let $X, Y$ and $Z$ be three random variables where $Y = 3X + 2$ and $Z = 2X - 3$. Which statement is correct?"
        },
        "options": [
            {"de": r"$\text{Corr}(X, Y) > \text{Corr}(X, Z)$", "en": r"$\text{Corr}(X, Y) > \text{Corr}(X, Z)$"},
            {"de": r"$\text{Corr}(X, Y) = \text{Corr}(X, Z)$", "en": r"$\text{Corr}(X, Y) = \text{Corr}(X, Z)$"},
            {"de": r"$\text{Corr}(X, Y) < \text{Corr}(X, Z)$", "en": r"$\text{Corr}(X, Y) < \text{Corr}(X, Z)$"},
            {"de": "Nicht genügend Informationen.", "en": "Not enough information."}
        ],
        "correct_idx": 1,
        "solution": {
            "de": r"""**Richtig: (b)**

### Study.Smart Guide
**Intuition:**
Sowohl Y als auch Z sind einfach nur X, das mit einer positiven Zahl multipliziert und verschoben wurde.
Eine lineare Transformation (mit positiver Steigung) ändert die Korrelation nicht. Das "Muster" bleibt perfekt erhalten.
X ist zu 100% korreliert mit X. Daher sind beide Korrelationen gleich 1.

---
### Offizielle Lösung
Beide sind lineare Transformationen mit positiver Steigung ($a=3$ und $a=2$). Die Korrelation mit sich selbst (linear transformiert) ist immer $+1$. Also $\text{Corr}(X,Y)=1$ und $\text{Corr}(X,Z)=1$.""",
            "en": r"""**Correct: (b)**

### Study.Smart Guide
**Intuition:**
Linear transformations (scaling and shifting) do not change correlation (as long as slope is positive).
Both Y and Z move perfectly in sync with X.
$\text{Corr} = 1$ for both.

---
### Official Solution
Both are linear transformations with positive slope ($a=3$ and $a=2$). Correlation with oneself (linearly transformed) is always $+1$. Thus $\text{Corr}(X,Y)=1$ and $\text{Corr}(X,Z)=1$."""
        }
    },

    "hs2015_mc8": {
        "source": "HS 2015, MC 8 (4 Punkte)",
        "type": "mc",
        "question": {
            "de": r"Aus einer Stichprobe von 3 Werten berechnet man $\bar{x} = 5.5$ und $s^2 = 4.5$. Median?",
            "en": r"Sample of 3 values: $\bar{x} = 5.5$ and $s^2 = 4.5$. Median?"
        },
        "options": [
            {"de": "-1", "en": "-1"},
            {"de": "1", "en": "1"},
            {"de": "4", "en": "4"},
            {"de": "Wir haben nicht genügend Informationen.", "en": "We do not have enough information."}
        ],
        "correct_idx": 3,
        "solution": {
            "de": r"""**Richtig: (d)**

### Study.Smart Guide
**Intuition:**
Du hast 3 Unbekannte ($x_1, x_2, x_3$) aber nur 2 Gleichungen (Mittelwert und Varianz).
Das System ist "unterbestimmt". Es gibt unendlich viele Zahlentrios, die auf diese Werte kommen, und sie haben unterschiedliche Mediane.

---
### Offizielle Lösung
Mit $n=3$ gibt es unendlich viele Kombinationen von 3 Zahlen, die diesen Mittelwert und diese Varianz ergeben. Der Median ist nicht eindeutig bestimmt.""",
            "en": r"""**Correct: (d)**

### Study.Smart Guide
**Intuition:**
We have 3 unknowns but only 2 constraints (Mean, Variance).
The system is underdetermined. Infinitely many sets of numbers fit, leading to different medians.

---
### Official Solution
With $n=3$, there are infinitely many combinations of 3 numbers yielding this mean and variance. The median is not uniquely determined."""
        }
    },

    "hs2015_mc9": {
        "source": "HS 2015, MC 9 (4 Punkte)",
        "type": "mc",
        "question": {
            "de": r"1000 Packungen Reis normalverteilt. 800 Packungen wiegen zwischen 343.2 und 356.8 Gramm. Ungefähre Varianz?",
            "en": r"1000 packages of rice normally distributed. 800 packages weigh between 343.2 and 356.8 grams. Approximate variance?"
        },
        "options": [
            {"de": r"$\sigma^2 \approx 16$", "en": r"$\sigma^2 \approx 16$"},
            {"de": r"$\sigma^2 \approx 25$", "en": r"$\sigma^2 \approx 25$"},
            {"de": r"$\sigma^2 \approx 36$", "en": r"$\sigma^2 \approx 36$"},
            {"de": r"$\sigma^2 \approx 49$", "en": r"$\sigma^2 \approx 49$"}
        ],
        "correct_idx": 1,
        "solution": {
            "de": r"""**Richtig: (b)**

### Study.Smart Guide
**Schritt-für-Schritt:**
1.  Anteil = 800/1000 = 80%.
2.  Wir suchen das symmetrische Intervall für 80%. Aus der Z-Tabelle (oder Faustregel):
    $P(-z \le Z \le z) = 0.8$. Das entspricht $z \approx 1.28$.
3.  Die Intervallbreite ist $2 \cdot z \cdot \sigma$.
    Breite: $356.8 - 343.2 = 13.6$.
4.  Gleichung aufstellen:
    $$2 \cdot 1.28 \cdot \sigma = 13.6$$
    $$2.56 \sigma = 13.6$$
    $$\sigma \approx 5.3$$
5.  Varianz ist $\sigma^2$:
    $$5.3^2 \approx 28$$
    Am nächsten liegt die 25.

---
### Offizielle Lösung
Anteil $800/1000 = 0.8$. Das symmetrische Intervall für $80\%$ Wahrscheinlichkeit ist $\mu \pm 1.28\sigma$.<br>Intervallbreite: $356.8 - 343.2 = 13.6$.<br>$2 \cdot 1.28 \sigma = 13.6 \Rightarrow \sigma \approx 5.31$.<br>$\sigma^2 \approx 28.2$. Am nächsten bei 25.""",
            "en": r"""**Correct: (b)**

### Study.Smart Guide
**Step-by-Step:**
1.  Target prob: 80%. Critical Z-score $\approx 1.28$.
2.  Total width of interval: $13.6$. This corresponds to $2 \times 1.28$ standard deviations.
3.  solve: $2.56 \sigma = 13.6 \implies \sigma \approx 5.31$.
4.  Variance: $5.31^2 \approx 28$. Closest option is 25.

---
### Official Solution
Proportion $800/1000 = 0.8$. Symmetric interval for $80\%$ probability is $\mu \pm 1.28\sigma$.<br>Interval width: $356.8 - 343.2 = 13.6$.<br>$2 \cdot 1.28 \sigma = 13.6 \Rightarrow \sigma \approx 5.31$.<br>$\sigma^2 \approx 28.2$. Closest to 25."""
        }
    },

    "hs2015_mc10": {
        "source": "HS 2015, MC 10 (4 Punkte)",
        "type": "mc",
        "question": {
            "de": r"Für $\theta > 1$ sei $X_i \sim U[1, \theta]$ (i.i.d.). Schätzer $\hat{\theta} = \frac{2}{n} \sum X_i$. Wahrheit?",
            "en": r"For $\theta > 1$ let $X_i \sim U[1, \theta]$ (i.i.d.). Estimator $\hat{\theta} = \frac{2}{n} \sum X_i$. Truth?"
        },
        "options": [
            {"de": r"Die Varianz des Schätzers ist $\frac{(\theta-1)^2}{3n}$.", "en": r"The variance of the estimator is $\frac{(\theta-1)^2}{3n}$."},
            {"de": r"Der Schätzer ist erwartungstreu, aber nicht konsistent.", "en": r"The estimator is unbiased but not consistent."},
            {"de": r"Der Schätzer ist konsistent, aber nicht erwartungstreu.", "en": r"The estimator is consistent but not unbiased."},
            {"de": r"Der Bias des Schätzers ist $\frac{\theta}{3n}$.", "en": r"The bias of the estimator is $\frac{\theta}{3n}$."}
        ],
        "correct_idx": 0,
        "solution": {
            "de": r"""**Richtig: (a)**

### Study.Smart Guide
**Schritt-für-Schritt:**
1.  Varianz von U[1, $\theta$]:
    $$\text{Var}(X) = \frac{(\theta-1)^2}{12}$$
2.  Varianz des Schätzers $\hat{\theta} = \frac{2}{n} \sum X_i$:
    $$\text{Var}(\frac{2}{n}S) = (\frac{2}{n})^2 \text{Var}(S) = \frac{4}{n^2} \cdot n \cdot \text{Var}(X)$$
3.  Einsetzen:
    $$\frac{4}{n} \cdot \frac{(\theta-1)^2}{12} = \frac{(\theta-1)^2}{3n}$$

---
### Offizielle Lösung
$\text{Var}(X) = \frac{(\theta-1)^2}{12}$.<br>$\text{Var}(\hat{\theta}) = (\frac{2}{n})^2 \cdot n \cdot \text{Var}(X) = \frac{4}{n} \cdot \frac{(\theta-1)^2}{12} = \frac{(\theta-1)^2}{3n}$.""",
            "en": r"""**Correct: (a)**

### Study.Smart Guide
**Calculation:**
1.  Individual Var: $(\theta-1)^2/12$.
2.  Sum Var: $n \times$ Individual Var.
3.  Scaled Sum Var: $(2/n)^2 \times$ Sum Var.
4.  Result: $4/n^2 \times n \times Var/12 = Var/3n$.

---
### Official Solution
$\text{Var}(X) = \frac{(\theta-1)^2}{12}$.<br>$\text{Var}(\hat{\theta}) = (\frac{2}{n})^2 \cdot n \cdot \text{Var}(X) = \frac{4}{n} \cdot \frac{(\theta-1)^2}{12} = \frac{(\theta-1)^2}{3n}$."""
        }
    },

    # --- LONG FORM PROBLEMS (Aufgabe 1-5) ---
    
    "hs2015_prob1": {
        "source": "HS 2015, Aufgabe 1 (12 Punkte)",
        "type": "problem",
        "question": {
            "de": r"**Teil 1A (4 Punkte):** Ordnen Sie die Verteilungen den Grafiken zu.<br>V1: $N(0,3)$, n=100<br>V2: Exp(3), n=100<br>V3: $N(0,1)$, n=100<br>V4: U[-3,3], n=100<br><br>Grafiken: A (Boxplot), B (Histogramm), C (ECDF), D (QQ-Plot).<br><br>**Teil 1B (8 Punkte):**<br>Daten: Note 0.7 (1x), 2.3 (5x), 3.0 (6x), 3.7 (6x), 4.0 (4x), 4.3 (6x), 4.7 (4x), 5.0 (7x).<br>1. Berechnen Sie Mittelwert und Modus.<br>2. Zeichnen Sie einen Boxplot (Quartile, IQA).",
            "en": r"**Part 1A (4 Points):** Match the distributions to the plots.<br>V1: $N(0,3)$, n=100<br>V2: Exp(3), n=100<br>V3: $N(0,1)$, n=100<br>V4: U[-3,3], n=100<br><br>Plots: A (Boxplot), B (Histogram), C (ECDF), D (QQ-Plot).<br><br>**Part 1B (8 Points):**<br>Data: Grade 0.7 (1x), 2.3 (5x), 3.0 (6x), 3.7 (6x), 4.0 (4x), 4.3 (6x), 4.7 (4x), 5.0 (7x).<br>1. Calculate Mean and Mode.<br>2. Draw a Boxplot (Quartiles, IQR)."
        },
        "solution": {
            "de": r"""### Study.Smart Guide
**Intuition - Teil 1A (Grafiken):**
*   **V2 (Exponential):** Ist stark schief (asymmetrisch). Der Boxplot (A) wird viele Ausreißer nach oben zeigen.
*   **V3 (Standardnormal):** Klassische Glockenkurve im Histogramm (B).
*   **V1 (N(0,3)):** S-Kurve im ECDF (C), aber flacher als N(0,1).
*   **V4 (Uniform):** Hat "leichte Ränder". Im Normal-QQ-Plot (D) sieht das wie ein S aus (abweichend von Gerade).

**Lösung - Teil 1B:**
Datenliste (sortiert): 39 Werte.
*   **Modus:** Der häufigste Wert. 5.0 kommt 7-mal vor.
*   **Median:** Der 20. Wert. (Zähle durch: 1+5+6 = 12. 12+6 = 18. Der 19. und 20. Wert sind beide 4.0). Median = 4.0.
*   **Quartile:** Position $0.25 \times 39 \approx 10$. (Wert 3.0). Position $0.75 \times 39 \approx 30$. (Wert 4.7).

---
### Offizielle Lösung
**Lösung 1A:**<br>A $\Leftrightarrow$ V2 (Asymmetrisch, viele Ausreißer)<br>B $\Leftrightarrow$ V3 (Glockenkurve)<br>C $\Leftrightarrow$ V1 (S-Kurve)<br>D $\Leftrightarrow$ V4 (QQ-Plot abweichend von Gerade an Rändern)<br><br>**Lösung 1B:**<br>1. Mittelwert = 3.79, Modus = 5.0 (7 Nennungen)<br>2. 25% Quartil = 3.0, Median = 4.0, 75% Quartil = 4.7. IQA = 1.7.""",
            "en": r"""### Study.Smart Guide
**Analysis:**
*   **V2 (Exp):** Asymmetric = Boxplot with outliers (A).
*   **V3 (Std Normal):** Bell curve = Histogram (B).
*   **median:** 20th value in sorted list = 4.0.

---
### Official Solution
**Solution 1A:**<br>A $\Leftrightarrow$ V2 (Asymmetric, outliers)<br>B $\Leftrightarrow$ V3 (Bell curve)<br>C $\Leftrightarrow$ V1 (S-curve)<br>D $\Leftrightarrow$ V4 (QQ-plot deviates at tails)<br><br>**Solution 1B:**<br>1. Mean = 3.79, Mode = 5.0 (7 counts)<br>2. 25% Quartile = 3.0, Median = 4.0, 75% Quartile = 4.7. IQR = 1.7."""
        }
    },

    "hs2015_prob2": {
        "source": "HS 2015, Aufgabe 2 (10 Punkte)",
        "type": "problem",
        "question": {
            "de": r"**Teil 2A (6 Punkte):** Urne mit 1 schwarzen, 2 roten Kugeln. Ziehen ohne Zurücklegen (3 mal).<br>1. Baumdiagramm zeichnen.<br>2. P(rote Kugel im 2. Zug)?<br>3. P(rot im 1. Zug | rot im 2. Zug)?<br><br>**Teil 2B (4 Punkte):** Multiple Choice Klausur (20 Fragen, 4 Antworten, 12 nötig).<br>1. Wahrscheinlichkeit, dass Rater besteht (1 falsche ausschließen, dann raten)?<br>2. Poisson Approximation für 100 Studenten (mind. 3 bestehen)?",
            "en": r"**Part 2A (6 Points):** Urn with 1 black, 2 red balls. Draw without replacement (3 times).<br>1. Draw tree diagram.<br>2. P(red ball in 2nd draw)?<br>3. P(red in 1st | red in 2nd)?<br><br>**Part 2B (4 Points):** Multiple Choice Exam (20 questions, 4 answers, 12 needed).<br>1. Probability guesser passes (exclude 1 false, then guess)?<br>2. Poisson approximation for 100 students (at least 3 pass)?"
        },
        "solution": {
            "de": r"""### Study.Smart Guide
**Teil 2A - Intuition:**
*   **Frage 2:** Wegen Symmetrie ist die Wahrscheinlichkeit, Rot an 2. Stelle zu ziehen, gleich wie an 1. Stelle. Also $2/3$.
*   **Frage 3:** Bayes-Theorem oder Baum umkehren.

**Teil 2B - Intuition:**
*   **Strategie:** 1 ausschließen $\to$ Ratewahrscheinlichkeit $p = 1/3$.
*   **Verteilung:** Binomial(n=20, p=1/3). Wir suchen $P(X \ge 12)$.
*   **Poisson:** Wenn $p$ sehr klein ist, können wir die Anzahl der erfolgreichen Studenten durch Poisson approximieren. $\lambda = n_{Stud} \cdot p_{Bestand}$.

---
### Offizielle Lösung
**Lösung 2A:**<br>2. P(Rot 2) = 2/3.<br>3. P(R1|R2) = 1/2.<br><br>**Lösung 2B:**<br>1. Binomial(n=20, p=1/3). P(X $\ge$ 12) $\approx$ 0.013.<br>2. $\lambda = 100 \cdot 0.013 = 1.3$. P(Y $\ge$ 3) = 1 - P(Y $\le$ 2) $\approx$ 0.1429.""",
            "en": r"""### Study.Smart Guide
**Intuition:**
*   **2A:** Symmetry argument: P(Red at 2) = P(Red at 1) = 2/3.
*   **2B:** With 1 option elimated, chance is 1/3. Use Binomial CDF.

---
### Official Solution
**Solution 2A:**<br>2. P(Red 2) = 2/3.<br>3. P(R1|R2) = 1/2.<br><br>**Solution 2B:**<br>1. Binomial(n=20, p=1/3). P(X $\ge$ 12) $\approx$ 0.013.<br>2. $\lambda = 100 \cdot 0.013 = 1.3$. P(Y $\ge$ 3) = 1 - P(Y $\le$ 2) $\approx$ 0.1429."""
        }
    },

    "hs2015_prob3": {
        "source": "HS 2015, Aufgabe 3 (18 Punkte)",
        "type": "problem",
        "question": {
            "de": r"Reifenlebensdauer $T_1 \sim \text{Exp}(1/500)$.<br>1. Berechnen Sie $F(t)$.<br>2. $P(X > 500)$.<br>3. Welche Lebensdauer wird mit $P=0.2$ überschritten?<br>4. $T = \min(T_1, T_2)$. Verteilung von $T$? ($T_1, T_2$ i.i.d).<br>5. 20 Reifenpaare nacheinander. Wahrscheinlichkeit > 15 Jahre?",
            "en": r"Tire lifespan $T_1 \sim \text{Exp}(1/500)$.<br>1. Calculate $F(t)$.<br>2. $P(X > 500)$.<br>3. What lifespan is exceeded with $P=0.2$?<br>4. $T = \min(T_1, T_2)$. Distribution of $T$? ($T_1, T_2$ i.i.d).<br>5. 20 tire pairs sequentially. Probability > 15 years?"
        },
        "solution": {
            "de": r"""### Study.Smart Guide
**Intuition:**
*   **Minimum:** "Ein System fällt aus, sobald der *erste* Reifen platzt." Die Rate addiert sich. 2 Reifen mit je Rate $\lambda$ $\to$ Systemrate $2\lambda$.
*   **Summe:** Zentraler Grenzwertsatz (CLT). Die Summe von 20 Variablen nähert sich einer Normalverteilung.

**Schritte:**
1.  Exp-Verteilung: $F(t) = 1 - e^{-\lambda t}$.
4.  Minimum von Exponentials: Summe der Raten. $\lambda_{neu} = 1/500 + 1/500 = 1/250$.

---
### Offizielle Lösung
**Lösung:**<br>1. $F(t) = 1 - e^{-t/500}$.<br>2. $e^{-1} \approx 0.368$.<br>3. $x \approx 805$ Tage.<br>4. $T \sim \text{Exp}(1/250)$.<br>5. Summe von 20 Exp-Variablen $\to$ Näherung durch Normalverteilung (CLT). $P(S > 5475) \approx 0.39$.""",
            "en": r"""### Study.Smart Guide
**Intuition:**
*   **Min of Exponentials:** Rates add up. Two tires fail twice as fast. $\lambda_{new} = 2\lambda$.
*   **Sum:** Use CLT to approximate sum of 20 durations as Normal.

---
### Official Solution
**Solution:**<br>1. $F(t) = 1 - e^{-t/500}$.<br>2. $e^{-1} \approx 0.368$.<br>3. $x \approx 805$ days.<br>4. $T \sim \text{Exp}(1/250)$.<br>5. Sum of 20 Exp variables $\to$ Approx via Normal (CLT). $P(S > 5475) \approx 0.39$."""
        }
    },

    "hs2015_prob4": {
        "source": "HS 2015, Aufgabe 4 (20 Punkte)",
        "type": "problem",
        "question": {
            "de": r"Gemeinsame Dichte $f(x,y) = \lambda(xy+c)$ auf Rechteck $x \in [0,2], y \in [0,1]$.<br>1. Zeigen Sie $\lambda = 1/(1+2c)$.<br>2. Berechnen Sie die Randdichte $f_X(x)$.<br>3. Varianz von $X$ für $c=1$.<br>4. Ansatz $P(X+Y < 6/5)$.<br>5. Berechnen Sie $P(X+Y < 6/5)$ für $c=0$.",
            "en": r"Joint density $f(x,y) = \lambda(xy+c)$ on rectangle $x \in [0,2], y \in [0,1]$.<br>1. Show $\lambda = 1/(1+2c)$.<br>2. Calculate marginal density $f_X(x)$.<br>3. Variance of $X$ for $c=1$.<br>4. Setup $P(X+Y < 6/5)$.<br>5. Calculate $P(X+Y < 6/5)$ for $c=0$."
        },
        "solution": {
            "de": r"""### Study.Smart Guide
**Schritt-für-Schritt:**
1.  **Normierung:** Das Doppelintegral über das Rechteck $[0,2] \times [0,1]$ muss 1 ergeben.
    $\int_0^2 \int_0^1 (xy+c) dy dx = ...$
2.  **Randdichte:** Man "integriert y heraus".
    $f_X(x) = \int_0^1 f(x,y) dy$.

---
### Offizielle Lösung
**Lösung:**<br>1. Integral über Bereich muss 1 geben.<br>2. $f_X(x) = \frac{x+2c}{2+4c}$.<br>3. $\text{Var}(X) \approx 0.32$.<br>5. Integral über Dreieck/Bereich $\approx 0.085$.""",
            "en": r"""### Study.Smart Guide
**Steps:**
1.  Set double integral to 1 to find $\lambda$.
2.  Integrate out $y$ to find marginal $f_X$.

---
### Official Solution
**Solution:**<br>1. Integral over domain must be 1.<br>2. $f_X(x) = \frac{x+2c}{2+4c}$.<br>3. $\text{Var}(X) \approx 0.32$.<br>5. Integral over triangle/domain $\approx 0.085$."""
        }
    },

    "hs2015_prob5": {
        "source": "HS 2015, Aufgabe 5 (20 Punkte)",
        "type": "problem",
        "question": {
            "de": r"Dichte $f(x) = \frac{\alpha}{x^{\alpha+1}}$ für $x \ge 1$.<br>1. Bestimmen Sie den Maximum Likelihood Schätzer (MLE) für $\alpha$.<br>2. Berechnen Sie MLE für Probe: 11.0, 16.4, 27.9, 15.9.<br>3. Bestimmen Sie den Momentenschätzer (MM) für $\alpha$.<br>4. Berechnen Sie MM für obige Probe.<br>5. Vergleich?",
            "en": r"Density $f(x) = \frac{\alpha}{x^{\alpha+1}}$ for $x \ge 1$.<br>1. Determine MLE for $\alpha$.<br>2. Calculate MLE for sample: 11.0, 16.4, 27.9, 15.9.<br>3. Determine Method of Moments (MM) estimator for $\alpha$.<br>4. Calculate MM for sample.<br>5. Compare?"
        },
        "solution": {
            "de": r"""### Study.Smart Guide
**MLE Rezept:**
1.  Likelihood aufstellen: $L = \prod f(x_i)$.
2.  Log-Likelihood: $l = \sum \ln f(x_i)$.
3.  Ableiten nach $\alpha$ und gleich 0 setzen.

**MM Rezept:**
1.  Theoretischen Erwartungswert $E[X]$ berechnen (Integral $x \cdot f(x)$).
2.  Gleichsetzen mit Stichprobenmittel $\bar{x}$.
3.  Nach $\alpha$ auflösen.

---
### Offizielle Lösung
**Lösung:**<br>1. $\hat{\alpha}_{MLE} = \frac{n}{\sum \ln x_i}$.<br>2. $\hat{\alpha} \approx 0.35$. (Achtung: Dichte braucht $\alpha > 0$.)<br>3. $E[X] = \frac{\alpha}{\alpha-1}$. Auflösen nach $\alpha$: $\hat{\alpha}_{MM} = \frac{\bar{x}}{\bar{x}-1}$.<br>4. $\bar{x}=17.8 \Rightarrow \hat{\alpha} \approx 1.06$.<br>5. Momentenmethode nur für $\alpha > 1$ definiert.""",
            "en": r"""### Study.Smart Guide
**MLE Recipe:**
1.  Log-Likelihood.
2.  Derivative w.r.t $\alpha = 0$.

**MM Recipe:**
1.  Calc theoretical Mean $E[X]$.
2.  Equate to Sample Mean $\bar{X}$.
3.  Solve for parameter.

---
### Official Solution
**Solution:**<br>1. $\hat{\alpha}_{MLE} = \frac{n}{\sum \ln x_i}$.<br>2. $\hat{\alpha} \approx 0.35$. (Note: Density needs $\alpha > 0$.)<br>3. $E[X] = \frac{\alpha}{\alpha-1}$. Solve for $\alpha$: $\hat{\alpha}_{MM} = \frac{\bar{x}}{\bar{x}-1}$.<br>4. $\bar{x}=17.8 \Rightarrow \hat{\alpha} \approx 1.06$.<br>5. Method of Moments only defined for $\alpha > 1$."""
        }
    }
}
