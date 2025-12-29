"""
Statistik Prüfungen - Fragen und Lösungen nach Thema organisiert
=================================================================
This is the SINGLE SOURCE OF TRUTH for all exam questions.
All topic files should import questions from here.

Structure:
- Each topic has a dict with question IDs as keys
- Each question contains: question (de/en), options (optional), correct_idx (optional), solution (de/en), source
"""

# =============================================================================
# PART I: WAHRSCHEINLICHKEITSRECHNUNG (Probability Theory)
# =============================================================================

# 1.1 Ereignisse, Ereignisraum und Ereignismenge
QUESTIONS_1_1 = {
    "uebung1_kf1": {
        "source": "Übung 1, Kontrollfrage",
        "type": "theory",
        "question": {
            "de": "Was ist der Unterschied zwischen einem Elementarereignis und einem Ereignis? Was ist der Unterschied zwischen dem Ereignisraum und der Ereignismenge?",
            "en": "What is the difference between an elementary event and an event? What is the difference between the sample space and the event set?"
        },
        "solution": {
            "de": "**Antwort:**<br>• Jedes Elementarereignis ist auch ein Ereignis, aber nicht jedes Ereignis ist gleichzeitig ein Elementarereignis.<br>• Der Ereignisraum S ist ein Element der Ereignismenge E(S).",
            "en": "**Answer:**<br>• Every elementary event is also an event, but not every event is an elementary event.<br>• The sample space S is an element of the event set E(S)."
        }
    },
    "q_1_1_stetig": {
        "source": "Konzept-Check 1.1",
        "type": "theory",
        "question": {
            "de": "**Welcher der folgenden Ereignisräume S ist stetig?**",
            "en": "**Which of the following sample spaces S is continuous?**"
        },
        "options": [
            {"id": "A", "de": r"$S = \{1, 2, 3, 4, 5, 6\}$ (Würfelwurf)", "en": r"$S = \{1, 2, 3, 4, 5, 6\}$ (Die Roll)"},
            {"id": "B", "de": r"$S = \{\text{Kopf, Zahl}\}$ (Münzwurf)", "en": r"$S = \{\text{Heads, Tails}\}$ (Coin Flip)"},
            {"id": "C", "de": r"$S = [0, \infty)$ (Wartezeit an der Haltestelle)", "en": r"$S = [0, \infty)$ (Waiting time at bus stop)"},
            {"id": "D", "de": r"$S = \{0, 1, 2, ...\}$ (Anzahl Kunden)", "en": r"$S = \{0, 1, 2, ...\}$ (Number of Customers)"}
        ],
        "correct_idx": 2,
        "solution": {
            "de": "**Richtig! (C)**<br>Zeit ist eine kontinuierliche Größe (überabzählbar). Alle anderen Beispiele sind **diskret** (abzählbar, auch wenn unendlich wie bei D).",
            "en": "**Correct! (C)**<br>Time is a continuous quantity (uncountable). All other examples are **discrete** (countable, even if infinite like D)."
        }
    }
}

# 1.2 Das Rechnen mit Ereignissen
QUESTIONS_1_2 = {
    "uebung1_kf2": {
        "source": "Übung 1, Kontrollfrage",
        "type": "theory",
        "question": {
            "de": "Sind komplementäre Ereignisse disjunkt? Sind disjunkte Ereignisse komplementär?",
            "en": "Are complementary events disjoint? Are disjoint events complementary?"
        },
        "solution": {
            "de": "**Antwort:**<br>• Komplementär ⇒ disjunkt (Ja)<br>• Disjunkt ⇒ nicht unbedingt komplementär (Nein)",
            "en": "**Answer:**<br>• Complementary ⇒ disjoint (Yes)<br>• Disjoint ⇒ not necessarily complementary (No)"
        }
    },
    "q_1_2_1_a": {
        "source": "Prüfungstraining 1.2.1 (A)",
        "question": {
            "de": r"Werfen von zwei Würfeln ($|S|=36$). Ereignis $A$: 'Mindestens ein Würfel zeigt eine Sechs'. $P(A) = ?$",
            "en": r"Throwing two dice ($|S|=36$). Event $A$: 'At least one die shows a six'. $P(A) = ?$"
        },
        "options": [r"$\frac{10}{36}$", r"$\frac{11}{36}$", r"$\frac{1}{6}$", r"$\frac{12}{36}$"],
        "correct_idx": 1,
        "solution": {
            "de": r"**Richtig! ($\frac{11}{36}$)**<br>Elemente: $\{(6,1), (6,2), \ldots, (6,6), (1,6), \ldots, (5,6)\}$. Das sind $6 + 5 = 11$.",
            "en": r"**Correct! ($\frac{11}{36}$)**<br>Elements: $\{(6,1), (6,2), \ldots, (6,6), (1,6), \ldots, (5,6)\}$. That is $6 + 5 = 11$."
        }
    },
    "q_1_2_1_b": {
        "source": "Prüfungstraining 1.2.1 (B)",
        "question": {
            "de": r"Werfen von zwei Würfeln. Ereignis $B$: 'Die Augensumme ist 9'. $P(B) = ?$",
            "en": r"Throwing two dice. Event $B$: 'The sum of dots is 9'. $P(B) = ?$"
        },
        "options": [r"$\frac{3}{36}$", r"$\frac{4}{36}$", r"$\frac{5}{36}$", r"$\frac{1}{9}$"],
        "correct_idx": 1,
        "solution": {
            "de": r"**Richtig! ($\frac{4}{36}$)**<br>Elemente: $\{(3,6), (4,5), (5,4), (6,3)\}$.",
            "en": r"**Correct! ($\frac{4}{36}$)**<br>Elements: $\{(3,6), (4,5), (5,4), (6,3)\}$."
        }
    },
    "q_1_2_1_c": {
        "source": "Prüfungstraining 1.2.1 (C)",
        "question": {
            "de": r"Werfen von zwei Würfeln. Ereignis $C$: 'Die Augensumme ist kleiner als 4'. $P(C) = ?$",
            "en": r"Throwing two dice. Event $C$: 'The sum of dots is less than 4'. $P(C) = ?$"
        },
        "options": [r"$\frac{3}{36}$", r"$\frac{2}{36}$", r"$\frac{4}{36}$", r"$\frac{1}{12}$"],
        "correct_idx": 0,
        "solution": {
            "de": r"**Richtig! ($\frac{3}{36}$)**<br>Elemente: $\{(1,1), (1,2), (2,1)\}$. Summe < 4 bedeutet Summe 2 oder 3.",
            "en": r"**Correct! ($\frac{3}{36}$)**<br>Elements: $\{(1,1), (1,2), (2,1)\}$. Sum < 4 means sum 2 or 3."
        }
    },
    "test1_q2": {
        "source": "Test 1, Frage 2",
        "question": {
            "de": r"Es seien $A$ und $B$ zwei beliebige Ereignisse mit $P(A) = 0.6$, $P(B) = 0.7$ und $P(\overline{A} \cap B) = 0.1$. Berechnen Sie $P(A \cap \overline{B})$.",
            "en": r"Let $A$ and $B$ be two arbitrary events with $P(A) = 0.6$, $P(B) = 0.7$ and $P(\overline{A} \cap B) = 0.1$. Calculate $P(A \cap \overline{B})$."
        },
        "options": [r"$0$", r"$0.1$", r"$0.2$", r"$0.3$"],
        "correct_idx": 0,
        "solution": {
            "de": r"**Richtig: $0$**<br>Wir wissen $P(B) = P(A \cap B) + P(\overline{A} \cap B)$.<br>Also $0.7 = P(A \cap B) + 0.1 \Rightarrow P(A \cap B) = 0.6$.<br>Weiterhin ist $P(A) = P(A \cap B) + P(A \cap \overline{B})$.<br>Also $0.6 = 0.6 + P(A \cap \overline{B}) \Rightarrow P(A \cap \overline{B}) = 0$.",
            "en": r"**Correct: $0$**<br>We know $P(B) = P(A \cap B) + P(\overline{A} \cap B)$.<br>So $0.7 = P(A \cap B) + 0.1 \Rightarrow P(A \cap B) = 0.6$.<br>Furthermore $P(A) = P(A \cap B) + P(A \cap \overline{B})$.<br>So $0.6 = 0.6 + P(A \cap \overline{B}) \Rightarrow P(A \cap \overline{B}) = 0$."
        }
    },
    "test3_q1": {
        "source": "Test 3, Frage 1",
        "question": {
            "de": r"Die Ereignisse $A$ und $B$ sind disjunkt mit $P(A)>0, P(B)>0$. Welche Aussage stimmt?",
            "en": r"Events $A$ and $B$ are disjoint with $P(A)>0, P(B)>0$. Which statement is true?"
        },
        "options": [
            {"de": r"$P(\overline{A} \cap \overline{B}) + P(B) > 1 - P(A)$", "en": r"$P(\overline{A} \cap \overline{B}) + P(B) > 1 - P(A)$"},
            {"de": r"$P(A \cap B) > P(A)$", "en": r"$P(A \cap B) > P(A)$"},
            {"de": r"$P(A|B) = P(B|A)$", "en": r"$P(A|B) = P(B|A)$"},
            {"de": r"$P(A \cup B) < P(A)$", "en": r"$P(A \cup B) < P(A)$"}
        ],
        "correct_idx": 2,
        "solution": {
            "de": r"**Richtig: (c)**<br>Da $A$ und $B$ disjunkt sind, ist $A \cap B = \emptyset$, also $P(A \cap B) = 0$.<br>Daher ist $P(A|B) = 0$ und $P(B|A) = 0$.",
            "en": r"**Correct: (c)**<br>Since $A$ and $B$ are disjoint, $A \cap B = \emptyset$, thus $P(A \cap B) = 0$.<br>Therefore $P(A|B) = 0$ and $P(B|A) = 0$."
        }
    },
}

# 1.3 Laplace Wahrscheinlichkeit
QUESTIONS_1_3 = {
    "q_1_3_concept": {
        "source": "Konzept-Check 1.3",
        "question": {
            "de": r"**Wann darf man die Laplace-Formel $P(A) = \frac{g}{m}$ verwenden?**",
            "en": r"**When are you allowed to use the Laplace formula $P(A) = \frac{g}{m}$?**"
        },
        "options": [
             {"id": "a", "de": "Immer wenn es eine endliche Anzahl Ereignisse gibt", "en": "Always when there is a finite number of events"},
             {"id": "b", "de": "Wenn man die Wahrscheinlichkeiten nicht kennt", "en": "When probabilities are unknown"},
             {"id": "c", "de": "Wenn jedes Elementarereignis die exakt gleiche Wahrscheinlichkeit hat", "en": "When every elementary event has exactly the same probability"}
        ],
        "correct_idx": 2,
        "solution": {
            "de": "**Richtig! (c)**<br>Das 'Indifferenzprinzip' ist entscheidend. Bei einem gezinkten Würfel (ungleiche Wahrscheinlichkeiten) funktioniert Laplace nicht.",
            "en": "**Correct (c)**<br>The 'Principle of Indifference' is crucial. Laplace does not work for loaded dice (unequal probabilities)."
        }
    }
}

# 1.4 Axiome der Wahrscheinlichkeit
QUESTIONS_1_4 = {
    "q_1_4_logic": {
        "source": "Logik-Check 1.4",
        "question": {
            "de": r"**Welche der folgenden Wahrscheinlichkeitszuweisungen ist ungültig?** ($S = \{e_1, e_2, e_3\}$)",
            "en": r"**Which of the following probability assignments is invalid?** ($S = \{e_1, e_2, e_3\}$)"
        },
        "options": [
            {"id": "a", "text": r"$P(e_1)=0.3, \; P(e_2)=0.3, \; P(e_3)=0.4$"},
            {"id": "b", "text": r"$P(e_1)=0.5, \; P(e_2)=0.5, \; P(e_3)=0$"},
            {"id": "c", "text": r"$P(e_1)=0.6, \; P(e_2)=-0.1, \; P(e_3)=0.5$"}
        ],
        "correct_idx": 2,
        "solution": {
            "de": "**Richtig! (c)**<br>Wahrscheinlichkeiten können nicht negativ sein. Dies verletzt **Axiom 1**.",
            "en": "**Correct (c)**<br>Probabilities cannot be negative. This violates **Axiom 1**."
        }
    }
}

# 1.5 Additionssatz
QUESTIONS_1_5 = {
    "q_1_5_add": {
        "source": "HS2022, MC 5",
        "question": {
             "de": r"**Gegeben sind:** $P(A)=0.3, P(B)=0.4, P(\overline{A}|B)=0.75$.\n\n**Gesucht ist:** $P(A \cup B)$.",
             "en": r"**Given:** $P(A)=0.3, P(B)=0.4, P(\overline{A}|B)=0.75$.\n\n**Find:** $P(A \cup B)$."
        },
        "hint": {
             "de": r"Hinweis: Nutze zuerst das Komplement $P(A|B) = 1 - P(\overline{A}|B)$. Verwende dann die Multiplikationsregel: $P(A \cap B) = P(A|B) \cdot P(B)$.", 
             "en": r"Hint: First find $P(A|B) = 1 - P(\overline{A}|B)$. Then use the multiplication rule: $P(A \cap B) = P(A|B) \cdot P(B)$."
        },
        "options": [r"$0.55$", r"$0.60$", r"$0.70$", r"$0.25$"],
        "correct_idx": 1,
        "solution": {
             "de": r"**Richtig: $0.6$**<br>1. $P(A|B) = 1 - 0.75 = 0.25$<br>2. $P(A \cap B) = 0.25 \cdot 0.4 = 0.1$<br>3. $P(A \cup B) = 0.3 + 0.4 - 0.1 = 0.6$",
             "en": r"**Correct: $0.6$**<br>1. $P(A|B) = 1 - 0.75 = 0.25$<br>2. $P(A \cap B) = 0.25 \cdot 0.4 = 0.1$<br>3. $P(A \cup B) = 0.3 + 0.4 - 0.1 = 0.6$"
        }
    },
    "hs2022_mc5": {
        "source": "HS 2022 Januar, MC #5",
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
            "de": r"**Richtig: (b)**<br>**Berechnung:**<br>1. $P(A \cap B) = P(A|B) \cdot P(B) = 0.75 \cdot 0.4 = 0.3$.<br>2. $P(A \cup B) = P(A) + P(B) - P(A \cap B) = 0.3 + 0.4 - 0.3 = 0.4$.<br><br>**Achtung:** Die offizielle Lösung gibt **0.6** an. Dies ist mathematisch mit den gegebenen Zahlen nicht herleitbar. Wir folgen hier der offiziellen Lösung (b), weisen aber auf den Fehler hin.",
            "en": r"**Correct: (b)**<br>**Calculation:**<br>1. $P(A \cap B) = 0.3$.<br>2. $P(A \cup B) = 0.4$.<br><br>**Note:** The official key says **0.6**. This contradicts the math. We list (b) to match the exam key, but the calculation yields 0.4."
        }
    },
    "uebung1_mc11": {
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
    },
    "uebung1_mc13": {
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
}

# 1.6 Wahrscheinlichkeitsräume
QUESTIONS_1_6 = {
    "q_1_6_dart": {
        "source": "Das Dart-Paradoxon",
        "question": {
            "de": "In einem stetigen Raum (z.B. Dartscheibe), wie groß ist die Wahrscheinlichkeit, einen exakten Punkt zu treffen?",
            "en": "In a continuous space (e.g. dartboard), what is the probability of hitting an exact point?"
        },
        "options": [r"$0$", "Unendlich klein, aber > 0", r"$1$", "Abhängig vom Radius"],
        "correct_idx": 0,
        "solution": {
            "de": r"**Antwort: $0$**<br>Ein mathematischer Punkt hat keine Fläche. $P(X=x) = 0$. Nur Intervalle/Flächen haben Wahrscheinlichkeiten $> 0$.",
            "en": r"**Answer: $0$**<br>A mathematical point has no area. $P(X=x) = 0$. Only intervals/areas have probabilities $> 0$."
        }
    }
}

# 1.7 Bedingte Wahrscheinlichkeit und stochastische Unabhängigkeit
QUESTIONS_1_7 = {
    "hs2024_mc5": {
        "source": "HS 2024 Januar, MC #5",
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
            "de": r"**Richtig: (c)**<br>Primzahlen: {2, 3, 5, ...}. Nur die 2 ist gerade.<br>A (Summe ungerade) $\implies$ genau eine Gerade (die 2) oder 3 Gerade (unmöglich). Also 2 muss dabei sein.<br>B (Alle ungerade) $\implies$ 2 ist NICHT dabei.<br>A und B schließen sich aus (disjunkt). Disjunkte Ereignisse sind abhängig.",
            "en": r"**Correct: (c)**<br>Primes: {2, 3, 5, ...}. Only 2 is even.<br>A (Sum odd) $\implies$ exactly one even (2) present.<br>B (All odd) $\implies$ 2 is NOT present.<br>A and B exclude each other (disjoint). Disjoint events are dependent."
        }
    },
    "uebung1_mc1": {
        "source": "Übung 1, MC1",
        "question": {
            "de": r"$A$ und $B$ sind zwei unabhängige Ereignisse. Dann gilt:",
            "en": r"$A$ and $B$ are two independent events. Then:"
        },
        "options": [
            {"de": r"$P[B | A] = 0$", "en": r"$P[B | A] = 0$"},
            {"de": r"$P[B | A] = P[B]$", "en": r"$P[B | A] = P[B]$"},
            {"de": r"$P[B | A] = P[A]$", "en": r"$P[B | A] = P[A]$"},
            {"de": "Wir haben nicht genügend Informationen", "en": "We do not have enough information"}
        ],
        "correct_idx": 1,
        "solution": {
            "de": r"**Richtig: (b)**<br>Definition der Unabhängigkeit: Das Eintreten von $A$ ändert die Wahrscheinlichkeit von $B$ nicht.",
            "en": r"**Correct: (b)**<br>Definition of independence: The occurrence of $A$ does not change the probability of $B$."
        }
    },
    "uebung1_mc2": {
        "source": "Übung 1, MC2",
        "question": {
            "de": r"$A$ und $B$ sind zwei disjunkte Ereignisse ($P(A)>0$). Dann gilt:",
            "en": r"$A$ and $B$ are two disjoint events ($P(A)>0$). Then:"
        },
        "options": [
            {"de": r"$P[B | A] = 0$", "en": r"$P[B | A] = 0$"},
            {"de": r"$P[B | A] = P[B]$", "en": r"$P[B | A] = P[B]$"},
            {"de": r"$P[B | A] = P[A]$", "en": r"$P[B | A] = P[A]$"},
            {"de": "Wir haben nicht genügend Informationen", "en": "We do not have enough information"}
        ],
        "correct_idx": 0,
        "solution": {
            "de": r"**Richtig: (a)**<br>Wenn $A$ eingetreten ist, kann $B$ nicht mehr eintreten (da keine Schnittmenge).",
            "en": r"**Correct: (a)**<br>If $A$ has occurred, $B$ cannot occur (since there is no intersection)."
        }
    },
    "uebung1_mc8": {
        "source": "Übung 1, MC8",
        "question": {
            "de": r"$A$ und $B$ sind zwei unvereinbare (disjunkte) Ereignisse mit $P(A) > 0$ und $P(B) > 0$. Dann gilt:",
            "en": r"$A$ and $B$ are two mutually exclusive (disjoint) events with $P(A) > 0$ and $P(B) > 0$. Then:"
        },
        "options": [
            {"de": r"$A$ und $B$ sind unabhängig", "en": r"$A$ and $B$ are independent"},
            {"de": r"$A$ und $B$ sind abhängig", "en": r"$A$ and $B$ are dependent"},
            {"de": "Wir haben nicht genügend Informationen", "en": "We do not have enough information"}
        ],
        "correct_idx": 1,
        "solution": {
            "de": r"**Richtig: (b)**<br>Disjunkte Ereignisse (mit positiver Wahrscheinlichkeit) sind STARK abhängig. Wenn ich weiss $A$ ist eingetreten, weiss ich zu $100\%$, dass $B$ NICHT eingetreten ist.",
            "en": r"**Correct: (b)**<br>Disjoint events (with positive probability) are STRONGLY dependent. If I know $A$ has occurred, I know $100\%$ that $B$ has NOT occurred."
        }
    },
    "uebung1_prob3": {
        "source": "Übung 1, Problem 3",
        "type": "problem",
        "question": {
            "de": r"Gegeben: $P(A) = 0.5$, $P(B) = 0.3$, $P(A \cap B) = 0.2$.<br>Berechnen Sie:<br>(a) $P(A \cup B)$<br>(b) $P(A | B)$<br>(c) $P(A \cap \overline{B})$",
            "en": r"Given: $P(A) = 0.5$, $P(B) = 0.3$, $P(A \cap B) = 0.2$.<br>Calculate:<br>(a) $P(A \cup B)$<br>(b) $P(A | B)$<br>(c) $P(A \cap \overline{B})$"
        },
        "solution": {
            "de": r"**Lösung:**<br>(a) $P(A \cup B) = 0.5 + 0.3 - 0.2 = \mathbf{0.6}$<br>(b) $P(A | B) = 0.2 / 0.3 = \mathbf{2/3}$<br>(c) $P(A \cap \overline{B}) = P(A) - P(A \cap B) = 0.5 - 0.2 = \mathbf{0.3}$",
            "en": r"**Solution:**<br>(a) $P(A \cup B) = 0.5 + 0.3 - 0.2 = \mathbf{0.6}$<br>(b) $P(A | B) = 0.2 / 0.3 = \mathbf{2/3}$<br>(c) $P(A \cap \overline{B}) = P(A) - P(A \cap B) = 0.5 - 0.2 = \mathbf{0.3}$"
        }
    },
    "hs2023_mc1": {
        "source": "HS2023, MC1",
        "question": {
            "de": r"Folgende Informationen sind gegeben: $P(A) = 0.5$, $P(B) = 0.3$, $P(A \cup B) = 0.4$. Welche der folgenden Aussagen ist wahr?",
            "en": r"The following information is given: $P(A) = 0.5$, $P(B) = 0.3$, $P(A \cup B) = 0.4$. Which of the following statements is true?"
        },
        "options": [
            {"de": r"$A$ und $B$ sind disjunkt", "en": r"$A$ and $B$ are disjoint"},
            {"de": r"$A$ und $B$ sind unabhängig", "en": r"$A$ and $B$ are independent"},
            {"de": r"$A$ und $B$ sind nicht unabhängig", "en": r"$A$ and $B$ are not independent"},
            {"de": "Nicht genügend Informationen gegeben", "en": "Not enough information given"}
        ],
        "correct_idx": 2,
        "solution": {
            "de": r"**Richtig: (c)**<br>$P(A \cap B) = P(A) + P(B) - P(A \cup B) = 0.5 + 0.3 - 0.4 = 0.4$.<br>$P(A)P(B) = 0.15 \neq 0.4$. Also abhängig.",
            "en": r"**Correct: (c)**<br>$P(A \cap B) = P(A) + P(B) - P(A \cup B) = 0.5 + 0.3 - 0.4 = 0.4$.<br>$P(A)P(B) = 0.15 \neq 0.4$. Therefore dependent."
        }
    },
    "hs2024_mc3": {
        "source": "HS2024, MC3",
        "question": {
            "de": "**Gegeben:** $\\mathbb{P}(A)=\\frac{1}{2}$, $\\mathbb{P}(B)=\\frac{2}{3}$ und $\\mathbb{P}(A\\cap B)=\\frac{1}{4}$.\\n\\n**Gesucht:** $\\mathbb{P}(A|\\overline{B})$.",
            "en": "**Given:** $\\mathbb{P}(A)=\\frac{1}{2}$, $\\mathbb{P}(B)=\\frac{2}{3}$ and $\\mathbb{P}(A\\cap B)=\\frac{1}{4}$.\\n\\n**Find:** $\\mathbb{P}(A|\\overline{B})$."
        },
        "options": ["0.25", "0.50", "0.75", "0.33"],
        "correct_idx": 2,
        "solution": {
            "de": "**Schritt 1: Formel aufstellen**\\n$P(A|\\overline{B}) = \\frac{P(A \\cap \\overline{B})}{P(\\overline{B})}$\\n\\n**Schritt 2: Nenner berechnen**\\n$P(\\overline{B}) = 1 - P(B) = 1 - \\frac{2}{3} = \\frac{1}{3}$.\\n\\n**Schritt 3: Zähler berechnen**\\n$P(A \\cap \\overline{B})$ ist 'A ohne B'.\\n$P(A \\cap \\overline{B}) = P(A) - P(A \\cap B) = \\frac{1}{2} - \\frac{1}{4} = \\frac{1}{4}$.\\n\\n**Schritt 4: Einsetzen**\\n$\\frac{1/4}{1/3} = \\frac{1}{4} \\cdot \\frac{3}{1} = \\frac{3}{4} = \\mathbf{0.75}$.",
            "en": "**Step 1: Setup Formula**\\n$P(A|\\overline{B}) = \\frac{P(A \\cap \\overline{B})}{P(\\overline{B})}$\\n\\n**Step 2: Calculate Denominator**\\n$P(\\overline{B}) = 1 - P(B) = 1 - \\frac{2}{3} = \\frac{1}{3}$.\\n\\n**Step 3: Calculate Numerator**\\n$P(A \\cap \\overline{B})$ is 'A without B'.\\n$P(A \\cap \\overline{B}) = P(A) - P(A \\cap B) = \\frac{1}{2} - \\frac{1}{4} = \\frac{1}{4}$.\\n\\n**Step 4: Solve**\\n$\\frac{1/4}{1/3} = \\frac{1}{4} \\cdot \\frac{3}{1} = \\frac{3}{4} = \\mathbf{0.75}$."
        },
        "hint": {
            "de": "Hinweis: Nutze die Formel $P(A|\\overline{B}) = \\frac{P(A \\cap \\overline{B})}{P(\\overline{B})}$.",
            "en": "Hint: Use the formula $P(A|\\overline{B}) = \\frac{P(A \\cap \\overline{B})}{P(\\overline{B})}$."
        }
    },
    "uebung1_mc5": {
        "source": "Übung 1, MC5 (Logik-Check)",
        "question": {
            "de": "**Zufallsexperiment:** Ziehen von 4 Zahlen aus den ersten 12 Primzahlen (ohne Zurücklegen).\\n\\n$A$: Summe ist ungerade.\\n$B$: Alle 4 Zahlen sind ungerade.\\n\\n**Sind $A$ und $B$ unabhängig oder disjunkt?**",
            "en": "**Experiment:** Draw 4 numbers from the first 12 primes (without replacement).\\n\\n$A$: Sum is odd.\\n$B$: All 4 numbers are odd.\\n\\n**Are $A$ and $B$ independent or disjoint?**"
        },
        "options": [
            {"de": "Unabhängig und Disjunkt", "en": "Independent and Disjoint"},
            {"de": "Abhängig und Disjunkt", "en": "Dependent and Disjoint"},
            {"de": "Unabhängig und Nicht-Disjunkt", "en": "Independent and Non-Disjoint"},
            {"de": "Abhängig und Nicht-Disjunkt", "en": "Dependent and Non-Disjoint"}
        ],
        "correct_idx": 1,
        "solution": {
            "de": "**Richtig: Abhängig und Disjunkt**<br>Es gibt nur *eine* gerade Primzahl (2). $A$ (Summe Ungerade) braucht die 2 (3 ungerade + 1 gerade). $B$ (Alle Ungerade) verbietet die 2. Also Disjunkt. Disjunkt impliziert Abhängigkeit (A schließt B aus).",
            "en": "**Correct: Dependent and Disjoint**<br>There is only *one* even prime (2). $A$ (Odd Sum) requires 2 (3 odd + 1 even). $B$ (All Odd) forbids 2. Thus Disjoint. Disjoint implies dependency (A excludes B)."
        },
        "hint": {
            "de": "Hinweis: Wie viele gerade Primzahlen gibt es?",
            "en": "Hint: How many even prime numbers are there?"
        }
    },
    "hs2023_mc1": {
        "source": "HS 2023 Januar, MC #1",
        "type": "mc",
        "question": {
            "de": r"Folgende Informationen sind gegeben: $P(A) = 0.5$, $P(B) = 0.3$, $P(A \cup B) = 0.4$. Welche der folgenden Aussagen ist wahr?",
            "en": r"Given: $P(A) = 0.5$, $P(B) = 0.3$, $P(A \cup B) = 0.4$. Which of the following statements is true?"
        },
        "options": [
            r"A und B sind disjunkt.",
            r"A und B sind unabhängig.",
            r"A und B sind nicht unabhängig.",
            r"Nicht genügend Informationen gegeben."
        ],
        "correct_idx": 2,
        "solution": {
            "de": r"**Richtig: (c)**<br>$P(A \cap B) = P(A) + P(B) - P(A \cup B) = 0.5 + 0.3 - 0.4 = 0.4$.<br>Unabhängigkeitstest: $P(A)P(B) = 0.15 \neq 0.4$. Also abhängig.",
            "en": r"**Correct: (c)**<br>$P(A \cap B) = P(A) + P(B) - P(A \cup B) = 0.5 + 0.3 - 0.4 = 0.4$.<br>Independence check: $P(A)P(B) = 0.15 \neq 0.4$. Thus dependent."
        }
    },
    "hs2023_mc8": {
        "source": "HS 2023 Januar, MC #8",
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
            "de": r"**Richtig: (b)**<br>Wenn B das Ereignis A wahrscheinlicher macht, muss das Nicht-Eintreten von B das Ereignis A unwahrscheinlicher machen (Erhaltung der Gesamtwahrscheinlichkeit).",
            "en": r"**Correct: (b)**<br>If B makes A more likely, then Not-B must make A less likely (Conservation of Probability)."
        }
    },
    "hs2022_mc9": {
        "source": "HS 2022 Januar, MC #9",
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
            "de": r"**Richtig: (d)**<br>(a) Falsch, Satz von Bayes ist $P(A|B)P(B) = P(B|A)P(A)$.<br>(b) Falsch, wenn $B \subset A$, dann $P(B) = P(A \cap B)$.<br>(c) Falsch, abhängig von Korrelation / Unabhängigkeit.",
            "en": r"**Correct: (d)**<br>(a) False, Bayes terms swapped.<br>(b) False, equality holds if subset.<br>(c) False, depends on correlation."
        }
    },
    "hs2022_mc12": {
        "source": "HS 2022 Januar, MC #12",
        "type": "mc",
        "question": {
            "de": r"Das Wal-Paradoxon: Zwei Wale, Geschlecht 50/50, Geburtstag unabhängig (1/7). Verhältnis $P(A|B)$ vs $P(A|C)$.<br>A: Beide männlich.<br>B: Mindestens einer männlich.<br>C: Mindestens einer männlich UND am Dienstag geboren.",
            "en": r"The Whale Paradox: Two whales, 50/50 gender, independent birthday (1/7). Ratio $P(A|B)$ vs $P(A|C)$.<br>A: Both male.<br>B: At least one male.<br>C: At least one male AND born on Tuesday."
        },
        "options": [
            r"$P(A|B) = P(A|C)$",
            r"$P(A|B) > P(A|C)$",
            r"$P(A|B) < P(A|C)$",
            r"Nicht genügend Infos."
        ],
        "correct_idx": 2,
        "solution": {
            "de": r"**Richtig: (c)**<br>Dies ist eine Variation des 'Boy or Girl Paradox'.<br>$P(A|B) = 1/3$.<br>$P(A|C) = 13/27 \approx 0.48$.<br>Je spezifischer die Zusatzinfo (Dienstag), desto näher an 1/2.",
            "en": r"**Correct: (c)**<br>Variation of the 'Boy or Girl Paradox'.<br>$P(A|B) = 1/3$.<br>$P(A|C) = 13/27 \approx 0.48$.<br>Specificity pushes probability towards 1/2."
        }
    },
    "test1_q1": {
        "source": "Test 1, Frage 1",
        "question": {
            "de": r"300 Hörer einer Statistik-Vorlesung:<br>VWL: $42$ m, $93$ w<br>BWL: $78$ m, $87$ w<br>Eine Hörerin wird gewählt. Wahrscheinlichkeit, dass sie BWL studiert?",
            "en": r"300 students in a stats lecture:<br>Econ: $42$ m, $93$ f<br>Bus: $78$ m, $87$ f<br>A female student is chosen. Probability she studies Business?"
        },
        "options": [r"$0.31$", r"$0.29$", r"$0.71$", r"$0.48$"],
        "correct_idx": 3,
        "solution": {
            "de": r"**Richtig: $0.48$**<br>Gesucht: $P(\text{BWL}|\text{w})$.<br>Anzahl w $= 93 + 87 = 180$.<br>Anzahl w und BWL $= 87$.<br>$P(\text{BWL}|\text{w}) = 87/180 \approx 0.48$.",
            "en": r"**Correct: $0.48$**<br>Find: $P(\text{Bus}|\text{f})$.<br>Total f $= 93 + 87 = 180$.<br>Total f and Bus $= 87$.<br>$P(\text{Bus}|\text{f}) = 87/180 \approx 0.48$."
        }
    }
}

# 1.8 Totale Wahrscheinlichkeit & Bayes
QUESTIONS_1_8 = {
    "uebung1_prob5": {
        "source": "Übung 1, Problem 5",
        "type": "problem",
        "question": {
            "de": r"Maschine $A$ produziert $70\%$ der Stücke ($8\%$ Fehlerquote). Maschine $B$ produziert $30\%$ ($6\%$ Fehlerquote). Ein zufällig gezogenes Stück ist fehlerhaft. Wie gross ist die Wahrscheinlichkeit, dass es von $A$ kommt?",
            "en": r"Machine $A$ produces $70\%$ of parts ($8\%$ defect rate). Machine $B$ produces $30\%$ ($6\%$ defect rate). A randomly chosen part is defective. What is the probability it came from $A$?"
        },
        "solution": {
            "de": r"**Lösung:**<br>$P(A|F) = (0.08 \cdot 0.7) / (0.08 \cdot 0.7 + 0.06 \cdot 0.3) = 0.056 / 0.074 \approx \mathbf{75.68\%}$",
            "en": r"**Solution:**<br>$P(A|F) = (0.08 \cdot 0.7) / (0.08 \cdot 0.7 + 0.06 \cdot 0.3) = 0.056 / 0.074 \approx \mathbf{75.68\%}$"
        }
    },
     "uebung1_prob6": {
        "source": "Übung 1, Problem 6",
        "type": "problem",
        "question": {
            "de": r"Gymnasium-Statistik:<br>• $40\%$ bestehen die Matura nicht ($NM$)<br>• $90\%$ von $NM$ hatten negativen Aufnahmetest ($T-$)<br>• $1\%$ von Bestandenen ($M$) hatten negativen Test ($T-$)<br>Wie gross ist $P(T-)$?",
            "en": r"High School Statistics:<br>• $40\%$ fail the Matura ($NM$)<br>• $90\%$ of $NM$ had a negative admission test ($T-$)<br>• $1\%$ of those who passed ($M$) had a negative test ($T-$)<br>What is $P(T-)$?"
        },
        "solution": {
            "de": r"**Lösung:**<br>$P(T-) = P(T-|NM)P(NM) + P(T-|M)P(M)$<br>$= 0.9\cdot 0.4 + 0.01\cdot 0.6 = 0.36 + 0.006 = \mathbf{36.6\%}$",
            "en": r"**Solution:**<br>$P(T-) = P(T-|NM)P(NM) + P(T-|M)P(M)$<br>$= 0.9\cdot 0.4 + 0.01\cdot 0.6 = 0.36 + 0.006 = \mathbf{36.6\%}$"
        }
    },
    "uebung1_prob_factory": {
        "source": "Interactive Mission: The Factory",
        "type": "problem",
        "question": {
            "de": r"Eine Maschine $A$ produziert $20\%$ aller Teile mit $5\%$ Fehler. Maschine $B$ produziert $80\%$ mit $1\%$ Fehler. Wie hoch ist die totale Fehlerrate?",
            "en": r"Machine $A$ produces $20\%$ of all parts with $5\%$ defects. Machine $B$ produces $80\%$ with $1\%$ defects. What is the total defect rate?"
        },
        "options": [r"$3\%$", r"$1.8\%$", r"$6\%$", r"$2.5\%$"],
        "correct_idx": 1,
        "solution": {
            "de": r"**Antwort: $1.8\%$**<br>Satz der totalen Wahrscheinlichkeit:<br>$P(D) = 0.05 \cdot 0.20 + 0.01 \cdot 0.80 = 0.01 + 0.008 = 0.018 = 1.8\%$",
            "en": r"**Answer: $1.8\%$**<br>Law of Total Probability:<br>$P(D) = 0.05 \cdot 0.20 + 0.01 \cdot 0.80 = 0.01 + 0.008 = 0.018 = 1.8\%$"
        }
    },
    "hs2022_mc2": {
        "source": "HS 2022 Januar, MC #2",
        "question": {
            "de": r"Sie haben $1000$ Münzen und wissen, dass es unter den $1000$ Münzen genau eine besondere Münze gibt, die auf beiden Seiten Zahl hat. Sie wählen eine Münze zufällig aus diesen $1000$ aus. Sie werfen diese eine Münze $10$ Mal. Sie zeigt $10$ Mal hintereinander Zahl an. Wie hoch ist die Wahrscheinlichkeit, dass Sie die besondere Münze genommen haben?",
            "en": r"You have $1000$ coins and know that among them there is exactly one special coin with tails on both sides. You randomly pick one coin and flip it $10$ times. It shows tails $10$ times in a row. What is the probability that you picked the special coin?"
        },
        "options": [r"$50.6\%$", r"$99.9\%$", r"$0.1\%$", r"$25\%$"],
        "correct_idx": 0,
        "solution": {
            "de": r"**Richtig: $50.6\%$**<br>Bayes' Theorem:<br>$P(\text{special}|10T) = \frac{1 \cdot \frac{1}{1000}}{1 \cdot \frac{1}{1000} + (\frac{1}{2})^{10} \cdot \frac{999}{1000}} \approx 0.506$",
            "en": r"**Correct: $50.6\%$**<br>Bayes' Theorem:<br>$P(\text{special}|10T) = \frac{1 \cdot \frac{1}{1000}}{1 \cdot \frac{1}{1000} + (\frac{1}{2})^{10} \cdot \frac{999}{1000}} \approx 0.506$"
        }
    },
    "hs2022_mc1": {
        "source": "HS 2022 Januar, MC #1",
        "question": {
            "de": "Drei Freunde spielen ein Spiel. Sie werfen eine faire Münze. Spieler 1 gewinnt bei erstem Wurf Kopf. Spieler 2 gewinnt bei zweitem Wurf Kopf. Spieler 3 gewinnt bei drittem Wurf Kopf. Wenn bis zur dritten Runde kein Gewinner, beginnt das Spiel von neuem. Wie hoch ist P(Spieler 3 gewinnt)?",
            "en": "Three friends play a game. They flip a fair coin. Player 1 wins on first flip heads. Player 2 wins on second flip heads. Player 3 wins on third flip heads. If no winner by round 3, game restarts. What is P(Player 3 wins)?"
        },
        "options": ["2/7", "1/7", "1/8", "3/7"],
        "correct_idx": 1,
        "solution": {
            "de": "**Richtig: 1/7**<br>Geometrische Reihe: $\\sum (1/2)^{3+6k} = (1/8) \\cdot \\frac{1}{1-(1/8)} = \\frac{1}{7}$",
            "en": "**Correct: 1/7**<br>Geometric series: $\\sum (1/2)^{3+6k} = (1/8) \\cdot \\frac{1}{1-(1/8)} = \\frac{1}{7}$"
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
            "de": r"**Lösung 2A:**<br>2. P(Rot 2) = 2/3.<br>3. P(R1|R2) = 1/2.<br><br>**Lösung 2B:**<br>1. Binomial(n=20, p=1/3). P(X $\ge$ 12) $\approx$ 0.013.<br>2. $\lambda = 100 \cdot 0.013 = 1.3$. P(Y $\ge$ 3) = 1 - P(Y $\le$ 2) $\approx$ 0.1429.",
            "en": r"**Solution 2A:**<br>2. P(Red 2) = 2/3.<br>3. P(R1|R2) = 1/2.<br><br>**Solution 2B:**<br>1. Binomial(n=20, p=1/3). P(X $\ge$ 12) $\approx$ 0.013.<br>2. $\lambda = 100 \cdot 0.013 = 1.3$. P(Y $\ge$ 3) = 1 - P(Y $\le$ 2) $\approx$ 0.1429."
        }
    }
}
QUESTIONS_1_9 = {
    "hs2024_mc6": {
        "source": "HS 2024 Januar, MC #6",
        "type": "mc",
        "question": {
            "de": r"Interview $P(I)=0.1$. Gute Note $G$. $P(G|I)=0.9$, $P(G|\bar{I})=0.2$. Gesucht $P(G)$.",
            "en": r"Interview $P(I)=0.1$. Good grade $G$. $P(G|I)=0.9$, $P(G|\bar{I})=0.2$. Find $P(G)$."
        },
        "options": [r"18%", r"25%", r"27%", r"50%"],
        "correct_idx": 2,
        "solution": {
            "de": r"**Richtig: 27%**<br>Satz der totalen Wahrscheinlichkeit:<br>$P(G) = P(G|I)P(I) + P(G|\bar{I})P(\bar{I}) = 0.9 \cdot 0.1 + 0.2 \cdot 0.9 = 0.09 + 0.18 = 0.27$.",
            "en": r"**Correct: 27%**<br>Law of Total Probability:<br>$P(G) = P(G|I)P(I) + P(G|\bar{I})P(\bar{I}) = 0.9 \cdot 0.1 + 0.2 \cdot 0.9 = 0.09 + 0.18 = 0.27$."
        }
    },
    # Include 1.8 questions if needed, but defining specific ones here
    "uebung1_prob6": QUESTIONS_1_8["uebung1_prob6"], # Reference to existing if reused
    "three_prisoners": {
        "source": "Logic Check: 3 Prisoners",
        "question": {
            "de": r"Drei Gefangene ($A, B, C$). Einer wird begnadigt. Wärter nennt $B$ als Todeskandidat. Steigt $A$s Chance?",
            "en": r"Three prisoners ($A, B, C$). One is pardoned. Warden names $B$ as executed. Does $A$'s chance increase?"
        },
        "options": [
            {"de": r"Ja, auf $50\%$", "en": r"Yes, to $50\%$"},
            {"de": r"Nein, bleibt $1/3$", "en": r"No, stays $1/3$"},
            {"de": r"Ja, auf $66\%$", "en": r"Yes, to $66\%$"},
            {"de": "Nein, sinkt", "en": "No, decreases"}
        ],
        "correct_idx": 1,
        "solution": {
            "de": r"**Antwort: Nein, bleibt $1/3$**<br>Der Wärter musste einen Namen nennen. Dass er $B$ nennt, gibt $A$ keine spezifische Information über sich selbst. Die 'überschüssige' Wahrscheinlichkeit wandert zu $C$ ($2/3$).",
            "en": r"**Answer: No, stays $1/3$**<br>The warden had to name someone. Naming $B$ gives $A$ no specific information about himself. The 'surplus' probability shifts to $C$ ($2/3$)."
        }
    },
    "hs2022_mc2": {
        "source": "HS 2022 Januar, MC #2",
        "type": "mc",
        "question": {
            "de": r"Sie haben $1000$ Münzen und wissen, dass es unter den $1000$ Münzen genau eine besondere Münze gibt, die auf beiden Seiten Zahl hat. Sie wählen eine Münze zufällig aus diesen $1000$ aus. Sie werfen diese eine Münze $10$ Mal. Sie zeigt $10$ Mal hintereinander Zahl an. Wie hoch ist die Wahrscheinlichkeit, dass Sie die besondere Münze genommen haben?",
            "en": r"You have $1000$ coins and know that among them there is exactly one special coin with tails on both sides. You randomly pick one coin and flip it $10$ times. It shows tails $10$ times in a row. What is the probability that you picked the special coin?"
        },
        "options": [r"$50.6\%$", r"$99.9\%$", r"$0.1\%$", r"$25\%$"],
        "correct_idx": 0,
        "solution": {
            "de": r"**Richtig: $50.6\%$**<br>Bayes' Theorem:<br>$P(\text{special}|10T) = \frac{1 \cdot \frac{1}{1000}}{1 \cdot \frac{1}{1000} + (\frac{1}{2})^{10} \cdot \frac{999}{1000}} \approx 0.506$",
            "en": r"**Correct: $50.6\%$**<br>Bayes' Theorem:<br>$P(\text{special}|10T) = \frac{1 \cdot \frac{1}{1000}}{1 \cdot \frac{1}{1000} + (\frac{1}{2})^{10} \cdot \frac{999}{1000}} \approx 0.506$"
        }
    }
}

# 1.10 Final Exam (The Gauntlet)
QUESTIONS_1_10 = {
    "l1": {
        "source": "Level 1: Coin Flip (Intro)",
        "question": {
            "de": "Eine faire Münze wird 3 Mal geworfen. Wie groß ist die Wahrscheinlichkeit, dass genau 2 Mal Kopf fällt?",
            "en": "A fair coin is tossed 3 times. What is the probability of getting exactly 2 heads?"
        },
        "options": [r"$\frac{1}{8}$", r"$\frac{3}{8}$", r"$\frac{1}{2}$", r"$\frac{2}{3}$"],
        "correct_idx": 1,
        "solution": {
            "de": r"**Richtig: $\frac{3}{8}$**<br>Möglichkeiten: (K,K,Z), (K,Z,K), (Z,K,K). Total 8 Pfade.",
            "en": r"**Correct: $\frac{3}{8}$**<br>Possibilities: (H,H,T), (H,T,H), (T,H,H). Total 8 paths."
        }
    },
    "l2": {
        "source": "Level 2: Days of the Week (Laplace)",
        "question": {
            "de": "Wie hoch ist die Wahrscheinlichkeit, an einem Wochenende (Sa oder So) geboren zu sein?",
            "en": "What is the probability of being born on a weekend (Sat or Sun)?"
        },
        "options": [r"$\frac{1}{7}$", r"$\frac{2}{7}$", r"$\frac{5}{7}$", r"$\frac{1}{14}$"],
        "correct_idx": 1,
        "solution": {
            "de": r"**Richtig: $\frac{2}{7}$**<br>Günstige Ereignisse: 2 (Sa, So). Mögliche Ereignisse: 7. Annahme: Alle Tage gleich wahrscheinlich (Laplace).",
            "en": r"**Correct: $\frac{2}{7}$**<br>Favorable events: 2 (Sat, Sun). Possible events: 7. Assumption: All days equally likely (Laplace)."
        }
    },
    "l3": {
        "source": "Level 3: The Password (Combinatorics)",
        "question": {
            "de": "Ein 4-stelliger PIN-Code besteht aus den Ziffern 0-9. Wie viele Möglichkeiten gibt es?",
            "en": "A 4-digit PIN code consists of the digits 0-9. How many possibilities are there?"
        },
        "options": [r"$3024 \; (10 \times 9 \times 8 \times 7)$", r"$10'000 \; (10^4)$", r"$40 \; (10 \times 4)$", r"$5040 \; (7!)$"],
        "correct_idx": 1,
        "solution": {
            "de": r"**Richtig: $10'000$**<br>Variation mit Wiederholung: $10^4$.",
            "en": r"**Correct: $10'000$**<br>Variation with repetition: $10^4$."
        }
    },
    "l4": {
        "source": "Level 4: Rare Disease (Bayes)",
        "question": {
            "de": r"Krankheit ($1\%$ Prävalenz). Test ($99\%$ genau). Du testest positiv. Wie groß ist die Wahrscheinlichkeit, dass du wirklich krank bist?",
            "en": r"Disease ($1\%$ prevalence). Test ($99\%$ accurate). You test positive. What is the probability you are actually sick?"
        },
        "options": [r"$99\%$", r"$50\%$", r"$1\%$", r"$90\%$"],
        "correct_idx": 1,
        "solution": {
            "de": r"**Richtig: $50\%$**<br>Klassische Bayes-Falle. Bei seltenen Krankheiten gibt es viele Falsch-Positive.",
            "en": r"**Correct: $50\%$**<br>Classic Bayes Trap. Rare diseases produce many false positives."
        }
    },
    "l5": {
        "source": "Level 5: Roulette (Exp Value)",
        "question": {
            "de": r"Du setzt $10$ CHF auf Rot ($18$ rote, $18$ schwarze, $1$ grüne Zahl). Gewinn: Verdoppelung. Was ist dein erwarteter Gewinn pro Spiel?",
            "en": r"You bet $10$ CHF on Red ($18$ red, $18$ black, $1$ green number). Win: Double up. What is your expected gain per game?"
        },
        "options": [r"$0$ CHF", r"$-0.27$ CHF", r"$+0.50$ CHF", r"$-10$ CHF"],
        "correct_idx": 1,
        "solution": {
            "de": r"**Richtig: $-0.27$ CHF**<br>$E[X] = \frac{18}{37} \cdot 10 + \frac{19}{37} \cdot (-10) = -\frac{10}{37} \approx -0.27$.",
            "en": r"**Correct: $-0.27$ CHF**<br>$E[X] = \frac{18}{37} \cdot 10 + \frac{19}{37} \cdot (-10) = -\frac{10}{37} \approx -0.27$."
        }
    },
    "l6": {
        "source": "Level 6: Waiting Time (Continuous)",
        "question": {
            "de": r"Der Bus kommt alle $10$ Minuten (gleichverteilt). Du kommst 'zufällig' an. Wie lange wartest du im Durchschnitt?",
            "en": r"The bus comes every $10$ minutes (uniformly distributed). You arrive 'randomly'. How long do you wait on average?"
        },
        "options": [r"$10$ min", r"$1$ min", r"$5$ min", r"$0$ min"],
        "correct_idx": 2,
        "solution": {
            "de": r"**Richtig: $5$ min**<br>Erwartungswert einer stetigen Gleichverteilung $[0, 10]$: $\frac{a+b}{2} = 5$.",
            "en": r"**Correct: $5$ min**<br>Expected value of continuous uniform distribution $[0, 10]$: $\frac{a+b}{2} = 5$."
        }
    }
}

# 2.1 Binomialkoeffizient
QUESTIONS_2_1 = {
    "q_2_1_scenario_mastery": {
        "source": "Konzept-Check 2.1",
        "question": {
            "de": "Warum teilen wir beim Binomialkoeffizienten durch k!?",
            "en": "Why do we divide by k! in the Binomial Coefficient?"
        },
        "options": [
            {"de": "Um die Permutationen (Reihenfolgen) innerhalb einer Gruppe zu löschen", "en": "To delete the permutations (orders) within a group"},
            {"de": "Weil n! immer zu groß ist", "en": "Because n! is always too large"}
        ],
        "correct_idx": 0,
        "solution": {
            "de": "**Richtig!** Wir entfernen die Mehrfachzählungen ('Ghosts'), die entstehen, wenn wir die Reihenfolge ignorieren.",
            "en": "**Correct!** We remove the multiple countings ('Ghosts') that arise when we ignore the order."
        }
    }
}

# 2.2 Fundamentalprinzip & 2.3/2.4 Kombinatorik
QUESTIONS_2_2 = {
    "q_2_2_club": {
        "source": "Test 2, Frage 1 (Variation)",
        "question": {
            "de": r"In einem Verein mit $10$ Mitgliedern ($4$ Frauen und $6$ Herren) soll nun ein Vorstand bestehend aus zwei Damen und zwei Herren gebildet werden. Wie viele Möglichkeiten gibt es?",
            "en": r"In a club with $10$ members ($4$ women and $6$ men), a board consisting of two women and two men is to be formed. How many possibilities are there?"
        },
        "options": [r"$90$", r"$25$", r"$210$", r"$60$"],
        "correct_idx": 0,
        "solution": {
            "de": r"**Richtig! ($90$)**<br>Frauen: $\binom{4}{2} = 6$. Männer: $\binom{6}{2} = 15$. Fundamentalprinzip: $6 \cdot 15 = 90$.",
            "en": r"**Correct! ($90$)**<br>Women: $\binom{4}{2} = 6$. Men: $\binom{6}{2} = 15$. Principle: $6 \cdot 15 = 90$."
        }
    }
}
QUESTIONS_2_3 = {
    "dvd_collection": {
        "source": "Statistik I, Aufgabe 3",
        "question": {
            "de": r"Sie besitzen **50 verschiedene DVDs** und die dazugehörigen 50 Hüllen. Auf wie viele Arten können die DVDs in die Hüllen einsortiert werden?",
            "en": r"You own **50 different DVDs** and their 50 cases. In how many ways can the DVDs be sorted into the cases?"
        },
        "options": [r"$50!$", r"$50^{50}$", r"$1$", r"$\text{Binom}(50, 50)$"],
        "correct_idx": 0,
        "solution": {
            "de": r"**Richtig: $50!$**<br>Permutation ohne Wiederholung.",
            "en": r"**Correct: $50!$**<br>Permutation without replacement."
        }
    },
    "test1_q3": {
        "source": "Test 1, Frage 3",
        "question": {
            "de": r"Sie besitzen $50$ verschiedene DVDs und $50$ Hüllen. Ihr Neffe verteilt die DVDs zufällig. Wie viele Arten der Verteilung gibt es?",
            "en": r"You have $50$ different DVDs and $50$ cases. Your nephew distributes them randomly. How many arrangements are possible?"
        },
        "options": [r"$50!$", r"$(50!)^2$", r"$50! \cdot 49!$", r"$\binom{100}{2}$"],
        "correct_idx": 0,
        "solution": {
            "de": r"**Richtig: $50!$**<br>Jede DVD kommt in genau eine Hülle. Das ist eine Permutation von $50$ Elementen.",
            "en": r"**Correct: $50!$**<br>Each DVD goes into exactly one case. This is a permutation of $50$ elements."
        }
    },
    "hs2015_mc4": {
        "source": "HS 2015 Januar, MC #4 (4 Punkte)",
        "type": "mc",
        "question": {
            "de": r"Herr Meyer hat seinen Schlüssel für das Schliessfach verloren. Die Schliessfachnummer hat er leider vergessen. Er erinnert sich allerdings daran, dass es sich um eine vierstellige Zahl handelt, bei der zwei Ziffern gleich sind und dass als Ziffern die 3, 5 und 7 vorkommen. Wieviele Schliessfächer erfüllen diese Kriterien?",
            "en": r"Mr. Meyer has lost his locker key. Unfortunately, he has forgotten the locker number. However, he remembers that it is a four-digit number where two digits are the same and that the digits 3, 5, and 7 appear. How many lockers meet these criteria?"
        },
        "options": ["12", "24", "36", "72"],
        "correct_idx": 2,
        "solution": {
            "de": r"**Richtig: 36**<br>Ziffern: $\{3, 5, 7\}$. Eine Ziffer muss doppelt vorkommen. <br>1. Wahl der doppelten Ziffer: $\binom{3}{1} = 3$ Möglichkeiten.<br>2. Anordnung von 4 Ziffern (z.B. 3,3,5,7): $\frac{4!}{2!1!1!} = \frac{24}{2} = 12$.<br>Total: $3 \cdot 12 = 36$.",
            "en": r"**Correct: 36**<br>Digits: $\{3, 5, 7\}$. One digit must appear twice. <br>1. Choose the doubled digit: $\binom{3}{1} = 3$ options.<br>2. Arrange 4 digits (e.g., 3,3,5,7): $\frac{4!}{2!1!1!} = \frac{24}{2} = 12$.<br>Total: $3 \cdot 12 = 36$."
        }
    }
}

QUESTIONS_2_4 = {
    "lottery": {
        "source": "Kombinatorik Grundlagen",
        "question": {
            "de": "Beim Schweizer Lotto '6 aus 49' wählt man 6 Zahlen aus 49. Wie viele verschiedene Tipps sind möglich?",
            "en": "In Swiss Lotto '6 out of 49', you pick 6 numbers from 49. How many different tickets are possible?"
        },
        "options": [
            {"de": r"$49!$", "en": r"$49!$"},
            {"de": r"$\binom{49}{6}$", "en": r"$\binom{49}{6}$"},
            {"de": r"$49^6$", "en": r"$49^6$"},
            {"de": r"$P(49,6)$", "en": r"$P(49,6)$"}
        ],
        "correct_idx": 1,
        "solution": {
            "de": r"**Richtig: $\binom{49}{6}$**<br>Reihenfolge egal, ohne Zurücklegen.",
            "en": r"**Correct: $\binom{49}{6}$**<br>Order doesn't matter, without replacement."
        }
    },
    "test2_q1": {
        "source": "Test 2, Frage 1",
        "question": {
            "de": r"Verein mit $10$ Mitgliedern ($4$ Frauen, $6$ Männer). Vorstand ($2$ Frauen, $2$ Männer) soll gebildet werden. Wie viele Möglichkeiten?",
            "en": r"Club with $10$ members ($4$ women, $6$ men). Board ($2$ women, $2$ men) to be formed. How many possibilities?"
        },
        "options": [r"$89$", r"$210$", r"$90$", r"$75$"],
        "correct_idx": 2,
        "solution": {
            "de": r"**Richtig: $90$**<br>$\binom{4}{2} \cdot \binom{6}{2} = 6 \cdot 15 = 90$.",
            "en": r"**Correct: $90$**<br>$\binom{4}{2} \cdot \binom{6}{2} = 6 \cdot 15 = 90$."
        }
    }
}

QUESTIONS_2_5 = {
    "coin_toss_seq": {
        "source": "Kombinatorik",
        "question": {
            "de": r"Eine Münze wird $4$ Mal geworfen. Wie viele Ergebnisfolgen?",
            "en": r"A coin is tossed $4$ times. How many outcome sequences?"
        },
        "options": [r"$24$", r"$16$", r"$6$", r"$8$"],
        "correct_idx": 1,
        "solution": {
            "de": r"**Richtig: $16$** $(2^4)$",
            "en": r"**Correct: $16$** $(2^4)$"
        }
    }
}

QUESTIONS_2_6 = {
    "test1_mc3": {
        "source": "Test 1, Q3",
        "type": "mc",
        "question": {
            "de": r"50 DVDs und 50 Hüllen. Zufällige Verteilung. Wie viele Möglichkeiten?",
            "en": r"50 DVDs, 50 cases. Random arrangement. How many possibilities?"
        },
        "options": [r"$50!$", r"$(50!)^2$", r"$50! \cdot 49!$", r"$100$"],
        "correct_idx": 0,
        "solution": {
            "de": r"**Richtig: $50!$**<br>Permutation von 50 unterschiedlichen Objekten.",
            "en": r"**Correct: $50!$**<br>Permutation of 50 distinct objects."
        }
    },
    "test2_mc1": {
        "source": "Test 2, Q1",
        "type": "mc",
        "question": {
            "de": r"10 Mitglieder (4F, 6M). Vorstand: 2 Damen, 2 Herren. Anzahl Möglichkeiten?",
            "en": r"10 members (4F, 6M). Board: 2F, 2M. Combinations?"
        },
        "options": [r"89", r"210", r"90", r"75"],
        "correct_idx": 2,
        "solution": {
            "de": r"**Richtig: 90**<br>$\binom{4}{2} \cdot \binom{6}{2} = 6 \cdot 15 = 90$.",
            "en": r"**Correct: 90**<br>$\binom{4}{2} \cdot \binom{6}{2} = 6 \cdot 15 = 90$."
        }
    }
}

# =============================================================================
# PART II: ZUFALLSVARIABLEN (Random Variables)
# =============================================================================

# 3.1 Verteilungsfunktion
QUESTIONS_3_1 = {
    "uebung2_mc6": {
        "source": "Übung 2, MC6",
        "question": {
            "de": r"Eine Funktion $f(x) \ge 0$ ist eine Dichtefunktion, wenn:",
            "en": r"A function $f(x) \ge 0$ is a density function if:"
        },
        "options": [
            {"de": r"$\sum f(x_i) = 1$", "en": r"$\sum f(x_i) = 1$"},
            {"de": r"$\int_{-\infty}^{+\infty} f(x) \, dx = 1$", "en": r"$\int_{-\infty}^{+\infty} f(x) \, dx = 1$"},
            {"de": r"$F(-\infty)=1$", "en": r"$F(-\infty)=1$"},
            {"de": r"$F(-\infty)=0$ und $F(+\infty)=1$", "en": r"$F(-\infty)=0$ and $F(+\infty)=1$"}
        ],
        "correct_idx": 1,
        "solution": {
            "de": r"**Richtig: (b) und (d)** (Hier als MC: $\int f(x)dx = 1$).",
            "en": r"**Correct: (b) and (d)** (Shown as MC: $\int f(x)dx = 1$)."
        }
    },
    "uebung2_prob2": {
        "source": "Übung 2, Problem 2",
        "type": "problem",
        "question": {
            "de": r"Dreiecksverteilung: $f(x) = 2ax$ für $0<x<1$, $f(x) = 3a-ax$ für $1 \le x < 3$.<br>Bestimmen Sie $a$.",
            "en": r"Triangle distribution: $f(x) = 2ax$ for $0<x<1$, $f(x) = 3a-ax$ for $1 \le x < 3$.<br>Determine $a$."
        },
        "solution": {
            "de": r"**Lösung: $a = \frac{1}{3}$**<br>Fläche unter dem Dreieck muss 1 sein.",
            "en": r"**Solution: $a = \frac{1}{3}$**<br>Area under the triangle must be 1."
        }
    },
    "hs2015_mc2": {
        "source": "HS 2015 Januar, MC #2 (4 Punkte)",
        "question": {
            "de": r"Sei $X$ eine stetige Zufallsvariable mit kumulativer Verteilungsfunktion $F(x)$. Welche der folgenden Aussagen ist **FALSCH**?",
            "en": r"Let $X$ be a continuous random variable with cumulative distribution function $F(x)$. Which of the following statements is **FALSE**?"
        },
        "options": [
            {"de": r"$P(a \le X \le b) = \int_a^b F(x)\,dx$", "en": r"$P(a \le X \le b) = \int_a^b F(x)\,dx$"},
            {"de": r"Wenn $X$ normalverteilt ist, dann gilt $E[X] = \text{Median}(X)$", "en": r"If $X$ is normally distributed, then $E[X] = \text{Median}(X)$"},
            {"de": r"Wenn $X$ uniform verteilt ist auf $[0, 1]$, dann ist $F(x)$ linear für $x \in [0, 1]$", "en": r"If $X$ is uniformly distributed on $[0, 1]$, then $F(x)$ is linear for $x \in [0, 1]$"},
            {"de": r"Wenn $X$ uniform verteilt ist, dann gilt $E[X] = \text{Median}(X)$", "en": r"If $X$ is uniformly distributed, then $E[X] = \text{Median}(X)$"}
        ],
        "correct_idx": 0,
        "solution": {
            "de": r"**Richtig: (a) ist FALSCH**<br>Die korrekte Formel lautet $P(a \le X \le b) = \int_a^b f(x)\,dx$ (mit der **Dichte** $f(x)$, nicht der Verteilungsfunktion $F(x)$).<br>Alternativ: $P(a \le X \le b) = F(b) - F(a)$.",
            "en": r"**Correct: (a) is FALSE**<br>The correct formula is $P(a \le X \le b) = \int_a^b f(x)\,dx$ (with the **density** $f(x)$, not the distribution function $F(x)$).<br>Alternatively: $P(a \le X \le b) = F(b) - F(a)$."
        }
    }
}

# 3.2 Diskrete Zufallsvariablen
QUESTIONS_3_2 = {
    "uebung2_mc5": {
        "source": "Übung 2, MC5",
        "question": {
            "de": r"$X$ sei diskret. $P[1 \le X < 2]$ ist dann:",
            "en": r"Let $X$ be discrete. $P[1 \le X < 2]$ is then:"
        },
        "options": [
            {"de": r"$F(2) - F(1)$", "en": r"$F(2) - F(1)$"},
            {"de": r"$F(2) - F(1) - P[X=2] + P[X=1]$", "en": r"$F(2) - F(1) - P[X=2] + P[X=1]$"},
            {"de": r"$F(2) - F(1) + P[X=1]$", "en": r"$F(2) - F(1) + P[X=1]$"}
        ],
        "correct_idx": 1,
        "solution": {
            "de": r"**Richtig:** $F(2) - F(1)$ schliesst $P(X=1)$ NICHT ein.<br>$P(1 \le X < 2) = F(2) - P[X=2] - F(1) + P[X=1]$",
            "en": r"**Correct:** $F(2) - F(1)$ excludes $P(X=1)$.<br>$P(1 \le X < 2) = F(2) - P[X=2] - F(1) + P[X=1]$"
        }
    },
    "test2_q4": {
        "source": "Test 2, Frage 4",
        "question": {
            "de": r"$X$ diskret. PMF $f(x) = \frac{x+4}{c}$ für $x=1,\dots,5$. Für welches $c$ ist $f(x)$ eine PMF?",
            "en": r"$X$ discrete. PMF $f(x) = \frac{x+4}{c}$ for $x=1,\dots,5$. For which $c$ is $f(x)$ a PMF?"
        },
        "options": [r"$c = 20$", r"$c = 25$", r"$c = 30$", r"$c = 35$"],
        "correct_idx": 3,
        "solution": {
            "de": r"**Richtig: $c=35$**<br>$\sum_{x=1}^{5}(x+4) = 5+6+7+8+9 = 35$.<br>Damit $\sum P(x)=1$, muss $c=35$ sein.",
            "en": r"**Correct: $c=35$**<br>$\sum_{x=1}^{5}(x+4) = 5+6+7+8+9 = 35$.<br>For $\sum P(x)=1$, $c$ must be 35."
        }
    },
    "hs2015_mc5": {
        "source": "HS 2015, MC 5 (4 Punkte)",
        "type": "mc",
        "question": {
            "de": r"Es sei $X$ eine diskrete Zufallsvariable mit einer Wahrscheinlichkeitsmassenfunktion der Form $f(x) = \frac{x+4}{c}$ für $x = 1, \dots, 5$ (0 sonst). Für welchen Wert von $c$ ist $f(x)$ eine Wahrscheinlichkeitsmassenfunktion?",
            "en": r"Let $X$ be a discrete random variable with a probability mass function of the form $f(x) = \frac{x+4}{c}$ for $x = 1, \dots, 5$ (0 otherwise). For which value of $c$ is $f(x)$ a probability mass function?"
        },
        "options": ["c = 20", "c = 25", "c = 30", "c = 35"],
        "correct_idx": 3,
        "solution": {
            "de": r"**Richtig: c = 35**<br>Summe der Wahrscheinlichkeiten muss 1 sein: $\sum_{x=1}^5 \frac{x+4}{c} = 1$.<br>Zähler-Summe: $(1+4)+(2+4)+(3+4)+(4+4)+(5+4) = 5+6+7+8+9 = 35$.<br>Also $35/c = 1 \Rightarrow c=35$.",
            "en": r"**Correct: c = 35**<br>Sum of probabilities must match 1: $\sum_{x=1}^5 \frac{x+4}{c} = 1$.<br>Numerator sum: $(1+4)+(2+4)+(3+4)+(4+4)+(5+4) = 5+6+7+8+9 = 35$.<br>Thus $35/c = 1 \Rightarrow c=35$."
        }
    },
    "hs2023_mc4": {
        "source": "HS 2023 Januar, MC #4",
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
            "de": r"**Richtig: (b)**<br>$E[Y] = 2/3$. $E[Y^2] = 1/2$.<br>$Var(Y) = 1/2 - 4/9 = 1/18$.",
            "en": r"**Correct: (b)**<br>$E[Y] = 2/3$. $E[Y^2] = 1/2$.<br>$Var(Y) = 1/2 - 4/9 = 1/18$."
        }
    }
}

# 3.3 Stetige Zufallsvariablen
QUESTIONS_3_3 = {
    "test2_q3": {
        "source": "Test 2, Frage 3",
        "question": {
            "de": r"$X$ stetig auf $[0, 10]$ mit Dichte $f(x) = \frac{1}{20} + \frac{x}{100}$. Berechnen Sie $P(2 \le X \le 6)$.",
            "en": r"$X$ continuous on $[0, 10]$ with density $f(x) = \frac{1}{20} + \frac{x}{100}$. Calculate $P(2 \le X \le 6)$."
        },
        "options": [r"$\frac{9}{25} \; (0.36)$", r"$\frac{2}{50}$", r"$\frac{12}{25}$", r"$\frac{3}{50}$"],
        "correct_idx": 0,
        "solution": {
            "de": r"**Richtig: $\frac{9}{25}$**<br>$\int_2^6 f(x)dx = \left[\frac{x}{20} + \frac{x^2}{200}\right]_2^6 = 0.36 = \frac{9}{25}$.",
            "en": r"**Correct: $\frac{9}{25}$**<br>$\int_2^6 f(x)dx = \left[\frac{x}{20} + \frac{x^2}{200}\right]_2^6 = 0.36 = \frac{9}{25}$."
        }
    }
}

# 3.4 Erwartungswerte
QUESTIONS_3_4 = {
    "hs2024_mc7": {
        "source": "HS 2024 Januar, MC #7",
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
            "de": r"**Richtig: (b)**<br>Symmetrie-Argument: Die Dichte ist symmetrisch um $\pi/2$ im Intervall $[0, \pi]$. Daher ist der Erwartungswert die Mitte.",
            "en": r"**Correct: (b)**<br>Symmetry argument: The density is symmetric around $\pi/2$ in the interval $[0, \pi]$. Thus the expectation is the center."
        }
    },
    "hs2024_mc12": {
        "source": "HS 2024 Januar, MC #12",
        "type": "mc",
        "question": {
            "de": r"Brunnen 10L. Täglich Entnahme $U[0, 1]$. Durchschnittliche Tage bis leer?",
            "en": r"Well 10L. Daily removal $U[0, 1]$. Avg days until empty?"
        },
        "options": ["12.5", "15", "17.5", "20"],
        "correct_idx": 3,
        "solution": {
            "de": r"**Richtig: 20**<br>Durchschnittliche Entnahme pro Tag: $E[X] = 0.5$.<br>Waldsche Identität / Intuition: $n \cdot E[X] = 10 \Rightarrow n = 10/0.5 = 20$.",
            "en": r"**Correct: 20**<br>Average removal per day: $E[X] = 0.5$.<br>Wald's Identity / Intuition: $n \cdot E[X] = 10 \Rightarrow n = 10/0.5 = 20$."
        }
    },
    "hs2023_mc11": {
        "source": "HS 2023 Januar, MC #11",
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
            "de": r"**Richtig: (d)**<br>Rekursion: $E = 3.5 + 0.5 E$. $E=7$.",
            "en": r"**Correct: (d)**<br>Recursion: $E = 3.5 + 0.5 E$. $E=7$."
        }
    },
    "uebung2_prob5": {
        "source": "Übung 2, Problem 5",
        "type": "problem",
        "question": {
            "de": r"$X$ ist gleichförmig verteilt auf $[0, 3]$ (Dichte $1/3$).<br>a) $E[X]$<br>b) $E[4X + 2]$",
            "en": r"$X$ is uniformly distributed on $[0, 3]$ (density $1/3$).<br>a) $E[X]$<br>b) $E[4X + 2]$"
        },
        "solution": {
            "de": r"**Lösung:**<br>a) Mitte des Intervalls: $\mathbf{1.5}$<br>b) Linearität: $4 \cdot 1.5 + 2 = \mathbf{8}$",
            "en": r"**Solution:**<br>a) Midpoint of interval: $\mathbf{1.5}$<br>b) Linearity: $4 \cdot 1.5 + 2 = \mathbf{8}$"
        }
    },
    "uebung2_prob7": {
        "source": "Übung 2, Problem 7 (Xenia)",
        "type": "problem",
        "question": {
            "de": r"Lernzeit Xenia:<br>• Schön ($1/10$): $20$ min<br>• Bewölkt ($1/3$): $60$ min<br>• Regen ($1/2$): $80$ min<br>• Schnee ($1/15$): $120$ min<br>Berechnen Sie den Erwartungswert.",
            "en": r"Xenia's study time:<br>• Sunny ($1/10$): $20$ min<br>• Cloudy ($1/3$): $60$ min<br>• Rain ($1/2$): $80$ min<br>• Snow ($1/15$): $120$ min<br>Calculate the expected value."
        },
        "solution": {
            "de": r"**Lösung: $70$ Minuten**<br>$E[X] = 1/10 \cdot 20 + 1/3 \cdot 60 + 1/2 \cdot 80 + 1/15 \cdot 120 = 2 + 20 + 40 + 8 = 70$",
            "en": r"**Solution: $70$ minutes**<br>$E[X] = 1/10 \cdot 20 + 1/3 \cdot 60 + 1/2 \cdot 80 + 1/15 \cdot 120 = 2 + 20 + 40 + 8 = 70$"
        }
    },
    "hs2022_mc11": {
        "source": "HS 2022 Januar, MC #11",
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
            "de": r"**Richtig: (d)**<br>$E[X]E[Y] = 1$ und $E[X]=E[Y]$ führt zu $E[X]^2 = 1 \Rightarrow E[X] = \pm 1$.<br>Der Wert von $E[Z]$ hängt vom Vorzeichen ab ($1.5$ oder $0.5$).",
            "en": r"**Correct: (d)**<br>$E[X]E[Y] = 1$ and $E[X]=E[Y]$ implies $E[X]^2 = 1 \Rightarrow E[X] = \pm 1$.<br>The value of $E[Z]$ depends on the sign ($1.5$ or $0.5$)."
        }
    }
}

# 3.5 Varianz
QUESTIONS_3_5 = {
    "uebung2_mc8": {
        "source": "Übung 2, MC8",
        "question": {
            "de": r"Dichte $f(x) = \frac{1}{18}x$ im Intervall $[0, 6]$. Berechnen Sie $V(X)$.",
            "en": r"Density $f(x) = \frac{1}{18}x$ in interval $[0, 6]$. Calculate $V(X)$."
        },
        "options": [r"$V(X)=3$", r"$V(X)=18$", r"$V(X)=9$", r"$V(X)=2$"],
        "correct_idx": 3,
        "solution": {
            "de": r"**Lösung: $V(X) = 2$**",
            "en": r"**Solution: $V(X) = 2$**"
        }
    }
}

# 3.6 Standardisieren
QUESTIONS_3_6 = {
    "test3_q2": {
        "source": "Test 3, Frage 2",
        "question": {
            "de": r"$X$ normalverteilt mit $\mu$ und $\sigma > 0$. Für $Y = X/\sigma$ gilt $E[Y^2] = ...$",
            "en": r"$X$ normal distributed with $\mu$ and $\sigma > 0$. For $Y = X/\sigma$, $E[Y^2] = ...$"
        },
        "options": [r"$1$", r"$1 - \mu^2/\sigma^2$", r"$1 + \mu^2/\sigma^2$", r"$?$"],
        "correct_idx": 2,
        "solution": {
            "de": r"**Richtig: (c)**<br>$E[Y^2] = 1/\sigma^2 \cdot E[X^2]$.<br>$Var(X) = E[X^2] - \mu^2 = \sigma^2 \Rightarrow E[X^2] = \sigma^2 + \mu^2$.<br>Also $E[Y^2] = (\sigma^2+\mu^2)/\sigma^2 = 1 + \mu^2/\sigma^2$.",
            "en": r"**Correct: (c)**<br>$E[Y^2] = 1/\sigma^2 \cdot E[X^2]$.<br>$Var(X) = E[X^2] - \mu^2 = \sigma^2 \Rightarrow E[X^2] = \sigma^2 + \mu^2$.<br>So $E[Y^2] = (\sigma^2+\mu^2)/\sigma^2 = 1 + \mu^2/\sigma^2$."
        }
    }
}

# 3.7 Additional Questions (Random Variables)
QUESTIONS_3_7 = {
    "hs2023_mc6": {
        "source": "HS 2023 Januar, MC #6",
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
            "de": r"**Richtig: (c)**<br>Summe der Wahrscheinlichkeiten muss 1 sein. $\sum \frac{1}{x!} = e$ (Taylorreihe). Also $c = 1/e$.",
            "en": r"**Correct: (c)**<br>Sum of probabilities must be 1. $\sum \frac{1}{x!} = e$ (Taylor series). Thus $c = 1/e$."
        }
    },
    "uebung2_mc1": {
        "source": "Übung 2, MC #1",
        "type": "mc",
        "question": {
            "de": r"Diskret ist eine Zufallsvariable, wenn:",
            "en": r"A random variable is discrete if:"
        },
        "options": [
            r"sie nur abzählbar viele Werte annehmen kann.",
            r"sie überabzählbar viele Werte annehmen kann.",
            r"sie nur endlich viele Werte annehmen kann.",
            r"sie unendlich viele Werte annehmen kann."
        ],
        "correct_idx": 0,
        "solution": {
            "de": r"**Richtig: (a)**<br>Diskret = Abzählbar (endlich oder abzählbar unendlich). CDF ist Treppenfunktion.",
            "en": r"**Correct: (a)**<br>Discrete = Countable. CDF is a step function."
        }
    },
    "uebung2_mc2": {
        "source": "Übung 2, MC #2",
        "type": "mc",
        "question": {
            "de": r"Stetig ist eine Zufallsvariable, wenn:",
            "en": r"A random variable is continuous if:"
        },
        "options": [
            r"sie nur abzählbar viele Werte annehmen kann.",
            r"sie überabzählbar viele Werte annehmen kann.",
            r"sie nur endlich viele Werte annehmen kann.",
            r"sie unendlich viele Werte annehmen kann."
        ],
        "correct_idx": 1,
        "solution": {
            "de": r"**Richtig: (b)**<br>Stetig = Überabzählbar viele Werte (Intervalle).",
            "en": r"**Correct: (b)**<br>Continuous = Uncountably many values (intervals)."
        }
    },
    "uebung2_mc3": {
        "source": "Übung 2, MC #3",
        "type": "mc",
        "question": {
            "de": r"Der Erwartungswert einer Verteilung ist:",
            "en": r"The expectation of a distribution is:"
        },
        "options": [
            r"der Median (50% Punkt).",
            r"der Modus (dichtester Punkt).",
            r"der Schwerpunkt (Center of Gravity).",
            r"immer der wahrscheinlichste Wert."
        ],
        "correct_idx": 2,
        "solution": {
            "de": r"**Richtig: (c)**<br>E[X] entspricht physikalisch dem Schwerpunkt der Wahrscheinlichkeitsmasse.",
            "en": r"**Correct: (c)**<br>E[X] corresponds physically to the center of gravity."
        }
    },
    "uebung2_mc4": {
        "source": "Übung 2, MC #4",
        "type": "mc",
        "question": {
            "de": r"Die Varianz einer diskreten Zufallsvariablen X ist:",
            "en": r"The variance of a discrete random variable X is:"
        },
        "options": [
            r"$\sum (x_i f(x_i) - E[X])^2$",
            r"ein Mass für die Streuung um den Erwartungswert.",
            r"die quadrierte Standardabweichung.",
            r"Alle obigen sind falsch."
        ],
        "correct_idx": 1,
        "solution": {
            "de": r"**Richtig: (b)**<br>Varianz misst die Streuung. (c) wäre auch richtig, (a) ist Formel-Salat (fresch geklammert).",
            "en": r"**Correct: (b)**<br>Variance measures dispersion."
        }
    },
    "uebung2_mc7": {
        "source": "Übung 2, MC #7",
        "type": "mc",
        "question": {
            "de": r"$f(x) = \frac{1}{2}x^2 - b$ für $1 \le x \le 2$, sonst 0. Für welches $b$ ist dies eine Dichte?",
            "en": r"$f(x) = \frac{1}{2}x^2 - b$ on $[1, 2]$. Find $b$."
        },
        "options": [
            r"$b=1/2$",
            r"$b=1/3$",
            r"$b=1/6$",
            r"$b=1$"
        ],
        "correct_idx": 2,
        "solution": {
            "de": r"**Richtig: (c)**<br>Integral muss 1 sein. $\int_1^2 (\frac{1}{2}x^2 - b) dx = [\frac{x^3}{6} - bx]_1^2 = (\frac{8}{6}-2b) - (\frac{1}{6}-b) = \frac{7}{6}-b = 1 \implies b=1/6$.",
            "en": r"**Correct: (c)**<br>Integral must be 1. Result $b=1/6$."
        }
    },
    "test2_mc2": {
        "source": "Test 2, Q2",
        "type": "mc",
        "question": {
            "de": r"$X \sim U[-4, 4]$. $P(X^2 \le 9)$?",
            "en": r"$X \sim U[-4, 4]$. $P(X^2 \le 9)$?"
        },
        "options": [r"7/9", r"4/9", r"2/3", r"3/4"],
        "correct_idx": 3,
        "solution": {
            "de": r"**Richtig: 3/4**<br>$[-3, 3]$ hat Länge 6. Intervall $[-4, 4]$ hat Länge 8. $6/8 = 3/4$.",
            "en": r"**Correct: 3/4**<br>$[-3, 3]$ length 6. Interval $[-4, 4]$ length 8. $6/8 = 3/4$."
        }
    },
    "test2_mc3": {
        "source": "Test 2, Q3",
        "type": "mc",
        "question": {
            "de": r"$X$ auf $[0, 10]$ mit Dichte $f(x) = \frac{x}{100} + \frac{1}{20}$. $P(2 \le X \le 6)$?",
            "en": r"$X$ on $[0, 10]$ with pdf $f(x) = x/100 + 1/20$. $P(2 \le X \le 6)$?"
        },
        "options": [r"9/25", r"2/50", r"1/12", r"3/50"],
        "correct_idx": 0,
        "solution": {
            "de": r"**Richtig: 9/25**<br>Integral von 2 bis 6 über $f(x)$ ergibt $0.36 = 36/100 = 9/25$.",
            "en": r"**Correct: 9/25**<br>Integral from 2 to 6 of $f(x)$ yields $0.36 = 36/100 = 9/25$."
        }
    },
    "test2_mc4": {
        "source": "Test 2, Q4",
        "type": "mc",
        "question": {
            "de": r"Diskrete ZV $f(x) = \frac{x+4}{c}$ für $x=1,..,5$. Bestimme c.",
            "en": r"Discrete RV $f(x) = (x+4)/c$ for $x=1..5$. Find c."
        },
        "options": [r"20", r"25", r"30", r"35"],
        "correct_idx": 3,
        "solution": {
            "de": r"**Richtig: 35**<br>Summe der Zähler: $5+6+7+8+9 = 35$. Damit Summe 1 ist, muss $c=35$.",
            "en": r"**Correct: 35**<br>Sum of numerators: $5+6+7+8+9 = 35$. For sum to be 1, $c=35$."
        }
    },
    "test3_mc2": {
        "source": "Test 3, Q2",
        "type": "mc",
        "question": {
            "de": r"$Y = X/\sigma$. $E(Y^2)$?",
            "en": r"$Y = X/\sigma$. $E(Y^2)$?"
        },
        "options": [r"1", r"$1 - \mu^2/\sigma^2$", r"$1 + \mu^2/\sigma^2$", r"N/A"],
        "correct_idx": 2,
        "solution": {
            "de": r"**Richtig: (c)**<br>$E[Y^2] = Var(Y) + E[Y]^2 = 1/\sigma^2 \cdot Var(X) + (\mu/\sigma)^2 = 1 + \mu^2/\sigma^2$.",
            "en": r"**Correct: (c)**<br>$E[Y^2] = Var(Y) + E[Y]^2 = 1/\sigma^2 \cdot Var(X) + (\mu/\sigma)^2 = 1 + \mu^2/\sigma^2$."
        }
    }
}


# =============================================================================
# PART III: VERTEILUNGEN (Distributions)
# =============================================================================

# 4.2 Bernoulli
QUESTIONS_4_2 = {
    "uebung2_bb_prob1": {
        "source": "Übung 2, Problem 1 (Basketball)",
        "type": "problem",
        "question": {
            "de": r"Basketball: Trefferquote $p = 1/2$. Vier Würfe.<br>Berechnen Sie $E[X]$ und $V(X)$.",
            "en": r"Basketball: Hit rate $p = 1/2$. Four shots.<br>Calculate $E[X]$ and $V(X)$."
        },
        "solution": {
            "de": r"**Lösung:**<br>Binomialverteilung $n=4, p=0.5$.<br>$E[X] = n \cdot p = 2$<br>$V(X) = n \cdot p \cdot (1-p) = 4 \cdot 0.25 = 1$",
            "en": r"**Solution:**<br>Binomial distribution $n=4, p=0.5$.<br>$E[X] = n \cdot p = 2$<br>$V(X) = n \cdot p \cdot (1-p) = 4 \cdot 0.25 = 1$"
        }
    }
}

# 4.3 Binomial
QUESTIONS_4_3 = {
    "uebung2_giro": {
        "source": "Übung 2, MC11",
        "question": {
            "de": r"Miguel gewinnt Giro d'Italia mit $30\%$. Wahrscheinlichkeit bei $5$ Teilnahmen mind. $2$ mal zu gewinnen?",
            "en": r"Miguel wins Giro d'Italia with $30\%$. Probability to win at least $2$ times in $5$ participations?"
        },
        "options": [r"$0.639$", r"$0.472$", r"$0.600$", r"$0.360$"],
        "correct_idx": 1,
        "solution": {
            "de": r"**Richtig: $0.47178$**<br>$1 - P(X=0) - P(X=1)$",
            "en": r"**Correct: $0.47178$**<br>$1 - P(X=0) - P(X=1)$"
        }
    },
    "uebung2_insur": {
        "source": "Übung 2, Problem 2 (Versicherung)",
        "type": "problem",
        "question": {
            "de": r"Herr Kaiser verkauft bei $20\%$ ($2$ von $10$) eine Versicherung. Er macht $16$ Besuche pro Tag.<br>Berechnen Sie $E[X]$ und $Var(X)$.",
            "en": r"Mr. Kaiser sells insurance in $20\%$ ($2$ of $10$) of visits. He makes $16$ visits per day.<br>Calculate $E[X]$ and $Var(X)$."
        },
        "solution": {
            "de": r"**Lösung:**<br>$E[X] = 16 \cdot 0.2 = \mathbf{3.2}$<br>$Var(X) = 16 \cdot 0.2 \cdot 0.8 = \mathbf{2.56}$",
            "en": r"**Solution:**<br>$E[X] = 16 \cdot 0.2 = \mathbf{3.2}$<br>$Var(X) = 16 \cdot 0.2 \cdot 0.8 = \mathbf{2.56}$"
        }
    },
    "hs2022_mc7": {
        "source": "HS 2022 Januar, MC #7",
        "question": {
            "de": r"Im Oktober macht Nina einen einwöchigen Städtetrip nach Hamburg. Die Wettervorhersage sagt für jeden Tag eine Regenwahrscheinlichkeit von $70\%$ voraus. Wie hoch ist in etwa die Wahrscheinlichkeit, dass es an mindestens $5$ von $7$ Tagen regnet?",
            "en": r"In October, Nina takes a one-week city trip to Hamburg. The weather forecast predicts $70\%$ rain probability each day. What is approximately the probability it rains at least $5$ of $7$ days?"
        },
        "options": [r"$65\%$", r"$35\%$", r"$50\%$", r"$80\%$"],
        "correct_idx": 0,
        "solution": {
            "de": r"**Richtig: $65\%$**<br>$X \sim \text{Bin}(7, 0.7)$.<br>$P(X \ge 5) = P(X=5) + P(X=6) + P(X=7) \approx 0.65$",
            "en": r"**Correct: $65\%$**<br>$X \sim \text{Bin}(7, 0.7)$.<br>$P(X \ge 5) = P(X=5) + P(X=6) + P(X=7) \approx 0.65$"
        }
    },
    "hs2023_mc12": {
        "source": "HS 2023 Januar, MC #12",
        "question": {
            "de": r"Jacob geht ins Casino mit $100$ Spielautomaten. Gewinnwahrscheinlichkeit $20\%$. Er spielt $5$ Spiele pro Automat. Wie groß ist die Wahrscheinlichkeit, an mindestens $4$ der $100$ Automaten mehr als zweimal zu gewinnen?",
            "en": r"Jacob goes to a casino with $100$ slot machines. Win probability $20\%$. He plays $5$ games per machine. What is the probability of winning more than twice at at least $4$ of the $100$ machines?"
        },
        "options": [r"$0.2513$", r"$0.8372$", r"$0.5000$", r"$0.9500$"],
        "correct_idx": 1,
        "solution": {
            "de": r"**Richtig: $0.8372$**<br>Zweistufig:<br>1) $P(X>2)$ für $\text{Bin}(5, 0.2) \approx 0.058$.<br>2) $Y \sim \text{Bin}(100, 0.058)$. $P(Y \ge 4) \approx 0.837$.",
            "en": r"**Correct: $0.8372$**<br>Two-stage:<br>1) $P(X>2)$ for $\text{Bin}(5, 0.2) \approx 0.058$.<br>2) $Y \sim \text{Bin}(100, 0.058)$. $P(Y \ge 4) \approx 0.837$."
        }
    }
}

# 4.4 Poisson
QUESTIONS_4_4 = {
    "uebung2_typo": {
        "source": "Übung 2, Problem 3 (Druckfehler)",
        "type": "problem",
        "question": {
            "de": r"Buch hat im Mittel $\mu = 8$ Druckfehler (Poisson).<br>a) $P(X \ge 6)$?<br>b) $P(X = 13)$?",
            "en": r"Book has on average $\mu = 8$ typos (Poisson).<br>a) $P(X \ge 6)$?<br>b) $P(X = 13)$?"
        },
        "solution": {
            "de": r"**Lösung:**<br>a) $1 - P(X \le 5) \approx \mathbf{0.8088}$<br>b) $(8^{13} \cdot e^{-8}) / 13! \approx \mathbf{0.0296}$",
            "en": r"**Solution:**<br>a) $1 - P(X \le 5) \approx \mathbf{0.8088}$<br>b) $(8^{13} \cdot e^{-8}) / 13! \approx \mathbf{0.0296}$"
        }
    },
    "test4_q1": {
        "source": "Test 4, Frage 1",
        "question": {
            "de": r"Sei $X \sim \text{Poisson}(10)$ und $Z = 2X$. Welche Aussage trifft NICHT zu?",
            "en": r"Let $X \sim \text{Poisson}(10)$ and $Z = 2X$. Which statement is FALSE?"
        },
        "options": [r"$Z \sim \text{Poisson}(20)$", r"$\text{Var}(Z) = 40$", r"$\text{Corr}(X, Z) = 1$", r"$E[Z] = 20$"],
        "correct_idx": 0,
        "solution": {
            "de": r"**Richtig: (a)** (Die falsche Aussage).<br>$Z$ nimmt nur gerade Werte an (0, 2, 4...), eine Poisson-Variable muss alle ganzen Zahlen annehmen können. Transformation ändert Verteilungstyp.",
            "en": r"**Correct: (a)** (The false statement).<br>$Z$ only takes even values (0, 2, 4...), a Poisson variable must be able to take all integers. Transformation changes distribution type."
        }
    }
}

# 4.5 Rechteckverteilung (Stetig)
QUESTIONS_4_5 = {
    "test2_q2": {
        "source": "Test 2, Frage 2",
        "question": {
            "de": r"$X$ gleichverteilt auf $[-4, 4]$. Wie gross ist $P(X^2 \le 9)$?",
            "en": r"$X$ uniformly distributed on $[-4, 4]$. What is $P(X^2 \le 9)$?"
        },
        "options": [r"$\frac{7}{9}$", r"$\frac{4}{9}$", r"$\frac{2}{3}$", r"$\frac{3}{4}$"],
        "correct_idx": 3,
        "solution": {
            "de": r"**Richtig: $\frac{3}{4}$**<br>$X^2 \le 9 \Leftrightarrow -3 \le X \le 3$.<br>Länge Intervall ist 6. Gesamtlänge $[-4, 4]$ ist 8.<br>$P = \frac{6}{8} = \frac{3}{4}$.",
            "en": r"**Correct: $\frac{3}{4}$**<br>$X^2 \le 9 \Leftrightarrow -3 \le X \le 3$.<br>Length interval is 6. Total length $[-4, 4]$ is 8.<br>$P = \frac{6}{8} = \frac{3}{4}$."
        }
    }
}

# 4.6 Exponential
QUESTIONS_4_6 = {
    "uebung2_mc12": {
        "source": "Übung 2, MC12",
        "question": {
            "de": r"Autobatterie, erwartete Lebensdauer $10\,000$ km (Exponential). $P(X > 20\,000)$?",
            "en": r"Car battery, expected life $10\,000$ km (Exponential). $P(X > 20\,000)$?"
        },
        "options": ["0.865", "0.607", "0.500", "0.135"],
        "correct_idx": 3,
        "solution": {
            "de": r"**Richtig: 0.135**<br>$P(X > 2\mu) = e^{-2} \approx 0.135$",
            "en": r"**Correct: 0.135**<br>$P(X > 2\mu) = e^{-2} \approx 0.135$"
        }
    },
    "hs2022_mc4": {
        "source": "HS 2022 Januar, MC #4",
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
            "de": r"**Richtig: (d)**<br>Integral muss 1 sein. Exponentialverteilung: $f(x) = \lambda e^{-\lambda x}$.<br>Hier $\lambda = 0.8 = 4/5$. Also $c = 0.8$.",
            "en": r"**Correct: (d)**<br>Integral must be 1. Exponential distribution: $f(x) = \lambda e^{-\lambda x}$.<br>Here $\lambda = 0.8 = 4/5$. So $c = 0.8$."
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
            "de": r"**Lösung:**<br>1. $F(t) = 1 - e^{-t/500}$.<br>2. $e^{-1} \approx 0.368$.<br>3. $x \approx 805$ Tage.<br>4. $T \sim \text{Exp}(1/250)$.<br>5. Summe von 20 Exp-Variablen $\to$ Näherung durch Normalverteilung (CLT). $P(S > 5475) \approx 0.39$.",
            "en": r"**Solution:**<br>1. $F(t) = 1 - e^{-t/500}$.<br>2. $e^{-1} \approx 0.368$.<br>3. $x \approx 805$ days.<br>4. $T \sim \text{Exp}(1/250)$.<br>5. Sum of 20 Exp variables $\to$ Approx via Normal (CLT). $P(S > 5475) \approx 0.39$."
        }
    },
    "hs2023_mc12": {
        "source": "HS 2023 Januar, MC #12",
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
            "de": r"**Richtig: (b)**<br>Zuerst $p_{neu} = P(\text{Win}>2)$ für einen Automaten ($B(5,0.2)$) berechnen ($\approx 0.0579$).<br>Dann $Y \sim B(100, p_{neu})$. Gesucht $P(Y \ge 4)$.",
            "en": r"**Correct: (b)**<br>First calc $p_{new} = P(\text{Win}>2)$ per slot ($B(5,0.2)$) ($\approx 0.0579$).<br>Then $Y \sim B(100, p_{new})$. Find $P(Y \ge 4)$."
        }
    }
}

# 4.7 Normalverteilung
QUESTIONS_4_7 = {
    "hs2023_mc7": {
        "source": "HS 2023 Januar, MC #7",
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
            "de": r"**Richtig: (a)**<br>$Z = \frac{25-20}{3} \approx 1.67$. $\Phi(1.67) \approx 0.952$.",
            "en": r"**Correct: (a)**<br>$Z = \frac{25-20}{3} \approx 1.67$. $\Phi(1.67) \approx 0.952$."
        }
    },
    "hs2024_mc9": {
        "source": "HS 2024 Januar, MC #9",
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
            "de": r"**Richtig: (d)**<br>Log-Transformation: $P(X < 12000) = P(\ln X < \ln 12000)$. $\ln(12000) \approx 9.39$.<br>$Z = \frac{9.39 - 8}{2} \approx 0.70$. $\Phi(0.70) \approx 0.758$.",
            "en": r"**Correct: (d)**<br>Log-Transformation: $P(X < 12000) = P(\ln X < \ln 12000)$. $\ln(12000) \approx 9.39$.<br>$Z = \frac{9.39 - 8}{2} \approx 0.70$. $\Phi(0.70) \approx 0.758$."
        }
    },
    "uebung2_mc13": {
        "source": "Übung 2, MC13",
        "question": {
            "de": r"$X \sim N(30, 9)$. Wie gross ist $P[X < 21]$?",
            "en": r"$X \sim N(30, 9)$. What is $P[X < 21]$?"
        },
        "options": ["0.999", "0.841", "0.159", "0.00135"],
        "correct_idx": 3,
        "solution": {
            "de": r"**Richtig: 0.00135**<br>$Z = \frac{21-30}{3} = -3$. $P(Z < -3) \approx 0.00135$",
            "en": r"**Correct: 0.00135**<br>$Z = \frac{21-30}{3} = -3$. $P(Z < -3) \approx 0.00135$"
        }
    },
    "hs2022_mc3": {
        "source": "HS 2022 Januar, MC #3",
        "question": {
            "de": "Nehmen wir an, dass X₁, X₂, ..., X₁₀₀ unabhängige und identisch i.i.d gleichverteilte Zufallsvariablen zwischen 0 und 1 sind. Wie groß ist ungefähr die Wahrscheinlichkeit, dass das arithmetische Mittel größer als 0.55 ist, wenn N = 100?",
            "en": "Let X₁, X₂, ..., X₁₀₀ be i.i.d. uniform random variables on [0, 1]. What is approximately the probability that the arithmetic mean is greater than 0.55 when N = 100?"
        },
        "options": ["4.2%", "50%", "95.8%", "10%"],
        "correct_idx": 0,
        "solution": {
            "de": "**Richtig: 4.2%**<br>CLT: μ = 0.5, σ² = 1/12.<br>σ_X̄ = √(1/1200).<br>Z = (0.55-0.5)/σ_X̄ ≈ 1.73.<br>P(Z > 1.73) ≈ 0.042.",
            "en": "**Correct: 4.2%**<br>CLT: μ = 0.5, σ² = 1/12.<br>σ_X̄ = √(1/1200).<br>Z = (0.55-0.5)/σ_X̄ ≈ 1.73.<br>P(Z > 1.73) ≈ 0.042."
        }
    },
    "hs2024_mc3_tanker": {
        "source": "HS 2024 Januar, MC #3",
        "question": {
            "de": r"Der vollbeladene Öltanker Ever Given II mit einer Gesamtkapazität von $30.000 \,\text{m}^3$ will den Kiel Kanal passieren. Hat der Tanker mehr als $27.040$ Tonnen Rohöl geladen so würde er auf Grund laufen. Das Gewicht von $1 \,\text{m}^3$ Rohöl ist unabhängig und identisch mit Mittelwert $0.9$ und unbekannter Varianz $\sigma^2$ verteilt. Mit Hilfe seiner Statistikkenntnisse schätzt der Kapitän die Wahrscheinlichkeit auf Grund zu laufen auf $0.2$. Welche Varianz $\sigma^2$ hat der Kapitän für das Gewicht von $1 \,\text{m}^3$ angenommen?",
            "en": r"The fully loaded oil tanker Ever Given II with capacity $30,000 \,\text{m}^3$ wants to pass the Kiel Canal. If it has more than $27,040$ tons of crude oil, it would run aground. The weight of $1 \,\text{m}^3$ of crude oil is i.i.d. with mean $0.9$ and unknown variance $\sigma^2$. The captain estimates the probability of running aground at $0.2$. What variance $\sigma^2$ has the captain assumed?"
        },
        "options": [r"$0.0064$", r"$0.0016$", r"$0.0100$", r"$0.0036$"],
        "correct_idx": 0,
        "solution": {
            "de": r"**Richtig: $0.0064$**<br>CLT: $P(\text{Summe} > 27.040) = 0.2$.<br>$\mu = 30000 \cdot 0.9 = 27000$.<br>Z-Wert für $0.8$: $z = 0.842$.<br>$(27040-27000)/\sqrt{30000 \cdot \sigma^2} = 0.842$.<br>$\sigma^2 = 0.0064$.",
            "en": r"**Correct: $0.0064$**<br>CLT: $P(\text{Sum} > 27,040) = 0.2$.<br>$\mu = 30,000 \cdot 0.9 = 27,000$.<br>Z-value for $0.8$: $z = 0.842$.<br>$(27040-27000)/\sqrt{30000 \cdot \sigma^2} = 0.842$.<br>$\sigma^2 = 0.0064$."
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
            r"$P(\frac{X-1}{2} \le y) = \Phi(y)$",
            r"$\Phi^{-1}(0.91) = 0.8186$ (laut Tabelle/Kontext, tatsächlich umgekehrt)",
            r"$E[2X - 3Y] = -1$",
            r"$\Phi(-1) = P(Y \ge 1)$"
        ],
        "correct_idx": 2,
        "solution": {
            "de": r"**Richtig: (c) ist FALSCH**<br>$E[2X - 3Y] = 2E[X] - 3E[Y] = 2(1) - 3(0) = 2$. Die Aussage behauptet $-1$.",
            "en": r"**Correct: (c) is FALSE**<br>$E[2X - 3Y] = 2E[X] - 3E[Y] = 2(1) - 3(0) = 2$. The statement claims $-1$."
        }
    }
}

# 4.8 Hypergeometrisch
QUESTIONS_4_8 = {
    "hypergeom_10_5_3": {
        "source": "Test 5, Frage 1",
        "question": {
            "de": r"Urne mit $N=10$ Kugeln, davon $M=5$ rot. Ziehe $n=3$ ohne Zurücklegen. $X = \text{Anzahl rote Kugeln}$. $P(X=2)$?",
            "en": r"Urn with $N=10$ balls, $M=5$ red. Draw $n=3$ without replacement. $X = \text{number of red balls}$. $P(X=2)$?"
        },
        "options": [r"$5/12$", r"$1/2$", r"$1/3$", r"$7/12$"],
        "correct_idx": 0,
        "solution": {
            "de": r"**Richtig: $5/12$**<br>Hypergeometrisch: $P(X=2) = \frac{\binom{5}{2} \cdot \binom{5}{1}}{\binom{10}{3}} = \frac{10 \cdot 5}{120} = \frac{50}{120} = \frac{5}{12}$.",
            "en": r"**Correct: $5/12$**<br>Hypergeometric: $P(X=2) = \frac{\binom{5}{2} \cdot \binom{5}{1}}{\binom{10}{3}} = \frac{10 \cdot 5}{120} = \frac{50}{120} = \frac{5}{12}$."
        }
    }
}

# 4.9 Additional Questions (Distributions)
QUESTIONS_4_9 = {
    "hs2023_prob3": {
        "source": "HS 2023 Januar, Problem 3",
        "type": "problem",
        "question": {
            "de": r"Schweinerennen. Max V. braucht 10s. 4 andere Schweine $Y \sim N(13, 2.5^2)$.<br>1. $P(\text{Max V. gewinnt})$.<br>2. $P(\text{Max V. mindestens Dritter})$.<br>3. CLT Approximation für N Rennen.",
            "en": r"Pig racing. Max V. takes 10s. 4 other pigs $Y \sim N(13, 2.5^2)$.<br>1. $P(\text{Max V. wins})$.<br>2. $P(\text{Max V. at least 3rd})$.<br>3. CLT Approximation."
        },
        "solution": {
            "de": r"**Lösung:**<br>1. $P(Y > 10) = P(Z > -1.2) \approx 0.885$. Sieg gegen alle 4: $0.885^4 \approx 0.613$.<br>2. Binomialverteilung.",
            "en": r"**Solution:**<br>1. $P(Y > 10) = P(Z > -1.2) \approx 0.885$. Win against all 4: $0.885^4 \approx 0.613$.<br>2. Binomial distribution."
        }
    },
    "uebung2_mc9": {
        "source": "Übung 2, MC #9",
        "type": "mc",
        "question": {
            "de": r"Die Binomialverteilung beschreibt:",
            "en": r"The Binomial distribution describes:"
        },
        "options": [
            r"Anzahl Erfolge bei n unabhängigen Versuchen (mit Zurücklegen).",
            r"Anzahl Versuche bis zum ersten Erfolg.",
            r"Anzahl Erfolge in einem festen Zeitintervall.",
            r"Anzahl Erfolge ohne Zurücklegen."
        ],
        "correct_idx": 0,
        "solution": {
            "de": r"**Richtig: (a)**<br>x Erfolge in n Versuchen. (b)=Geometrisch, (c)=Poisson, (d)=Hypergeometrisch.",
            "en": r"**Correct: (a)**<br>x successes in n trials. (b)=Geometric, (c)=Poisson, (d)=Hypergeometric."
        }
    },
    "uebung2_mc10": {
        "source": "Übung 2, MC #10",
        "type": "mc",
        "question": {
            "de": r"Wann ist die Normalverteilung eine gute Approximation für die Binomialverteilung?",
            "en": r"When is the Normal distribution a good approximation for the Binomial distribution?"
        },
        "options": [
            r"Wenn n > 30 und p < 0.1",
            r"Wenn die Varianz groß genug ist ($np(1-p) > 9$).",
            r"Wenn n < 30.",
            r"Wenn p = 0.5 exakt."
        ],
        "correct_idx": 1,
        "solution": {
            "de": r"**Richtig: (b)**<br>Faustregel (Moivre-Laplace): Varianz $> 9$.",
            "en": r"**Correct: (b)**<br>Rule of thumb: Variance $> 9$."
        }
    },
    "uebung2_mc14": {
        "source": "Übung 2, MC #14",
        "type": "mc",
        "question": {
            "de": r"$X \sim N(30, 9)$. Finde $t$ so dass $P(X \ge t) = 0.0668$.",
            "en": r"$X \sim N(30, 9)$. Find $t$ s.t. $P(X \ge t) = 0.0668$."
        },
        "options": [
            r"34.5",
            r"33.0",
            r"31.5",
            r"30.0"
        ],
        "correct_idx": 0,
        "solution": {
            "de": r"**Richtig: (a)**<br>Fläche rechts = 0.0668 $\implies$ Fläche links = 0.9332.<br>Tabelle: $z \approx 1.5$.<br>$x = 30 + 1.5 \cdot 3 = 34.5$.",
            "en": r"**Correct: (a)**<br>Area right = 0.0668 $\implies$ Area left = 0.9332.<br>Table: $z \approx 1.5$.<br>$x = 30 + 1.5 \cdot 3 = 34.5$."
        }
    },
    "uebung2_mc15": {
        "source": "Übung 2, MC #15",
        "type": "mc",
        "question": {
            "de": r"$X \sim N(30, 9)$. Zentrales 95% Intervall?",
            "en": r"$X \sim N(30, 9)$. Central 95% interval?"
        },
        "options": [
            r"[29.05, 30.95]",
            r"[24.12, 35.88]",
            r"[27.00, 33.00]",
            r"[25.05, 34.95]"
        ],
        "correct_idx": 1,
        "solution": {
            "de": r"**Richtig: (b)**<br>$\mu \pm 1.96\sigma = 30 \pm 1.96 \cdot 3 = 30 \pm 5.88 = [24.12, 35.88]$.",
            "en": r"**Correct: (b)**<br>$\mu \pm 1.96\sigma = 30 \pm 1.96 \cdot 3 = 30 \pm 5.88 = [24.12, 35.88]$."
        }
    },
    "uebung2_mc11": {
        "source": "Übung 2, MC #11",
        "type": "mc",
        "question": {
            "de": r"Miguel gewinnt Giro d'Italia mit $p=0.3$. 5 Teilnahmen. Wahrscheinlichkeit mind. 2 Siege?",
            "en": r"Win prob 0.3. 5 attempts. Prob of at least 2 wins?"
        },
        "options": [r"0.6398", r"0.4718", r"0.6", r"0.3602", r"0.5282"],
        "correct_idx": 1,
        "solution": {
            "de": r"**Richtig: (b)**<br>Gegenwahrscheinlichkeit: $1 - (P(0)+P(1)) = 1 - (0.168 + 0.360) = 0.472$.",
            "en": r"**Correct: (b)**<br>Complement: $1 - (P(0)+P(1)) = 1 - (0.168 + 0.360) = 0.472$."
        }
    },
    "hs2022_mc6": {
        "source": "HS 2022 Januar, MC #6",
        "type": "mc",
        "question": {
            "de": r"7 Tage Hamburg, Regenwahrscheinlichkeit pro Tag 70%. Wahrscheinlichkeit für mind. 5 Regentage?",
            "en": r"7 days Hamburg, 70% rain chance per day. Probability of at least 5 rainy days?"
        },
        "options": [r"65%", r"66%", r"67%", r"68%"],
        "correct_idx": 0,
        "solution": {
            "de": r"**Richtig: 65%**<br>Binomial $n=7, p=0.7$. $P(5)+P(6)+P(7) \approx 0.318+0.247+0.082 = 0.647$.",
            "en": r"**Correct: 65%**<br>Binomial $n=7, p=0.7$. $P(5)+P(6)+P(7) \approx 0.318+0.247+0.082 = 0.647$."
        }
    },
    "test4_mc1": {
        "source": "Test 4, Q1",
        "type": "mc",
        "question": {
            "de": r"$X \sim Pois(10), Z=2X$. Welche Aussage trifft NICHT zu?",
            "en": r"$X \sim Pois(10), Z=2X$. Which is FALSE?"
        },
        "options": [r"$Z \sim Pois(20)$", r"$Var(Z) = 40$", r"Corr(X, Z) = 1$", r"$E[Z] = 20$"],
        "correct_idx": 0,
        "solution": {
            "de": r"**Richtig: (a)**<br>$Z$ nimmt nur gerade Werte an, Poisson muss alle ganzen Zahlen können.",
            "en": r"**Correct: (a)**<br>$Z$ only takes even values, Poisson requires all integers."
        }
    },
    "test5_mc1": {
        "source": "Test 5, Q1",
        "type": "mc",
        "question": {
            "de": r"1000 Leute (700 Smart, 300 Gewöhnlich). Stichprobe 200. $P(X=10)$ gewöhnliche?",
            "en": r"1000 ppl (700 smart, 300 ordinary). Sample 200. $P(X=10)$ ordinary?"
        },
        "options": [r"Additiv", r"Multiplikativ", r"Hypergeometrisch", r"Unbekannt"],
        "correct_idx": 2,
        "solution": {
            "de": r"**Richtig: Hypergeometrisch**<br>Ziehen ohne Zurücklegen aus zwei Gruppen.",
            "en": r"**Correct: Hypergeometric**<br>Sampling without replacement from two groups."
        }
    }
}

# 5.1 Erwartungswert
QUESTIONS_5_1 = {
    "test3_q4": {
        "source": "Test 3, Frage 4",
        "question": {
            "de": r"Sei $E[X] = 2$ und $E[Y] = 3$. Was ist $E[X + Y]$?",
            "en": r"Let $E[X] = 2$ and $E[Y] = 3$. What is $E[X + Y]$?"
        },
        "options": [{"de": r"$5$", "en": r"$5$"}, {"de": r"$6$", "en": r"$6$"}, {"de": r"$1$", "en": r"$1$"}, {"de": "Unbekannt", "en": "Unknown"}],
        "correct_idx": 0,
        "solution": {
            "de": r"**Richtig: $5$**<br>Linearität des Erwartungswertes: $E[X+Y] = E[X] + E[Y]$.",
            "en": r"**Correct: $5$**<br>Linearity of expectation: $E[X+Y] = E[X] + E[Y]$."
        }
    },
    "uebung3_mc5": {
        "source": "Übung 3, MC5",
        "question": {
            "de": r"Der Erwartungswert-Operator $E[\cdot]$ ist...",
            "en": r"The expectation operator $E[\cdot]$ is..."
        },
        "options": [{"de": "Linear", "en": "Linear"}, {"de": "Quadratisch", "en": "Quadratic"}, {"de": "Logarithmisch", "en": "Logarithmic"}, {"de": "Exponentiell", "en": "Exponential"}],
        "correct_idx": 0,
        "solution": {
            "de": r"**Richtig: Linear**<br>$E[aX + bY] = aE[X] + bE[Y]$.",
            "en": r"**Correct: Linear**<br>$E[aX + bY] = aE[X] + bE[Y]$."
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
            "de": r"**Lösung:**<br>1. Integral über Bereich muss 1 geben.<br>2. $f_X(x) = \frac{x+2c}{2+4c}$.<br>3. $\text{Var}(X) \approx 0.32$.<br>5. Integral über Dreieck/Bereich $\approx 0.085$.",
            "en": r"**Solution:**<br>1. Integral over domain must be 1.<br>2. $f_X(x) = \frac{x+2c}{2+4c}$.<br>3. $\text{Var}(X) \approx 0.32$.<br>5. Integral over triangle/domain $\approx 0.085$."
        }
    },
    "uebung3_prob1": {
        "source": "Übung 3, Probe #1",
        "type": "problem",
        "question": {
            "de": r"Gemeinsame Massenfunktion (Tabelle). X (10, 20, 30), Y (2, 3, 4).<br>(a) Randverteilungen.<br>(c) V(X), V(Y).<br>(d) Cov, Rho.<br>(e) Unabhängig?",
            "en": r"Joint PMF table.<br>(a) Marginals.<br>(c) Variances.<br>(d) Cov, Rho.<br>(e) Indep?"
        },
        "solution": {
            "de": r"**Lösung:**<br>(a) Marginale $1/3$.<br>(d) Cov=0 (unkorreliert).<br>(e) Abhängig ($f(x,y) \neq f(x)f(y)$).",
            "en": r"**Solution:**<br>(a) Marginals $1/3$.<br>(d) Cov=0 (uncorrelated).<br>(e) Dependent."
        }
    },
    "uebung3_prob2": {
        "source": "Übung 3, Probe #2",
        "type": "problem",
        "question": {
            "de": r"Tabelle mit $x_1..x_4, y_1..y_3$.<br>(a) $f_X(x_3), f_Y(y_2)$.<br>(b) Bedingte W'keiten.",
            "en": r"Joint PMF.<br>(a) Marginals.<br>(b) Conditionals."
        },
        "solution": {
            "de": r"**Lösung:**<br>(a) Zeilensummen/Spaltensummen.<br>(b) Zelle / Randsumme.",
            "en": r"**Solution:**<br>(a) Row/Col sums.<br>(b) Cell / Marginal."
        }
    },
    "uebung3_prob4": {
        "source": "Übung 3, Probe #4",
        "type": "problem",
        "question": {
            "de": r"$f(x,y) = 24xy$ für $x+y \le 1$.<br>(a) Zeige Dichte.<br>(b) Unabhängig?",
            "en": r"$f(x,y) = 24xy$ on simplex.<br>(a) Verify PDF.<br>(b) Indep?"
        },
        "solution": {
            "de": r"**Lösung:**<br>(b) Abhängig, da Definitionsbereich (Dreieck) kein Rechteck ist.",
            "en": r"**Solution:**<br>(b) Dependent, because support (triangle) is not a rectangle."
        }
    },
    "uebung3_prob5": {
        "source": "Übung 3, Probe #5",
        "type": "problem",
        "question": {
            "de": r"$f(x,y) = 2x e^{-y}$ auf Rechteck $0<x<1, y>0$.<br>(a) Zeige Dichte.<br>(b) Unabhängig?",
            "en": r"$f(x,y) = 2x e^{-y}$.<br>(a) Verify PDF.<br>(b) Indep?"
        },
        "solution": {
            "de": r"**Lösung:**<br>(b) Unabhängig (Rechteck + Faktorisierung).",
            "en": r"**Solution:**<br>(b) Independent (Rectangle + Factorization)."
        }
    }
}

# 5.2 Varianz
QUESTIONS_5_2 = {
    "hs2023_mc9": {
        "source": "HS 2023 Januar, MC #9",
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
            "de": r"**Richtig: (b)**<br>$Cov(Y, 3-2X+3Y) = Cov(Y,3) - 2Cov(Y,X) + 3Cov(Y,Y)$.<br>$= 0 - 0 + 3Var(Y) = 3 \cdot 3 = 9$.",
            "en": r"**Correct: (b)**<br>$Cov(Y, 3-2X+3Y) = Cov(Y,3) - 2Cov(Y,X) + 3Cov(Y,Y)$.<br>$= 0 - 0 + 3Var(Y) = 3 \cdot 3 = 9$."
        }
    },
    "test3_q5": {
        "source": "Test 3, Frage 5",
        "question": {
            "de": r"$X, Y$ unabhängig. $\text{Var}(X)=2$, $\text{Var}(Y)=3$. Was ist $\text{Var}(X - Y)$?",
            "en": r"$X, Y$ independent. $\text{Var}(X)=2$, $\text{Var}(Y)=3$. What is $\text{Var}(X - Y)$?"
        },
        "options": [r"$5$", r"$-1$", r"$1$", r"$13$"],
        "correct_idx": 0,
        "solution": {
            "de": r"**Richtig: $5$**<br>Unabhängig: $\text{Var}(X - Y) = \text{Var}(X) + (-1)^2 \text{Var}(Y) = 2 + 3 = 5$.",
            "en": r"**Correct: $5$**<br>Independent: $\text{Var}(X - Y) = \text{Var}(X) + (-1)^2 \text{Var}(Y) = 2 + 3 = 5$."
        }
    },
    "uebung3_mc7": {
        "source": "Übung 3, MC7",
        "question": {
            "de": r"Was gilt allgemein für $\text{Var}(aX + b)$?",
            "en": r"What holds generally for $\text{Var}(aX + b)$?"
        },
        "options": [r"$a^2 \text{Var}(X)$", r"$a \cdot \text{Var}(X)$", r"$a^2 \text{Var}(X) + b$", r"$a \cdot \text{Var}(X) + b$"],
        "correct_idx": 0,
        "solution": {
            "de": r"**Richtig: $a^2 \text{Var}(X)$**<br>Verschiebung $b$ ändert Varianz nicht. Skalierung $a$ geht quadratisch ein.",
            "en": r"**Correct: $a^2 \text{Var}(X)$**<br>Shift $b$ does not change variance. Scaling $a$ enters quadratically."
        }
    },
    "uebung3_prob3": {
        "source": "Übung 3, Probe #3",
        "type": "problem",
        "question": {
            "de": r"X, Y Tabelle (0, 0.5, 1 vs 0, 1).<br>(a) Unabhängig?<br>(b) Cov?<br>(c) Varianz von X-Y?",
            "en": r"Table.<br>(a) Indep?<br>(b) Cov?<br>(c) V(X-Y)?"
        },
        "solution": {
            "de": r"**Lösung:**<br>(a) Abhängig.<br>(b) Cov=0.<br>(c) $V(X)+V(Y)$ (da unkorreliert).",
            "en": r"**Solution:**<br>(a) Dependent.<br>(b) Cov=0.<br>(c) $V(X)+V(Y)$ (since uncorr)."
        }
    },
    "uebung3_prob7": {
        "source": "Übung 3, Probe #7",
        "type": "problem",
        "question": {
            "de": r"X, Y, Z unabhängig. Diskrete Verteilungen gegeben.<br>(a) Mittelwert/Varianz X, Y, X-Y.<br>(b) Verteilung Summen.<br>(c) Wahrscheinlichkeiten.",
            "en": r"X, Y, Z indep discrete.<br>(a) Moments.<br>(b) Sum dists.<br>(c) Probs."
        },
        "solution": {
            "de": r"**Lösung:**<br>(a) Additivität.<br>(b) Faltung.",
            "en": r"**Solution:**<br>(a) Additivity.<br>(b) Convolution."
        }
    }
}

# 5.3 Kovarianz
QUESTIONS_5_3 = {
    "hs2024_mc2": {
        "source": "HS 2024 Januar, MC #2",
        "type": "mc",
        "question": {
            "de": r"Seien $E[X^2] = E[Y] = 1/3$, $E[X]=0$ und $\rho_{X^2, Y} > 0$. Welche Aussage über $\rho_{X,Y}$ ist immer wahr?",
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
            "de": r"**Richtig: (d)**<br>Korrelation misst lineare Abhängigkeit. $X$ könnte symmetrisch sein ($Y=X^2 \implies \rho=0$) oder nicht ($Y=X+X^2 \implies \rho \neq 0$). Nichts ist *immer* wahr.",
            "en": r"**Correct: (d)**<br>Correlation measures linear dependence. $X$ could be symmetric ($Y=X^2 \implies \rho=0$) or not ($Y=X+X^2 \implies \rho \neq 0$). Nothing is *always* true."
        }
    },
    "uebung3_mc1": {
        "source": "Übung 3, MC1",
        "question": {
            "de": "Die Kovarianz misst...",
            "en": "The covariance measures..."
        },
        "options": [
            {"de": "nur die Stärke", "en": "only the strength"},
            {"de": "nur die Richtung (linear)", "en": "only the direction (linear)"},
            {"de": "Stärke und Richtung", "en": "strength and direction"}
        ],
        "correct_idx": 1,
        "solution": {
            "de": "**Richtig: (b)** Die Kovarianz ist nicht normiert, daher schwer für Stärke zu interpretieren.",
            "en": "**Correct: (b)** Covariance is not normalized, thus hard to interpret for strength."
        }
    },
    "uebung3_mc9": {
        "source": "Übung 3, MC9",
        "question": {
            "de": r"Urne mit $5$ Kugeln ($1-5$). Ziehen ohne Zurücklegen. $X = 1$. Kugel, $Y = 2$. Kugel. Korrelation?",
            "en": r"Urn with $5$ balls ($1-5$). Draw without replacement. $X = 1$st ball, $Y = 2$nd ball. Correlation?"
        },
        "options": [r"$0$", r"$-0.25$", r"$-0.5$"],
        "correct_idx": 1,
        "solution": {
            "de": r"**Richtig: $-0.25$**<br>$\rho = \frac{-1}{N-1} = \frac{-1}{4} = -0.25$",
            "en": r"**Correct: $-0.25$**<br>$\rho = \frac{-1}{N-1} = \frac{-1}{4} = -0.25$"
        }
    },
    "test4_q2": {
        "source": "Test 4, Frage 2",
        "question": {
            "de": r"$\text{Cov}(X,Y) = 3$, $\text{Var}(X) = 4$, $\text{Var}(Y) = 9$. Berechnen Sie $\text{Cor}(X,Y)$.",
            "en": r"$\text{Cov}(X,Y) = 3$, $\text{Var}(X) = 4$, $\text{Var}(Y) = 9$. Calculate $\text{Cor}(X,Y)$."
        },
        "options": [r"$0.5$", r"$0.25$", r"$0.75$", r"$0.33$"],
        "correct_idx": 0,
        "solution": {
            "de": r"**Richtig: $0.5$**<br>$\text{Cor} = \frac{\text{Cov}}{\sigma_X \cdot \sigma_Y} = \frac{3}{2 \cdot 3} = \frac{3}{6} = 0.5$.",
            "en": r"**Correct: $0.5$**<br>$\text{Cor} = \frac{\text{Cov}}{\sigma_X \cdot \sigma_Y} = \frac{3}{2 \cdot 3} = \frac{3}{6} = 0.5$."
        }
    },
    "test4_q4": {
        "source": "Test 4, Frage 4",
        "question": {
            "de": r"Wenn $X$ und $Y$ unabhängig sind, dann ist die Kovarianz...",
            "en": r"If $X$ and $Y$ are independent, then the covariance is..."
        },
        "options": [{"de": "0", "en": "0"}, {"de": "1", "en": "1"}, {"de": "-1", "en": "-1"}, {"de": "Unbestimmt", "en": "Undefined"}],
        "correct_idx": 0,
        "solution": {
            "de": "**Richtig: 0**<br>Unabhängigkeit impliziert Unkorreliertheit.",
            "en": "**Correct: 0**<br>Independence implies uncorrelatedness."
        }
    },
    "hs2015_mc1": {
        "source": "HS 2015, MC 1 (4 Punkte)",
        "type": "mc",
        "question": {
            "de": r"Es seien $X, Y$ zwei stetige Zufallsvariablen. Welche der folgenden Aussagen ist immer korrekt?",
            "en": r"Let $X, Y$ be two continuous random variables. Which of the following statements is always correct?"
        },
        "options": [
            r"Wenn die Randdichten $f_X(x)$ und $f_Y(y)$ bekannt sind, können wir daraus die gemeinsame Dichte $f_{X,Y}(x, y)$ berechnen.",
            r"$X$ und $Y$ sind unabhängig dann und nur dann wenn $\text{Cov}(X, Y) = 0$.",
            r"$f_{Y|X}(y|x) = f_{X|Y}(x|y)$.",
            r"$\text{Cov}(X, Y) = 0$ dann und nur dann wenn $E[XY] = E[X]E[Y]$."
        ],
        "correct_idx": 3,
        "solution": {
            "de": r"**Richtig: (d)**<br>$\text{Cov}(X,Y) = E[XY] - E[X]E[Y]$. Wenn dies 0 ist, folgt direkt $E[XY] = E[X]E[Y]$.",
            "en": r"**Correct: (d)**<br>$\text{Cov}(X,Y) = E[XY] - E[X]E[Y]$. If this is 0, it directly follows that $E[XY] = E[X]E[Y]$."
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
            r"$\text{Corr}(X, Y) > \text{Corr}(X, Z)$",
            r"$\text{Corr}(X, Y) = \text{Corr}(X, Z)$",
            r"$\text{Corr}(X, Y) < \text{Corr}(X, Z)$",
            "Nicht genügend Informationen."
        ],
        "correct_idx": 1,
        "solution": {
            "de": r"**Richtig: (b)**<br>Beide sind lineare Transformationen mit positiver Steigung ($a=3$ und $a=2$). Die Korrelation mit sich selbst (linear transformiert) ist immer $+1$. Also $\text{Corr}(X,Y)=1$ und $\text{Corr}(X,Z)=1$.",
            "en": r"**Correct: (b)**<br>Both are linear transformations with positive slope ($a=3$ and $a=2$). Correlation with oneself (linearly transformed) is always $+1$. Thus $\text{Corr}(X,Y)=1$ and $\text{Corr}(X,Z)=1$."
        }
    }
}


# 5.4 Korrelation
QUESTIONS_5_4 = {
    "uebung3_mc10": {
        "source": "Übung 3, MC10",
        "question": {
            "de": "Der Korrelationskoeffizient liegt immer zwischen...",
            "en": "The correlation coefficient is always between..."
        },
        "options": [r"$-1$ und $1$", r"$0$ und $1$", r"$-\infty$ und $\infty$", r"$0$ und $\infty$"],
        "correct_idx": 0,
        "solution": {
            "de": r"**Richtig: $-1$ und $1$**<br>Eigenschaft der Korrelation: $-1 \le \rho \le 1$.",
            "en": r"**Correct: $-1$ and $1$**<br>Property of correlation: $-1 \le \rho \le 1$."
        }
    },
    "uebung3_mc11": {
        "source": "Übung 3, MC11",
        "question": {
            "de": r"$\text{Corr}(X,Y) = 0.8$ bedeutet...",
            "en": r"$\text{Corr}(X,Y) = 0.8$ means..."
        },
        "options": [
            {"de": "Starker positiver linearer Zusammenhang", "en": "Strong positive linear relationship"},
            {"de": "Schwacher Zusammenhang", "en": "Weak relationship"},
            {"de": "Kein Zusammenhang", "en": "No relationship"},
            {"de": "Negativer Zusammenhang", "en": "Negative relationship"}
        ],
        "correct_idx": 0,
        "solution": {
            "de": "**Richtig: Starker positiver linearer Zusammenhang.**",
            "en": "**Correct: Strong positive linear relationship.**"
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
            "Hinreichend für 1: Identisch verteilt. Hinreichend für 2: Unabhängig.",
            "Hinreichend für 1: Unabhängig. Hinreichend für 2: Identisch verteilt.",
            "Beide gelten immer, auch bei Abhängigkeit.",
            "Beide gelten immer, auch bei nicht-identischer Verteilung."
        ],
        "correct_idx": 1,
        "solution": {
            "de": r"**Richtig: (b)**<br>Gleichung 1 (Bienaymé) gilt, wenn die Variablen **unabhängig** (oder zumindest unkorreliert) sind.<br>Gleichung 2 gilt, wenn alle Varianzen gleich sind, also wenn sie **identisch verteilt** sind.",
            "en": r"**Correct: (b)**<br>Equation 1 (Bienaymé) holds if variables are **independent** (or at least uncorrelated).<br>Equation 2 holds if all variances are equal, i.e., if they are **identically distributed**."
        }
    },
    "uebung3_prob6": {
        "source": "Übung 3, Probe #6",
        "type": "problem",
        "question": {
            "de": r"Notenverteilung Mathe (X) Englisch (Y). Tabelle.<br>(a) Momente zeigen.<br>(b) Cov, Rho.<br>(c) $Z = (X+Y)/2$.",
            "en": r"Grades Math/Eng. Table.<br>(a) Moments.<br>(b) Cov/Rho.<br>(c) Average Z."
        },
        "solution": {
            "de": r"**Lösung:**<br>(b) Cov 0.29, Rho 0.36.<br>(c) Diversifikationseffekt (kleinere Varianz).",
            "en": r"**Solution:**<br>(b) Cov 0.29, Rho 0.36.<br>(c) Diversification (lower variance)."
        }
    }
}




# 5.5 Additional Questions (Multidimensional)
QUESTIONS_5_5 = {
    "uebung3_mc2": {
        "source": "Übung 3, MC #2",
        "type": "mc",
        "question": {
            "de": r"Der Korrelationskoeffizient $\rho$:",
            "en": r"Correlation coefficient $\rho$:"
        },
        "options": [
            r"misst nur die Stärke.",
            r"misst nur die Richtung.",
            r"misst Stärke und Richtung des linearen Zusammenhangs.",
            r"hat keine Aussagekraft."
        ],
        "correct_idx": 2,
        "solution": {
            "de": r"**Richtig: (c)**<br>Korrelation ist normiert (-1 bis 1) und misst linearen Zusammenhang.",
            "en": r"**Correct: (c)**<br>Correlation is normalized (-1 to 1) and measures linear relationship."
        }
    },
    "uebung3_mc3": {
        "source": "Übung 3, MC #3",
        "type": "mc",
        "question": {
            "de": r"Zwei Variablen sind unabhängig, wenn:",
            "en": r"Two variables are independent if:"
        },
        "options": [
            r"$\rho = 0$.",
            r"$f(x,y) = f_X(x) \cdot f_Y(y)$.",
            r"$f(x,y) = f_X(x) + f_Y(y)$.",
            r"Cov = 1."
        ],
        "correct_idx": 1,
        "solution": {
            "de": r"**Richtig: (b)**<br>Unabhängigkeit bedeutet Faktorisierung der Dichte.",
            "en": r"**Correct: (b)**<br>Independence means factorization of the density."
        }
    },
    "uebung3_mc4": {
        "source": "Übung 3, MC #4",
        "type": "mc",
        "question": {
            "de": r"Die Kovarianz wird errechnet mit:",
            "en": r"Covariance is calculated as:"
        },
        "options": [
            r"$E[XY] - E[X]E[Y]$",
            r"$E[XY] - E[X^2]E[Y^2]$",
            r"$E[XY]^2 - E[X]E[Y]$",
            r"$E[X^2Y^2] - ...$"
        ],
        "correct_idx": 0,
        "solution": {
            "de": r"**Richtig: (a)**<br>Verschiebungssatz für Kovarianz.",
            "en": r"**Correct: (a)**<br>Shift formula for covariance."
        }
    },
    "uebung3_mc6": {
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
            r"Nur falls X und Y identisch sind."
        ],
        "correct_idx": 2,
        "solution": {
            "de": r"**Richtig: (c)**<br>Das ist die Definition von Unkorreliertheit ($Cov=0$). Unabhängigkeit impliziert dies auch.",
            "en": r"**Correct: (c)**<br>Definition of uncorrelated ($Cov=0$). Independence implies this too."
        }
    },
    "uebung3_mc8": {
        "source": "Übung 3, MC #8",
        "type": "mc",
        "question": {
            "de": r"X = Würfel, Y = Münze ('Kopf'). $P(X > 3 | Y = \text{'Kopf'})$?",
            "en": r"X = Die, Y = Coin ('Head'). $P(X > 3 | Y = \text{'Head'})$?"
        },
        "options": [
            r"1/3",
            r"1/2",
            r"2/3",
            r"0"
        ],
        "correct_idx": 1,
        "solution": {
            "de": r"**Richtig: (b)**<br>Unabhängig. Münze egal. Würfel > 3 (4,5,6) ist 3/6 = 1/2.",
            "en": r"**Correct: (b)**<br>Independent. Die prob is 3/6 = 1/2."
        }
    },
    "uebung3_mc12": {
        "source": "Übung 3, MC #12",
        "type": "mc",
        "question": {
            "de": r"Dichte $f(x,y) = x/12 + y/6$ auf $[0,2]^2$. $E[X+2Y]$?",
            "en": r"Density $f(x,y) = x/12 + y/6$ on $[0,2]^2$. $E[X+2Y]$?"
        },
        "options": [
            r"33/9",
            r"34/9",
            r"10/3",
            r"32/9"
        ],
        "correct_idx": 3,
        "solution": {
            "de": r"**Richtig: (d)**<br>$E[X]=10/9, E[Y]=11/9$. Summe: $32/9$.",
            "en": r"**Correct: (d)**<br>$E[X]=10/9, E[Y]=11/9$. Sum: $32/9$."
        }
    },
    "uebung3_mc13": {
        "source": "Übung 3, MC #13",
        "type": "mc",
        "question": {
            "de": r"Gleiche Dichte wie #12. $V(Y)$?",
            "en": r"Same density. $V(Y)$?"
        },
        "options": [
            r"23/81",
            r"25/81",
            r"26/81",
            r"28/81"
        ],
        "correct_idx": 0,
        "solution": {
            "de": r"**Richtig: (a)**<br>$E[Y^2] - E[Y]^2 = 16/9 - 121/81 = 23/81$.",
            "en": r"**Correct: (a)**<br>$E[Y^2] - E[Y]^2 = 16/9 - 121/81 = 23/81$."
        }
    },
    "test3_mc3": {
        "source": "Test 3, Q3",
        "type": "mc",
        "question": {
            "de": r"$Corr(X,Y)=-1, Var(X)=1, SD(Y)=2$. $Var(3X+Y)$?",
            "en": r"$Corr(X,Y)=-1, Var(X)=1, SD(Y)=2$. $Var(3X+Y)$?"
        },
        "options": [r"7", r"13", r"5", r"1"],
        "correct_idx": 3,
        "solution": {
            "de": r"**Richtig: 1**<br>$9(1) + 4 + 2(3)(1)(-1)(1)(2) = 13 - 12 = 1$.",
            "en": r"**Correct: 1**<br>$9(1) + 4 + 2(3)(1)(-1)(1)(2) = 13 - 12 = 1$."
        }
    },
    "test3_mc4": {
        "source": "Test 3, Q4",
        "type": "mc",
        "question": {
            "de": r"X, Y unkorreliert. $E(X)=E(Y)=1, Var(X)=Var(Y)=1$. Was gilt?",
            "en": r"X, Y uncorrelated. Moments given. True?"
        },
        "options": [r"$3E(X^2) + Cov(X,Y) = 2$", r"$E(XY) = 2$", r"$Cov(X, Y+2) = 2$", r"$E((X-Y)^2) = 2$"],
        "correct_idx": 3,
        "solution": {
            "de": r"**Richtig: (d)**<br>$E[(X-Y)^2] = Var(X-Y) + (E[X-Y])^2 = (1+1) + 0 = 2$.",
            "en": r"**Correct: (d)**<br>$E[(X-Y)^2] = Var(X-Y) + (E[X-Y])^2 = (1+1) + 0 = 2$."
        }
    },
    "test4_mc2": {
        "source": "Test 4, Q2",
        "type": "mc",
        "question": {
            "de": r"$Z = 4X - 3Y + 2$. $Cov(X, Z)$ unter Annahme Unkorreliertheit?",
            "en": r"$Z = 4X - 3Y + 2$. $Cov(X, Z)$ assuming uncorrelated?"
        },
        "options": [r"0", r"64", r"16", r"Info fehlt"],
        "correct_idx": 2,
        "solution": {
            "de": r"**Richtig: 16**<br>$Cov(X, 4X) = 4 Var(X) = 16$ (wenn Var=4... Moment, Frage unvollständig im Original, Annahme Var=4 aus Kontext oder Typo $4 \cdot 1$? Staging sagt '4 Var(X) = 16'. Also Var=4).",
            "en": r"**Correct: 16**<br>$Cov(X, 4X) = 4 Var(X) = 16$ (assuming Var=4)."
        }
    },
    "test5_mc2": {
        "source": "Test 5, Q2",
        "type": "mc",
        "question": {
            "de": r"Stetige ZV X, Y. Was ist immer korrekt bzgl. Unkorreliertheit?",
            "en": r"Continuous X, Y. What is always correct re: uncorrelatedness?"
        },
        "options": [r"Randdichten reichen", r"Unabh <=> Cov=0", r"$f(y|x)$...", r"$Cov=0 \iff E[XY] = E[X]E[Y]$"],
        "correct_idx": 3,
        "solution": {
            "de": r"**Richtig: (d)**<br>Definition von Covariance=0.",
            "en": r"**Correct: (d)**<br>Definition of Covariance=0."
        }
    }
}


# 6. Zentraler Grenzwertsatz (CLT)
QUESTIONS_6_3 = {
    "uebung4_mc1": {
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
            "de": r"**Richtig: (b), (c), (d)**<br>Präzise (b): Standardisierte Summe konvergiert gegen $N(0,1)$.<br>Praktisch (c): Summe ist approx. $N(n\mu, n\sigma^2)$.",
            "en": r"**Correct: (b), (c), (d)**<br>Precise (b): Standardized sum converges to $N(0,1)$.<br>Practical (c): Sum is approx. $N(n\mu, n\sigma^2)$."
        }
    },
    "uebung4_mc2": {
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
            "de": r"**Richtig: (a), (c), (e)**<br>Summe (a), i.i.d. (c), Großes n (e).",
            "en": r"**Correct: (a), (c), (e)**<br>Sum (a), i.i.d. (c), Large n (e)."
        }
    },
    "uebung4_mc3": {
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
            "de": r"**Richtig: (a), (d)**<br>(a) $B(n,p)+B(m,p) \sim B(n+m, p)$.<br>(d) $N(0,1)+N(0,1) \sim N(0, 2)$ (Normal, aber nicht Standard).",
            "en": r"**Correct: (a), (d)**<br>(a) $B(n,p)+B(m,p) \sim B(n+m, p)$.<br>(d) $N(0,1)+N(0,1) \sim N(0, 2)$ (Normal, not Standard)."
        }
    },
    "uebung4_prob3": {
        "source": "Übung 4, Probe #3",
        "type": "problem",
        "question": {
            "de": r"Produktion $n=2000$. Zurückweisung wenn $>200$ defekt. Gesucht max $p$, damit mit 95% W'keit *nicht* zurückgewiesen ($k \le 200$).",
            "en": r"$n=2000$. Reject if $>200$. Find max $p$ s.t. $P(X \le 200) \ge 0.95$."
        },
        "options": [
            r"0.080",
            r"0.090",
            r"0.100",
            r"0.110"
        ],
        "correct_idx": 1,
        "solution": {
             "de": r"**Richtig: 0.090**<br>$P(X \le 200) = 0.95 \implies Z=1.645$. Auflösen nach p.",
             "en": r"**Correct: 0.090**<br>$P(X \le 200) = 0.95 \implies Z=1.645$. Solve for p."
        }
    },
    "uebung4_prob7": {
        "source": "Übung 4, Probe #7",
        "type": "problem",
        "question": {
            "de": r"Seilbahn max 4200kg. 50 Personen, $\mu=80, \sigma=10$. Wahrscheinlichkeit Überlastung?",
            "en": r"Cable car max 4200kg. 50 ppl mean 80 SD 10. Overload prob?"
        },
        "options": [
            r"0.23%",
            r"2.3%",
            r"0.02%",
            r"5%"
        ],
        "correct_idx": 0,
        "solution": {
            "de": r"**Richtig: 0.23%**<br>$\mu_{sum} = 4000, \sigma_{sum} = \sqrt{50}\cdot 10 \approx 70.7$.<br>$Z = 200/70.7 \approx 2.83$. $1-\Phi(2.83) = 0.0023$.",
            "en": r"**Correct: 0.23%**<br>$\mu_{sum} = 4000, \sigma_{sum} = \sqrt{50}\cdot 10 \approx 70.7$.<br>$Z = 200/70.7 \approx 2.83$. $1-\Phi(2.83) = 0.0023$."
        }
    }
}

# 7. Beschreibende Statistik (Descriptive Statistics)
QUESTIONS_7 = {
    "test4_q3": {
        "source": "Test 4, Frage 3",
        "question": {
            "de": r"Welche Zahl ist KEINER dieser Maße (Mean, Median, Mode)? Datensatz: $\{4, 4, 7, 7, 7, 8, 11, 13, 13, 14, 22\}$",
            "en": r"Which number is NONE of these measures (Mean, Median, Mode)? Dataset: $\{4, 4, 7, 7, 7, 8, 11, 13, 13, 14, 22\}$"
        },
        "options": [r"$7$", r"$8$", r"$9.8$", r"$11$"],
        "correct_idx": 3,
        "solution": {
            "de": r"**Richtig: $11$**<br>Mean $\approx 9.8$, Median $= 8$, Mode $= 7$.<br>11 ist keines davon.",
            "en": r"**Correct: $11$**<br>Mean $\approx 9.8$, Median $= 8$, Mode $= 7$.<br>11 is none of these."
        }
    },
    "hs2015_mc9": {
        "source": "HS 2015 Januar, MC #9 (4 Punkte)",
        "type": "mc",
        "question": {
            "de": r"1000 Packungen Reis werden gewogen (annähernd normalverteilt). 800 Packungen wiegen zwischen 343.2 und 356.8 Gramm. Was ist die ungefähre Varianz des Gewichtes?",
            "en": r"1000 packages of rice are weighed (approximately normally distributed). 800 packages weigh between 343.2 and 356.8 grams. What is the approximate variance of the weight?"
        },
        "options": [
            r"$\sigma^2 \approx 16$",
            r"$\sigma^2 \approx 25$",
            r"$\sigma^2 \approx 36$",
            r"$\sigma^2 \approx 49$"
        ],
        "correct_idx": 1,
        "solution": {
            "de": r"**Richtig: (b)**<br>Anteil $800/1000 = 0.8$. Das symmetrische Intervall für $80\%$ Wahrscheinlichkeit ist $\mu \pm 1.28\sigma$.<br>Intervallbreite: $356.8 - 343.2 = 13.6$.<br>$2 \cdot 1.28 \sigma = 13.6 \Rightarrow \sigma \approx 5.31$.<br>$\sigma^2 \approx 28.2$. Am nächsten bei 25.",
            "en": r"**Correct: (b)**<br>Proportion $800/1000 = 0.8$. Symmetric interval for $80\%$ probability is $\mu \pm 1.28\sigma$.<br>Interval width: $356.8 - 343.2 = 13.6$.<br>$2 \cdot 1.28 \sigma = 13.6 \Rightarrow \sigma \approx 5.31$.<br>$\sigma^2 \approx 28.2$. Closest to 25."
        },
    },
    "hs2015_mc8": {
        "source": "HS 2015, MC 8 (4 Punkte)",
        "type": "mc",
        "question": {
            "de": r"Aus einer Stichprobe von 3 Werten berechnet man den Mittelwert ($\bar{x} = 5.5$) und die empirische Varianz ($s^2 = 4.5$). Der mittlere der beiden Werte ist dann notwendigerweise:",
            "en": r"From a sample of 3 values, the mean ($\bar{x} = 5.5$) and empirical variance ($s^2 = 4.5$) are calculated. The middle of the two values (?) is necessarily:"
        },
        "options": [
            "-1",
            "1",
            "4",
            "Wir haben nicht genügend Informationen."
        ],
        "correct_idx": 3,
        "solution": {
            "de": r"**Richtig: (d)**<br>Mit $n=3$ gibt es unendlich viele Kombinationen von 3 Zahlen, die diesen Mittelwert und diese Varianz ergeben. Der Median ist nicht eindeutig bestimmt.",
            "en": r"**Correct: (d)**<br>With $n=3$, there are infinitely many combinations of 3 numbers yielding this mean and variance. The median is not uniquely determined."
        }
    },
    "hs2015_prob1": {
        "source": "HS 2015, Aufgabe 1 (12 Punkte)",
        "type": "problem",
        "question": {
            "de": r"**Teil 1A (4 Punkte):** Ordnen Sie die Verteilungen den Grafiken zu.<br>V1: $N(0,3)$, n=100<br>V2: Exp(3), n=100<br>V3: $N(0,1)$, n=100<br>V4: U[-3,3], n=100<br><br>Grafiken: A (Boxplot), B (Histogramm), C (ECDF), D (QQ-Plot).<br><br>**Teil 1B (8 Punkte):**<br>Daten: Note 0.7 (1x), 2.3 (5x), 3.0 (6x), 3.7 (6x), 4.0 (4x), 4.3 (6x), 4.7 (4x), 5.0 (7x).<br>1. Berechnen Sie Mittelwert und Modus.<br>2. Zeichnen Sie einen Boxplot (Quartile, IQA).",
            "en": r"**Part 1A (4 Points):** Match the distributions to the plots.<br>V1: $N(0,3)$, n=100<br>V2: Exp(3), n=100<br>V3: $N(0,1)$, n=100<br>V4: U[-3,3], n=100<br><br>Plots: A (Boxplot), B (Histogram), C (ECDF), D (QQ-Plot).<br><br>**Part 1B (8 Points):**<br>Data: Grade 0.7 (1x), 2.3 (5x), 3.0 (6x), 3.7 (6x), 4.0 (4x), 4.3 (6x), 4.7 (4x), 5.0 (7x).<br>1. Calculate Mean and Mode.<br>2. Draw a Boxplot (Quartiles, IQR)."
        },
        "solution": {
            "de": r"**Lösung 1A:**<br>A $\Leftrightarrow$ V2 (Asymmetrisch, viele Ausreißer)<br>B $\Leftrightarrow$ V3 (Glockenkurve)<br>C $\Leftrightarrow$ V1 (S-Kurve)<br>D $\Leftrightarrow$ V4 (QQ-Plot abweichend von Gerade an Rändern)<br><br>**Lösung 1B:**<br>1. Mittelwert = 3.79, Modus = 5.0 (7 Nennungen)<br>2. 25% Quartil = 3.0, Median = 4.0, 75% Quartil = 4.7. IQA = 1.7.",
            "en": r"**Solution 1A:**<br>A $\Leftrightarrow$ V2 (Asymmetric, outliers)<br>B $\Leftrightarrow$ V3 (Bell curve)<br>C $\Leftrightarrow$ V1 (S-curve)<br>D $\Leftrightarrow$ V4 (QQ-plot deviates at tails)<br><br>**Solution 1B:**<br>1. Mean = 3.79, Mode = 5.0 (7 counts)<br>2. 25% Quartile = 3.0, Median = 4.0, 75% Quartile = 4.7. IQR = 1.7."
        }
    },
    "hs2023_mc4": {
        "source": "HS 2023 Januar, MC #4",
        "question": {
            "de": r"Gegeben sei eine Zufallsvariable $Y$ mit einer Wahrscheinlichkeitsdichtefunktion $f_Y(y) = 2y$ für $0 \le y \le 1$, 0 sonst. Wie gross ist die Varianz von $Y$?",
            "en": r"Given a random variable $Y$ with probability density function $f_Y(y) = 2y$ for $0 \le y \le 1$, 0 otherwise. What is the variance of $Y$?"
        },
        "options": [r"$\frac{1}{3}$", r"$\frac{1}{18}$", r"$\frac{1}{6}$", r"$\frac{2}{9}$"],
        "correct_idx": 1,
        "solution": {
            "de": r"**Richtig: $\frac{1}{18}$**<br>$E[Y] = \int_0^1 2y^2 \, dy = \frac{2}{3}$.<br>$E[Y^2] = \int_0^1 2y^3 \, dy = \frac{1}{2}$.<br>$\text{Var}(Y) = E[Y^2] - E[Y]^2 = \frac{1}{2} - \frac{4}{9} = \frac{1}{18}$.",
            "en": r"**Correct: $\frac{1}{18}$**<br>$E[Y] = \int_0^1 2y^2 \, dy = \frac{2}{3}$.<br>$E[Y^2] = \int_0^1 2y^3 \, dy = \frac{1}{2}$.<br>$\text{Var}(Y) = E[Y^2] - E[Y]^2 = \frac{1}{2} - \frac{4}{9} = \frac{1}{18}$."
        }
    },
    "test3_q3": {
        "source": "Test 3, Frage 3",
        "question": {
            "de": r"$\text{Var}(3X + Y) = ?$ bei $\text{Corr}(X,Y) = -1$, $\text{Var}(X) = 1$, $\sigma_Y = 2$",
            "en": r"$\text{Var}(3X + Y) = ?$ given $\text{Corr}(X,Y) = -1$, $\text{Var}(X) = 1$, $\sigma_Y = 2$"
        },
        "options": [r"$13$", r"$5$", r"$4$", r"$1$"],
        "correct_idx": 3,
        "solution": {
            "de": r"**Richtig: $1$**<br>$\text{Var}(3X+Y) = 9 \cdot \text{Var}(X) + \text{Var}(Y) + 2 \cdot 3 \cdot 1 \cdot (-1) \cdot \sigma_X \cdot \sigma_Y$<br>$= 9 + 4 - 12 = 1$.",
            "en": r"**Correct: $1$**<br>$\text{Var}(3X+Y) = 9 \cdot \text{Var}(X) + \text{Var}(Y) + 2 \cdot 3 \cdot 1 \cdot (-1) \cdot \sigma_X \cdot \sigma_Y$<br>$= 9 + 4 - 12 = 1$."
        }
    },
    "hs2023_mc9": {
        "source": "HS 2023 Januar, MC #9",
        "question": {
            "de": r"Seien $X$ und $Y$ zwei Zufallsvariablen mit Verteilungen $X \sim N(4, 4)$ und $Y \sim N(0, 9)$. Des Weiteren gilt $E[XY] = E[X]E[Y]$. Sei $Z$ eine Zufallsvariable welche als $Z = 3 + 2X - 3Y$ definiert ist. Wie lautet die Kovarianz $\text{Cov}(Y, Z)$?",
            "en": r"Let $X$ and $Y$ be two random variables with distributions $X \sim N(4, 4)$ and $Y \sim N(0, 9)$. Furthermore $E[XY] = E[X]E[Y]$. Let $Z = 3 + 2X - 3Y$. What is $\text{Cov}(Y, Z)$?"
        },
        "options": [r"$-27$", r"$-9$", r"$0$", r"$27$"],
        "correct_idx": 0,
        "solution": {
            "de": r"**Richtig: $-27$**<br>$E[XY] = E[X]E[Y] \Rightarrow \text{Cov}(X,Y) = 0$.<br>$\text{Cov}(Y, Z) = \text{Cov}(Y, 3 + 2X - 3Y) = 2 \cdot \text{Cov}(Y,X) - 3 \cdot \text{Var}(Y)$<br>$= 0 - 3 \cdot 9 = -27$.",
            "en": r"**Correct: $-27$**<br>$E[XY] = E[X]E[Y] \Rightarrow \text{Cov}(X,Y) = 0$.<br>$\text{Cov}(Y, Z) = \text{Cov}(Y, 3 + 2X - 3Y) = 2 \cdot \text{Cov}(Y,X) - 3 \cdot \text{Var}(Y)$<br>$= 0 - 3 \cdot 9 = -27$."
        }
    }
}


# 6. Zentraler Grenzwertsatz
QUESTIONS_6 = {
    "uebung4_prob1": {
        "source": "Übung 4, Problem 1",
        "type": "problem",
        "question": {
            "de": r"$100'000$ Chips. Stichprobe $n=400$. Annahme wenn $\le 44$ defekt. Ablehnung wenn $\ge 51$. Totalkontrolle sonst. Wahre Fehlerrate $10\%$. Berechnen Sie die Wahrscheinlichkeiten.",
            "en": r"$100'000$ chips. Sample $n=400$. Accept if $\le 44$ defective. Reject if $\ge 51$. Total check otherwise. True defect rate $10\%$. Calculate probabilities."
        },
        "solution": {
            "de": r"**Lösung:**<br>1) Annahme: $P(X \le 44) \approx \mathbf{0.7434}$<br>2) Ablehnung: $P(X \ge 51) \approx \mathbf{0.040}$<br>3) Totalkontrolle: Rest $\approx \mathbf{0.1866}$",
            "en": r"**Solution:**<br>1) Accept: $P(X \le 44) \approx \mathbf{0.7434}$<br>2) Reject: $P(X \ge 51) \approx \mathbf{0.040}$<br>3) Total check: Rest $\approx \mathbf{0.1866}$"
        }
    },
    "hs2023_mc2": {
        "source": "HS 2023 Januar, MC #2",
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
            "de": r"**Richtig: (c) ist FALSCH**<br>Die Summe zweier Gleichverteilungen ist eine Dreiecksverteilung. Die Masse konzentriert sich um 0. $P(\bar{X} < -0.5) = 0.125 \neq 0.25$.",
            "en": r"**Correct: (c) is FALSE**<br>Sum of two uniforms is triangular. Mass concentrates around 0. $P(\bar{X} < -0.5) = 0.125 \neq 0.25$."
        }
    },
    "hs2023_mc3": {
        "source": "HS 2023 Januar, MC #3",
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
            "de": r"**Richtig: (a)**<br>Puffer = 40. $z \approx 2.88$ (für 0.002). $40 = 2.88 \cdot \sqrt{30000}\sigma$. $\sigma \approx 0.08 \Rightarrow \sigma^2 = 0.0064$.",
            "en": r"**Correct: (a)**<br>Buffer = 40. $z \approx 2.88$ (for 0.002). $40 = 2.88 \cdot \sqrt{30000}\sigma$. $\sigma \approx 0.08 \Rightarrow \sigma^2 = 0.0064$."
        }
    },
    "hs2022_mc3": {
        "source": "HS 2022 Januar, MC #3",
        "type": "mc",
        "question": {
            "de": r"$X_i \sim U[0,1]$ i.i.d., $N=100$. Wahrscheinlichkeit, dass Mittelwert $> 0.55$ ist?",
            "en": r"$X_i \sim U[0,1]$ i.i.d., $N=100$. Probability that mean $> 0.55$?"
        },
        "options": ["4.2%", "1.2%", "3.3%", "3.1%"],
        "correct_idx": 0,
        "solution": {
            "de": r"**Richtig: 4.2%**<br>$\mu=0.5, \sigma^2=1/12$.<br>Standardfehler $SE = \sqrt{\frac{1/12}{100}} \approx 0.0289$.<br>$Z = \frac{0.55 - 0.5}{0.0289} \approx 1.73$.<br>$P(Z > 1.73) \approx 0.042$.",
            "en": r"**Correct: 4.2%**<br>$\mu=0.5, \sigma^2=1/12$.<br>Standard Error $SE = \sqrt{\frac{1/12}{100}} \approx 0.0289$.<br>$Z = \frac{0.55 - 0.5}{0.0289} \approx 1.73$.<br>$P(Z > 1.73) \approx 0.042$."
        }
    },
    "hs2022_mc10": {
        "source": "HS 2022 Januar, MC #10",
        "type": "mc",
        "question": {
            "de": r"Cheating Detection: $n=1000$ Züge. Starker Spieler findet Top-Move mit $p=0.3$. Ban wenn $\ge 340$ Top-Moves. P(False Ban)?",
            "en": r"Cheating Detection: $n=1000$ moves. Strong player matches top move $p=0.3$. Ban if $\ge 340$ matches. P(False Ban)?"
        },
        "options": ["0.1%", "0.3%", "0.5%", "0.7%"],
        "correct_idx": 1,
        "solution": {
            "de": r"**Richtig: 0.3%**<br>$\mu = 300, \sigma = \sqrt{1000 \cdot 0.3 \cdot 0.7} \approx 14.5$.<br>$Z = \frac{340-300}{14.5} \approx 2.76$.<br>$P(Z > 2.76) \approx 0.003$.",
            "en": r"**Correct: 0.3%**<br>$\mu = 300, \sigma = \sqrt{1000 \cdot 0.3 \cdot 0.7} \approx 14.5$.<br>$Z = \frac{340-300}{14.5} \approx 2.76$.<br>$P(Z > 2.76) \approx 0.003$."
        }
    }
}

# 8. Punktschätzung
QUESTIONS_8 = {
    "uebung5_prob1": {
        "source": "Übung 5, Problem 1",
        "type": "problem",
        "question": {
            "de": r"Schätzer für $\mu$:<br>1) $(X_1+X_2)/2$<br>2) $X_1/3 + 2X_2/3$<br>Welcher ist effizienter?",
            "en": r"Estimators for $\mu$:<br>1) $(X_1+X_2)/2$<br>2) $X_1/3 + 2X_2/3$<br>Which is more efficient?"
        },
        "solution": {
            "de": r"**Lösung:** Schätzer 1 ist effizienter (kleinere Varianz: $Var/2$ vs $5Var/9$).",
            "en": r"**Solution:** Estimator 1 is more efficient (lower variance: $Var/2$ vs $5Var/9$)."
        }
    },
    "hs2022_mc8": {
        "source": "HS 2022 Januar, MC #8",
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
            "de": r"**Richtig: (b)**<br>MLE für $U[0,b]$ ist das Maximum der Stichprobe: $\max(x_i) = 5.2$.",
            "en": r"**Correct: (b)**<br>MLE for $U[0,b]$ is the sample maximum: $\max(x_i) = 5.2$."
        }
    },
    "uebung5_prob7": {
        "source": "Übung 5, Problem 7",
        "type": "problem",
        "question": {
            "de": r"Poisson $X$, $\mu=\lambda$. ML-Schätzer für $\lambda$?",
            "en": r"Poisson $X$, $\mu=\lambda$. ML estimator for $\lambda$?"
        },
        "solution": {
            "de": "**Lösung:** Das arithmetische Mittel (Sample Mean).",
            "en": "**Solution:** The arithmetic mean (sample mean)."
        }
    },
    "uebung5_prob2": {
        "source": "Übung 5, Problem 2",
        "type": "problem",
        "question": {
            "de": r"$n=100$, $\bar{x}=10$, $\sigma=2$ known. $95\%$ KI für $\mu$?",
            "en": r"$n=100$, $\bar{x}=10$, $\sigma=2$ known. $95\%$ CI for $\mu$?"
        },
        "solution": {
            "de": r"**Lösung:** $10 \pm 1.96 \cdot 2/10 = [9.608, 10.392]$",
            "en": r"**Solution:** $10 \pm 1.96 \cdot 2/10 = [9.608, 10.392]$"
        }
    },
    "uebung5_prob4": {
        "source": "Übung 5, Problem 4",
        "type": "problem",
        "question": {
            "de": r"Anteil $p$. $n=400$, $k=80$ ($20\%$). $95\%$ KI für $p$?",
            "en": r"Proportion $p$. $n=400$, $k=80$ ($20\%$). $95\%$ CI for $p$?"
        },
        "solution": {
            "de": r"**Lösung:** $0.2 \pm 1.96 \cdot \sqrt{0.2 \cdot 0.8/400} = 0.2 \pm 0.0392 = [0.1608, 0.2392]$",
            "en": r"**Solution:** $0.2 \pm 1.96 \cdot \sqrt{0.2 \cdot 0.8/400} = 0.2 \pm 0.0392 = [0.1608, 0.2392]$"
        }
    },
    "hs2022_mc8": {
        "source": "HS 2022 Januar, MC #8",
        "question": {
            "de": r"Sie beobachten eine auf dem Intervall $[0, b]$ gleichverteilte Zufallsvariable $X$. Beobachtungen: $\{1.1, 3.8, 4.2, 0.5, 5.2\}$. Wie lautet der Maximum-Likelihood-Schätzer für $b$?",
            "en": r"You observe a uniformly distributed random variable $X$ on $[0, b]$. Observations: $\{1.1, 3.8, 4.2, 0.5, 5.2\}$. What is the maximum likelihood estimator for $b$?"
        },
        "options": ["4.2", "5.2", "2.96", "5.0"],
        "correct_idx": 1,
        "solution": {
            "de": r"**Richtig: 5.2**<br>Die Likelihood $L(b) = \frac{1}{b^n}$ ist fallend in $b$.<br>Aber alle $x_i$ müssen $\le b$ sein.<br>Das kleinste erlaubte $b = \max\{x_i\} = 5.2$.",
            "en": r"**Correct: 5.2**<br>The likelihood $L(b) = \frac{1}{b^n}$ is decreasing in $b$.<br>But all $x_i$ must be $\le b$.<br>The smallest allowed $b = \max\{x_i\} = 5.2$."
        }
    },
    "hs2023_mc10": {
        "source": "HS 2023 Januar, MC #10",
        "question": {
            "de": r"Sei $x_1, x_2, \ldots, x_n$ eine Stichprobe unabhängiger und identischer I.I.D Zufallsvariablen $X$. Welcher der folgenden Schätzer des Erwartungswerts von $X$ ist erwartungstreu?",
            "en": r"Let $x_1, x_2, \ldots, x_n$ be a sample of i.i.d. random variables $X$. Which of the following estimators of the expected value of $X$ is unbiased?"
        },
        "options": [{"de": r"$x_1$", "en": r"$x_1$"}, {"de": r"$\frac{x_1 + x_n}{3}$", "en": r"$\frac{x_1 + x_n}{3}$"}, {"de": r"$x_1^2$", "en": r"$x_1^2$"}, {"de": r"$\frac{\bar{x}}{2}$", "en": r"$\frac{\bar{x}}{2}$"}],
        "correct_idx": 0,
        "solution": {
            "de": r"**Richtig: $x_1$**<br>$E[x_1] = E[X] = \mu$.<br>Alle anderen Schätzer sind entweder gewichtet oder nichtlinear und führen zu Bias.",
            "en": r"**Correct: $x_1$**<br>$E[x_1] = E[X] = \mu$.<br>All other estimators are either weighted or nonlinear and lead to bias."
        }
    },
    "hs2015_mc10": {
        "source": "HS 2015 Januar, MC #10 (4 Punkte)",
        "type": "mc",
        "question": {
            "de": r"Für $\theta > 1$ sei $X_1, X_2, \ldots, X_n$ eine unabhängige Folge in $[1, \theta]$ gleichverteilter Zufallsvariablen. Wir betrachten den Schätzer $\hat{\theta} = \frac{2}{n} \sum x_i$ für den Parameter $\theta$. Welche der folgenden Aussagen über $\hat{\theta}$ trifft zu?",
            "en": r"For $\theta > 1$, let $X_1, X_2, \ldots, X_n$ be i.i.d. uniformly distributed on $[1, \theta]$. We consider the estimator $\hat{\theta} = \frac{2}{n} \sum x_i$ for $\theta$. Which statement about $\hat{\theta}$ is true?"
        },
        "options": [
            {"de": r"Die Varianz des Schätzers ist $\frac{(\theta-1)^2}{3n}$.", "en": r"The variance of the estimator is $\frac{(\theta-1)^2}{3n}$."},
            {"de": r"Der Schätzer ist erwartungstreu, aber nicht konsistent.", "en": r"The estimator is unbiased but not consistent."},
            {"de": r"Der Schätzer ist konsistent, aber nicht erwartungstreu.", "en": r"The estimator is consistent but not unbiased."},
            {"de": r"Der Bias des Schätzers ist $\frac{\theta}{3n}$.", "en": r"The bias of the estimator is $\frac{\theta}{3n}$."}
        ],
        "correct_idx": 0,
        "solution": {
            "de": r"**Richtig: (a)**<br>$\text{Var}(X) = \frac{(\theta-1)^2}{12}$.<br>$\text{Var}(\hat{\theta}) = (\frac{2}{n})^2 \cdot n \cdot \text{Var}(X) = \frac{4}{n} \cdot \frac{(\theta-1)^2}{12} = \frac{(\theta-1)^2}{3n}$.",
            "en": r"**Correct: (a)**<br>$\text{Var}(X) = \frac{(\theta-1)^2}{12}$.<br>$\text{Var}(\hat{\theta}) = (\frac{2}{n})^2 \cdot n \cdot \text{Var}(X) = \frac{4}{n} \cdot \frac{(\theta-1)^2}{12} = \frac{(\theta-1)^2}{3n}$."
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
            "de": r"**Lösung:**<br>1. $\hat{\alpha}_{MLE} = \frac{n}{\sum \ln x_i}$.<br>2. $\hat{\alpha} \approx 0.35$. (Achtung: Dichte braucht $\alpha > 0$.)<br>3. $E[X] = \frac{\alpha}{\alpha-1}$. Auflösen nach $\alpha$: $\hat{\alpha}_{MM} = \frac{\bar{x}}{\bar{x}-1}$.<br>4. $\bar{x}=17.8 \Rightarrow \hat{\alpha} \approx 1.06$.<br>5. Momentenmethode nur für $\alpha > 1$ definiert.",
            "en": r"**Solution:**<br>1. $\hat{\alpha}_{MLE} = \frac{n}{\sum \ln x_i}$.<br>2. $\hat{\alpha} \approx 0.35$. (Note: Density needs $\alpha > 0$.)<br>3. $E[X] = \frac{\alpha}{\alpha-1}$. Solve for $\alpha$: $\hat{\alpha}_{MM} = \frac{\bar{x}}{\bar{x}-1}$.<br>4. $\bar{x}=17.8 \Rightarrow \hat{\alpha} \approx 1.06$.<br>5. Method of Moments only defined for $\alpha > 1$."
        }
    },
}

# 9. Konfidenzintervalle (Confidence Intervals)
QUESTIONS_9 = {
    "hs2023_mc5": {
        "source": "HS 2023 Januar, MC #5",
        "question": {
            "de": r"Im Auftrag eines Großhandlers müssen Konfidenzintervalle für die durchschnittliche Füllmenge eines Abfüllsystems für $500$ ml Bierflaschen bestimmt werden. Die Abfüllmenge $X$ ist mit einer Varianz von $10$ ml Normalverteilt. Zehn Flaschen: $\{501, 495, 503, 498, 500, 498, 497, 503, 497, 501\}$. Wie lautet das korrekte symmetrische $95\%$ Konfidenzintervall?",
            "en": r"A wholesaler needs confidence intervals for the average fill volume of a $500$ ml beer bottle filling system. Fill volume $X$ is normally distributed with variance $10$ ml. Ten bottles: $\{501, 495, 503, 498, 500, 498, 497, 503, 497, 501\}$. What is the correct symmetric $95\%$ confidence interval?"
        },
        "options": [r"$[495.0, 503.6]$", r"$[496.5, 502.1]$", r"$[498.0, 500.6]$", r"$[497.34, 501.26]$"],
        "correct_idx": 3,
        "solution": {
            "de": r"**Richtig: $[497.34, 501.26]$**<br>$\bar{x} = 499.3$, $\sigma = \sqrt{10} \approx 3.16$, $n = 10$.<br>KI = $\bar{x} \pm z_{0.975} \cdot \sigma/\sqrt{n} = 499.3 \pm 1.96 \cdot (3.16/\sqrt{10}) \approx 499.3 \pm 1.96$.",
            "en": r"**Correct: $[497.34, 501.26]$**<br>$\bar{x} = 499.3$, $\sigma = \sqrt{10} \approx 3.16$, $n = 10$.<br>CI = $\bar{x} \pm z_{0.975} \cdot \sigma/\sqrt{n} = 499.3 \pm 1.96 \cdot (3.16/\sqrt{10}) \approx 499.3 \pm 1.96$."
        }
    }
}

# 10. Hypothesentests


QUESTIONS_10_5 = {
    "hs2024_mc1": {
        "source": "HS 2024 Januar, MC #1",
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
            "de": r"**Richtig: (b)**<br>Standardfehler $SE = \sqrt{0.5/25} \approx 0.1414$.<br>Kritischer Wert (einseitig 5%): $z = 1.645$.<br>Grenze: $\mu_0 + 1.645 \cdot SE = 0.5 + 0.232 = 0.732$.",
            "en": r"**Correct: (b)**<br>Standard Error $SE = \sqrt{0.5/25} \approx 0.1414$.<br>Critical value (one-sided 5%): $z = 1.645$.<br>Limit: $\mu_0 + 1.645 \cdot SE = 0.5 + 0.232 = 0.732$."
        }
    },
    "hs2024_mc8": {
        "source": "HS 2024 Januar, MC #8",
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
            "de": r"**Richtig: (b)**<br>Teststatistik $Z = \frac{4.95 - 8}{\sqrt{5}/\sqrt{5}} = -3.05$.<br>p-Wert (zweiseitig) = $2 \cdot P(Z < -3.05) \approx 2 \cdot 0.0011 = 0.0022$.",
            "en": r"**Correct: (b)**<br>Test Statistic $Z = \frac{4.95 - 8}{\sqrt{5}/\sqrt{5}} = -3.05$.<br>p-value (two-sided) = $2 \cdot P(Z < -3.05) \approx 2 \cdot 0.0011 = 0.0022$."
        }
    }
}


QUESTIONS_10 = {
    "uebung6_prob1": {
        "source": "Übung 6, Problem 1",
        "type": "problem",
        "question": {
            "de": r"$\bar{x} = 218$. $H_0: \mu=210$. $n=225$ ($\sigma^2$ bekannt -> Z-Test).",
            "en": r"$\bar{x} = 218$. $H_0: \mu=210$. $n=225$ ($\sigma^2$ known -> Z-test)."
        },
        "solution": {
            "de": r"**Lösung:** $Z = 1.6$. Bei $5\%$ Level ($1.645$) NICHT verwerfen.",
            "en": r"**Solution:** $Z = 1.6$. Do NOT reject at $5\%$ level ($1.645$ critical value)."
        }
    },
    "uebung6_prob4": {
        "source": "Übung 6, Problem 4",
        "type": "problem",
        "question": {
            "de": r"t-Test. $n=16$, $\bar{x}=10$, $s=2$. $H_0: \mu=12$. Teststatistik?",
            "en": r"t-Test. $n=16$, $\bar{x}=10$, $s=2$. $H_0: \mu=12$. Test statistic?"
        },
        "solution": {
            "de": r"**Lösung:** $t = (10-12)/(2/4) = -4$. Verwerfen.",
            "en": r"**Solution:** $t = (10-12)/(2/4) = -4$. Reject."
        }
    },
    "uebung6_prob8": {
        "source": "Übung 6, Problem 8",
        "type": "problem",
        "question": {
            "de": r"$p$-Wert $= 0.03$. $\alpha = 0.05$. Entscheidung?",
            "en": r"$p$-value $= 0.03$. $\alpha = 0.05$. Decision?"
        },
        "solution": {
            "de": r"**Lösung:** $H_0$ verwerfen (da $p < \alpha$).",
            "en": r"**Solution:** Reject $H_0$ (since $p < \alpha$)."
        }
    }
}


# 8. Punktschätzung (Point Estimation)
QUESTIONS_8_4 = {
    "uebung5_mc1": {
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
            "de": r"**Richtig: Falsch**<br>Erwartungstreue ($E[\hat{\theta}] = \theta$) hat nichts mit Symmetrie zu tun.",
            "en": r"**Correct: False**<br>Unbiasedness ($E[\hat{\theta}] = \theta$) implies nothing about symmetry."
        }
    },
    "uebung5_mc2": {
        "source": "Übung 5, MC #2",
        "type": "mc",
        "question": {
            "de": r"Effiziente Schätzungen sind im Vorlesungskontext immer auch erwartungstreu.",
            "en": r"Efficient estimators are always unbiased (in lecture context)."
        },
        "options": [
            r"Richtig",
            r"Falsch"
        ],
        "correct_idx": 0,
        "solution": {
            "de": r"**Richtig: Richtig**<br>Effizienz bezieht sich auf MVUE (Minimum Variance Unbiased Estimator).",
            "en": r"**Correct: True**<br>Efficiency refers to MVUE (Minimum Variance Unbiased Estimator)."
        }
    },
    "uebung5_mc3": {
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
            "de": r"**Richtig: Falsch**<br>Beispiel: $X_1$ (nur erster Wert) ist erwartungstreu aber nicht konsistent (Varianz sinkt nicht).",
            "en": r"**Correct: False**<br>Example: $X_1$ (first value only) is unbiased but not consistent (variance doesn't shrink)."
        }
    },
    "uebung5_mc4": {
        "source": "Übung 5, MC #4",
        "type": "mc",
        "question": {
            "de": r"Schätzer sind Zufallsvariablen.",
            "en": r"Estimators are random variables."
        },
        "options": [
             r"Richtig",
             r"Falsch"
        ],
        "correct_idx": 0,
        "solution": {
             "de": r"**Richtig: Richtig**<br>Sie hängen von der zufälligen Stichprobe ab.",
             "en": r"**Correct: True**<br>They depend on the random sample."
        }
    },
    "uebung5_mc5": {
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
             "de": r"**Richtig: Falsch**<br>$MSE = Var + Bias^2$. Ein kleiner Bias kann Varianz massiv senken (Bias-Variance Tradeoff).",
             "en": r"**Correct: False**<br>$MSE = Var + Bias^2$. Small bias can trade for huge variance reduction."
        }
    },
    "uebung5_mc6": {
        "source": "Übung 5, MC #6",
        "type": "mc",
        "question": {
            "de": r"$\bar{X}$. Welche Aussagen sind richtig?<br>(a) $Var(\bar{X}) = \sigma^2/n$.<br>(b) $\bar{X}$ konsistent.<br>(c) $\bar{X}$ standardnormalverteilt.",
            "en": r"$\bar{X}$. True?<br>(a) $Var(\bar{X}) = \sigma^2/n$.<br>(b) Consistent.<br>(c) Standard Normal."
        },
        "options": [
             r"a) und b)",
             r"b) und c)",
             r"a) und c)",
             r"Nur a)"
        ],
        "correct_idx": 0,
        "solution": {
             "de": r"**Richtig: (a), (b)**<br>(c) ist falsch, sie ist normal ($N(\mu, \dots)$) aber nicht Standardnormal ($N(0,1)$).",
             "en": r"**Correct: (a), (b)**<br>(c) is false, it's Normal ($N(\mu, \dots)$) but not Standard Normal ($N(0,1)$)."
        }
    },
    "uebung5_mc10": {
        "source": "Übung 5, MC #10",
        "type": "mc",
        "question": {
            "de": r"Wann ist ein linearer Schätzer $\sum w_i X_i$ erwartungstreu?",
            "en": r"When is a linear estimator $\sum w_i X_i$ unbiased?"
        },
        "options": [
             r"Immer.",
             r"Wenn $\sum w_i = 0$.",
             r"Wenn $\sum w_i = 1$.",
             r"Wenn $w_i = 1/n$."
        ],
        "correct_idx": 2, 
        "solution": {
             "de": r"**Richtig: Summe Gewichte = 1.**",
             "en": r"**Correct: Sum of weights = 1.**"
        }
    },
    "uebung5_mc11": {
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
             "de": r"**Richtig: (c)**<br>Gleichsetzen $\bar{X} = \frac{1}{3+\lambda}$ und nach $\lambda$ auflösen.",
             "en": r"**Correct: (c)**<br>Equate $\bar{X} = \frac{1}{3+\lambda}$ and solve for $\lambda$."
        }
    },
    "uebung5_mc12": {
        "source": "Übung 5, MC #12",
        "type": "mc",
        "question": {
            "de": r"Momentenmethode und MLE liefern stets gleiche Ergebnisse?",
            "en": r"MOM and MLE always yield same results?"
        },
        "options": [
             r"Richtig",
             r"Falsch"
        ],
        "correct_idx": 1,
        "solution": {
             "de": r"**Richtig: Falsch**<br>Gegenbeispiel: Gleichverteilung (MOM: $2\bar{X}$, MLE: $\max X_i$).",
             "en": r"**Correct: False**<br>Counter-example: Uniform (MOM: $2\bar{X}$, MLE: $\max X_i$)."
        }
    },
    "uebung5_mc13": {
        "source": "Übung 5, MC #13",
        "type": "mc",
        "question": {
            "de": r"MLE sind nie erwartungstreu?",
            "en": r"MLE are never unbiased?"
        },
        "options": [
             r"Richtig",
             r"Falsch"
        ],
        "correct_idx": 1,
        "solution": {
             "de": r"**Richtig: Falsch**<br>$\bar{X}$ bei Normalverteilung ist MLE und erwartungstreu.",
             "en": r"**Correct: False**<br>$\bar{X}$ in Normal dist is MLE and unbiased."
        }
    },
    "uebung5_prob1": {
        "source": "Übung 5, Probe #1",
        "type": "problem",
        "question": {
            "de": r"Vergleich $\mu_1 = 0.5 X_1 + 0.5 X_2$ vs $\mu_2 = \frac{1}{3}X_1 + \frac{2}{3}X_2$. Effizienter?",
            "en": r"Compare $\mu_1 = 0.5 X_1 + 0.5 X_2$ vs $\mu_2 = \frac{1}{3}X_1 + \frac{2}{3}X_2$. More efficient?"
        },
        "options": [
             r"$\mu_1$",
             r"$\mu_2$",
             r"Beide gleich"
        ],
        "correct_idx": 0,
        "solution": {
             "de": r"**Richtig: $\mu_1$**<br>Summe Quadrate der Gewichte: $\mu_1 \to 0.5$, $\mu_2 \to 0.55$. Kleiner ist besser.",
             "en": r"**Correct: $\mu_1$**<br>Sum of squared weights: $\mu_1 \to 0.5$, $\mu_2 \to 0.55$. Smaller is better."
        }
    },
    "test5_mc3": {
        "source": "Test 5, Q3",
        "type": "mc",
        "question": {
            "de": r"$X_i \sim U[1, \theta]$. Schätzer $\hat{\theta} = \frac{2}{n}\sum X_i$.",
            "en": r"$X_i \sim U[1, \theta]$. Est $\hat{\theta} = \frac{2}{n}\sum X_i$."
        },
        "options": [r"Varianz ist $\frac{(\theta-1)^2}{3n}$", r"Erwartungstreu", r"Konsistent", r"Bias ..."],
        "correct_idx": 0,
        "solution": {
            "de": r"**Richtig: (a)**<br>$Var(2\bar{X}) = 4 Var(\bar{X}) = 4 \frac{(\theta-1)^2/12}{n} = \frac{(\theta-1)^2}{3n}$.",
            "en": r"**Correct: (a)**<br>$Var(2\bar{X}) = 4 Var(\bar{X}) = 4 \frac{(\theta-1)^2/12}{n} = \frac{(\theta-1)^2}{3n}$."
        }
    },
    "uebung5_mc7": {
        "source": "Übung 5, MC #7",
        "type": "mc",
        "question": {
            "de": r"Systematischer Fehler beim Schätzen heißt Bias.",
            "en": r"Systematic error in estimation is called Bias."
        },
        "options": [r"Richtig", r"Falsch"],
        "correct_idx": 0,
        "solution": {
            "de": r"**Richtig: (a)**<br>$Bias = E[\hat{\theta}] - \theta$.",
            "en": r"**Correct: (a)**<br>$Bias = E[\hat{\theta}] - \theta$."
        }
    },
    "uebung5_mc8": {
        "source": "Übung 5, MC #8",
        "type": "mc",
        "question": {
            "de": r"Ein Schätzer ist positiv verzerrt (Bias > 0). Überschätzt oder unterschätzt er im Mittel?",
            "en": r"Positive bias (Bias > 0). Does it over- or underestimate on average?"
        },
        "options": [r"Überschätzt", r"Unterschätzt"],
        "correct_idx": 0,
        "solution": {
            "de": r"**Richtig: (a)**<br>$E[\hat{\theta}] > \theta$.",
            "en": r"**Correct: (a)**<br>$E[\hat{\theta}] > \theta$."
        }
    },
    "uebung5_mc9": {
        "source": "Übung 5, MC #9",
        "type": "mc",
        "question": {
            "de": r"Wichtigstes Ziel beim Schätzen ist es, Schätzer mit kleinen Varianzen zu finden.",
            "en": r"Main goal is finding estimators with small variances."
        },
        "options": [r"Richtig", r"Falsch"],
        "correct_idx": 1,
        "solution": {
            "de": r"**Richtig: (b)**<br>Wir wollen kleinen MSE (Varianz + Bias).",
            "en": r"**Correct: (b)**<br>We want small MSE (Variance + Bias)."
        }
    },
    "uebung5_mc14": {
        "source": "Übung 5, MC #14",
        "type": "mc",
        "question": {
            "de": r"Maximierung der Loglikelihood und Likelihood führt zum selben Ergebnis (Schätzer).",
            "en": r"Maximizing Loglikelihood vs Likelihood yields the same estimator."
        },
        "options": [r"Richtig", r"Falsch"],
        "correct_idx": 0,
        "solution": {
            "de": r"**Richtig: (a)**<br>Log ist monoton steigend. Maximum ist an der gleichen Stelle.",
            "en": r"**Correct: (a)**<br>Log is monotonic. Max location is identical."
        }
    },
    "uebung5_mc15": {
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
            "de": r"**Richtig: (c)**<br>Produkt der Dichten: $f(1)f(2)f(3)f(1)$.",
            "en": r"**Correct: (c)**<br>Product of densities: $f(1)f(2)f(3)f(1)$."
        }
    },
    "uebung5_prob3": {
        "source": "Übung 5, Probe #3",
        "type": "problem",
        "question": {
            "de": r"Rechteckverteilung $[\theta, \theta+1]$.<br>(a) $E[X]$, $Var[X]$.<br>(b) Bias von $\bar{X}$?",
            "en": r"Uniform $[\theta, \theta+1]$. (a) Moments. (b) Bias of mean?"
        },
        "solution": {
            "de": r"**Lösung:**<br>(a) $E[X] = \theta+0.5$.<br>(b) $Bias = 0.5$. Korrektur: $\bar{X}-0.5$.",
            "en": r"**Solution:**<br>(a) $E[X] = \theta+0.5$.<br>(b) $Bias = 0.5$. Correction: $\bar{X}-0.5$."
        }
    },
    "uebung5_prob5": {
        "source": "Übung 5, Probe #5",
        "type": "problem",
        "question": {
            "de": r"Bernoulli $\pi$. Schätzer $\hat{\pi}$ vs Laplace Smoothing $T = \frac{\sum X + 1}{n+2}$.",
            "en": r"Bernoulli. MLE vs Laplace Smoothing."
        },
        "solution": {
            "de": r"**Lösung:** Laplace hat Bias, aber geringeren MSE bei kleinen Stichproben (Bias-Variance Tradeoff).",
            "en": r"**Solution:** Laplace has bias, but lower MSE for small samples (Bias-Variance Tradeoff)."
        }
    },
    "uebung5_prob6": {
        "source": "Übung 5, Probe #6",
        "type": "problem",
        "question": {
            "de": r"Momentenschätzer herleiten für:<br>(a) Exponential<br>(b) Rechteck $[\theta-0.5, \theta+0.5]$",
            "en": r"MOM for (a) Exp (b) Uniform."
        },
        "solution": {
            "de": r"**Lösung:**<br>(a) $E[X]=1/\lambda \implies \hat{\lambda} = 1/\bar{X}$.<br>(b) $E[X]=\theta \implies \hat{\theta} = \bar{X}$.",
            "en": r"**Solution:**<br>(a) $\hat{\lambda} = 1/\bar{X}$.<br>(b) $\hat{\theta} = \bar{X}$."
        }
    },
    "uebung5_prob8": {
        "source": "Übung 5, Probe #8",
        "type": "problem",
        "question": {
            "de": r"Binomial $B(n,p)$. n,p unbekannt. Momentenschätzer?",
            "en": r"Binomial $B(n,p)$. n,p unknown. MOM?"
        },
        "solution": {
            "de": r"**Lösung:** Zwei Gleichungen nötig.<br>1) $np = \bar{X}$<br>2) $np(1-p) = S^2$.<br>Lösen nach n und p.",
            "en": r"**Solution:** Two equations.<br>1) $np = \bar{X}$<br>2) $np(1-p) = S^2$."
        }
    }
}

# 9. Konfidenzintervalle (Confidence Intervals)
QUESTIONS_9_4 = {
    "uebung5_mc16": {
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
             "de": r"**Richtig: Niveau größer -> Intervall größer**<br>Mehr Sicherheit braucht breiteres Netz.",
             "en": r"**Correct: Higher level -> Wider interval**<br>More confidence needs wider net."
        }
    },
    "uebung5_mc17": {
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
             "de": r"**Richtig: Richtig**<br>Sie hängen von der Stichprobe ab. Der Parameter ist fest.",
             "en": r"**Correct: True**<br>They depend on the sample. The parameter is fixed."
        }
    },
    "uebung5_mc18": {
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
             "de": r"**Richtig: Falsch**<br>Hängt von Varianz ab, nicht vom Mittelwert.",
             "en": r"**Correct: False**<br>Depends on variance, not mean."
        }
    },
    "uebung5_prob9": {
        "source": "Übung 5, Probe #9",
        "type": "problem",
        "question": {
             "de": r"$n=300, \sigma=5, \bar{x}=50$. 95% KI?",
             "en": r"$n=300, \sigma=5, \bar{x}=50$. 95% CI?"
        },
        "options": [
             r"$50 \pm 0.57$",
             r"$50 \pm 0.28$",
             r"$50 \pm 1.96$",
             r"$50 \pm 0.03$"
        ],
        "correct_idx": 0,
        "solution": {
             "de": r"**Richtig: $50 \pm 0.57$**<br>$1.96 \cdot 5 / \sqrt{300} \approx 0.565$.",
             "en": r"**Correct: $50 \pm 0.57$**<br>$1.96 \cdot 5 / \sqrt{300} \approx 0.565$."
        }
    },
    "test5_mc4": {
        "source": "Test 5, Q4",
        "type": "mc",
        "question": {
            "de": r"Normalverteilt $\mu=400, \sigma^2=25$ ($\sigma=5$). 95% Intervall?",
            "en": r"Normal $\mu=400, \sigma=5$. 95% interval?"
        },
        "options": [r"[391.8, 408.2]", r"[390.2, 409.8]", r"[393.6, 406.4]", r"[351.0, 449.0]"],
        "correct_idx": 1,
        "solution": {
            "de": r"**Richtig: [390.2, 409.8]**<br>$400 \pm 1.96(5) = 400 \pm 9.8$.",
            "en": r"**Correct: [390.2, 409.8]**<br>$400 \pm 1.96(5) = 400 \pm 9.8$."
        }
    }
}


# 10. Hypothesentests (Hypothesis Testing)
QUESTIONS_10_5 = {
    "uebung6_prob1": {
        "source": "Übung 6, Probe #1",
        "type": "problem",
        "question": {
             "de": r"Steak braten. $\mu \sim N(\mu, 225)$. $n=9, \bar{x}=218$. Teste $H_0: \mu = 210$ vs $\mu \ne 210$ ($\alpha=0.1$).",
             "en": r"Steak frying. $N(\mu, 225)$. $n=9, \bar{x}=218$. Test $H_0: \mu = 210$ vs $\mu \ne 210$ ($\alpha=0.1$)."
        },
        "options": [
             r"Verwerfen",
             r"Nicht verwerfen"
        ],
        "correct_idx": 1,
        "solution": {
             "de": r"**Richtig: Nicht verwerfen**<br>$Z = (218-210)/5 = 1.6$. Kritisch $1.645$. $|1.6| < 1.645$.",
             "en": r"**Correct: Do not reject**<br>$Z = (218-210)/5 = 1.6$. Critical $1.645$. $|1.6| < 1.645$."
        }
    },
    "uebung6_prob2": {
        "source": "Übung 6, Probe #2",
        "type": "problem",
        "question": {
             "de": r"Schrittlänge. $\sigma=0.2, n=7, \bar{x}=85.186$. Teste $H_0: \mu \le 85$ ($\alpha=0.01$).",
             "en": r"Step length. $\sigma=0.2, n=7, \bar{x}=85.186$. Test $H_0: \mu \le 85$ ($\alpha=0.01$)."
        },
        "options": [
             r"Verwerfen",
             r"Nicht verwerfen"
        ],
        "correct_idx": 0,
        "solution": {
             "de": r"**Richtig: Verwerfen**<br>$Z = 2.46$. Kritisch $2.33$. $2.46 > 2.33$.",
             "en": r"**Correct: Reject**<br>$Z = 2.46$. Critical $2.33$. $2.46 > 2.33$."
        }
    },
    "uebung6_prob3": {
        "source": "Übung 6, Probe #3",
        "type": "problem",
        "question": {
             "de": r"Internetsessions. $\bar{x}=140.5$. Ist Dauer signifikant < 148? ($\alpha=0.01$).",
             "en": r"Internet sessions. $\bar{x}=140.5$. Is duration sig. < 148? ($\alpha=0.01$)."
        },
        "options": [
             r"Ja (Verwerfen)",
             r"Nein (Nicht verwerfen)"
        ],
        "correct_idx": 0,
        "solution": {
             "de": r"**Richtig: Ja**<br>$Z = -2.39$. Kritisch $-2.33$. $-2.39 < -2.33$.",
             "en": r"**Correct: Yes**<br>$Z = -2.39$. Critical $-2.33$. $-2.39 < -2.33$."
        }
    },
    "uebung6_prob4": {
        "source": "Übung 6, Probe #4",
        "type": "problem",
        "question": {
             "de": r"Mobilfunk. $\bar{x}=0.91$. Nachweis Grenzwert 1.0 eingehalten (< 1.0)?",
             "en": r"Mobile radiation. $\bar{x}=0.91$. Proof limit 1.0 complied (< 1.0)?"
        },
        "options": [
             r"Ja",
             r"Nein"
        ],
        "correct_idx": 0,
        "solution": {
             "de": r"**Richtig: Ja**<br>$H_1: \mu < 1.0$. $Z = -2.58$. Kritisch -2.33. Signifikant.",
             "en": r"**Correct: Yes**<br>$H_1: \mu < 1.0$. $Z = -2.58$. Critical -2.33. Significant."
        }
    }
}

# 11. Fachübergreifende Aufgaben
QUESTIONS_11_1 = {}

# Additional Question Stubs
QUESTIONS_1_11 = {
    "hs2024_mc10": {
        "source": "HS 2024 Januar, MC #10",
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
            "de": r"**Richtig: (a)**<br>'Überlappungs-Penalty': Wenn Ruben (1,1) sucht und nach einer 1 eine 2 würfelt, muss er ganz von vorne anfangen. Wenn Jochen (1,2) nach einer 1 eine 1 würfelt, hat er immer noch den Anfang seiner Sequenz. Ruben braucht länger ($42$ Würfe vs $36$).",
            "en": r"**Correct: (a)**<br>'Overlap Penalty': If Ruben (targets 1,1) rolls a 2 after a 1, he restarts completely. If Jochen (targets 1,2) rolls a 1 after a 1, he keeps the start of his sequence. Ruben takes longer ($42$ throws vs $36$)."
        }
    },
    "test1_mc1": {
        "source": "Test 1, Q1",
        "type": "mc",
        "question": {
            "de": r"Statistik-Vorlesung: VWL (42m, 93w), BWL (78m, 87w). Eine Hörerin wird gewählt. Wahrscheinlichkeit, dass sie BWLerin ist?",
            "en": r"Stats class: Econ (42m, 93f), Bus (78m, 87f). A female student is chosen. Probability she is Business?"
        },
        "options": [r"0.31", r"0.29", r"0.71", r"0.48"],
        "correct_idx": 3,
        "solution": {
            "de": r"**Richtig: 0.48**<br>Bedingt auf Frauen: Total $93+87=180$. BWL-Frauen $87$. $P = 87/180 \approx 0.48$.",
            "en": r"**Correct: 0.48**<br>Conditioned on women: Total $93+87=180$. Bus-Women $87$. $P = 87/180 \approx 0.48$."
        }
    },
    "test1_mc2": {
        "source": "Test 1, Q2",
        "type": "mc",
        "question": {
            "de": r"$P(A)=0.6, P(B)=0.7, P(\bar{A} \cap B)=0.1$. Berechne $P(A \cap \bar{B})$.",
            "en": r"$P(A)=0.6, P(B)=0.7, P(\bar{A} \cap B)=0.1$. Find $P(A \cap \bar{B})$."
        },
        "options": [r"0", r"0.1", r"0.2", r"0.3"],
        "correct_idx": 0,
        "solution": {
            "de": r"**Richtig: 0**<br>$P(A \cap B) = P(B) - P(\bar{A} \cap B) = 0.7 - 0.1 = 0.6$.<br>$P(A \cap \bar{B}) = P(A) - P(A \cap B) = 0.6 - 0.6 = 0$.",
            "en": r"**Correct: 0**<br>$P(A \cap B) = P(B) - P(\bar{A} \cap B) = 0.7 - 0.1 = 0.6$.<br>$P(A \cap \bar{B}) = P(A) - P(A \cap B) = 0.6 - 0.6 = 0$."
        }
    },
    "test3_mc1": {
        "source": "Test 3, Q1",
        "type": "mc",
        "question": {
            "de": r"A, B disjunkt, P(A), P(B)>0. Welche Aussage trifft zu?",
            "en": r"A, B disjoint. Which is true?"
        },
        "options": [
            r"$P(\bar{A} \cap \bar{B}) ...$",
            r"$P(A \cap B) > ...$",
            r"$P(A|B) = P(B|A)$",
            r"$P(A \cup B) < ...$"
        ],
        "correct_idx": 2,
        "solution": {
            "de": r"**Richtig: (c)**<br>Disjunkt $\implies$ Keine Schnittmenge. $P(A|B)=0$ und $P(B|A)=0$.",
            "en": r"**Correct: (c)**<br>Disjoint $\implies$ No intersection. $P(A|B)=0$ and $P(B|A)=0$."
        }
    },
    "uebung1_mc3": {
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
            "de": r"**Richtig: (a)**<br>$P(B \cap A) = P(B|A) \cdot P(A) = 0.6 \cdot 0.5 = 0.3$.",
            "en": r"**Correct: (a)**<br>$P(B \cap A) = P(B|A) \cdot P(A) = 0.6 \cdot 0.5 = 0.3$."
        }
    },
    "uebung1_mc4": {
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
            "de": r"**Richtig: (a)**<br>Wenn $P(B|A)=0$, ist der Schnitt leer ($P(A \cap B)=0$). Das ist 'praktisch' disjunkt (innerhalb A).",
            "en": r"**Correct: (a)**<br>If $P(B|A)=0$, the intersection is empty ($P(A \cap B)=0$)."
        }
    },
    "uebung1_mc6": {
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
            "de": r"**Richtig: (a)**<br>Wenn wir 'in B' (Insel) sind, und B Teil von A (Land) ist, sind wir zu 100% 'in A'.",
            "en": r"**Correct: (a)**<br>If we are 'in B' (island), and B is part of A (country), we are 100% 'in A'."
        }
    },
    "uebung1_mc7": {
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
            "de": r"**Richtig: (c)**<br>Disjunkt = kein Überlapp = $0$ Wahrscheinlichkeit.",
            "en": r"**Correct: (c)**<br>Disjoint = no overlap = $0$ probability."
        }
    },
    "uebung1_mc9": {
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
            "de": r"**Richtig: (a)**<br>Wenn das Universum auf B schrumpft, wird der relative Anteil von A (Teilmenge) größer.",
            "en": r"**Correct: (a)**<br>If the universe shrinks to B, the relative share of A (subset) increases."
        }
    },
    "uebung1_mc10": {
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
            "de": r"**Richtig: (c) (und b)**<br>Disjunkt $\implies$ Schnitt ist leer (c) und Wahrscheinlichkeit additiv (b).",
            "en": r"**Correct: (c) (and b)**<br>Disjoint $\implies$ empty intersection (c) and additive probability (b)."
        }
    },
    "uebung1_mc12": {
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
            "de": r"**Richtig: (b)**<br>Unabhängigkeitstest: $0.6 \cdot 0.8 = 0.48 \ne 0.4$. Also abhängig.",
            "en": r"**Correct: (b)**<br>Check independence: $0.6 \cdot 0.8 = 0.48 \ne 0.4$. So dependent."
        }
    },
    "uebung1_mc14": {
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
            "de": r"**Richtig: (d)**<br>Wir wissen nichts über die Abhängigkeit. Schnitt könnte alles sein.",
            "en": r"**Correct: (d)**<br>We know nothing about dependence. Intersection could be anything."
        }
    },
    "uebung1_mc15": {
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
            "de": r"**Richtig: (c)**<br>$P(A \cap B) = 1/3 \cdot 1/3 = 1/9$.<br>$P(A|B) = (1/9) / (1/2) = 2/9$.",
            "en": r"**Correct: (c)**<br>$P(A \cap B) = 1/3 \cdot 1/3 = 1/9$.<br>$P(A|B) = (1/9) / (1/2) = 2/9$."
        }
    },
    "uebung1_mc16": {
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
            "de": r"**Richtig: (d)**<br>Das 3er-Produkt reicht nicht. Paarweise Unabhängigkeit ist auch nötig.",
            "en": r"**Correct: (d)**<br>Triple product is necessary but not sufficient (need pairwise independence)."
        }
    },
    "hs2022_prob3": {
        "source": "HS 2022 Januar, Problem 3 (15 Punkte)",
        "type": "multi_stage",
        "stem": {
            "de": r"**Szenario: Aktienkurs Modellierung (Kim)**<br><br>Ein Aktienkurs wird über 3 Tage modelliert:<br>• **Tag 1:** Startet bei 100. Geht mit 50% hoch (U) oder 50% runter (D).<br>• **Tag 2:** *Momentum-Effekt*: Wenn Tag 1 'U', dann 55% für weiteres 'U' (gleiche Richtung). Sonst (wenn D) 55% für 'D'.<br>• **Tag 3:** *Trend-Bestätigung*: Wenn 2x gleiche Richtung (UU oder DD), dann 60% Wahrscheinlichkeit für Fortsetzung (UUU oder DDD). Wenn Wechsel (UD oder DU), dann nur 50% für 'U'.",
            "en": r"**Scenario: Stock Price Modeling (Kim)**<br><br>Modeling a stock price over 3 days:<br>• **Day 1:** Starts at 100. Goes Up (U) 50% or Down (D) 50%.<br>• **Day 2:** *Momentum*: If Day 1 was U, 55% chance for another U. If D, 55% for D.<br>• **Day 3:** *Trend*: If 2x same direction (UU or DD), 60% chance to continue (UUU or DDD). If switch (UD or DU), then 50% for U."
        },
        "parts": [
            {
                "id": "part1",
                "type": "open",
                "question": {
                    "de": "Zeichnen Sie das Baumdiagramm für diesen Prozess. (Für diese Online-Aufgabe: Beschreiben Sie die Wahrscheinlichkeiten für die Pfade 'UUU' und 'UUD').",
                    "en": "Draw the tree diagram. (For this online task: Describe the probabilities for paths 'UUU' and 'UUD')."
                },
                "solution": {
                    "de": r"**Lösung:**<br>• $P(U) = 0.5$<br>• $P(U|U) = 0.55 \Rightarrow P(UU) = 0.5 \cdot 0.55 = 0.275$<br>• $P(U|UU) = 0.6 \Rightarrow P(UUU) = 0.275 \cdot 0.6 = 0.165$<br>• $P(D|UU) = 0.4 \Rightarrow P(UUD) = 0.275 \cdot 0.4 = 0.11$",
                    "en": r"**Solution:**<br>• $P(U) = 0.5$<br>• $P(U|U) = 0.55 \Rightarrow P(UU) = 0.5 \cdot 0.55 = 0.275$<br>• $P(U|UU) = 0.6 \Rightarrow P(UUU) = 0.275 \cdot 0.6 = 0.165$<br>• $P(D|UU) = 0.4 \Rightarrow P(UUD) = 0.275 \cdot 0.4 = 0.11$"
                }
            },
            {
                 "id": "part2",
                 "type": "mc",
                 "question": {
                     "de": "Berechnen Sie die Wahrscheinlichkeit für 3x Hoch (UUU).",
                     "en": "Calculate the probability for 3x Up (UUU)."
                 },
                 "options": ["0.125", "0.165", "0.225", "0.333"],
                 "correct_idx": 1,
                 "solution": {
                     "de": r"**Richtig: 0.165**<br>$P(UUU) = 0.5 \cdot 0.55 \cdot 0.6 = 0.165$.",
                     "en": r"**Correct: 0.165**<br>$P(UUU) = 0.5 \cdot 0.55 \cdot 0.6 = 0.165$."
                 }
            },
            {
                "id": "part3",
                "type": "open",
                "question": {
                    "de": "Berechnen Sie die Wahrscheinlichkeit, dass die Aktie am 3. Tag steigt ($U_3$).",
                    "en": "Calculate the probability that the stock goes up on Day 3 ($U_3$)."
                },
                "solution": {
                    "de": r"**Lösung: 0.5**<br>Wir müssen alle Pfade summieren, die mit U enden:<br>• $UUU: 0.165$<br>• $UDU: 0.5 \cdot 0.45 \cdot 0.5 = 0.1125$<br>• $DUU: 0.5 \cdot 0.45 \cdot 0.5 = 0.1125$<br>• $DDU: 0.5 \cdot 0.55 \cdot 0.4 = 0.11$<br>Summe: $0.165 + 0.1125 + 0.1125 + 0.11 = 0.5$.",
                    "en": r"**Solution: 0.5**<br>Sum all paths ending in U:<br>• $UUU: 0.165$<br>• $UDU: 0.1125$<br>• $DUU: 0.1125$<br>• $DDU: 0.11$<br>Total: $0.5$."
                }
            }
        ]
    }
}
QUESTIONS_2_6 = {
    "hs2022_mc1": {
        "source": "HS 2022 Januar, MC #1",
        "type": "mc",
        "question": {
            "de": "Drei Freunde spielen ein Spiel. Sie werfen eine faire Münze. Spieler 1 gewinnt bei erstem Wurf Kopf. Spieler 2 gewinnt bei zweitem Wurf Kopf. Spieler 3 gewinnt bei drittem Wurf Kopf. Wenn bis zur dritten Runde kein Gewinner, beginnt das Spiel von neuem. Wie hoch ist P(Spieler 3 gewinnt)?",
            "en": "Three friends play a game. They flip a fair coin. Player 1 wins on first flip heads. Player 2 wins on second flip heads. Player 3 wins on third flip heads. If no winner by round 3, game restarts. What is P(Player 3 wins)?"
        },
        "options": ["2/7", "1/7", "1/8", "3/7"],
        "correct_idx": 1,
        "solution": {
            "de": "**Richtig: 1/7**<br>Geometrische Reihe: Wahrscheinlichkeit in erster Runde ist $1/8$. Spiel wiederholt sich mit Wkt $1/8$.<br>$P_{win} = \frac{1/8}{1 - 1/8} = \frac{1}{7}$.",
            "en": "**Correct: 1/7**<br>Geometric series: Probability in first round is $1/8$. Game repeats with prob $1/8$.<br>$P_{win} = \frac{1/8}{1 - 1/8} = \frac{1}{7}$."
        }
    },
    "hs2022_mc7": {
        "source": "HS 2022 Januar, MC #7",
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
            "de": r"**Richtig: (a)**<br>Wir berechnen $P(A \text{ wins})$, da einfacher (A braucht 3 Siege).<br>$P(A) = 0.6^3 + 3 \cdot 0.4 \cdot 0.6^3 = 0.216 + 0.2592 = 0.4752$.<br>$P(B) = 1 - 0.4752 = 0.5248$.",
            "en": r"**Correct: (a)**<br>Calculate $P(A \text{ wins})$ (A needs 3 wins).<br>$P(A) = 0.6^3 + 3 \cdot 0.4 \cdot 0.6^3 = 0.4752$.<br>$P(B) = 1 - 0.4752 = 0.5248$."
        }
    },
    "hs2022_prob2": {
        "source": "HS 2022 Januar, Problem 2 (15 Punkte)",
        "type": "multi_stage",
        "stem": {
            "de": r"**Christopher segelt nach San Salvador (Westen).**<br>Diskussion verschiedener Modelle für die Ankunft.",
            "en": r"**Christopher sails to San Salvador (West).**<br>Discussion of different arrival models."
        },
        "parts": [
            {
                "id": "part1",
                "type": "open",
                "question": {
                    "de": "Modell Christopher: 4 Richtungen (N, E, S, W) gleichwahrscheinlich. Berechne die Wahrscheinlichkeit bei 2 Schritten, die Distanz nach Westen zu verringern (oder anzukommen?). (Annahme: Er muss 'Westen' treffen oder Distanz verringern? Lösung impliziert 9/16).",
                    "en": "Christopher's model: 4 directions (N, E, S, W) equally likely. Calculate probability to make progress West in 2 steps."
                },
                "solution": {
                    "de": r"**Lösung: 9/16**<br>Interpretation unklar aus Staging-Daten, aber offizielles Ergebnis 9/16.",
                    "en": r"**Solution: 9/16**."
                }
            },
            {
               "id": "part2",
                "type": "open",
                "question": {
                    "de": "Modell Diego: 8 Richtungen (N, NE, E, SE, S, SW, W, NW). Wahrscheinlichkeit?",
                    "en": "Diego's model: 8 directions. Probability?"
                },
                "solution": {
                    "de": "**Lösung: 25/64**",
                    "en": "**Solution: 25/64**"
                }
            }
        ]
    }
}
QUESTIONS_3_7 = {
    "hs2024_mc11": {
        "source": "HS 2024 Januar, MC #11",
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
            "de": r"**Richtig: (a)**<br>Die Verteilung der Gewinne beim fairen Münzwurf ist symmetrisch um 0. Daher ist die Verteilung von $X$ identisch mit der von $-X$ ($=Y$).",
            "en": r"**Correct: (a)**<br>The distribution of gains in a fair coin toss is symmetric around 0. Thus the distribution of $X$ is identical to that of $-X$ ($=Y$)."
        }
    }
}
QUESTIONS_4_9 = {}
QUESTIONS_5_5 = {
    "hs2023_prob2": {
        "source": "HS 2023 Januar, Problem 2 (15 Punkte)",
        "type": "problem",
        "question": {
            "de": r"Nachhaltigkeit und Kredite. A: Kredit bewilligt. B: Grüner Sachbearbeiter. $P(B)=0.5$. $P(A)=0.7$. $P(A|B)=0.8$.<br>1. Kontingenztabelle ausfüllen.<br>2. Berechne $P(A \cap B)$, $P(A|B)$, $P(A \cup B)$.<br>3. Sind A und B unabhängig?<br>4. Interview mit 8 Sachbearbeitern. Wahrscheinlichkeit, dass nur der erste 'Braun' ist? Wahrscheinlichkeit 4 Grün, 4 Braun?",
            "en": r"Sustainability and Loans. A: Loan approved. B: Green officer. $P(B)=0.5$. $P(A)=0.7$. $P(A|B)=0.8$.<br>1. Fill contingency table.<br>2. Calc $P(A \cap B)$, $P(A|B)$, $P(A \cup B)$.<br>3. Independence?<br>4. Interview 8 officers. Prob only first is Brown? Prob 4 Green, 4 Brown?"
        },
        "solution": {
            "de": r"**Lösung:**<br>1. $P(A \cap B) = 0.4$.<br>2. Abhängig ($0.8 \neq 0.7$).<br>3. $P(\text{1 Braun}) = 0.5^8 \approx 0.0039$.<br>4. $P(\text{4G, 4B}) = \binom{8}{4} 0.5^8 \approx 0.273$.",
            "en": r"**Solution:**<br>1. $P(A \cap B) = 0.4$.<br>2. Dependent ($0.8 \neq 0.7$).<br>3. $P(\text{1 Brown}) = 0.5^8 \approx 0.0039$.<br>4. $P(\text{4G, 4B}) = \binom{8}{4} 0.5^8 \approx 0.273$."
        }
    },
    "hs2023_prob4": {
        "source": "HS 2023 Januar, Problem 4 (15 Punkte)",
        "type": "problem",
        "question": {
            "de": r"Vektor $(X,Y)$. $f_X(x) = (4a e^{ax})^{-1}$ für $x \ge 0$. <br>1. Bestimme $a$.<br>2. Bestimme $b$ aus $F_Y$.<br>3. Gemeinsame Dichte.<br>4. Erwartungswert $Z = XY$.",
            "en": r"Vector $(X,Y)$. $f_X(x) = (4a e^{ax})^{-1}$. <br>1. Find $a$.<br>2. Find $b$ from $F_Y$.<br>3. Joint density.<br>4. Expectation $Z = XY$."
        },
        "solution": {
            "de": r"**Lösung:**<br>1. $a = 1/2$.<br>4. Unabhängigkeit angenommen (Produkt von Randdichten): $E[XY] = E[X]E[Y] = 2 \cdot 3 = 6$.",
            "en": r"**Solution:**<br>1. $a = 1/2$.<br>4. Assuming independence: $E[XY] = E[X]E[Y] = 2 \cdot 3 = 6$."
        }
    },
    "hs2022_prob4": {
        "source": "HS 2022 Januar, Problem 4 (15 Punkte)",
        "type": "multi_stage",
        "stem": {
            "de": r"**Teil 4A:** Gegeben ist die Randdichte $f_X(x) = a \sin(x)$ auf $[0, \pi]$. Die gemeinsame Dichte ist $f_{X,Y}(x,y) = \frac{1}{4} \sin(x) \cos(y)$ auf einem geeigneten Bereich.<br><br>**Teil 4B:** Gegeben sei $f_{X,Y}(x,y) = c(x + x/y)$ für $0 \le x \le 1$ und $1 \le y \le e$.",
            "en": r"**Part 4A:** Given marginal density $f_X(x) = a \sin(x)$ on $[0, \pi]$. The joint density is $f_{X,Y}(x,y) = \frac{1}{4} \sin(x) \cos(y)$ on a suitable domain.<br><br>**Part 4B:** Given $f_{X,Y}(x,y) = c(x + x/y)$ for $0 \le x \le 1$ and $1 \le y \le e$."
        },
        "parts": [
            {
                "id": "part1",
                "type": "open",
                "question": {
                    "de": "Teil 4A: Bestimmen Sie die Konstante $a$.",
                    "en": "Part 4A: Determine the constant $a$."
                },
                "solution": {
                    "de": r"**Lösung: $a=1/2$**<br>$\int_0^\pi \sin(x) dx = 2$. Damit das Integral 1 ist, muss $a=1/2$ sein.",
                    "en": r"**Solution: $a=1/2$**<br>$\int_0^\pi \sin(x) dx = 2$. For the integral to be 1, $a$ must be $1/2$."
                }
            },
            {
                "id": "part2",
                "type": "mc",
                "question": {
                    "de": "Teil 4A: Sind $X$ und $Y$ unabhängig?",
                    "en": "Part 4A: Are $X$ and $Y$ independent?"
                },
                "options": ["Ja / Yes", "Nein / No"],
                "correct_idx": 0,
                "solution": {
                    "de": r"**Richtig: Ja**<br>Die Dichte faktorisiert: $f(x,y) = \sin(x) \cdot \frac{1}{4}\cos(y)$.",
                    "en": r"**Correct: Yes**<br>The density factorizes: $f(x,y) = \sin(x) \cdot \frac{1}{4}\cos(y)$."
                }
            },
            {
                "id": "part3",
                "type": "open",
                "question": {
                    "de": r"Teil 4B: Berechnen Sie $P(X \le Y)$.",
                    "en": r"Part 4B: Calculate $P(X \le Y)$."
                },
                "solution": {
                    "de": r"**Lösung: 1**<br>Der Definitionsbereich ist $0 \le x \le 1$ und $1 \le y \le e$. Da $x$ immer maximal 1 und $y$ immer mindestens 1 ist, gilt $x \le y$ immer.",
                    "en": r"**Solution: 1**<br>The domain is $0 \le x \le 1$ and $1 \le y \le e$. Since $x$ is max 1 and $y$ is min 1, $x \le y$ holds everywhere."
                }
            },
            {
                "id": "part4",
                "type": "open",
                "question": {
                    "de": "Teil 4B: Zeigen Sie, dass $c = 2/e$.",
                    "en": "Part 4B: Show that $c = 2/e$."
                },
                "solution": {
                    "de": r"**Lösung:**<br>Doppelintegral berechnen.<br>$\int_1^e \int_0^1 c(x + x/y) dx dy = 1$.<br>$\int_0^1 x(1+1/y) dx = [\frac{1}{2}x^2]_0^1 (1+1/y) = \frac{1}{2}(1+1/y)$.<br>$\int_1^e \frac{c}{2}(1+1/y) dy = \frac{c}{2} [y + \ln(y)]_1^e = \frac{c}{2} (e+1 - 1 - 0) = \frac{c}{2} e$.<br>Gleich 1 setzen: $\frac{c e}{2} = 1 \Rightarrow c = 2/e$.",
                    "en": r"**Solution:**<br>Calculate double integral.<br>Result is $\frac{c e}{2} = 1 \Rightarrow c = 2/e$."
                }
            }
        ]
    }
}
QUESTIONS_6_3 = {}
QUESTIONS_7_6 = {
    "hs2023_prob1": {
        "source": "HS 2023 Januar, Problem 1 (12 Punkte)",
        "type": "problem",
        "question": {
            "de": r"**Teil 1A:** Ordnen Sie Verteilungen Diagrammen zu.<br>F1: Poisson(50), n=200<br>F2: Uniform[14, 26], n=200<br>F3: Normal(20, 4), n=200<br>F4: Binomial(200, 0.2), n=200<br><br>**Teil 1B:** Höchstgeschwindigkeit von 10 Autos: 180, 195, 240, 185, 230, 300, 290, 180, 235, 280.<br>1. Berechne Mittelwert, Modus, IQR.<br>2. Zeichne Histogramm.",
            "en": r"**Part 1A:** Match distributions to diagrams.<br>F1: Poisson(50)<br>F2: Uniform[14, 26]<br>F3: Normal(20, 4)<br>F4: Binomial(200, 0.2)<br><br>**Part 1B:** Top speeds of 10 cars: 180, 195, 240, 185, 230, 300, 290, 180, 235, 280.<br>1. Mean, Mode, IQR.<br>2. Histogram."
        },
        "solution": {
            "de": r"**Lösung 1A:**<br>F1: 50 (Mittel), F4: 40 (Mittel), F3: 20 (Mittel), F2: Flach.<br>**Lösung 1B:**<br>Sortiert: 180, 180, 185, 195, 230, 235, 240, 280, 290, 300.<br>Mittelwert: 231.5. Modus: 180.<br>IQR: $Q_3 - Q_1 = 280 - 185 = 95$.",
            "en": r"**Solution 1A:**<br>F1: 50 (Mean), F4: 40 (Mean), F3: 20 (Mean), F2: Flat.<br>**Solution 1B:**<br>Mean: 231.5. Mode: 180.<br>IQR: $280 - 185 = 95$."
        }
    },
    "hs2022_prob1": {
        "source": "HS 2022 Januar, Problem 1 (12 Punkte)",
        "type": "multi_stage",
        "stem": {
            "de": r"**Teil 1A:** Ordnen Sie die Verteilungen den Diagrammen zu (Diagramme nicht abgebildet, bitte theoretisch lösen based on parameters):<br>1) $N(0, 0.5)$<br>2) $B(100, 0.6)$<br>3) $U[-2, 2]$<br>4) $Exp(1/60)$<br><br>**Teil 1B:** Salatverkauf in der Mensa (11 Tage):<br>321, 321, 205, 320, 240, 450, 261, 345, 321, 276, 399.",
            "en": r"**Part 1A:** Match distributions to diagrams (solve theoretically):<br>1) $N(0, 0.5)$<br>2) $B(100, 0.6)$<br>3) $U[-2, 2]$<br>4) $Exp(1/60)$<br><br>**Part 1B:** Salad sales (11 days):<br>321, 321, 205, 320, 240, 450, 261, 345, 321, 276, 399."
        },
        "parts": [
            {
                "id": "part1",
                "type": "open",
                "question": {
                    "de": "Teil 1A: Beschreiben Sie die Charakteristika für die Zuordnung (z.B. Schiefe, Symmetrie).",
                    "en": "Part 1A: Describe the characteristics for matching (e.g., skewness, symmetry)."
                },
                "solution": {
                    "de": r"**Lösung:**<br>1. Normal: Symmetrisch um 0.<br>2. Binomial: Leicht schief oder fast symmetrisch um $np=60$. Diskret.<br>3. Uniform: Kastenform (Histogramm) oder Gerade (QQ).<br>4. Exponentiell: Stark rechtsschief, fällt monoton.",
                    "en": r"**Solution:**<br>1. Normal: Symmetric around 0.<br>2. Binomial: Around $np=60$.<br>3. Uniform: Box shape.<br>4. Exponential: Strongly right-skewed."
                }
            },
            {
                "id": "part2",
                "type": "open",
                "question": {
                    "de": "Teil 1B: Berechnen Sie Median und Modus der Salatverkäufe.",
                    "en": "Part 1B: Calculate Median and Mode of salad sales."
                },
                "solution": {
                    "de": r"**Lösung:**<br>Sortierte Daten: 205, 240, 261, 276, 320, **321**, 321, 321, 345, 399, 450.<br>Median (6. Wert): **321**.<br>Modus (häufigster Wert): **321**.",
                    "en": r"**Solution:**<br>Sorted: 205, 240, 261, 276, 320, **321**, 321, 321, 345, 399, 450.<br>Median: **321**.<br>Mode: **321**."
                }
            },
            {
                "id": "part3",
                "type": "open",
                "question": {
                     "de": "Teil 1B: Berechnen Sie die Grenzen für den Boxplot (Q1, Q3, Whiskers).",
                     "en": "Part 1B: Calculate boxplot limits (Q1, Q3, Whiskers)."
                },
                "solution": {
                    "de": r"**Lösung:**<br>Q1 (25%): 261.<br>Q3 (75%): 345.<br>IQR: $345-261 = 84$.<br>Whiskers: $[Q1 - 1.5 IQR, Q3 + 1.5 IQR] = [135, 471]$. Alle Daten liegen innerhalb.",
                    "en": r"**Solution:**<br>Q1: 261, Q3: 345.<br>IQR: 84.<br>Whiskers: $[135, 471]$."
                }
            }
        ]
    }
}
QUESTIONS_8_4 = {
    "hs2023_prob5": {
        "source": "HS 2023 Januar, Problem 5 (15 Punkte)",
        "type": "problem",
        "question": {
            "de": r"5A: $f(x) = \frac{2x}{\lambda^2} e^{-(x/\lambda)^2}$. MLE für $\lambda$.<br>5B: Diskrete Verteilung $1/\theta$. Daten: 1, 4, 3, 4, 2.<br>1. Momentenschätzer für $\theta$.<br>2. MLE für $\theta$.<br>3. Werte berechnen.",
            "en": r"5A: MLE for $\lambda$ given density.<br>5B: Discrete uniform $1/\theta$. Data: 1, 4, 3, 4, 2.<br>1. MME for $\theta$.<br>2. MLE for $\theta$.<br>3. Calculate values."
        },
        "solution": {
            "de": r"**Lösung:**<br>5A: $\hat{\lambda} = \sqrt{\frac{1}{n} \sum x_i^2}$.<br>5B: MME $\hat{\theta} = 2\bar{X} - 1 = 4.6$. MLE $\hat{\theta} = \max(x_i) = 4$.",
            "en": r"**Solution:**<br>5A: $\hat{\lambda} = \sqrt{\frac{1}{n} \sum x_i^2}$.<br>5B: MME $\hat{\theta} = 2\bar{X} - 1 = 4.6$. MLE $\hat{\theta} = \max(x_i) = 4$."
        }
    },
    "hs2022_prob5": {
        "source": "HS 2022 Januar, Problem 5 (15 Punkte)",
        "type": "multi_stage",
        "stem": {
            "de": r"**Poisson Verteilung:** Gegeben sei eine Zufallsstichprobe $X_1, \dots, X_n$ aus einer Poisson-Verteilung mit Parameter $\lambda$.<br>Daten: 0.5, 0.25, 0.15.",
            "en": r"**Poisson Distribution:** Given a random sample $X_1, \dots, X_n$ from a Poisson distribution with parameter $\lambda$.<br>Data: 0.5, 0.25, 0.15."
        },
        "parts": [
            {
                "id": "part1",
                "type": "open",
                "question": {
                    "de": r"Berechnen Sie den Momentenschätzer $\hat{\lambda}_{MM}$.",
                    "en": r"Calculate the Method of Moments estimator $\hat{\lambda}_{MM}$."
                },
                "solution": {
                    "de": r"**Lösung:** $\hat{\lambda}_{MM} = \bar{X}$.<br>Bei Poisson ist $E[X] = \lambda$. Wir setzen $E[X] = \bar{X}$.",
                    "en": r"**Solution:** $\hat{\lambda}_{MM} = \bar{X}$.<br>For Poisson, $E[X] = \lambda$. We set $E[X] = \bar{X}$."
                }
            },
            {
                "id": "part2",
                "type": "open",
                "question": {
                    "de": r"Berechnen Sie den Maximum-Likelihood-Schätzer $\hat{\lambda}_{MLE}$.",
                    "en": r"Calculate the Maximum Likelihood Estimator $\hat{\lambda}_{MLE}$."
                },
                "solution": {
                    "de": r"**Lösung:** $\hat{\lambda}_{MLE} = \bar{X}$.<br>Likelihood ableiten und Null setzen führt ebenfalls zum Mittelwert.",
                    "en": r"**Solution:** $\hat{\lambda}_{MLE} = \bar{X}$.<br>Deriving likelihood and setting to zero also yields the mean."
                }
            },
            {
                "id": "part3",
                "type": "open",
                "question": {
                    "de": "Berechnen Sie den Schätzwert für die Daten: 0.5, 0.25, 0.15. (Hinweis: Die Daten sind nicht ganzzahlig, theoretisch problematisch für Poisson, aber hier rein rechnerisch gemeint).",
                    "en": "Calculate the estimate for the data: 0.5, 0.25, 0.15. (Note: Data is non-integer, theoretically problematic for Poisson, but meant computationally)."
                },
                "solution": {
                    "de": r"**Lösung:** $\bar{X} = (0.5+0.25+0.15)/3 = 0.9/3 = 0.3$.",
                    "en": r"**Solution:** $\bar{X} = 0.3$."
                }
            }
        ]
    }
}
QUESTIONS_9_4 = {
    "hs2024_mc4": {
        "source": "HS 2024 Januar, MC #4",
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
            "de": r"**Richtig: (b)**<br>Gesucht ist das Schwankungsintervall für einen *Einzelwert* $X$ (nicht Mittelwert).<br>$500 \pm z_{0.995} \cdot \sigma = 500 \pm 2.576 \cdot \sqrt{40} \approx 500 \pm 16.29$.",
            "en": r"**Correct: (b)**<br>Prediction interval for a *single value* $X$ (not mean).<br>$500 \pm z_{0.995} \cdot \sigma = 500 \pm 2.576 \cdot \sqrt{40} \approx 500 \pm 16.29$."
        }
    }
}
QUESTIONS_10_5 = {}

# Aliases for export
QUESTIONS_5 = QUESTIONS_5_3

def get_question(topic_id: str, question_id: str) -> dict:
    """Retrieve a specific question by topic and question ID."""
    topic_map = {
        "1.1": QUESTIONS_1_1,
        "1.2": QUESTIONS_1_2,
        "1.3": QUESTIONS_1_3,
        "1.4": QUESTIONS_1_4,
        "1.5": QUESTIONS_1_5,
        "1.6": QUESTIONS_1_6,
        "1.7": QUESTIONS_1_7,
        "1.8": QUESTIONS_1_8,
        "1.9": QUESTIONS_1_9,
        "1.10": QUESTIONS_1_10,
        "1.11": QUESTIONS_1_11,
        "2.1": QUESTIONS_2_1,
        "2.2": QUESTIONS_2_2,
        "2.3": QUESTIONS_2_3,
        "2.4": QUESTIONS_2_4,
        "2.5": QUESTIONS_2_5,
        "2.6": QUESTIONS_2_6,
        "3.1": QUESTIONS_3_1,
        "3.2": QUESTIONS_3_2,
        "3.3": QUESTIONS_3_3,
        "3.4": QUESTIONS_3_4,
        "3.5": QUESTIONS_3_5,
        "3.6": QUESTIONS_3_6,
        "3.7": QUESTIONS_3_7,
        "4.2": QUESTIONS_4_2,
        "4.3": QUESTIONS_4_3,
        "4.4": QUESTIONS_4_4,
        "4.5": QUESTIONS_4_5,
        "4.6": QUESTIONS_4_6,
        "4.7": QUESTIONS_4_7,
        "4.8": QUESTIONS_4_8,
        "4.9": QUESTIONS_4_9,
        "5.1": QUESTIONS_5_1,
        "5.2": QUESTIONS_5_2,
        "5.3": QUESTIONS_5_3,
        "5.4": QUESTIONS_5_4,
        "5.5": QUESTIONS_5_5,
        "6": QUESTIONS_6,
        "6.3": QUESTIONS_6_3,
        "7": QUESTIONS_7,
        "7.6": QUESTIONS_7_6,
        "8": QUESTIONS_8,
        "8.4": QUESTIONS_8_4,
        "9": QUESTIONS_9,
        "9.4": QUESTIONS_9_4,
        "10": QUESTIONS_10,
        "10.5": QUESTIONS_10_5,
        "11.1": QUESTIONS_11_1,
    }
    
    topic_questions = topic_map.get(topic_id, {})
    return topic_questions.get(question_id, None)

def get_all_questions_for_topic(topic_id: str) -> dict:
    """Retrieve all questions for a given topic."""
    topic_map = {
        "1.1": QUESTIONS_1_1,
        "1.2": QUESTIONS_1_2,
        "1.3": QUESTIONS_1_3,
        "1.4": QUESTIONS_1_4,
        "1.5": QUESTIONS_1_5,
        "1.6": QUESTIONS_1_6,
        "1.7": QUESTIONS_1_7,
        "1.8": QUESTIONS_1_8,
        "1.9": QUESTIONS_1_9,
        "1.10": QUESTIONS_1_10,
        "1.11": QUESTIONS_1_11,
        "2.1": QUESTIONS_2_1,
        "2.2": QUESTIONS_2_2,
        "2.3": QUESTIONS_2_3,
        "2.4": QUESTIONS_2_4,
        "2.5": QUESTIONS_2_5,
        "2.6": QUESTIONS_2_6,
        "3.1": QUESTIONS_3_1,
        "3.2": QUESTIONS_3_2,
        "3.3": QUESTIONS_3_3,
        "3.4": QUESTIONS_3_4,
        "3.5": QUESTIONS_3_5,
        "3.6": QUESTIONS_3_6,
        "3.7": QUESTIONS_3_7,
        "4.2": QUESTIONS_4_2,
        "4.3": QUESTIONS_4_3,
        "4.4": QUESTIONS_4_4,
        "4.5": QUESTIONS_4_5,
        "4.6": QUESTIONS_4_6,
        "4.7": QUESTIONS_4_7,
        "4.8": QUESTIONS_4_8,
        "4.9": QUESTIONS_4_9,
        "5.1": QUESTIONS_5_1,
        "5.2": QUESTIONS_5_2,
        "5.3": QUESTIONS_5_3,
        "5.4": QUESTIONS_5_4,
        "5.5": QUESTIONS_5_5,
        "6": QUESTIONS_6,
        "6.3": QUESTIONS_6_3,
        "7": QUESTIONS_7,
        "7.6": QUESTIONS_7_6,
        "8": QUESTIONS_8,
        "8.4": QUESTIONS_8_4,
        "9": QUESTIONS_9,
        "9.4": QUESTIONS_9_4,
        "10": QUESTIONS_10,
        "10.5": QUESTIONS_10_5,
        "11.1": QUESTIONS_11_1,
    }
    return topic_map.get(topic_id, {})
