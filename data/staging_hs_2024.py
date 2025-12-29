
# HS 2024 Exam Staging File
# Content extracted from:
# - HS2024_january_german (1).pdf
# - HS2024_january_german_solution.pdf
# Dual-Mode: Study.Smart Guide + Official Solution

# ------------------------------------------------------------------
# MULTIPLE CHOICE (4 Punkte each)
# ------------------------------------------------------------------

hs2024_mc1 = {
    "source": "HS 2024 Januar, MC #1 (4 Punkte)",
    "type": "mc",
    "question": {
        "de": r"Wir beobachten 25 i.i.d. Zufallsvariablen aus $N(\mu, \sigma^2=0.5)$. Test $H_0: \mu=0.5$ gegen $H_1: \mu \ge 0.5$ ($\alpha=5\%$). Für welchen Wertebereich von $\bar{x}$ wird $H_0$ verworfen?",
        "en": r"We observe 25 i.i.d. random variables from $N(\mu, \sigma^2=0.5)$. Test $H_0: \mu=0.5$ vs $H_1: \mu \ge 0.5$ ($\alpha=5\%$). For which range of $\bar{x}$ is $H_0$ rejected?"
    },
    "options": [
        r"$\bar{x} > 0.66$",
        r"$\bar{x} > 0.73$",
        r"$\bar{x} > 0.78$",
        r"$\bar{x} > 1.64$"
    ],
    "correct_idx": 1, 
    "solution": {
        "de": r"""**Richtig: (b)**

### Study.Smart Guide
**Schritt-für-Schritt:**
1.  **Standardfehler (SE):** $\sigma_{\bar{x}} = \frac{\sigma}{\sqrt{n}} = \frac{\sqrt{0.5}}{5} \approx \frac{0.707}{5} \approx 0.1414$.
2.  **Kritischer Z-Wert:** Für einen einseitigen Test ($>$) mit $\alpha=5\%$ schneiden wir die oberen 5% ab. $z_{0.95} = 1.645$.
3.  **Grenzwert berechnen:**
    Grenze = $H_0\text{-Mittelwert} + z \cdot SE$
    $= 0.5 + 1.645 \cdot 0.1414$
    $= 0.5 + 0.2326$
    $\approx 0.733$.
    Wir verwerfen, wenn $\bar{x}$ größer als dieser Wert ist.

---
### Offizielle Lösung
Einseitiger Test. Kritischer Wert $z_{0.95} = 1.645$.<br>Grenze: $\mu_0 + z \frac{\sigma}{\sqrt{n}} = 0.5 + 1.645 \frac{\sqrt{0.5}}{5} = 0.5 + 1.645 \cdot 0.1414 \approx 0.5 + 0.232 = 0.732$.""",
        "en": r"""**Correct: (b)**

### Study.Smart Guide
**Calculation:**
1.  Std Error: $\sqrt{0.5}/5 \approx 0.141$.
2.  Critical Z: $1.645$ (one-sided 5%).
3.  Cutoff: $0.5 + 1.645(0.141) \approx 0.732$.

---
### Official Solution
One-sided test. $z_{0.95} = 1.645$.<br>Limit: $0.5 + 1.645 \frac{\sqrt{0.5}}{5} \approx 0.73$."""
    }
}

hs2024_mc2 = {
    "source": "HS 2024 Januar, MC #2 (4 Punkte)",
    "type": "mc",
    "question": {
        "de": r"Seien $E[X^2] = E[Y] = 1/3$, $E[X]=0$ und $\rho_{X^2, Y} > 0$. Welche Aussage über $\rho_{X,Y}$ (Korrelation von X und Y) ist immer wahr?",
        "en": r"Let $E[X^2] = E[Y] = 1/3$, $E[X]=0$ and $\rho_{X^2, Y} > 0$. Which statement about $\rho_{X,Y}$ is always true?"
    },
    "options": [
        r"$-1 \le \rho_{X,Y} < 0$",
        r"$\rho_{X,Y} = 0$",
        r"$0 < \rho_{X,Y} \le 1$",
        r"Keine der obigen Aussagen ist immer wahr."
    ],
    "correct_idx": 3,
    "solution": {
        "de": r"""**Richtig: (d)**

### Study.Smart Guide
**Intuition:**
Die Korrelation misst nur *lineare* Zusammenhänge.
Informationen über $X^2$ sagen nichts zwingendes über $X$ aus, da das Vorzeichen von $X$ verloren geht.
*   **Gegenbeispiel A:**
    Sei $Y = X^2$. Dann ist $\rho_{X^2, Y} = 1 > 0$.
    Aber wenn $X$ symmetrisch um 0 ist, ist $\rho_{X, Y} = 0$ (unkorreliert).
*   **Gegenbeispiel B:**
    Sei $Y = X + X^2$. Da ist sicher eine Korrelation zwischen $X$ und $Y$ vorhanden.
Da es verschiedene Möglichkeiten gibt (0 oder ungleich 0), ist keine der Aussagen (a), (b), (c) *immer* wahr.

---
### Offizielle Lösung
Korrelation zwischen $X^2$ und $Y$ impliziert nichts über Korrelation zwischen $X$ und $Y$.<br>Beispiel 1: $Y=X^2$ (symmetrisch um 0) $\to \rho_{X,Y}=0$.<br>Beispiel 2: $Y=X^2+X \to \rho_{X,Y} \neq 0$.""",
        "en": r"""**Correct: (d)**

### Study.Smart Guide
**Counterexamples:**
1.  Assume $Y = X^2$ and $X$ is standard normal.
    Then Corr($X^2, Y$) = 1 (positive).
    But Corr($X, Y$) = Corr($X, X^2$) = 0 (by symmetry).
2.  Assume $Y = X + X^2$.
    Then Corr($X, Y$) $\neq 0$.
Since it could be 0 or non-zero, (d) is the only valid answer.

---
### Official Solution
Correlation between $X^2$ and $Y$ implies nothing about $X$ and $Y$.<br>Could be 0 (if $Y=X^2$ symmetric) or non-zero."""
    }
}

hs2024_mc3 = {
    "source": "HS 2024 Januar, MC #3 (4 Punkte)",
    "type": "mc",
    "question": {
        "de": r"Gegeben: $P(A)=1/2, P(B)=2/3, P(A \cap B)=1/4$. Wie gross ist die bedingte Wahrscheinlichkeit $P(A | \bar{B})$?",
        "en": r"Given: $P(A)=1/2, P(B)=2/3, P(A \cap B)=1/4$. What is $P(A | \bar{B})$?"
    },
    "options": [
        r"$1/4$",
        r"$1/3$",
        r"$3/4$",
        r"$5/6$"
    ],
    "correct_idx": 2,
    "solution": {
        "de": r"""**Richtig: (c)**

### Study.Smart Guide
**Venn-Diagramm Logik:**
Wir suchen den Anteil von A, der *außerhalb* von B liegt ($A \cap \bar{B}$), relativ zur Gesamtfläche außerhalb von B ($\bar{B}$).

**Schritt-für-Schritt:**
1.  **Zähler ($A$ ohne $B$):**
    $P(A \cap \bar{B}) = P(A) - P(A \cap B) = 1/2 - 1/4 = 1/4$.
2.  **Nenner (Nicht $B$):**
    $P(\bar{B}) = 1 - P(B) = 1 - 2/3 = 1/3$.
3.  **Quotient:**
    $\frac{1/4}{1/3} = \frac{1}{4} \cdot \frac{3}{1} = \frac{3}{4}$.

---
### Offizielle Lösung
$P(A | \bar{B}) = \frac{P(A \cap \bar{B})}{P(\bar{B})} = \frac{P(A) - P(A \cap B)}{1 - P(B)} = \frac{1/2 - 1/4}{1 - 2/3} = \frac{1/4}{1/3} = 3/4$.""",
        "en": r"""**Correct: (c)**

### Study.Smart Guide
**Step-by-Step:**
1.  Prob of A satisfying "Not B": $P(A) - P(A \cap B) = 0.5 - 0.25 = 0.25$.
2.  Prob of "Not B": $1 - 2/3 = 1/3$.
3.  Conditional: $0.25 / (1/3) = 0.75 = 3/4$.

---
### Official Solution
$P(A | \bar{B}) = \frac{P(A) - P(A \cap B)}{1 - P(B)} = \frac{0.25}{0.333} = 0.75$."""
    }
}

hs2024_mc4 = {
    "source": "HS 2024 Januar, MC #4 (4 Punkte)",
    "type": "mc",
    "question": {
        "de": r"Nudeln. $X \sim N(500, 40)$. Symmetrisches 99% Konfidenzintervall für das Gewicht einer einzelnen Packung?",
        "en": r"Pasta. $X \sim N(500, 40)$. Symmetric 99% confidence interval for the weight of a single package?"
    },
    "options": [
        r"[396.97 ; 603.03]",
        r"[483.71 ; 516.29]",
        r"[485.29 ; 514.71]",
        r"[487.60 ; 512.40]"
    ],
    "correct_idx": 1,
    "solution": {
        "de": r"""**Richtig: (b)**

### Study.Smart Guide
**Achtung, Begriffsfalle:**
Nach Lehrbuch ist ein "Konfidenzintervall" für einen *Parameter* (wie $\mu$). Hier ist $\mu=500$ aber schon bekannt!
Die Frage sucht eigentlich das **Schwankungsintervall** (Prediction Interval), in dem 99% der *einzelnen Packungen* liegen.
Wir nutzen also direkt $\sigma$ (Varianz der Einzelwerte), NICHT $\sigma/\sqrt{n}$ (Varianz des Mittelwerts).

**Schritt-für-Schritt:**
1.  Parameter: $\mu=500$, $\sigma = \sqrt{40} \approx 6.325$.
2.  Z-Score für 99% (symmetrisch): $z = 2.576$.
3.  Breite:
    $2.576 \cdot 6.325 \approx 16.29$.
4.  Intervall:
    $500 \pm 16.29 \Rightarrow [483.71, 516.29]$.

---
### Offizielle Lösung
Vorhersageintervall für X (nicht KI für Mittelwert!).<br>$500 \pm z_{0.995} \cdot \sigma = 500 \pm 2.576 \cdot \sqrt{40} = 500 \pm 16.29$.<br>Intervall: $[483.71, 516.29]$.""",
        "en": r"""**Correct: (b)**

### Study.Smart Guide
**Important Distinction:**
We are looking for the range of a *single package* (Population Distribution), NOT the range of the mean estimate.
So we use $\sigma$, not Standard Error.

**Calculation:**
$\mu \pm 2.576 \sigma = 500 \pm 2.576 \cdot 6.325 = 500 \pm 16.29$.

---
### Official Solution
Range containing 99% of packages: $\mu \pm 2.576 \sigma = 500 \pm 16.3 = [483.7, 516.3]$."""
    }
}

hs2024_mc5 = {
    "source": "HS 2024 Januar, MC #5 (4 Punkte)",
    "type": "mc",
    "question": {
        "de": r"4 Zahlen aus ersten 12 Primzahlen ohne Zurücklegen. A: Summe ungerade. B: Alle 4 ungerade. Beziehung zwischen A und B?",
        "en": r"4 numbers from first 12 primes without replacement. A: Sum odd. B: All 4 odd. Relation between A and B?"
    },
    "options": [
        r"Unabhängig und disjunkt.",
        r"Unabhängig, aber nicht disjunkt.",
        r"Abhängig und disjunkt.",
        r"Abhängig und nicht disjunkt."
    ],
    "correct_idx": 2,
    "solution": {
        "de": r"""**Richtig: (c)**

### Study.Smart Guide
**Intuition:**
Primzahlen: 2, 3, 5, 7, 11, ...
Der Schlüssel: Die **2** ist die *einzige* gerade Primzahl. Alle anderen sind ungerade.
*   **Ereignis B (Alle ungerade):** Das bedeutet, die 2 wurde NICHT gezogen.
    Summe von 4 Ungeraden = Gerade. (z.B. 3+5+7+11 = 26).
    Also: Wenn B eintritt, ist die Summe GERADE.
*   **Ereignis A (Summe ungerade):** Eine Summe ist nur ungerade, wenn eine *ungerade Anzahl* von Summanden ungerade ist (z.B. 1 oder 3).
    Da wir nur eine einzige gerade Zahl (2) haben, tritt A nur ein, wenn wir genau diese eine gerade Zahl (2) und 3 ungerade Zahlen gezogen haben.
    (Summe = 2 + U + U + U = Gerade + U = Ungerade).

**Fazit:**
*   A passiert $\iff$ 2 ist dabei.
*   B passiert $\iff$ 2 ist NICHT dabei.
*   Sie können niemals gleichzeitig passieren ($A \cap B = \emptyset$). Sie sind **disjunkt**.
*   Disjunkte Ereignisse (mit $P>0$) sind extrem **abhängig** (Wenn A passiert, wissen wir sicher, dass B nicht passiert ist).

---
### Offizielle Lösung
Also A tritt ein gdw. die 2 dabei ist. B tritt ein gdw. die 2 NICHT dabei ist.<br>A und B sind disjunkt ($A \cap B = \emptyset$). Disjunkte Ereignisse mit $P>0$ sind abhängig.""",
        "en": r"""**Correct: (c)**

### Study.Smart Guide
**Logic:**
*   **Primes:** Only '2' is even.
*   **Sum of 4 Odds:** Always Even. So if B (all odd) happens, A (sum odd) CANNOT happen.
*   **Conclusion:** They are Mutually Exclusive (Disjoint).
*   Disjoint events are Dependent (knowing one occurred gives info about the other - namely that it didn't).

---
### Official Solution
Only one even prime (2).<br>If B (all odd), Sum is even -> A is False. Disjoint.<br>Disjoint implies dependent."""
    }
}

hs2024_mc6 = {
    "source": "HS 2024 Januar, MC #6 (4 Punkte)",
    "type": "mc",
    "question": {
        "de": r"Interview $P(I)=0.1$. Gute Note $G$. $P(G|I)=0.9$, $P(G|\bar{I})=0.2$. Gesucht $P(G)$.",
        "en": r"Interview $P(I)=0.1$. Good grade $G$. $P(G|I)=0.9$, $P(G|\bar{I})=0.2$. Find $P(G)$."
    },
    "options": [
        r"18%",
        r"25%",
        r"27%",
        r"50%"
    ],
    "correct_idx": 2,
    "solution": {
        "de": r"""**Richtig: (c)**

### Study.Smart Guide
**Satz der totalen Wahrscheinlichkeit:**
Die Wahrscheinlichkeit für eine Gute Note setzt sich zusammen aus den zwei Wegen (mit Interview und ohne):
1.  Weg 1: Interview + Gute Note = $0.1 \cdot 0.9 = 0.09$.
2.  Weg 2: Kein Interview + Gute Note = $0.9 \cdot 0.2 = 0.18$.
3.  Summe: $0.09 + 0.18 = 0.27$.

---
### Offizielle Lösung
Totale Wahrscheinlichkeit: $P(G) = 0.9 \cdot 0.1 + 0.2 \cdot 0.9 = 0.09 + 0.18 = 0.27$.""",
        "en": r"""**Correct: (c)**

### Study.Smart Guide
**Total Probability:**
$P(G) = P(G|I)P(I) + P(G|\text{No } I)P(\text{No } I)$
$= 0.9(0.1) + 0.2(0.9) = 0.09 + 0.18 = 0.27$.

---
### Official Solution
$P(G) = 0.09 + 0.18 = 0.27$."""
    }
}

hs2024_mc7 = {
    "source": "HS 2024 Januar, MC #7 (4 Punkte)",
    "type": "mc",
    "question": {
        "de": r"$f_Y(y) = \frac{1}{2}\sin(y)$ für $0 < y < \pi$. Erwartungswert $E[Y]$?",
        "en": r"$f_Y(y) = \frac{1}{2}\sin(y)$ for $0 < y < \pi$. Expectation $E[Y]$?"
    },
    "options": [
        r"$\ln(\pi)$",
        r"$\pi/2$",
        r"$\sqrt{2\pi}$",
        r"$3\pi/2$"
    ],
    "correct_idx": 1,
    "solution": {
        "de": r"""**Richtig: (b)**

### Study.Smart Guide
**Trick (Symmetrie):**
Die Sinus-Funktion ist im Intervall $[0, \pi]$ vollkommen symmetrisch um die Mitte ($\pi/2$).
Der "Schwerpunkt" (Erwartungswert) einer symmetrischen Fläche liegt immer in der Mitte.
Keine Integration nötig! $E = \pi/2$.

**Falls du integrieren willst:**
$\int_0^\pi y \cdot 0.5 \sin(y) dy$.
Partielle Integration... mühsam.

---
### Offizielle Lösung
Symmetrie um $\pi/2$. Dichte ist symmetrisch, also $E[Y] = \pi/2$.<br>Rechnung: $\int_0^\pi y \frac{1}{2}\sin y dy = \frac{1}{2} [\sin y - y \cos y]_0^\pi = \frac{1}{2} (0 - \pi(-1)) = \pi/2$.""",
        "en": r"""**Correct: (b)**

### Study.Smart Guide
**Intuition:**
The Sine function on $[0, \pi]$ is symmetric around $\pi/2$.
Therefore, expectated value (center of mass) is $\pi/2$.

---
### Official Solution
Symmetry around $\pi/2$."""
    }
}

hs2024_mc8 = {
    "source": "HS 2024 Januar, MC #8 (4 Punkte)",
    "type": "mc",
    "question": {
        "de": r"$X \sim N(\mu, 5)$. Test $H_0: \mu=8$ vs $H_1: \mu \neq 8$. $n=5$. $\hat{\mu}=4.95$. p-Wert?",
        "en": r"$X \sim N(\mu, 5)$. Test $H_0: \mu=8$ vs $H_1: \mu \neq 8$. $n=5$. $\hat{\mu}=4.95$. p-value?"
    },
    "options": [
        r"0.0011",
        r"0.0022",
        r"0.1738",
        r"0.3476"
    ],
    "correct_idx": 1,
    "solution": {
        "de": r"""**Richtig: (b)**

### Study.Smart Guide
**Schritt-für-Schritt:**
1.  **Teststatistik:**
    Wir haben Varianz 5 für eine Einzelbeobachtung (Notation $N(\mu, \sigma^2)$). Also $\sigma^2=5$.
    Standardfehler $SE = \frac{\sqrt{5}}{\sqrt{5}} = 1$.
    Abstand zum Nullwert: $4.95 - 8 = -3.05$.
    $Z = -3.05 / 1 = -3.05$.
2.  **p-Wert (zweiseitig):**
    Wir suchen die Wahrscheinlichkeit, so extrem (oder noch extremer) zu sein. Da $H_1: \mu \neq 8$, schauen wir nach links und rechts.
    $P(Z < -3.05)$ aus Tabelle $\approx 0.0011$.
    Mal 2 nehmen (beide Seiten): $2 \cdot 0.0011 = 0.0022$.

---
### Offizielle Lösung
$z = \frac{4.95 - 8}{\sqrt{5}/\sqrt{5}} = \frac{-3.05}{1} = -3.05$.<br>Zweiseitiger Test: $p = 2 \cdot P(Z < -3.05) = 2 \cdot (1 - \Phi(3.05)) = 2 \cdot (1 - 0.9989) = 2 \cdot 0.0011 = 0.0022$.""",
        "en": r"""**Correct: (b)**

### Study.Smart Guide
**Calculation:**
1.  $Z = (4.95 - 8) / (\sqrt{5}/\sqrt{5}) = -3.05$.
2.  One-sided p-value: $P(Z < -3.05) \approx 0.0011$.
3.  Two-sided: $2 \times 0.0011 = 0.0022$.

---
### Official Solution
$z = -3.05$. Two-sided p-value: $2 \cdot 0.0011 = 0.0022$."""
    }
}

hs2024_mc9 = {
    "source": "HS 2024 Januar, MC #9 (4 Punkte)",
    "type": "mc",
    "question": {
        "de": r"Lognormal $\ln(X) \sim N(8, 4)$. Wahrscheinlichkeit $X < 12000$?",
        "en": r"Lognormal $\ln(X) \sim N(8, 4)$. Probability $X < 12000$?"
    },
    "options": [
        r"0.242",
        r"0.363",
        r"0.637",
        r"0.758"
    ],
    "correct_idx": 3,
    "solution": {
        "de": r"""**Richtig: (d)**

### Study.Smart Guide
**Intuition:**
Eine Lognormal-Verteilung zu berechnen ist schwer.
Trick: Logarithmieren! Dann haben wir eine normale Normalverteilung.
$P(X < 12000) \iff P(\ln X < \ln 12000)$.

**Schritt-für-Schritt:**
1.  Grenzwert transformieren: $\ln(12000) \approx 9.39$.
2.  Verteilung: $\ln X \sim N(8, 4)$. Also $\mu=8, \sigma=2$.
3.  Z-Score:
    $$Z = \frac{9.39 - 8}{2} = \frac{1.39}{2} \approx 0.70$$
4.  Tabelle $\Phi(0.70) \approx 0.758$.

---
### Offizielle Lösung
$P(X < 12000) = P(\ln X < \ln 12000) = P(Z < \frac{9.39 - 8}{2}) = P(Z < 0.696)$.<br>$\Phi(0.70) \approx 0.758$.""",
        "en": r"""**Correct: (d)**

### Study.Smart Guide
**Step-by-Step:**
1.  Log-Transform limit: $\ln(12000) \approx 9.39$.
2.  Standardize: $Z = (9.39 - 8) / 2 = 0.695$.
3.  Lookup $\Phi(0.70) \approx 0.758$.

---
### Official Solution
Standardize $\ln(X)$: $z = \frac{\ln(12000)-8}{2} \approx 0.7$. Phi(0.7) = 0.758."""
    }
}

hs2024_mc10 = {
    "source": "HS 2024 Januar, MC #10 (4 Punkte)",
    "type": "mc",
    "question": {
        "de": r"Ruben wartet auf Sequenz (1, 1). Jochen wartet auf (1, 2). Wer braucht im Durchschnitt länger?",
        "en": r"Ruben waits for sequence (1, 1). Jochen waits for (1, 2). Who takes longer on average?"
    },
    "options": [
        r"Ruben braucht länger.",
        r"Jochen braucht länger.",
        r"Beide gleich.",
        r"Nicht bestimmbar."
    ],
    "correct_idx": 0,
    "solution": {
        "de": r"""**Richtig: (a)**

### Study.Smart Guide
**Intuition ("Überlappungs-Penalty"):**
Stell dir vor, du hast die erste Zahl geschafft (eine 1).
*   **Fall Ruben (1,1):** Du würfelst eine 2. Mist! Du hast "1-2". Das ist nicht das Ziel und nicht mal ein Anfang. Du musst komplett von vorne beginnen.
*   **Fall Jochen (1,2):** Du würfelst eine 1. Mist! Du hast "1-1". Das ist nicht das Ziel (1-2), ABER: Du hast immer noch eine "1" am Ende. Du bist also immer noch "halb fertig". Das Scheitern wirft dich nicht ganz zurück.

Da Jochen beim Scheitern "weicher fällt", kommt er im Schnitt schneller ans Ziel. Ruben braucht Länger.

**Formel (ABRACADABRA-Theorem):**
$E = 6^2 + 6^1 = 36+6=42$ für (1,1) (Selbst-Overlap).
$E = 6^2 = 36$ für (1,2) (Kein Overlap).

---
### Offizielle Lösung
Ruben (1,1): Wenn man 1 würfelt und dann keine 1, muss man von vorne anfangen. <br>Jochen (1,2): Wenn man 1 würfelt und dann 1 (statt 2), ist man immer noch 'im Spiel' für den Start der Sequenz.<br>$E_{11} = 6+36=42$, $E_{12} = 36$. (Bekanntes Resultat).""",
        "en": r"""**Correct: (a)**

### Study.Smart Guide
**Intuition:**
Ruben's target (1,1) overlaps with itself. A failure during the sequence is more costly.
Jochen's target (1,2) doesn't overlap. Rolling a '1' when you needed a '2' (sequence 1-1) keeps you in the game (you still have a starting '1').
So Jochen is faster. Ruben takes longer.

---
### Official Solution
Sequence (1,1) overlaps with itself, making it harder to restart. $E[1,1] = 6^2+6=42$. $E[1,2]=6^2=36$."""
    }
}

hs2024_mc11 = {
    "source": "HS 2024 Januar, MC #11 (4 Punkte)",
    "type": "mc",
    "question": {
        "de": r"Münzwurf n Runden. X: Rubens Gewinn. Y: Jochens Gewinn. (X = -Y). Welche Aussage ist wahr?",
        "en": r"Coin toss n rounds. X: Ruben's gain. Y: Jochen's gain (X = -Y). Which is true?"
    },
    "options": [
        r"X und Y haben dieselbe Verteilung.",
        r"X = Y",
        r"X und Y sind unabhängig.",
        r"Keine der obigen."
    ],
    "correct_idx": 0,
    "solution": {
        "de": r"""**Richtig: (a)**

### Study.Smart Guide
**Intuition (Symmetrie):**
Bei einem fairen Münzwurf ist ein Gewinn von +10 genauso wahrscheinlich wie ein Gewinn von -10 (Verlust).
Das Histogramm der möglichen Gewinne ist perfekt spiegelbildlich um die 0.
Wenn man eine symmetrische Verteilung an der y-Achse spiegelt ($Y = -X$), sieht sie exakt gleich aus.
Daher haben $X$ und $Y$ dieselbe Verteilung ("gestapelte Histogramme decken sich"), auch wenn $X$ und $Y$ nie den gleichen Wert haben (wenn einer gewinnt, verliert der andere).

---
### Offizielle Lösung
Symmetrischer Random Walk um 0. Verteilung von X ist symmetrisch ($P(X=k) = P(X=-k)$).<br>Da $Y=-X$, ist die Verteilung identisch.""",
        "en": r"""**Correct: (a)**

### Study.Smart Guide
**Intuition:**
Fair coin tosses create a symmetric distribution centered at 0.
Flipping a symmetric shape left-to-right (multiplying by -1) results in the exact same shape.
So Distribution(X) = Distribution(-X).

---
### Official Solution
Symmetric random walk. Distribution is symmetric around 0, so $f(x) = f(-x)$. Thus $X \sim -X \sim Y$."""
    }
}

hs2024_mc12 = {
    "source": "HS 2024 Januar, MC #12 (4 Punkte)",
    "type": "mc",
    "question": {
        "de": r"Brunnen 10L. Täglich Entnahme $U[0, 1]$. Durchschnittliche Tage bis leer?",
        "en": r"Well 10L. Daily removal $U[0, 1]$. Avg days until empty?"
    },
    "options": [
        r"12.5",
        r"15",
        r"17.5",
        r"20"
    ],
    "correct_idx": 3,
    "solution": {
        "de": r"""**Richtig: (d)**

### Study.Smart Guide
**Intuition:**
Im Durchschnitt entnehmen wir 0.5 Liter pro Tag (Mittelwert von $U[0,1]$).
Wie viele 0.5-Liter-Portionen passen in 10 Liter?
$10 / 0.5 = 20$.

**Hintergrund:**
Dies folgt aus der Wald'schen Identität für Stoppzeiten (oder einfachem Menschenverstand für Erwartungswerte).

---
### Offizielle Lösung
Wald'sche Gleichung / Approximation: $E[S_n] = 10$. $n \cdot E[X] = 10$.<br>$E[X] = 0.5$. $n = 10 / 0.5 = 20$.""",
        "en": r"""**Correct: (d)**

### Study.Smart Guide
**Intuition:**
Average removal per day = 0.5L.
Total Capacity = 10L.
Days needed = Total / Avg Rate = 10 / 0.5 = 20.

---
### Official Solution
$n \cdot \mu = 10 \to n \cdot 0.5 = 10 \to n = 20$."""
    }
}
