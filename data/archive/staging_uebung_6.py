
# Übung 6 Exam Staging File
# Content extracted from:
# - Uebung_6.pdf (questions)
# - ML_Uebung_6.pdf (solutions)
# Dual-Mode: Study.Smart Guide + Official Solution

# ------------------------------------------------------------------
# PROBLEMS (No MC in Übung 6)
# ------------------------------------------------------------------

uebung6_prob1 = {
    "source": "Übung 6, Probe #1",
    "type": "problem",
    "question": {
        "de": r"Steak braten. $\mu \sim N(\mu, 225)$. Stichprobe: 235, 229, 217, 210, 223, 214, 210, 211, 213 ($n=9$).<br>(a) Teste $H_0: \mu = 210$ vs $H_1: \mu \ne 210$ ($\alpha=0.1$).<br>(b) Akzeptanzbereich für $\bar{x}$?",
        "en": r"Steak frying. $N(\mu, 225)$. Sample n=9.<br>(a) Test $\mu=210$ vs $\neq$ ($\alpha=0.1$).<br>(b) Acceptance region?"
    },
    "solution": {
        "de": r"""### Study.Smart Guide
**Z-Test (Varianz bekannt):**
Parameter: $\sigma = \sqrt{225} = 15$. $n=9$.
Standardfehler: $SE = 15/\sqrt{9} = 5$.
Stichprobenmittel (Taschenrechner): $\bar{x} = 1962 / 9 = 218$.

**(a) Hypothesentest:**
$H_0: \mu = 210$.
$Z = \frac{218 - 210}{5} = \frac{8}{5} = 1.6$.
Kritischer Wert ($\alpha=0.1$, zweiseitig): Wir schneiden 5% links und 5% rechts ab. $z_{0.95} = 1.645$.
$|1.6| < 1.645$.
Entscheidung: **$H_0$ nicht verwerfen**. (Knapp dran, aber im Rahmen).

**(b) Akzeptanzbereich:**
Alle $\bar{x}$, die nicht verworfen werden.
$\mu_0 \pm z_{crit} \cdot SE$.
$210 \pm 1.645 \cdot 5$.
$210 \pm 8.225$.
Intervall: $[201.775, 218.225]$.
Unser Wert 218 liegt gerade noch drin.

---
### Offizielle Lösung
$\bar{x} = 218$. $\sigma=15$.<br>(a) $Z = 1.6$. Kritischer Wert $1.645$. $|1.6| < 1.645 \implies H_0$ nicht verwerfen.<br>(b) $210 \pm 1.645 \cdot 5 \implies [201.775, 218.225]$.""",
        "en": r"""### Study.Smart Guide
**Analysis:**
$\bar{x}=218, SE=5$.
$Z = (218-210)/5 = 1.6$.
Critical $Z_{0.95} = 1.645$ (Two-sided 10%).
$1.6 < 1.645 \implies$ Fail to reject.

---
### Official Solution
Mean 218. Z=1.6. Fail to reject. CI [201.8, 218.2]."""
    }
}

uebung6_prob2 = {
    "source": "Übung 6, Probe #2",
    "type": "problem",
    "question": {
        "de": r"Schrittlänge $N(\mu, 0.04)$. $n=7$. Werte: 85.1, 85.4, 85.3, 85.0, 84.9, 85.2, 85.4.<br>(a) Teste $H_0: \mu \le 85$ ($\alpha=0.01$).<br>(b) Entscheidung bei $\alpha=0.4$ und $\alpha=0.0005$.<br>(c) p-Wert (Grenzniveau).<br>(d) Macht des Tests bei $\mu_{wahr}=85.1$.",
        "en": r"Step length $N(\mu, 0.04)$. $n=7$.<br>(a) Test $\mu \le 85$ ($\alpha=0.01$).<br>(b) Decisions.<br>(c) p-value.<br>(d) Power at 85.1."
    },
    "solution": {
        "de": r"""### Study.Smart Guide
**Daten-Check:**
$\sigma = \sqrt{0.04} = 0.2$. $n=7$. $SE = 0.2/\sqrt{7} \approx 0.0756$.
$\bar{x} = 596.3 / 7 \approx 85.186$.

**(a) Test:**
$H_0: \mu \le 85$ (Einseitig rechts testen, da $\bar{x} > 85$).
$Z = \frac{85.186 - 85}{0.0756} = 2.46$.
Kritisch ($\alpha=0.01$): $\Phi^{-1}(0.99) = 2.33$.
$2.46 > 2.33 \implies$ **Verwerfen**. (Signifikant länger als 85).

**(c) p-Wert:**
$P(Z > 2.46) = 1 - \Phi(2.46) = 1 - 0.9931 = 0.0069$.
(Das bestätigt die Entscheidung, da $0.0069 < 0.01$).

**(d) Power (Macht) bei $\mu=85.1$:**
Kritische Grenze (in cm): $x_{krit} = 85 + 2.33 \cdot 0.0756 = 85.176$.
Wenn $\mu_{neu} = 85.1$, wie wahrscheinlich ist es, dass wir "Verwerfen" ($X > 85.176$) rufen?
$Z_{neu} = \frac{85.176 - 85.1}{0.0756} = 1.00$.
$P(Z > 1.00) = 1 - 0.8413 = 0.1587$.
Die Macht ist 15.9% (sehr schwach). Der Unterschied (85.1 vs 85.0) ist zu klein für $n=7$.

---
### Offizielle Lösung
$\bar{x} \approx 85.186$. $\sigma=0.2$.<br>(a) $Z \approx 2.46$. $z_{0.99}=2.33$. Verwerfen.<br>(c) $P(Z>2.46) \approx 0.007$.<br>(d) Power $\approx 0.1587$.""",
        "en": r"""### Study.Smart Guide
**Analysis:**
(a) $Z=2.46$. Critical $2.33$. Reject.
(c) p-value = 0.007.
(d) Power calculation:
    Critical value in units = 85.176.
    Prob($X > 85.176 | \mu=85.1$) = Prob($Z > 1.0$) = 0.16.

---
### Official Solution
Mean 85.19. Z=2.46. Reject. p=0.007. Power 0.16."""
    }
}

uebung6_prob3 = {
    "source": "Übung 6, Probe #3",
    "type": "problem",
    "question": {
        "de": r"Internetsessions. $\sigma=35, n=125, \bar{x}=140.5$. Signifikant ($\alpha=0.01$)?<br>(a) Dauer > 148?<br>(b) Dauer < 148?",
        "en": r"Internet sessions. $\sigma=35, n=125, \bar{x}=140.5$. Test $\alpha=0.01$.<br>(a) $>148$? (b) $<148$?"
    },
    "solution": {
        "de": r"""### Study.Smart Guide
**Setup:**
$SE = 35 / \sqrt{125} \approx 3.13$.
Beobachtung: $140.5$. Vergleichswert: $148$.  
$Z = \frac{140.5 - 148}{3.13} = \frac{-7.5}{3.13} = -2.39$.

**(a) Test auf "> 148":**
$H_1: \mu > 148$. (Einseitig rechts).
Da unser Z-Wert negativ ist (-2.39), sind wir *unter* dem Ziel. Wir können niemals beweisen, dass wir *darüber* liegen.
Nicht verwerfen.

**(b) Test auf "< 148":**
$H_1: \mu < 148$. (Einseitig links).
Kritischer Wert (1%): $z_{0.01} = -2.33$.
Unser Wert: $-2.39$.
Der Wert liegt noch weiter links (im Ablehnungsbereich).
**Verwerfen.** Wir können statistisch zeigen, dass die Dauer unter 148 liegt.

---
### Offizielle Lösung
$Z \approx -2.4$.<br>(a) Z negativ, nicht verwerfen.<br>(b) $-2.4 < -2.33 \implies$ Verwerfen. Bestätigt 'unter 148'.""",
        "en": r"""### Study.Smart Guide
**Logic:**
$Z = -2.39$.
(a) Trying to prove "Greater"? Impossible with negative Z.
(b) Trying to prove "Less"? Critical -2.33. We are at -2.39. Success (Reject Null).

---
### Official Solution
Z = -2.4. (a) No. (b) Yes, reject null (confirm < 148)."""
    }
}

uebung6_prob4 = {
    "source": "Übung 6, Probe #4",
    "type": "problem",
    "question": {
        "de": r"Mobilfunk. $n=40, \bar{x}=0.91, \sigma=0.22$. $\alpha=0.01$.<br>(a) Teste: i) $\mu \ne 0.9$. ii) $\mu > 0.9$. iii) $\mu < 0.9$.<br>(b) Hypothesenwahl zum Nachweis Grenzwert 1.0 eingehalten?",
        "en": r"Mobile radiation. Tests against 0.9. (b) Prove < 1.0."
    },
    "solution": {
        "de": r"""### Study.Smart Guide
**(a) Test gegen 0.9:**
$SE = 0.22 / \sqrt{40} \approx 0.0348$.
$Z = \frac{0.91 - 0.9}{0.0348} = \frac{0.01}{0.0348} \approx 0.29$.
Ein Z-Wert von 0.29 ist winzig. (Kritisch wäre > 2.33 oder > 2.57).
Wir sind sehr nah an 0.9. Kein Test wird signifikant sein.

**(b) Nachweis "Grenzwert eingehalten" (< 1.0):**
In der Statistik wollen wir das, was wir beweisen wollen, immer in die **Alternativhypothese $H_1$** schreiben. (Nur $H_1$ kann "bewiesen" werden durch Ablehnung von $H_0$).
Also:
$H_1: \mu < 1.0$ (Eingehalten).
$H_0: \mu \ge 1.0$ (Verletzt).
Test: $Z = \frac{0.91 - 1.0}{0.0348} = -2.58$.
Kritisch (1% links): -2.33.
$-2.58 < -2.33$. Verwerfen!
Wir haben statistisch signifikant gezeigt, dass der Grenzwert eingehalten wird.

---
### Offizielle Lösung
(a) $Z \approx 0.29$. Alle nicht verwerfen.<br>(b) $H_1: \mu < 1.0$ (was man zeigen will), $H_0: \mu \ge 1.0$.""",
        "en": r"""### Study.Smart Guide
**Strategy:**
(a) $Z=0.29$. No significance.
(b) To prove compliance ($\mu < 1.0$), set it as $H_1$.
    Test against $\mu=1.0$: $Z = (0.91-1)/0.035 = -2.57$.
    Reject $H_0$. Proof successful.

---
### Official Solution
Z=0.29. Fail all tests. (b) Alt hypothesis < 1.0."""
    }
}
