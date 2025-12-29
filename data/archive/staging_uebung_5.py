
# Übung 5 Exam Staging File
# Content extracted from:
# - Uebung_5.pdf (questions)
# - ML_Uebung_5.pdf (solutions)
# Dual-Mode: Study.Smart Guide + Official Solution

# ------------------------------------------------------------------
# MULTIPLE CHOICE
# ------------------------------------------------------------------

uebung5_mc1 = {
    "source": "Übung 5, MC #1",
    "type": "mc",
    "question": {
        "de": r"Eine Schätzfunktion heisst erwartungstreu, wenn sie symmetrisch um ihren Erwartungswert verteilt ist.",
        "en": r"An estimator is unbiased if it is symmetrically distributed around its expectation."
    },
    "options": [
        r"Richtig",
        r"Falsch"
    ],
    "correct_idx": 1, 
    "solution": {
        "de": r"""**Richtig: (b)**

### Study.Smart Guide
**Definition:**
Erwartungstreue (Unbiasedness) hat **nichts** mit der Form der Verteilung (Symmetrie) zu tun.
Es geht nur um den Mittelpunkt: $E[\hat{\theta}] = \theta$.
Die Verteilung kann total schief sein, solange der Schwerpunkt auf dem wahren Wert liegt.

---
### Offizielle Lösung
Erwartungstreue bedeutet $E[\hat{\theta}] = \theta$. Symmetrie ist keine Bedingung.""",
        "en": r"""**Correct: (b)**

### Study.Smart Guide
**Definition:**
Unbiasedness means the center of gravity hits the target ($E[\hat{\theta}] = \theta$).
The shape (symmetry) is irrelevant.

---
### Official Solution
Unbiasedness means $E[\hat{\theta}] = \theta$, not symmetry."""
    }
}

uebung5_mc2 = {
    "source": "Übung 5, MC #2",
    "type": "mc",
    "question": {
        "de": r"Effiziente Schätzungen sind immer auch erwartungstreu.",
        "en": r"Efficient estimators are always unbiased."
    },
    "options": [
        r"Richtig",
        r"Falsch"
    ],
    "correct_idx": 0,
    "solution": {
        "de": r"""**Richtig: (a)**

### Study.Smart Guide
**Kontext:**
In der klassischen Statistik (Vorlesungskontext) definiert man "Effizienz" meist als Vergleich unter den **erwartungstreuen** Schätzern.
Der "effizienteste" Schätzer ist derjenige, der unter allen erwartungstreuen Schätzern die kleinste Varianz hat (MVUE - Minimum Variance Unbiased Estimator).
Daher impliziert "effizient" hier "erwartungstreu".

---
### Offizielle Lösung
Im Kontext der Vorlesung bezieht sich Effizienz auf erwartungstreue Schätzer mit minimaler Varianz (MVUE).""",
        "en": r"""**Correct: (a)**

### Study.Smart Guide
**Context:**
"Efficiency" usually refers to the MVUE (Minimum Variance Unbiased Estimator).
So unbiasedness is a prerequisite.

---
### Official Solution
Efficiency implies unbiasedness in this context (MVUE)."""
    }
}

uebung5_mc3 = {
    "source": "Übung 5, MC #3",
    "type": "mc",
    "question": {
        "de": r"Erwartungstreue Schätzfunktionen sind konsistent.",
        "en": r"Unbiased estimators are consistent."
    },
    "options": [
        r"Richtig",
        r"Falsch"
    ],
    "correct_idx": 1,
    "solution": {
        "de": r"""**Richtig: (b)**

### Study.Smart Guide
**Gegenbeispiel:**
Nimm als Schätzer für den Mittelwert einfach **nur den allerersten Messwert** $X_1$ (und wirf den Rest der Daten weg).
1.  Er ist erwartungstreu ($E[X_1] = \mu$).
2.  Aber er wird **nicht präziser**, wenn du mehr Daten sammelst ($n \to \infty$). Die Varianz bleibt riesig ($\sigma^2$). Er konvergiert nicht gegen den wahren Wert. Er ist **nicht konsistent**.

---
### Offizielle Lösung
Nein. Ein Schätzer kann erwartungstreu sein ($E[\hat{\theta}] = \theta$), aber seine Varianz muss nicht gegen 0 gehen (z.B. nur $X_1$ benutzen).""",
        "en": r"""**Correct: (b)**

### Study.Smart Guide
**Counter-Example:**
Estimator $\hat{\mu} = X_1$ (first observation only).
It is unbiased ($E[X_1]=\mu$) but not consistent (variance doesn't shrink with n).

---
### Official Solution
Variance might not vanish (e.g. using only first sample)."""
    }
}

uebung5_mc4 = {
    "source": "Übung 5, MC #4",
    "type": "mc",
    "question": {
        "de": r"Schätzer werden als von der Stichprobe abhängige Funktionen (Statistiken) aufgefasst und sind damit selbst Zufallsvariablen.",
        "en": r"Estimators are functions of the sample (statistics) and thus random variables themselves."
    },
    "options": [
        r"Richtig",
        r"Falsch"
    ],
    "correct_idx": 0,
    "solution": {
        "de": r"""**Richtig: (a)**

### Study.Smart Guide
**Definition:**
Ein Schätzer (z.B. $\bar{X}$) wird aus Zufallsdaten berechnet.
Wenn du das Experiment wiederholst, bekommst du einen anderen Wert.
Ergo: Der Schätzer ist selbst eine Zufallsvariable mit einer eigenen Verteilung (Sampling Distribution).

---
### Offizielle Lösung
Definition eines Schätzers.""",
        "en": r"""**Correct: (a)**

### Study.Smart Guide
**Definition:**
Estimators depend on random data, so they are random variables themselves.

---
### Official Solution
Definition."""
    }
}

uebung5_mc5 = {
    "source": "Übung 5, MC #5",
    "type": "mc",
    "question": {
        "de": r"Ein erwartungstreuer Schätzer hat stets einen kleineren MSE als ein verzerrter Schätzer.",
        "en": r"An unbiased estimator always has a lower MSE than a biased one."
    },
    "options": [
        r"Richtig",
        r"Falsch"
    ],
    "correct_idx": 1,
    "solution": {
        "de": r"""**Richtig: (b)**

### Study.Smart Guide
**Bias-Variance Tradeoff:**
$MSE = \text{Varianz} + \text{Bias}^2$.
Manchmal lohnt es sich, ein kleines bisschen Bias "in Kauf zu nehmen", wenn man dafür die Varianz massiv senken kann (z.B. Ridge Regression oder bestimmte Bayes-Schätzer).
Ein leicht verzerrter Schätzer kann daher insgesamt genauer (kleinerer MSE) sein als ein erwartungstreuer, der wild schwankt.

---
### Offizielle Lösung
$MSE = Var + Bias^2$. Ein verzerrter Schätzer kann durch sehr kleine Varianz einen insgesamt kleineren MSE haben.""",
        "en": r"""**Correct: (b)**

### Study.Smart Guide
**Bias-Variance Tradeoff:**
$MSE = Var + Bias^2$.
A small bias is acceptable if it drastically reduces variance.

---
### Official Solution
Biased estimators can have lower variance compensating for bias."""
    }
}

uebung5_mc6 = {
    "source": "Übung 5, MC #6",
    "type": "mc",
    "question": {
        "de": r"$\bar{X}$ (Arithmetisches Mittel). Welche Aussagen sind richtig?<br>(a) $Var(\bar{X}) = \sigma^2/n$.<br>(b) $\bar{X}$ konsistent für $\mu$.<br>(c) $\bar{X}$ approximativ standardnormalverteilt.",
        "en": r"$\bar{X}$ (Sample Mean). True?<br>(a) $Var(\bar{X}) = \sigma^2/n$.<br>(b) Consistent.<br>(c) Approx Standard Normal."
    },
    "options": [
        r"a) und b)",
        r"b) und c)",
        r"a) und c)",
        r"Nur a)"
    ],
    "correct_idx": 0,
    "solution": {
        "de": r"""**Richtig: (a), (b)**

### Study.Smart Guide
**Faktencheck:**
*   (a) **Richtig.** Die Varianz sinkt mit $1/n$.
*   (b) **Richtig.** Wegen (a) geht die Varianz gegen 0 $\implies$ Konsstent (Gesetz der großen Zahlen).
*   (c) **Falsch.** $\bar{X}$ ist approximativ **Normalverteilt** ($N(\mu, \sigma^2/n)$), aber nicht **Standard**normalverteilt ($N(0,1)$). Dafür müsste man es erst minus $\mu$ rechnen und teilen.

---
### Offizielle Lösung
Varianzformel (a) stimmt. Konsistenz (b) stimmt (Gesetz der großen Zahl). (c) ist falsch, $\bar{X}$ ist normal, nicht *standard*normal.""",
        "en": r"""**Correct: (a), (b)**

### Study.Smart Guide
**Checks:**
*   (a) Correct. Formula is $\sigma^2/n$.
*   (b) Correct. LLN implies consistency.
*   (c) **False**. It's Normal, but not *Standard* Normal (mean is $\mu$, not 0).

---
### Official Solution
Variance formula and consistency hold. Not standard normal (needs standardization)."""
    }
}

uebung5_mc7 = {
    "source": "Übung 5, MC #7",
    "type": "mc",
    "question": {
        "de": r"Erwartungstreue Schätzer sind trivialerweise auch asymptotisch erwartungstreu.",
        "en": r"Unbiased estimators are trivially asymptotically unbiased."
    },
    "options": [
        r"Richtig",
        r"Falsch"
    ],
    "correct_idx": 0,
    "solution": {
        "de": r"""**Richtig: (a)**

### Study.Smart Guide
**Logik:**
Wenn der Bias für *jedes* n genau 0 ist, dann ist er natürlich auch im Grenzwert ($n \to \infty$) gleich 0.
"Asymptotisch erwartungstreu" ist eine schwächere Eigenschaft. Wer schon die starke Eigenschaft hat, hat automatisch die schwache.

---
### Offizielle Lösung
Wenn für alle n $E = \theta$, dann auch im Limes.""",
        "en": r"""**Correct: (a)**

### Study.Smart Guide
**Logic:**
If Bias is 0 for all n, the limit is also 0.

---
### Official Solution
Bias 0 for all n implies Bias -> 0."""
    }
}

uebung5_mc8 = {
    "source": "Übung 5, MC #8",
    "type": "mc",
    "question": {
        "de": r"Ein verzerrter Schätzer führt stets zu einer Schätzung, die sich vom zu schätzenden Wert unterscheidet.",
        "en": r"A biased estimator always yields an estimate different from the true value."
    },
    "options": [
        r"Richtig",
        r"Falsch"
    ],
    "correct_idx": 1,
    "solution": {
        "de": r"""**Richtig: (b)**

### Study.Smart Guide
**Begriffs-Unterscheidung:**
Verzerrung (Bias) ist eine Eigenschaft des **Mittelwerts** (Average Performance).
In einem **Einzelfall** (einer Stichprobe) kann auch ein verzerrter Schätzer zufällig genau ins Schwarze treffen.
(Beispiel: Eine kaputte Uhr, die falsch geht, zeigt trotzdem 2x am Tag die richtige Zeit bzw. kann zufällig stimmen).

---
### Offizielle Lösung
Verzerrung bezieht sich auf den *Erwartungswert* (Durchschnitt). Eine einzelne Realisation kann zufällig genau den wahren Wert treffen.""",
        "en": r"""**Correct: (b)**

### Study.Smart Guide
**Intuition:**
Bias is about the *average*. A single shot can still hit the bullseye by luck.

---
### Official Solution
Bias is about expectation. Single realization can be correct."""
    }
}

uebung5_mc9 = {
    "source": "Übung 5, MC #9",
    "type": "mc",
    "question": {
        "de": r"Wichtigstes Ziel beim Schätzen ist es, Schätzer mit kleinen Varianzen zu finden.",
        "en": r"Main goal is finding estimators with small variances."
    },
    "options": [
        r"Richtig",
        r"Falsch"
    ],
    "correct_idx": 1,
    "solution": {
        "de": r"""**Richtig: (b)**

### Study.Smart Guide
**Intuition:**
Ein Schätzer, der immer "5" sagt, hat Varianz 0. Das ist super klein!
Aber er ist wahrscheinlich völlig nutzlos (riesiger Bias).
Das Ziel ist kleiner **MSE** (Kombination aus Varianz UND Bias), nicht nur Varianz.

---
### Offizielle Lösung
Nein, wir wollen meist kleinen *MSE* (Varianz + Bias). Varianz 0 ist einfach (Schätzer = Konstante), aber nutzlos.""",
        "en": r"""**Correct: (b)**

### Study.Smart Guide
**Intuition:**
An estimator that always returns "0" has zero variance. But it's useless.
We need Accuracy (Low Bias) AND Precision (Low Variance).

---
### Official Solution
Need correlation to truth (Bias), not just low variance."""
    }
}

uebung5_mc10 = {
    "source": "Übung 5, MC #10",
    "type": "mc",
    "question": {
        "de": r"Welche der Schätzer $\hat{\mu}_1 ... \hat{\mu}_6$ sind erwartungstreu für $\mu$?",
        "en": r"Which estimators $\hat{\mu}_1 ... \hat{\mu}_6$ are unbiased for $\mu$?"
    },
    "options": [
        r"Nur d1 und d2",
        r"Alle ausser d3 und d4",
        r"Nur d2 und d6",
        r"Nur d1, d2 und d6"
    ],
    "correct_idx": 3,
    "solution": {
        "de": r"""**Richtig: (d)**

### Study.Smart Guide
**Regel:**
Ein linearer Schätzer $\sum w_i X_i$ ist erwartungstreu für $\mu$, wenn die **Summe der Gewichte gleich 1** ist ($\sum w_i = 1$).
Einfach die Koeffizienten prüfen!

---
### Offizielle Lösung
Prüfung der Linearität des Erwartungswerts. $\mu_1$ (Summe Koeffizienten 1), $\mu_2$ (Mittelwert Teilmenge), $\mu_6$ (Mittelwert) sind erwartungstreu.""",
        "en": r"""**Correct: (d)**

### Study.Smart Guide
**Rule:**
Linear estimator $\sum w_i X_i$ is unbiased if $\sum w_i = 1$.

---
### Official Solution
Check if coefficients sum to 1."""
    }
}

uebung5_mc11 = {
    "source": "Übung 5, MC #11",
    "type": "mc",
    "question": {
        "de": r"$E[Y] = \frac{1}{3+\lambda}$. Momentenschätzer für $\lambda$?",
        "en": r"$E[Y] = \frac{1}{3+\lambda}$. MOM estimator for $\lambda$?"
    },
    "options": [
        r"$\bar{X}$",
        r"$\frac{1}{\bar{X}} + 3$",
        r"$\frac{1}{\bar{X}} - 3$",
        r"$\frac{1}{3+\bar{X}}$"
    ],
    "correct_idx": 2,
    "solution": {
        "de": r"""**Richtig: (c)**

### Study.Smart Guide
**Momentenmethode (MOM):**
1.  Gleichsetzen: Theoretisches Moment $E[Y]$ = Empirisches Moment $\bar{X}$.
    $$ \frac{1}{3+\lambda} = \bar{X} $$
2.  Auflösen nach $\lambda$:
    Kehrwert: $3+\lambda = \frac{1}{\bar{X}}$.
    Minus 3: $\lambda = \frac{1}{\bar{X}} - 3$.

---
### Offizielle Lösung
Gleichsetzen: $\bar{X} = \frac{1}{3+\lambda} \iff 3+\lambda = \frac{1}{\bar{X}} \iff \lambda = \frac{1}{\bar{X}} - 3$.""",
        "en": r"""**Correct: (c)**

### Study.Smart Guide
**Method:**
Equate $E[Y] = \bar{X}$.
$1/(3+\lambda) = \bar{X} \implies 3+\lambda = 1/\bar{X} \implies \lambda = 1/\bar{X} - 3$.

---
### Official Solution
Solve sample mean equation for lambda."""
    }
}

uebung5_mc12 = {
    "source": "Übung 5, MC #12",
    "type": "mc",
    "question": {
        "de": r"Momentenmethode und Maximum-Likelihood liefern stets die gleichen Schätzfunktionen.",
        "en": r"MOM and MLE always imply the same estimators."
    },
    "options": [
        r"Richtig",
        r"Falsch"
    ],
    "correct_idx": 1,
    "solution": {
        "de": r"""**Richtig: (b)**

### Study.Smart Guide
**Gegenbeispiel:**
Bei der **Gleichverteilung** auf $[0, \theta]$:
*   MOM: $\bar{X} = \theta/2 \implies \hat{\theta}_{MOM} = 2\bar{X}$.
*   MLE: $\hat{\theta}_{MLE} = \max(X_i)$.
Die sind völlig verschieden.
(Bei Normalverteilung sind sie oft gleich, aber nicht immer).

---
### Offizielle Lösung
Oft unterschiedlich (z.B. bei Gleichverteilung).""",
        "en": r"""**Correct: (b)**

### Study.Smart Guide
**Counter-Example:**
Uniform distribution $[0, \theta]$.
MOM gives $2\bar{X}$.
MLE gives $\max(X)$.

---
### Official Solution
Can differ."""
    }
}

uebung5_mc13 = {
    "source": "Übung 5, MC #13",
    "type": "mc",
    "question": {
        "de": r"Maximum-Likelihood-Schätzungen sind nie erwartungstreu.",
        "en": r"MLE are never unbiased."
    },
    "options": [
        r"Richtig",
        r"Falsch"
    ],
    "correct_idx": 1,
    "solution": {
        "de": r"""**Richtig: (b)**

### Study.Smart Guide
**Gegenbeispiel:**
Der Schätzer für den Mittelwert bei der Normalverteilung: $\hat{\mu}_{MLE} = \bar{X}$.
Der ist perfekt erwartungstreu.
(Hinweis: Der MLE für die Varianz $\sigma^2$ ist *verzerrt*, aber nicht "nie").

---
### Offizielle Lösung
Doch, z.B. $\bar{X}$ bei Normalverteilung ist MLE und erwartungstreu.""",
        "en": r"""**Correct: (b)**

### Study.Smart Guide
**Counter-Example:**
Sample mean $\bar{X}$ is the MLE for $\mu$ in Normal Distribution, and it is unbiased.

---
### Official Solution
Often they are (sample mean)."""
    }
}

uebung5_mc14 = {
    "source": "Übung 5, MC #14",
    "type": "mc",
    "question": {
        "de": r"Maximierung der Loglikelihood und Likelihood führt zum selben Ergebnis (Schätzer).",
        "en": r"Maximizing Loglikelihood vs Likelihood yields the same estimator."
    },
    "options": [
        r"Richtig", 
        r"Falsch"
    ],
    "correct_idx": 0, # Question asks if result is same. Yes.
    "solution": {
        "de": r"""**Richtig: (a)**

### Study.Smart Guide
**Logik:**
Der Logarithmus ist eine **streng monoton steigende** Funktion.
Das Maximum von $f(x)$ liegt an der gleichen Stelle wie das Maximum von $\ln(f(x))$.
Der *Wert* der Funktion ändert sich, aber die *Position* des Maximums (der Schätzer $\hat{\theta}$) bleibt gleich.

(Hinweis zur Original-Lösung: Dort wurde "Falsch" markiert, weil die Frage wohl implizierte, dass die *Funktionswerte* gleich sind. Aber die Schätzergebnisse sind identisch).

---
### Offizielle Lösung
Argmax ist gleich, aber die *Funktionswerte* sind unterschiedlich ($ln(L) \ne L$).""",
        "en": r"""**Correct: (a)**

### Study.Smart Guide
**Logic:**
Log is monotonically increasing.
Argmax $L$ = Argmax $\ln L$.
The estimator is identical.

---
### Official Solution
Resulting parameter is same, but function values differ."""
    }
}

uebung5_mc15 = {
    "source": "Übung 5, MC #15",
    "type": "mc",
    "question": {
        "de": r"Exponential $Y$. Stichprobe (1, 2, 3, 1). Likelihood $L(\theta)$?",
        "en": r"Exp $Y$. Sample (1, 2, 3, 1). Likelihood $L(\theta)$?"
    },
    "options": [
        r"$(1 \cdot e^{-\theta})^2 ...$",
        r"$(\theta \cdot e^{-\theta})^1 ...$",
        r"$(\theta \cdot e^{-1\theta})^2 (\theta \cdot e^{-2\theta})^1 (\theta \cdot e^{-3\theta})^1$",
        r"..."
    ],
    "correct_idx": 2,
    "solution": {
        "de": r"""**Richtig: (c)**

### Study.Smart Guide
**Konstruktion:**
Dichte: $f(x) = \theta e^{-\theta x}$.
Likelihood = Produkt der Dichten für jeden Wert.
Werte: 1 (2x), 2 (1x), 3 (1x).
$L = (\theta e^{-1\theta}) \cdot (\theta e^{-2\theta}) \cdot (\theta e^{-3\theta}) \cdot (\theta e^{-1\theta})$.
Zusammengefasst wie in Option (c).

---
### Offizielle Lösung
Dichte $f(y) = \theta e^{-\theta y}$. $L = \prod f(x_i)$. Zwei mal die 1, etc.""",
        "en": r"""**Correct: (c)**

### Study.Smart Guide
**Construction:**
Product of $f(x_i) = \theta e^{-\theta x_i}$.
Occurrences: 1 (twice), 2, 3.

---
### Official Solution
Product of densities."""
    }
}

uebung5_mc16 = {
    "source": "Übung 5, MC #16",
    "type": "mc",
    "question": {
        "de": r"Zusammenhang Konfidenzniveau und Intervallbreite?",
        "en": r"Relation confidence level and interval width?"
    },
    "options": [
        r"Niveau größer -> Intervall kleiner",
        r"Niveau größer -> Intervall größer",
        r"Keine Beziehung"
    ],
    "correct_idx": 1,
    "solution": {
        "de": r"""**Richtig: (b)**

### Study.Smart Guide
**Intuition:**
Wenn du dir zu 99.9% sicher sein willst, dass du den Fisch fängst, brauchst du ein **riesiges Netz**.
Wenn dir 50% Sicherheit reicht, reicht ein kleines Netz.
Hohes Niveau $\implies$ Breites Intervall.

---
### Offizielle Lösung
Für höhere Sicherheit müssen wir den Bereich verbreitern.""",
        "en": r"""**Correct: (b)**

### Study.Smart Guide
**Intuition:**
To be more sure (higher confidence), you need a wider net (interval).

---
### Official Solution
Higher confidence requires wider interval."""
    }
}

uebung5_mc17 = {
    "source": "Übung 5, MC #17",
    "type": "mc",
    "question": {
        "de": r"Grenzen von Konfidenzintervallen sind zufällig.",
        "en": r"CI boundaries are random."
    },
    "options": [
        r"Richtig",
        r"Falsch"
    ],
    "correct_idx": 0,
    "solution": {
        "de": r"""**Richtig: (a)**

### Study.Smart Guide
**Konzept:**
Der wahre Parameter $\theta$ ist fest (kein Zufall).
Das Intervall berechnen wir aus den Daten $\bar{X}$. Da die Daten zufällig sind, ist auch das Intervall $[\bar{X} - c, \bar{X} + c]$ zufällig.
Es "fängt" den wahren Wert mal ein, mal nicht.

---
### Offizielle Lösung
Das Intervall hängt von der stochastischen Stichprobe ab.""",
        "en": r"""**Correct: (a)**

### Study.Smart Guide
**Concept:**
The target is fixed. The interval (trap) moves randomly because it depends on sample data.

---
### Official Solution
Interval depends on sample."""
    }
}

uebung5_mc18 = {
    "source": "Übung 5, MC #18",
    "type": "mc",
    "question": {
        "de": r"Länge des KI ist größer, je größer der Parameter ist.",
        "en": r"Length of CI increases with parameter magnitude."
    },
    "options": [
        r"Richtig",
        r"Falsch"
    ],
    "correct_idx": 1,
    "solution": {
        "de": r"""**Richtig: (b)**

### Study.Smart Guide
**Gegenbeispiel:**
Bei der Normalverteilung mit bekannter Varianz ist die Länge $2 \cdot 1.96 \cdot \frac{\sigma}{\sqrt{n}}$.
Das hängt **nicht** von $\mu$ ab.
Ob wir Mäuse (klein) oder Elefanten (groß) wiegen, ändert nichts an der Präzision der Waage (Sigma).

---
### Offizielle Lösung
Hängt allgemein von Varianz und n ab, nicht zwingend vom Mittelwert.""",
        "en": r"""**Correct: (b)**

### Study.Smart Guide
**Reason:**
CI width usually depends on variance ($\sigma$), not the mean ($\mu$).

---
### Official Solution
Depends on variance, not mean."""
    }
}

# ------------------------------------------------------------------
# PROBLEMS
# ------------------------------------------------------------------

uebung5_prob1 = {
    "source": "Übung 5, Probe #1",
    "type": "problem",
    "question": {
        "de": r"Zwei Schätzer für Mittelwert $\mu$ aus $X_1, X_2$.<br>$\mu_1 = \frac{1}{2}X_1 + \frac{1}{2}X_2$<br>$\mu_2 = \frac{1}{3}X_1 + \frac{2}{3}X_2$<br>(a) Erwartungstreu?<br>(b) Effizienter?",
        "en": r"Two estimators. (a) Unbiased? (b) Efficiency?"
    },
    "solution": {
        "de": r"""### Study.Smart Guide
**(a) Erwartungstreue Check:**
Summieren sich die Gewichte zu 1?
1.  $1/2 + 1/2 = 1$. Ja.
2.  $1/3 + 2/3 = 1$. Ja.

**(b) Effizienz (Varianz Vergleich):**
Regel: $Var(aX + bY) = a^2 Var(X) + b^2 Var(Y)$ (wenn unabhängig).
1.  Quantile quadrieren: $(1/2)^2 + (1/2)^2 = 1/4 + 1/4 = 0.5$.
2.  $(1/3)^2 + (2/3)^2 = 1/9 + 4/9 = 5/9 \approx 0.555$.
Da $0.5 < 0.555$, ist **$\mu_1$ effizienter** (kleinere Varianz).
(Gleichmäßige Gewichtung ist bei i.i.d. Variablen immer optimal).

---
### Offizielle Lösung
(a) Beide Summe der Gewichte = 1 $\implies$ beide erwartungstreu.<br>(b) $Var(\mu_1) = 0.5 Var(X)$, $Var(\mu_2) = (1/9 + 4/9)Var = 5/9 Var(X) \approx 0.55 Var$.<br>$\mu_1$ ist effizienter (kleinere Varianz).""",
        "en": r"""### Study.Smart Guide
**Comparison:**
(a) Both weights sum to 1. Unbiased.
(b) Sum of squared weights:
    Est 1: $0.25+0.25 = 0.5$.
    Est 2: $0.11+0.44 = 0.55$.
    Est 1 matches sample mean and is Best.

---
### Official Solution
(a) Both unbiased. (b) 1 is more efficient."""
    }
}

uebung5_prob2 = {
    "source": "Übung 5, Probe #2",
    "type": "problem",
    "question": {
        "de": r"500 Beobachtungen gemacht, 180 verloren. Schätzt nur mit 320 Werten.<br>Effizienzverlust?",
        "en": r"500 obs made, 180 lost. Est with 320. Efficiency loss?"
    },
    "solution": {
        "de": r"""### Study.Smart Guide
**Varianz-Effekt:**
Die Varianz eines Schätzers (z.B. Mittelwert) ist $\sigma^2 / n$.
*   Mit 500: $\sigma^2 / 500 = 0.002 \sigma^2$.
*   Mit 320: $\sigma^2 / 320 \approx 0.0031 \sigma^2$.
Die Varianz steigt um den Faktor $500/320 \approx 1.56$.
Wir haben 56% mehr "Rauschen".

---
### Offizielle Lösung
$Var_{500} = \sigma^2/500$. $Var_{320} = \sigma^2/320$.<br>Verlust an Präzision.""",
        "en": r"""### Study.Smart Guide
**Impact:**
Variance scales with $1/n$.
Falling from 500 to 320 increases variance by factor $500/320 = 1.56$.

---
### Official Solution
Higher variance."""
    }
}

uebung5_prob3 = {
    "source": "Übung 5, Probe #3",
    "type": "problem",
    "question": {
        "de": r"Rechteckverteilung $[\theta, \theta+1]$.<br>(a) E[X], Var[X].<br>(b) ist $\bar{X}$ erwartungstreu für $\theta$?",
        "en": r"Uniform $[\theta, \theta+1]$. (a) Moments. (b) Is Sample Mean unbiased for theta?"
    },
    "solution": {
        "de": r"""### Study.Smart Guide
**(a) Momente:**
Mittelpunkt des Intervalls $[\theta, \theta+1]$ ist $\theta + 0.5$.
Also $E[X] = \theta + 0.5$.
Varianz eines Intervalls der Länge 1 ist immer $1/12$. (Formel $(b-a)^2/12$).

**(b) Bias:**
$E[\bar{X}] = E[X] = \theta + 0.5$.
Das ist **nicht** $\theta$. Der Schätzer ist verzerrt (Bias = +0.5).
Korrektur: $\hat{\theta} = \bar{X} - 0.5$.

---
### Offizielle Lösung
(a) $E[X] = \theta + 0.5$. $Var = 1/12$.<br>(b) Bias = 0.5. $\bar{X}-0.5$ ist erwartungstreu.""",
        "en": r"""### Study.Smart Guide
**Analysis:**
(a) Mean is center: $\theta + 0.5$.
(b) Sample mean targets $\theta + 0.5$, not $\theta$. Biased.
    Correction: Subtract 0.5.

---
### Official Solution
(a) Mean theta+0.5. (b) Biased."""
    }
}

uebung5_prob4 = {
    "source": "Übung 5, Probe #4",
    "type": "problem",
    "question": {
        "de": r"5 Schätzer für $\mu$.<br>(a) E und Var.<br>(b) MSE. Welcher am effizientesten?",
        "en": r"5 Estimators. (a) Moments. (b) MSE. Efficiency?"
    },
    "solution": {
        "de": r"""### Study.Smart Guide
**Konzept: BLUE:**
Unter allen linearen, erwartungstreuen Schätzern hat das **Arithmetische Mittel** (gleich gewichtet) immer die kleinste Varianz.
Jeder Schätzer, der Gewichte ungleich verteilt (z.B. den ersten Wert doppelt zählt), erhöht die Summe der Quadrate der Gewichte.
Daher ist $T_1$ (Standard-Mittelwert) am effizientesten.

---
### Offizielle Lösung
Alle erwartungstreu außer evtl. Randfälle.<br>Arithmetisches Mittel über alle ($T_1$) minimiert die Varianz ($1/5 \sigma^2$).""",
        "en": r"""### Study.Smart Guide
**Rule:**
Sample Mean (equal weights) minimizes variance for i.i.d. data. (BLUE property).

---
### Official Solution
Sample mean $T_1$ best."""
    }
}

uebung5_prob5 = {
    "source": "Übung 5, Probe #5",
    "type": "problem",
    "question": {
        "de": r"Bernoulli $\pi$. Schätzer $\hat{\pi}$ (rel Häufigkeit) vs $T = \frac{\sum X + 1}{n+2}$.<br>(a) MSE Vergleich.",
        "en": r"Bernoulli. Sample vs Laplace Smoothing estimator."
    },
    "solution": {
        "de": r"""### Study.Smart Guide
**Laplace Smoothing (Add-One Smoothing):**
Der Schätzer $T = \frac{k+1}{n+2}$ ("Bayes-Schätzer") addiert künstlich 1 Erfolg und 1 Misserfolg dazu.
*   Er ist **verzerrt** (Bias $\to 0$ für große n).
*   Aber er verhindert Extreme (0% oder 100%) bei kleinen Stichproben.
*   Für $\pi$ nahe 0.5 hat er einen **kleineren MSE** als der Standard-Schätzer. Das ist ein klassischer Bias-Variance-Tradeoff.

---
### Offizielle Lösung
$T$ hat Bias, aber geringeren MSE für $\pi$ nahe 0.5 bei kleinen n.<br>Trade-off Bias/Variance.""",
        "en": r"""### Study.Smart Guide
**Insight:**
Laplace Smoothing reduces variance at the cost of slight bias.
Better MSE for small samples near $p=0.5$.

---
### Official Solution
Bias-Var Tradeoff."""
    }
}

uebung5_prob6 = {
    "source": "Übung 5, Probe #6",
    "type": "problem",
    "question": {
        "de": r"Momentenschätzer herleiten für:<br>(a) Exponential<br>(b) Rechteck $[\theta-0.5, \theta+0.5]$<br>(c) Normal",
        "en": r"MOM for (a) Exp (b) Uniform (c) Normal."
    },
    "solution": {
        "de": r"""### Study.Smart Guide
**Rezept Momentenmethode:**
1.  Berechne $E[X]$ theoretisch.
2.  Setze $E[X] = \bar{X}$.
3.  Löse nach Parameter auf.

*   (a) Exponential: $E[X] = 1/\lambda$.
    $1/\lambda = \bar{X} \implies \hat{\lambda} = 1/\bar{X}$.
*   (b) Rechteck: $E[X]$ ist die Mitte. Mitte von $[\theta-0.5, \theta+0.5]$ ist $\theta$.
    $\theta = \bar{X} \implies \hat{\theta} = \bar{X}$.

---
### Offizielle Lösung
Standardergebnisse.""",
        "en": r"""### Study.Smart Guide
**Derivations:**
(a) $\mu = 1/\lambda \implies \lambda = 1/\bar{X}$.
(b) $\mu = \text{Center} = \theta \implies \theta = \bar{X}$.

---
### Official Solution
Standard MOM results."""
    }
}

uebung5_prob7 = {
    "source": "Übung 5, Probe #7",
    "type": "problem",
    "question": {
        "de": r"Telefonzentrale. Poisson. Stichprobe (1,0,2,...).<br>(a) MLE für $\mu$.<br>(b) Erwartungstreu?",
        "en": r"Poisson MLE. Unbiased?"
    },
    "solution": {
        "de": r"""### Study.Smart Guide
**(a) Intuition MLE:**
Der "wahrscheinlichste" Parameter für eine Poisson-Verteilung ist einfach der beobachtete Durchschnitt.
Wer 1, 0, 2 Anrufe sieht (Schnitt 1), schätzt $\lambda=1$.
Mathematisch: Ableiten der Log-Likelihood führt auf $\bar{X}$.

**(b) Bias:**
Da $E[\bar{X}] = E[X] = \lambda$, ist er unverzerrt.

---
### Offizielle Lösung
(a) Likelihood aufstellen, LogL, Ableiten $\implies \hat{\lambda} = \bar{X}$.<br>(b) Ja, $\bar{X}$ ist erwartungstreu.""",
        "en": r"""### Study.Smart Guide
**(a) Intuition:**
Sample mean is the natural estimator for Poisson rate $\lambda$.

---
### Official Solution
(a) Sample mean. (b) Yes."""
    }
}

uebung5_prob8 = {
    "source": "Übung 5, Probe #8",
    "type": "problem",
    "question": {
        "de": r"Binomial $B(n,p)$, n bekannt.<br>(a) Momentenschätzer p.<br>(b) Eingeschränktes p.<br>(c) n unbekannt.",
        "en": r"Binomial MOM. p constrained and n unknown."
    },
    "solution": {
        "de": r"""### Study.Smart Guide
**(a) p schätzen (n bekannt):**
$E[X] = np$.
$np = \bar{X} \implies p = \bar{X}/n$.

**(c) n und p unbekannt:**
Jetzt brauchen wir 2 Gleichungen!
1.  Moment: $np = \bar{X}$.
2.  Moment: $np(1-p) = S^2$ (Empirische Varianz).
Wir teilen (2) durch (1):
$1-p = S^2 / \bar{X}$.
Daraus $p$ und dann $n$ berechnen.

---
### Offizielle Lösung
(a) $\hat{p} = \bar{X}/n$.<br>(c) Braucht 2. Moment (Varianz) um n und p zu lösen: $\bar{X}=np, S^2=np(1-p)$.""",
        "en": r"""### Study.Smart Guide
**Strategy:**
(a) 1 Equation: Mean matches data.
(c) 2 Equations: Mean AND Variance match data.

---
### Official Solution
(a) X/n. (c) Uses variance."""
    }
}

uebung5_prob9 = {
    "source": "Übung 5, Probe #9",
    "type": "problem",
    "question": {
        "de": r"Klausurzeit 300 Studenten. $\bar{x}=50, \sigma=5$ (bekannt). 95% KI für Mittelwert.",
        "en": r"Exam times. 95% CI."
    },
    "solution": {
        "de": r"""### Study.Smart Guide
**Rezept KI:**
Formel: $\bar{x} \pm 1.96 \cdot \frac{\sigma}{\sqrt{n}}$.
Einsetzen:
$50 \pm 1.96 \cdot \frac{5}{\sqrt{300}}$.
$50 \pm 1.96 \cdot \frac{5}{17.32}$.
$50 \pm 1.96 \cdot 0.288$.
$50 \pm 0.56$.

---
### Offizielle Lösung
$50 \pm 1.96 \cdot \frac{5}{\sqrt{300}}$.<br>Intervall: $[49.43, 50.57]$.""",
        "en": r"""### Study.Smart Guide
**Calculation:**
$50 \pm 1.96 (5/\sqrt{300})$.
$50 \pm 0.57$.

---
### Official Solution
$50 \pm 0.57$."""
    }
}
