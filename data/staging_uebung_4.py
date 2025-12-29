
# Übung 4 Exam Staging File
# Content extracted from:
# - Uebung_4_CLT.pdf (questions)
# - ML_Uebung_4_CLT.pdf (solutions)
# Dual-Mode: Study.Smart Guide + Official Solution

# ------------------------------------------------------------------
# MULTIPLE CHOICE
# ------------------------------------------------------------------

uebung4_mc1 = {
    "source": "Übung 4, MC #1",
    "type": "mc",
    "question": {
        "de": r"Seien $X_1, ..., X_n$ i.i.d. mit endlichem E und Var. $S_n = \sum X_i$. Der Zentrale Grenzwertsatz besagt:",
        "en": r"Let $X_1, ..., X_n$ be i.i.d. with finite mean/var. $S_n = \sum X_i$. CLT states:"
    },
    "options": [
        r"$S_n$ ist approximativ standardnormalverteilt (n > 30).",
        r"Die standardisierte ZV $S_n$ ist approximativ standardnormalverteilt (n > 30).",
        r"$S_n$ ist approximativ normalverteilt (n > 30).",
        r"Die standardisierte ZV $S_n$ ist approximativ normalverteilt (n > 30).",
        r"Die standardisierte ZV $S_n$ ist approximativ standardnormalverteilt (n <= 30)."
    ],
    "correct_idx": 1, 
    "solution": {
        "de": r"""**Richtig: (b), (c), (d)**

### Study.Smart Guide
**Die Feinheit:**
*   (b) ist die präziseste mathematische Formulierung: Wenn man die Summe "zentriert und staucht" (standardisiert), konvergiert ihre Form gegen die Standardnormalverteilung $N(0,1)$.
*   (c) ist die "praktische" Formulierung: Die Summe $S_n$ selbst sieht aus wie eine Glockenkurve, aber mit Mittelwert $n\mu$ und Varianz $n\sigma^2$ (nicht 0 und 1). Die Lösung markiert dies auch als richtig, weil es die Konsequenz ist.
*   (a) ist Falsch! Die Summe $S_n$ wächst mit $n$ (Mittelwert wandert nach rechts), sie kann nicht $N(0,1)$ sein.

---
### Offizielle Lösung
Der ZGS besagt, dass die *standardisierte* Summe gegen $N(0,1)$ konvergiert. Daraus folgt, dass die Summe selbst approximativ normalverteilt ist ($N(n\mu, n\sigma^2)$).""",
        "en": r"""**Correct: (b), (c), (d)**

### Study.Smart Guide
**Nuance:**
*   (b) Precise definition: Standardized sum converges to $N(0,1)$.
*   (c) Practical usage: Sum is approx Normal ($n\mu, n\sigma^2$).
*   (a) False: The sum grows with n, so it cannot stay $N(0,1)$.

---
### Official Solution
Standardized sum converges to N(0,1). Sum is approx Normal."""
    }
}

uebung4_mc2 = {
    "source": "Übung 4, MC #2",
    "type": "mc",
    "question": {
        "de": r"Bedingungen für den Zentralen Grenzwertsatz:",
        "en": r"Conditions for CLT:"
    },
    "options": [
        r"$S_n = X_1 + ... + X_n$.",
        r"$S_n = X_1^2 + ... + X_n^2$.",
        r"$X_i$ sind identisch verteilt.",
        r"$X_i$ sind gleichverteilt.",
        r"$n > 30$."
    ],
    "correct_idx": 2, 
    "solution": {
        "de": r"""**Richtig: (a), (c), (e)**

### Study.Smart Guide
**Checklist:**
1.  **Summe:** Wir summieren Zufallsvariablen (a).
2.  **i.i.d.:** Unabhängig (implizit angenommen in der Basisversion) und **identisch verteilt** (c). Wenn jeder Summand eine völlig andere Verteilung hätte, würde es nicht funktionieren.
3.  **Großes n:** Damit die Approximation gut ist, braucht man genug Summanden. Faustregel $n>30$ (e).
(d) ist falsch, sie müssen nicht *Gleichverteilt* sein, jede Verteilung (die definiert ist) funktioniert.

---
### Offizielle Lösung
Summe von unabhängigen ZV. Identisch verteilt (für die einfache Version). Großes n (Faustregel > 30).""",
        "en": r"""**Correct: (a), (c), (e)**

### Study.Smart Guide
**Checklist:**
1.  Summation (a).
2.  i.i.d. (Identically distributed) (c).
3.  Large Sample Size ($n>30$) (e).

---
### Official Solution
Sum of i.i.d. variables, large n."""
    }
}

uebung4_mc3 = {
    "source": "Übung 4, MC #3",
    "type": "mc",
    "question": {
        "de": r"X, Y unabhängig. Summe Z = X + Y ist:",
        "en": r"X, Y independent. Sum Z = X + Y follows:"
    },
    "options": [
        r"Binomial, wenn X, Y binomial mit selbem p.",
        r"Normalverteilt, wenn X, Y normal mit selben Parametern.",
        r"Standardnormal, wenn X, Y standardnormal.",
        r"Normal, wenn X, Y standardnormal."
    ],
    "correct_idx": 0, 
    "solution": {
        "de": r"""**Richtig: (a), (d)**

### Study.Smart Guide
**Regeln der Addition:**
*   (a) **Binomial:** $B(n, p) + B(m, p) = B(n+m, p)$. ("Ich werfe n mal, dann noch m mal"). Aber nur wenn die Erfolgswahrscheinlichkeit $p$ gleich ist! Richtig.
*   (b) **Normal:** Summe von Normalverteilungen ist immer Normalverteilt. Aber die Parameter addieren sich: $\mu_{neu} = 2\mu$, $\sigma^2_{neu} = 2\sigma^2$. Die Aussage impliziert, dass die Parameter *gleich bleiben*, was falsch ist.
*   (c) **Standardnormal:** $N(0,1) + N(0,1) = N(0, 2)$. Das ist nicht mehr Standardnormal (Varianz ist 2). Falsch.
*   (d) Richtig, es ist eine Normalverteilung (wenn auch nicht Standard).

---
### Offizielle Lösung
(a) $B(n,p)+B(m,p) \sim B(n+m, p)$.<br>(b) Falsch, da sich Parameter addieren ($\mu_{tot} = 2\mu \ne \mu$).<br>(d) $N(0,1)+N(0,1) \sim N(0, 2)$, also normalverteilt.""",
        "en": r"""**Correct: (a), (d)**

### Study.Smart Guide
**Addition Rules:**
*   (a) Binomials add if $p$ is same.
*   (c) $N(0,1) + N(0,1) = N(0, 2)$. Not Standard Normal.
*   (d) But it IS Normal. Correct.

---
### Official Solution
Binomials add (same p). Normals add (variance sum)."""
    }
}

# ------------------------------------------------------------------
# PROBLEMS
# ------------------------------------------------------------------

uebung4_prob1 = {
    "source": "Übung 4, Probe #1",
    "type": "problem",
    "question": {
        "de": r"Speicherchips $N=100'000$. Stichprobe $n=400$. 10% defekt ($p=0.1$).<br>1) Annahme ($\le 44$ defekt).<br>2) Ablehnung ($\ge 51$ defekt).<br>3) Totalkontrolle (45-50).",
        "en": r"Chips $n=400, p=0.1$.<br>1) Accept ($\le 44$).<br>2) Reject ($\ge 51$).<br>3) Check (45-50)."
    },
    "solution": {
        "de": r"""### Study.Smart Guide
**Schritt-für-Schritt (Normal-Approximation):**
*Parameter:* $n=400, p=0.1$.
$\mu = np = 40$.
$\sigma = \sqrt{400 \cdot 0.1 \cdot 0.9} = \sqrt{36} = 6$.

**1) Annahme ($X \le 44$):**
Stetigkeitskorrektur: Wir nehmen bis $44.5$.
$Z = \frac{44.5 - 40}{6} = \frac{4.5}{6} = 0.75$.
$\Phi(0.75) \approx 0.7734$.

**2) Ablehnung ($X \ge 51$):**
Stetigkeitskorrektur: Wir starten ab $50.5$.
$Z = \frac{50.5 - 40}{6} = \frac{10.5}{6} = 1.75$.
$P(Z \ge 1.75) = 1 - \Phi(1.75) = 1 - 0.9599 = 0.0401$.

**3) Totalkontrolle:**
Der Rest: $1 - 0.7734 - 0.0401 = 0.1865$.

---
### Offizielle Lösung
Approximation durch Normalverteilung mit $\mu = 40, \sigma = 6$.<br>1) $P(X \le 44) \approx \Phi(0.75) \approx 0.7734$.<br>2) $P(X \ge 51) = 1 - \Phi(1.75) \approx 0.040$.<br>3) Rest: $0.187$.""",
        "en": r"""### Study.Smart Guide
**Calculation:**
$\mu=40, \sigma=6$.
1.  Accept: $P(X \le 44.5) \to Z=0.75 \to 0.7734$.
2.  Reject: $P(X \ge 50.5) \to Z=1.75 \to 0.0401$.
3.  Check: Remainder $\approx 0.1865$.

---
### Official Solution
Normal Approx. 1) 0.77. 2) 0.04. 3) 0.19."""
    }
}

uebung4_prob2 = {
    "source": "Übung 4, Probe #2",
    "type": "problem",
    "question": {
        "de": r"Einkommen $\mu=32600, \sigma=6200, n=400$.<br>(a) $P(\bar{X} > 32000)$?<br>(b) $P(32100 \le \bar{X} \le 33100)$?<br>(c) $P(32350 \le \bar{X} \le 32950)$?",
        "en": r"Income $\mu=32600, \sigma=6200, n=400$. Sample mean probs."
    },
    "solution": {
        "de": r"""### Study.Smart Guide
**Konzept: Standardfehler:**
Wir betrachten den **Mittelwert** $\bar{X}$.
Dieser streut viel weniger als ein Einzelwert X.
$\sigma_{\bar{x}} = \frac{\sigma}{\sqrt{n}} = \frac{6200}{20} = 310$.

**(a) $P(\bar{X} > 32000)$:**
$Z = \frac{32000 - 32600}{310} = \frac{-600}{310} \approx -1.94$.
$P(Z > -1.94) = \Phi(1.94) \approx 0.9738$.

---
### Offizielle Lösung
Standardfehler $\sigma_{\bar{x}} = 6200 / 20 = 310$.<br>(a) $Z = -1.94 \to 0.973$.<br>(b) $\approx 0.893$.<br>(c) $\approx 0.662$.""",
        "en": r"""### Study.Smart Guide
**Concept:**
Standard Error $SE = 6200 / \sqrt{400} = 310$.
Use this SE for Z-scores.

---
### Official Solution
SE=310. (a) 0.97. (b) 0.89."""
    }
}

uebung4_prob3 = {
    "source": "Übung 4, Probe #3",
    "type": "problem",
    "question": {
        "de": r"Produktion $n=2000$. Zurückweisung wenn $>200$ defekt. Gesucht max $p$, damit mit 95% W'keit *nicht* zurückgewiesen ($k \le 200$).",
        "en": r"$n=2000$. Reject if $>200$. Find max $p$ s.t. $P(X \le 200) \ge 0.95$."
    },
    "solution": {
        "de": r"""### Study.Smart Guide
**Inverse Normalverteilung:**
1.  Grenzbedingung: $P(X \le 200) = 0.95$.
2.  Z-Score für 95%: $1.645$.
3.  Formel:
    $$ \frac{200 - np}{\sqrt{np(1-p)}} = 1.645 $$
    Approximation: Da $p$ klein ist (nahe $200/2000=0.1$), setzen wir im Nenner $p \approx 0.1$ für eine erste Schätzung. $\sqrt{2000 \cdot 0.1 \cdot 0.9} = \sqrt{180} \approx 13.4$.
    $200 - 2000p = 1.645 \cdot 13.4 \approx 22$.
    $2000p = 178$.
    $p \approx 0.089$.
    (Exakte Lösung der quadratischen Gleichung bringt $p \approx 0.090$).

---
### Offizielle Lösung
$P(X \le 200) = 0.95 \implies \frac{200 - 2000p}{\sqrt{2000p(1-p)}} = 1.645$.<br>Auflösen nach p. Ergebnis $p \approx 0.090$.""",
        "en": r"""### Study.Smart Guide
**Strategy:**
Set Z-score of limit (200) to 1.645 (95th percentile).
Solve for p.
$p \approx 0.090$.

---
### Official Solution
$p \approx 0.090$."""
    }
}

uebung4_prob4 = {
    "source": "Übung 4, Probe #4",
    "type": "problem",
    "question": {
        "de": r"Würfel 180 Mal. $X$ = Anzahl 6er. Normalapprox.<br>(a) $P(28 < X \le 32)$.<br>(b) $P(31 \le X < 36)$.<br>(c) $P(X=30)$.",
        "en": r"Die 180 rolls. X = count of 6s. Normal approx."
    },
    "solution": {
        "de": r"""### Study.Smart Guide
**Stetigkeitskorrektur-Training:**
Parameter: $n=180, p=1/6$.
$\mu = 30$. $\sigma = \sqrt{180 \cdot \frac{1}{6} \cdot \frac{5}{6}} = \sqrt{25} = 5$.

**(a) $28 < X \le 32$:**
Das bedeutet: Werte $\{29, 30, 31, 32\}$.
Grenzen: von $28.5$ bis $32.5$.
$Z_u = (28.5-30)/5 = -0.3$.
$Z_o = (32.5-30)/5 = 0.5$.
$\Phi(0.5) - \Phi(-0.3)$.

**(c) Exakt $X=30$:**
Grenzen: von $29.5$ bis $30.5$.
$Z_u = -0.1, Z_o = 0.1$.
$\Phi(0.1) - \Phi(-0.1)$.

---
### Offizielle Lösung
$\mu = 30, \sigma = 5$.<br>(a) $\Phi(0.5) - \Phi(-0.3) = 0.3094$.<br>(c) $\Phi(0.1) - \Phi(-0.1) = 0.0796$.""",
        "en": r"""### Study.Smart Guide
**Continuity Correction:**
$\mu=30, \sigma=5$.
(a) Integer range 29-32 $\to$ continuous 28.5-32.5.
(c) Integer 30 $\to$ continuous 29.5-30.5.

---
### Official Solution
Mean 30, SD 5. (a) 0.31. (c) 0.08."""
    }
}

uebung4_prob5 = {
    "source": "Übung 4, Probe #5",
    "type": "problem",
    "question": {
        "de": r"DAX Dividende $N(\mu, 0.025)$. $n=16$.<br>(a) $P(\bar{X} > \mu + 0.01)$.<br>(b) $P(|\bar{X}-\mu| > 0.012)$?",
        "en": r"DAX Divs $N(\mu, 0.025)$. $n=16$.<br>(a) Probs."
    },
    "solution": {
        "de": r"""### Study.Smart Guide
**Standardfehler:**
$\sigma_{\bar{x}} = \frac{0.025}{\sqrt{16}} = \frac{0.025}{4} = 0.00625$.

**(a) Abweichung +0.01:**
Wie viele Standardfehler sind das?
$Z = \frac{0.01}{0.00625} = 1.6$.
$P(Z > 1.6) = 1 - 0.9452 = 0.0548$.

---
### Offizielle Lösung
$\sigma_{\bar{x}} = 0.00625$.<br>(a) $Z=1.6 \to 0.0548$.<br>(b) $2 \cdot 0.0274 = 0.0548$.""",
        "en": r"""### Study.Smart Guide
**Calculation:**
SE = 0.00625.
(a) $Z = 0.01 / SE = 1.6$. Prob = 0.0548.

---
### Official Solution
SE=0.00625. (a) 0.05. (b) 0.05."""
    }
}

uebung4_prob6 = {
    "source": "Übung 4, Probe #6",
    "type": "problem",
    "question": {
        "de": r"Funkgerät 1000 Elemente. $p=0.001$.<br>(a) Exakt 2 Ausfälle (Formel).<br>(b) Normalapprox $P(2 < X < 6)$.<br>(c) Ausfall Gerät ($X \ge 1$).",
        "en": r"1000 elements, $p=0.001$.<br>(a) Exact 2.<br>(b) Approx 2<X<6.<br>(c) Fail."
    },
    "solution": {
        "de": r"""### Study.Smart Guide
**Methoden-Vergleich:**
$n=1000, p=0.001$. Erwartungswert $\mu = 1$.
Das ist ein sehr kleines $p$. Normalverteilung ist hier eigentlich **schlecht** (Schiefe Verteilung bei $\mu=1$). Poisson ist besser.

**(c) Ausfall ($X \ge 1$):**
Exakt (Gegenereignis $X=0$):
$P(0) = (0.999)^{1000} \approx 0.3677$.
$P(\ge 1) = 1 - 0.3677 = 0.6323$.
Mit Poisson ($\lambda = 1$): $P(0) = e^{-1} \approx 0.3679$. (Sehr gut).
Normalapprox hier ungeeignet.

---
### Offizielle Lösung
(a) Binomialformel.<br>(b) Poisson $\lambda=1$ oder Normalapprox. Lösung: 0.0668.<br>(c) $1 - P(0) = 1 - e^{-1} \approx 0.632$.""",
        "en": r"""### Study.Smart Guide
**Choice of Approximation:**
Since $p$ is tiny and $\mu=1$, Poisson is best. Normal is risky (skewed).
(c) $1 - e^{-1} \approx 0.63$.

---
### Official Solution
(a) Binomial. (b) 0.07. (c) 0.63."""
    }
}

uebung4_prob7 = {
    "source": "Übung 4, Probe #7",
    "type": "problem",
    "question": {
        "de": r"Seilbahn max 4200kg. 50 Personen, $\mu=80, \sigma=10$.<br>Wahrscheinlichkeit Überlastung?",
        "en": r"Cable car max 4200kg. 50 ppl mean 80 SD 10. Overload prob?"
    },
    "solution": {
        "de": r"""### Study.Smart Guide
**Summe von ZV:**
Wir betrachten die Summe $S = \sum_{i=1}^{50} X_i$.
1.  Summen-Erwartung: $50 \cdot 80 = 4000$ kg.
2.  Summen-Varianz: $50 \cdot 10^2 = 5000$.
3.  Summen-Standardabweichung: $\sqrt{5000} \approx 70.7$ kg.
    (Achtung: NICHT $50 \cdot 10 = 500$! Fehler addieren sich quadratisch, heben sich teilweise auf).

**Rechnung:**
Grenze 4200.
$Z = \frac{4200 - 4000}{70.7} = \frac{200}{70.7} \approx 2.83$.
Wahrscheinlichkeit drüber: $1 - \Phi(2.83) = 1 - 0.9977 = 0.0023$.

---
### Offizielle Lösung
Gesamtgewicht $S_{50}$. $E[S] = 4000, SD[S] = \sqrt{50} \cdot 10 \approx 70.7$.<br>$P(S > 4200) = 1 - \Phi(2.83) = 0.0023$.""",
        "en": r"""### Study.Smart Guide
**Summing Variance:**
$\mu_{sum} = 50 \times 80 = 4000$.
$\sigma_{sum} = \sqrt{50} \times 10 = 70.7$. (Root-n Rule).
$Z = 200 / 70.7 = 2.83$.

---
### Official Solution
Mean 4000. SD 70.7. Prob 0.002."""
    }
}
