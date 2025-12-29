
# Test 1-5 Exam Staging File (DUAL MODE)
# Content extracted from Test_Statistics[1-5]_german.pdf
# Solutions: Study.Smart Premium + Official (Placeholder)

# ------------------------------------------------------------------
# Test 1 (Übung 1 Quiz)
# ------------------------------------------------------------------

test1_mc1 = {
    "source": "Test 1, Q1",
    "type": "mc",
    "question": {
        "de": r"Statistik-Vorlesung: VWL (42m, 93w), BWL (78m, 87w). Eine Hörerin wird gewählt. Wahrscheinlichkeit, dass sie BWLerin ist?",
        "en": r"Stats class: Econ (42m, 93f), Bus (78m, 87f). A female student is chosen. Probability she is Business?"
    },
    "options": [
        r"0.31",
        r"0.29",
        r"0.71",
        r"0.48"
    ],
    "correct_idx": 3,
    "solution": {
        "de": r"""**Richtig: (d)**

### Study.Smart Guide
**Intuition:**
Dies ist eine bedingte Wahrscheinlichkeit. Da wir bereits *wissen*, dass eine Hörerin gewählt wurde, interessieren uns die Männer nicht mehr. Unsere "Welt" besteht nur noch aus den Frauen.

**Schritt-für-Schritt:**
1.  Berechne die Gesamtzahl der Frauen (unsere neue Basis):
    $$n_{Frauen} = 93 \text{ (VWL)} + 87 \text{ (BWL)} = 180$$
2.  Identifiziere die gewünschte Gruppe (BWL-Frauen):
    $$k = 87$$
3.  Berechne den Anteil:
    $$P = \frac{87}{180} \approx 0.4833$$

---
### Offizielle Lösung
*(Nicht in den Quellen enthalten)*""",
        "en": r"""**Correct: (d)**

### Study.Smart Guide
**Intuition:**
This is conditional probability. The "universe" shrinks to just the women.

**Step-by-Step:**
1.  Total women: $93 + 87 = 180$.
2.  Business women: $87$.
3.  Ratio: $\frac{87}{180} \approx 0.4833$.

---
### Official Solution
*(Not provided in source)*"""
    }
}

test1_mc2 = {
    "source": "Test 1, Q2",
    "type": "mc",
    "question": {
        "de": r"$P(A)=0.6, P(B)=0.7, P(\bar{A} \cap B)=0.1$. Berechne $P(A \cap \bar{B})$.",
        "en": r"$P(A)=0.6, P(B)=0.7, P(\bar{A} \cap B)=0.1$. Find $P(A \cap \bar{B})$."
    },
    "options": [
        r"0",
        r"0.1",
        r"0.2",
        r"0.3"
    ],
    "correct_idx": 0,
    "solution": {
        "de": r"""**Richtig: (a)**

### Study.Smart Guide
**Intuition:**
Stell dir ein Venn-Diagramm vor. B besteht aus "Überlapp" und "Nicht-Überlapp". Wenn B (0.7) und der Nicht-Überlapp (0.1) bekannt sind, muss der Überlapp 0.6 sein.
Da A selbst nur 0.6 groß ist, liegt A also *vollständig* im Überlapp.

**Schritt-für-Schritt:**
1.  $P(A \cap B) = P(B) - P(\bar{A} \cap B) = 0.7 - 0.1 = 0.6$.
2.  $P(A \cap \bar{B}) = P(A) - P(A \cap B) = 0.6 - 0.6 = 0$.

---
### Offizielle Lösung
*(Nicht in den Quellen enthalten)*""",
        "en": r"""**Correct: (a)**

### Study.Smart Guide
**Intuition:**
A is fully contained inside B.

**Step-by-Step:**
1.  Overlap: $P(A \cap B) = 0.7 - 0.1 = 0.6$.
2.  A without B: $P(A) - 0.6 = 0$.

---
### Official Solution
*(Not provided in source)*"""
    }
}

test1_mc3 = {
    "source": "Test 1, Q3",
    "type": "mc",
    "question": {
        "de": r"50 DVDs und 50 Hüllen. Zufällige Verteilung. Wie viele Möglichkeiten?",
        "en": r"50 DVDs, 50 cases. Random arrangement. How many possibilities?"
    },
    "options": [
        r"$50!$",
        r"$(50!)^2$",
        r"$50! \cdot 49!$",
        r"$100$"
    ],
    "correct_idx": 0,
    "solution": {
        "de": r"""**Richtig: (a)**

### Study.Smart Guide
**Intuition:**
Für die 1. Hülle gibt es 50 mögliche DVDs. Für die 2. Hülle nur noch 49. Ein klassischer Countdown.

**Formel:**
$$N = 50 \cdot 49 \cdot ... \cdot 1 = 50!$$

---
### Offizielle Lösung
*(Nicht in den Quellen enthalten)*""",
        "en": r"""**Correct: (a)**

### Study.Smart Guide
**Intuition:**
Choosing without replacement where order matters (specific DVD in specific case).

**Formula:**
$$50!$$

---
### Official Solution
*(Not provided in source)*"""
    }
}

# ------------------------------------------------------------------
# Test 2 (Übung 2 Quiz)
# ------------------------------------------------------------------

test2_mc1 = {
    "source": "Test 2, Q1",
    "type": "mc",
    "question": {
        "de": r"10 Mitglieder (4 Frauen, 6 Männer). Vorstand: 2 Damen, 2 Herren. Anzahl Möglichkeiten?",
        "en": r"10 members (4F, 6M). Board: 2F, 2M. Combinations?"
    },
    "options": [
        r"89",
        r"210",
        r"90",
        r"75"
    ],
    "correct_idx": 2,
    "solution": {
        "de": r"""**Richtig: (c)**

### Study.Smart Guide
**Intuition:**
Zwei separate Wahlvorgänge ("Damenwahl" und "Herrenwahl") werden kombiniert (multipliziert). Reihenfolge egal $\to$ Binomialkoeffizient.

**Schritt-für-Schritt:**
1.  Frauen: $\binom{4}{2} = 6$.
2.  Männer: $\binom{6}{2} = 15$.
3.  Gesamt: $6 \cdot 15 = 90$.

---
### Offizielle Lösung
*(Nicht in den Quellen enthalten)*""",
        "en": r"""**Correct: (c)**

### Study.Smart Guide
**Step-by-Step:**
1.  Women: $\binom{4}{2} = 6$.
2.  Men: $\binom{6}{2} = 15$.
3.  Total: $90$.

---
### Official Solution
*(Not provided in source)*"""
    }
}

test2_mc2 = {
    "source": "Test 2, Q2",
    "type": "mc",
    "question": {
        "de": r"$X \sim U[-4, 4]$. $P(X^2 \le 9)$?",
        "en": r"$X \sim U[-4, 4]$. $P(X^2 \le 9)$?"
    },
    "options": [
        r"7/9",
        r"4/9",
        r"2/3",
        r"3/4"
    ],
    "correct_idx": 3,
    "solution": {
        "de": r"""**Richtig: (d)**

### Study.Smart Guide
**Intuition:**
$X^2 \le 9$ heißt $X$ ist zwischen -3 und 3. Verhältnis der Länge $[-3,3]$ zur Gesamtlänge $[-4,4]$.

**Rechnung:**
$$\frac{3 - (-3)}{4 - (-4)} = \frac{6}{8} = \frac{3}{4}$$

---
### Offizielle Lösung
*(Nicht in den Quellen enthalten)*""",
        "en": r"""**Correct: (d)**

### Study.Smart Guide
**Intuition:**
Ratio of target range length (6) to total range length (8).

**Calculation:**
$$6/8 = 3/4$$

---
### Official Solution
*(Not provided in source)*"""
    }
}

test2_mc3 = {
    "source": "Test 2, Q3",
    "type": "mc",
    "question": {
        "de": r"$X$ auf $[0, 10]$ mit Dichte $f(x) = \frac{x}{100} + \frac{1}{20}$. $P(2 \le X \le 6)$?",
        "en": r"$X$ on $[0, 10]$ with pdf $f(x) = x/100 + 1/20$. $P(2 \le X \le 6)$?"
    },
    "options": [
        r"9/25",
        r"2/50",
        r"1/12",
        r"3/50"
    ],
    "correct_idx": 0,
    "solution": {
        "de": r"""**Richtig: (a)**

### Study.Smart Guide
**Schritt-für-Schritt:**
1.  Stammfunktion: $F(x) = \frac{x^2}{200} + \frac{x}{20}$.
2.  Berechne $F(6) - F(2)$:
    $$(0.18 + 0.3) - (0.02 + 0.1) = 0.48 - 0.12 = 0.36 = 9/25$$

---
### Offizielle Lösung
*(Nicht in den Quellen enthalten)*""",
        "en": r"""**Correct: (a)**

### Study.Smart Guide
**Step-by-Step:**
1.  Integrate PDF from 2 to 6.
2.  Result is $0.36$.

---
### Official Solution
*(Not provided in source)*"""
    }
}

test2_mc4 = {
    "source": "Test 2, Q4",
    "type": "mc",
    "question": {
        "de": r"Diskrete ZV $f(x) = \frac{x+4}{c}$ für $x=1,..,5$. Bestimme c.",
        "en": r"Discrete RV $f(x) = (x+4)/c$ for $x=1..5$. Find c."
    },
    "options": [
        r"20",
        r"25",
        r"30",
        r"35"
    ],
    "correct_idx": 3,
    "solution": {
        "de": r"""**Richtig: (d)**

### Study.Smart Guide
**Intuition:**
Alle Wahrscheinlichkeiten müssen zusammen 1 ergeben.

**Rechnung:**
Summe der Zähler: $5+6+7+8+9 = 35$.
Also muss $c=35$ sein, damit $\frac{35}{35}=1$.

---
### Offizielle Lösung
*(Nicht in den Quellen enthalten)*""",
        "en": r"""**Correct: (d)**

### Study.Smart Guide
**Intuition:**
Probabilities sum to 1.
Sum of numerators is 35, so denominator must be 35.

---
### Official Solution
*(Not provided in source)*"""
    }
}

# ------------------------------------------------------------------
# Test 3 (Übung 4 Quiz)
# ------------------------------------------------------------------

test3_mc1 = {
    "source": "Test 3, Q1",
    "type": "mc",
    "question": {
        "de": r"A, B disjunkt, P(A), P(B)>0. Welche Aussage trifft zu?",
        "en": r"A, B disjoint. Which is true?"
    },
    "options": [
        r"$P(\bar{A} \cap \bar{B}) + P(B) > 1 - P(A)$",
        r"$P(A \cap B) > P(A)$",
        r"$P(A|B) = P(B|A)$",
        r"$P(A \cup B) < P(A)$"
    ],
    "correct_idx": 2,
    "solution": {
        "de": r"""**Richtig: (c)**

### Study.Smart Guide
**Intuition:**
Disjunkt = Kein Überlapp.
Wenn B passiert ist, kann A unmöglich passieren ($0\%$). Und umgekehrt.

**Rechnung:**
$P(A|B) = 0$. $P(B|A) = 0$. Also gleich.

---
### Offizielle Lösung
*(Nicht in den Quellen enthalten)*""",
        "en": r"""**Correct: (c)**

### Study.Smart Guide
**Intuition:**
Disjoint implies zero overlap, so zero conditional probability in both directions.

---
### Official Solution
*(Not provided in source)*"""
    }
}

test3_mc2 = {
    "source": "Test 3, Q2",
    "type": "mc",
    "question": {
        "de": r"$Y = X/\sigma$. $E(Y^2)$?",
        "en": r"$Y = X/\sigma$. $E(Y^2)$?"
    },
    "options": [
        r"1",
        r"$1 - \mu^2/\sigma^2$",
        r"$1 + \mu^2/\sigma^2$",
        r"Nicht beantwortbar"
    ],
    "correct_idx": 2,
    "solution": {
        "de": r"""**Richtig: (c)**

### Study.Smart Guide
**Schritt-für-Schritt:**
1.  $Var(Y) = Var(\frac{X}{\sigma}) = \frac{1}{\sigma^2}Var(X) = 1$.
2.  $E[Y] = \frac{\mu}{\sigma}$.
3.  $E[Y^2] = Var(Y) + (E[Y])^2 = 1 + \frac{\mu^2}{\sigma^2}$.

---
### Offizielle Lösung
*(Nicht in den Quellen enthalten)*""",
        "en": r"""**Correct: (c)**

### Study.Smart Guide
**Calculation:**
Using $E[Y^2] = Var(Y) + E[Y]^2$, with standardized variance leaving 1.

---
### Official Solution
*(Not provided in source)*"""
    }
}

test3_mc3 = {
    "source": "Test 3, Q3",
    "type": "mc",
    "question": {
        "de": r"$Corr(X,Y)=-1, Var(X)=1, SD(Y)=2$. $Var(3X+Y)$?",
        "en": r"$Corr(X,Y)=-1, Var(X)=1, SD(Y)=2$. $Var(3X+Y)$?"
    },
    "options": [
        r"7",
        r"13",
        r"5",
        r"1"
    ],
    "correct_idx": 3,
    "solution": {
        "de": r"""**Richtig: (d)**

### Study.Smart Guide
**Intuition:**
Starke negative Korrelation reduziert die Gesamtvarianz der Summe.

**Schritt-für-Schritt:**
$$Var = 3^2 Var(X) + 1^2 Var(Y) + 2(3)(1) Corr \cdot \sigma_X \sigma_Y$$
$$= 9(1) + 4 + 6(-1)(1)(2)$$
$$= 13 - 12 = 1$$

---
### Offizielle Lösung
*(Nicht in den Quellen enthalten)*""",
        "en": r"""**Correct: (d)**

### Study.Smart Guide
**Step-by-Step:**
Calculation yields $13 - 12 = 1$.

---
### Official Solution
*(Not provided in source)*"""
    }
}

test3_mc4 = {
    "source": "Test 3, Q4",
    "type": "mc",
    "question": {
        "de": r"X, Y unkorreliert. $E(X)=E(Y)=1, Var(X)=Var(Y)=1$. Was gilt?",
        "en": r"X, Y uncorrelated. Moments given. True?"
    },
    "options": [
        r"$3E(X^2) + Cov(X,Y) = 2$",
        r"$E(XY) = 2$",
        r"$Cov(X, Y+2) = 2$",
        r"$E((X-Y)^2) = 2$"
    ],
    "correct_idx": 3,
    "solution": {
        "de": r"""**Richtig: (d)**

### Study.Smart Guide
**Schritt-für-Schritt:**
$E[(X-Y)^2] = Var(X-Y) + (E[X-Y])^2$.
$Var(X-Y) = Var(X) + Var(Y) = 2$ (da unkorreliert).
$E[X-Y] = 0$.
Ergebnis: 2.

---
### Offizielle Lösung
*(Nicht in den Quellen enthalten)*""",
        "en": r"""**Correct: (d)**

### Study.Smart Guide
Check 2nd moment of difference. Result is 2.

---
### Official Solution
*(Not provided in source)*"""
    }
}

# ------------------------------------------------------------------
# Test 4 (Übung 3 Quiz)
# ------------------------------------------------------------------

test4_mc1 = {
    "source": "Test 4, Q1",
    "type": "mc",
    "question": {
        "de": r"$X \sim Pois(10), Z=2X$. Welche Aussage trifft NICHT zu?",
        "en": r"$X \sim Pois(10), Z=2X$. Which is FALSE?"
    },
    "options": [
        r"$Z \sim Pois(20)$",
        r"$Var(Z) = 40$",
        r"Corr(X, Z) = 1$",
        r"$E[Z] = 20$"
    ],
    "correct_idx": 0,
    "solution": {
        "de": r"""**Richtig: (a)**

### Study.Smart Guide
**Die Falle:**
Eine Poisson-Verteilung muss alle ganzen Zahlen abdecken (0,1,2,3...).
$Z=2X$ kann aber nur gerade Zahlen annehmen (0,2,4...). Daher ist es *keine* Poisson-Verteilung, obwohl Erwartungswert und Varianz vielleicht passen würden.

---
### Offizielle Lösung
*(Nicht in den Quellen enthalten)*""",
        "en": r"""**Correct: (a)**

### Study.Smart Guide
**The Trap:**
$2X$ only takes even values, violating the Poisson support (all integers).

---
### Official Solution
*(Not provided in source)*"""
    }
}

test4_mc2 = {
    "source": "Test 4, Q2",
    "type": "mc",
    "question": {
        "de": r"$Z = 4X - 3Y + 2$. $Cov(X, Z)$ unter Annahme Unkorreliertheit?",
        "en": r"$Z = 4X - 3Y + 2$. $Cov(X, Z)$ assuming uncorrelated?"
    },
    "options": [
        r"0",
        r"64",
        r"16",
        r"Info fehlt"
    ],
    "correct_idx": 2,
    "solution": {
        "de": r"""**Richtig: (c)**

### Study.Smart Guide
**Intuition:**
Wir messen $Cov(X, 4X - ...)$. Der Faktor 4 wird herausgezogen. $Cov(X,X)$ ist die Varianz.

**Rechnung:**
$4 Var(X) = 4 \cdot 4 = 16$.

---
### Offizielle Lösung
*(Nicht in den Quellen enthalten)*""",
        "en": r"""**Correct: (c)**

### Study.Smart Guide
**Calculation:**
$4 Var(X) = 16$.

---
### Official Solution
*(Not provided in source)*"""
    }
}

test4_mc3 = {
    "source": "Test 4, Q3",
    "type": "mc",
    "question": {
        "de": r"Zahlenreihe: 13, 7, 22, 4, 11, 8, 7, 4, 13, 7, 14. Welche Zahl ist weder Mean, Mode noch Median?",
        "en": r"Series. Which number is neither Mean, Mode, nor Median?"
    },
    "options": [
        r"7",
        r"8",
        r"10",
        r"11"
    ],
    "correct_idx": 3,
    "solution": {
        "de": r"""**Richtig: (d)**

### Study.Smart Guide
**Analyse:**
*   Mode = 7 (3x)
*   Median = 8 (Mitte)
*   Mean = 10
Die 11 kommt nicht vor.

---
### Offizielle Lösung
*(Nicht in den Quellen enthalten)*""",
        "en": r"""**Correct: (d)**

### Study.Smart Guide
11 matches none of the metrics.

---
### Official Solution
*(Not provided in source)*"""
    }
}

# ------------------------------------------------------------------
# Test 5 (Seminar 5)
# ------------------------------------------------------------------

test5_mc1 = {
    "source": "Test 5, Q1",
    "type": "mc",
    "question": {
        "de": r"1000 Leute (700 Smart, 300 Gewöhnlich). Stichprobe 200. $P(X=10)$ gewöhnliche?",
        "en": r"1000 ppl (700 smart, 300 ordinary). Sample 200. $P(X=10)$ ordinary?"
    },
    "options": [
        r"Additiv",
        r"Multiplikativ",
        r"Hypergeometrisch: $\frac{\binom{300}{10}\binom{700}{190}}{\binom{1000}{200}}$",
        r"Unbekannt"
    ],
    "correct_idx": 2,
    "solution": {
        "de": r"""**Richtig: (c)**

### Study.Smart Guide
**Intuition:**
Ziehen ohne Zurücklegen aus zwei Gruppen = Hypergeometrisch.

**Formel:**
"Günstige Möglichkeiten" geteilt durch "Alle Möglichkeiten".
Günstig: 10 aus 300 UND 190 aus 700.

---
### Offizielle Lösung
*(Nicht in den Quellen enthalten)*""",
        "en": r"""**Correct: (c)**

### Study.Smart Guide
Hypergeometric distribution logic.

---
### Official Solution
*(Not provided in source)*"""
    }
}

test5_mc2 = {
    "source": "Test 5, Q2",
    "type": "mc",
    "question": {
        "de": r"Stetige ZV X, Y. Was ist immer korrekt?",
        "en": r"Continuous X, Y. Which is always true?"
    },
    "options": [
        r"Randdichten reichen für gemeinsame Dichte",
        r"Unabh <=> Cov=0",
        r"$f(y|x) = f(x|y)$",
        r"$Cov(X,Y)=0 \iff E[XY] = E[X]E[Y]$"
    ],
    "correct_idx": 3,
    "solution": {
        "de": r"""**Richtig: (d)**

### Study.Smart Guide
**Intuition:**
Dies ist die Definition von "Unkorreliertheit". Wenn Covariance Null ist, faktorisieren die Erwartungswerte.

---
### Offizielle Lösung
*(Nicht in den Quellen enthalten)*""",
        "en": r"""**Correct: (d)**

### Study.Smart Guide
Definition of zero covariance.

---
### Official Solution
*(Not provided in source)*"""
    }
}

test5_mc3 = {
    "source": "Test 5, Q3",
    "type": "mc",
    "question": {
        "de": r"$X_i \sim U[1, \theta]$. Schätzer $\hat{\theta} = \frac{2}{n}\sum X_i$.",
        "en": r"$X_i \sim U[1, \theta]$. Est $\hat{\theta} = \frac{2}{n}\sum X_i$."
    },
    "options": [
        r"Varianz ist $\frac{(\theta-1)^2}{3n}$",
        r"Erwartungstreu",
        r"Konsistent",
        r"Bias ..."
    ],
    "correct_idx": 0,
    "solution": {
        "de": r"""**Richtig: (a)**

### Study.Smart Guide
**Schritt-für-Schritt:**
1.  $Var(X) = (\theta-1)^2 / 12$.
2.  Schätzer ist "2 mal das Stichprobenmittel".
3.  $Var(2 \bar{X}) = 4 Var(\bar{X}) = 4 \frac{Var(X)}{n}$.
4.  Einsetzen: $4 \frac{(\theta-1)^2}{12n} = \frac{(\theta-1)^2}{3n}$.

---
### Offizielle Lösung
*(Nicht in den Quellen enthalten)*""",
        "en": r"""**Correct: (a)**

### Study.Smart Guide
**Calculation:**
Variance of $2 \bar{X}$ is $4/n$ times individual variance. Result is correct.

---
### Official Solution
*(Not provided in source)*"""
    }
}

test5_mc4 = {
    "source": "Test 5, Q4",
    "type": "mc",
    "question": {
        "de": r"Normalverteilt $\mu=400, \sigma^2=25$ ($\sigma=5$). 95% Intervall?",
        "en": r"Normal $\mu=400, \sigma=5$. 95% interval?"
    },
    "options": [
        r"[391.8, 408.2]",
        r"[390.2, 409.8]",
        r"[393.6, 406.4]",
        r"[351.0, 449.0]"
    ],
    "correct_idx": 1,
    "solution": {
        "de": r"""**Richtig: (b)**

### Study.Smart Guide
**Intuition:**
95% $\approx$ 2 Standardabweichungen (genau 1.96).

**Rechnung:**
$400 \pm 1.96(5) = 400 \pm 9.8$.

---
### Offizielle Lösung
*(Nicht in den Quellen enthalten)*""",
        "en": r"""**Correct: (b)**

### Study.Smart Guide
**Intuition:**
Mean +/- 1.96 SD.

---
### Official Solution
*(Not provided in source)*"""
    }
}
