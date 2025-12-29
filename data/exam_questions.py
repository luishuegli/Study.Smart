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
            "de": r"Werfen von zwei Würfeln ($|S|=36$). Ereignis A: 'Mindestens ein Würfel zeigt eine Sechs'. P(A) = ?",
            "en": r"Throwing two dice ($|S|=36$). Event A: 'At least one die shows a six'. P(A) = ?"
        },
        "options": ["10/36", "11/36", "1/6", "12/36"],
        "correct_idx": 1,
        "solution": {
            "de": "**Richtig! (11/36)**<br>Elemente: {(6,1), (6,2), ..., (6,6), (1,6), ..., (5,6)}. Das sind 6 + 5 = 11.",
            "en": "**Correct! (11/36)**<br>Elements: {(6,1), (6,2), ..., (6,6), (1,6), ..., (5,6)}. That is 6 + 5 = 11."
        }
    },
    "q_1_2_1_b": {
        "source": "Prüfungstraining 1.2.1 (B)",
        "question": {
            "de": r"Werfen von zwei Würfeln. Ereignis B: 'Die Augensumme ist 9'. P(B) = ?",
            "en": r"Throwing two dice. Event B: 'The sum of dots is 9'. P(B) = ?"
        },
        "options": ["3/36", "4/36", "5/36", "1/9"],
        "correct_idx": 1,
        "solution": {
            "de": "**Richtig! (4/36)**<br>Elemente: {(3,6), (4,5), (5,4), (6,3)}.",
            "en": "**Correct! (4/36)**<br>Elements: {(3,6), (4,5), (5,4), (6,3)}."
        }
    },
    "q_1_2_1_c": {
        "source": "Prüfungstraining 1.2.1 (C)",
        "question": {
            "de": r"Werfen von zwei Würfeln. Ereignis C: 'Die Augensumme ist kleiner als 4'. P(C) = ?",
            "en": r"Throwing two dice. Event C: 'The sum of dots is less than 4'. P(C) = ?"
        },
        "options": ["3/36", "2/36", "4/36", "1/12"],
        "correct_idx": 0,
        "solution": {
            "de": "**Richtig! (3/36)**<br>Elemente: {(1,1), (1,2), (2,1)}. Summe < 4 bedeutet Summe 2 oder 3.",
            "en": "**Correct! (3/36)**<br>Elements: {(1,1), (1,2), (2,1)}. Sum < 4 means sum 2 or 3."
        }
    },
    "test1_q2": {
        "source": "Test 1, Frage 2",
        "question": {
            "de": "Es seien A und B zwei beliebige Ereignisse mit $P(A) = 0.6$, $P(B) = 0.7$ und $P(\\overline{A} \\cap B) = 0.1$. Berechnen Sie $P(A \\cap \\overline{B})$.",
            "en": "Let A and B be two arbitrary events with $P(A) = 0.6$, $P(B) = 0.7$ and $P(\\overline{A} \\cap B) = 0.1$. Calculate $P(A \\cap \\overline{B})$."
        },
        "options": ["0", "0.1", "0.2", "0.3"],
        "correct_idx": 0,
        "solution": {
            "de": "**Richtig: 0**<br>Wir wissen $P(B) = P(A \\cap B) + P(\\overline{A} \\cap B)$.<br>Also $0.7 = P(A \\cap B) + 0.1 \\Rightarrow P(A \\cap B) = 0.6$.<br>Weiterhin ist $P(A) = P(A \\cap B) + P(A \\cap \\overline{B})$.<br>Also $0.6 = 0.6 + P(A \\cap \\overline{B}) \\Rightarrow P(A \\cap \\overline{B}) = 0$.",
            "en": "**Correct: 0**<br>We know $P(B) = P(A \\cap B) + P(\\overline{A} \\cap B)$.<br>So $0.7 = P(A \\cap B) + 0.1 \\Rightarrow P(A \\cap B) = 0.6$.<br>Furthermore $P(A) = P(A \\cap B) + P(A \\cap \\overline{B})$.<br>So $0.6 = 0.6 + P(A \\cap \\overline{B}) \\Rightarrow P(A \\cap \\overline{B}) = 0$."
        }
    },
    "test3_q1": {
        "source": "Test 3, Frage 1",
        "question": {
            "de": "Die Ereignisse A und B sind disjunkt mit $P(A)>0, P(B)>0$. Welche Aussage stimmt?",
            "en": "Events A and B are disjoint with $P(A)>0, P(B)>0$. Which statement is true?"
        },
        "options": [
            {"de": "$P(\\overline{A} \\cap \\overline{B}) + P(B) > 1 - P(A)$", "en": "$P(\\overline{A} \\cap \\overline{B}) + P(B) > 1 - P(A)$"},
            {"de": "$P(A \\cap B) > P(A)$", "en": "$P(A \\cap B) > P(A)$"},
            {"de": "$P(A|B) = P(B|A)$", "en": "$P(A|B) = P(B|A)$"},
            {"de": "$P(A \\cup B) < P(A)$", "en": "$P(A \\cup B) < P(A)$"}
        ],
        "correct_idx": 2,
        "solution": {
            "de": "**Richtig: (c)**<br>Da A und B disjunkt sind, ist $A \\cap B = \\emptyset$, also $P(A \\cap B) = 0$.<br>Daher ist $P(A|B) = 0$ und $P(B|A) = 0$.",
            "en": "**Correct: (c)**<br>Since A and B are disjoint, $A \\cap B = \\emptyset$, thus $P(A \\cap B) = 0$.<br>Therefore $P(A|B) = 0$ and $P(B|A) = 0$."
        }
    }
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
             "de": "Hinweis: Nutze zuerst das Komplement $P(A|B) = 1 - P(\\overline{A}|B)$. Verwende dann die Multiplikationsregel: $P(A \\cap B) = P(A|B) \\cdot P(B)$.", 
             "en": "Hint: First find $P(A|B) = 1 - P(\\overline{A}|B)$. Then use the multiplication rule: $P(A \\cap B) = P(A|B) \\cdot P(B)$."
        },
        "options": ["0.55", "0.60", "0.70", "0.25"],
        "correct_idx": 1,
        "solution": {
             "de": r"**Richtig: 0.6**<br>1. $P(A|B) = 1 - 0.75 = 0.25$<br>2. $P(A \cap B) = 0.25 \cdot 0.4 = 0.1$<br>3. $P(A \cup B) = 0.3 + 0.4 - 0.1 = 0.6$",
             "en": r"**Correct: 0.6**<br>1. $P(A|B) = 1 - 0.75 = 0.25$<br>2. $P(A \cap B) = 0.25 \cdot 0.4 = 0.1$<br>3. $P(A \cup B) = 0.3 + 0.4 - 0.1 = 0.6$"
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
        "options": ["0", "Unendlich klein, aber > 0", "1", "Abhängig vom Radius"],
        "correct_idx": 0,
        "solution": {
            "de": "**Antwort: 0**<br>Ein mathematischer Punkt hat keine Fläche. $P(X=x) = 0$. Nur Intervalle/Flächen haben Wahrscheinlichkeiten > 0.",
            "en": "**Answer: 0**<br>A mathematical point has no area. $P(X=x) = 0$. Only intervals/areas have probabilities > 0."
        }
    }
}

# 1.7 Bedingte Wahrscheinlichkeit und stochastische Unabhängigkeit
QUESTIONS_1_7 = {
    "uebung1_mc1": {
        "source": "Übung 1, MC1",
        "question": {
            "de": "A und B sind zwei unabhängige Ereignisse. Dann gilt:",
            "en": "A and B are two independent events. Then:"
        },
        "options": [
            {"de": "P[B | A] = 0", "en": "P[B | A] = 0"},
            {"de": "P[B | A] = P[B]", "en": "P[B | A] = P[B]"},
            {"de": "P[B | A] = P[A]", "en": "P[B | A] = P[A]"},
            {"de": "Wir haben nicht genügend Informationen", "en": "We do not have enough information"}
        ],
        "correct_idx": 1,
        "solution": {
            "de": "**Richtig: (b)**<br>Definition der Unabhängigkeit: Das Eintreten von A ändert die Wahrscheinlichkeit von B nicht.",
            "en": "**Correct: (b)**<br>Definition of independence: The occurrence of A does not change the probability of B."
        }
    },
    "uebung1_mc2": {
        "source": "Übung 1, MC2",
        "question": {
            "de": "A und B sind zwei disjunkte Ereignisse (P(A)>0). Dann gilt:",
            "en": "A and B are two disjoint events (P(A)>0). Then:"
        },
        "options": [
            {"de": "P[B | A] = 0", "en": "P[B | A] = 0"},
            {"de": "P[B | A] = P[B]", "en": "P[B | A] = P[B]"},
            {"de": "P[B | A] = P[A]", "en": "P[B | A] = P[A]"},
            {"de": "Wir haben nicht genügend Informationen", "en": "We do not have enough information"}
        ],
        "correct_idx": 0,
        "solution": {
            "de": "**Richtig: (a)**<br>Wenn A eingetreten ist, kann B nicht mehr eintreten (da keine Schnittmenge).",
            "en": "**Correct: (a)**<br>If A has occurred, B cannot occur (since there is no intersection)."
        }
    },
    "uebung1_mc8": {
        "source": "Übung 1, MC8",
        "question": {
            "de": "A und B sind zwei unvereinbare (disjunkte) Ereignisse mit P[A] > 0 und P[B] > 0. Dann gilt:",
            "en": "A and B are two mutually exclusive (disjoint) events with P[A] > 0 and P[B] > 0. Then:"
        },
        "options": [
            {"de": "A und B sind unabhängig", "en": "A and B are independent"},
            {"de": "A und B sind abhängig", "en": "A and B are dependent"},
            {"de": "Wir haben nicht genügend Informationen", "en": "We do not have enough information"}
        ],
        "correct_idx": 1,
        "solution": {
            "de": "**Richtig: (b)**<br>Disjunkte Ereignisse (mit positiver Wahrscheinlichkeit) sind STARK abhängig. Wenn ich weiss A ist eingetreten, weiss ich zu 100%, dass B NICHT eingetreten ist.",
            "en": "**Correct: (b)**<br>Disjoint events (with positive probability) are STRONGLY dependent. If I know A has occurred, I know 100% that B has NOT occurred."
        }
    },
    "uebung1_prob3": {
        "source": "Übung 1, Problem 3",
        "type": "problem",
        "question": {
            "de": "Gegeben: P[A] = 0.5, P[B] = 0.3, P[A ∩ B] = 0.2.<br>Berechnen Sie:<br>(a) P[A ∪ B]<br>(b) P[A | B]<br>(c) P[A ∩ B̄]",
            "en": "Given: P[A] = 0.5, P[B] = 0.3, P[A ∩ B] = 0.2.<br>Calculate:<br>(a) P[A ∪ B]<br>(b) P[A | B]<br>(c) P[A ∩ B̄]"
        },
        "solution": {
            "de": "**Lösung:**<br>(a) P[A ∪ B] = 0.5 + 0.3 − 0.2 = **0.6**<br>(b) P[A | B] = 0.2 / 0.3 = **2/3**<br>(c) P[A ∩ B̄] = P[A] − P[A ∩ B] = 0.5 − 0.2 = **0.3**",
            "en": "**Solution:**<br>(a) P[A ∪ B] = 0.5 + 0.3 − 0.2 = **0.6**<br>(b) P[A | B] = 0.2 / 0.3 = **2/3**<br>(c) P[A ∩ B̄] = P[A] − P[A ∩ B] = 0.5 − 0.2 = **0.3**"
        }
    },
    "hs2023_mc1": {
        "source": "HS2023, MC1",
        "question": {
            "de": "Folgende Informationen sind gegeben: P(A) = 0,5, P(B) = 0,3, P(A ∪ B) = 0,4. Welche der folgenden Aussagen ist wahr?",
            "en": "The following information is given: P(A) = 0.5, P(B) = 0.3, P(A ∪ B) = 0.4. Which of the following statements is true?"
        },
        "options": [
            {"de": "A und B sind disjunkt", "en": "A and B are disjoint"},
            {"de": "A und B sind unabhängig", "en": "A and B are independent"},
            {"de": "A und B sind nicht unabhängig", "en": "A and B are not independent"},
            {"de": "Nicht genügend Informationen gegeben", "en": "Not enough information given"}
        ],
        "correct_idx": 2,
        "solution": {
            "de": "**Richtig: (c)**<br>P(A ∩ B) = P(A) + P(B) - P(A ∪ B) = 0.5 + 0.3 - 0.4 = 0.4.<br>P(A)P(B) = 0.15 ≠ 0.4. Also abhängig.",
            "en": "**Correct: (c)**<br>P(A ∩ B) = P(A) + P(B) - P(A ∪ B) = 0.5 + 0.3 - 0.4 = 0.4.<br>P(A)P(B) = 0.15 ≠ 0.4. Therefore dependent."
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
    "test1_q1": {
        "source": "Test 1, Frage 1",
        "question": {
            "de": "300 Hörer einer Statistik-Vorlesung:<br>VWL: 42 m, 93 w<br>BWL: 78 m, 87 w<br>Eine Hörerin wird gewählt. Wahrscheinlichkeit, dass sie BWL studiert?",
            "en": "300 students in a stats lecture:<br>Econ: 42 m, 93 f<br>Bus: 78 m, 87 f<br>A female student is chosen. Probability she studies Business?"
        },
        "options": ["0.31", "0.29", "0.71", "0.48"],
        "correct_idx": 3,
        "solution": {
            "de": "**Richtig: 0.48**<br>Gesucht: $P(\\text{BWL}|\\text{w})$.<br>Anzahl w = 93 + 87 = 180.<br>Anzahl w und BWL = 87.<br>$P(\\text{BWL}|\\text{w}) = 87/180 \\approx 0.48$.",
            "en": "**Correct: 0.48**<br>Find: $P(\\text{Bus}|\\text{f})$.<br>Total f = 93 + 87 = 180.<br>Total f and Bus = 87.<br>$P(\\text{Bus}|\\text{f}) = 87/180 \\approx 0.48$."
        }
    }
}

# 1.8 Totale Wahrscheinlichkeit & Bayes
QUESTIONS_1_8 = {
    "uebung1_prob5": {
        "source": "Übung 1, Problem 5",
        "type": "problem",
        "question": {
            "de": "Maschine A produziert 70% der Stücke (8% Fehlerquote). Maschine B produziert 30% (6% Fehlerquote). Ein zufällig gezogenes Stück ist fehlerhaft. Wie gross ist die Wahrscheinlichkeit, dass es von A kommt?",
            "en": "Machine A produces 70% of parts (8% defect rate). Machine B produces 30% (6% defect rate). A randomly chosen part is defective. What is the probability it came from A?"
        },
        "solution": {
            "de": "**Lösung:**<br>P(A|F) = (0.08 · 0.7) / (0.08 · 0.7 + 0.06 · 0.3) = 0.056 / 0.074 ≈ **75.68%**",
            "en": "**Solution:**<br>P(A|F) = (0.08 · 0.7) / (0.08 · 0.7 + 0.06 · 0.3) = 0.056 / 0.074 ≈ **75.68%**"
        }
    },
     "uebung1_prob6": {
        "source": "Übung 1, Problem 6",
        "type": "problem",
        "question": {
            "de": "Gymnasium-Statistik:<br>• 40% bestehen die Matura nicht (NM)<br>• 90% von NM hatten negativen Aufnahmetest (T-)<br>• 1% von Bestandenen (M) hatten negativen Test (T-)<br>Wie gross ist P(T-)?",
            "en": "High School Statistics:<br>• 40% fail the Matura (NM)<br>• 90% of NM had a negative admission test (T-)<br>• 1% of those who passed (M) had a negative test (T-)<br>What is P(T-)?"
        },
        "solution": {
            "de": "**Lösung:**<br>P(T-) = P(T-|NM)P(NM) + P(T-|M)P(M)<br>= 0.9·0.4 + 0.01·0.6 = 0.36 + 0.006 = **36.6%**",
            "en": "**Solution:**<br>P(T-) = P(T-|NM)P(NM) + P(T-|M)P(M)<br>= 0.9·0.4 + 0.01·0.6 = 0.36 + 0.006 = **36.6%**"
        }
    },
    "uebung1_prob_factory": {
        "source": "Interactive Mission: The Factory",
        "type": "problem",
        "question": {
            "de": "Eine Maschine A produziert 20% aller Teile mit 5% Fehler. Maschine B produziert 80% mit 1% Fehler. Wie hoch ist die totale Fehlerrate?",
            "en": "Machine A produces 20% of all parts with 5% defects. Machine B produces 80% with 1% defects. What is the total defect rate?"
        },
        "options": ["3%", "1.8%", "6%", "2.5%"],
        "correct_idx": 1,
        "solution": {
            "de": "**Antwort: 1.8%**<br>Satz der totalen Wahrscheinlichkeit:<br>$P(D) = 0.05 \\cdot 0.20 + 0.01 \\cdot 0.80 = 0.01 + 0.008 = 0.018 = 1.8\\%$",
            "en": "**Answer: 1.8%**<br>Law of Total Probability:<br>$P(D) = 0.05 \\cdot 0.20 + 0.01 \\cdot 0.80 = 0.01 + 0.008 = 0.018 = 1.8\\%$"
        }
    },
    "hs2022_mc2": {
        "source": "HS 2022 Januar, MC #2",
        "question": {
            "de": "Sie haben 1000 Münzen und wissen, dass es unter den 1000 Münzen genau eine besondere Münze gibt, die auf beiden Seiten Zahl hat. Sie wählen eine Münze zufällig aus diesen 1000 aus. Sie werfen diese eine Münze 10 Mal. Sie zeigt 10 Mal hintereinander Zahl an. Wie hoch ist die Wahrscheinlichkeit, dass Sie die besondere Münze genommen haben?",
            "en": "You have 1000 coins and know that among them there is exactly one special coin with tails on both sides. You randomly pick one coin and flip it 10 times. It shows tails 10 times in a row. What is the probability that you picked the special coin?"
        },
        "options": ["50.6%", "99.9%", "0.1%", "25%"],
        "correct_idx": 0,
        "solution": {
            "de": "**Richtig: 50.6%**<br>Bayes' Theorem:<br>$P(\\text{special}|10T) = \\frac{1 \\cdot \\frac{1}{1000}}{1 \\cdot \\frac{1}{1000} + (\\frac{1}{2})^{10} \\cdot \\frac{999}{1000}} \\approx 0.506$",
            "en": "**Correct: 50.6%**<br>Bayes' Theorem:<br>$P(\\text{special}|10T) = \\frac{1 \\cdot \\frac{1}{1000}}{1 \\cdot \\frac{1}{1000} + (\\frac{1}{2})^{10} \\cdot \\frac{999}{1000}} \\approx 0.506$"
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
    }
}
QUESTIONS_1_9 = {
    # Include 1.8 questions if needed, but defining specific ones here
    "uebung1_prob6": QUESTIONS_1_8["uebung1_prob6"], # Reference to existing if reused
    "three_prisoners": {
        "source": "Logic Check: 3 Prisoners",
        "question": {
            "de": "Drei Gefangene (A, B, C). Einer wird begnadigt. Wärter nennt B als Todeskandidat. Steigt As Chance?",
            "en": "Three prisoners (A, B, C). One is pardoned. Warden names B as executed. Does A's chance increase?"
        },
        "options": [
            {"de": "Ja, auf 50%", "en": "Yes, to 50%"},
            {"de": "Nein, bleibt 1/3", "en": "No, stays 1/3"},
            {"de": "Ja, auf 66%", "en": "Yes, to 66%"},
            {"de": "Nein, sinkt", "en": "No, decreases"}
        ],
        "correct_idx": 1,
        "solution": {
            "de": "**Antwort: Nein, bleibt 1/3**<br>Der Wärter musste einen Namen nennen. Dass er B nennt, gibt A keine spezifische Information über sich selbst. Die 'überschüssige' Wahrscheinlichkeit wandert zu C (2/3).",
            "en": "**Answer: No, stays 1/3**<br>The warden had to name someone. Naming B gives A no specific information about himself. The 'surplus' probability shifts to C (2/3)."
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
            "de": "Krankheit (1% Prävalenz). Test (99% genau). Du testest positiv. Wie groß ist die Wahrscheinlichkeit, dass du wirklich krank bist?",
            "en": "Disease (1% prevalence). Test (99% accurate). You test positive. What is the probability you are actually sick?"
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
            "de": "Du setzt 10 CHF auf Rot (18 rote, 18 schwarze, 1 grüne Zahl). Gewinn: Verdoppelung. Was ist dein erwarteter Gewinn pro Spiel?",
            "en": "You bet 10 CHF on Red (18 red, 18 black, 1 green number). Win: Double up. What is your expected gain per game?"
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
            "de": "Der Bus kommt alle 10 Minuten (gleichverteilt). Du kommst 'zufällig' an. Wie lange wartest du im Durchschnitt?",
            "en": "The bus comes every 10 minutes (uniformly distributed). You arrive 'randomly'. How long do you wait on average?"
        },
        "options": ["10 min", "1 min", "5 min", "0 min"],
        "correct_idx": 2,
        "solution": {
            "de": r"**Richtig: 5 min**<br>Erwartungswert einer stetigen Gleichverteilung $[0, 10]$: $\frac{a+b}{2} = 5$.",
            "en": r"**Correct: 5 min**<br>Expected value of continuous uniform distribution $[0, 10]$: $\frac{a+b}{2} = 5$."
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
            "de": "In einem Verein mit 10 Mitgliedern (4 Frauen und 6 Herren) soll nun ein Vorstand bestehend aus zwei Damen und zwei Herren gebildet werden. Wie viele Möglichkeiten gibt es?", 
            "en": "In a club with 10 members (4 women and 6 men), a board consisting of two women and two men is to be formed. How many possibilities are there?"
        },
        "options": ["90", "25", "210", "60"],
        "correct_idx": 0,
        "solution": {
            "de": "**Richtig! (90)**<br>Frauen: $\\binom{4}{2} = 6$. Männer: $\\binom{6}{2} = 15$. Fundamentalprinzip: $6 \\cdot 15 = 90$.", 
            "en": "**Correct! (90)**<br>Women: $\\binom{4}{2} = 6$. Men: $\\binom{6}{2} = 15$. Principle: $6 \\cdot 15 = 90$."
        }
    }
}
QUESTIONS_2_3 = {
    "dvd_collection": {
        "source": "Statistik I, Aufgabe 3",
        "question": {
            "de": "Sie besitzen **50 verschiedene DVDs** und die dazugehörigen 50 Hüllen. Auf wie viele Arten können die DVDs in die Hüllen einsortiert werden?",
            "en": "You own **50 different DVDs** and their 50 cases. In how many ways can the DVDs be sorted into the cases?"
        },
        "options": ["50!", "50^50", "1", "Binom(50, 50)"],
        "correct_idx": 0,
        "solution": {
            "de": "**Richtig: 50!**<br>Permutation ohne Wiederholung.",
            "en": "**Correct: 50!**<br>Permutation without replacement."
        }
    },
    "test1_q3": {
        "source": "Test 1, Frage 3",
        "question": {
            "de": "Sie besitzen 50 verschiedene DVDs und 50 Hüllen. Ihr Neffe verteilt die DVDs zufällig. Wie viele Arten der Verteilung gibt es?",
            "en": "You have 50 different DVDs and 50 cases. Your nephew distributes them randomly. How many arrangements are possible?"
        },
        "options": ["50!", "$(50!)^2$", "$50! \\cdot 49!$", "$\\binom{100}{2}$"],
        "correct_idx": 0,
        "solution": {
            "de": "**Richtig: 50!**<br>Jede DVD kommt in genau eine Hülle. Das ist eine Permutation von 50 Elementen.",
            "en": "**Correct: 50!**<br>Each DVD goes into exactly one case. This is a permutation of 50 elements."
        }
    },
    "hs2015_mc4": {
        "source": "HS 2015 Januar, MC #4",
        "question": {
            "de": "Herr Meyer hat seinen Schlüssel für das Schliessfach verloren. Die Schliessfachnummer hat er leider vergessen. Er erinnert sich allerdings daran, dass es sich um eine vierstellige Zahl handelt, bei der zwei Ziffern gleich sind und dass als Ziffern die 3, 5 und 7 vorkommen. Wieviele Schliessfacher erfüllen diese Kriterien?",
            "en": "Mr. Meyer lost his locker key. He forgot the locker number. He remembers it's a four-digit number where two digits are the same and the digits 3, 5, and 7 appear. How many lockers meet these criteria?"
        },
        "options": ["18", "24", "36", "48"],
        "correct_idx": 2,
        "solution": {
            "de": "**Richtig: 36**<br>Wähle die doppelte Ziffer: C(3,1) = 3.<br>Arrangiere 4 Positionen mit 2 gleichen: 4!/(2!) = 12.<br>Total: 3 × 12 = 36.",
            "en": "**Correct: 36**<br>Choose the repeated digit: C(3,1) = 3.<br>Arrange 4 positions with 2 same: 4!/(2!) = 12.<br>Total: 3 × 12 = 36."
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
            {"de": "49!", "en": "49!"},
            {"de": "C(49,6)", "en": "C(49,6)"},
            {"de": "49^6", "en": "49^6"},
            {"de": "P(49,6)", "en": "P(49,6)"}
        ],
        "correct_idx": 1,
        "solution": {
            "de": "**Richtig: C(49,6)**<br>Reihenfolge egal, ohne Zurücklegen.",
            "en": "**Correct: C(49,6)**<br>Order doesn't matter, without replacement."
        }
    },
    "test2_q1": {
        "source": "Test 2, Frage 1",
        "question": {
            "de": "Verein mit 10 Mitgliedern (4 Frauen, 6 Männer). Vorstand (2 Frauen, 2 Männer) soll gebildet werden. Wie viele Möglichkeiten?",
            "en": "Club with 10 members (4 women, 6 men). Board (2 women, 2 men) to be formed. How many possibilities?"
        },
        "options": ["89", "210", "90", "75"],
        "correct_idx": 2,
        "solution": {
            "de": "**Richtig: 90**<br>$\\binom{4}{2} \\cdot \\binom{6}{2} = 6 \\cdot 15 = 90$.",
            "en": "**Correct: 90**<br>$\\binom{4}{2} \\cdot \\binom{6}{2} = 6 \\cdot 15 = 90$."
        }
    }
}

QUESTIONS_2_5 = {
    "coin_toss_seq": {
        "source": "Kombinatorik",
        "question": {
            "de": "Eine Münze wird 4 Mal geworfen. Wie viele Ergebnisfolgen?",
            "en": "A coin is tossed 4 times. How many outcome sequences?"
        },
        "options": ["24", "16", "6", "8"],
        "correct_idx": 1,
        "solution": {
            "de": "**Richtig: 16** (2^4)",
            "en": "**Correct: 16** (2^4)"
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
    "uebung2_prob5": {
        "source": "Übung 2, Problem 5",
        "type": "problem",
        "question": {
            "de": "X ist gleichförmig verteilt auf [0, 3] (Dichte 1/3).<br>a) E[X]<br>b) E[4X + 2]",
            "en": "X is uniformly distributed on [0, 3] (density 1/3).<br>a) E[X]<br>b) E[4X + 2]"
        },
        "solution": {
            "de": "**Lösung:**<br>a) Mitte des Intervalls: **1.5**<br>b) Linearität: 4·1.5 + 2 = **8**",
            "en": "**Solution:**<br>a) Midpoint of interval: **1.5**<br>b) Linearity: 4·1.5 + 2 = **8**"
        }
    },
    "uebung2_prob7": {
        "source": "Übung 2, Problem 7 (Xenia)",
        "type": "problem",
        "question": {
            "de": "Lernzeit Xenia:<br>• Schön (1/10): 20 min<br>• Bewölkt (1/3): 60 min<br>• Regen (1/2): 80 min<br>• Schnee (1/15): 120 min<br>Berechnen Sie den Erwartungswert.",
            "en": "Xenia's study time:<br>• Sunny (1/10): 20 min<br>• Cloudy (1/3): 60 min<br>• Rain (1/2): 80 min<br>• Snow (1/15): 120 min<br>Calculate the expected value."
        },
        "solution": {
            "de": "**Lösung: 70 Minuten**<br>E[X] = 1/10·20 + 1/3·60 + 1/2·80 + 1/15·120 = 2 + 20 + 40 + 8 = 70",
            "en": "**Solution: 70 minutes**<br>E[X] = 1/10·20 + 1/3·60 + 1/2·80 + 1/15·120 = 2 + 20 + 40 + 8 = 70"
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
            "de": "X normalverteilt mit $\\mu$ und $\\sigma > 0$. Für $Y = X/\\sigma$ gilt $E[Y^2] = ...$",
            "en": "X normal distributed with $\\mu$ and $\\sigma > 0$. For $Y = X/\\sigma$, $E[Y^2] = ...$"
        },
        "options": ["1", "$1 - \\mu^2/\\sigma^2$", "$1 + \\mu^2/\\sigma^2$", "?"],
        "correct_idx": 2,
        "solution": {
            "de": "**Richtig: (c)**<br>$E[Y^2] = 1/\\sigma^2 \\cdot E[X^2]$.<br>$Var(X) = E[X^2] - \\mu^2 = \\sigma^2 \\Rightarrow E[X^2] = \\sigma^2 + \\mu^2$.<br>Also $E[Y^2] = (\\sigma^2+\\mu^2)/\\sigma^2 = 1 + \\mu^2/\\sigma^2$.",
            "en": "**Correct: (c)**<br>$E[Y^2] = 1/\\sigma^2 \\cdot E[X^2]$.<br>$Var(X) = E[X^2] - \\mu^2 = \\sigma^2 \\Rightarrow E[X^2] = \\sigma^2 + \\mu^2$.<br>So $E[Y^2] = (\\sigma^2+\\mu^2)/\\sigma^2 = 1 + \\mu^2/\\sigma^2$."
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
            "de": "Basketball: Trefferquote p = 1/2. Vier Würfe.<br>Berechnen Sie E[X] und V(X).",
            "en": "Basketball: Hit rate p = 1/2. Four shots.<br>Calculate E[X] and V(X)."
        },
        "solution": {
            "de": "**Lösung:**<br>Binomialverteilung n=4, p=0.5.<br>E[X] = n·p = 2<br>V(X) = n·p·(1-p) = 4·0.25 = 1",
            "en": "**Solution:**<br>Binomial distribution n=4, p=0.5.<br>E[X] = n·p = 2<br>V(X) = n·p·(1-p) = 4·0.25 = 1"
        }
    }
}

# 4.3 Binomial
QUESTIONS_4_3 = {
    "uebung2_giro": {
        "source": "Übung 2, MC11",
        "question": {
            "de": "Miguel gewinnt Giro d'Italia mit 30%. Wahrscheinlichkeit bei 5 Teilnahmen mind. 2 mal zu gewinnen?",
            "en": "Miguel wins Giro d'Italia with 30%. Probability to win at least 2 times in 5 participations?"
        },
        "options": ["0.639", "0.472", "0.600", "0.360"],
        "correct_idx": 1,
        "solution": {
            "de": "**Richtig: 0.47178**<br>1 - P(X=0) - P(X=1)",
            "en": "**Correct: 0.47178**<br>1 - P(X=0) - P(X=1)"
        }
    },
    "uebung2_insur": {
        "source": "Übung 2, Problem 2 (Versicherung)",
        "type": "problem",
        "question": {
            "de": "Herr Kaiser verkauft bei 20% (2 von 10) eine Versicherung. Er macht 16 Besuche pro Tag.<br>Berechnen Sie E[X] und Var(X).",
            "en": "Mr. Kaiser sells insurance in 20% (2 of 10) of visits. He makes 16 visits per day.<br>Calculate E[X] and Var(X)."
        },
        "solution": {
            "de": "**Lösung:**<br>E[X] = 16 · 0.2 = **3.2**<br>Var(X) = 16 · 0.2 · 0.8 = **2.56**",
            "en": "**Solution:**<br>E[X] = 16 · 0.2 = **3.2**<br>Var(X) = 16 · 0.2 · 0.8 = **2.56**"
        }
    },
    "hs2022_mc7": {
        "source": "HS 2022 Januar, MC #7",
        "question": {
            "de": "Im Oktober macht Nina einen einwöchigen Städtetrip nach Hamburg. Die Wettervorhersage sagt für jeden Tag eine Regenwahrscheinlichkeit von 70% voraus. Wie hoch ist in etwa die Wahrscheinlichkeit, dass es an mindestens 5 von 7 Tagen regnet?",
            "en": "In October, Nina takes a one-week city trip to Hamburg. The weather forecast predicts 70% rain probability each day. What is approximately the probability it rains at least 5 of 7 days?"
        },
        "options": ["65%", "35%", "50%", "80%"],
        "correct_idx": 0,
        "solution": {
            "de": "**Richtig: 65%**<br>$X \\sim \\text{Bin}(7, 0.7)$.<br>$P(X \\ge 5) = P(X=5) + P(X=6) + P(X=7) \\approx 0.65$",
            "en": "**Correct: 65%**<br>$X \\sim \\text{Bin}(7, 0.7)$.<br>$P(X \\ge 5) = P(X=5) + P(X=6) + P(X=7) \\approx 0.65$"
        }
    },
    "hs2023_mc12": {
        "source": "HS 2023 Januar, MC #12",
        "question": {
            "de": "Jacob geht ins Casino mit 100 Spielautomaten. Gewinnwahrscheinlichkeit 20%. Er spielt 5 Spiele pro Automat. Wie groß ist die Wahrscheinlichkeit, an mindestens 4 der 100 Automaten mehr als zweimal zu gewinnen?",
            "en": "Jacob goes to a casino with 100 slot machines. Win probability 20%. He plays 5 games per machine. What is the probability of winning more than twice at at least 4 of the 100 machines?"
        },
        "options": ["0.2513", "0.8372", "0.5000", "0.9500"],
        "correct_idx": 1,
        "solution": {
            "de": "**Richtig: 0.8372**<br>Zweistufig:<br>1) $P(X>2)$ für Bin(5, 0.2) ≈ 0.058.<br>2) $Y \\sim \\text{Bin}(100, 0.058)$. $P(Y \\ge 4) \\approx 0.837$.",
            "en": "**Correct: 0.8372**<br>Two-stage:<br>1) $P(X>2)$ for Bin(5, 0.2) ≈ 0.058.<br>2) $Y \\sim \\text{Bin}(100, 0.058)$. $P(Y \\ge 4) \\approx 0.837$."
        }
    }
}

# 4.4 Poisson
QUESTIONS_4_4 = {
    "uebung2_typo": {
        "source": "Übung 2, Problem 3 (Druckfehler)",
        "type": "problem",
        "question": {
            "de": "Buch hat im Mittel µ = 8 Druckfehler (Poisson).<br>a) P(X ≥ 6)?<br>b) P(X = 13)?",
            "en": "Book has on average µ = 8 typos (Poisson).<br>a) P(X ≥ 6)?<br>b) P(X = 13)?"
        },
        "solution": {
            "de": "**Lösung:**<br>a) 1 - P(X≤5) ≈ **0.8088**<br>b) (8^13 · e^-8) / 13! ≈ **0.0296**",
            "en": "**Solution:**<br>a) 1 - P(X≤5) ≈ **0.8088**<br>b) (8^13 · e^-8) / 13! ≈ **0.0296**"
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
    }
}

# 4.7 Normalverteilung
QUESTIONS_4_7 = {
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
    "hs2023_mc7": {
        "source": "HS 2023 Januar, MC #7",
        "question": {
            "de": "Die ausführliche Analyse von Prüfungsergebnissen eines Statistik Kurses hat ergeben, dass Studenten durchschnittlich 20 Punkte erreichen. Die Punkte sind mit einer Varianz von neun Punkten Normalverteilt. Wie groß ist die Wahrscheinlichkeit, dass ein Student weniger als 25 Punkte erreicht?",
            "en": "Analysis of statistics exam results shows students score on average 20 points. With variance of 9 and normal distribution. What is the probability a student scores less than 25 points?"
        },
        "options": ["0.952", "0.841", "0.500", "0.159"],
        "correct_idx": 0,
        "solution": {
            "de": "**Richtig: 0.952**<br>X ~ N(20, 9), σ = 3.<br>Z = (25-20)/3 = 5/3 ≈ 1.67.<br>P(X < 25) = Φ(1.67) ≈ 0.952.",
            "en": "**Correct: 0.952**<br>X ~ N(20, 9), σ = 3.<br>Z = (25-20)/3 = 5/3 ≈ 1.67.<br>P(X < 25) = Φ(1.67) ≈ 0.952."
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
            "de": "Der vollbeladene Öltanker Ever Given II mit einer Gesamtkapazität von 30.000 m³ will den Kiel Kanal passieren. Hat der Tanker mehr als 27.040 Tonnen Rohöl geladen so würde er auf Grund laufen. Das Gewicht von 1 m³ Rohöl ist unabhängig und identisch mit Mittelwert 0.9 und unbekannter Varianz σ² verteilt. Mit Hilfe seiner Statistikkenntnisse schätzt der Kapitän die Wahrscheinlichkeit auf Grund zu laufen auf 0.2. Welche Varianz σ² hat der Kapitän für das Gewicht von 1 m³ angenommen?",
            "en": "The fully loaded oil tanker Ever Given II with capacity 30,000 m³ wants to pass the Kiel Canal. If it has more than 27,040 tons of crude oil, it would run aground. The weight of 1 m³ of crude oil is i.i.d. with mean 0.9 and unknown variance σ². The captain estimates the probability of running aground at 0.2. What variance σ² has the captain assumed?"
        },
        "options": ["0.0064", "0.0016", "0.0100", "0.0036"],
        "correct_idx": 0,
        "solution": {
            "de": "**Richtig: 0.0064**<br>CLT: P(Summe > 27.040) = 0.2.<br>μ = 30000 × 0.9 = 27000.<br>Z-Wert für 0.8: z = 0.842.<br>(27040-27000)/√(30000·σ²) = 0.842.<br>σ² = 0.0064.",
            "en": "**Correct: 0.0064**<br>CLT: P(Sum > 27,040) = 0.2.<br>μ = 30,000 × 0.9 = 27,000.<br>Z-value for 0.8: z = 0.842.<br>(27040-27000)/√(30000·σ²) = 0.842.<br>σ² = 0.0064."
        }
    }
}

# 4.8 Hypergeometrisch
QUESTIONS_4_8 = {
    "hypergeom_10_5_3": {
        "source": "Test 5, Frage 1",
        "question": {
            "de": "Urne mit N=10 Kugeln, davon M=5 rot. Ziehe n=3 ohne Zurücklegen. X = Anzahl rote Kugeln. P(X=2)?",
            "en": "Urn with N=10 balls, M=5 red. Draw n=3 without replacement. X = number of red balls. P(X=2)?"
        },
        "options": ["5/12", "1/2", "1/3", "7/12"],
        "correct_idx": 0,
        "solution": {
            "de": "**Richtig: 5/12**<br>Hypergeometrisch: P(X=2) = (5C2 * 5C1) / 10C3 = (10*5)/120 = 50/120 = 5/12.",
            "en": "**Correct: 5/12**<br>Hypergeometric: P(X=2) = (5C2 * 5C1) / 10C3 = (10*5)/120 = 50/120 = 5/12."
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
        "options": [{"de": "5", "en": "5"}, {"de": "6", "en": "6"}, {"de": "1", "en": "1"}, {"de": "Unbekannt", "en": "Unknown"}],
        "correct_idx": 0,
        "solution": {
            "de": r"**Richtig: 5**<br>Linearität des Erwartungswertes: $E[X+Y] = E[X] + E[Y]$.",
            "en": r"**Correct: 5**<br>Linearity of expectation: $E[X+Y] = E[X] + E[Y]$."
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
    }
}

# 5.2 Varianz
QUESTIONS_5_2 = {
    "test3_q5": {
        "source": "Test 3, Frage 5",
        "question": {
            "de": r"$X, Y$ unabhängig. $\text{Var}(X)=2$, $\text{Var}(Y)=3$. Was ist $\text{Var}(X - Y)$?",
            "en": r"$X, Y$ independent. $\text{Var}(X)=2$, $\text{Var}(Y)=3$. What is $\text{Var}(X - Y)$?"
        },
        "options": ["5", "-1", "1", "13"],
        "correct_idx": 0,
        "solution": {
            "de": r"**Richtig: 5**<br>Unabhängig: $\text{Var}(X - Y) = \text{Var}(X) + (-1)^2 \text{Var}(Y) = 2 + 3 = 5$.",
            "en": r"**Correct: 5**<br>Independent: $\text{Var}(X - Y) = \text{Var}(X) + (-1)^2 \text{Var}(Y) = 2 + 3 = 5$."
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
    }
}

# 5.3 Kovarianz
QUESTIONS_5_3 = {
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
            "de": r"Urne mit 5 Kugeln (1-5). Ziehen ohne Zurücklegen. $X$ = 1. Kugel, $Y$ = 2. Kugel. Korrelation?",
            "en": r"Urn with 5 balls (1-5). Draw without replacement. $X$ = 1st ball, $Y$ = 2nd ball. Correlation?"
        },
        "options": ["0", "-0.25", "-0.5"],
        "correct_idx": 1,
        "solution": {
            "de": r"**Richtig: -0.25**<br>$\rho = \frac{-1}{N-1} = \frac{-1}{4} = -0.25$",
            "en": r"**Correct: -0.25**<br>$\rho = \frac{-1}{N-1} = \frac{-1}{4} = -0.25$"
        }
    },
    "test4_q2": {
        "source": "Test 4, Frage 2",
        "question": {
            "de": r"$\text{Cov}(X,Y) = 3$, $\text{Var}(X) = 4$, $\text{Var}(Y) = 9$. Berechnen Sie $\text{Cor}(X,Y)$.",
            "en": r"$\text{Cov}(X,Y) = 3$, $\text{Var}(X) = 4$, $\text{Var}(Y) = 9$. Calculate $\text{Cor}(X,Y)$."
        },
        "options": ["0.5", "0.25", "0.75", "0.33"],
        "correct_idx": 0,
        "solution": {
            "de": r"**Richtig: 0.5**<br>$\text{Cor} = \frac{\text{Cov}}{\sigma_X \cdot \sigma_Y} = \frac{3}{2 \cdot 3} = \frac{3}{6} = 0.5$.",
            "en": r"**Correct: 0.5**<br>$\text{Cor} = \frac{\text{Cov}}{\sigma_X \cdot \sigma_Y} = \frac{3}{2 \cdot 3} = \frac{3}{6} = 0.5$."
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
        "options": ["7", "8", "9.8", "11"],
        "correct_idx": 3,
        "solution": {
            "de": r"**Richtig: 11**<br>Mean $\approx 9.8$, Median $= 8$, Mode $= 7$.<br>11 ist keines davon.",
            "en": r"**Correct: 11**<br>Mean $\approx 9.8$, Median $= 8$, Mode $= 7$.<br>11 is none of these."
        }
    },
    "hs2015_mc9": {
        "source": "HS 2015 Januar, MC #9",
        "question": {
            "de": r"Zu Kontrollzwecken werden 1000 Packungen Reis aus der Produktion entnommen und gewogen. Dabei stellt sich heraus, dass das Gewicht der Packungen annähernd normalverteilt ist. Wenn 800 der Packungen zwischen 343.2 und 356.8 Gramm wiegen, was ist dann die ungefähre Varianz des Gewichtes?",
            "en": r"For quality control, 1000 packages of rice are sampled and weighed. The weight is approximately normally distributed. If 800 of the packages weigh between 343.2 and 356.8 grams, what is the approximate variance of the weight?"
        },
        "options": ["9", "25", "36", "49"],
        "correct_idx": 2,
        "solution": {
            "de": r"**Richtig: 36**<br>$800/1000 = 80\%$ liegt im inneren Bereich.<br>Für 80%: $\mu \pm 1.28\sigma$.<br>$2 \cdot 1.28\sigma = 356.8 - 343.2 = 13.6$.<br>$\sigma \approx 5.3$, also $\sigma^2 \approx 28$ → Nächster Wert: 36.",
            "en": r"**Correct: 36**<br>$800/1000 = 80\%$ is in the inner region.<br>For 80%: $\mu \pm 1.28\sigma$.<br>$2 \cdot 1.28\sigma = 356.8 - 343.2 = 13.6$.<br>$\sigma \approx 5.3$, so $\sigma^2 \approx 28$ → Closest: 36."
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
        "options": ["13", "5", "4", "1"],
        "correct_idx": 3,
        "solution": {
            "de": r"**Richtig: 1**<br>$\text{Var}(3X+Y) = 9 \cdot \text{Var}(X) + \text{Var}(Y) + 2 \cdot 3 \cdot 1 \cdot (-1) \cdot \sigma_X \cdot \sigma_Y$<br>$= 9 + 4 - 12 = 1$.",
            "en": r"**Correct: 1**<br>$\text{Var}(3X+Y) = 9 \cdot \text{Var}(X) + \text{Var}(Y) + 2 \cdot 3 \cdot 1 \cdot (-1) \cdot \sigma_X \cdot \sigma_Y$<br>$= 9 + 4 - 12 = 1$."
        }
    },
    "hs2023_mc9": {
        "source": "HS 2023 Januar, MC #9",
        "question": {
            "de": r"Seien $X$ und $Y$ zwei Zufallsvariablen mit Verteilungen $X \sim N(4, 4)$ und $Y \sim N(0, 9)$. Des Weiteren gilt $E[XY] = E[X]E[Y]$. Sei $Z$ eine Zufallsvariable welche als $Z = 3 + 2X - 3Y$ definiert ist. Wie lautet die Kovarianz $\text{Cov}(Y, Z)$?",
            "en": r"Let $X$ and $Y$ be two random variables with distributions $X \sim N(4, 4)$ and $Y \sim N(0, 9)$. Furthermore $E[XY] = E[X]E[Y]$. Let $Z = 3 + 2X - 3Y$. What is $\text{Cov}(Y, Z)$?"
        },
        "options": ["-27", "-9", "0", "27"],
        "correct_idx": 0,
        "solution": {
            "de": r"**Richtig: -27**<br>$E[XY] = E[X]E[Y] \Rightarrow \text{Cov}(X,Y) = 0$.<br>$\text{Cov}(Y, Z) = \text{Cov}(Y, 3 + 2X - 3Y) = 2 \cdot \text{Cov}(Y,X) - 3 \cdot \text{Var}(Y)$<br>$= 0 - 3 \cdot 9 = -27$.",
            "en": r"**Correct: -27**<br>$E[XY] = E[X]E[Y] \Rightarrow \text{Cov}(X,Y) = 0$.<br>$\text{Cov}(Y, Z) = \text{Cov}(Y, 3 + 2X - 3Y) = 2 \cdot \text{Cov}(Y,X) - 3 \cdot \text{Var}(Y)$<br>$= 0 - 3 \cdot 9 = -27$."
        }
    }
}

# 6. Zentraler Grenzwertsatz
QUESTIONS_6 = {
    "uebung4_prob1": {
        "source": "Übung 4, Problem 1",
        "type": "problem",
        "question": {
            "de": "100'000 Chips. Stichprobe n=400. Annahme wenn ≤44 defekt. Ablehnung wenn ≥51. Totalkontrolle sonst. Wahre Fehlerrate 10%. Berechnen Sie die Wahrscheinlichkeiten.",
            "en": "100,000 chips. Sample n=400. Accept if ≤44 defective. Reject if ≥51. Total check otherwise. True defect rate 10%. Calculate probabilities."
        },
        "solution": {
            "de": "**Lösung:**<br>1) Annahme: P(X ≤ 44) ≈ **0.7434**<br>2) Ablehnung: P(X ≥ 51) ≈ **0.040**<br>3) Totalkontrolle: Rest ≈ **0.1866**",
            "en": "**Solution:**<br>1) Accept: P(X ≤ 44) ≈ **0.7434**<br>2) Reject: P(X ≥ 51) ≈ **0.040**<br>3) Total check: Rest ≈ **0.1866**"
        }
    }
}

# 8. Punktschätzung
QUESTIONS_8 = {
    "uebung5_prob1": {
        "source": "Übung 5, Problem 1",
        "type": "problem",
        "question": {
            "de": "Schätzer für µ:<br>1) (X1+X2)/2<br>2) X1/3 + 2X2/3<br>Welcher ist effizienter?",
            "en": "Estimators for µ:<br>1) (X1+X2)/2<br>2) X1/3 + 2X2/3<br>Which is more efficient?"
        },
        "solution": {
            "de": "**Lösung:** Schätzer 1 ist effizienter (kleinere Varianz: Var/2 vs 5Var/9).",
            "en": "**Solution:** Estimator 1 is more efficient (lower variance: Var/2 vs 5Var/9)."
        }
    },
    "uebung5_prob7": {
        "source": "Übung 5, Problem 7",
        "type": "problem",
        "question": {
            "de": "Poisson X, µ=λ. ML-Schätzer für λ?",
            "en": "Poisson X, µ=λ. ML estimator for λ?"
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
            "de": "n=100, x_bar=10, sigma=2 known. 95% KI für µ?",
            "en": "n=100, x_bar=10, sigma=2 known. 95% CI for µ?"
        },
        "solution": {
            "de": "**Lösung:** 10 ± 1.96 · 2/10 = [9.608, 10.392]",
            "en": "**Solution:** 10 ± 1.96 · 2/10 = [9.608, 10.392]"
        }
    },
    "uebung5_prob4": {
        "source": "Übung 5, Problem 4",
        "type": "problem",
        "question": {
            "de": "Anteil p. n=400, k=80 (20%). 95% KI für p?",
            "en": "Proportion p. n=400, k=80 (20%). 95% CI for p?"
        },
        "solution": {
            "de": "**Lösung:** 0.2 ± 1.96 · sqrt(0.2·0.8/400) = 0.2 ± 0.0392 = [0.1608, 0.2392]",
            "en": "**Solution:** 0.2 ± 1.96 · sqrt(0.2·0.8/400) = 0.2 ± 0.0392 = [0.1608, 0.2392]"
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
        "source": "HS 2015 Januar, MC #10",
        "question": {
            "de": r"Für $\theta > 1$ sei $X_1, X_2, \ldots, X_n$ eine unabhängige Folge in $[1, \theta]$ gleichverteilter Zufallsvariablen. Wir betrachten den Schätzer $\hat{\theta} = \frac{2}{n} \sum x_i$ für den Parameter $\theta$. Welche der folgenden Aussagen über $\hat{\theta}$ trifft zu?",
            "en": r"For $\theta > 1$, let $X_1, X_2, \ldots, X_n$ be i.i.d. uniformly distributed on $[1, \theta]$. We consider the estimator $\hat{\theta} = \frac{2}{n} \sum x_i$ for $\theta$. Which statement about $\hat{\theta}$ is true?"
        },
        "options": [
            {"de": "Erwartungstreu und konsistent", "en": "Unbiased and consistent"},
            {"de": "Erwartungstreu aber nicht konsistent", "en": "Unbiased but not consistent"},
            {"de": "Konsistent aber nicht erwartungstreu", "en": "Consistent but not unbiased"},
            {"de": "Weder noch", "en": "Neither"}
        ],
        "correct_idx": 2,
        "solution": {
            "de": r"**Richtig: (c)**<br>$E[\hat{\theta}] = 2 \cdot E[X] = 2 \cdot \frac{1+\theta}{2} = 1+\theta \neq \theta$.<br>Also nicht erwartungstreu.<br>Aber für $n \to \infty$ konvergiert $\hat{\theta} \to \theta$ (konsistent).",
            "en": r"**Correct: (c)**<br>$E[\hat{\theta}] = 2 \cdot E[X] = 2 \cdot \frac{1+\theta}{2} = 1+\theta \neq \theta$.<br>So not unbiased.<br>But as $n \to \infty$, $\hat{\theta} \to \theta$ (consistent)."
        }
    },
    "hs2023_mc5": {
        "source": "HS 2023 Januar, MC #5",
        "question": {
            "de": "Im Auftrag eines Großhandlers müssen Konfidenzintervalle für die durchschnittliche Füllmenge eines Abfüllsystems für 500 ml Bierflaschen bestimmt werden. Die Abfüllmenge X ist mit einer Varianz von 10 ml Normalverteilt. Zehn Flaschen: {501, 495, 503, 498, 500, 498, 497, 503, 497, 501}. Wie lautet das korrekte symmetrische 95% Konfidenzintervall?",
            "en": "A wholesaler needs confidence intervals for the average fill volume of a 500ml beer bottle filling system. Fill volume X is normally distributed with variance 10 ml. Ten bottles: {501, 495, 503, 498, 500, 498, 497, 503, 497, 501}. What is the correct symmetric 95% confidence interval?"
        },
        "options": ["[495.0, 503.6]", "[496.5, 502.1]", "[498.0, 500.6]", "[497.34, 501.26]"],
        "correct_idx": 3,
        "solution": {
            "de": "**Richtig: [497.34, 501.26]**<br>X̄ = 499.3, σ = √10 ≈ 3.16, n = 10.<br>KI = X̄ ± z_{0.975}·σ/√n = 499.3 ± 1.96·(3.16/√10) ≈ 499.3 ± 1.96.",
            "en": "**Correct: [497.34, 501.26]**<br>X̄ = 499.3, σ = √10 ≈ 3.16, n = 10.<br>CI = X̄ ± z_{0.975}·σ/√n = 499.3 ± 1.96·(3.16/√10) ≈ 499.3 ± 1.96."
        }
    }
}

# 10. Hypothesentests
QUESTIONS_10 = {
    "uebung6_prob1": {
        "source": "Übung 6, Problem 1",
        "type": "problem",
        "question": {
            "de": "X_bar = 218. H0: µ=210. n=225 (sigma² bekannt -> Z-Test).",
            "en": "X_bar = 218. H0: µ=210. n=225 (sigma² known -> Z-test)."
        },
        "solution": {
            "de": "**Lösung:** Z = 1.6. Bei 5% Level (1.645) NICHT verwerfen.",
            "en": "**Solution:** Z = 1.6. Do NOT reject at 5% level (1.645 critical value)."
        }
    },
    "uebung6_prob4": {
        "source": "Übung 6, Problem 4",
        "type": "problem",
        "question": {
            "de": "t-Test. n=16, x_bar=10, s=2. H0: µ=12. Teststatistik?",
            "en": "t-Test. n=16, x_bar=10, s=2. H0: µ=12. Test statistic?"
        },
        "solution": {
            "de": "**Lösung:** t = (10-12)/(2/4) = -4. Verwerfen.",
            "en": "**Solution:** t = (10-12)/(2/4) = -4. Reject."
        }
    },
    "uebung6_prob8": {
        "source": "Übung 6, Problem 8",
        "type": "problem",
        "question": {
            "de": "p-Wert = 0.03. Alpha = 0.05. Entscheidung?",
            "en": "p-value = 0.03. Alpha = 0.05. Decision?"
        },
        "solution": {
            "de": "**Lösung:** H0 verwerfen (da p < alpha).",
            "en": "**Solution:** Reject H0 (since p < alpha)."
        }
    }
}

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
        "2.1": QUESTIONS_2_1,
        "2.2": QUESTIONS_2_2,
        "2.3": QUESTIONS_2_3,
        "2.4": QUESTIONS_2_4,
        "2.5": QUESTIONS_2_5,
        "3.1": QUESTIONS_3_1,
        "3.2": QUESTIONS_3_2,
        "3.3": QUESTIONS_3_3,
        "3.4": QUESTIONS_3_4,
        "3.5": QUESTIONS_3_5,
        "3.6": QUESTIONS_3_6,
        "4.2": QUESTIONS_4_2,
        "4.3": QUESTIONS_4_3,
        "4.4": QUESTIONS_4_4,
        "4.5": QUESTIONS_4_5,
        "4.6": QUESTIONS_4_6,
        "4.7": QUESTIONS_4_7,
        "4.8": QUESTIONS_4_8,
        "5.1": QUESTIONS_5_1,
        "5.2": QUESTIONS_5_2,
        "5.3": QUESTIONS_5_3,
        "5.4": QUESTIONS_5_4,
        "6": QUESTIONS_6,
        "7": QUESTIONS_7,
        "8": QUESTIONS_8,
        "10": QUESTIONS_10,

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
        "2.1": QUESTIONS_2_1,
        "2.2": QUESTIONS_2_2,
        "2.3": QUESTIONS_2_3,
        "2.4": QUESTIONS_2_4,
        "2.5": QUESTIONS_2_5,
        "3.1": QUESTIONS_3_1,
        "3.2": QUESTIONS_3_2,
        "3.3": QUESTIONS_3_3,
        "3.4": QUESTIONS_3_4,
        "3.5": QUESTIONS_3_5,
        "3.6": QUESTIONS_3_6,
        "4.2": QUESTIONS_4_2,
        "4.3": QUESTIONS_4_3,
        "4.4": QUESTIONS_4_4,
        "4.5": QUESTIONS_4_5,
        "4.6": QUESTIONS_4_6,
        "4.7": QUESTIONS_4_7,
        "4.8": QUESTIONS_4_8,
        "5.1": QUESTIONS_5_1,
        "5.2": QUESTIONS_5_2,
        "5.3": QUESTIONS_5_3,
        "5.4": QUESTIONS_5_4,
        "6": QUESTIONS_6,
        "7": QUESTIONS_7,
        "8": QUESTIONS_8,
        "10": QUESTIONS_10,

    }
    return topic_map.get(topic_id, {})
