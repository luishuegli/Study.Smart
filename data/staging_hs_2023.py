
# HS 2023 Exam Staging File
# Content extracted from:
# - HS2023_january_german.pdf
# - HS2023_january_german_solution.pdf
# Dual-Mode: Study.Smart Guide + Official Solution

# ------------------------------------------------------------------
# MULTIPLE CHOICE (4 Punkte each)
# ------------------------------------------------------------------

hs2023_mc1 = {
    "source": "HS 2023 Januar, MC #1 (4 Punkte)",
    "type": "mc",
    "question": {
        "de": r"Folgende Informationen sind gegeben: $P(A) = 0.5$, $P(B) = 0.3$, $P(A \cup B) = 0.4$. Welche der folgenden Aussagen ist wahr?",
        "en": r"Given: $P(A) = 0.5$, $P(B) = 0.3$, $P(A \cup B) = 0.4$. Which of the following statements is true?"
    },
    "options": [
        r"A und B sind disjunkt. (A and B are disjoint.)",
        r"A und B sind unabhängig. (A and B are independent.)",
        r"A und B sind nicht unabhängig. (A and B are not independent.)",
        r"Nicht genügend Informationen gegeben. (Not enough information given.)"
    ],
    "correct_idx": 2, 
    "solution": {
        "de": r"""**Richtig: (c)**

### Study.Smart Guide
**Intuition:**
Unabhängigkeit bedeutet: "Die Wahrscheinlichkeit für A und B zusammen ($A \cap B$) ist einfach das Produkt der Einzelwahrscheinlichkeiten."
Wir prüfen also: Ist $P(A \cap B) = P(A) \cdot P(B)$?

**Schritt-für-Schritt:**
1.  **Schnittmenge berechnen:**
    Nutze den Additionssatz: $P(A \cup B) = P(A) + P(B) - P(A \cap B)$.
    $0.4 = 0.5 + 0.3 - P(A \cap B)$
    $P(A \cap B) = 0.8 - 0.4 = 0.4$.
2.  **Unabhängigkeitstest:**
    Soll: $P(A) \cdot P(B) = 0.5 \cdot 0.3 = 0.15$.
    Ist: $0.4$.
3.  **Vergleich:**
    $0.4 \neq 0.15$.
    Also sind sie **nicht** unabhängig (sie "kleben" stark zusammen, da der Überlapp viel größer ist als zufällig erwartet).

---
### Offizielle Lösung
$P(A \cap B) = P(A) + P(B) - P(A \cup B) = 0.5 + 0.3 - 0.4 = 0.4$.<br>Prüfung auf Unabhängigkeit: $P(A)P(B) = 0.5 \cdot 0.3 = 0.15$.<br>Da $0.4 \neq 0.15$, sind sie nicht unabhängig.""",
        "en": r"""**Correct: (c)**

### Study.Smart Guide
**Step-by-Step:**
1.  **Find Intersection:**
    $P(A \cap B) = P(A) + P(B) - P(A \cup B) = 0.5 + 0.3 - 0.4 = 0.4$.
2.  **Test Independence:**
    Target Product: $0.5 \times 0.3 = 0.15$.
    Actual Intersection: $0.4$.
3.  **Conclusion:**
    $0.4 \neq 0.15 \Rightarrow$ Not independent.

---
### Official Solution
$P(A \cap B) = P(A) + P(B) - P(A \cup B) = 0.5 + 0.3 - 0.4 = 0.4$.<br>Check independence: $P(A)P(B) = 0.5 \cdot 0.3 = 0.15$.<br>Since $0.4 \neq 0.15$, they are not independent."""
    }
}

hs2023_mc2 = {
    "source": "HS 2023 Januar, MC #2 (4 Punkte)",
    "type": "mc",
    "question": {
        "de": r"Zwei unabhängige Zufallsvariablen $X_1$ und $X_2$ sind zwischen -1 und 1 stetig gleichverteilt ($U[-1, 1]$). Welche Aussage über den Mittelwert $\bar{X} = \frac{X_1 + X_2}{2}$ ist falsch?",
        "en": r"Two independent random variables $X_1$ and $X_2$ are uniformly distributed between -1 and 1 ($U[-1, 1]$). Which statement about the mean $\bar{X} = \frac{X_1 + X_2}{2}$ is false?"
    },
    "options": [
        r"$P(\bar{X} = 0) = 0$",
        r"$P(|\bar{X}| > 1) = 0$",
        r"$P(\bar{X} < -0.5) = 0.25$",
        r"$P(\bar{X} < 0) = 0.5$"
    ],
    "correct_idx": 2,
    "solution": {
        "de": r"""**Richtig: (c) ist FALSCH**

### Study.Smart Guide
**Intuition:**
Wenn man zwei Rechteck-Verteilungen (Uniform) addiert, entsteht eine **Dreiecksverteilung** (die Faltung von zwei Rechtecken).
Die Wahrscheinlichkeitsmasse sammelt sich in der Mitte (bei 0). Die Ränder ("Extreme Werte") werden seltener.
Daher ist die "linke Ecke" (kleiner als -0.5) viel kleiner als 25%. Bei einer Uniform-Verteilung wäre es 25%, aber hier ist es "dünner".

**Schritt-für-Schritt:**
1.  Support von $X_1+X_2$: $[-2, 2]$. Support von $\bar{X}$: $[-1, 1]$.
2.  Die Dichte von $\bar{X}$ ist ein Dreieck mit Spitze bei 0.
3.  Die Wahrscheinlichkeit $P(\bar{X} < -0.5)$ ist die Fläche des kleinen Dreiecks ganz links.
    Basis: $-1$ bis $-0.5$ (Länge 0.5). Höhe bei -0.5 ist 0.5.
    Fläche $\frac{1}{2} \cdot 0.5 \cdot 0.5 = 0.125$.
    Die Aussage behauptet 0.25. Das ist falsch.

---
### Offizielle Lösung
Die Summe zweier Gleichverteilungen ist eine Dreiecksverteilung (Irwin-Hall).<br>$P(\bar{X} < -0.5) = P(X_1 + X_2 < -1) = \frac{1}{2} \cdot 0.5 \cdot 0.5 = 0.125 \neq 0.25$.<br>(a) Wahr (stetig). (b) Wahr (Support $[-1, 1]$). (d) Wahr (Symmetrie).""",
        "en": r"""**Correct: (c) is FALSE**

### Study.Smart Guide
**Intuition:**
Sum of 2 Uniforms = Triangle Distribution.
Values concentrate near the mean (0). The "tails" are thinner than a uniform distribution box.
The area below -0.5 is the tip of the triangle, equal to $1/8 (12.5\%)$, not $25\%$.

---
### Official Solution
Sum of two uniforms is triangular.<br>$P(\bar{X} < -0.5) = P(X_1 + X_2 < -1) = \frac{1}{2} \cdot 0.5 \cdot 0.5 = 0.125 \neq 0.25$.<br>(a) True (continuous). (b) True (support). (d) True (symmetry)."""
    }
}

hs2023_mc3 = {
    "source": "HS 2023 Januar, MC #3 (4 Punkte)",
    "type": "mc",
    "question": {
        "de": r"Öltanker Kapazität 30.000 $m^3$. Max Last 27.040 Tonnen. Gewicht pro $m^3$ hat $\mu = 0.9$. Wahrscheinlichkeit Überladung = 0.2%. Welche Varianz $\sigma^2$ wurde angenommen?",
        "en": r"Oil tanker capacity 30,000 $m^3$. Max load 27,040 tons. Weight per $m^3$ has $\mu = 0.9$. Overload probability = 0.2%. What variance $\sigma^2$ was assumed?"
    },
    "options": [
        r"0.0064",
        r"0.0802",
        r"193.1477",
        r"Nicht genügend Informationen."
    ],
    "correct_idx": 0,
    "solution": {
        "de": r"""**Richtig: (a)**

### Study.Smart Guide
**Schritt-für-Schritt:**
1.  **Erwartetes Gesamtgewicht:**
    $E[S] = n \cdot \mu = 30'000 \cdot 0.9 = 27'000$ Tonnen.
2.  **Sicherheitsabstand ("Puffer"):**
    Erlaubt sind 27'040 Tonnen. Der Puffer ist 40 Tonnen.
3.  **Z-Score:**
    0.2% Überschreitungswahrscheinlichkeit entspricht einem Z-Score von ca. 2.88 (siehe Tabelle für 0.998).
4.  **Gleichung:**
    Puffer = Z $\cdot$ Standardabweichung(Gesamt)
    $40 = 2.88 \cdot \sqrt{n} \cdot \sigma$
    $40 = 2.88 \cdot 173.2 \cdot \sigma$
    $40 \approx 498.8 \cdot \sigma$
    $\sigma \approx 0.08$
5.  **Varianz:**
    $\sigma^2 = 0.08^2 = 0.0064$.

---
### Offizielle Lösung
Zentraler Grenzwertsatz: $S_{30000} \sim N(n\mu, n\sigma^2)$.<br>$P(S > 27040) = 0.002 \rightarrow P(Z > z) = 0.002 \rightarrow z \approx 2.878$.<br>$z = \frac{27040 - 27000}{\sqrt{30000}\sigma} \rightarrow 2.88 = \frac{40}{173.2 \sigma}$.<br>$\sigma \approx 0.08 \rightarrow \sigma^2 \approx 0.0064$.""",
        "en": r"""**Correct: (a)**

### Study.Smart Guide
**Step-by-Step:**
1.  $E[Total] = 27,000$. Limit = 27,040. Buffer = 40.
2.  Tail prob 0.002 corresponds to $Z \approx 2.88$.
3.  $Buffer = Z \cdot \sqrt{n} \cdot \sigma$.
    $40 = 2.88 \cdot 173.2 \cdot \sigma$.
    $\sigma \approx 0.08$.
4.  Variance $\sigma^2 = 0.0064$.

---
### Official Solution
CLT: $S_{30000} \sim N(n\mu, n\sigma^2)$.<br>$z \approx 2.878$ for 0.002 tail.<br>$z = \frac{40}{\sqrt{30000}\sigma} \rightarrow \sigma \approx 0.08 \rightarrow \sigma^2 \approx 0.0064$."""
    }
}

hs2023_mc4 = {
    "source": "HS 2023 Januar, MC #4 (4 Punkte)",
    "type": "mc",
    "question": {
        "de": r"Gegeben Dichtefunktion $f_Y(y) = 2y$ für $0 < y < 1$, sonst 0. Wie gross ist die Varianz von Y?",
        "en": r"Given PDF $f_Y(y) = 2y$ for $0 < y < 1$, else 0. What is the variance of Y?"
    },
    "options": [
        r"$\frac{1}{2}$",
        r"$\frac{1}{18}$",
        r"$\frac{1}{3}$",
        r"$\frac{1}{4}$"
    ],
    "correct_idx": 1,
    "solution": {
        "de": r"""**Richtig: (b)**

### Study.Smart Guide
**Rezept: Varianz-Verschiebungssatz**
$Var(Y) = E[Y^2] - (E[Y])^2$.

**Schritt-für-Schritt:**
1.  **Erstes Moment $E[Y]$:**
    $\int_0^1 y \cdot (2y) dy = \int_0^1 2y^2 dy = [\frac{2}{3}y^3]_0^1 = \frac{2}{3}$.
2.  **Zweites Moment $E[Y^2]$:**
    $\int_0^1 y^2 \cdot (2y) dy = \int_0^1 2y^3 dy = [\frac{2}{4}y^4]_0^1 = \frac{1}{2}$.
3.  **Kombinieren:**
    $Var = \frac{1}{2} - (\frac{2}{3})^2 = \frac{1}{2} - \frac{4}{9} = \frac{9}{18} - \frac{8}{18} = \frac{1}{18}$.

---
### Offizielle Lösung
$E[Y] = \int_0^1 2y^2 dy = [\frac{2}{3}y^3]_0^1 = \frac{2}{3}$.<br>$E[Y^2] = \int_0^1 2y^3 dy = [\frac{2}{4}y^4]_0^1 = \frac{1}{2}$.<br>$Var(Y) = \frac{1}{2} - (\frac{2}{3})^2 = \frac{1}{2} - \frac{4}{9} = \frac{9-8}{18} = \frac{1}{18}$.""",
        "en": r"""**Correct: (b)**

### Study.Smart Guide
**Step-by-Step:**
1.  $E[Y] = 2/3$.
2.  $E[Y^2] = 1/2$.
3.  $Var = 1/2 - (2/3)^2 = 1/18$.

---
### Official Solution
$E[Y] = 2/3$. $E[Y^2] = 1/2$.<br>$Var(Y) = 1/2 - 4/9 = 1/18$."""
    }
}

hs2023_mc5 = {
    "source": "HS 2023 Januar, MC #5 (4 Punkte)",
    "type": "mc",
    "question": {
        "de": r"Konfidenzintervall für Durchschnittliche Füllmenge. $Var=10$. Stichprobe ($n=10$): 501, 495, 503, 498, 500, 498, 497, 503, 497, 501. Gesucht: 95% KI (symmetrisch).",
        "en": r"Confidence Interval for mean fill amount. $Var=10$. Sample ($n=10$): 501, 495, 503, 498, 500, 498, 497, 503, 497, 501. Find symmetric 95% CI."
    },
    "options": [
        r"[493.10; 505.50]",
        r"[497.66; 500.95]",
        r"[494.08; 504.52]",
        r"[497.34; 501.26]"
    ],
    "correct_idx": 3,
    "solution": {
        "de": r"""**Richtig: (d)**

### Study.Smart Guide
**Schritt-für-Schritt:**
1.  **Mittelwert $\bar{x}$:** Summe / 10 = $499.3$.
2.  **Standardfehler:** Da Varianz **bekannt** ($Var=10$), nutzen wir $z$ (Normalverteilung), nicht $t$.
    $SE = \frac{\sqrt{10}}{\sqrt{10}} = 1$. (Zufall: $\sigma = \sqrt{10}$ und $n=10$).
3.  **Z-Score:** Für 95% ist $z = 1.96$.
4.  **Intervall:**
    $499.3 \pm 1.96 \cdot 1$
    $[497.34, 501.26]$

---
### Offizielle Lösung
Mittelwert $\bar{x} = 499.3$. $\sigma = \sqrt{10}$. $\alpha = 0.05$. $z_{0.975} = 1.96$.<br>$499.3 \pm 1.96 \cdot \frac{\sqrt{10}}{\sqrt{10}} = 499.3 \pm 1.96$.<br>$[497.34; 501.26]$.""",
        "en": r"""**Correct: (d)**

### Study.Smart Guide
**Calculation:**
1.  Sample Mean: $499.3$.
2.  Standard Error: $\sigma / \sqrt{n} = \sqrt{10} / \sqrt{10} = 1$.
3.  Margin: $1.96 \times 1 = 1.96$.
4.  CI: $499.3 \pm 1.96$.

---
### Official Solution
Mean $\bar{x} = 499.3$. $\sigma = \sqrt{10}$. $z_{0.975} = 1.96$.<br>$499.3 \pm 1.96 = [497.34; 501.26]$."""
    }
}

hs2023_mc6 = {
    "source": "HS 2023 Januar, MC #6 (4 Punkte)",
    "type": "mc",
    "question": {
        "de": r"Für welche Konstante $c$ ist $p(x) = \frac{c}{x!}$ für $x=0, 1, 2, ...$ eine Wahrscheinlichkeitsmassefunktion?",
        "en": r"For which constant $c$ is $p(x) = \frac{c}{x!}$ for $x=0, 1, 2, ...$ a probability mass function?"
    },
    "options": [
        r"$c = \frac{1}{\pi}$",
        r"$c = 1$",
        r"$c = \frac{1}{e}$",
        r"Jedes beliebige $c$"
    ],
    "correct_idx": 2,
    "solution": {
        "de": r"""**Richtig: (c)**

### Study.Smart Guide
**Intuition:**
Die Summe aller Wahrscheinlichkeiten muss 1 sein.
Die Reihe $\sum \frac{1}{x!}$ ist die berühmte Definition der Eulerschen Zahl $e$.

**Rechnung:**
1.  Summe bilden:
    $$\sum_{x=0}^{\infty} \frac{c}{x!} = c \sum_{x=0}^{\infty} \frac{1}{x!}$$
2.  Reihenwert einsetzen:
    $$c \cdot e$$
3.  Gleich 1 setzen:
    $$c \cdot e = 1 \Rightarrow c = \frac{1}{e}$$

---
### Offizielle Lösung
Summe muss 1 sein: $\sum_{x=0}^\infty \frac{c}{x!} = 1$.<br>Taylorreihe für $e^z$ bei $z=1$: $\sum \frac{1}{x!} = e$.<br>$c \cdot e = 1 \rightarrow c = 1/e$.""",
        "en": r"""**Correct: (c)**

### Study.Smart Guide
**Intuition:**
Recall Taylor Series for $e^x$ at $x=1$ is $\sum 1/k! = e$.
So the sum of unnormalized probabilities is $e$.
To make total probability 1, we must divide by $e$.

---
### Official Solution
Sum must be 1. $\sum \frac{c}{x!} = c \sum \frac{1}{x!} = c \cdot e = 1$.<br>$c = 1/e$."""
    }
}

hs2023_mc7 = {
    "source": "HS 2023 Januar, MC #7 (4 Punkte)",
    "type": "mc",
    "question": {
        "de": r"Punkte in Statistik Kurs: $\mu=20, \sigma^2=9$. Normalverteilt. Wahrscheinlichkeit, dass Student < 25 Punkte erreicht?",
        "en": r"Points in Stats course: $\mu=20, \sigma^2=9$. Normally distributed. Probability that student gets < 25 points?"
    },
    "options": [
        r"0.952",
        r"0.048",
        r"0.726",
        r"0.274"
    ],
    "correct_idx": 0,
    "solution": {
        "de": r"""**Richtig: (a)**

### Study.Smart Guide
**Schritt-für-Schritt:**
1.  Standardabweichung $\sigma = \sqrt{9} = 3$.
2.  Z-Transformation:
    $$Z = \frac{25 - 20}{3} = \frac{5}{3} \approx 1.67$$
3.  Nachschlagen in Tabelle (oder approximieren):
    Ein Wert von +1.67 liegt weit rechts (viel Masse links).
    $\Phi(1.67) \approx 0.952$.

---
### Offizielle Lösung
$X \sim N(20, 9)$. $\sigma=3$.<br>$P(X < 25) = P(Z < \frac{25-20}{3}) = P(Z < 1.666)$.<br>Tabelle 1.66: $\Phi(1.66) \approx 0.9515$.""",
        "en": r"""**Correct: (a)**

### Study.Smart Guide
**Calculation:**
$Z = (25-20)/3 = 1.67$.
Cumulative probability $\Phi(1.67) \approx 95.2\%$.

---
### Official Solution
$X \sim N(20, 9)$. $\sigma=3$.<br>$Z = \frac{5}{3} \approx 1.67$. $\Phi(1.67) \approx 0.952$."""
    }
}

hs2023_mc8 = {
    "source": "HS 2023 Januar, MC #8 (4 Punkte)",
    "type": "mc",
    "question": {
        "de": r"Seien A, B, C Ereignisse mit positiver Wahrscheinlichkeit. Welche Aussage ist wahr?",
        "en": r"Let A, B, C be events with positive probability. Which statement is true?"
    },
    "options": [
        r"Falls A perp B und B perp C, dann A perp C.",
        r"$P(A|B) > P(A) \iff P(A|B^c) < P(A)$",
        r"Wenn A, B disjunkt, dann unabhängig.",
        r"Keine der obigen."
    ],
    "correct_idx": 1, 
    "solution": {
        "de": r"""**Richtig: (b)**

### Study.Smart Guide
**Intuition:**
Denk an ein Gefäß mit Wasser (Wahrscheinlichkeit).
$P(A)$ ist der durchschnittliche Wasserstand.
$P(A|B)$ ist der Wasserstand im Bereich B.
Wenn der Wasserstand in B *höher* ist als der Durchschnitt ($P(A|B) > P(A)$), dann **muss** er im restlichen Bereich ($B^c$) zwangsläufig *niedriger* als der Durchschnitt sein, damit der Gesamtdurchschnitt erhalten bleibt.

**Gegenbeispiele für andere:**
*   (a) Ich bin unabh. von meinem Freund. Freund unabh. von seiner Mutter. Bin ich unabh. von seiner Mutter? Nicht zwingend.
*   (c) Disjunkt heißt: Wenn A eintritt, kann B nicht eintreten. Das ist maximale Abhängigkeit!

---
### Offizielle Lösung
Wenn B das Ereignis A wahrscheinlicher macht ($P(A|B) > P(A)$), dann muss das Nicht-Eintreten von B das Ereignis A unwahrscheinlicher machen ($P(A|B^c) < P(A)$).<br>(c) ist falsch (Disjunkt $\Rightarrow$ Abhängig, da $P(A \cap B)=0 \neq P(A)P(B)$).""",
        "en": r"""**Correct: (b)**

### Study.Smart Guide
**Intuition:**
Conservation of Probability.
If A is "concentrated" inside B, it must be "diluted" outside B to maintain the overall average $P(A)$.

---
### Official Solution
If B makes A more likely, then NOT B must make A less likely.<br>(c) False, disjoint implies dependent."""
    }
}

hs2023_mc9 = {
    "source": "HS 2023 Januar, MC #9 (4 Punkte)",
    "type": "mc",
    "question": {
        "de": r"Seien $X \sim N(4, 2)$ und $Y \sim N(0, 3)$. $E[XY] = E[X]E[Y]$. Sei $Z = 3 - 2X + 3Y$. Was ist $Cov(Y, Z)$?",
        "en": r"Let $X \sim N(4, 2)$ and $Y \sim N(0, 3)$. $E[XY] = E[X]E[Y]$. Let $Z = 3 - 2X + 3Y$. What is $Cov(Y, Z)$?"
    },
    "options": [
        r"27",
        r"9",
        r"12",
        r"Keine der obigen."
    ],
    "correct_idx": 1,
    "solution": {
        "de": r"""**Richtig: (b)**

### Study.Smart Guide
**Schritt-für-Schritt:**
1.  **Info auswerten:** $E[XY] = E[X]E[Y]$ bedeutet $Cov(X,Y) = 0$ (unkorreliert).
2.  **Linearität der Kovarianz:**
    $Cov(Y, Z) = Cov(Y, 3 - 2X + 3Y)$
    Konstanten ($3$) fallen weg. Faktor $-2$ und $3$ kann man rausziehen.
    $= -2 Cov(Y, X) + 3 Cov(Y, Y)$
3.  **Einsetzen:**
    $Cov(Y, X) = 0$.
    $Cov(Y, Y) = Var(Y) = 3$ (Achtung: Im Text steht $N(0,3)$, meist meint das bei Normalverteilung Notation $N(\mu, \sigma^2)$, also Varianz 3).
    $= 0 + 3 \cdot 3 = 9$.

---
### Offizielle Lösung
$E[XY]=E[X]E[Y] \Rightarrow Cov(X,Y)=0$.<br>$Cov(Y, 3 - 2X + 3Y) = Cov(Y, 3) - 2Cov(Y, X) + 3Cov(Y, Y)$.<br>$= 0 - 0 + 3Var(Y) = 3 \cdot 3 = 9$.""",
        "en": r"""**Correct: (b)**

### Study.Smart Guide
**Step-by-Step:**
1.  $X, Y$ are uncorrelated.
2.  Expand bilinear form:
    $Cov(Y, 3 - 2X + 3Y) = -2 Cov(Y,X) + 3 Cov(Y,Y)$.
3.  Substitute:
    $0 + 3 \cdot Var(Y)$.
    $3 \cdot 3 = 9$.

---
### Official Solution
$E[XY]=E[X]E[Y] \Rightarrow Cov(X,Y)=0$.<br>$Cov(Y, 3 - 2X + 3Y) = 3Var(Y) = 3 \cdot 3 = 9$."""
    }
}

hs2023_mc10 = {
    "source": "HS 2023 Januar, MC #10 (4 Punkte)",
    "type": "mc",
    "question": {
        "de": r"Welcher Schätzer für $E[X]$ ist erwartungstreu?",
        "en": r"Which estimator for $E[X]$ is unbiased?"
    },
    "options": [
        r"$\hat{\mu} = x_1$",
        r"$\hat{\mu} = \frac{1}{n-1} \sum x_i$",
        r"$\hat{\mu} = \frac{x_1 + x_3 + x_n}{4}$",
        r"Keiner."
    ],
    "correct_idx": 0,
    "solution": {
        "de": r"""**Richtig: (a)**

### Study.Smart Guide
**Die Falle:**
Du bist wahrscheinlich gewohnt, dass man durch $n-1$ teilt (bei der *Varianz*).
Hier geht es aber um den **Erwartungswert** (Mittelwert).
Ein einzelner Datenpunkt $x_1$ ist zwar eine sehr schlechte ("wackelige") Schätzung, aber er ist im Durchschnitt korrekt (unbiased). $E[x_1] = \mu$.
Die Option (b) teilt die Summe von $n$ Werten durch $n-1$. Das wäre systematisch zu groß ($\frac{n}{n-1} \mu$).

---
### Offizielle Lösung
$E[x_1] = E[X] = \mu$. Ein einzelner Wert ist erwartungstreu (aber ineffizient).<br>(b) Summe durch $n-1$: $E = \frac{n}{n-1}\mu \neq \mu$.<br>(c) Summe von 3 Werten durch 4: $E = \frac{3}{4}\mu$.""",
        "en": r"""**Correct: (a)**

### Study.Smart Guide
**The Trap:**
Don't confuse with variance estimation ($1/(n-1)$).
For the mean:
$E[X_1] = \mu$. (Unbiased!)
Option (b) sums $n$ items but divides by $n-1$, resulting in $\frac{n}{n-1}\mu$ (Biased).

---
### Official Solution
$E[x_1] = \mu$. Unbiased.<br>(b) is biased (factor $n/(n-1)$). (c) is biased ($3/4 \mu$)."""
    }
}

hs2023_mc11 = {
    "source": "HS 2023 Januar, MC #11 (4 Punkte)",
    "type": "mc",
    "question": {
        "de": r"Würfelspiel: Auszahlung=Augenzahl. Bei 4,5,6 darf man additiv neu würfeln. Bei 1,2,3 Ende. Erwarteter Gewinn?",
        "en": r"Dice game: Payoff=value. If 4,5,6 roll again (additiv). If 1,2,3 end. Expected payoff?"
    },
    "options": [
        r"3.5",
        r"5",
        r"6",
        r"7"
    ],
    "correct_idx": 3,
    "solution": {
        "de": r"""**Richtig: (d)**

### Study.Smart Guide
**Strategie: Rekursion**
Der Erwartungswert $E$ setzt sich zusammen aus dem aktuellen Wurf (Mittelwert 3.5) plus - mit 50% Wahrscheinlichkeit - dem zukünftigen Wert des gleichen Spiels ($E$).
$E = 3.5 + 0.5 \cdot E$.

**Warum?**
Wenn wir 1,2,3 würfeln (Schnitt 2), ist Schluss.
Wenn wir 4,5,6 würfeln (Schnitt 5), kriegen wir die 5 PLUS ein neues Spiel.
$(0.5 \cdot 2) + 0.5 \cdot (5 + E) = 1 + 2.5 + 0.5E = 3.5 + 0.5E$.
Auflösen: $0.5E = 3.5 \Rightarrow E = 7$.

---
### Offizielle Lösung
$E = \frac{1}{6}(1+2+3) + \frac{1}{6}( (4+E) + (5+E) + (6+E) )$.<br>$E = \frac{6}{6} + \frac{15}{6} + \frac{3E}{6} = 1 + 2.5 + 0.5E = 3.5 + 0.5E$.<br>$0.5E = 3.5 \Rightarrow E = 7$.""",
        "en": r"""**Correct: (d)**

### Study.Smart Guide
**Recursive Equation:**
Expected value of one roll is 3.5.
Prob of rolling again is 0.5.
$E = 3.5 + 0.5 E$.
$0.5 E = 3.5 \implies E = 7$.

---
### Official Solution
Recursive expectation: $E = 0.5 \cdot 2 + 0.5 \cdot (5 + E)$. (Avg of 1,2,3 is 2; Avg of 4,5,6 is 5).<br>Wait, calculation: Avg(1..6) = 3.5.<br>$E = 3.5 + P(roll again) \cdot E = 3.5 + 0.5E \rightarrow E=7$."""
    }
}

hs2023_mc12 = {
    "source": "HS 2023 Januar, MC #12 (4 Punkte)",
    "type": "mc",
    "question": {
        "de": r"Casino. 100 Automaten. Gewinnchance $p=0.2$. An jedem Automaten 5 Spiele. Wahrscheinlichkeit, dass an mindestens 4 Automaten mehr als 2 mal gewonnen wird?",
        "en": r"Casino. 100 slots. Win chance $p=0.2$. 5 games per slot. Probability of winning > 2 times on at least 4 slots?"
    },
    "options": [
        r"0.0579",
        r"0.8372",
        r"0.9421",
        r"0.1628"
    ],
    "correct_idx": 1,
    "solution": {
        "de": r"""**Richtig: (b)**

### Study.Smart Guide
**Strategie: "Problem im Problem"**
1.  **Mikro-Level:** Wie hoch ist die Wkt, an *einem* Automaten "erfolgreich" zu sein ( > 2 Siege bei 5 Spielen)?
    $X \sim B(5, 0.2)$.
    $P(X > 2) = P(3) + P(4) + P(5)$.
    $\approx 0.0512 + 0.0064 + 0.0003 = 0.0579$.
    Nennen wir das $p_{neu}$.
2.  **Makro-Level:** Nun haben wir 100 Automaten. Ein Automat ist "Gewinner" mit $p_{neu} = 0.0579$.
    $Y \sim B(100, 0.0579)$.
    Gesucht: $P(Y \ge 4)$.
    Das ist $1 - P(Y \le 3) = 1 - (P(0)+P(1)+P(2)+P(3))$.
    Ergibt ca. $83.7\%$.

---
### Offizielle Lösung
Zuerst P(Win > 2) für einen Automaten ($B(5, 0.2)$).<br>$P(X>2) = 1 - P(\le 2) \approx 0.05792$.<br>Nun $Y \sim B(100, 0.05792)$. Gesucht $P(Y \ge 4) = 1 - P(Y \le 3)$.<br>Resultat $\approx 0.8372$.""",
        "en": r"""**Correct: (b)**

### Study.Smart Guide
**Step-by-Step:**
1.  **Inner Probability:** $P(Bin(5, 0.2) > 2) \approx 0.0579$.
2.  **Outer Probability:** $P(Bin(100, 0.0579) \ge 4)$.
    Using normal approx or cumulative sum:
    $1 - P(\le 3) \approx 0.8372$.

---
### Official Solution
First $P(Win > 2)$ per slot ($B(5, 0.2)$). $p' \approx 0.0579$.<br>Then $Y \sim B(100, p')$. $P(Y \ge 4) = 1 - P(Y \le 3) \approx 0.8372$."""
    }
}

# ------------------------------------------------------------------
# PROBLEMS
# ------------------------------------------------------------------

hs2023_prob1 = {
    "source": "HS 2023 Januar, Problem 1 (12 Punkte)",
    "type": "problem",
    "question": {
        "de": r"**Teil 1A:** Ordnen Sie Verteilungen Diagrammen zu.<br>F1: Poisson(50), n=200<br>F2: Uniform[14, 26], n=200<br>F3: Normal(20, 4), n=200<br>F4: Binomial(200, 0.2), n=200<br><br>**Teil 1B:** Höchstgeschwindigkeit von 10 Autos: 180, 195, 240, 185, 230, 300, 290, 180, 235, 280.<br>1. Berechne Mittelwert, Modus, IQR.<br>2. Zeichne Histogramm.",
        "en": r"**Part 1A:** Match distributions to diagrams.<br>F1: Poisson(50)<br>F2: Uniform[14, 26]<br>F3: Normal(20, 4)<br>F4: Binomial(200, 0.2)<br><br>**Part 1B:** Top speeds of 10 cars: 180, 195, 240, 185, 230, 300, 290, 180, 235, 280.<br>1. Mean, Mode, IQR.<br>2. Histogram."
    },
    "solution": {
        "de": r"""### Study.Smart Guide
**Intuition 1A:**
*   **F1 Poisson(50):** Mittelwert bei 50. Schau auf die x-Achse.
*   **F4 Binomial(200, 0.2):** Mittelwert $n \cdot p = 40$. x-Achse um 40.
*   **F3 Normal(20, 4):** Glocke um 20.
*   **F2 Uniform:** Flacher Kasten.

**(Hinweis: Achte primär auf die Lage (Mittelwert/x-Achse), um die distributions zu unterscheiden!)**

**Lösung 1B:**
Daten sortiert: 180, 180, 185, 195, 230, 235, 240, 280, 290, 300.
*   Mittelwert: 231.5.
*   Q1 (2.75 pos $\approx$ 3. Wert): 185.
*   Q3 (8.25 pos $\approx$ 8. Wert): 280.
*   IQR: $280 - 185 = 95$.

---
### Offizielle Lösung
**1A:** F1:d, F2:b, F3:a, F4:c.<br>**1B:** Mean = 231.5. Mode = 180. Sorted: 180, 180, 185, 195, 230, 235, 240, 280, 290, 300.<br>Q3-Q1 = 280-185 = 95.""",
        "en": r"""### Study.Smart Guide
**Analysis:**
Identify distributions by their Mean (Center point on x-axis).
Poisson(50) -> x=50.
Binom(200, 0.2) -> x=40.
Normal(20) -> x=20.

---
### Official Solution
**1A:** F1:d, F2:b, F3:a, F4:c.<br>**1B:** Mean = 231.5. Mode = 180. IQR = 95."""
    }
}

hs2023_prob2 = {
    "source": "HS 2023 Januar, Problem 2 (15 Punkte)",
    "type": "problem",
    "question": {
        "de": r"Nachhaltigkeit und Kredite. A: Kredit bewilligt. B: Grüner Sachbearbeiter. $P(B)=0.5$. $P(A)=0.7$. $P(A|B)=0.8$.<br>1. Kontingenztabelle ausfüllen.<br>2. Berechne $P(A \cap B)$, $P(A|B)$, $P(A \cup B)$.<br>3. Sind A und B unabhängig?<br>4. Interview mit 8 Sachbearbeitern. Wahrscheinlichkeit, dass nur der erste 'Braun' ist? Wahrscheinlichkeit 4 Grün, 4 Braun?",
        "en": r"Sustainability and Loans. A: Loan approved. B: Green officer. $P(B)=0.5$. $P(A)=0.7$. $P(A|B)=0.8$.<br>1. Fill contingency table.<br>2. Calc $P(A \cap B)$, $P(A|B)$, $P(A \cup B)$.<br>3. Independence?<br>4. Interview 8 officers. Prob only first is Brown? Prob 4 Green, 4 Brown?"
    },
    "solution": {
        "de": r"""### Study.Smart Guide
**Schritt-für-Schritt:**
1.  **Schnitt:** $P(A \cap B) = P(A|B) \cdot P(B) = 0.8 \cdot 0.5 = 0.4$.
    (40% der Fälle sind "Bewilligt UND Grün").
2.  **Tabelle füllen:**
    Wir wissen: Zeilensumme $P(A)=0.7$, Spaltensumme $P(B)=0.5$.
    Zelle $(A, B) = 0.4$.
    Rest ergibt sich durch Subtraktion (z.B. $P(A, B^c) = 0.7 - 0.4 = 0.3$).
3.  **Unabhängigkeit:**
    Vergleich $P(A|B) = 0.8$ mit $P(A) = 0.7$.
    Grüne bewilligen mehr. Abhängig.

---
### Offizielle Lösung
1. Tabelle: $P(A \cap B) = 0.4$. Rest hergeleitet.<br>2. $P(A \cap B) = 0.4$. $P(A|B) = 0.8 \neq 0.7$. $P(A \cup B) = 0.7 + 0.5 - 0.4 = 0.8$.<br>3. Abhängig.<br>4. a) $0.5^8 \approx 0.0039$. b) $\binom{8}{4} 0.5^8 = 70/256 \approx 0.273$.""",
        "en": r"""### Study.Smart Guide
**Analysis:**
1.  Intersection: $0.8 \times 0.5 = 0.4$.
2.  Independence check: $P(A|B) \neq P(A)$. (0.8 vs 0.7).
3.  Binomial part: 8 trials, p=0.5. Sequence "BGGGGGGG" has prob $0.5^8$. "4 of 8" uses $\binom{8}{4}$.

---
### Official Solution
1. Table derived from intersection 0.4.<br>2. Intersection 0.4, Union 0.8.<br>3. Dependent.<br>4. a) $0.5^8$. b) $\binom{8}{4} 0.5^8$."""
    }
}

hs2023_prob3 = {
    "source": "HS 2023 Januar, Problem 3 (15 Punkte)",
    "type": "problem",
    "question": {
        "de": r"Schweinerennen. Max V. braucht 10s. 4 andere Schweine $Y \sim N(13, 2.5^2)$.<br>1. $P(\text{Max V. gewinnt})$.<br>2. $P(\text{Max V. mindestens Dritter})$.<br>3. CLT Approximation für N Rennen.",
        "en": r"Pig racing. Max V. takes 10s. 4 other pigs $Y \sim N(13, 2.5^2)$.<br>1. $P(\text{Max V. wins})$.<br>2. $P(\text{Max V. at least 3rd})$.<br>3. CLT Approximation."
    },
    "solution": {
        "de": r"""### Study.Smart Guide
**Analyse:**
Max gewinnt, wenn seine Zeit (10) *kleiner* ist als die der anderen ($Y$).
Da alle anderen Schweine unabhängig laufen, müssen wir die Wahrscheinlichkeit berechnen, dass *ein* Schwein langsamer als 10s ist, und das dann hoch 4 nehmen.
Moment... $Y \sim N(13, 2.5)$. 13 ist langsam (viel Zeit). 10 ist schnell.
Wir suchen $P(Y > 10)$. (Schwein Y braucht länger als Max).

**Schritt-für-Schritt:**
1.  Z-Score für Y=10:
    $Z = \frac{10 - 13}{2.5} = -1.2$.
2.  $P(Y > 10) = P(Z > -1.2) = P(Z < 1.2) \approx 0.885$.
3.  Max gewinnt gegen alle 4:
    $0.885^4 \approx 0.613$.

---
### Offizielle Lösung
1. $P(Y > 10) = P(Z > -1.2) = 0.8849$. Max gewinnt wenn alle 4 langsamer. $0.8849^4 = 0.6132$.<br>2. $X$: Platzierung. $P(X \le 3)$. Binomial Ansatz.<br>3. CLT für $N \ge 4$.""",
        "en": r"""### Study.Smart Guide
**Analysis:**
Max Time = 10.
Others Mean = 13.
Max wins if Others > 10.
$P(Other > 10) = P(Z > -1.2) \approx 0.885$.
Win Prob = $0.885^4$.

---
### Official Solution
1. $P(Y > 10) = 0.8849$. All 4 slower: $0.6132$.<br>2. Binomial sum for placement.<br>3. CLT calculation yields $N=4$ (approx)."""
    }
}

hs2023_prob4 = {
    "source": "HS 2023 Januar, Problem 4 (15 Punkte)",
    "type": "problem",
    "question": {
        "de": r"Vektor $(X,Y)$. $f_X(x) = (4a e^{ax})^{-1}$ für $x \ge 0$. <br>1. Bestimme $a$.<br>2. Bestimme $b$ aus $F_Y$.<br>3. Gemeinsame Dichte.<br>4. Erwartungswert $Z = XY$.",
        "en": r"Vector $(X,Y)$. $f_X(x) = (4a e^{ax})^{-1}$. <br>1. Find $a$.<br>2. Find $b$ from $F_Y$.<br>3. Joint density.<br>4. Expectation $Z = XY$."
    },
    "solution": {
        "de": r"""### Study.Smart Guide
**Lösungsskizze:**
1.  Dichte muss integrieren zu 1.
    Achtung: $(4a e^{ax})^{-1} = \frac{1}{4a} e^{-ax}$.
    Das ist eine Exponentialverteilung mit "Rate" a. Aber der Vorfaktor stimmt nicht ganz.
    Normal: $a e^{-ax}$. Wir haben $\frac{1}{4a} e^{-ax}$.
    Damit Integral 1 ist, muss $\frac{1}{4a} \cdot \frac{1}{a} = 1$ sein? Nein.
    $\int \frac{1}{4a} e^{-ax} dx = \frac{1}{4a} [\frac{-1}{a}e^{-ax}] = \frac{1}{4a^2}$.
    Setze $1/(4a^2) = 1 \Rightarrow 4a^2 = 1 \Rightarrow a = 1/2$.

4.  $E[XY]$ bei Unabhängigkeit ist $E[X]E[Y]$.
    $E[X]$ (Exp mit a=0.5) = $1/a = 2$.
    $E[Y]$ (laut Lösung 3) = 3.
    Produkt = 6.

---
### Offizielle Lösung
1. $a = 1/2$.<br>2. $b = 6$.<br>3. $f_{X,Y} = f_X f_Y$ (Unabhängigkeit).<br>4. $E[XY] = E[X]E[Y] = 2 \cdot 3 = 6$.""",
        "en": r"""### Study.Smart Guide
**Step-by-Step:**
1.  Integrate PDF: Result is $1/(4a^2)$. Set to 1. $a=1/2$.
2.  Independence assumed (vector components usually imply joint structure analysis).
3.  $E[XY] = E[X]E[Y] = 2 \times 3 = 6$.

---
### Official Solution
1. $a = 1/2$.<br>2. $b = 6$.<br>3. Product of marginals.<br>4. $E[XY] = 6$."""
    }
}

hs2023_prob5 = {
    "source": "HS 2023 Januar, Problem 5 (15 Punkte)",
    "type": "problem",
    "question": {
        "de": r"5A: $f(x) = \frac{2x}{\lambda^2} e^{-(x/\lambda)^2}$. MLE für $\lambda$.<br>5B: Diskrete Verteilung $1/\theta$. Daten: 1, 4, 3, 4, 2.<br>1. Momentenschätzer für $\theta$.<br>2. MLE für $\theta$.<br>3. Werte berechnen.",
        "en": r"5A: MLE for $\lambda$ given density.<br>5B: Discrete uniform $1/\theta$. Data: 1, 4, 3, 4, 2.<br>1. MME for $\theta$.<br>2. MLE for $\theta$.<br>3. Calculate values."
    },
    "solution": {
        "de": r"""### Study.Smart Guide
**5B (Discrete Uniform 1..theta):**
Dies ist das "German Tank Problem".
*   **MLE:** Wie beim Würfel. Wenn ich eine "4" sehe, muss der Würfel mindestens 4 Seiten haben.
    Um die Wahrscheinlichkeit ($1/\theta$) zu maximieren, wähle ich $\theta$ so klein wie möglich.
    $\hat{\theta}_{MLE} = \max(x_i) = 4$.
*   **MME (Momente):** Der theoretische Mittelwert eines Würfels mit $\theta$ Seiten ist $(\theta+1)/2$.
    Setze $(\theta+1)/2 = \bar{X}$.
    $\theta + 1 = 2\bar{X} \Rightarrow \theta = 2\bar{X} - 1$.
    Daten: 1,4,3,4,2. Mittelwert 2.8.
    $\hat{\theta} = 2(2.8) - 1 = 5.6 - 1 = 4.6$.

---
### Offizielle Lösung
5A: $\hat{\lambda} = \sqrt{\frac{1}{n} \sum x_i^2}$.<br>5B-1: $\hat{\theta}_{MME} = 2\bar{X} - 1$.<br>5B-2: $\hat{\theta}_{MLE} = \max(x_i)$.<br>5B-3: MME = 4.6. MLE = 4.""",
        "en": r"""### Study.Smart Guide
**Intuition 5B:**
Standard "German Tank Problem".
*   **MLE:** Max observed value (4).
*   **MME:** Based on mean. Mean of $1..\theta$ is approx $\theta/2$. So $\theta \approx 2 \times Mean$.
    Exact: $2\bar{X} - 1 = 4.6$.

---
### Official Solution
5A: $\hat{\lambda} = \sqrt{\frac{1}{n} \sum x_i^2}$.<br>5B-1: $\hat{\theta}_{MME} = 2\bar{X} - 1$.<br>5B-2: MLE is max.<br>Result: MME=4.6, MLE=4."""
    }
}
