
# Übung 3 Exam Staging File
# Content extracted from:
# - Uebung_3.pdf (questions)
# - ML_Uebung_3.pdf (solutions)
# Dual-Mode: Study.Smart Guide + Official Solution

# ------------------------------------------------------------------
# MULTIPLE CHOICE
# ------------------------------------------------------------------

uebung3_mc1 = {
    "source": "Übung 3, MC #1",
    "type": "mc",
    "question": {
        "de": r"Die Kovarianz:",
        "en": r"Covariance:"
    },
    "options": [
        r"misst nur die Stärke des Zusammenhangs zwischen zwei Variablen.",
        r"misst nur die Richtung des Zusammenhangs zwischen zwei Variablen.",
        r"misst die Stärke und die Richtung des Zusammenhangs zwischen zwei Variablen.",
        r"hat keinerlei Aussagekraft über den Zusammenhang zwischen zwei Variablen.",
        r"nimmt immer Werte zwischen -1 und +1 an."
    ],
    "correct_idx": 1, 
    "solution": {
        "de": r"""**Richtig: (b)**

### Study.Smart Guide
**Intuition:**
Die Kovarianz ist ein "rohes" Maß.
*   Wenn sie positiv ist, geht der Trend nach oben (Richtung).
*   Wenn sie negativ ist, geht der Trend nach unten.
*   Aber der **Wert** selbst ist schwer zu interpretieren, da er von der Maßeinheit abhängt (z.B. Meter vs. Zentimeter). Eine Kovarianz von 1000 kann "wenig" sein (in Millimetern) oder "viel" (in Kilometern). Daher misst sie nicht verlässlich die "Stärke". Dafür braucht man die Korrelation.

---
### Offizielle Lösung
Die Kovarianz ist maßstabsabhängig und gibt daher nur die Richtung (Positiv/Negativ) an, nicht die Stärke.""",
        "en": r"""**Correct: (b)**

### Study.Smart Guide
**Intuition:**
Covariance is scale-dependent (e.g., changing meters to cm changes covariance by 100x).
So the magnitude tells us little.
Only the sign (+/-) is reliable (Direction).

---
### Official Solution
Covariance indicates direction but generally not strength (scale dependent)."""
    }
}

uebung3_mc2 = {
    "source": "Übung 3, MC #2",
    "type": "mc",
    "question": {
        "de": r"Der Korrelationskoeffizient $\rho$:",
        "en": r"Correlation coefficient $\rho$:"
    },
    "options": [
        r"misst nur die Stärke des Zusammenhangs zwischen zwei Variablen.",
        r"misst nur die Richtung des Zusammenhangs zwischen zwei Variablen.",
        r"misst die Stärke und die Richtung des linearen Zusammenhangs zwischen zwei Variablen.",
        r"hat keinerlei Aussagekraft über den Zusammenhang zwischen zwei Variablen.",
        r"nimmt immer Werte zwischen -1 und +1 an."
    ],
    "correct_idx": 2, # Also (e) is true
    "solution": {
        "de": r"""**Richtig: (c), (e)**

### Study.Smart Guide
**Definition:**
Die Korrelation ist die "normierte Kovarianz".
1.  Sie liegt immer zwischen **-1 und +1** (Aussage e).
2.  Sie misst exakt, wie gut die Punkte auf einer **Geraden** liegen (Stärke) und ob die Gerade steigt oder fällt (Richtung) (Aussage c).

---
### Offizielle Lösung
Misst Stärke und Richtung von *linearen* Zusammenhängen (c). Ist normiert auf $[-1, 1]$ (e).""",
        "en": r"""**Correct: (c), (e)**

### Study.Smart Guide
**Definition:**
Correlation is normalized covariance.
Range $[-1, 1]$. Measures linear fit and direction.

---
### Official Solution
Measures linear relationship strength/direction (c). Normalized to [-1, 1] (e)."""
    }
}

uebung3_mc3 = {
    "source": "Übung 3, MC #3",
    "type": "mc",
    "question": {
        "de": r"Zwei Variablen sind unabhängig, wenn:",
        "en": r"Two variables are independent if:"
    },
    "options": [
        r"der Korrelationskoeffizient $\rho = 0$ ist.",
        r"das Produkt der Randverteilungen und die gemeinsame Wahrscheinlichkeitsverteilung übereinstimmen.",
        r"die Summe der Randverteilungen und die gemeinsame Wahrscheinlichkeitsverteilung übereinstimmen.",
        r"die Kovarianz Cov = 1 ist.",
        r"die Kovarianz Cov = 0 ist."
    ],
    "correct_idx": 1,
    "solution": {
        "de": r"""**Richtig: (b)**

### Study.Smart Guide
**Definition:**
Unabhängigkeit bedeutet: $P(X \cap Y) = P(X) \cdot P(Y)$.
Dichte-Schreibweise: $f(x, y) = f_X(x) \cdot f_Y(y)$.
(a) und (e) sind falsch, weil Unkorreliertheit ($\rho=0$) schwächer ist als Unabhängigkeit. (Man kann unkorreliert, aber abhängig sein).

---
### Offizielle Lösung
Definition der Unabhängigkeit: $f(x,y) = f_X(x) \cdot f_Y(y)$. Unkorreliertheit (a, e) folgt aus Unabhängigkeit, aber nicht umgekehrt.""",
        "en": r"""**Correct: (b)**

### Study.Smart Guide
**Definition:**
Joint PDF = Product of Marginal PDFs.
$f(x,y) = f(x)f(y)$.

---
### Official Solution
Definition: joint pdf equals product of marginals."""
    }
}

uebung3_mc4 = {
    "source": "Übung 3, MC #4",
    "type": "mc",
    "question": {
        "de": r"Die Kovarianz wird errechnet mit:",
        "en": r"Covariance is calculated as:"
    },
    "options": [
        r"$Cov(X, Y) = E[XY] - E[X]E[Y]$",
        r"$Cov(X, Y) = E[XY] - E[X^2]E[Y^2]$",
        r"$Cov(X, Y) = E[X^2Y^2] - E[X]E[Y]$",
        r"$Cov(X, Y) = E[X^2Y^2] - E[X^2]E[Y^2]$",
        r"$Cov(X, Y) = E[XY]^2 - E[X]E[Y]$"
    ],
    "correct_idx": 0,
    "solution": {
        "de": r"""**Richtig: (a)**

### Study.Smart Guide
**Merkregel: Verschiebungssatz**
Dies ist die Standardformel ("Königsformel") für die schnelle Berechnung der Kovarianz.
$Cov = E[XY] - E[X] \cdot E[Y]$.

---
### Offizielle Lösung
Verschiebungssatz für Kovarianz.""",
        "en": r"""**Correct: (a)**

### Study.Smart Guide
**Formula:**
Computational formula for covariance: $E[XY] - \mu_X \mu_Y$.

---
### Official Solution
Standard formula."""
    }
}

uebung3_mc5 = {
    "source": "Übung 3, MC #5",
    "type": "mc",
    "question": {
        "de": r"Welche Aussagen sind wahr?",
        "en": r"Which statements are true?"
    },
    "options": [
        r"$X, Y$ unabhängig $\implies X, Y$ unkorreliert.",
        r"$X, Y$ unkorreliert $\implies X, Y$ unabhängig.",
        r"$E[X+Y] = E[X] + E[Y]$.",
        r"$V(X+Y) = V(X) + V(Y)$.",
        r"$\rho_{XY} = -1$ bedeutet: Je größer X desto kleiner Y."
    ],
    "correct_idx": 0, # Solution marks (a), (c), (e), (f option in solution text)
    "solution": {
        "de": r"""**Richtig: (a), (c), (e)**

### Study.Smart Guide
**Faktencheck:**
*   (a) **Richtig.** Unabhängigkeit ist die stärkste Form. Wenn unabhängig, dann sicher auch linear unkorreliert.
*   (c) **Richtig.** Linearität des Erwartungswerts gilt **IMMER**, egal ob unabhängig oder nicht!
*   (e) **Richtig.** Korrelation -1 ist eine fallende Gerade.
*   (b) Falsch. Unkorreliert heißt nur "keine Gerade", es könnte aber eine Parabel ($Y=X^2$) sein (abhängig).
*   (d) Falsch. Gleichung von Bienaymé gilt nur bei Unabhängigkeit (oder Unkorreliertheit). Sonst fehlt der Cov-Term $2Cov(X,Y)$.

---
### Offizielle Lösung
(a) Unabhängigkeit impliziert Unkorreliertheit. (c) Linearität des Erwartungswerts gilt immer. (e) Perfekter negativer linearer Zshg.<br>(b) falsch (Gegenbeispiele). (d) falsch (nur bei Unkorreliertheit).""",
        "en": r"""**Correct: (a), (c), (e)**

### Study.Smart Guide
**Checks:**
*   (a) True. Indep $\to$ Uncorr.
*   (c) True. $E$ is always linear.
*   (e) True. Perfect negative linear slope.

---
### Official Solution
Indep implies uncorr. Expectation is linear. Rho=-1 is perfect neg correlation."""
    }
}

uebung3_mc6 = {
    "source": "Übung 3, MC #6",
    "type": "mc",
    "question": {
        "de": r"Wann gilt $E[XY] = E[X]E[Y]$?",
        "en": r"When does $E[XY] = E[X]E[Y]$ hold?"
    },
    "options": [
        r"Immer.",
        r"Nie.",
        r"Falls X und Y unkorreliert sind.",
        r"Falls X und Y unabhängig sind.",
        r"Falls $E[X] = E[Y] = 0$."
    ],
    "correct_idx": 2, # Solution marks (c) and (d)
    "solution": {
        "de": r"""**Richtig: (c), (d)**

### Study.Smart Guide
**Logik:**
Die Gleichung umgeformt ist genau die Definition von Kovarianz 0:
$Cov = E[XY] - E[X]E[Y] = 0 \iff E[XY] = E[X]E[Y]$.
Das heißt "Unkorreliertheit" (c).
Da Unabhängigkeit (d) immer Unkorreliertheit impliziert, gilt es auch dann.

---
### Offizielle Lösung
Dies ist die Definition von Unkorreliertheit ($Cov = E[XY] - E[X]E[Y] = 0$). Unabhängigkeit impliziert Unkorreliertheit, also auch (d).""",
        "en": r"""**Correct: (c), (d)**

### Study.Smart Guide
**Logic:**
This equation is equivalent to Covariance = 0.
So (c) is correct by definition.
(d) is correct because Independence implies Uncorrelatedness.

---
### Official Solution
Definition of uncorrelated. Independence implies it."""
    }
}

uebung3_mc7 = {
    "source": "Übung 3, MC #7",
    "type": "mc",
    "question": {
        "de": r"Zuordnung Korrelationskoeffizienten zu Streudiagrammen (Visuell).",
        "en": r"Matching correlation coeffs to scatterplots."
    },
    "options": [
        r"Oben links: 0.6, Oben rechts: 0.9, Unten links: -0.7, Unten rechts: 0",
        r"Oben links: 0.9, Oben rechts: 0.6, Unten links: 0, Unten rechts: -0.7",
        r"Oben links: -0.7, Oben rechts: 0, Unten links: 0.6, Unten rechts: 0.9",
        r"Oben links: 0, Oben rechts: -0.7, Unten links: 0.9, Unten rechts: 0.6"
    ],
    "correct_idx": 0,
    "solution": {
        "de": r"""**Richtig: (a)**

### Study.Smart Guide
**Visuelle Schule:**
*   **0.9:** Eine sehr "dünne", deutliche Wolke bergauf. (Oben Rechts).
*   **0.6:** Eine "dickere" Wolke bergauf. (Oben Links).
*   **-0.7:** Eine Wolke bergab. (Unten Links).
*   **0:** Eine runde Punktwolke ("Schrotflinte"). (Unten Rechts).

---
### Offizielle Lösung
OL (leicht positiv): 0.6. OR (stark positiv): 0.9. UL (negativ): -0.7. UR (kein Trend): 0.""",
        "en": r"""**Correct: (a)**

### Study.Smart Guide
**Visual Inspection:**
*   Strong pos slope: 0.9.
*   Weak pos slope: 0.6.
*   Neg slope: -0.7.
*   No slope: 0.

---
### Official Solution
Visual inspection."""
    }
}

uebung3_mc8 = {
    "source": "Übung 3, MC #8",
    "type": "mc",
    "question": {
        "de": r"X = Würfelwurf, Y = Münzwurf ('Kopf'). $P(X > 3 | Y = \text{'Kopf'})$?",
        "en": r"X = Die, Y = Coin ('Head'). $P(X > 3 | Y = \text{'Head'})$?"
    },
    "options": [
        r"1/3",
        r"1/2",
        r"2/3",
        r"0",
        r"1"
    ],
    "correct_idx": 1,
    "solution": {
        "de": r"""**Richtig: (b)**

### Study.Smart Guide
**Die Falle:**
Lass dich nicht von Y verwirren!
Es sollte klar sein, dass ein Münzwurf einen Würfel nicht physikalisch beeinflusst.
Sie sind **unabhängig**.
Daher: $P(X>3 | Y) = P(X>3)$.
Beim Würfel sind (4, 5, 6) größer als 3. Das sind 3 von 6 Möglichkeiten.
$3/6 = 1/2$.

---
### Offizielle Lösung
X und Y sind unabhängig. Der Münzwurf beeinflusst den Würfel nicht.<br>$P(X>3) = P(\{4,5,6\}) = 3/6 = 1/2$.""",
        "en": r"""**Correct: (b)**

### Study.Smart Guide
**Intuition:**
Independent events. The coin tells us nothing about the die.
$P(X>3) = 3/6 = 0.5$.

---
### Official Solution
Independent events. Prob is 1/2."""
    }
}

uebung3_mc9 = {
    "source": "Übung 3, MC #9",
    "type": "mc",
    "question": {
        "de": r"Urne (1-5). Ziehen ohne Zurücklegen. X=1. Ziehung, Y=2. Ziehung. Was gilt?",
        "en": r"Urn (1-5). Draw w/o replacement. X=1st, Y=2nd. What holds?"
    },
    "options": [
        r"X und Y sind unabhängig.",
        r"Cov(X, Y) = 0.",
        r"Korrelation $\rho = 0$.",
        r"Korrelation $\rho = -0.25$.",
        r"Korrelation $\rho = -0.5$."
    ],
    "correct_idx": 3,
    "solution": {
        "de": r"""**Richtig: (d)**

### Study.Smart Guide
**Intuition:**
Wenn ich als erstes eine **hohe** Zahl ziehe (z.B. 5), fehlt diese hohe Zahl für den zweiten Zug.
Der zweite Zug wird also tendenziell **kleiner** ausfallen.
Großes X $\implies$ Kleines Y. Das ist eine **negative** Korrelation.
(Unabhängigkeit und Cov=0 sind also falsch).

**Formel:** (für $1..N$ ohne Zurücklegen):
$\rho = -\frac{1}{N-1} = -\frac{1}{5-1} = -0.25$.

---
### Offizielle Lösung
Ziehen ohne Zurücklegen $\implies$ negative Korrelation (wenn X groß, muss Y kleiner sein im Schnitt, da große Zahl weg). Spezifischer Wert -0.25 ($-\frac{1}{N-1}$ für $1..N$).""",
        "en": r"""**Correct: (d)**

### Study.Smart Guide
**Intuition:**
Without replacement creates competition. Drawing a high number leaves smaller numbers.
Negative correlation.
Formula: $\rho = -1/(N-1) = -1/4$.

---
### Official Solution
Without replacement implies negative correlation. Formula $-\frac{1}{N-1}$ gives $-1/4$."""
    }
}

uebung3_mc10 = {
    "source": "Übung 3, MC #10",
    "type": "mc",
    "question": {
        "de": r"Dichte $f(x,y) = \frac{1}{2}x + y$ für $0 \le x \le a, 0 \le y \le 1$. Bestimme a.",
        "en": r"Density $f(x,y) = \frac{1}{2}x + y$ on region. Find a."
    },
    "options": [
        r"1.236",
        r"2",
        r"3.236",
        r"3",
        r"1"
    ],
    "correct_idx": 0,
    "solution": {
        "de": r"""**Richtig: (a)**

### Study.Smart Guide
**Schritt-für-Schritt:**
1.  Doppelintegral muss 1 sein.
    $\int_0^1 \int_0^a (\frac{1}{2}x + y) dx dy = 1$.
2.  Inneres Integral (dx):
    $[\frac{1}{4}x^2 + xy]_0^a = \frac{a^2}{4} + ay$.
3.  Äußeres Integral (dy):
    $\int_0^1 (\frac{a^2}{4} + ay) dy = [\frac{a^2}{4}y + \frac{a}{2}y^2]_0^1 = \frac{a^2}{4} + \frac{a}{2}$.
4.  Gleichung lösen:
    $\frac{a^2}{4} + \frac{a}{2} = 1  \quad | \cdot 4$
    $a^2 + 2a - 4 = 0$.
5.  Mitternachtsformel:
    $a = \frac{-2 \pm \sqrt{4 - 4(1)(-4)}}{2} = \frac{-2 + \sqrt{20}}{2} = -1 + \sqrt{5} \approx 1.236$.

---
### Offizielle Lösung
Integral muss 1 sein. Führt auf quadratische Gleichung für a. $a \approx 1.236$.""",
        "en": r"""**Correct: (a)**

### Study.Smart Guide
**Step-by-Step:**
1.  $\int_0^1 \int_0^a (0.5x + y) dx dy = 1$.
2.  Evaluates to $a^2/4 + a/2 = 1$.
3.  $a^2 + 2a - 4 = 0$.
4.  $a = \sqrt{5} - 1 \approx 1.236$.

---
### Official Solution
Integrate to 1."""
    }
}

uebung3_mc11 = {
    "source": "Übung 3, MC #11",
    "type": "mc",
    "question": {
        "de": r"Dichte $f(x,y) = \frac{1}{12}x + \frac{1}{6}y$ auf $[0,2]^2$. Bedingte Dichte $f_{Y|X}(y)$?",
        "en": r"Density given. Conditional density $f_{Y|X}(y)$?"
    },
    "options": [
        r"$\frac{x+2y}{2+4y}$",
        r"$\frac{x+2y}{2x+4}$",
        r"$\frac{x+2y}{2x+4}$ ",
        r"$\frac{x+2y}{x+2}$",
        r"$\frac{1+2y}{...}$"
    ],
    "correct_idx": 1, 
    "solution": {
        "de": r"""**Richtig: (b)**

### Study.Smart Guide
**Rezept:**
$f_{Y|X}(y) = \frac{\text{Gemeinsame Dichte}}{\text{Randdichte X}}$.
1.  Gemeinsam: $\frac{x}{12} + \frac{y}{6} = \frac{x+2y}{12}$.
2.  Randdichte $f_X(x)$ berechnen (Integral über y von 0 bis 2):
    $\int_0^2 (\frac{x}{12} + \frac{y}{6}) dy = [\frac{xy}{12} + \frac{y^2}{12}]_0^2 = \frac{2x}{12} + \frac{4}{12} = \frac{2x+4}{12}$.
3.  Teilen:
    $\frac{(x+2y)/12}{(2x+4)/12} = \frac{x+2y}{2x+4}$.

---
### Offizielle Lösung
Ratio: Joint / Marginal X. Result: $\frac{x+2y}{2x+4}$.""",
        "en": r"""**Correct: (b)**

### Study.Smart Guide
**Step-by-Step:**
1.  Calculate Marginal $f_X(x) = \int f(x,y) dy$.
    Result: $(2x+4)/12$.
2.  Divide joint specificiation $(x+2y)/12$ by marginal.
    Result: $(x+2y)/(2x+4)$.

---
### Official Solution
Divide joint by marginal X."""
    }
}

uebung3_mc12 = {
    "source": "Übung 3, MC #12",
    "type": "mc",
    "question": {
        "de": r"Gleiche Dichte wie #11. $E[X+2Y]$?",
        "en": r"Same density. $E[X+2Y]$?"
    },
    "options": [
        r"33/9",
        r"34/9",
        r"10/3",
        r"32/9",
        r"10/3"
    ],
    "correct_idx": 3,
    "solution": {
        "de": r"""**Richtig: (d)**

### Study.Smart Guide
**Strategie:**
Nutze Linearität: $E[X+2Y] = E[X] + 2E[Y]$.
1.  Aus Symmetrie der Dichte ($x/12 + y/6$ vs Grenzen 0..2) und Termen... besser rechnen.
    $f_X(x) = \frac{x+2}{6}$ auf [0,2].
    $E[X] = \int_0^2 x \frac{x+2}{6} dx = \frac{1}{6} [\frac{x^3}{3} + x^2]_0^2 = \frac{1}{6} (\frac{8}{3} + 4) = \frac{1}{6} \frac{20}{3} = \frac{10}{9}$.
2.  Randdichte $Y$: symmetrisch? Nein.
    $f_Y(y) = \int_0^2 (\frac{x}{12} + \frac{y}{6}) dx = [\frac{x^2}{24} + \frac{xy}{6}]_0^2 = \frac{4}{24} + \frac{2y}{6} = \frac{1}{6} + \frac{y}{3} = \frac{1+2y}{6}$.
    $E[Y] = \int_0^2 y \frac{1+2y}{6} dy = \frac{1}{6} [\frac{y^2}{2} + \frac{2y^3}{3}]_0^2 = \frac{1}{6} (2 + \frac{16}{3}) = \frac{1}{6} \frac{22}{3} = \frac{11}{9}$.
3.  Summe:
    $E[X] + 2E[Y] = \frac{10}{9} + \frac{22}{9} = \frac{32}{9}$.

---
### Offizielle Lösung
Rechnung ergibt 32/9.""",
        "en": r"""**Correct: (d)**

### Study.Smart Guide
**Calculation:**
1.  $E[X] = 10/9$.
2.  $E[Y] = 11/9$.
3.  $E[X] + 2E[Y] = 10/9 + 22/9 = 32/9$.

---
### Official Solution
Linearity of expectation."""
    }
}

uebung3_mc13 = {
    "source": "Übung 3, MC #13",
    "type": "mc",
    "question": {
        "de": r"Gleiche Dichte wie #11. $V(Y)$?",
        "en": r"Same density. $V(Y)$?"
    },
    "options": [
        r"23/81",
        r"25/81",
        r"26/81",
        r"28/81",
        r"29/81"
    ],
    "correct_idx": 0,
    "solution": {
        "de": r"""**Richtig: (a)**

### Study.Smart Guide
**Verschiebungssatz:** $V(Y) = E[Y^2] - E[Y]^2$.
Wir wissen schon $E[Y] = 11/9$.
1.  $E[Y^2] = \int_0^2 y^2 \frac{1+2y}{6} dy = \frac{1}{6} [\frac{y^3}{3} + \frac{2y^4}{4}]_0^2 = \frac{1}{6} (\frac{8}{3} + 8) = \frac{1}{6} \frac{32}{3} = \frac{16}{9}$.
2.  Varianz:
    $\frac{16}{9} - (\frac{11}{9})^2 = \frac{144}{81} - \frac{121}{81} = \frac{23}{81}$.

---
### Offizielle Lösung
$V(Y) = E[Y^2] - E[Y]^2$. Genaues Rechnen erforderlich.""",
        "en": r"""**Correct: (a)**

### Study.Smart Guide
**Calculation:**
1.  $E[Y^2] = 16/9$.
2.  $E[Y] = 11/9$.
3.  Var = $16/9 - 121/81 = 144/81 - 121/81 = 23/81$.

---
### Official Solution
Standard variance formula."""
    }
}

# ------------------------------------------------------------------
# PROBLEMS
# ------------------------------------------------------------------

uebung3_prob1 = {
    "source": "Übung 3, Probe #1",
    "type": "problem",
    "question": {
        "de": r"Gemeinsame Massenfunktion (Tabelle). X (10, 20, 30), Y (2, 3, 4).<br>(a) Randverteilungen.<br>(c) V(X), V(Y).<br>(d) Cov, Rho.<br>(e) Unabhängig?",
        "en": r"Joint PMF table.<br>(a) Marginals.<br>(c) Variances.<br>(d) Cov, Rho.<br>(e) Indep?"
    },
    "solution": {
        "de": r"""### Study.Smart Guide
**Intuition (e) Unabhängigkeit:**
Schau dir die Tabelle an. Wenn es unabhängige Variablen wären, müsste jede Zeile ein Vielfaches der anderen sein ("gleiches Muster").
Wenn du z.B. siehst, dass in einer Zelle eine 0 steht, aber die Randwahrscheinlichkeiten nicht 0 sind, ist die Sache sofort klar: Abhängig! (Denn $a \cdot b = 0$ nur wenn $a=0$ oder $b=0$).

**Rechnung (d):**
Covariance-Formel verwenden: $E[XY] - E[X]E[Y]$.
Hier kommt zufällig 0 raus. Die Variablen sind unkorreliert, aber (wie in e gezeigt) abhängig. (Klassisches Beispiel: Punktwolke ist symmetrisch, aber nicht rechteckig).

---
### Offizielle Lösung
(a) Zeilen/Spaltensummen. Alle marginal $1/3$.<br>(c) $V(X)=66.67, V(Y)=0.67$.<br>(d) $Cov=0, \rho=0$.<br>(e) Nein, da $f(x,y) \neq f(x)f(y)$ für min. einen Fall (z.B. (30,4)).""",
        "en": r"""### Study.Smart Guide
**Analysis:**
Uncorrelated ($Cov=0$) but Dependent!
Check $f(x,y)$ vs $f(x)f(y)$. Discrepancy proves dependence.

---
### Official Solution
(a) Uniform marginals. (c) Var given. (d) 0. (e) Dependent."""
    }
}

uebung3_prob2 = {
    "source": "Übung 3, Probe #2",
    "type": "problem",
    "question": {
        "de": r"Tabelle mit $x_1..x_4, y_1..y_3$.<br>(a) $f_X(x_3), f_Y(y_2)$.<br>(b) Bedingte W'keiten.",
        "en": r"Joint PMF.<br>(a) Marginals.<br>(b) Conditionals."
    },
    "solution": {
        "de": r"""### Study.Smart Guide
**Kochrezept:**
1.  **Randverteilung (Marginal):** Einfach die Zeile oder Spalte aufsummieren. $P(X=x_3)$ ist die Summe der 3. Spalte.
2.  **Bedingte Wkt:** $P(Y|X) = \frac{\text{Zelle}}{\text{Spaltensumme}}$.
    Wir zoomen auf eine Spalte (Bedingung X) und schauen, wie groß der Anteil der Zelle Y darin ist.

---
### Offizielle Lösung
(a) Summen bilden. $f_X(x_3)=0.52$. $f_Y(y_2)=0.3$.<br>(b) $1; 0.4138; 0$.""",
        "en": r"""### Study.Smart Guide
**Recipe:**
Marginal = Sum of row/col.
Conditional = Cell / Sum of condition row/col.

---
### Official Solution
(a) 0.52, 0.3. (b) 1, 0.41, 0."""
    }
}

uebung3_prob3 = {
    "source": "Übung 3, Probe #3",
    "type": "problem",
    "question": {
        "de": r"X, Y Tabelle (0, 0.5, 1 vs 0, 1).<br>(a) Unabhängig?<br>(b) Cov?<br>(c) Varianz von X-Y?",
        "en": r"Table.<br>(a) Indep?<br>(b) Cov?<br>(c) V(X-Y)?"
    },
    "solution": {
        "de": r"""### Study.Smart Guide
**Wichtiger Zusammenhang (c):**
Allgemein gilt: $V(X-Y) = V(X) + V(Y) - 2 Cov(X,Y)$.
Da wir in (b) gesehen haben, dass Cov = 0 ist, vereinfacht sich das zu:
$V(X) + V(Y)$.
Rechenfehler vermeiden: Minuszeichen wird beim Quadrieren positiv ($(-1)^2 Var(Y)$), aber die Kovarianz wird subtrahiert. Bei Unkorreliertheit addieren sich Varianzen immer (egal ob X+Y oder X-Y).

---
### Offizielle Lösung
(a) Abhängig ($f(0,0)$ passt nicht).<br>(b) Cov 0 (unkorreliert aber abhängig!).<br>(c) $V(X-Y) = V(X)+V(Y)$ da unkorreliert.""",
        "en": r"""### Study.Smart Guide
**Formula (c):**
$V(X-Y) = V(X) + V(Y) - 2Cov(X,Y)$.
Since Cov=0, just sum the variances.

---
### Official Solution
(a) Dep. (b) 0. (c) Sum of vars."""
    }
}

uebung3_prob4 = {
    "source": "Übung 3, Probe #4",
    "type": "problem",
    "question": {
        "de": r"$f(x,y) = 24xy$ für $x+y \le 1$.<br>(a) Zeige Dichteeigenschaft.<br>(b) Unabhängig?",
        "en": r"$f(x,y) = 24xy$ on simplex.<br>(a) Verify PDF.<br>(b) Indep?"
    },
    "solution": {
        "de": r"""### Study.Smart Guide
**Trick (b) Unabhängigkeit:**
Schau dir den **Definitionsbereich** an (Support).
Hier gilt: $x+y \le 1$.
Das ist ein Dreieck.
Ein Dreieck ist **kein Rechteck**.
Wenn der Definitionsbereich kein Rechteck (Produkt von Intervallen) ist, sind X und Y **immer abhängig**.
Grund: Wenn X sehr groß ist (z.B. 0.9), *muss* Y klein sein (max 0.1). X schränkt Y ein. $\implies$ Abhängig.

---
### Offizielle Lösung
(a) Integral über Dreieck rechnen = 1.<br>(b) Abhängig. Bereich koppelt x und y.""",
        "en": r"""### Study.Smart Guide
**Pro Tip (b):**
Check domain boundaries. $x+y \le 1$ creates a triangle.
Ideally independent variables have rectangular support ($a<x<b, c<y<d$).
Triangular support $\implies$ Dependent.

---
### Official Solution
(a) Integral 1. (b) Dependent (domain)."""
    }
}

uebung3_prob5 = {
    "source": "Übung 3, Probe #5",
    "type": "problem",
    "question": {
        "de": r"$f(x,y) = 2x e^{-y}$ auf Rechteck $0<x<1, y>0$.<br>(a) Zeige Dichte.<br>(b) Unabhängig?",
        "en": r"$f(x,y) = 2x e^{-y}$.<br>(a) Verify PDF.<br>(b) Indep?"
    },
    "solution": {
        "de": r"""### Study.Smart Guide
**Analyse (b):**
1.  Definitionsbereich: Ein unendlicher Streifen (Rechteck). Check.
2.  Funktionsterm: $2x \cdot e^{-y}$. Lässt sich perfekt trennen in $g(x) \cdot h(y)$. Check.
Daher: Unabhängig.

---
### Offizielle Lösung
(a) Produktform auf Rechteck $\implies$ Integral = 1.<br>(b) Unabhängig, da $f(x,y)$ faktorisiert und Bereich rechteckig.""",
        "en": r"""### Study.Smart Guide
**Analysis:**
Rectangular domain + Factorizable function = Independent.

---
### Official Solution
(a) Valid. (b) Independent."""
    }
}

uebung3_prob6 = {
    "source": "Übung 3, Probe #6",
    "type": "problem",
    "question": {
        "de": r"Notenverteilung Mathe (X) Englisch (Y). Tabelle.<br>(a) Momente zeigen.<br>(b) Cov, Rho.<br>(c) $Z = (X+Y)/2$.",
        "en": r"Grades Math/Eng. Table.<br>(a) Moments.<br>(b) Cov/Rho.<br>(c) Average Z."
    },
    "solution": {
        "de": r"""### Study.Smart Guide
**Intuition (c) Diversifikation:**
Wir berechnen die Varianz des Durchschnitts $Z$.
Da Mathe und Englisch nicht perfekt korreliert sind (nur $\rho=0.36$, nicht 1), wird die Varianz des Durchschnitts kleiner als der Durchschnitt der Varianzen.
Das ist der "Portfolio-Effekt": Eine schlechte Note in Mathe kann durch eine gute in Englisch ausgeglichen werden. Der Durchschnitt schwankt weniger extrem als die Einzelnoten.

---
### Offizielle Lösung
(b) Cov 0.29, Rho 0.36 (positiver Zusammenhang).<br>(c) $V(Z)$ kleiner als Einzelvarianz (Diversifikation).""",
        "en": r"""### Study.Smart Guide
**Insight:**
Variance of average is lower than individual variance due to diversification (imperfect correlation).

---
### Official Solution
(b) 0.29, 0.36. (c) Reduced variance."""
    }
}

uebung3_prob7 = {
    "source": "Übung 3, Probe #7",
    "type": "problem",
    "question": {
        "de": r"X, Y, Z unabhängig. Diskrete Verteilungen gegeben.<br>(a) Mittelwert/Varianz X, Y, X-Y.<br>(b) Verteilung Summen.<br>(c) Wahrscheinlichkeiten.",
        "en": r"X, Y, Z indep discrete.<br>(a) Moments.<br>(b) Sum dists.<br>(c) Probs."
    },
    "solution": {
        "de": r"""### Study.Smart Guide
**Konzept:**
Faltung (Convolution).
Wenn wir die *Verteilung* der Summe $S = X+Y$ suchen, müssen wir alle Kombinationen durchgehen, die eine bestimmte Summe s ergeben.
z.B. $P(S=3) = P(X=1, Y=2) + P(X=2, Y=1) + ...$
Wegen Unabhängigkeit multiplizieren wir die Einzelwahrscheinlichkeiten.

---
### Offizielle Lösung
(a) Additivität bei Unabhängigkeit.<br>(b) Faltung der Verteilungen.<br>(c) Produktregel.""",
        "en": r"""### Study.Smart Guide
**Concept:**
Convolution. Summing probabilities of all combinations leading to total S.

---
### Official Solution
(a) Additive. (b) Convolution. (c) Product."""
    }
}
