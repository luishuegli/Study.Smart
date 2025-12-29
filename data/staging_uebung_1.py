
# Übung 1 Exam Staging File
# Content extracted from:
# - Uebung_1.pdf (questions)
# - ML_Uebung_1.pdf (solutions)
# Dual-Mode: Study.Smart Guide + Official Solution

# ------------------------------------------------------------------
# MULTIPLE CHOICE
# Note: "Übung 1" explicitly allows multiple correct answers.
# Where multiple are correct, the 'solution' text lists them,
# but 'correct_idx' points to the first correct option for compatibility.
# ------------------------------------------------------------------

uebung1_mc1 = {
    "source": "Übung 1, MC #1",
    "type": "mc",
    "question": {
        "de": r"A und B sind zwei unabhängige Ereignisse. Dann gilt:",
        "en": r"A and B are two independent events. Then:"
    },
    "options": [
        r"$P(B | A) = 0$",
        r"$P(B | A) = P(B)$",
        r"$P(B | A) = P(A)$",
        r"Nicht genügend Informationen."
    ],
    "correct_idx": 1,
    "solution": {
        "de": r"""**Richtig: (b)**

### Study.Smart Guide
**Intuition:**
Unabhängigkeit heißt wörtlich: "Das Wissen, dass A passiert ist, ändert meine Einschätzung für B überhaupt nicht."
Die Wahrscheinlichkeit von B bleibt einfach $P(B)$, egal was A macht.
Formel: $P(B|A) = P(B)$.

---
### Offizielle Lösung
Definition der Unabhängigkeit: $P(B|A) = P(B)$.""",
        "en": r"""**Correct: (b)**

### Study.Smart Guide
**Intuition:**
Independence means knowing A occurred gives zero information about B.
So probability of B remains $P(B)$.

---
### Official Solution
Definition of independence: $P(B|A) = P(B)$."""
    }
}

uebung1_mc2 = {
    "source": "Übung 1, MC #2",
    "type": "mc",
    "question": {
        "de": r"A und B sind zwei disjunkte Ereignisse. Dann gilt:",
        "en": r"A and B are two disjoint events. Then:"
    },
    "options": [
        r"$P(B | A) = 0$",
        r"$P(B | A) = P(B)$",
        r"$P(B | A) = P(A)$",
        r"Nicht genügend Informationen."
    ],
    "correct_idx": 0,
    "solution": {
        "de": r"""**Richtig: (a)**

### Study.Smart Guide
**Intuition:**
Disjunkt heißt "getrennt". Sie können niemals gleichzeitig auftreten.
Wenn ich weiß, dass A passiert ist, dann ist es **unmöglich**, dass B passiert ist.
Die Wahrscheinlichkeit ist 0.

---
### Offizielle Lösung
Disjunkt bedeutet $A \cap B = \emptyset$, also $P(A \cap B) = 0$.<br>Somit $P(B|A) = \frac{P(A \cap B)}{P(A)} = 0$.""",
        "en": r"""**Correct: (a)**

### Study.Smart Guide
**Intuition:**
Disjoint = Mutually Exclusive.
If A happened, B cannot happen.
Probability is 0.

---
### Official Solution
Disjoint means $P(A \cap B) = 0$, so $P(B|A) = 0$."""
    }
}

uebung1_mc3 = {
    "source": "Übung 1, MC #3",
    "type": "mc",
    "question": {
        "de": r"$P(A) = 0.5$ und $P(B | A) = 0.6$. Dann gilt:",
        "en": r"$P(A) = 0.5$ and $P(B | A) = 0.6$. Then:"
    },
    "options": [
        r"$P(B \cap A) = 0.3$",
        r"$P(B \cap A) = 0.83$",
        r"$P(B \cap A) = 0.5$",
        r"$P(B \cap A) = 0.6$"
    ],
    "correct_idx": 0,
    "solution": {
        "de": r"""**Richtig: (a)**

### Study.Smart Guide
**Formel:**
Multiplikationsregel: $P(A \cap B) = P(B|A) \cdot P(A)$.
Rechnung: $0.6 \cdot 0.5 = 0.3$.

---
### Offizielle Lösung
$P(A \cap B) = P(B|A) \cdot P(A) = 0.6 \cdot 0.5 = 0.3$.""",
        "en": r"""**Correct: (a)**

### Study.Smart Guide
**Calculation:**
$P(A \cap B) = 0.6 \times 0.5 = 0.3$.

---
### Official Solution
$P(A \cap B) = 0.6 \cdot 0.5 = 0.3$."""
    }
}

uebung1_mc4 = {
    "source": "Übung 1, MC #4",
    "type": "mc",
    "question": {
        "de": r"$P(B | A) = 0$. Dann gilt:",
        "en": r"$P(B | A) = 0$. Then:"
    },
    "options": [
        r"$P(B \cap A) = 0$",
        r"$P(B \cap A) = P(A) \cdot P(B)$",
        r"$P(B \cap A) = 1$",
        r"$P(B \cup A) = 1$"
    ],
    "correct_idx": 0,
    "solution": {
        "de": r"""**Richtig: (a)**

### Study.Smart Guide
**Intuition:**
Wenn die bedingte Wahrscheinlichkeit 0 ist, ist der Schnitt leer (oder hat Wahrscheinlichkeit 0).
"Wenn A ist, ist B unmöglich" $\implies$ A und B überschneiden sich nicht.

---
### Offizielle Lösung
$P(B \cap A) = P(B|A)P(A) = 0 \cdot P(A) = 0$.""",
        "en": r"""**Correct: (a)**

### Study.Smart Guide
**Intuition:**
If $P(B|A)=0$, then the intersection is empty (probability 0).

---
### Official Solution
$P(B \cap A) = 0$."""
    }
}

uebung1_mc5 = {
    "source": "Übung 1, MC #5",
    "type": "mc",
    "question": {
        "de": r"A und B seien zwei Ereignisse und A eine Teilmenge von B ($A \subset B$). Dann gilt:",
        "en": r"A and B are events and A is a subset of B ($A \subset B$). Then:"
    },
    "options": [
        r"$P(A | B) = 1$",
        r"$P(A | B) = P(A)/P(B)$",
        r"$P(A | B) = 0$",
        r"Nicht genügend Informationen."
    ],
    "correct_idx": 1,
    "solution": {
        "de": r"""**Richtig: (b)**

### Study.Smart Guide
**Visualisierung:**
A liegt komplett *im Inneren* von B.
Der Schnitt $A \cap B$ ist also einfach A selbst.
$P(A|B) = \frac{P(A \cap B)}{P(B)} = \frac{P(A)}{P(B)}$.

---
### Offizielle Lösung
$A \subset B \implies A \cap B = A$.<br>$P(A|B) = \frac{P(A \cap B)}{P(B)} = \frac{P(A)}{P(B)}$.""",
        "en": r"""**Correct: (b)**

### Study.Smart Guide
**Visual:**
A is inside B. Intersection is A.
$P(A|B) = P(A)/P(B)$.

---
### Official Solution
$A \subset B \implies A \cap B = A$. So $P(A|B) = P(A)/P(B)$."""
    }
}

uebung1_mc6 = {
    "source": "Übung 1, MC #6",
    "type": "mc",
    "question": {
        "de": r"A und B sind zwei Ereignisse, wobei B eine Teilmenge von A ist ($B \subset A$). Dann gilt:",
        "en": r"A and B are events, where B is a subset of A ($B \subset A$). Then:"
    },
    "options": [
        r"$P(A | B) = 1$",
        r"$P(A | B) = P(A)/P(B)$",
        r"$P(A | B) = 0$",
        r"Nicht genügend Informationen."
    ],
    "correct_idx": 0,
    "solution": {
        "de": r"""**Richtig: (a)**

### Study.Smart Guide
**Intuition:**
B ist eine Insel *innerhalb* von A.
Wenn wir wissen, dass wir auf der Insel B stehen, stehen wir automatisch auch auf dem Land A.
Die Wahrscheinlichkeit ist 100%.

---
### Offizielle Lösung
$B \subset A \implies A \cap B = B$.<br>$P(A|B) = \frac{P(A \cap B)}{P(B)} = \frac{P(B)}{P(B)} = 1$.""",
        "en": r"""**Correct: (a)**

### Study.Smart Guide
**Intuition:**
If you are in B, and B is inside A, you are definitely in A.
Probability 1.

---
### Official Solution
$B \subset A \implies A \cap B = B$. $P(A|B) = P(B)/P(B) = 1$."""
    }
}

uebung1_mc7 = {
    "source": "Übung 1, MC #7",
    "type": "mc",
    "question": {
        "de": r"A und B sind zwei Ereignisse, die sich gegenseitig ausschliessen (disjunkt). Dann gilt:",
        "en": r"A and B are mutually exclusive (disjoint) events. Then:"
    },
    "options": [
        r"$P(A | B) = 1$",
        r"$P(A | B) = P(A)/P(B)$",
        r"$P(A | B) = 0$",
        r"Nicht genügend Informationen."
    ],
    "correct_idx": 2,
    "solution": {
        "de": r"""**Richtig: (c)**

### Study.Smart Guide
**Intuition:**
Gleiche Frage wie MC #2.
Disjunkt = Kein Überlapp = Wahrscheinlichkeit 0.

---
### Offizielle Lösung
Disjunkt $\implies P(A \cap B) = 0 \implies P(A|B) = 0$.""",
        "en": r"""**Correct: (c)**

### Study.Smart Guide
**Intuition:**
Same as MC #2. Disjoint means intersection zero.

---
### Official Solution
Disjoint $\implies P(A|B) = 0$."""
    }
}

uebung1_mc8 = {
    "source": "Übung 1, MC #8",
    "type": "mc",
    "question": {
        "de": r"A und B sind zwei unvereinbare (disjunkte) Ereignisse mit $P(A)>0$ und $P(B)>0$. Dann gilt:",
        "en": r"A and B are mutually exclusive (disjoint) events with $P(A)>0$ and $P(B)>0$. Then:"
    },
    "options": [
        r"A und B sind unabhängig.",
        r"A und B sind abhängig.",
        r"Nicht genügend Informationen."
    ],
    "correct_idx": 1,
    "solution": {
        "de": r"""**Richtig: (b)**

### Study.Smart Guide
**Die Falle:**
Viele verwechseln "Disjunkt" (getrennt) mit "Unabhängig" (egal).
Das Gegenteil ist der Fall! Disjunkte Ereignisse sind **maximal abhängig**.
Wenn A eintritt, verbietet es B komplett. Das ist eine massive Beeinflussung.
Mathematisch: $P(A \cap B) = 0$, aber $P(A)P(B) > 0$. Ungleichheit $\implies$ abhängig.

---
### Offizielle Lösung
$P(A \cap B) = 0$ (da disjunkt).<br>$P(A)P(B) > 0$.<br>Da $0 \neq >0$, sind sie abhängig.""",
        "en": r"""**Correct: (b)**

### Study.Smart Guide
**The Trap:**
Disjoint implies Dependent.
If I roll a 6, I know for sure I didn't roll a 5. The information is perfectly correlated (negatively).

---
### Official Solution
Disjoint ($P(\cap)=0$) implies dependent if probabilities are non-zero."""
    }
}

uebung1_mc9 = {
    "source": "Übung 1, MC #9",
    "type": "mc",
    "question": {
        "de": r"Aus 'A impliziert B' ($A \subseteq B$) folgt ($P(A)>0$):",
        "en": r"From 'A implies B' ($A \subseteq B$) follows ($P(A)>0$):"
    },
    "options": [
        r"$P(A | B) \ge P(A)$",
        r"$P(A | B) < P(A)$",
        r"$P(A | B) \ge P(B)$",
        r"$P(B | A) > 0$"
    ],
    "correct_idx": 0,
    "solution": {
        "de": r"""**Richtig: (a) und (d)**

### Study.Smart Guide
**Analyse:**
*   (a) $P(A|B) = \frac{P(A)}{P(B)}$. Da $P(B) \le 1$, wird der Bruch größer oder gleich $P(A)$. Wenn das "Universum" schrumpft (auf B), nimmt der relative Anteil von A zu.
*   (d) $P(B|A) = 1$. Und $1 > 0$. Das ist auch wahr.
Die offizielle Lösung nennt beides richtig.

---
### Offizielle Lösung
(a) $P(A|B) = P(A)/P(B) \ge P(A)$.<br>(d) $P(B|A) = 1 > 0$.<br>Lösung markiert (a) und (d).""",
        "en": r"""**Correct: (a) and (d)**

### Study.Smart Guide
**Analysis:**
*   (a) Correct. Shrinking the sample space to B increases A's relative size.
*   (d) Correct. If A implies B, $P(B|A)=1$.

---
### Official Solution
(a) $P(A|B) = P(A)/P(B) \ge P(A)$.<br>(d) $P(B|A) = 1$."""
    }
}

uebung1_mc10 = {
    "source": "Übung 1, MC #10",
    "type": "mc",
    "question": {
        "de": r"Aus 'A und B sind unvereinbar' folgt ($P(A)>0$):",
        "en": r"From 'A and B are mutually exclusive' follows ($P(A)>0$):"
    },
    "options": [
        r"$P(A \cap B) = P(A)P(B)$",
        r"$P(A \cup B) = P(A) + P(B)$",
        r"$P(A \cap B) = 0$",
        r"$P(A | B) = P(A)$"
    ],
    "correct_idx": 2,
    "solution": {
        "de": r"""**Richtig: (b) und (c)**

### Study.Smart Guide
**Intuition:**
Unvereinbar (Disjunkt) bedeutet zweierlei:
1.  Der Schnitt ist leer (c).
2.  Die Fläche ist die einfache Summe der Teile (b).

---
### Offizielle Lösung
(b) Additivität für disjunkte Ereignisse.<br>(c) Definition der Unvereinbarkeit.""",
        "en": r"""**Correct: (b) and (c)**

### Study.Smart Guide
**Analysis:**
Disjoint means intersection is zero (c) and union is simple sum (b).

---
### Official Solution
(b) Sum rule.<br>(c) Definition of disjoint."""
    }
}

uebung1_mc11 = {
    "source": "Übung 1, MC #11",
    "type": "mc",
    "question": {
        "de": r"$P(A)=0.5, P(B)=0.4, P(\overline{A \cup B}) = 0.2$. Dann gilt:",
        "en": r"$P(A)=0.5, P(B)=0.4, P(\text{neither A nor B}) = 0.2$. Then:"
    },
    "options": [
        r"A und B sind unvereinbar.",
        r"A und B sind nicht unvereinbar.",
        r"A und B sind unabhängig.",
        r"A und B sind nicht unabhängig."
    ],
    "correct_idx": 1,
    "solution": {
        "de": r"""**Richtig: (b) und (d)**

### Study.Smart Guide
**Schritt-für-Schritt:**
1.  **Außenbereich:** "Weder A noch B" ist 0.2.
    Also ist die Vereinigung $P(A \cup B) = 1 - 0.2 = 0.8$.
2.  **Schnitt:**
    $P(A \cap B) = P(A) + P(B) - P(A \cup B) = 0.5 + 0.4 - 0.8 = 0.1$.
3.  **Check Unvereinbar (Disjunkt):**
    Ist Schnitt 0? Nein (0.1). Also "Nicht unvereinbar" (b).
4.  **Check Unabhängig:**
    Ist $P(A)P(B) = P(A \cap B)$?
    $0.5 \cdot 0.4 = 0.2$.
    Schnitt ist 0.1.
    $0.2 \neq 0.1$. Also "Nicht unabhängig" (d).

---
### Offizielle Lösung
$P(A \cap B) = 0.1$.<br>Da $P(A \cap B) \neq 0$ -> nicht unvereinbar (b).<br>Da $P(A \cap B) = 0.1 \neq P(A)P(B) = 0.2$ -> nicht unabhängig (d).""",
        "en": r"""**Correct: (b) and (d)**

### Study.Smart Guide
**Step-by-Step:**
1.  $P(A \cup B) = 0.8$.
2.  Intersection = $0.5 + 0.4 - 0.8 = 0.1$.
3.  Not disjoint (intersection non-zero).
4.  Not independent ($0.5 \times 0.4 = 0.2 \neq 0.1$).

---
### Official Solution
$P(A \cup B) = 0.8$. $P(A \cap B) = 0.1$.<br>Not disjoint ($0.1 \neq 0$). Not independent ($0.1 \neq 0.2$)."""
    }
}

uebung1_mc12 = {
    "source": "Übung 1, MC #12",
    "type": "mc",
    "question": {
        "de": r"$P(A)=0.6, P(B)=0.8, P(A \cap B)=0.4, P(C)=0.3, C \subset A$. Dann gilt:",
        "en": r"$P(A)=0.6, P(B)=0.8, P(A \cap B)=0.4, P(C)=0.3, C \subset A$. Then:"
    },
    "options": [
        r"A und B sind unvereinbar.",
        r"A und B sind abhängig.",
        r"$A \cup B = S$",
        r"$P(C | A) = 2/3$"
    ],
    "correct_idx": 1, 
    "solution": {
        "de": r"""**Richtig: (b), (c), (e), (f)**

### Study.Smart Guide
**Analyse:**
*   (b) Unabhängigkeitstest: $0.6 \cdot 0.8 = 0.48 \neq 0.4$. Abhängig. Richtig.
*   (c) Vereinigung: $0.6 + 0.8 - 0.4 = 1.0$. Das ist der gesamte Raum S. Richtig.
*   (e) $P(C | A) = P(C \cap A) / P(A)$. Da $C \subset A$, ist $C \cap A = C$.
    $0.3 / 0.6 = 0.5$. (Option d in der Liste sagt 2/3? Die Lösung markiert e/f, die nicht in den Optionen waren? Wir nehmen an, die Lösung addiert e/f).
    Wenn Option d = 2/3 ist, ist sie falsch.
*   (f) $P(A | C) = 1$. Richtig.

---
### Offizielle Lösung
(b) $P(A \cap B)=0.4 \neq 0.48$ (abh).<br>(c) $P(A \cup B) = 0.6+0.8-0.4 = 1$ (Raum S).<br>(e) $P(C|A) = P(C)/P(A) = 0.3/0.6 = 1/2$.<br>(f) $P(A|C) = 1$ (da $C \subset A$).""",
        "en": r"""**Correct: (b), (c), (e), (f)**

### Study.Smart Guide
**Analysis:**
Dependent ($0.48 \neq 0.4$).
Union = 1.0.
$P(C|A) = 0.5$.

---
### Official Solution
Dependent.<br>$P(A \cup B)=1$.<br>$P(C|A)=0.5$.<br>$P(A|C)=1$."""
    }
}

uebung1_mc13 = {
    "source": "Übung 1, MC #13",
    "type": "mc",
    "question": {
        "de": r"A, B unabhängig. $P(A)=0.9, P(A \cup B)=0.5$. Dann gilt:",
        "en": r"A, B independent. $P(A)=0.9, P(A \cup B)=0.5$. Then:"
    },
    "options": [
        r"$P(B) = 0.05$",
        r"$P(B) = 0.44$",
        r"$P(B) = 0.55$",
        r"Nicht genügend Informationen." 
    ],
    "correct_idx": 1,
    "solution": {
        "de": r"""**Richtig: (b)**

### Study.Smart Guide
**Achtung, Fehler in der Aufgabenstellung!**
Die Angabe $P(A)=0.9$ und $P(A \cup B)=0.5$ ist unmöglich. Die Vereinigung muss immer mindestens so groß sein wie A ($0.5 < 0.9$ ist falsch).
Die offizielle Lösung ignoriert dies und kommt auf 0.44.
Wir vermuten, dass eigentlich **$P(A)=0.1$** gemeint war.

**Rechnung (mit $P(A)=0.1$):**
1.  Formel: $P(A \cup B) = P(A) + P(B) - P(A)P(B)$.
2.  Einsetzen: $0.5 = 0.1 + P(B) - 0.1 P(B)$.
3.  $0.4 = 0.9 P(B)$.
4.  $P(B) = 0.4 / 0.9 \approx 0.44$. -> Option (b).

---
### Offizielle Lösung
Hinweis: Die Angabe $P(A)=0.9$ und $P(A \cup B)=0.5$ ist mathematisch unmöglich ($P(A \cup B) \ge P(A)$).<br>Unter der Annahme, dass $P(A) \approx 0.1$, folgt $0.5 = 0.1 + P(B)(0.9) \implies 0.4 = 0.9 P(B) \implies P(B) \approx 0.44$.""",
        "en": r"""**Correct: (b)**

### Study.Smart Guide
**Typo Alert:**
P(A)=0.9 is impossible given Union=0.5.
Assuming P(A)=0.1:
$0.5 = 0.1 + P(B)(1 - 0.1)$.
$0.4 = 0.9 P(B) \implies P(B) \approx 0.44$.

---
### Official Solution
Note: $P(A)=0.9$ contradicts $P(A \cup B)=0.5$. Assuming $P(A)=0.1$ yields correct result."""
    }
}

uebung1_mc14 = {
    "source": "Übung 1, MC #14",
    "type": "mc",
    "question": {
        "de": r"$P(A)=0.1, P(B)=0.5$. Dann gilt:",
        "en": r"$P(A)=0.1, P(B)=0.5$. Then:"
    },
    "options": [
        r"$P(A \cap B) = 0.05$",
        r"$P(A \cap B) = 0.6$",
        r"$P(A \cap B) = P(A | B)$",
        r"Nicht genügend Informationen."
    ],
    "correct_idx": 3,
    "solution": {
        "de": r"""**Richtig: (d)**

### Study.Smart Guide
**Intuition:**
Wir wissen nicht, ob sie unabhängig sind.
*   Wenn unabhängig: Schnitt = 0.05.
*   Wenn disjunkt: Schnitt = 0.
*   Wenn A in B: Schnitt = 0.1.
Alles ist möglich. Daher "Nicht genügend Informationen".

---
### Offizielle Lösung
Ohne Angabe von Unabhängigkeit oder Abhängigkeit kann der Schnitt nicht berechnet werden.""",
        "en": r"""**Correct: (d)**

### Study.Smart Guide
**Intuition:**
We don't know the correlation. Could be anything between 0 and 0.1.

---
### Official Solution
Not enough information (could be dependent)."""
    }
}

uebung1_mc15 = {
    "source": "Übung 1, MC #15",
    "type": "mc",
    "question": {
        "de": r"$P(A)=1/3, P(B)=1/2, P(B|A)=1/3$. Dann gilt:",
        "en": r"$P(A)=1/3, P(B)=1/2, P(B|A)=1/3$. Then:"
    },
    "options": [
        r"$P(A | B) = 1/6$",
        r"$P(A | B) = 1/9$",
        r"$P(A | B) = 2/9$",
        r"$P(A | B) = 1/2$"
    ],
    "correct_idx": 2,
    "solution": {
        "de": r"""**Richtig: (c)**

### Study.Smart Guide
**Schritt-für-Schritt (Bayes 'Lite'):**
1.  **Schnitt berechnen:**
    $P(A \cap B) = P(B|A) P(A) = 1/3 \cdot 1/3 = 1/9$.
2.  **Umkehren:**
    $P(A|B) = \frac{P(A \cap B)}{P(B)} = \frac{1/9}{1/2}$.
3.  **Bruchrechnung:**
    $1/9 \cdot 2/1 = 2/9$.

---
### Offizielle Lösung
$P(A \cap B) = P(B|A)P(A) = 1/3 \cdot 1/3 = 1/9$.<br>$P(A|B) = \frac{P(A \cap B)}{P(B)} = \frac{1/9}{1/2} = 2/9$.""",
        "en": r"""**Correct: (c)**

### Study.Smart Guide
**Step-by-Step:**
1.  Intersection: $1/9$.
2.  Conditional: $(1/9) / (1/2) = 2/9$.

---
### Official Solution
$P(A|B) = \frac{1/9}{1/2} = 2/9$."""
    }
}

uebung1_mc16 = {
    "source": "Übung 1, MC #16",
    "type": "mc",
    "question": {
        "de": r"$P(A \cap B \cap C) = P(A)P(B)P(C)$. Dann gilt:",
        "en": r"$P(A \cap B \cap C) = P(A)P(B)P(C)$. Then:"
    },
    "options": [
        r"A, B, C sind unabhängig.",
        r"A und C sind unabhängig.",
        r"A, B, C sind nicht unabhängig.",
        r"Nicht genügend Informationen für Unabhängigkeit."
    ],
    "correct_idx": 3,
    "solution": {
        "de": r"""**Richtig: (d)**

### Study.Smart Guide
**Die Falle:**
Nur weil das "grosse Produkt" stimmt, heißt das nicht, dass alles unabhängig ist.
Für echte Unabhängigkeit müssen ALLE Teilkombinationen stimmen:
*   $P(A \cap B) = P(A)P(B)$
*   $P(A \cap C) = P(A)P(C)$
*   $P(B \cap C) = P(B)P(C)$
Es könnte sein, dass das 3er-Produkt zufällig passt, aber die Paare völlig falsch liegen.
Daher: Nicht genügend Info.

---
### Offizielle Lösung
Die Produktformel für den 3er-Schnitt ist notwendig, aber nicht hinreichend für Unabhängigkeit. Es muss auch paarweise Unabhängigkeit gelten.""",
        "en": r"""**Correct: (d)**

### Study.Smart Guide
**The Rule:**
Triple product is necessary but NOT sufficient.
You also need pairwise independence ($A \perp B, B \perp C, A \perp C$).

---
### Official Solution
Triple intersection product is necessary but not sufficient (need pairwise independence)."""
    }
}
