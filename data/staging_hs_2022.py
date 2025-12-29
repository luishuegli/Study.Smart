
# HS 2022 Exam Staging File
# Content extracted from:
# - HS2022_january_german (1).pdf
# - HS2022_january_solution_german (1).pdf
# Dual-Mode: Study.Smart Guide + Official Solution

# ------------------------------------------------------------------
# MULTIPLE CHOICE (4 Punkte each)
# ------------------------------------------------------------------

hs2022_mc1 = {
    "source": "HS 2022 Januar, MC #1 (4 Punkte)",
    "type": "mc",
    "question": {
        "de": r"Drei Freunde spielen ein Spiel. Sie werfen eine faire Münze. Spieler 1 gewinnt, wenn beim ersten Wurf Kopf herauskommt. Spieler 2 gewinnt, wenn beim zweiten Wurf Kopf herauskommt. Spieler 3 gewinnt, wenn beim dritten Wurf Kopf herauskommt. Wenn bis zur dritten Runde kein Gewinner ermittelt wurde, beginnt das Spiel von neuem. Wie hoch ist die Wahrscheinlichkeit, dass Spieler 3 das Spiel gewinnt?",
        "en": r"Three friends play a game. They flip a fair coin. Player 1 wins if heads comes up on the first toss. Player 2 wins if heads comes up on the second toss. Player 3 wins if heads comes up on the third toss. If no winner is determined by the third round, the game starts over. What is the probability that Player 3 wins the game?"
    },
    "options": [
        r"$\frac{1}{6}$",
        r"$\frac{1}{7}$",
        r"$\frac{1}{5}$",
        r"$\frac{1}{3}$"
    ],
    "correct_idx": 1, 
    "solution": {
        "de": r"""**Richtig: (b)**

### Study.Smart Guide
**Intuition:**
Spieler 3 kann nur gewinnen, wenn er in Runde 1 drankommt (also Wurf 1 und 2 "Zahl" waren) und er dann "Kopf" wirft. Das passiert mit Wahrscheinlichkeit $(1/2)^3 = 1/8$.
Aber das Spiel endet nicht immer in Runde 1. Wenn niemand gewinnt (Wkt $1/8$), wird resetet.
Wir suchen also $1/8$ von $100\%$, plus $1/8$ vom Rest, etc. Das ist eine geometrische Reihe.
Oder einfacher: Die relativen Gewinnchancen verhalten sich wie $P(S1):P(S2):P(S3) = 4:2:1$. Summe = 7 Teile. S3 hat 1 Teil davon.

**Schritt-für-Schritt:**
1.  Wkt, dass S3 in der *ersten* Runde gewinnt:
    $Zahl, Zahl, Kopf \Rightarrow \frac{1}{2} \cdot \frac{1}{2} \cdot \frac{1}{2} = \frac{1}{8}$.
2.  Wkt, dass *niemand* in der ersten Runde gewinnt:
    $Zahl, Zahl, Zahl \Rightarrow \frac{1}{8}$.
3.  Gesamtwahrscheinlichkeit (Geometrische Reihe):
    $$P = \frac{1}{8} \sum_{k=0}^{\infty} (\frac{1}{8})^k = \frac{1}{8} \cdot \frac{1}{1 - 1/8} = \frac{1}{8} \cdot \frac{8}{7} = \frac{1}{7}$$

---
### Offizielle Lösung
Dies ist eine geometrische Reihe. P(P3 gewinnt in Runde 1) = $(1/2)^3 = 1/8$.<br>Das Spiel startet neu mit Wahrscheinlichkeit $1/8$.<br>P(Sieg) = $\frac{1}{8} \sum_{k=0}^{\infty} (\frac{1}{8})^k = \frac{1}{8} \cdot \frac{1}{1-1/8} = \frac{1}{8} \cdot \frac{8}{7} = \frac{1}{7}$.""",
        "en": r"""**Correct: (b)**

### Study.Smart Guide
**Intuition:**
Player 3 wins only in the sequence T-T-H, which has probability $1/8$.
However, the game repeats if T-T-T occurs (prob $1/8$).
Relative odds are $4:2:1$ (since P1 wins on H, P2 on TH, P3 on TTH). Total shares = 7. P3 gets 1/7.

**Step-by-Step:**
1.  Win in Round 1: $1/8$.
2.  Restart probability: $1/8$.
3.  Geometric Series Formula:
    $$P = \frac{a}{1-r} = \frac{1/8}{1 - 1/8} = \frac{1/8}{7/8} = \frac{1}{7}$$

---
### Official Solution
This is a geometric series. P(P3 wins in Round 1) = $(1/2)^3 = 1/8$.<br>The game restarts with probability $1/8$.<br>P(Win) = $\frac{1}{8} \sum_{k=0}^{\infty} (\frac{1}{8})^k = \frac{1}{8} \cdot \frac{1}{1-1/8} = \frac{1}{8} \cdot \frac{8}{7} = \frac{1}{7}$."""
    }
}

hs2022_mc2 = {
    "source": "HS 2022 Januar, MC #2 (4 Punkte)",
    "type": "mc",
    "question": {
        "de": r"Sie haben 1000 Münzen und wissen, dass es genau eine Münze gibt mit beidseitig Kopf. Sie wählen eine Münze zufällig aus. Sie werfen diese 10 Mal und erhalten 10 Mal Kopf. Wie hoch ist die Wahrscheinlichkeit, dass Sie die besondere Münze haben?",
        "en": r"You have 1000 coins and know that there is exactly one double-headed coin. You randomly choose one. You flip it 10 times and get 10 heads. What is the probability that you picked the special coin?"
    },
    "options": [
        r"50.6%",
        r"1.8%",
        r"51.9%",
        r"2.9%"
    ],
    "correct_idx": 0,
    "solution": {
        "de": r"""**Richtig: (a)**

### Study.Smart Guide
**Intuition:**
Vor dem Werfen war die Chance 1 zu 1000 ($0.1\%$).
Das Ergebnis "10x Kopf" ist bei einer fairen Münze extrem unwahrscheinlich ($1/1024$), bei der falschen Münze aber sicher ($1$).
Das "Gewicht" der falschen Münze explodiert durch dieses Update massiv, fast auf 50/50.

**Schritt-für-Schritt (Bayes):**
1.  Hypothesen: $B$ (Biased), $F$ (Fair).
    $P(B) = 0.001, P(F) = 0.999$.
2.  Likelihood für 10x Kopf ($D$):
    $P(D|B) = 1$.
    $P(D|F) = 0.5^{10} \approx 0.000976$.
3.  Bayes Formel:
    $$P(B|D) = \frac{P(D|B)P(B)}{P(D|B)P(B) + P(D|F)P(F)}$$
    $$= \frac{1 \cdot 0.001}{1 \cdot 0.001 + 0.000976 \cdot 0.999}$$
    $$= \frac{0.001}{0.001 + 0.000975} \approx \frac{0.001}{0.001975} \approx 0.506$$

---
### Offizielle Lösung
Sei $F$ die faire Münze, $B$ die besondere (biased).<br>$P(10H | B) = 1$, $P(10H | F) = (0.5)^{10}$.<br>$P(B) = 1/1000$, $P(F) = 999/1000$.<br>Bayes: $P(B | 10H) = \frac{1 \cdot 0.001}{1 \cdot 0.001 + (0.5)^{10} \cdot 0.999} \approx 0.506$.""",
        "en": r"""**Correct: (a)**

### Study.Smart Guide
**Intuition:**
Prior is very low ($1/1000$).
The Evidence (10 Heads) is HUGE. It is ~1000x more likely to come from the biased coin than a fair one.
This balances out the low prior, bringing the probability to roughly 50%.

**Step-by-Step:**
1.  Evidence factor: $(0.5)^{10} \approx 1/1000$.
2.  Ratio calculation:
    $1 \times 1$ (for biased) vs $1000 \times 1/1024$ (for fair).
    Roughly $1 : 0.97$.
3.  Probability is $1 / (1+0.97) \approx 0.506$.

---
### Official Solution
Let $F$ be the fair coin, $B$ the special one.<br>$P(10H | B) = 1$, $P(10H | F) = (0.5)^{10}$.<br>$P(B) = 1/1000$, $P(F) = 999/1000$.<br>Bayes: $P(B | 10H) = \frac{1 \cdot 0.001}{1 \cdot 0.001 + (0.5)^{10} \cdot 0.999} \approx 0.506$."""
    }
}

hs2022_mc3 = {
    "source": "HS 2022 Januar, MC #3 (4 Punkte)",
    "type": "mc",
    "question": {
        "de": r"$X_i \sim U[0,1]$ i.i.d., $N=100$. Wahrscheinlichkeit, dass Mittelwert $> 0.55$ ist?",
        "en": r"$X_i \sim U[0,1]$ i.i.d., $N=100$. Probability that mean $> 0.55$?"
    },
    "options": [
        r"4.2%",
        r"1.2%",
        r"3.3%",
        r"3.1%"
    ],
    "correct_idx": 0,
    "solution": {
        "de": r"""**Richtig: (a)**

### Study.Smart Guide
**Intuition:**
Zentraler Grenzwertsatz (CLT): Der Durchschnitt von vielen Zufallsvariablen ist immer normalverteilt, egal wie die Ursprungsvariablen aussahen.
Wir suchen die Fläche unter der Normalglocke rechts von 0.55.

**Schritt-für-Schritt:**
1.  Momente der Einzelvariablen ($U[0,1]$):
    $\mu = 0.5$, $\sigma^2 = \frac{1}{12}$.
2.  Momente des Mittelwerts ($\bar{X}_{100}$):
    $\mu_{\bar{X}} = 0.5$ (bleibt gleich).
    $\sigma_{\bar{X}}^2 = \frac{\sigma^2}{n} = \frac{1}{1200}$.
    $\sigma_{\bar{X}} = \sqrt{1/1200} \approx 0.02887$.
3.  Z-Transformation:
    $$Z = \frac{0.55 - 0.5}{0.02887} \approx 1.732$$
4.  Nachschlagen ($\Phi(1.73)$):
    $\approx 0.958$.
    Gesuchte Fläche (rechts): $1 - 0.958 = 0.042 = 4.2\%$.

---
### Offizielle Lösung
$E[X] = 0.5$, $Var(X) = 1/12$.<br>$\bar{X} \sim_{approx} N(\mu, \sigma^2/n) = N(0.5, \frac{1}{1200})$.<br>$Z = \frac{0.55 - 0.5}{\sqrt{1/1200}} \approx \frac{0.05}{0.0288} \approx 1.73$.<br>$P(Z > 1.73) = 1 - \Phi(1.73) \approx 1 - 0.9582 = 0.0418 \approx 4.2\%$.""",
        "en": r"""**Correct: (a)**

### Study.Smart Guide
**Step-by-Step:**
1.  Parameters: $\mu=0.5, \sigma = \sqrt{1/12}$.
2.  Standard Error: $SE = \frac{\sigma}{\sqrt{100}} = \frac{1}{\sqrt{1200}} \approx 0.0289$.
3.  Z-Score:
    $$Z = \frac{0.55 - 0.50}{0.0289} = 1.73$$
4.  Probability $P(Z > 1.73) \approx 4.2\%$.

---
### Official Solution
$E[X] = 0.5$, $Var(X) = 1/12$.<br>$\bar{X} \sim_{approx} N(\mu, \sigma^2/n) = N(0.5, \frac{1}{1200})$.<br>$Z = \frac{0.55 - 0.5}{\sqrt{1/1200}} \approx \frac{0.05}{0.0288} \approx 1.73$.<br>$P(Z > 1.73) = 1 - \Phi(1.73) \approx 1 - 0.9582 = 0.0418 \approx 4.2\%$."""
    }
}

hs2022_mc4 = {
    "source": "HS 2022 Januar, MC #4 (4 Punkte)",
    "type": "mc",
    "question": {
        "de": r"Für welchen Wert von $c$ ist $f(x) = c \cdot e^{-0.8x}$ ($x \ge 0$) eine Dichtefunktion?",
        "en": r"For which value of $c$ is $f(x) = c \cdot e^{-0.8x}$ ($x \ge 0$) a PDF?"
    },
    "options": [
        r"$c = \frac{5}{4}$",
        r"$c = \frac{1}{2}$",
        r"$c = -\frac{9}{7}$",
        r"$c = \frac{4}{5}$"
    ],
    "correct_idx": 3,
    "solution": {
        "de": r"""**Richtig: (d)**

### Study.Smart Guide
**Intuition:**
Das ist eine Exponentialverteilung mit Parameter $\lambda = 0.8$.
Die Formel ist immer $\lambda e^{-\lambda x}$.
Also muss $c = \lambda = 0.8$ sein.

**Schritt-für-Schritt:**
1.  Bedingung: Integral muss 1 sein.
    $$\int_0^{\infty} c e^{-0.8x} dx = 1$$
2.  Stammfunktion von $e^{kx}$ ist $\frac{1}{k}e^{kx}$.
    $$c \left[ \frac{1}{-0.8} e^{-0.8x} \right]_0^{\infty} = 1$$
3.  Einsetzen ($\infty \to 0$, $0 \to 1$):
    $$c (0 - (-1.25)) = 1 \Rightarrow 1.25c = 1 \Rightarrow c = 0.8 = 4/5$$

---
### Offizielle Lösung
Damit es eine Dichtefunktion ist, muss das Integral 1 ergeben.<br>$\int_0^{\infty} c e^{-0.8x} dx = 1 \Rightarrow c \cdot \frac{1}{0.8} = 1 \Rightarrow c = 0.8 = \frac{4}{5}$.""",
        "en": r"""**Correct: (d)**

### Study.Smart Guide
**Intuition:**
This matches the Exponential Distribution definition $f(x) = \lambda e^{-\lambda x}$.
Here, $\lambda = 0.8$. So $c$ must be $0.8$ ($4/5$).

---
### Official Solution
Integral must equal 1.<br>$\int_0^{\infty} c e^{-0.8x} dx = 1 \Rightarrow c \cdot \frac{1}{0.8} = 1 \Rightarrow c = 0.8 = \frac{4}{5}$."""
    }
}

hs2022_mc5 = {
    "source": "HS 2022 Januar, MC #5 (4 Punkte)",
    "type": "mc",
    "question": {
        "de": r"Gegeben: $P(A) = 0.3$, $P(B) = 0.4$, $P(A | B) = 0.75$. Berechne $P(A \cup B)$.",
        "en": r"Given: $P(A) = 0.3$, $P(B) = 0.4$, $P(A | B) = 0.75$. Calculate $P(A \cup B)$."
    },
    "options": [
        r"0.425",
        r"0.6",
        r"0.7",
        r"Keine der obigen"
    ],
    "correct_idx": 1,
    "solution": {
        "de": r"""**Richtig: (b)**

### Study.Smart Guide
**Berechnung:**
1.  Schnittmenge berechnen:
    $P(A \cap B) = P(A|B) \cdot P(B) = 0.75 \cdot 0.4 = 0.3$.
2.  Vereinigung berechnen (Inklusion-Exklusion):
    $P(A \cup B) = P(A) + P(B) - P(A \cap B)$.
    $= 0.3 + 0.4 - 0.3 = 0.4$.
    
**Anmerkung zum Ergebnis:**
Die offizielle Lösung gibt **0.6** an. Dies ist mathematisch mit den gegebenen Zahlen ($P(A)=0.3$) nicht herleitbar (ergibt 0.4).
Möglicherweise war im Original $P(A|B)$ anders definiert oder es ist ein Druckfehler in der Prüfung. Wir listen hier die offizielle Lösung (b), weisen aber auf die Diskrepanz hin.

---
### Offizielle Lösung
$P(A \cap B) = P(A|B)P(B) = 0.75 \cdot 0.4 = 0.3$.
(Hinweis: Offizielle Lösung markiert 0.6 als richtig, rechnerisch ergibt sich 0.4)""",
        "en": r"""**Correct: (b)**

### Study.Smart Guide
**Calculation steps:**
1.  Intersection: $P(A \cap B) = 0.75 \times 0.4 = 0.3$.
2.  Union: $0.3 + 0.4 - 0.3 = 0.4$.

**Discrepancy Note:**
The official key marks **0.6** as correct. This contradicts the standard formula calculation based on the printed numbers. It is likely a typo in the exam source.

---
### Official Solution
$P(A \cap B) = P(A|B)P(B) = 0.75 \cdot 0.4 = 0.3$."""
    }
}

hs2022_mc6 = {
    "source": "HS 2022 Januar, MC #6 (4 Punkte)",
    "type": "mc",
    "question": {
        "de": r"7 Tage Hamburg, Regenwahrscheinlichkeit pro Tag 70%. Wahrscheinlichkeit für mind. 5 Regentage?",
        "en": r"7 days Hamburg, 70% rain chance per day. Probability of at least 5 rainy days?"
    },
    "options": [
        r"65%",
        r"66%",
        r"67%",
        r"68%"
    ],
    "correct_idx": 0,
    "solution": {
        "de": r"""**Richtig: (a)**

### Study.Smart Guide
**Intuition:**
Binomialverteilung mit $n=7$ und $p=0.7$.
"Mindestens 5" heißt: 5 oder 6 oder 7.

**Schritt-für-Schritt:**
Wir nutzen die Bernoulli-Formel $\binom{n}{k} p^k (1-p)^{n-k}$:
1.  $k=5:\binom{7}{5} 0.7^5 0.3^2 = 21 \cdot 0.168 \cdot 0.09 \approx 0.318$
2.  $k=6:\binom{7}{6} 0.7^6 0.3^1 = 7 \cdot 0.118 \cdot 0.3 \approx 0.247$
3.  $k=7:\binom{7}{7} 0.7^7 = 1 \cdot 0.082 \approx 0.082$
4.  Summe: $0.318 + 0.247 + 0.082 = 0.647 \approx 65\%$

---
### Offizielle Lösung
$X \sim B(7, 0.7)$. P(X $\ge$ 5) = P(5)+P(6)+P(7).<br>Summe $\approx 0.317 + 0.247 + 0.082 = 0.646 \approx 65\%$.""",
        "en": r"""**Correct: (a)**

### Study.Smart Guide
**Intuition:**
Binomial distribution $B(7, 0.7)$. Sum probabilities for $k=5, 6, 7$.

**Step-by-Step:**
1.  $P(5) \approx 0.318$
2.  $P(6) \approx 0.247$
3.  $P(7) \approx 0.082$
4.  Total $\approx 0.65$

---
### Official Solution
$X \sim B(7, 0.7)$. P(X $\ge$ 5) = P(5)+P(6)+P(7).<br>Sum is approx $0.646 \approx 65\%$."""
    }
}

hs2022_mc7 = {
    "source": "HS 2022 Januar, MC #7 (4 Punkte)",
    "type": "mc",
    "question": {
        "de": r"Best-of-5 (wer zuerst 3 gewinnt). Stand 0:1 für B. B gewinnt eine Runde mit 40%. Wkt, dass B das Spiel gewinnt?",
        "en": r"Best-of-5 (first to 3). Score 0:1 for B. B wins round with 40%. Prob B wins match?"
    },
    "options": [
        r"52.48%",
        r"34.56%",
        r"50.05%",
        r"45.24%"
    ],
    "correct_idx": 0,
    "solution": {
        "de": r"""**Richtig: (a)**

### Study.Smart Guide
**Analyse:**
B hat schon 1 Sieg. B braucht noch 2 Siege.
Maximale noch zu spielende Runden: 4 (gesamt max 5).
B verliert nur, wenn A 3 Siege holt, *bevor* B 2 Siege holt.

**Pfade zum Sieg für B:**
(Notation: Wer gewinnt das nächste Spiel?)
1.  **B gewinnt Spiel 2** (40%): Stand 0:2. B braucht noch 1. Sehr gut.
2.  Oder wir zählen einfach alle Siegespfade für B:
    *   BB (0:3) $\to 0.4^2 = 0.16$
    *   BAB (1:3) $\to 0.4 \cdot 0.6 \cdot 0.4 = 0.096$
    *   ABB (1:3) $\to 0.6 \cdot 0.4 \cdot 0.4 = 0.096$
    *   BAAB, ABAB, AABB...
    
    *Alternativ via Gegenwahrscheinlichkeit (A gewinnt):*
    A braucht 3 Siege in Folge oder 3 aus 4.
    A gewinnt Serie: $AAA$ ($0.6^3$) + $BAAA$ + $ABAA$ + $AABA$.
    $P(A_{wins}) = 0.216 + 3 \cdot (0.4 \cdot 0.6^3) = 0.216 + 0.2592 = 0.4752$.
    $P(B_{wins}) = 1 - 0.4752 = 0.5248$.

---
### Offizielle Lösung
B braucht noch 2 Siege, bevor A 3 Siege holt.<br>Berechnet: 0.5248.""",
        "en": r"""**Correct: (a)**

### Study.Smart Guide
**Strategy:**
Easier to calculate probability of A winning (A needs 3 wins).
A wins if sequence is:
1.  AAA ($0.6^3 = 0.216$)
2.  BAAA ($0.4 \cdot 0.6^3 = 0.0864$)
3.  ABAA ($0.6 \cdot 0.4 \cdot 0.6^2 = 0.0864$)
4.  AABA ($0.6^2 \cdot 0.4 \cdot 0.6 = 0.0864$)
Sum P(A) = 0.4752.
P(B) = 1 - 0.4752 = 0.5248.

---
### Official Solution
B needs 2 more wins before A gets 3.<br>Calculated probability of B reaching 3 wins first starting from 1:0 lead is 52.48%."""
    }
}

hs2022_mc8 = {
    "source": "HS 2022 Januar, MC #8 (4 Punkte)",
    "type": "mc",
    "question": {
        "de": r"$X \sim U[0, b]$. Messwerte: 1.1, 3.8, 4.2, 0.5, 5.2. MLE für $b$?",
        "en": r"$X \sim U[0, b]$. Values: 1.1, 3.8, 4.2, 0.5, 5.2. MLE for $b$?"
    },
    "options": [
        r"$\hat{b}_{ML} = 6.23$",
        r"$\hat{b}_{ML} = 5.20$",
        r"$\hat{b}_{ML} = 5.92$",
        r"$\hat{b}_{ML} = 5.75$"
    ],
    "correct_idx": 1,
    "solution": {
        "de": r"""**Richtig: (b)**

### Study.Smart Guide
**Intuition:**
Wenn ich behaupte "Die Zahlen gehen maximal bis $b=4$", aber ich habe eine 5.2 beobachtet, ist meine Behauptung unmöglich (Likelihood 0).
Ich muss $b$ also *mindestens* so groß wählen wie den größten beobachteten Wert.
Um die Wahrscheinlichkeitsdichte $1/b$ zu maximieren, sollte ich $b$ so *klein wie möglich* wählen (aber immer noch gültig).
Das Minimum der gültigen Werte ist genau das Maximum der Daten.

**Merksatz:**
Bei Uniform $[0, b]$ ist der MLE immer $max(x_i)$.

---
### Offizielle Lösung
Für die Gleichverteilung $U[0,b]$ ist der MLE das Maximum der Beobachtungen: $max(x_i)$.<br>$max(1.1, 3.8, 4.2, 0.5, 5.2) = 5.2$.""",
        "en": r"""**Correct: (b)**

### Study.Smart Guide
**Intuition:**
The parameter $b$ must be at least as large as the largest observation (otherwise probability is 0).
To maximize the density function $1/b$, we want $b$ to be as small as possible.
Therefore: $\hat{b} = \max(x_i)$.

---
### Official Solution
For uniform distribution $U[0,b]$, the MLE is the maximum of observations: $max(x_i)$.<br>$max(1.1, 3.8, 4.2, 0.5, 5.2) = 5.2$."""
    }
}

hs2022_mc9 = {
    "source": "HS 2022 Januar, MC #9 (4 Punkte)",
    "type": "mc",
    "question": {
        "de": r"A und B sind zwei Ereignisse mit $P(A) > 0$ und $P(B) > 0$. Welche Aussage muss wahr sein?",
        "en": r"A and B are two events with $P(A) > 0$ and $P(B) > 0$. Which statement must be true?"
    },
    "options": [
        r"$P(A|B) \cdot P(A) = P(B|A) \cdot P(B)$",
        r"$P(B) > P(A \cap B)$",
        r"$P(A) > P(A|B)$",
        r"Keine der oben genannten."
    ],
    "correct_idx": 3,
    "solution": {
        "de": r"""**Richtig: (d)**

### Study.Smart Guide
**Analye:**
*   (a) Dies sieht aus wie Bayes, ist aber falsch!
    Richtig wäre: $P(A|B) P(B) = P(B|A) P(A)$. Hier wurde $P(A)$ und $P(B)$ vertauscht.
*   (b) Nicht zwingend. Wenn $B$ eine Teilmenge von $A$ ist, dann ist $P(B) = P(A \cap B)$. Es ist also nicht strikt "größer" ($>$), sondern könnte gleich sein ($\ge$).
*   (c) Nicht zwingend. Wenn $A$ und $B$ positiv korreliert sind, ist $P(A|B) > P(A)$.

Daher: Keine ist *immer* wahr.

---
### Offizielle Lösung
(a) Falsch, Satz von Bayes ist $P(A|B)P(B) = P(B|A)P(A)$. Hier sind $P(A)$ und $P(B)$ vertauscht.<br>(b) Falsch, wenn $B \subset A$, dann $P(B) = P(A \cap B)$.<br>(c) Falsch, abhängig von Korrelation.""",
        "en": r"""**Correct: (d)**

### Study.Smart Guide
**Analysis:**
*   (a) Incorrect Bayes formula (terms swapped).
*   (b) Equality holds if $B \subset A$.
*   (c) Depends on correlation (could be $>$ or $<$ or $=$).
*   (d) Correct.

---
### Official Solution
(a) False, Bayes is $P(A|B)P(B) = P(B|A)P(A)$. Here terms are swapped.<br>(b) False, if $B \subset A$, then equality holds.<br>(c) False, depends on correlation."""
    }
}

hs2022_mc10 = {
    "source": "HS 2022 Januar, MC #10 (4 Punkte)",
    "type": "mc",
    "question": {
        "de": r"Cheating Detection: $n=1000$ Züge. Starker Spieler findet Top-Move mit $p=0.3$. Ban wenn $\ge 340$ Top-Moves. P(False Ban)?",
        "en": r"Cheating Detection: $n=1000$ moves. Strong player matches top move $p=0.3$. Ban if $\ge 340$ matches. P(False Ban)?"
    },
    "options": [
        r"0.1%",
        r"0.3%",
        r"0.5%",
        r"0.7%"
    ],
    "correct_idx": 1,
    "solution": {
        "de": r"""**Richtig: (b)**

### Study.Smart Guide
**Schritt-für-Schritt:**
1.  **Erwartungswert:** Bei 1000 Zügen und 30% Skill erwarten wir $\mu = 300$ Top-Moves.
2.  **Standardabweichung:** $\sigma = \sqrt{np(1-p)} = \sqrt{1000 \cdot 0.3 \cdot 0.7} = \sqrt{210} \approx 14.5$.
3.  **Grenzwert:** Wir testen ab 340. Das ist eine Abweichung von $+40$.
4.  **Z-Score:** Wie viele Sigmas sind das?
    $$Z = \frac{340 - 300}{14.5} \approx 2.76$$
5.  **Wahrscheinlichkeit:** Ein Ereignis jenseits von 2.76 Sigma ist sehr selten.
    $1 - \Phi(2.76) \approx 0.003 = 0.3\%$.

---
### Offizielle Lösung
Approximiere mit Normalverteilung (CLT).<br>$\mu = 300, \sigma \approx 14.49$.<br>$P(X \ge 340) \approx P(Z \ge 2.73)$.<br>$1 - \Phi(2.73) \approx 0.003 = 0.3\%$.""",
        "en": r"""**Correct: (b)**

### Study.Smart Guide
**Step-by-Step:**
1.  Mean: 300.
2.  SD: 14.5.
3.  Target: 340. Distance: 40.
4.  Z-Score: $40 / 14.5 \approx 2.76$.
5.  The tail probability for $Z > 2.76$ is approx $0.3\%$.

---
### Official Solution
Normal Approximation.<br>$\mu = 300, \sigma \approx 14.49$.<br>$P(X \ge 340) \approx P(Z \ge 2.73) \approx 0.3\%$."""
    }
}

hs2022_mc11 = {
    "source": "HS 2022 Januar, MC #11 (4 Punkte)",
    "type": "mc",
    "question": {
        "de": r"Seien $X, Y, Z$ Zufallsvariablen mit $E[X] = E[Y]$, $E[XY] = 1$ und $E[X + Y - 2Z] = -1$. $X$ und $Y$ sind unabhängig. Wie groß ist $E[Z]$?",
        "en": r"Let $X, Y, Z$ be random variables with $E[X] = E[Y]$, $E[XY] = 1$ and $E[X + Y - 2Z] = -1$. $X$ and $Y$ are independent. What is $E[Z]$?"
    },
    "options": [
        r"-0.5",
        r"1.5",
        r"3",
        r"Nicht genügend Informationen."
    ],
    "correct_idx": 3,
    "solution": {
        "de": r"""**Richtig: (d)**

### Study.Smart Guide
**Die Falle:**
Wir wissen $E[XY] = 1$. Dank Unabhängigkeit gilt auch $E[X]E[Y] = 1$.
Da $E[X]=E[Y]$, muss gelten: $(E[X])^2 = 1$.
Das hat **zwei** Lösungen: $E[X] = 1$ oder $E[X] = -1$.
Je nachdem, welche Lösung stimmt, ändert sich $E[Z]$.
Da wir das Vorzeichen nicht kennen, ist die Info ungenügend.

---
### Offizielle Lösung
Unabhängigkeit $\Rightarrow E[XY] = E[X]E[Y]$.<br>$E[X]^2 = 1 \Rightarrow E[X] = 1$ oder $-1$.<br>$E[X+Y-2Z] = 2E[X] - 2E[Z] = -1$.<br>Ohne Vorzeichen von $E[X]$ ist $E[Z]$ nicht eindeutig ($1.5$ oder $0.5$).""",
        "en": r"""**Correct: (d)**

### Study.Smart Guide
**The Trap:**
$E[X]^2 = 1$ implies $E[X]$ is either $+1$ or $-1$.
If $+1$, then $2 - 2E[Z] = -1 \Rightarrow E[Z] = 1.5$.
If $-1$, then $-2 - 2E[Z] = -1 \Rightarrow E[Z] = -0.5$.
Two possibilities $\to$ Not enough info.

---
### Official Solution
Independence $\Rightarrow E[XY] = E[X]E[Y]$.<br>$E[X]^2 = 1 \Rightarrow E[X] = \pm 1$.<br>$2E[X] - 2E[Z] = -1$.<br>Depends on sign of $E[X]$."""
    }
}

hs2022_mc12 = {
    "source": "HS 2022 Januar, MC #12 (4 Punkte)",
    "type": "mc",
    "question": {
        "de": r"Zwei Wale. Jeder mit 50% männlich. Geburtstag unabhängig (1/7). Verhältnis $P(A|B)$ vs $P(A|C)$.<br>A: Beide männlich.<br>B: Mindestens einer männlich.<br>C: Mindestens einer männlich UND am Dienstag geboren.",
        "en": r"Two whales. Each 50% male. Birthday independent (1/7). Ratio $P(A|B)$ vs $P(A|C)$.<br>A: Both male.<br>B: At least one male.<br>C: At least one male AND born on Tuesday."
    },
    "options": [
        r"$P(A|B) = P(A|C)$",
        r"$P(A|B) > P(A|C)$",
        r"$P(A|B) < P(A|C)$",
        r"Nicht genügend Infos."
    ],
    "correct_idx": 2,
    "solution": {
        "de": r"""**Richtig: (c)**

### Study.Smart Guide
**Das Skandal-Paradoxon:**
Dies ist eine Variation des "Boy or Girl Paradox".
*   Fall B ("Mindestens einer"): Die möglichen Welten sind {MM, MF, FM}. (FF ist raus). MM ist 1 von 3. Also $1/3$.
*   Fall C ("Einer ist Männlich-Dienstag"): Das ist sehr spezifisch!
    Die Wahrscheinlichkeit nähert sich $1/2$ an, je spezifischer die Info wird.
    Rechnerisch: $13/27 \approx 0.48$.
    $0.33 < 0.48$.

**Merksatz:**
Spezifische Zusatzinfos ("geboren am Dienstag", "heißt Florida") erhöhen die Wahrscheinlichkeit für "Beide", da sie den "Gemischten Fall" (MF/FM) weniger wahrscheinlich machen als den "Doppelten Fall" (MM), relativ gesehen.

---
### Offizielle Lösung
Das ist ein bekanntes Paradoxon.<br>$P(A|B) = 1/3$.<br>$P(A|C) = 13/27 \approx 0.48$.<br>Daher $P(A|B) < P(A|C)$.""",
        "en": r"""**Correct: (c)**

### Study.Smart Guide
**The Paradox:**
*   $P(MM | \text{at least one M}) = 1/3$.
*   $P(MM | \text{at least one M-Tuesday}) \approx 1/2$.
    The more specific the condition (Tuesday), the closer it gets to independence (1/2).
    Technically: $13/27 \approx 0.48$.

---
### Official Solution
Known paradox.<br>$P(A|B) = 1/3$.<br>$P(A|C) = 13/27 \approx 0.48$.<br>Thus $P(A|B) < P(A|C)$."""
    }
}

# ------------------------------------------------------------------
# PROBLEMS
# ------------------------------------------------------------------

hs2022_prob1 = {
    "source": "HS 2022 Januar, Problem 1 (12 Punkte)",
    "type": "problem",
    "question": {
        "de": r"**Teil 1A (4 Punkte):** Ordne Verteilungen den Diagrammen zu.<br>$F_1$: $N(0, 0.5)$<br>$F_2$: $B(100, 0.6)$<br>$F_3$: $U[-2, 2]$<br>$F_4$: $Exp(1/60)$<br><br>**Teil 1B (8 Punkte):** Salatverkauf: 321, 321, 205, 320, 240, 450, 261, 345, 321, 276, 399.<br>1. Berechne Mittelwert, Median, Modus.<br>2. Zeichne Boxplot (Grenzen berechnen).",
        "en": r"**Part 1A (4 Points):** Match distributions to diagrams.<br>$F_1$: $N(0, 0.5)$<br>$F_2$: $B(100, 0.6)$<br>$F_3$: $U[-2, 2]$<br>$F_4$: $Exp(1/60)$<br><br>**Part 1B (8 Points):** Salad sales: 321, 321, 205, 320, 240, 450, 261, 345, 321, 276, 399.<br>1. Calculate Mean, Median, Mode.<br>2. Draw Boxplot (calculate limits)."
    },
    "solution": {
        "de": r"""### Study.Smart Guide
**Intuition 1A**
*   **Exponential:** Immer extrem schief. Viele kleine Werte, wenige große. Das Histogramm fällt steil ab.
*   **Uniform (Gleichverteilung):** Der QQ-Plot gegen Normalverteilung sieht aus wie eine S-Kurve, aber mit "flachen" Enden (light tails).

**Lösung 1B**
Sortierte Daten (n=11):
205, 240, 261, 276, 320, **321**, 321, 321, 345, 399, 450.
*   Median: Der 6. Wert $\to$ 321.
*   Modus: 321 ist 3x vorhanden.
*   Q1 (25%): 3. Wert $\to$ 261.
*   Q3 (75%): 9. Wert $\to$ 345.
*   IQR: $345 - 261 = 84$.
*   Whiskers: $Q1 - 1.5 IQR = 135$. (Min Datenwert 205 liegt darüber). $Q3 + 1.5 IQR = 471$.

---
### Offizielle Lösung
**Lösung 1A:**<br>$F_1 = c$, $F_2 = a$, $F_3 = d$, $F_4 = b$.<br><br>**Lösung 1B:**<br>Mittelwert: 314.45.<br>Median: 321.<br>Modus: 321.<br>Q1 = 261, Q3 = 345, IQR = 84.<br>Grenzen: Min 205, Max 450.""",
        "en": r"""### Study.Smart Guide
**Analysis:**
*   **Sort Data first!** 205, 240, 261, 276, 320, 321, 321, 321, 345, 399, 450.
*   **Median:** Middle element (6th) is 321.
*   **Mode:** Most frequent is 321.

---
### Official Solution
**Solution 1A:**<br>$F_1 = c$, $F_2 = a$, $F_3 = d$, $F_4 = b$.<br><br>**Solution 1B:**<br>Mean: 314.45.<br>Median: 321.<br>Mode: 321.<br>Q1 = 261, Q3 = 345, IQR = 84.<br>Whiskers: Min 205, Max 450."""
    }
}

hs2022_prob2 = {
    "source": "HS 2022 Januar, Problem 2 (15 Punkte)",
    "type": "problem",
    "question": {
        "de": r"Christopher segelt nach San Salvador (Westen).<br>1. Vorhersage Christopher: 4 Richtungen (N, E, S, W). P(ankommen in 2 Tagen)?<br>2. Vorhersage Diego: 8 Richtungen. P(ankommen in 2 Tagen)?<br>3. Vorhersage Rodrigo: 4 Richtungen, aber Änderung max 90 Grad. P(ankommen in 2 Tagen)?<br>4. P(Nahrung reicht für 3 Tage)?",
        "en": r"Christopher sails to San Salvador (West).<br>1. Christopher's model: 4 directions (N, E, S, W). P(arrive in 2 days)?<br>2. Diego's model: 8 directions. P(arrive in 2 days)?<br>3. Rodrigo's model: 4 directions, max 90 deg change. P(arrive in 2 days)?<br>4. P(Food lasts 3 days)?"
    },
    "solution": {
        "de": r"""### Study.Smart Guide
**Intuition:**
Ein "Random Walk" (Zufallspfad). Wir suchen Pfade, die nach 2 Schritten "im Westen" (oder am Ziel?) ankommen.
Das Ziel ist wohl "ankommen" oder "im Westen sein". Kontext impliziert: Die Distanz verringern? Oder genau einen Punkt treffen?
(Annahme aus Lösung: Es geht um spezifische Pfade).

**Lösung 1:** $9/16$.
**Lösung 2:** $25/64$.
**Lösung 3:** Bedingte Wahrscheinlichkeit (Markov Kette).

---
### Offizielle Lösung
1. $9/16$.<br>2. $25/64$.<br>3. $7/12$.<br>4. $27/32$.""",
        "en": r"""### Study.Smart Guide
**Intuition:**
Random Walk problem. Counting favorable paths vs total paths.

---
### Official Solution
1. $9/16$.<br>2. $25/64$.<br>3. $7/12$.<br>4. $27/32$."""
    }
}

hs2022_prob3 = {
    "source": "HS 2022 Januar, Problem 3 (15 Punkte)",
    "type": "problem",
    "question": {
        "de": r"Aktienkurs Modellierung (Kim).<br>Tag 1: 50% hoch/runter.<br>Tag 2: Momentum (0.55 gleich).<br>Tag 3: Trend (0.6 wenn 2x gleich, 0.5 wenn Wechsel).<br>1. Baumdiagramm.<br>2. P(3x hoch), P(Wechsel), P(Tag 3 runter | 2x hoch).<br>3. P(Tag 3 hoch).<br>4. Unternehmen Y (50% jeden Tag). P(mind 4 von 5 Tagen hoch)?",
        "en": r"Stock price modeling (Kim).<br>Day 1: 50% up/down.<br>Day 2: Momentum (0.55 same).<br>Day 3: Trend (0.6 if 2x same, 0.5 if switch).<br>1. Tree diagram.<br>2. P(3x up), P(switch), P(Day 3 down | 2x up).<br>3. P(Day 3 up).<br>4. Company Y (50% every day). P(at least 4 of 5 days up)?"
    },
    "solution": {
        "de": r"""### Study.Smart Guide
**Schritt-für-Schritt:**
1.  **Baumdiagramm:**
    Start $\to$ U (0.5) / D (0.5).
    U $\to$ UU (0.55) / UD (0.45).
    UU (2x gleich) $\to$ UUU (0.6) / UUD (0.4).
2.  **Pfadwahrscheinlichkeiten:**
    $P(UUU) = 0.5 \cdot 0.55 \cdot 0.6 = 0.165$.

---
### Offizielle Lösung
2. P(u,u,u)=0.165. P(Wechsel)=0.225. P(d|u,u)=0.4.<br>3. P(Tag 3 up) = 0.5.<br>4. Binomial(5, 0.5). P(X>=4) = $6/32 = 0.1875$.""",
        "en": r"""### Study.Smart Guide
**Step-by-Step:**
Multiply probabilities along valid tree branches.
$P(UUU) = 0.5 \times 0.55 \times 0.6 = 0.165$.

---
### Official Solution
2. P(u,u,u)=0.165. P(switch)=0.225. P(d|u,u)=0.4.<br>3. P(Day 3 up) = 0.5.<br>4. Binomial(5, 0.5). P(X>=4) = $6/32 = 0.1875$."""
    }
}

hs2022_prob4 = {
    "source": "HS 2022 Januar, Problem 4 (15 Punkte)",
    "type": "problem",
    "question": {
        "de": r"**Teil 4A:** $f_X(x) = a \sin(x)$ auf $[0, \pi]$.<br>1. Bestimme $a$.<br>2. $f_{X,Y} = \frac{1}{4} \sin(x) \cos(y)$. Bestimme $f_Y(y)$.<br>3. Sind X, Y unabhängig?<br><br>**Teil 4B:** $f_{X,Y} = c(x + x/y)$.<br>1. Berechne $P(X \le Y)$.<br>2. Zeige dass $c=2/e$.",
        "en": r"**Part 4A:** $f_X(x) = a \sin(x)$ on $[0, \pi]$.<br>1. Find $a$.<br>2. $f_{X,Y} = \frac{1}{4} \sin(x) \cos(y)$. Find $f_Y(y)$.<br>3. Are X, Y independent?<br><br>**Part 4B:** $f_{X,Y} = c(x + x/y)$.<br>1. Calculate $P(X \le Y)$.<br>2. Show that $c=2/e$."
    },
    "solution": {
        "de": r"""### Study.Smart Guide
**Rechnung 4A:**
1.  $\int_0^\pi \sin(x) dx = [-\cos(x)]_0^\pi = -(-1) - (-1) = 2$.
    Also muss $a \cdot 2 = 1 \Rightarrow a = 1/2$.
2.  Unabhängigkeit? Ja, da sich die Funktion perfekt in $g(x) \cdot h(y)$ zerlegen lässt.
    $\sin(x) \cos(y) = \text{Term}(x) \cdot \text{Term}(y)$.

---
### Offizielle Lösung
4A: 1. $a=1/2$. 2. $f_Y(y) = 1/2 \cos(y)$. 3. Ja.<br>4B: 1. 1 (da Bereich $x<1<y$). 2. Integralrechnung.""",
        "en": r"""### Study.Smart Guide
**Calculation:**
1.  Integral of sine is cosine. Value is 2. So $a=1/2$.
2.  Factorization implies independence.

---
### Official Solution
4A: 1. $a=1/2$. 2. $f_Y(y) = 1/2 \cos(y)$. 3. Yes.<br>4B: 1. 1 (domain $x<1<y$). 2. Integral calculation."""
    }
}

hs2022_prob5 = {
    "source": "HS 2022 Januar, Problem 5 (15 Punkte)",
    "type": "problem",
    "question": {
        "de": r"Poisson Verteilung $P(X=x) = \frac{\lambda^x e^{-\lambda}}{x!}$.<br>1. Momentenschätzer für $\lambda$.<br>2. MLE für $\lambda$.<br>3. Berechne für Daten 0.5, 0.25, 0.15 (Wait, Poisson muss ganzzahlig sein? Typo in Exam?).",
        "en": r"Poisson Distribution $P(X=x) = \frac{\lambda^x e^{-\lambda}}{x!}$.<br>1. Method of Moments estimator for $\lambda$.<br>2. MLE for $\lambda$.<br>3. Calculate for data 0.5, 0.25, 0.15 (Poisson must be integer? Exam typo?)."
    },
    "solution": {
        "de": r"""### Study.Smart Guide
**Intuition:**
Bei Poisson ist $\lambda$ sowohl der Mittelwert ($E[X]$) als auch die Varianz.
Daher ist der naheliegendste Schätzer einfach der Durchschnitt der Beobachtungen $\bar{X}$.
Sowohl MLE als auch MM führen zum gleichen Ergebnis.

**Warnung:**
Die Daten (0.5, 0.25...) sind keine ganzen Zahlen. Poisson ist aber für Zählungen (0, 1, 2...). Die Aufgabe ist theoretisch fragwürdig, aber wir wenden die Formel einfach "blind" an.

---
### Offizielle Lösung
1. $\hat{\lambda}_{MM} = \bar{X}$.<br>2. $\hat{\lambda}_{MLE} = \bar{X}$.<br>3. $\bar{X} = 0.3$.""",
        "en": r"""### Study.Smart Guide
**Intuition:**
For Poisson, lambda is the mean. So sample mean is the best estimator.
Both MLE and MM yield $\bar{X}$.

---
### Official Solution
1. $\hat{\lambda}_{MM} = \bar{X}$.<br>2. $\hat{\lambda}_{MLE} = \bar{X}$.<br>3. $\bar{X} = 0.3$."""
    }
}
