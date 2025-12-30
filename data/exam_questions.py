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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Was ist der Unterschied zwischen einem Elementarereignis und einem Ereignis? Was ist der Unterschied zwischen dem Ereignisraum und der Ereignismenge?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>What is the difference between an elementary event and an event? What is the difference between the sample space and the event set?</span>"""
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>**Welcher der folgenden Ereignisräume S ist stetig?**</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>**Which of the following sample spaces S is continuous?**</span>"""
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Sind komplementäre Ereignisse disjunkt? Sind disjunkte Ereignisse komplementär?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Are complementary events disjoint? Are disjoint events complementary?</span>"""
        },
        "solution": {
            "de": "**Antwort:**<br>• Komplementär ⇒ disjunkt (Ja)<br>• Disjunkt ⇒ nicht unbedingt komplementär (Nein)",
            "en": "**Answer:**<br>• Complementary ⇒ disjoint (Yes)<br>• Disjoint ⇒ not necessarily complementary (No)"
        }
    },
    "q_1_2_1_a": {
        "source": "Prüfungstraining 1.2.1 (A)",
        "question": {
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Werfen von zwei Würfeln ($|S|=36$). Ereignis $A$: 'Mindestens ein Würfel zeigt eine Sechs'. $P(A) = ?$</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Throwing two dice ($|S|=36$). Event $A$: 'At least one die shows a six'. $P(A) = ?$</span>"""
        },
        "options": [
            {"de": r"$\frac{10}{36}$", "en": r"$\frac{10}{36}$"},
            {"de": r"$\frac{11}{36}$", "en": r"$\frac{11}{36}$"},
            {"de": r"$\frac{1}{6}$", "en": r"$\frac{1}{6}$"},
            {"de": r"$\frac{12}{36}$", "en": r"$\frac{12}{36}$"}
        ],
        "correct_idx": 1,
        "solution": {
            "de": r"**Richtig! ($\frac{11}{36}$)**<br>Elemente: $\{(6,1), (6,2), \ldots, (6,6), (1,6), \ldots, (5,6)\}$. Das sind $6 + 5 = 11$.",
            "en": r"**Correct! ($\frac{11}{36}$)**<br>Elements: $\{(6,1), (6,2), \ldots, (6,6), (1,6), \ldots, (5,6)\}$. That is $6 + 5 = 11$."
        }
    },
    "q_1_2_1_b": {
        "source": "Prüfungstraining 1.2.1 (B)",
        "question": {
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Werfen von zwei Würfeln. Ereignis $B$: 'Die Augensumme ist 9'. $P(B) = ?$</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Throwing two dice. Event $B$: 'The sum of dots is 9'. $P(B) = ?$</span>"""
        },
        "options": [
            {"de": r"$\frac{3}{36}$", "en": r"$\frac{3}{36}$"},
            {"de": r"$\frac{4}{36}$", "en": r"$\frac{4}{36}$"},
            {"de": r"$\frac{5}{36}$", "en": r"$\frac{5}{36}$"},
            {"de": r"$\frac{1}{9}$", "en": r"$\frac{1}{9}$"}
        ],
        "correct_idx": 1,
        "solution": {
            "de": r"**Richtig! ($\frac{4}{36}$)**<br>Elemente: $\{(3,6), (4,5), (5,4), (6,3)\}$.",
            "en": r"**Correct! ($\frac{4}{36}$)**<br>Elements: $\{(3,6), (4,5), (5,4), (6,3)\}$."
        }
    },
    "q_1_2_1_c": {
        "source": "Prüfungstraining 1.2.1 (C)",
        "question": {
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Werfen von zwei Würfeln. Ereignis $C$: 'Die Augensumme ist kleiner als 4'. $P(C) = ?$</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Throwing two dice. Event $C$: 'The sum of dots is less than 4'. $P(C) = ?$</span>"""
        },
        "options": [
            {"de": r"$\frac{3}{36}$", "en": r"$\frac{3}{36}$"},
            {"de": r"$\frac{2}{36}$", "en": r"$\frac{2}{36}$"},
            {"de": r"$\frac{4}{36}$", "en": r"$\frac{4}{36}$"},
            {"de": r"$\frac{1}{12}$", "en": r"$\frac{1}{12}$"}
        ],
        "correct_idx": 0,
        "solution": {
            "de": r"**Richtig! ($\frac{3}{36}$)**<br>Elemente: $\{(1,1), (1,2), (2,1)\}$. Summe < 4 bedeutet Summe 2 oder 3.",
            "en": r"**Correct! ($\frac{3}{36}$)**<br>Elements: $\{(1,1), (1,2), (2,1)\}$. Sum < 4 means sum 2 or 3."
        }
    },
    "test1_q2": {
        "source": "Test 1, Frage 2",
        "question": {
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Es seien $A$ und $B$ zwei beliebige Ereignisse mit $P(A) = 0.6$, $P(B) = 0.7$ und $P(\overline{A} \cap B) = 0.1$. Berechnen Sie $P(A \cap \overline{B})$.</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Let $A$ and $B$ be two arbitrary events with $P(A) = 0.6$, $P(B) = 0.7$ and $P(\overline{A} \cap B) = 0.1$. Calculate $P(A \cap \overline{B})$.</span>"""
        },
        "options": [
            {"de": r"$0$", "en": r"$0$"},
            {"de": r"$0.1$", "en": r"$0.1$"},
            {"de": r"$0.2$", "en": r"$0.2$"},
            {"de": r"$0.3$", "en": r"$0.3$"}
        ],
        "correct_idx": 0,
        "solution": {
            "de": r"**Richtig: $0$**<br>Wir wissen $P(B) = P(A \cap B) + P(\overline{A} \cap B)$.<br>Also $0.7 = P(A \cap B) + 0.1 \Rightarrow P(A \cap B) = 0.6$.<br>Weiterhin ist $P(A) = P(A \cap B) + P(A \cap \overline{B})$.<br>Also $0.6 = 0.6 + P(A \cap \overline{B}) \Rightarrow P(A \cap \overline{B}) = 0$.",
            "en": r"**Correct: $0$**<br>We know $P(B) = P(A \cap B) + P(\overline{A} \cap B)$.<br>So $0.7 = P(A \cap B) + 0.1 \Rightarrow P(A \cap B) = 0.6$.<br>Furthermore $P(A) = P(A \cap B) + P(A \cap \overline{B})$.<br>So $0.6 = 0.6 + P(A \cap \overline{B}) \Rightarrow P(A \cap \overline{B}) = 0$."
        }
    },
    "test3_q1": {
        "source": "Test 3, Frage 1",
        "question": {
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Die Ereignisse $A$ und $B$ sind disjunkt mit $P(A)>0, P(B)>0$. Welche Aussage stimmt?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Events $A$ and $B$ are disjoint with $P(A)>0, P(B)>0$. Which statement is true?</span>"""
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>**Wann darf man die Laplace-Formel $P(A) = \frac{g}{m}$ verwenden?**</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>**When are you allowed to use the Laplace formula $P(A) = \frac{g}{m}$?**</span>"""
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>**Welche der folgenden Wahrscheinlichkeitszuweisungen ist ungültig?** ($S = \{e_1, e_2, e_3\}$)</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>**Which of the following probability assignments is invalid?** ($S = \{e_1, e_2, e_3\}$)</span>"""
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
             "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>**Gegeben sind:** $P(A)=0.3, P(B)=0.4, P(\overline{A}|B)=0.75$.\n\n**Gesucht ist:** $P(A \cup B)$.</span>""",
             "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>**Given:** $P(A)=0.3, P(B)=0.4, P(\overline{A}|B)=0.75$.\n\n**Find:** $P(A \cup B)$.</span>"""
        },
        "hint": {
             "de": r"Hinweis: Nutze zuerst das Komplement $P(A|B) = 1 - P(\overline{A}|B)$. Verwende dann die Multiplikationsregel: $P(A \cap B) = P(A|B) \cdot P(B)$.", 
             "en": r"Hint: First find $P(A|B) = 1 - P(\overline{A}|B)$. Then use the multiplication rule: $P(A \cap B) = P(A|B) \cdot P(B)$."
        },
        "options": [
            {"de": r"$0.55$", "en": r"$0.55$"},
            {"de": r"$0.60$", "en": r"$0.60$"},
            {"de": r"$0.70$", "en": r"$0.70$"},
            {"de": r"$0.25$", "en": r"$0.25$"}
        ],
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>5. (4 Punkte) Folgende Angaben sind gegeben: P (A) = 0.3, P (B) = 0.4, P A |B = 0.75. Wie
groß ist die Wahrscheinlichkeit von P (A ∪ B) ?
(a) 0.425
(b) 0.6
(c) 0.7
(d) Keine der obigen Angaben ist richtig.</span>""",
"en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>5. (4 Points) The following information is given: $P(A) = 0.3$, $P(B) = 0.4$, $P(A | B) = 0.75$. What is the probability of $P(A \cup B)$?
(a) 0.425
(b) 0.6
(c) 0.7
(d) None of the above.</span>"""
        },
        "options": [
            {"de": "0.425", "en": "0.425"},
            {"de": "0.6", "en": "0.6"},
            {"de": "0.7", "en": "0.7"},
            {"de": "Keine der obigen", "en": "Keine der obigen"}
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>$P(A)=0.5, P(B)=0.4, P(\overline{A \cup B}) = 0.2$. Dann gilt:</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>$P(A)=0.5, P(B)=0.4, P(\text{neither A nor B}) = 0.2$. Then:</span>"""
        },
        "options": [
            {"de": "A und B sind unvereinbar.", "en": "A und B sind unvereinbar."},
            {"de": "A und B sind nicht unvereinbar.", "en": "A und B sind nicht unvereinbar."},
            {"de": "A und B sind unabhängig.", "en": "A und B sind unabhängig."},
            {"de": "A und B sind nicht unabhängig.", "en": "A und B sind nicht unabhängig."}
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>A, B unabhängig. $P(A)=0.9, P(A \cup B)=0.5$. Dann gilt:</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>A, B independent. $P(A)=0.9, P(A \cup B)=0.5$. Then:</span>"""
        },
        "options": [
            {"de": r"$P(B) = 0.05$", "en": r"$P(B) = 0.05$"},
            {"de": r"$P(B) = 0.44$", "en": r"$P(B) = 0.44$"},
            {"de": r"$P(B) = 0.55$", "en": r"$P(B) = 0.55$"},
            {"de": "Nicht genügend Informationen.", "en": "Nicht genügend Informationen."}
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>In einem stetigen Raum (z.B. Dartscheibe), wie groß ist die Wahrscheinlichkeit, einen exakten Punkt zu treffen?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>In a continuous space (e.g. dartboard), what is the probability of hitting an exact point?</span>"""
        },
        "options": [
            {"de": r"$0$", "en": r"$0$"},
            {"de": "Unendlich klein, aber > 0", "en": "Unendlich klein, aber > 0"},
            {"de": r"$1$", "en": r"$1$"},
            {"de": "Abhängig vom Radius", "en": "Abhängig vom Radius"}
        ],
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>5. (4 Punkte) Es werden zufällig 4 Zahlen aus den ersten 12 Primzahlen ohne Zurücklegen ausgewählt. Betrachten Sie die beiden Ereignisse:<br>^ A: Die Summe der 4 ausgewählten Zahlen ist ungerade.<br>^ B: Alle vier ausgewählten Zahlen sind ungerade.<br>Welche der folgenden Aussagen ist richtig in Bezug auf die Ereignisse A und B?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>5. (4 Points) 4 numbers are randomly chosen from the first 12 prime numbers without replacement. Consider the two events:<br><br>- A: The sum of the 4 chosen numbers is odd.<br>- B: All four chosen numbers are odd.<br><br>Which of the following statements is true regarding events A and B?</span>"""
        },
        "options": [
            {"de": "Unabhängig und disjunkt.", "en": "Unabhängig und disjunkt."},
            {"de": "Unabhängig, aber nicht disjunkt.", "en": "Unabhängig, aber nicht disjunkt."},
            {"de": "Abhängig und disjunkt.", "en": "Abhängig und disjunkt."},
            {"de": "Abhängig und nicht disjunkt.", "en": "Abhängig und nicht disjunkt."}
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>$A$ und $B$ sind zwei unabhängige Ereignisse. Dann gilt:</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>$A$ and $B$ are two independent events. Then:</span>"""
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>$A$ und $B$ sind zwei disjunkte Ereignisse ($P(A)>0$). Dann gilt:</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>$A$ and $B$ are two disjoint events ($P(A)>0$). Then:</span>"""
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>$A$ und $B$ sind zwei unvereinbare (disjunkte) Ereignisse mit $P(A) > 0$ und $P(B) > 0$. Dann gilt:</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>$A$ and $B$ are two mutually exclusive (disjoint) events with $P(A) > 0$ and $P(B) > 0$. Then:</span>"""
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Gegeben: $P(A) = 0.5$, $P(B) = 0.3$, $P(A \cap B) = 0.2$.<br>Berechnen Sie:<br>(a) $P(A \cup B)$<br>(b) $P(A | B)$<br>(c) $P(A \cap \overline{B})$</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Given: $P(A) = 0.5$, $P(B) = 0.3$, $P(A \cap B) = 0.2$.<br>Calculate:<br>(a) $P(A \cup B)$<br>(b) $P(A | B)$<br>(c) $P(A \cap \overline{B})$</span>"""
        },
        "solution": {
            "de": r"**Lösung:**<br>(a) $P(A \cup B) = 0.5 + 0.3 - 0.2 = \mathbf{0.6}$<br>(b) $P(A | B) = 0.2 / 0.3 = \mathbf{2/3}$<br>(c) $P(A \cap \overline{B}) = P(A) - P(A \cap B) = 0.5 - 0.2 = \mathbf{0.3}$",
            "en": r"**Solution:**<br>(a) $P(A \cup B) = 0.5 + 0.3 - 0.2 = \mathbf{0.6}$<br>(b) $P(A | B) = 0.2 / 0.3 = \mathbf{2/3}$<br>(c) $P(A \cap \overline{B}) = P(A) - P(A \cap B) = 0.5 - 0.2 = \mathbf{0.3}$"
        }
    },
    "hs2023_mc1": {
        "source": "HS2023, MC1 (4 Punkte)",
        "question": {
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>1. Folgende Informationen sind gegeben: P (A) = 0, 5, P (B) = 0, 3, P (A ∪ B) = 0, 4.
Welche der folgenden Aussagen ist wahr?</span>""",
"en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>1. The following information is given: $P(A) = 0.5$, $P(B) = 0.3$, $P(A \cup B) = 0.4$. Which of the following statements is true?</span>"""
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>$A$ und $B$ sind Ereignisse. Es sei $P(A) = 1/2$, $P(B) = 2/3$ und $P(A \cap B) = 1/4$. $\bar{B}$ bezeichnet das Komplement von $B$. Wie gross ist der Wert von $P(A | \bar{B})$?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>$A$ and $B$ are events. Let $P(A) = 1/2$, $P(B) = 2/3$ and $P(A \cap B) = 1/4$. $\bar{B}$ denotes the complement of $B$. What is the value of $P(A | \bar{B})$?</span>"""
        },
        "options": [
            {"de": "0.25", "en": "0.25"},
            {"de": "0.50", "en": "0.50"},
            {"de": "0.75", "en": "0.75"},
            {"de": "0.33", "en": "0.33"}
        ],
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>**Zufallsexperiment:** Ziehen von 4 Zahlen aus den ersten 12 Primzahlen (ohne Zurücklegen).\n\n$A$: Summe ist ungerade.\n$B$: Alle 4 Zahlen sind ungerade.\n\n**Sind $A$ und $B$ unabhängig oder disjunkt?**</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>**Experiment:** Draw 4 numbers from the first 12 primes (without replacement).\n\n$A$: Sum is odd.\n$B$: All 4 numbers are odd.\n\n**Are $A$ and $B$ independent or disjoint?**</span>"""
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
    "hs2023_mc8": {
        "source": "HS 2023 Januar, MC #8",
        "type": "mc",
        "question": {
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>8. (4 Punkte) Seien A, B und C drei Ereignisse mit P(A) > 0, P(B) > 0 und P(C) > 0. Welche
der folgenden Aussagen ist wahr?
(a) Falls A unabhängig von B, und B unabhängig von C ist, dann ist A auch unabhängig von C.
(b) P(A|B) > P(A) ⇐⇒ P(A|B) < P(A)
(c) Wenn sich A und B gegenseitig ausschliessen, dann sind sie auch unabhängig.
(d) Keine der obigen Angaben ist richtig.</span>""",
"en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>8. (4 Points) Let A, B, and C be three events with P(A) > 0, P(B) > 0, and P(C) > 0. Which of the following statements is true?
(a) If A is independent of B, and B is independent of C, then A is also independent of C.
(b) P(A|B) > P(A) ⇐⇒ P(A|B^c) < P(A)
(c) If A and B are mutually exclusive, then they are also independent.
(d) None of the above statements is correct.</span>"""
        },
        "options": [
            {"de": "Falls A perp B und B perp C, dann A perp C.", "en": "Falls A perp B und B perp C, dann A perp C."},
            {"de": r"$P(A|B) > P(A) \iff P(A|B^c) < P(A)$", "en": r"$P(A|B) > P(A) \iff P(A|B^c) < P(A)$"},
            {"de": "Wenn A, B disjunkt, dann unabhängig.", "en": "Wenn A, B disjunkt, dann unabhängig."},
            {"de": "Keine der obigen.", "en": "Keine der obigen."}
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>9. (4 Punkte) A und B sind zwei Ereignisse mit P (A) > 0 und P (B) > 0, welche Aussage muss
wahr sein?
(a) P (A | B) · P (A) = P (B | A) · P (B)
(b) P (B) > P (A ∩ B)
(c) P (A) > P (A | B)
(d) Keine der oben genannten Möglichkeiten.</span>""",
"en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>9. (4 Points) A and B are two events with $P(A) > 0$ and $P(B) > 0$. Which statement must be true?
(a) $P(A | B) \cdot P(A) = P(B | A) \cdot P(B)$
(b) $P(B) > P(A \cap B)$
(c) $P(A) > P(A | B)$
(d) None of the above options.</span>"""
        },
        "options": [
            {"de": r"$P(A|B) \cdot P(A) = P(B|A) \cdot P(B)$", "en": r"$P(A|B) \cdot P(A) = P(B|A) \cdot P(B)$"},
            {"de": r"$P(B) > P(A \cap B)$", "en": r"$P(B) > P(A \cap B)$"},
            {"de": r"$P(A) > P(A|B)$", "en": r"$P(A) > P(A|B)$"},
            {"de": "Keine der oben genannten.", "en": "Keine der oben genannten."}
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>12. (4 Punkte) Sie haben zwei Wale. Ein Wal ist mit einer Wahrscheinlichkeit von 50% männlich,
ansonsten weiblich. Der Tag der Geburt eines Wals ist unabhängig vom Geschlecht, mit der
Wahrscheinlichkeit 71 für jeden Tag. Geben Sie das Verhältnis der bedingten Wahrscheinlichkeiten P (A|B) und P (A|C) an:
 Ereignis A: Beide Wale sind männlich.
 Ereignis B: Mindestens ein Wal ist männlich.
 Ereignis C: Mindestens ein Wal ist männlich UND an einem Dienstag geboren.
(a) P (A|B) = P (A|C)
(b) P (A|B) > P (A|C)
(c) P (A|B) < P (A|C)
(d) Nicht genügend Informationen gegeben.</span>""",
"en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>12. (4 Points) You have two whales. A whale is male with a probability of 50%, otherwise female. The day of birth of a whale is independent of gender, with probability 1/7 for each day. State the relationship between the conditional probabilities P(A|B) and P(A|C):
- Event A: Both whales are male.
- Event B: At least one whale is male.
- Event C: At least one whale is male AND born on a Tuesday.
(a) P(A|B) = P(A|C)
(b) P(A|B) > P(A|C)
(c) P(A|B) < P(A|C)
(d) Not enough information given.</span>"""
        },
        "options": [
            {"de": r"$P(A|B) = P(A|C)$", "en": r"$P(A|B) = P(A|C)$"},
            {"de": r"$P(A|B) > P(A|C)$", "en": r"$P(A|B) > P(A|C)$"},
            {"de": r"$P(A|B) < P(A|C)$", "en": r"$P(A|B) < P(A|C)$"},
            {"de": "Nicht genügend Infos.", "en": "Nicht genügend Infos."}
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>300 Hörer einer Statistik-Vorlesung:<br>VWL: $42$ m, $93$ w<br>BWL: $78$ m, $87$ w<br>Eine Hörerin wird gewählt. Wahrscheinlichkeit, dass sie BWL studiert?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>300 students in a stats lecture:<br>Econ: $42$ m, $93$ f<br>Bus: $78$ m, $87$ f<br>A female student is chosen. Probability she studies Business?</span>"""
        },
        "options": [
            {"de": r"$0.31$", "en": r"$0.31$"},
            {"de": r"$0.29$", "en": r"$0.29$"},
            {"de": r"$0.71$", "en": r"$0.71$"},
            {"de": r"$0.48$", "en": r"$0.48$"}
        ],
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Maschine $A$ produziert $70\%$ der Stücke ($8\%$ Fehlerquote). Maschine $B$ produziert $30\%$ ($6\%$ Fehlerquote). Ein zufällig gezogenes Stück ist fehlerhaft. Wie gross ist die Wahrscheinlichkeit, dass es von $A$ kommt?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Machine $A$ produces $70\%$ of parts ($8\%$ defect rate). Machine $B$ produces $30\%$ ($6\%$ defect rate). A randomly chosen part is defective. What is the probability it came from $A$?</span>"""
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Gymnasium-Statistik:<br>• $40\%$ bestehen die Matura nicht ($NM$)<br>• $90\%$ von $NM$ hatten negativen Aufnahmetest ($T-$)<br>• $1\%$ von Bestandenen ($M$) hatten negativen Test ($T-$)<br>Wie gross ist $P(T-)$?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>High School Statistics:<br>• $40\%$ fail the Matura ($NM$)<br>• $90\%$ of $NM$ had a negative admission test ($T-$)<br>• $1\%$ of those who passed ($M$) had a negative test ($T-$)<br>What is $P(T-)$?</span>"""
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Eine Maschine $A$ produziert $20\%$ aller Teile mit $5\%$ Fehler. Maschine $B$ produziert $80\%$ mit $1\%$ Fehler. Wie hoch ist die totale Fehlerrate?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Machine $A$ produces $20\%$ of all parts with $5\%$ defects. Machine $B$ produces $80\%$ with $1\%$ defects. What is the total defect rate?</span>"""
        },
        "options": [
            {"de": r"$3\%$", "en": r"$3\%$"},
            {"de": r"$1.8\%$", "en": r"$1.8\%$"},
            {"de": r"$6\%$", "en": r"$6\%$"},
            {"de": r"$2.5\%$", "en": r"$2.5\%$"}
        ],
        "correct_idx": 1,
        "solution": {
            "de": r"**Antwort: $1.8\%$**<br>Satz der totalen Wahrscheinlichkeit:<br>$P(D) = 0.05 \cdot 0.20 + 0.01 \cdot 0.80 = 0.01 + 0.008 = 0.018 = 1.8\%$",
            "en": r"**Answer: $1.8\%$**<br>Law of Total Probability:<br>$P(D) = 0.05 \cdot 0.20 + 0.01 \cdot 0.80 = 0.01 + 0.008 = 0.018 = 1.8\%$"
        }
    },
    "hs2022_mc2": {
        "source": "HS 2022 Januar, MC #2",
        "question": {
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>2. (4 Punkte) Sie haben 1000 Münzen und wissen, dass es unter den 1000 Münzen genau eine
besondere Münze gibt, die auf beiden Seiten Zahl hat. Sie wählen eine Münze zufällig aus
diesen 1000 aus. Sie werfen diese eine Münze 10 Mal. Sie zeigt 10 Mal hintereinander Zahl
an. Wie hoch ist die Wahrscheinlichkeit, dass Sie die besondere Münze genommen haben?
(a) 50.6%
(b) 1.8%
(c) 51.9%
(d) 2.9%</span>""",
"en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>2. (4 Points) You have $1000$ coins and know that among them there is exactly one special coin with tails on both sides. You randomly pick one coin and flip it $10$ times. It shows tails $10$ times in a row. What is the probability that you picked the special coin?</span>"""
        },
        "options": [
            {"de": r"$50.6\%$", "en": r"$50.6\%$"},
            {"de": r"$99.9\%$", "en": r"$99.9\%$"},
            {"de": r"$0.1\%$", "en": r"$0.1\%$"},
            {"de": r"$25\%$", "en": r"$25\%$"}
        ],
        "correct_idx": 0,
        "solution": {
            "de": r"**Richtig: $50.6\%$**<br>Bayes' Theorem:<br>$P(\text{special}|10T) = \frac{1 \cdot \frac{1}{1000}}{1 \cdot \frac{1}{1000} + (\frac{1}{2})^{10} \cdot \frac{999}{1000}} \approx 0.506$",
            "en": r"**Correct: $50.6\%$**<br>Bayes' Theorem:<br>$P(\text{special}|10T) = \frac{1 \cdot \frac{1}{1000}}{1 \cdot \frac{1}{1000} + (\frac{1}{2})^{10} \cdot \frac{999}{1000}} \approx 0.506$"
        }
    },
    "hs2022_mc1": {
        "source": "HS 2022 Januar, MC #1",
        "question": {
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>1. (4 Punkte) Drei Freunde spielen ein Spiel. Sie werfen eine faire Münze. Spieler 1 gewinnt,
wenn beim ersten Wurf Kopf herauskommt. Spieler zwei gewinnt, wenn beim zweiten Wurf
Kopf herauskommt. Spieler drei gewinnt, wenn beim dritten Wurf Kopf herauskommt. Wenn
bis zur dritten Runde kein Gewinner ermittelt wurde, beginnt das Spiel∑︁von neuem. Wie hoch
∞           a
ist die Wahrscheinlichkeit, dass Spieler 3 das Spiel gewinnt? Hinweis: i=0 a·k i = 1-k , wenn
der absolute Wert von k kleiner als 1 ist.
(a) 1/6
(b) 1/7
(c) 1/5
(d) 1/3</span>""",
"en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>1. (4 Points) Three friends play a game. They flip a fair coin. Player 1 wins on first flip heads. Player 2 wins on second flip heads. Player 3 wins on third flip heads. If no winner by round 3, game restarts. What is P(Player 3 wins)?</span>"""
        },
        "options": [
            {"de": "2/7", "en": "2/7"},
            {"de": "1/7", "en": "1/7"},
            {"de": "1/8", "en": "1/8"},
            {"de": "3/7", "en": "3/7"}
        ],
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Aufgabe 2 (10 Punkte)
Teil 2A (6 Punkte)
Gegeben sei eine Urne mit einer schwarzen und zwei roten Kugeln. Wir betrachten die Ereignisse
• R: “Es wird eine rote Kugel gezogen” und
• S: “Es wird eine schwarze Kugel gezogen”.
Es werde nun dreimal aus dieser Urne ohne Zurücklegen gezogen - die Urne ist also nach dem letzten
Zug leer.
1. (1 Punkte) Zeichnen Sie hierzu ein Baumdiagramm und zeichnen Sie die zugehörigen Wahrscheinlichkeiten ein.
2. (2 Punkte) Wie gross ist die Wahrscheinlichkeit, im zweiten Zug eine rote Kugel zu ziehen?
3. (3 Punkte) Nehmen Sie an, es wurde im zweiten Zug eine rote Kugel gezogen. Mit welcher Wahrscheinlichkeit wurde im ersten Zug ebenfalls eine rote Kugel gezogen?
Teil 2B (4 Punkte)
Bei einer Klausur werden 20 Multiple-Choice-Fragen mit jeweils vier angebotenen Antworten gestellt,
von denen genau eine richtig ist. Zum Bestehen der Klausur sind mindestens 12 richtige Antworten
notwendig.
1. (2 Punkte) Mit welcher Wahrscheinlichkeit p besteht ein Student die Prüfung, der bei jeder Frage
eine der vier Antwortmöglichkeiten als falsch erkennt und rein zufällig eine der restlichen drei
Antworten ankreuzt? (Ersatzergebnis: p = 0.015)
2. (2 Punkte) Die Klausur wird von 100 Studenten geschrieben, welche alle wie in der vorigen
Aufgabe beschrieben vorgehen. Was ist die Wahrscheinlichkeit, dass mindestens drei Studenten
die Klausur bestehen? Approximieren Sie die gegebene Wahrscheinlichkeit mittels der Poisson
Verteilung.
mehr Platz benötigen, machen Sie einen klaren Verweis auf dem Aufgabenblatt der Prüfung und beschriften Sie auch das zusätzliche
Blatt klar und deutlich. Die Aufgabe wird sonst nicht gewertet.</span>""",            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>**Part 2A (6 Points):** Urn with 1 black, 2 red balls. Draw without replacement (3 times).<br>1. Draw tree diagram.<br>2. P(red ball in 2nd draw)?<br>3. P(red in 1st | red in 2nd)?<br><br>**Part 2B (4 Points):** Multiple Choice Exam (20 questions, 4 answers, 12 needed).<br>1. Probability guesser passes (exclude 1 false, then guess)?<br>2. Poisson approximation for 100 students (at least 3 pass)?</span>"""
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>6. (4 Punkte) In einem Bewerbungsverfahren beträgt die Wahrscheinlichkeit, zu einem Vorstellungsgespräch eingeladen zu werden, 10%. Von denjenigen, die eingeladen werden, haben 90% in ihrer Statistikprüfung eine bessere Note als 5 erreicht. Umgekehrt haben von den Bewerbern, die nicht zu einem Vorstellungsgespräch eingeladen wurden, nur 20% eine bessere Note als 5 erreicht. Wie hoch ist die Wahrscheinlichkeit, dass ein zufällig ausgewählter Bewerber eine bessere Note als 5 in Statistik hat?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>6. (4 Points) In an application process, the probability of being invited to an interview is 10%. Of those invited, 90% achieved a grade better than 5 in their statistics exam. Conversely, of those not invited to an interview, only 20% achieved a grade better than 5. What is the probability that a randomly selected applicant has a grade better than 5 in statistics?</span>"""
        },
        "options": [
            {"de": "18%", "en": "18%"},
            {"de": "25%", "en": "25%"},
            {"de": "27%", "en": "27%"},
            {"de": "50%", "en": "50%"}
        ],
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Drei Gefangene ($A, B, C$). Einer wird begnadigt. Wärter nennt $B$ als Todeskandidat. Steigt $A$s Chance?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Three prisoners ($A, B, C$). One is pardoned. Warden names $B$ as executed. Does $A$'s chance increase?</span>"""
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
    "l2": {
        "source": "Level 2: Days of the Week (Laplace)",
        "question": {
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Wie hoch ist die Wahrscheinlichkeit, an einem Wochenende (Sa oder So) geboren zu sein?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>What is the probability of being born on a weekend (Sat or Sun)?</span>"""
        },
        "options": [
            {"de": r"$\frac{1}{7}$", "en": r"$\frac{1}{7}$"},
            {"de": r"$\frac{2}{7}$", "en": r"$\frac{2}{7}$"},
            {"de": r"$\frac{5}{7}$", "en": r"$\frac{5}{7}$"},
            {"de": r"$\frac{1}{14}$", "en": r"$\frac{1}{14}$"}
        ],
        "correct_idx": 1,
        "solution": {
            "de": r"**Richtig: $\frac{2}{7}$**<br>Günstige Ereignisse: 2 (Sa, So). Mögliche Ereignisse: 7. Annahme: Alle Tage gleich wahrscheinlich (Laplace).",
            "en": r"**Correct: $\frac{2}{7}$**<br>Favorable events: 2 (Sat, Sun). Possible events: 7. Assumption: All days equally likely (Laplace)."
        }
    },
    "l3": {
        "source": "Level 3: The Password (Combinatorics)",
        "question": {
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Ein 4-stelliger PIN-Code besteht aus den Ziffern 0-9. Wie viele Möglichkeiten gibt es?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>A 4-digit PIN code consists of the digits 0-9. How many possibilities are there?</span>"""
        },
        "options": [
            {"de": r"$3024 \; (10 \times 9 \times 8 \times 7)$", "en": r"$3024 \; (10 \times 9 \times 8 \times 7)$"},
            {"de": r"$10'000 \; (10^4)$", "en": r"$10'000 \; (10^4)$"},
            {"de": r"$40 \; (10 \times 4)$", "en": r"$40 \; (10 \times 4)$"},
            {"de": r"$5040 \; (7!)$", "en": r"$5040 \; (7!)$"}
        ],
        "correct_idx": 1,
        "solution": {
            "de": r"**Richtig: $10'000$**<br>Variation mit Wiederholung: $10^4$.",
            "en": r"**Correct: $10'000$**<br>Variation with repetition: $10^4$."
        }
    },
    "l4": {
        "source": "Level 4: Rare Disease (Bayes)",
        "question": {
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Krankheit ($1\%$ Prävalenz). Test ($99\%$ genau). Du testest positiv. Wie groß ist die Wahrscheinlichkeit, dass du wirklich krank bist?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Disease ($1\%$ prevalence). Test ($99\%$ accurate). You test positive. What is the probability you are actually sick?</span>"""
        },
        "options": [
            {"de": r"$99\%$", "en": r"$99\%$"},
            {"de": r"$50\%$", "en": r"$50\%$"},
            {"de": r"$1\%$", "en": r"$1\%$"},
            {"de": r"$90\%$", "en": r"$90\%$"}
        ],
        "correct_idx": 1,
        "solution": {
            "de": r"**Richtig: $50\%$**<br>Klassische Bayes-Falle. Bei seltenen Krankheiten gibt es viele Falsch-Positive.",
            "en": r"**Correct: $50\%$**<br>Classic Bayes Trap. Rare diseases produce many false positives."
        }
    },
    "l5": {
        "source": "Level 5: Roulette (Exp Value)",
        "question": {
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Du setzt $10$ CHF auf Rot ($18$ rote, $18$ schwarze, $1$ grüne Zahl). Gewinn: Verdoppelung. Was ist dein erwarteter Gewinn pro Spiel?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>You bet $10$ CHF on Red ($18$ red, $18$ black, $1$ green number). Win: Double up. What is your expected gain per game?</span>"""
        },
        "options": [
            {"de": r"$0$ CHF", "en": r"$0$ CHF"},
            {"de": r"$-0.27$ CHF", "en": r"$-0.27$ CHF"},
            {"de": r"$+0.50$ CHF", "en": r"$+0.50$ CHF"},
            {"de": r"$-10$ CHF", "en": r"$-10$ CHF"}
        ],
        "correct_idx": 1,
        "solution": {
            "de": r"**Richtig: $-0.27$ CHF**<br>$E[X] = \frac{18}{37} \cdot 10 + \frac{19}{37} \cdot (-10) = -\frac{10}{37} \approx -0.27$.",
            "en": r"**Correct: $-0.27$ CHF**<br>$E[X] = \frac{18}{37} \cdot 10 + \frac{19}{37} \cdot (-10) = -\frac{10}{37} \approx -0.27$."
        }
    },
    "l6": {
        "source": "Level 6: Waiting Time (Continuous)",
        "question": {
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Der Bus kommt alle $10$ Minuten (gleichverteilt). Du kommst 'zufällig' an. Wie lange wartest du im Durchschnitt?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>The bus comes every $10$ minutes (uniformly distributed). You arrive 'randomly'. How long do you wait on average?</span>"""
        },
        "options": [
            {"de": r"$10$ min", "en": r"$10$ min"},
            {"de": r"$1$ min", "en": r"$1$ min"},
            {"de": r"$5$ min", "en": r"$5$ min"},
            {"de": r"$0$ min", "en": r"$0$ min"}
        ],
        "correct_idx": 2,
        "solution": {
            "de": r"**Richtig: $5$ min**<br>Erwartungswert einer stetigen Gleichverteilung $[0, 10]$: $\frac{a+b}{2} = 5$.",
            "en": r"**Correct: $5$ min**<br>Expected value of continuous uniform distribution $[0, 10]$: $\frac{a+b}{2} = 5$."
        }
    }
}

QUESTIONS_1_10 = {}

QUESTIONS_1_11 = {}

# 2.1 Binomialkoeffizient
QUESTIONS_2_1 = {
    "q_2_1_scenario_mastery": {
        "source": "Konzept-Check 2.1",
        "question": {
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Warum teilen wir beim Binomialkoeffizienten durch k!?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Why do we divide by k! in the Binomial Coefficient?</span>"""
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>In einem Verein mit $10$ Mitgliedern ($4$ Frauen und $6$ Herren) soll nun ein Vorstand bestehend aus zwei Damen und zwei Herren gebildet werden. Wie viele Möglichkeiten gibt es?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>In a club with $10$ members ($4$ women and $6$ men), a board consisting of two women and two men is to be formed. How many possibilities are there?</span>"""
        },
        "options": [
            {"de": r"$90$", "en": r"$90$"},
            {"de": r"$25$", "en": r"$25$"},
            {"de": r"$210$", "en": r"$210$"},
            {"de": r"$60$", "en": r"$60$"}
        ],
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Sie besitzen **50 verschiedene DVDs** und die dazugehörigen 50 Hüllen. Auf wie viele Arten können die DVDs in die Hüllen einsortiert werden?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>You own **50 different DVDs** and their 50 cases. In how many ways can the DVDs be sorted into the cases?</span>"""
        },
        "options": [
            {"de": r"$50!$", "en": r"$50!$"},
            {"de": r"$50^{50}$", "en": r"$50^{50}$"},
            {"de": r"$1$", "en": r"$1$"},
            {"de": r"$\text{Binom}(50, 50)$", "en": r"$\text{Binom}(50, 50)$"}
        ],
        "correct_idx": 0,
        "solution": {
            "de": r"**Richtig: $50!$**<br>Permutation ohne Wiederholung.",
            "en": r"**Correct: $50!$**<br>Permutation without replacement."
        }
    },
    "test1_q3": {
        "source": "Test 1, Frage 3",
        "question": {
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Sie besitzen $50$ verschiedene DVDs und $50$ Hüllen. Ihr Neffe verteilt die DVDs zufällig. Wie viele Arten der Verteilung gibt es?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>You have $50$ different DVDs and $50$ cases. Your nephew distributes them randomly. How many arrangements are possible?</span>"""
        },
        "options": [
            {"de": r"$50!$", "en": r"$50!$"},
            {"de": r"$(50!)^2$", "en": r"$(50!)^2$"},
            {"de": r"$50! \cdot 49!$", "en": r"$50! \cdot 49!$"},
            {"de": r"$\binom{100}{2}$", "en": r"$\binom{100}{2}$"}
        ],
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>4. Herr Meyer hat seinen Schlüssel für das Schliessfach verloren. Die Schliessfachnummer leider vergessen. Er erinnert sich allerdings daran, dass es sich um eine vierstellige Zahl handelt, bei der zwei Ziffern gleich sind und dass als Ziffern die 3, 5 und 7 vorkommen. Wieviele Schliessfächer erfüllen diese Kriterien?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>4. Mr. Meyer has lost his locker key. Unfortunately, he has forgotten the locker number. However, he remembers that it is a four-digit number where two digits are the same and that the digits 3, 5, and 7 appear. How many lockers meet these criteria?</span>"""
        },
        "options": [
            {"de": "12", "en": "12"},
            {"de": "24", "en": "24"},
            {"de": "36", "en": "36"},
            {"de": "72", "en": "72"}
        ],
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Beim Schweizer Lotto '6 aus 49' wählt man 6 Zahlen aus 49. Wie viele verschiedene Tipps sind möglich?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>In Swiss Lotto '6 out of 49', you pick 6 numbers from 49. How many different tickets are possible?</span>"""
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Verein mit $10$ Mitgliedern ($4$ Frauen, $6$ Männer). Vorstand ($2$ Frauen, $2$ Männer) soll gebildet werden. Wie viele Möglichkeiten?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Club with $10$ members ($4$ women, $6$ men). Board ($2$ women, $2$ men) to be formed. How many possibilities?</span>"""
        },
        "options": [
            {"de": r"$89$", "en": r"$89$"},
            {"de": r"$210$", "en": r"$210$"},
            {"de": r"$90$", "en": r"$90$"},
            {"de": r"$75$", "en": r"$75$"}
        ],
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Eine Münze wird $4$ Mal geworfen. Wie viele Ergebnisfolgen?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>A coin is tossed $4$ times. How many outcome sequences?</span>"""
        },
        "options": [
            {"de": r"$24$", "en": r"$24$"},
            {"de": r"$16$", "en": r"$16$"},
            {"de": r"$6$", "en": r"$6$"},
            {"de": r"$8$", "en": r"$8$"}
        ],
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>50 DVDs und 50 Hüllen. Zufällige Verteilung. Wie viele Möglichkeiten?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>50 DVDs, 50 cases. Random arrangement. How many possibilities?</span>"""
        },
        "options": [
            {"de": r"$50!$", "en": r"$50!$"},
            {"de": r"$(50!)^2$", "en": r"$(50!)^2$"},
            {"de": r"$50! \cdot 49!$", "en": r"$50! \cdot 49!$"},
            {"de": r"$100$", "en": r"$100$"}
        ],
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>10 Mitglieder (4F, 6M). Vorstand: 2 Damen, 2 Herren. Anzahl Möglichkeiten?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>10 members (4 women, 6 men). Executive Board: 2 women, 2 men. Number of possibilities?</span>"""
        },
        "options": [
            {"de": "89", "en": "89"},
            {"de": "210", "en": "210"},
            {"de": "90", "en": "90"},
            {"de": "75", "en": "75"}
        ],
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
        "source": "Übung 2, MC #6",
        "type": "mc",
        "question": {
            "de": r"Eine Funktion $f(x) \ge 0$ ist eine Dichtefunktion, wenn:",
            "en": r"A function $f(x) \ge 0$ is a probability density function (PDF) if:"
        },
        "options": [
            {"de": r"$\sum f(x_i) = 1$.", "en": r"$\sum f(x_i) = 1$."},
            {"de": r"$\int_{-\infty}^{\infty} f(x) dx = 1$.", "en": r"$\int_{-\infty}^{\infty} f(x) dx = 1$."},
            {"de": r"die Fläche unterhalb gleich 1 ist.", "en": r"the area underneath is equal to 1."},
            {"de": r"$F(-\infty)=1$.", "en": r"$F(-\infty)=1$."},
            {"de": r"$F(-\infty)=0$ und $F(+\infty)=1$.", "en": r"$F(-\infty)=0$ and $F(+\infty)=1$."}
        ],
        "correct_idx": [1, 2, 4],
        "solution": {
            "de": r"**Richtig: (b), (c), (e)**<br>Eine Dichte muss zwei Dinge erfüllen:<br>1. Niemals negativ ($f(x) \ge 0$).<br>2. Gesamtfläche ist 1 (Normierung). Das ist Aussage (b) und (c).<br>(e) bezieht sich auf die Verteilungsfunktion CDF, ist aber auch eine korrekte Eigenschaft, die aus der Dichte folgt.",
            "en": r"**Correct: (b), (c), (e)**<br>Total Area = 1. Non-negative."
        }
    },
    "uebung2_prob2": {
        "source": "Übung 2, Problem 2",
        "type": "problem",
        "question": {
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Dreiecksverteilung: $f(x) = 2ax$ für $0<x<1$, $f(x) = 3a-ax$ für $1 \le x < 3$.<br>Bestimmen Sie $a$.</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Triangle distribution: $f(x) = 2ax$ for $0<x<1$, $f(x) = 3a-ax$ for $1 \le x < 3$.<br>Determine $a$.</span>"""
        },
        "solution": {
            "de": r"**Lösung: $a = \frac{1}{3}$**<br>Fläche unter dem Dreieck muss 1 sein.",
            "en": r"**Solution: $a = \frac{1}{3}$**<br>Area under the triangle must be 1."
        }
    },
    "hs2015_mc2": {
        "source": "HS 2015 Januar, MC #2 (4 Punkte)",
        "question": {
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>2. Sei X eine stetige Zufallsvariable mit kumulativer Verteilungsfunktion F (x). Welche
der folgenden Aussagen ist FALSCH?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>2. (4 Points) Let X be a continuous random variable with cumulative distribution function F(x). Which of the following statements is FALSCH (FALSE)?</span>"""
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
        "source": "Übung 2, MC #5",
        "type": "mc",
        "question": {
            "de": r"X diskret. $P(1 \le X < 2)$ ist:",
            "en": r"X discrete. $P(1 \le X < 2)$ is:"
        },
        "options": [
            {"de": r"$F(2) - F(1)$", "en": r"$F(2) - F(1)$"},
            {"de": r"$F(2) - F(1) - P(X=2)$", "en": r"$F(2) - F(1) - P(X=2)$"},
            {"de": r"$F(2) - F(1) + P(X=1)$", "en": r"$F(2) - F(1) + P(X=1)$"},
            {"de": r"$F(2) - F(1) - P(X=2) + P(X=1)$", "en": r"$F(2) - F(1) - P(X=2) + P(X=1)$"},
            {"de": r"$F(2) - F(1) + P(X=2)$", "en": r"$F(2) - F(1) + P(X=2)$"}
        ],
        "correct_idx": 3,
        "solution": {
            "de": r"**Richtig: (d)**<br>Formel: $F(2) - F(1) - P(X=2) + P(X=1)$.",
            "en": r"**Correct: (d)**<br>We need to adjust boundaries: Add $P(1)$ back, remove $P(2)$."
        }
    },
    "test2_q4": {
        "source": "Test 2, Frage 4",
        "question": {
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>$X$ diskret. PMF $f(x) = \frac{x+4}{c}$ für $x=1,\dots,5$. Für welches $c$ ist $f(x)$ eine PMF?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>$X$ discrete. PMF $f(x) = \frac{x+4}{c}$ for $x=1,\dots,5$. For which $c$ is $f(x)$ a PMF?</span>"""
        },
        "options": [
            {"de": r"$c = 20$", "en": r"$c = 20$"},
            {"de": r"$c = 25$", "en": r"$c = 25$"},
            {"de": r"$c = 30$", "en": r"$c = 30$"},
            {"de": r"$c = 35$", "en": r"$c = 35$"}
        ],
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>5. Es sei X eine diskrete Zufallsvariable mit einer Wahrscheinlichkeitsmassenfunktion
der Form
$$f(x) = \begin{cases} \frac{x+4}{c} & \text{für x = 1, . . . , 5} \\ 0 & \text{sonst.} \end{cases}$$
Für welchen Wert von c ist f (x) eine Wahrscheinlichkeitsmassenfunktion?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>5. Let $X$ be a discrete random variable with a probability mass function of the form $f(x) = \frac{x+4}{c}$ for $x = 1, \dots, 5$ and $0$ otherwise. For which value of $c$ is $f(x)$ a valid probability mass function?</span>"""
        },
        "options": [
            {"de": "c = 20", "en": "c = 20"},
            {"de": "c = 25", "en": "c = 25"},
            {"de": "c = 30", "en": "c = 30"},
            {"de": "c = 35", "en": "c = 35"}
        ],
        "correct_idx": 3,
        "solution": {
            "de": r"**Richtig: c = 35**<br>Summe der Wahrscheinlichkeiten muss 1 sein: $\sum_{x=1}^5 \frac{x+4}{c} = 1$.<br>Zähler-Summe: $(1+4)+(2+4)+(3+4)+(4+4)+(5+4) = 5+6+7+8+9 = 35$.<br>Also $35/c = 1 \Rightarrow c=35$.",
            "en": r"**Correct: c = 35**<br>Sum of probabilities must match 1: $\sum_{x=1}^5 \frac{x+4}{c} = 1$.<br>Numerator sum: $(1+4)+(2+4)+(3+4)+(4+4)+(5+4) = 5+6+7+8+9 = 35$.<br>Thus $35/c = 1 \Rightarrow c=35$."
        }
    },
    "hs2023_mc4": {
        "source": "HS 2023 Januar, MC #4 (4 Punkte)",
        "type": "mc",
        "question": {
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>4. Gegeben sei eine Zufallsvariable Y mit einer Wahrscheinlichkeitsdichtefunktion
$$f_Y(y) = \begin{cases} 2y & \text{for } 0 < y < 1 \\ 0 & \text{sonst.} \end{cases}$$
Wie gross ist die Varianz von Y ?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>4. (4 Points) Let Y be a random variable with a probability density function
$$f_Y(y) = \begin{cases} 2y & \text{for } 0 < y < 1 \\ 0 & \text{otherwise} \end{cases}$$
What is the variance of Y?</span>"""
        },
        "options": [
            {"de": r"$\frac{1}{2}$", "en": r"$\frac{1}{2}$"},
            {"de": r"$\frac{1}{18}$", "en": r"$\frac{1}{18}$"},
            {"de": r"$\frac{1}{3}$", "en": r"$\frac{1}{3}$"},
            {"de": r"$\frac{1}{4}$", "en": r"$\frac{1}{4}$"}
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>$X$ stetig auf $[0, 10]$ mit Dichte $f(x) = \frac{1}{20} + \frac{x}{100}$. Berechnen Sie $P(2 \le X \le 6)$.</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>$X$ continuous on $[0, 10]$ with density $f(x) = \frac{1}{20} + \frac{x}{100}$. Calculate $P(2 \le X \le 6)$.</span>"""
        },
        "options": [
            {"de": r"$\frac{9}{25} \; (0.36)$", "en": r"$\frac{9}{25} \; (0.36)$"},
            {"de": r"$\frac{2}{50}$", "en": r"$\frac{2}{50}$"},
            {"de": r"$\frac{12}{25}$", "en": r"$\frac{12}{25}$"},
            {"de": r"$\frac{3}{50}$", "en": r"$\frac{3}{50}$"}
        ],
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
        "source": "HS 2024 Januar, MC #7 (4 Punkte)",
        "type": "mc",
        "question": {
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>7. Sei Y eine stetige Zufallsvariable mit Dichtefunktion
$$f_Y(y) = \begin{cases} \frac{1}{2}\sin(y) & \text{für } 0 < y < \pi \\ 0 & \text{sonst.} \end{cases}$$
Wie gross ist der Erwartungswert von Y ?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>7. (4 Points) Let $Y$ be a continuous random variable with probability density function
$$f_Y(y) = \begin{cases} \frac{1}{2}\sin(y) & \text{for } 0 < y < \pi \\ 0 & \text{otherwise} \end{cases}$$
What is the expected value of $Y$?</span>"""
        },
        "options": [
            {"de": r"$\ln(\pi)$", "en": r"$\ln(\pi)$"},
            {"de": r"$\pi/2$", "en": r"$\pi/2$"},
            {"de": r"$\sqrt{2\pi}$", "en": r"$\sqrt{2\pi}$"},
            {"de": r"$3\pi/2$", "en": r"$3\pi/2$"}
        ],
        "correct_idx": 1,
        "solution": {
            "de": r"**Richtig: (b)**<br>Symmetrie-Argument: Die Dichte ist symmetrisch um $\pi/2$ im Intervall $[0, \pi]$. Daher ist der Erwartungswert die Mitte.",
            "en": r"**Correct: (b)**<br>Symmetry argument: The density is symmetric around $\pi/2$ in the interval $[0, \pi]$. Thus the expectation is the center."
        }
    },
    "hs2024_mc12": {
        "source": "HS 2024 Januar, MC #12 (4 Punkte)",
        "type": "mc",
        "question": {
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>12. Ein Brunnen enthält 10 Liter Wasser. Jeden Tag wird eine zufällige Menge Wasser aus dem Brunnen gepumpt. Die täglich gepumpte Wassermenge ist i.i.d. und gleichverteilt zwischen 0 und 1 Litern. Wie viele Tage dauert es im Durchschnitt, bis der Brunnen leer ist?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>12. (4 Points) A well contains 10 liters of water. Every day a random amount of water is pumped out of the well. The daily pumped amount is i.i.d. and uniformly distributed between 0 and 1 liters. How many days does it take on average until the well is empty?</span>"""
        },
        "options": [
            {"de": "12.5", "en": "12.5"},
            {"de": "15", "en": "15"},
            {"de": "17.5", "en": "17.5"},
            {"de": "20", "en": "20"}
        ],
        "correct_idx": 3,
        "solution": {
            "de": r"**Richtig: 20**<br>Durchschnittliche Entnahme pro Tag: $E[X] = 0.5$.<br>Waldsche Identität / Intuition: $n \cdot E[X] = 10 \Rightarrow n = 10/0.5 = 20$.",
            "en": r"**Correct: 20**<br>Average removal per day: $E[X] = 0.5$.<br>Wald's Identity / Intuition: $n \cdot E[X] = 10 \Rightarrow n = 10/0.5 = 20$."
        }
    },
    "hs2023_mc11": {
        "source": "HS 2023 Januar, MC #11 (4 Punkte)",
        "type": "mc",
        "question": {
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>11. Angenommen Sie würfeln. Für jeden Wurf erhalten Sie die Augenzahl als
Auszahlung. Erscheint die 4, 5 oder 6 so können Sie erneut würfeln. Sobald Sie 1, 2, oder
3 würfeln, endet das Spiel. Wie hoch ist der zu erwartende Gewinn dieses Spiels?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>11. (4 Points) Suppose you roll a die. For each roll, you receive the number of dots as a payoff. If 4, 5, or 6 appears, you can roll again. As soon as you roll 1, 2, or 3, the game ends. What is the expected payoff of this game?</span>"""
        },
        "options": [
            {"de": "3.5", "en": "3.5"},
            {"de": "5", "en": "5"},
            {"de": "6", "en": "6"},
            {"de": "7", "en": "7"}
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>$X$ ist gleichförmig verteilt auf $[0, 3]$ (Dichte $1/3$).<br>a) $E[X]$<br>b) $E[4X + 2]$</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>$X$ is uniformly distributed on $[0, 3]$ (density $1/3$).<br>a) $E[X]$<br>b) $E[4X + 2]$</span>"""
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Lernzeit Xenia:<br>• Schön ($1/10$): $20$ min<br>• Bewölkt ($1/3$): $60$ min<br>• Regen ($1/2$): $80$ min<br>• Schnee ($1/15$): $120$ min<br>Berechnen Sie den Erwartungswert.</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Xenia's study time:<br>• Sunny ($1/10$): $20$ min<br>• Cloudy ($1/3$): $60$ min<br>• Rain ($1/2$): $80$ min<br>• Snow ($1/15$): $120$ min<br>Calculate the expected value.</span>"""
        },
        "solution": {
            "de": r"**Lösung: $70$ Minuten**<br>$E[X] = 1/10 \cdot 20 + 1/3 \cdot 60 + 1/2 \cdot 80 + 1/15 \cdot 120 = 2 + 20 + 40 + 8 = 70$",
            "en": r"**Solution: $70$ minutes**<br>$E[X] = 1/10 \cdot 20 + 1/3 \cdot 60 + 1/2 \cdot 80 + 1/15 \cdot 120 = 2 + 20 + 40 + 8 = 70$"
        }
    },
    "hs2022_mc11": {
        "source": "HS 2022 Januar, MC #11 (4 Punkte)",
        "type": "mc",
        "question": {
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>11. Seien X, Y und Z 3 Zufallsvariablen mit E[X] = E[Y ], E[XY ] = 1 und E[X +
Y - 2Z] = -1. X und Y sind unabhängig. Wie groß ist der Wert von E[Z]?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>11. Let $X, Y$ and $Z$ be 3 random variables with $E[X] = E[Y]$, $E[XY] = 1$ and $E[X + Y - 2Z] = -1$. $X$ and $Y$ are independent. What is the value of $E[Z]$?</span>"""
        },
        "options": [
            {"de": "-0.5", "en": "-0.5"},
            {"de": "1.5", "en": "1.5"},
            {"de": "3", "en": "3"},
            {"de": "Nicht genügend Informationen.", "en": "Nicht genügend Informationen."}
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
        "source": "Übung 2, MC #8",
        "type": "mc",
        "question": {
            "de": r"$f(x) = \frac{1}{18}x$ für $x \in [0, 6]$. Varianz $V(X)$?",
            "en": r"$f(x) = \frac{1}{18}x$ on $[0, 6]$. Variance $V(X)$?"
        },
        "options": [
            {"de": r"3", "en": r"3"},
            {"de": r"18", "en": r"18"},
            {"de": r"9", "en": r"9"},
            {"de": r"14/3", "en": r"14/3"},
            {"de": r"2", "en": r"2"}
        ],
        "correct_idx": 4,
        "solution": {
            "de": r"**Richtig: (e)**<br>$E[X] = 4$. $E[X^2] = 18$.<br>$V(X) = 18 - 4^2 = 2$.",
            "en": r"**Correct: (e)**<br>$E[X]=4, E[X^2]=18, V(X)=2$."
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
            {"de": r"sie nur abzählbar viele Werte annehmen kann.", "en": r"it can only take countably many values."},
            {"de": r"sie überabzählbar viele Werte annehmen kann.", "en": r"it can take uncountably many values."},
            {"de": r"sie nur endlich viele Werte annehmen kann.", "en": r"it can only take finitely many values."},
            {"de": r"sie unendlich viele Werte annehmen kann.", "en": r"it can take infinitely many values."},
            {"de": r"ihre Verteilungsfunktion nur als Treppenfunktion gezeichnet werden kann.", "en": r"its CDF can only be drawn as a step function."}
        ],
        "correct_idx": [0, 2, 4],
        "solution": {
            "de": r"**Richtig: (a), (c), (e)**<br>Diskret heißt \"Körnig\". Wie Sandkörner oder LEGO-Steine.<br>Man kann die Werte \"durchnummerieren\" (1, 2, 3...). Es gibt Lücken dazwischen.<br>Das Gegenteil ist \"Stetig\" (wie Wasser oder eine Linie), wo es keine Lücken gibt.<br>*   (a) Richtig (Definition).<br>*   (c) Auch richtig (Endlich ist ein Spezialfall von Abzählbar).<br>*   (e) Richtig. Da die Wahrscheinlichkeit an einzelnen Punkten \"klebt\", springt die kumulative Kurve (CDF) in Stufen hoch.",
            "en": r"**Correct: (a), (c), (e)**<br>Discrete means \"Grainy\" (like integers).<br>The values are countable. There are gaps.<br>The CDF looks like a staircase."
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
            {"de": r"sie nur abzählbar viele Werte annehmen kann.", "en": r"it can only take countably many values."},
            {"de": r"sie überabzählbar viele Werte annehmen kann.", "en": r"it can take uncountably many values."},
            {"de": r"sie nur endlich viele Werte annehmen kann.", "en": r"it can only take finitely many values."},
            {"de": r"sie unendlich viele Werte annehmen kann.", "en": r"it can take infinitely many values."},
            {"de": r"ihre Verteilungsfunktion nur als Treppenfunktion gezeichnet werden kann.", "en": r"its CDF can only be drawn as a step function."}
        ],
        "correct_idx": [1, 3],
        "solution": {
            "de": r"**Richtig: (b), (d)**<br>Stetig heißt \"Fließend\". Wie Zeit oder Temperatur.<br>Zwischen zwei beliebigen Werten gibt es unendlich viele weitere Werte.<br>Es gibt *überabzählbar* viele Möglichkeiten (wie die reellen Zahlen).",
            "en": r"**Correct: (b), (d)**<br>Continuous means \"Fluid\". Like time or distance.<br>Uncountably many values."
        }
    },
    "uebung2_mc3": {
        "source": "Übung 2, MC #3",
        "type": "mc",
        "question": {
            "de": r"Der Erwartungswert einer Verteilung:",
            "en": r"The expectation of a distribution:"
        },
        "options": [
            {"de": r"ist der Wert, unter dem 50% der Masse liegt (Median).", "en": r"is the value below which 50% of the mass lies (Median)."},
            {"de": r"ist der erwartete Wert vor dem Experiment.", "en": r"is the expected value before the experiment."},
            {"de": r"ist der Wert, an dem die Dichte maximal ist (Modus).", "en": r"is the value where the density is maximal (Mode)."},
            {"de": r"ist der Schwerpunkt einer Verteilung.", "en": r"is the center of gravity of a distribution."},
            {"de": r"ist bei diskreten Verteilungen der wahrscheinlichste Wert.", "en": r"is the most probable value for discrete distributions."}
        ],
        "correct_idx": [1, 3],
        "solution": {
            "de": r"**Richtig: (b), (d)**<br>Der Erwartungswert ist der physikalische **Schwerpunkt** (Center of Gravity).<br>Wenn du die Verteilungskurve aus Pappe ausschneiden würdest, könntest du sie genau an diesem Punkt auf einer Nadelspitze balancieren.",
            "en": r"**Correct: (b), (d)**<br>Center of Gravity. The balance point."
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
            {"de": r"$\sum (x_i f(x_i) - E[X])^2$", "en": r"$\sum (x_i f(x_i) - E[X])^2$"},
            {"de": r"ein Mass für die Streuung.", "en": r"a measure of dispersion."},
            {"de": r"ein Mass für den Schwerpunkt.", "en": r"a measure of the center of gravity."},
            {"de": r"die quadrierte Standardabweichung.", "en": r"the squared standard deviation."},
            {"de": r"$\sum x_i^2 f(x_i) - E[X^2]$", "en": r"$\sum x_i^2 f(x_i) - E[X^2]$"}
        ],
        "correct_idx": [1, 3],
        "solution": {
            "de": r"**Richtig: (b), (d)**<br>* (a) Falsch. Korrekt wäre: $\sum (x_i - E[X])^2 f(x_i)$. Das $f(x_i)$ gehört nach draußen als Gewicht.<br>* (b) Richtig.<br>* (d) Richtig ($\sigma^2$).<br>* (e) Falsch. Korrekt wäre $E[X^2] - (E[X])^2$ (Verschiebungssatz).",
            "en": r"**Correct: (b), (d)**<br>(a) Wrong brackets.<br>(e) Wrong shift formula terms.<br>(b) and (d) are correct definitions."
        }
    },
    "uebung2_mc7": {
        "source": "Übung 2, MC #7",
        "type": "mc",
        "question": {
            "de": r"$f(x) = \frac{1}{2}x^2 - b$ für $1 \le x \le 2$, sonst 0. Für welches $b$ ist dies eine Dichte?",
            "en": r"$f(x) = \frac{1}{2}x^2 - b$ for $1 \le x \le 2$, otherwise 0. For which $b$ is this a density?"
        },
        "options": [
            {"de": r"$b=1/2$", "en": r"$b=1/2$"},
            {"de": r"$b=1/3$", "en": r"$b=1/3$"},
            {"de": r"$b=1/6$", "en": r"$b=1/6$"},
            {"de": r"$b=1$", "en": r"$b=1$"},
            {"de": r"Keine Dichte möglich.", "en": r"No density possible."}
        ],
        "correct_idx": 2,
        "solution": {
            "de": r"**Richtig: (c)**<br>Integral gleich 1 setzen: $\int_1^2 (\frac{1}{2}x^2 - b) dx = 1 \implies b = 1/6$.",
            "en": r"**Correct: (c)**<br>Integral condition gives $b=1/6$."
        }
    },
    "test2_mc2": {
        "source": "Test 2, Q2",
        "type": "mc",
        "question": {
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>$X \sim U[-4, 4]$. $P(X^2 \le 9)$?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>$X \sim U[-4, 4]$. $P(X^2 \le 9)$?</span>"""
        },
        "options": [
            {"de": "7/9", "en": "7/9"},
            {"de": "4/9", "en": "4/9"},
            {"de": "2/3", "en": "2/3"},
            {"de": "3/4", "en": "3/4"}
        ],
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>$X$ auf $[0, 10]$ mit Dichte $f(x) = \frac{x}{100} + \frac{1}{20}$. $P(2 \le X \le 6)$?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>$X$ on $[0, 10]$ with pdf $f(x) = x/100 + 1/20$. $P(2 \le X \le 6)$?</span>"""
        },
        "options": [
            {"de": "9/25", "en": "9/25"},
            {"de": "2/50", "en": "2/50"},
            {"de": "1/12", "en": "1/12"},
            {"de": "3/50", "en": "3/50"}
        ],
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Diskrete ZV $f(x) = \frac{x+4}{c}$ für $x=1,..,5$. Bestimme c.</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Discrete RV $f(x) = (x+4)/c$ for $x=1..5$. Find c.</span>"""
        },
        "options": [
            {"de": "20", "en": "20"},
            {"de": "25", "en": "25"},
            {"de": "30", "en": "30"},
            {"de": "35", "en": "35"}
        ],
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>$Y = X/\sigma$. $E(Y^2)$?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>$Y = X/\sigma$. $E(Y^2)$?</span>"""
        },
        "options": [
            {"de": "1", "en": "1"},
            {"de": r"$1 - \mu^2/\sigma^2$", "en": r"$1 - \mu^2/\sigma^2$"},
            {"de": r"$1 + \mu^2/\sigma^2$", "en": r"$1 + \mu^2/\sigma^2$"},
            {"de": "N/A", "en": "N/A"}
        ],
        "correct_idx": 2,
        "solution": {
            "de": r"**Richtig: (c)**<br>$E[Y^2] = Var(Y) + E[Y]^2 = 1/\sigma^2 \cdot Var(X) + (\mu/\sigma)^2 = 1 + \mu^2/\sigma^2$.",
            "en": r"**Correct: (c)**<br>$E[Y^2] = Var(Y) + E[Y]^2 = 1/\sigma^2 \cdot Var(X) + (\mu/\sigma)^2 = 1 + \mu^2/\sigma^2$."
        }
    }
}

QUESTIONS_3_6 = {}


# =============================================================================
# PART III: VERTEILUNGEN (Distributions)
# =============================================================================

# 4.2 Bernoulli
QUESTIONS_4_2 = {
    "uebung2_bb_prob1": {
        "source": "Übung 2, Problem 1 (Basketball)",
        "type": "problem",
        "question": {
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Basketball: Trefferquote $p = 1/2$. Vier Würfe.<br>Berechnen Sie $E[X]$ und $V(X)$.</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Basketball: Hit rate $p = 1/2$. Four shots.<br>Calculate $E[X]$ and $V(X)$.</span>"""
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Miguel gewinnt Giro d'Italia mit $30\%$. Wahrscheinlichkeit bei $5$ Teilnahmen mind. $2$ mal zu gewinnen?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Miguel wins Giro d'Italia with $30\%$. Probability to win at least $2$ times in $5$ participations?</span>"""
        },
        "options": [
            {"de": r"$0.639$", "en": r"$0.639$"},
            {"de": r"$0.472$", "en": r"$0.472$"},
            {"de": r"$0.600$", "en": r"$0.600$"},
            {"de": r"$0.360$", "en": r"$0.360$"}
        ],
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Herr Kaiser verkauft bei $20\%$ ($2$ von $10$) eine Versicherung. Er macht $16$ Besuche pro Tag.<br>Berechnen Sie $E[X]$ und $Var(X)$.</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Mr. Kaiser sells insurance in $20\%$ ($2$ of $10$) of visits. He makes $16$ visits per day.<br>Calculate $E[X]$ and $Var(X)$.</span>"""
        },
        "solution": {
            "de": r"**Lösung:**<br>$E[X] = 16 \cdot 0.2 = \mathbf{3.2}$<br>$Var(X) = 16 \cdot 0.2 \cdot 0.8 = \mathbf{2.56}$",
            "en": r"**Solution:**<br>$E[X] = 16 \cdot 0.2 = \mathbf{3.2}$<br>$Var(X) = 16 \cdot 0.2 \cdot 0.8 = \mathbf{2.56}$"
        }
    },
    "hs2022_mc7": {
        "source": "HS 2022 Januar, MC #7 (4 Punkte)",
        "question": {
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>7. Zwei Spieler stehen sich in einem Best-of-5-Spiel gegenüber, d.h. der erste Spieler,
der 3 Runden gewinnt, gewinnt das Spiel. Bei jeder Runde hat Spieler A eine 60%ige Chance
zu gewinnen und Spieler B eine 40%ige Chance (es gibt keine Unentschieden). Nach einer
Runde geht Spieler B in Führung und hat nun einen Vorsprung von eins in der Best-of-
5-Serie. Wie hoch ist die Wahrscheinlichkeit, dass Spieler B nach dieser ersten Runde das
gesamte Spiel gewinnt?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>7. Two players face each other in a Best-of-5 game, i.e., the first player to win 3 rounds wins the game. In each round, Player A has a 60% chance of winning and Player B has a 40% chance (there are no draws). After one round, Player B takes the lead and now has a lead of one in the Best-of-5 series. What is the probability that Player B wins the entire game after this first round?</span>"""
        },
        "options": [
            {"de": r"$65\%$", "en": r"$65\%$"},
            {"de": r"$35\%$", "en": r"$35\%$"},
            {"de": r"$50\%$", "en": r"$50\%$"},
            {"de": r"$80\%$", "en": r"$80\%$"}
        ],
        "correct_idx": 0,
        "solution": {
            "de": r"**Richtig: $65\%$**<br>$X \sim \text{Bin}(7, 0.7)$.<br>$P(X \ge 5) = P(X=5) + P(X=6) + P(X=7) \approx 0.65$",
            "en": r"**Correct: $65\%$**<br>$X \sim \text{Bin}(7, 0.7)$.<br>$P(X \ge 5) = P(X=5) + P(X=6) + P(X=7) \approx 0.65$"
        }
    },
    "hs2023_mc12": {
        "source": "HS 2023 Januar, MC #12 (4 Punkte)",
        "question": {
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>12. Jacob möchte sein Wissen, das er während des Statistikunterrichts erworben hat, nutzen, um im Casino etwas Geld zu gewinnen. In seinem Lieblingscasino in Paris gibt es 100 Spielautomaten. Das Casino kann die Gewinnwahrscheinlichkeit an einem Spielautomaten beeinflussen und fixiert diese bei 20%. Jacob möchte wissen: Wie groß ist die Wahrscheinlichkeit, an mindestens 4 der 100 Spielautomaten mehr als zweimal zu gewinnen, wenn er an jedem Automaten fünf Spiele spielt?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>12. Jacob wants to use the knowledge he acquired during statistics class to win some money at the casino. In his favorite casino in Paris, there are 100 slot machines. The casino can influence the winning probability at a slot machine and fixes it at 20%. Jacob wants to know: What is the probability of winning more than twice at at least 4 of the 100 slot machines if he plays five games at each machine?</span>"""
        },
        "options": [
            {"de": r"0.0579", "en": r"0.0579"},
            {"de": r"0.8372", "en": r"0.8372"},
            {"de": r"0.9421", "en": r"0.9421"},
            {"de": r"0.1628", "en": r"0.1628"}
        ],
        "correct_idx": 1,
        "solution": {
            "de": r"**Richtig: $0.8372$ (b)**<br>Zweistufig:<br>1) $P(X>2)$ für $\text{Bin}(5, 0.2) \approx 0.0579$.<br>2) $Y \sim \text{Bin}(100, 0.0579)$. $P(Y \ge 4) \approx 0.8372$.",
            "en": r"**Correct: $0.8372$ (b)**<br>Two-stage:<br>1) $P(X>2)$ for $\text{Bin}(5, 0.2) \approx 0.0579$.<br>2) $Y \sim \text{Bin}(100, 0.0579)$. $P(Y \ge 4) \approx 0.8372$."
        }
    }
}

# 4.4 Poisson
QUESTIONS_4_4 = {
    "uebung2_typo": {
        "source": "Übung 2, Problem 3 (Druckfehler)",
        "type": "problem",
        "question": {
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Buch hat im Mittel $\mu = 8$ Druckfehler (Poisson).<br>a) $P(X \ge 6)$?<br>b) $P(X = 13)$?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Book has on average $\mu = 8$ typos (Poisson).<br>a) $P(X \ge 6)$?<br>b) $P(X = 13)$?</span>"""
        },
        "solution": {
            "de": r"**Lösung:**<br>a) $1 - P(X \le 5) \approx \mathbf{0.8088}$<br>b) $(8^{13} \cdot e^{-8}) / 13! \approx \mathbf{0.0296}$",
            "en": r"**Solution:**<br>a) $1 - P(X \le 5) \approx \mathbf{0.8088}$<br>b) $(8^{13} \cdot e^{-8}) / 13! \approx \mathbf{0.0296}$"
        }
    },
    "test4_q1": {
        "source": "Test 4, Frage 1",
        "question": {
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Sei $X \sim \text{Poisson}(10)$ und $Z = 2X$. Welche Aussage trifft NICHT zu?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Let $X \sim \text{Poisson}(10)$ and $Z = 2X$. Which statement is FALSE?</span>"""
        },
        "options": [
            {"de": r"$Z \sim \text{Poisson}(20)$", "en": r"$Z \sim \text{Poisson}(20)$"},
            {"de": r"$\text{Var}(Z) = 40$", "en": r"$\text{Var}(Z) = 40$"},
            {"de": r"$\text{Corr}(X, Z) = 1$", "en": r"$\text{Corr}(X, Z) = 1$"},
            {"de": r"$E[Z] = 20$", "en": r"$E[Z] = 20$"}
        ],
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>$X$ gleichverteilt auf $[-4, 4]$. Wie gross ist $P(X^2 \le 9)$?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>$X$ uniformly distributed on $[-4, 4]$. What is $P(X^2 \le 9)$?</span>"""
        },
        "options": [
            {"de": r"$\frac{7}{9}$", "en": r"$\frac{7}{9}$"},
            {"de": r"$\frac{4}{9}$", "en": r"$\frac{4}{9}$"},
            {"de": r"$\frac{2}{3}$", "en": r"$\frac{2}{3}$"},
            {"de": r"$\frac{3}{4}$", "en": r"$\frac{3}{4}$"}
        ],
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
        "source": "Übung 2, MC #12",
        "type": "mc",
        "question": {
            "de": r"Autobatterie Erwartung 10000 km. $P(X > 20000)$? (Annahme Exponential).",
            "en": r"Car battery expected 10000 km. $P(X > 20000)$? (Assume Exponential)."
        },
        "options": [
            {"de": r"0.865", "en": r"0.865"},
            {"de": r"0.607", "en": r"0.607"},
            {"de": r"0.5", "en": r"0.5"},
            {"de": r"0.393", "en": r"0.393"},
            {"de": r"0.135", "en": r"0.135"}
        ],
        "correct_idx": 4,
        "solution": {
            "de": r"**Richtig: (e)**<br>$P(X > 20000) = e^{-(1/10000) \cdot 20000} = e^{-2} \approx 0.135$.",
            "en": r"**Correct: (e)**<br>$e^{-2} = 0.135$."
        }
    },
    "hs2022_mc4": {
        "source": "HS 2022 Januar, MC #4 (4 Punkte)",
        "type": "mc",
        "question": {
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>4. Für welchen Wert von c ist die Funktion
$$f(x) = \begin{cases} ce^{-0.8x} & \text{for } x \ge 0 \\ 0 & \text{for } x < 0 \end{cases}$$
eine Dichtefunktion?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>4. (4 Points) For which value of $c$ is the function
$$f(x) = \begin{cases} ce^{-0.8x} & \text{for } x \ge 0 \\ 0 & \text{for } x < 0 \end{cases}$$
a density function?</span>"""
        },
        "options": [
            {"de": r"$c = \frac{5}{4}$", "en": r"$c = \frac{5}{4}$"},
            {"de": r"$c = \frac{1}{2}$", "en": r"$c = \frac{1}{2}$"},
            {"de": r"$c = -\frac{9}{7}$", "en": r"$c = -\frac{9}{7}$"},
            {"de": r"$c = \frac{4}{5}$", "en": r"$c = \frac{4}{5}$"}
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Aufgabe 3 (18 Punkte)
Davide hat sich ein neues Motorrad gekauft und fährt damit nun täglich. Da er häufig auf Kieswegen
fährt, hat Davide oft einen platten Reifen. Die Zufallsvariable T1 beschreibt die Lebensdauer eines
Reifens in Tagen (d.h. die Zeit bis er platt ist). Nehmen Sie an T1 ist exponential verteilt mit der
folgenden Wahrscheinlichkeitsdichtefunktion
$$f(t) = \begin{cases} \frac{1}{500} \exp\left(-\frac{t}{500}\right) & \text{für } t \ge 0 \\ 0 & \text{sonst.} \end{cases}$$
1. (2 Punkte) Berechnen Sie die kumulative Verteilungsfunktion F (t).
2. (2 Punkte) Wie gross ist die Wahrscheinlichkeit, dass der vordere Reifen länger als 500 Tage keine
Reifenpanne aufweist?
3. (2 Punkte) Welche Lebensdauer wird von dem vorderen Reifen mit einer Wahrscheinlichkeit von
0.2 überschritten?
Wir betrachten nun zusätzlich die Zufallsvariable T2 , welche die Lebensdauer (in Tagen) des hinteren
Reifens beschreibt. Wir nehmen an, dass T1 und T2 unabhängige und identisch verteilte Zufallsvariablen
sind.
Sobald ein Reifen platt ist, ersetzt Davide beide Reifen durch neue. Die Zufallsvariable T bezeichnet die
Anzahl Tage zwischen dem Ersetzen der beiden Reifen bis zum nächsten Mal, dass die Reifen gewechselt
werden müssen. (Hinweis: Es gilt T = min(T1 , T2 ))
4. (6 Punkte) Berechnen Sie die kumulative Verteilungsfunktion von T . (Ersatzergebnis: T ∼ Exp(λ)
mit λ = 220 ).
5. (6 Punkte) Davide besitzt 20 Paar Reifen. Sobald ein Reifen platt ist, ersetzt er das alte Paar
Reifen durch ein neues Paar. Sobald er keine Reifen mehr übrig hat, will er sich ein Auto kaufen.
Nehmen Sie an, dass die Lebenszeiten aller Reifenpaare identisch und unabhängig verteilt sind.
Nehmen Sie ausserdem an, dass die Verteilung für jedes Reifenpaar derjenigen aus der vorigen
Teilaufgabe entspricht.
Berechnen Sie die ungefähre Wahrscheinlichkeit, dass Davide mit dieser Vorgehensweise nach
frühestens 15 Jahren ein Auto kauft (1 Jahr = 365 Tage).
mehr Platz benötigen, machen Sie einen klaren Verweis auf dem Aufgabenblatt der Prüfung und beschriften Sie auch das zusätzliche
Blatt klar und deutlich. Die Aufgabe wird sonst nicht gewertet.</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Problem 3 (18 Points)
Davide bought a new motorcycle and rides it daily. Since he often rides on gravel paths, Davide often gets a flat tire. The random variable $T_1$ describes the lifespan of a tire in days (i.e., the time until it is flat). Assume $T_1$ is exponentially distributed with the following probability density function:
$$f(t) = \begin{cases} \frac{1}{500} \exp\left(-\frac{t}{500}\right) & \text{for } t \ge 0 \\ 0 & \text{otherwise} \end{cases}$$
1. (2 Points) Calculate the cumulative distribution function $F(t)$.
2. (2 Points) What is the probability that the front tire has no flat tire for longer than 500 days?
3. (2 Points) Which lifespan is exceeded by the front tire with a probability of 0.2?
We now additionally consider the random variable $T_2$, which describes the lifespan (in days) of the rear tire. We assume that $T_1$ and $T_2$ are independent and identically distributed random variables.
As soon as a tire is flat, Davide replaces both tires with new ones. The random variable T describes the number of days between the replacing of the two tires until the next time the tires must be changed. (Hint: $T = \min(T_1, T_2)$)
4. (6 Points) Calculate the cumulative distribution function of T. (Alternative result: $T \sim \text{Exp}(\lambda)$ with $\lambda = \frac{1}{220}$).
5. (6 Points) Davide owns 20 pairs of tires. As soon as a tire is flat, he replaces the old pair of tires with a new pair. As soon as he has no tires left, he wants to buy a car. Assume that the lifespans of all tire pairs are identically and independently distributed. Also assume that the distribution for each tire pair corresponds to that from the previous question.
Calculate the probability that he can ride his motorcycle for more than 15 years (1 year = 365 days) before he has to buy a car. (Hint: Use the Central Limit Theorem).</span>"""
        },
        "solution": {
            "de": r"**Lösung:**<br>1. $F(t) = 1 - e^{-t/500}$.<br>2. $e^{-1} \approx 0.368$.<br>3. $x \approx 805$ Tage.<br>4. $T \sim \text{Exp}(1/250)$.<br>5. Summe von 20 Exp-Variablen $\to$ Näherung durch Normalverteilung (CLT). $P(S > 5475) \approx 0.39$.",
            "en": r"**Solution:**<br>1. $F(t) = 1 - e^{-t/500}$.<br>2. $e^{-1} \approx 0.368$.<br>3. $x \approx 805$ days.<br>4. $T \sim \text{Exp}(1/250)$.<br>5. Sum of 20 Exp variables $\to$ Approx via Normal (CLT). $P(S > 5475) \approx 0.39$."
        }
    },

}

# 4.7 Normalverteilung
QUESTIONS_4_7 = {
    "hs2023_mc7": {
        "source": "HS 2023 Januar, MC #7 (4 Punkte)",
        "type": "mc",
        "question": {
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>7. Die ausführliche Analyse von Prüfungsergebnissen eines Statistik Kurses an
einer Schweizer Universität hat ergeben, dass Studenten durchschnittlich 20 Punkte erreichen. Die Punkte sind mit einer Varianz von neun Punkten Normalverteilt. Wie gross ist die
Wahrscheinlichkeit, dass ein Student weniger als 25 Punkte erreicht?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>7. (4 Points) Detailed analysis of exam results from a statistics course at a Swiss university has shown that students achieve an average of 20 points. The points are normally distributed with a variance of nine points. What is the probability that a student achieves fewer than 25 points?</span>"""
        },
        "options": [
            {"de": "0.952", "en": "0.952"},
            {"de": "0.048", "en": "0.048"},
            {"de": "0.726", "en": "0.726"},
            {"de": "0.274", "en": "0.274"}
        ],
        "correct_idx": 0,
        "solution": {
            "de": r"**Richtig: (a)**<br>$Z = \frac{25-20}{3} \approx 1.67$. $\Phi(1.67) \approx 0.952$.",
            "en": r"**Correct: (a)**<br>$Z = \frac{25-20}{3} \approx 1.67$. $\Phi(1.67) \approx 0.952$."
        }
    },
    "hs2024_mc9": {
        "source": "HS 2024 Januar, MC #9 (4 Punkte)",
        "type": "mc",
        "question": {
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>9. Das Einkommen X der Bürger einer Stadt ist lognormal verteilt (d.h. ln(X) ∼
N (µ, σ 2 )) mit µ = 8 und σ 2 = 4. Wie hoch ist die Wahrscheinlichkeit, dass das Einkommen
eines Bürgers unter 12000 CHF liegt?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>9. (4 Points) The income $X$ of the citizens of a city is log-normally distributed (i.e. $\ln(X) \sim N(\mu, \sigma^2)$) with $\mu = 8$ and $\sigma^2 = 4. What is the probability that a citizen's income is below 12000 CHF?</span>"""
        },
        "options": [
            {"de": "0.242", "en": "0.242"},
            {"de": "0.363", "en": "0.363"},
            {"de": "0.637", "en": "0.637"},
            {"de": "0.758", "en": "0.758"}
        ],
        "correct_idx": 3,
        "solution": {
            "de": r"**Richtig: (d)**<br>Log-Transformation: $P(X < 12000) = P(\ln X < \ln 12000)$. $\ln(12000) \approx 9.39$.<br>$Z = \frac{9.39 - 8}{2} \approx 0.70$. $\Phi(0.70) \approx 0.758$.",
            "en": r"**Correct: (d)**<br>Log-Transformation: $P(X < 12000) = P(\ln X < \ln 12000)$. $\ln(12000) \approx 9.39$.<br>$Z = \frac{9.39 - 8}{2} \approx 0.70$. $\Phi(0.70) \approx 0.758$."
        }
    },
    "uebung2_mc13": {
        "source": "Übung 2, MC #13",
        "type": "mc",
        "question": {
            "de": r"$X \sim N(30, 9)$. $P(X < 21)$?",
            "en": r"$X \sim N(30, 9)$. $P(X < 21)$?"
        },
        "options": [
            {"de": r"0.9987", "en": r"0.9987"},
            {"de": r"0.8413", "en": r"0.8413"},
            {"de": r"0.1587", "en": r"0.1587"},
            {"de": r"0.00135", "en": r"0.00135"}
        ],
        "correct_idx": 3,
        "solution": {
            "de": r"**Richtig: (d)**<br>$Z = (21-30)/3 = -3$.<br>$\Phi(-3) \approx 0.00135$.",
            "en": r"**Correct: (d)**<br>$z=-3$. $\Phi(-3) \approx 0.00135$."
        }
    },
    "hs2022_mc3": {
        "source": "HS 2022 Januar, MC #3 (4 Punkte)",
        "question": {
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>3. Nehmen wir an, dass X1 , X2 , ..., XN unabhängige und identisch (I.I.D) gleichverteilte Zufallsvariablen zwischen 0 und 1 sind. Wie groß ist ungefähr die Wahrscheinlichkeit,
dass das arithmetische Mittel größer als 0.55 ist, wenn N = 100?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>3. Assume that $X_1, X_2, \ldots, X_N$ are independent and identically (i.i.d.) uniformly distributed random variables between 0 and 1. What is approximately the probability that the arithmetic mean is greater than 0.55 if N = 100?</span>"""
        },
        "options": [
            {"de": "4.2%", "en": "4.2%"},
            {"de": "50%", "en": "50%"},
            {"de": "95.8%", "en": "95.8%"},
            {"de": "10%", "en": "10%"}
        ],
        "correct_idx": 0,
        "solution": {
            "de": "**Richtig: 4.2%**<br>CLT: μ = 0.5, σ² = 1/12.<br>σ_X̄ = √(1/1200).<br>Z = (0.55-0.5)/σ_X̄ ≈ 1.73.<br>P(Z > 1.73) ≈ 0.042.",
            "en": "**Correct: 4.2%**<br>CLT: μ = 0.5, σ² = 1/12.<br>σ_X̄ = √(1/1200).<br>Z = (0.55-0.5)/σ_X̄ ≈ 1.73.<br>P(Z > 1.73) ≈ 0.042."
        }
    },

    "hs2015_mc3": {
        "source": "HS 2015, MC 3 (4 Punkte)",
        "type": "mc",
        "question": {
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>3. Es seien X und Y zwei normal verteilte Zufallsvariablen mit $\mu_X = 1, \sigma_X^2 = 4, \mu_Y = 0$ und $\sigma_Y^2 = 1$. Let $\Phi(\cdot)$ denote the CDF of the standard normal distribution.
Welche der folgenden Aussagen ist FALSCH?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>3. (4 Points) Let $X$ and $Y$ be two normally distributed random variables with $\mu_X = 1, \sigma_X^2 = 4, \mu_Y = 0$ and $\sigma_Y^2 = 1$. Let $\Phi(\cdot)$ denote the CDF of the standard normal distribution. Which of the following statements is FALSE?</span>"""
        },
        "options": [
            {"de": r"$P(\frac{X-1}{2} \le y) = \Phi(y)$", "en": r"$P(\frac{X-1}{2} \le y) = \Phi(y)$"},
            {"de": r"$\Phi^{-1}(0.91) = 0.8186$ (laut Tabelle/Kontext, tatsächlich umgekehrt)", "en": r"$\Phi^{-1}(0.91) = 0.8186$ (laut Tabelle/Kontext, tatsächlich umgekehrt)"},
            {"de": r"$E[2X - 3Y] = -1$", "en": r"$E[2X - 3Y] = -1$"},
            {"de": r"$\Phi(-1) = P(Y \ge 1)$", "en": r"$\Phi(-1) = P(Y \ge 1)$"}
        ],
        "correct_idx": 2,
        "solution": {
            "de": r"**Richtig: (c) ist FALSCH**<br>$E[2X - 3Y] = 2E[X] - 3E[Y] = 2(1) - 3(0) = 2$. Die Aussage behauptet $-1$.",
            "en": r"**Correct: (c) is FALSE**<br>$E[2X - 3Y] = 2E[X] - 3E[Y] = 2(1) - 3E[Y] = 2(1) - 3(0) = 2$. The statement claims $-1$."
        }
    }
}

# 4.8 Hypergeometrisch
QUESTIONS_4_8 = {
    "hypergeom_10_5_3": {
        "source": "Test 5, Frage 1",
        "question": {
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Urne mit $N=10$ Kugeln, davon $M=5$ rot. Ziehe $n=3$ ohne Zurücklegen. $X = \text{Anzahl rote Kugeln}$. $P(X=2)$?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Urn with $N=10$ balls, $M=5$ red. Draw $n=3$ without replacement. $X = \text{number of red balls}$. $P(X=2)$?</span>"""
        },
        "options": [
            {"de": r"$5/12$", "en": r"$5/12$"},
            {"de": r"$1/2$", "en": r"$1/2$"},
            {"de": r"$1/3$", "en": r"$1/3$"},
            {"de": r"$7/12$", "en": r"$7/12$"}
        ],
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Problem 3 (15 Punkte)
An der Olma-Messe in St. Gallen gibt es eine lange Tradition des Schweinerennens: Fünf namentlich genannte Schweine treten gegeneinander an, um als erste an der Futterstation anzukommen.
Das teilnehmende Star-Schwein Max V. beendet das Rennen immer in genau 10 Sekunden. Für
die anderen 4 Schweine ist die Rennzeit unabhängig normalverteilt mit einem Mittelwert von
µ = 13 Sekunden und einer Standardabweichung von σ = 2, 5 Sekunden.
1. (5 Punkte) Wie hoch ist die Wahrscheinlichkeit, dass Max V. das Rennen gewinnt?
2. (5 Punkte) Wie hoch ist die Wahrscheinlichkeit, dass Max V. nicht schlechter als Dritter
wird?
Sie interessieren sich nun für die Rennplatzierung X (1., 2., 3., 4., 5.) von Max V.. Um eine Reihe
von Wetten abzuschlieÃen, möchten Sie sehr sicher sein, dass die durchschnittliche Platzierung
$\bar{X}_N$ über N unabhängige Rennen hinweg mindestens Zweiter ist ($\bar{X}_N \le 2$).
3. (5 Punkte) Verwenden Sie die Näherung des zentralen Grenzwertsatzes: Was ist die niedrigste Anzahl von Rennen N, so dass $P(\bar{X}_N \le 2) \ge 0.999$?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Problem 3 (15 Points)
Pig racing. Max V. takes 10s. 4 other pigs $Y \sim N(13, 2.5^2)$.<br>1. $P(\text{Max V. wins})$.<br>2. $P(\text{Max V. at least 3rd})$.<br>3. CLT Approximation.</span>"""
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
            "de": r"Binomialverteilung beschreibt:",
            "en": r"Binomial distribution describes:"
        },
        "options": [
            {"de": r"Erfolg im x-ten Versuch.", "en": r"Success in the x-th trial."},
            {"de": r"x Erfolge in n Versuchen (mit Zurücklegen).", "en": r"x successes in n trials (with replacement)."},
            {"de": r"x Erfolge in Intervall.", "en": r"x successes in an interval."},
            {"de": r"x Erfolge in n Versuchen (ohne Zurücklegen).", "en": r"x successes in n trials (without replacement)."},
            {"de": r"n Erfolge in x Versuchen.", "en": r"n successes in x trials."}
        ],
        "correct_idx": 1,
        "solution": {
            "de": r"**Richtig: (b)**<br>Binomial = **n mal** ziehen **MIT Zurücklegen**.",
            "en": r"**Correct: (b)**<br>Successes in n independent trials (with replacement)."
        }
    },
    "uebung2_mc10": {
        "source": "Übung 2, MC #10",
        "type": "mc",
        "question": {
            "de": r"Binomialverteilung Approximation:",
            "en": r"Binomial approximation:"
        },
        "options": [
            {"de": r"Exponential wenn n > 30.", "en": r"Exponential if n > 30."},
            {"de": r"Normal wenn $np(1-p) > 9$.", "en": r"Normal if $np(1-p) > 9$."},
            {"de": r"Normal wenn n > 30, p < 0.1.", "en": r"Normal if n > 30, p < 0.1."},
            {"de": r"Poisson wenn $np(1-p) > 9$.", "en": r"Poisson if $np(1-p) > 9$."},
            {"de": r"Poisson wenn $n > 30, p \le 0.1$.", "en": r"Poisson if $n > 30, p \le 0.1$."}
        ],
        "correct_idx": [1, 4],
        "solution": {
            "de": r"**Richtig: (b), (e)**<br>**Normal-Approximation (Moivre-Laplace):** Wenn die Varianz groß genug ist ($\sigma^2 > 9$).<br>**Poisson-Approximation:** Wenn $n$ riesig und $p$ winzig ist (\"Seltene Ereignisse\"). Regel: $n>30, p \le 0.1$.",
            "en": r"**Correct: (b), (e)**<br>Normal: Variance > 9.<br>Poisson: Rare events ($n$ large, $p$ small)."
        }
    },
    "uebung2_mc14": {
        "source": "Übung 2, MC #14",
        "type": "mc",
        "question": {
            "de": r"$X \sim N(30, 9)$. Finde t so dass $P(X \ge t) = 0.0668$.",
            "en": r"$X \sim N(30, 9)$. Find t s.t. $P(X \ge t) = 0.0668$."
        },
        "options": [
            {"de": r"34.5", "en": r"34.5"},
            {"de": r"33", "en": r"33"},
            {"de": r"31.5", "en": r"31.5"},
            {"de": r"30", "en": r"30"}
        ],
        "correct_idx": 0,
        "solution": {
            "de": r"**Richtig: (a)**<br>$\Phi(z) = 1 - 0.0668 = 0.9332 \implies z \approx 1.5$.<br>$x = 30 + 1.5 \cdot 3 = 34.5$.",
            "en": r"**Correct: (a)**<br>$z=1.5 \implies t=34.5$."
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
            {"de": r"29.05 - 30.95", "en": r"29.05 - 30.95"},
            {"de": r"27.00 - 33.00", "en": r"27.00 - 33.00"},
            {"de": r"25.05 - 34.95", "en": r"25.05 - 34.95"},
            {"de": r"24.12 - 35.88", "en": r"24.12 - 35.88"}
        ],
        "correct_idx": 3,
        "solution": {
            "de": r"**Richtig: (d)**<br>$30 \pm 1.96 \cdot 3 = [24.12, 35.88]$.",
            "en": r"**Correct: (d)**<br>$\mu \pm 1.96\sigma = [24.12, 35.88]$."
        }
    },
    "uebung2_mc11": {
        "source": "Übung 2, MC #11",
        "type": "mc",
        "question": {
            "de": r"Miguel gewinnt Giro d'Italia mit $p=0.3$. 5 Teilnahmen. Wahrscheinlichkeit mind. 2 Siege?",
            "en": r"Win prob 0.3. 5 attempts. Prob of at least 2 wins?"
        },
        "options": [
            {"de": r"0.6398", "en": r"0.6398"},
            {"de": r"0.4718", "en": r"0.4718"},
            {"de": r"0.6", "en": r"0.6"},
            {"de": r"0.3602", "en": r"0.3602"},
            {"de": r"0.5282", "en": r"0.5282"}
        ],
        "correct_idx": 1,
        "solution": {
            "de": r"**Richtig: (b)**<br>Gegenwahrscheinlichkeit (0 oder 1 Sieg):<br>$P(0)+P(1) = 0.5282$.<br>$1 - 0.5282 = 0.4718$.",
            "en": r"**Correct: (b)**<br>$1 - (P(0)+P(1)) = 0.47178$."
        }
    },
    "hs2022_mc6": {
        "source": "HS 2022 Januar, MC #6 (4 Punkte)",
        "type": "mc",
        "question": {
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>6. Im Oktober macht Nina einen einwöchigen Städtetrip nach Hamburg. Die Wettervorhersage sagt für jeden Tag eine Regenwahrscheinlichkeit von 70% voraus. Wie hoch ist
in etwa die Wahrscheinlichkeit, dass es an mindestens 5 von 7 Tagen regnet?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>6. (4 Points) In October, Nina takes a one-week city trip to Hamburg. The weather forecast predicts a 70% rain probability for each day. What is approximately the probability that it rains on at least 5 of 7 days?</span>"""
        },
        "options": [
            {"de": "65%", "en": "65%"},
            {"de": "66%", "en": "66%"},
            {"de": "67%", "en": "67%"},
            {"de": "68%", "en": "68%"}
        ],
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>$X \sim Pois(10), Z=2X$. Welche Aussage trifft NICHT zu?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>$X \sim Pois(10), Z=2X$. Which is FALSE?</span>"""
        },
        "options": [
            {"de": r"$Z \sim Pois(20)$", "en": r"$Z \sim Pois(20)$"},
            {"de": r"$Var(Z) = 40$", "en": r"$Var(Z) = 40$"},
            {"de": r"Corr(X, Z) = 1$", "en": r"Corr(X, Z) = 1$"},
            {"de": r"$E[Z] = 20$", "en": r"$E[Z] = 20$"}
        ],
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>1000 Leute (700 Smart, 300 Gewöhnlich). Stichprobe 200. $P(X=10)$ gewöhnliche?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>1000 ppl (700 smart, 300 ordinary). Sample 200. $P(X=10)$ ordinary?</span>"""
        },
        "options": [
            {"de": "Additiv", "en": "Additiv"},
            {"de": "Multiplikativ", "en": "Multiplikativ"},
            {"de": "Hypergeometrisch", "en": "Hypergeometrisch"},
            {"de": "Unbekannt", "en": "Unbekannt"}
        ],
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Sei $E[X] = 2$ und $E[Y] = 3$. Was ist $E[X + Y]$?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Let $E[X] = 2$ and $E[Y] = 3$. What is $E[X + Y]$?</span>"""
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Der Erwartungswert-Operator $E[\cdot]$ ist...</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>The expectation operator $E[\cdot]$ is...</span>"""
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Aufgabe 4 (20 Punkte)
Wir betrachten die beiden Zufallsvariablen X und Y mit gemeinsamer Dichte
$$f_{X,Y}(x, y) = \begin{cases} \lambda(xy + c) & \text{für } 0 \le x \le 2 \text{ und } 0 \le y \le 1 \\ 0 & \text{sonst,} \end{cases}$$
für die Parameter $\lambda \in \mathbb{R}$ und $c \ge 0$.
1. (3 Punkte) Zeigen Sie, dass fX,Y für $\lambda = 1/(1 + 2c)$ eine Dichtefunktion ist.
2. (2 Punkte) Zeigen Sie, dass für die Randdichte fX (x) gilt:
$$f_X(x) = \begin{cases} \frac{x+2c}{2+4c} & \text{für } 0 \le x \le 2 \\ 0 & \text{sonst.} \end{cases}$$
3. (5 Punkte) Berechnen Sie die Varianz von X für c = 1.
4. (5 Punkte) Geben Sie den Ansatz zur Berechnung der Wahrscheinlichkeit P(X + Y < 6/5).
Fertigen Sie hierfür zuerst eine Skizze in der xy-Ebene an.
5. (5 Punkte) Berechnen Sie die Wahrscheinlichkeit P(X + Y < 6/5) für c = 0.</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Problem 4 (20 Points)
We consider the two random variables X and Y with joint density
$$f_{X,Y}(x, y) = \begin{cases} \lambda(xy + c) & \text{for } 0 \le x \le 2 \text{ and } 0 \le y \le 1 \\ 0 & \text{otherwise} \end{cases}$$
for parameters $\lambda \in \mathbb{R}$ and $c \ge 0$.
1. (3 Points) Show that for $\lambda = 1/(1 + 2c)$, $f_{X,Y}$ is a density function.
2. (2 Points) Show that for the marginal density $f_X(x)$:
$$f_X(x) = \begin{cases} \frac{x+2c}{2+4c} & \text{for } 0 \le x \le 2 \\ 0 & \text{otherwise} \end{cases}$$
3. (5 Points) Calculate the variance of X for c = 1.
4. (5 Points) State the approach for calculating the probability $P(X + Y < 6/5)$. First, make a sketch in the xy-plane for this.
5. (5 Points) Calculate the probability $P(X + Y < 6/5)$ for c = 0.</span>"""
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Gemeinsame Massenfunktion (Tabelle). X (10, 20, 30), Y (2, 3, 4).<br>(a) Randverteilungen.<br>(c) V(X), V(Y).<br>(d) Cov, Rho.<br>(e) Unabhängig?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Consider the joint probability mass function given in the table below for random variables X (taking values 10, 20, 30) and Y (taking values 2, 3, 4).<br>(a) Determine the marginal distributions of X and Y.<br>(c) Calculate the variances V(X) and V(Y).<br>(d) Calculate the Covariance and Correlation Coefficient.<br>(e) Are X and Y independent?</span>"""
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Tabelle mit $x_1..x_4, y_1..y_3$.<br>(a) $f_X(x_3), f_Y(y_2)$.<br>(b) Bedingte W'keiten.</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Consider a joint distribution table with values $x_1, \dots, x_4$ and $y_1, \dots, y_3$.<br>(a) Calculate the marginal probabilities $f_X(x_3)$ and $f_Y(y_2)$.<br>(b) Calculate the conditional probabilities.</span>"""
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>$f(x,y) = 24xy$ für $x+y \le 1$.<br>(a) Zeige Dichte.<br>(b) Unabhängig?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>$f(x,y) = 24xy$ on simplex.<br>(a) Verify PDF.<br>(b) Indep?</span>"""
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>$f(x,y) = 2x e^{-y}$ auf Rechteck $0<x<1, y>0$.<br>(a) Zeige Dichte.<br>(b) Unabhängig?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>$f(x,y) = 2x e^{-y}$ on the rectangle $0 < x < 1, y > 0$.<br>(a) Verify that it is a PDF.<br>(b) Are they independent?</span>"""
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>9. Seien X und Y zwei Zufallsvariablen mit Verteilungen X ∼ N (µ = 4, σ 2 = 2)
und Y ∼ N (µ = 0, σ 2 = 3). Des Weiteren gilt E[XY ] = E[X]E[Y ]. Sei Z eine Zufallsvariable
welche als Z = 3 - 2X + 3Y definiert ist. Wie lautet die Kovarianz Cov(Y, Z)?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>9. (4 Points) Let X and Y be two random variables with distributions X ~ N(mu = 4, sigma^2 = 2) and Y ~ N(mu = 0, sigma^2 = 3). Furthermore, E[XY] = E[X]E[Y] holds. Let Z be a random variable defined as Z = 3 - 2X + 3Y. What is the covariance Cov(Y, Z)?</span>"""
        },
        "options": [
            {"de": "27", "en": "27"},
            {"de": "9", "en": "9"},
            {"de": "12", "en": "12"},
            {"de": "Keine der obigen.", "en": "Keine der obigen."}
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>$X, Y$ unabhängig. $\text{Var}(X)=2$, $\text{Var}(Y)=3$. Was ist $\text{Var}(X - Y)$?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>$X, Y$ independent. $\text{Var}(X)=2$, $\text{Var}(Y)=3$. What is $\text{Var}(X - Y)$?</span>"""
        },
        "options": [
            {"de": r"$5$", "en": r"$5$"},
            {"de": r"$-1$", "en": r"$-1$"},
            {"de": r"$1$", "en": r"$1$"},
            {"de": r"$13$", "en": r"$13$"}
        ],
        "correct_idx": 0,
        "solution": {
            "de": r"**Richtig: $5$**<br>Unabhängig: $\text{Var}(X - Y) = \text{Var}(X) + (-1)^2 \text{Var}(Y) = 2 + 3 = 5$.",
            "en": r"**Correct: $5$**<br>Independent: $\text{Var}(X - Y) = \text{Var}(X) + (-1)^2 \text{Var}(Y) = 2 + 3 = 5$."
        }
    },
    "uebung3_mc7": {
        "source": "Übung 3, MC7",
        "question": {
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Was gilt allgemein für $\text{Var}(aX + b)$?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>What holds generally for $\text{Var}(aX + b)$?</span>"""
        },
        "options": [
            {"de": r"$a^2 \text{Var}(X)$", "en": r"$a^2 \text{Var}(X)$"},
            {"de": r"$a \cdot \text{Var}(X)$", "en": r"$a \cdot \text{Var}(X)$"},
            {"de": r"$a^2 \text{Var}(X) + b$", "en": r"$a^2 \text{Var}(X) + b$"},
            {"de": r"$a \cdot \text{Var}(X) + b$", "en": r"$a \cdot \text{Var}(X) + b$"}
        ],
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>X, Y Tabelle (0, 0.5, 1 vs 0, 1).<br>(a) Unabhängig?<br>(b) Cov?<br>(c) Varianz von X-Y?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Given a joint distribution table for X (values 0, 0.5, 1) and Y (values 0, 1).<br>(a) Are X and Y independent?<br>(b) Calculate the Covariance.<br>(c) Calculate the variance of X - Y.</span>"""
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>X, Y, Z unabhängig. Diskrete Verteilungen gegeben.<br>(a) Mittelwert/Varianz X, Y, X-Y.<br>(b) Verteilung Summen.<br>(c) Wahrscheinlichkeiten.</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Let X, Y, and Z be independent discrete random variables with given distributions.<br>(a) Calculate the mean and variance for X, Y, and X - Y.<br>(b) Determine the distribution of the sums.<br>(c) Calculate specific probabilities.</span>"""
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
        "source": "HS 2015, MC 6 (4 Punkte)",
        "type": "mc",
        "question": {
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>6. Es seien Xi , i = 1, . . . , n Zufallsvariablen, die jedoch nicht notwendigerweise unabhängig oder identisch verteilt sind. Nehmen Sie an, folgende Gleichungen sind erfüllt:
E[Xi ] = µ,
Var(Xi ) = σ 2 ,
Cov(Xi , Xj ) = 0, für i ̸= j.
Sei X̄n = n1 ni=1 Xi das Stichprobenmittel. Welche der folgenden Aussagen ist falsch?</span>""",
"en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>6. Let $X_i, i = 1, \dots, n$ be random variables, which are not necessarily independent or identically distributed. Assume the following equations hold:
$E[X_i] = \mu$,
$Var(X_i) = \sigma^2$,
$Cov(X_i, X_j) = 0$, for $i \neq j$.
Let $\bar{X}_n = \frac{1}{n} \sum_{i=1}^n X_i$ be the sample mean. Which of the following statements is false?</span>"""
        },
        "options": [
            {"de": r"$-1 \le \rho_{X,Y} < 0$", "en": r"$-1 \le \rho_{X,Y} < 0$"},
            {"de": r"$\rho_{X,Y} = 0$", "en": r"$\rho_{X,Y} = 0$"},
            {"de": r"$0 < \rho_{X,Y} \le 1$", "en": r"$0 < \rho_{X,Y} \le 1$"},
            {"de": "Keine der obigen Aussagen ist immer wahr.", "en": "Keine der obigen Aussagen ist immer wahr."}
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Die Kovarianz misst...</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>The covariance measures...</span>"""
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Urne mit $5$ Kugeln ($1-5$). Ziehen ohne Zurücklegen. $X = 1$. Kugel, $Y = 2$. Kugel. Korrelation?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Urn with $5$ balls ($1-5$). Draw without replacement. $X = 1$st ball, $Y = 2$nd ball. Correlation?</span>"""
        },
        "options": [
            {"de": r"$0$", "en": r"$0$"},
            {"de": r"$-0.25$", "en": r"$-0.25$"},
            {"de": r"$-0.5$", "en": r"$-0.5$"}
        ],
        "correct_idx": 1,
        "solution": {
            "de": r"**Richtig: $-0.25$**<br>$\rho = \frac{-1}{N-1} = \frac{-1}{4} = -0.25$",
            "en": r"**Correct: $-0.25$**<br>$\rho = \frac{-1}{N-1} = \frac{-1}{4} = -0.25$"
        }
    },
    "test4_q2": {
        "source": "Test 4, Frage 2",
        "question": {
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>$\text{Cov}(X,Y) = 3$, $\text{Var}(X) = 4$, $\text{Var}(Y) = 9$. Berechnen Sie $\text{Cor}(X,Y)$.</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>$\text{Cov}(X,Y) = 3$, $\text{Var}(X) = 4$, $\text{Var}(Y) = 9$. Calculate $\text{Cor}(X,Y)$.</span>"""
        },
        "options": [
            {"de": r"$0.5$", "en": r"$0.5$"},
            {"de": r"$0.25$", "en": r"$0.25$"},
            {"de": r"$0.75$", "en": r"$0.75$"},
            {"de": r"$0.33$", "en": r"$0.33$"}
        ],
        "correct_idx": 0,
        "solution": {
            "de": r"**Richtig: $0.5$**<br>$\text{Cor} = \frac{\text{Cov}}{\sigma_X \cdot \sigma_Y} = \frac{3}{2 \cdot 3} = \frac{3}{6} = 0.5$.",
            "en": r"**Correct: $0.5$**<br>$\text{Cor} = \frac{\text{Cov}}{\sigma_X \cdot \sigma_Y} = \frac{3}{2 \cdot 3} = \frac{3}{6} = 0.5$."
        }
    },
    "test4_q4": {
        "source": "Test 4, Frage 4",
        "question": {
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Wenn $X$ und $Y$ unabhängig sind, dann ist die Kovarianz...</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>If $X$ and $Y$ are independent, then the covariance is...</span>"""
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>1. Es seien X, Y zwei stetige Zufallsvariablen. Welche der folgenden Aussagen ist immer
korrekt?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>1. Let $X, Y$ be two continuous random variables. Which of the following statements is always correct?</span>"""
        },
        "options": [
            {"de": r"Wenn die Randdichten $f_X(x)$ und $f_Y(y)$ bekannt sind, können wir daraus die gemeinsame Dichte $f_{X,Y}(x, y)$ berechnen.", "en": r"If the marginal densities $f_X(x)$ and $f_Y(y)$ are known, we can calculate the joint density $f_{X,Y}(x, y)$."},
            {"de": r"$X$ und $Y$ sind unabhängig dann und nur dann wenn $\text{Cov}(X, Y) = 0$.", "en": r"$X$ and $Y$ are independent if and only if $\text{Cov}(X, Y) = 0$."},
            {"de": r"$f_{Y|X}(y|x) = f_{X|Y}(x|y)$.", "en": r"$f_{Y|X}(y|x) = f_{X|Y}(x|y)$."},
            {"de": r"$\text{Cov}(X, Y) = 0$ dann und nur dann wenn $E[XY] = E[X]E[Y]$.", "en": r"$\text{Cov}(X, Y) = 0$ if and only if $E[XY] = E[X]E[Y]$."}
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>7. Es seien X, Y und Z drei Zufallsvariablen wobei Y = 3X + 2 und Z = 2X - 3. Welche
der folgenden Aussagen ist richtig?</span>""",
"en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>7. Let $X, Y$ and $Z$ be three random variables where $Y = 3X + 2$ and $Z = 2X - 3$. Which of the following statements is correct?</span>"""
        },
        "options": [
            {"de": r"$\text{Corr}(X, Y) > \text{Corr}(X, Z)$", "en": r"$\text{Corr}(X, Y) > \text{Corr}(X, Z)$"},
            {"de": r"$\text{Corr}(X, Y) = \text{Corr}(X, Z)$", "en": r"$\text{Corr}(X, Y) = \text{Corr}(X, Z)$"},
            {"de": r"$\text{Corr}(X, Y) < \text{Corr}(X, Z)$", "en": r"$\text{Corr}(X, Y) < \text{Corr}(X, Z)$"},
            {"de": "Nicht genügend Informationen.", "en": "Nicht genügend Informationen."}
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Der Korrelationskoeffizient liegt immer zwischen...</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>The correlation coefficient is always between...</span>"""
        },
        "options": [
            {"de": r"$-1$ und $1$", "en": r"$-1$ und $1$"},
            {"de": r"$0$ und $1$", "en": r"$0$ und $1$"},
            {"de": r"$-\infty$ und $\infty$", "en": r"$-\infty$ und $\infty$"},
            {"de": r"$0$ und $\infty$", "en": r"$0$ und $\infty$"}
        ],
        "correct_idx": 0,
        "solution": {
            "de": r"**Richtig: $-1$ und $1$**<br>Eigenschaft der Korrelation: $-1 \le \rho \le 1$.",
            "en": r"**Correct: $-1$ and $1$**<br>Property of correlation: $-1 \le \rho \le 1$."
        }
    },
    "uebung3_mc11": {
        "source": "Übung 3, MC11",
        "question": {
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>$\text{Corr}(X,Y) = 0.8$ bedeutet...</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>$\text{Corr}(X,Y) = 0.8$ means...</span>"""
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>6. Es seien Xi , i = 1, . . . , n Zufallsvariablen, die jedoch nicht notwendigerweise unabhängig oder identisch verteilt sind. Nehmen Sie an, folgende Gleichungen sind erfüllt:
n            n
!
1                2
X            X
V ar       Xi =         V ar (Xi ) = n · V ar (Xj ) , ∀j = 1, . . . , n
i=1        i=1
Welche der folgenden Aussagen ist korrekt?</span>""",
"en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>6. Let $X_i, i = 1, \dots, n$ be random variables, which are not necessarily independent or identically distributed. Assume the following equations hold:
(1) $\text{Var}(\sum_{i=1}^n X_i) = \sum_{i=1}^n \text{Var}(X_i)$
(2) $\text{Var}(\sum_{i=1}^n X_i) = n \cdot \text{Var}(X_j), \forall j = 1, \dots, n$
Which of the following statements is correct?</span>"""
        },
        "options": [
            {"de": "Hinreichend für 1: Identisch verteilt. Hinreichend für 2: Unabhängig.", "en": "Hinreichend für 1: Identisch verteilt. Hinreichend für 2: Unabhängig."},
            {"de": "Hinreichend für 1: Unabhängig. Hinreichend für 2: Identisch verteilt.", "en": "Hinreichend für 1: Unabhängig. Hinreichend für 2: Identisch verteilt."},
            {"de": "Beide gelten immer, auch bei Abhängigkeit.", "en": "Beide gelten immer, auch bei Abhängigkeit."},
            {"de": "Beide gelten immer, auch bei nicht-identischer Verteilung.", "en": "Beide gelten immer, auch bei nicht-identischer Verteilung."}
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Notenverteilung Mathe (X) Englisch (Y). Tabelle.<br>(a) Momente zeigen.<br>(b) Cov, Rho.<br>(c) $Z = (X+Y)/2$.</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Grade distribution Math (X) and English (Y). Table given.<br>(a) Show moments.<br>(b) Calculate Covariance and Correlation.<br>(c) Consider $Z = (X+Y)/2$.</span>"""
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Der Korrelationskoeffizient $\rho$:</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Correlation coefficient $\rho$:</span>"""
        },
        "options": [
            {"de": "misst nur die Stärke.", "en": "misst nur die Stärke."},
            {"de": "misst nur die Richtung.", "en": "misst nur die Richtung."},
            {"de": "misst Stärke und Richtung des linearen Zusammenhangs.", "en": "misst Stärke und Richtung des linearen Zusammenhangs."},
            {"de": "hat keine Aussagekraft.", "en": "hat keine Aussagekraft."}
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Zwei Variablen sind unabhängig, wenn:</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Two variables are independent if:</span>"""
        },
        "options": [
            {"de": r"$\rho = 0$.", "en": r"$\rho = 0$."},
            {"de": r"$f(x,y) = f_X(x) \cdot f_Y(y)$.", "en": r"$f(x,y) = f_X(x) \cdot f_Y(y)$."},
            {"de": r"$f(x,y) = f_X(x) + f_Y(y)$.", "en": r"$f(x,y) = f_X(x) + f_Y(y)$."},
            {"de": "Cov = 1.", "en": "Cov = 1."}
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Die Kovarianz wird errechnet mit:</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Covariance is calculated as:</span>"""
        },
        "options": [
            {"de": r"$E[XY] - E[X]E[Y]$", "en": r"$E[XY] - E[X]E[Y]$"},
            {"de": r"$E[XY] - E[X^2]E[Y^2]$", "en": r"$E[XY] - E[X^2]E[Y^2]$"},
            {"de": r"$E[XY]^2 - E[X]E[Y]$", "en": r"$E[XY]^2 - E[X]E[Y]$"},
            {"de": r"$E[X^2Y^2] - ...$", "en": r"$E[X^2Y^2] - ...$"}
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Wann gilt $E[XY] = E[X]E[Y]$?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>When does $E[XY] = E[X]E[Y]$ hold?</span>"""
        },
        "options": [
            {"de": "Immer.", "en": "Immer."},
            {"de": "Nie.", "en": "Nie."},
            {"de": "Falls X und Y unkorreliert sind.", "en": "Falls X und Y unkorreliert sind."},
            {"de": "Nur falls X und Y identisch sind.", "en": "Nur falls X und Y identisch sind."}
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>X = Würfel, Y = Münze ('Kopf'). $P(X > 3 | Y = \text{'Kopf'})$?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>X = Die, Y = Coin ('Head'). $P(X > 3 | Y = \text{'Head'})$?</span>"""
        },
        "options": [
            {"de": "1/3", "en": "1/3"},
            {"de": "1/2", "en": "1/2"},
            {"de": "2/3", "en": "2/3"},
            {"de": "0", "en": "0"}
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Dichte $f(x,y) = x/12 + y/6$ auf $[0,2]^2$. $E[X+2Y]$?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Density $f(x,y) = x/12 + y/6$ on $[0,2]^2$. $E[X+2Y]$?</span>"""
        },
        "options": [
            {"de": "33/9", "en": "33/9"},
            {"de": "34/9", "en": "34/9"},
            {"de": "10/3", "en": "10/3"},
            {"de": "32/9", "en": "32/9"}
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Gleiche Dichte wie #12. $V(Y)$?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Consider the same density as in the previous question (#12). What is the variance $V(Y)$?</span>"""
        },
        "options": [
            {"de": "23/81", "en": "23/81"},
            {"de": "25/81", "en": "25/81"},
            {"de": "26/81", "en": "26/81"},
            {"de": "28/81", "en": "28/81"}
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>$Corr(X,Y)=-1, Var(X)=1, SD(Y)=2$. $Var(3X+Y)$?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>$Corr(X,Y)=-1, Var(X)=1, SD(Y)=2$. $Var(3X+Y)$?</span>"""
        },
        "options": [
            {"de": "7", "en": "7"},
            {"de": "13", "en": "13"},
            {"de": "5", "en": "5"},
            {"de": "1", "en": "1"}
        ],
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>X, Y unkorreliert. $E(X)=E(Y)=1, Var(X)=Var(Y)=1$. Was gilt?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>X and Y are uncorrelated. Given $E(X)=E(Y)=1$ and $Var(X)=Var(Y)=1$. Which of the following holds?</span>"""
        },
        "options": [
            {"de": r"$3E(X^2) + Cov(X,Y) = 2$", "en": r"$3E(X^2) + Cov(X,Y) = 2$"},
            {"de": r"$E(XY) = 2$", "en": r"$E(XY) = 2$"},
            {"de": r"$Cov(X, Y+2) = 2$", "en": r"$Cov(X, Y+2) = 2$"},
            {"de": r"$E((X-Y)^2) = 2$", "en": r"$E((X-Y)^2) = 2$"}
        ],
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>$Z = 4X - 3Y + 2$. $Cov(X, Z)$ unter Annahme Unkorreliertheit?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>$Z = 4X - 3Y + 2$. $Cov(X, Z)$ assuming uncorrelated?</span>"""
        },
        "options": [
            {"de": "0", "en": "0"},
            {"de": "64", "en": "64"},
            {"de": "16", "en": "16"},
            {"de": "Info fehlt", "en": "Info fehlt"}
        ],
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Stetige ZV X, Y. Was ist immer korrekt bzgl. Unkorreliertheit?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Continuous X, Y. What is always correct re: uncorrelatedness?</span>"""
        },
        "options": [
            {"de": "Randdichten reichen", "en": "Randdichten reichen"},
            {"de": "Unabh <=> Cov=0", "en": "Unabh <=> Cov=0"},
            {"de": r"$f(y|x)$...", "en": r"$f(y|x)$..."},
            {"de": r"$Cov=0 \iff E[XY] = E[X]E[Y]$", "en": r"$Cov=0 \iff E[XY] = E[X]E[Y]$"}
        ],
        "correct_idx": 3,
        "solution": {
            "de": r"**Richtig: (d)**<br>Definition von Covariance=0.",
            "en": r"**Correct: (d)**<br>Definition of Covariance=0."
        }
    }
}


# 6. Zentraler Grenzwertsatz (CLT)
QUESTIONS_6 = {}
QUESTIONS_6_3 = {
    "uebung4_mc1": {
        "source": "Übung 4, MC #1",
        "type": "mc",
        "question": {
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Seien $X_1, ..., X_n$ i.i.d. mit endlichem E und Var. $S_n = \sum X_i$. Der Zentrale Grenzwertsatz besagt:</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Let $X_1, ..., X_n$ be i.i.d. with finite mean/var. $S_n = \sum X_i$. CLT states:</span>"""
        },
        "options": [
            {"de": r"$S_n$ ist approximativ standardnormalverteilt (n > 30).", "en": r"$S_n$ ist approximativ standardnormalverteilt (n > 30)."},
            {"de": r"Die standardisierte ZV $S_n$ ist approximativ standardnormalverteilt (n > 30).", "en": r"Die standardisierte ZV $S_n$ ist approximativ standardnormalverteilt (n > 30)."},
            {"de": r"$S_n$ ist approximativ normalverteilt (n > 30).", "en": r"$S_n$ ist approximativ normalverteilt (n > 30)."},
            {"de": r"Die standardisierte ZV $S_n$ ist approximativ normalverteilt (n > 30).", "en": r"Die standardisierte ZV $S_n$ ist approximativ normalverteilt (n > 30)."},
            {"de": r"Die standardisierte ZV $S_n$ ist approximativ standardnormalverteilt (n <= 30).", "en": r"Die standardisierte ZV $S_n$ ist approximativ standardnormalverteilt (n <= 30)."}
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Bedingungen für den Zentralen Grenzwertsatz:</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Conditions for the Central Limit Theorem:</span>"""
        },
        "options": [
            {"de": r"$S_n = X_1 + ... + X_n$.", "en": r"$S_n = X_1 + ... + X_n$."},
            {"de": r"$S_n = X_1^2 + ... + X_n^2$.", "en": r"$S_n = X_1^2 + ... + X_n^2$."},
            {"de": r"$X_i$ sind identisch verteilt.", "en": r"$X_i$ sind identisch verteilt."},
            {"de": r"$X_i$ sind gleichverteilt.", "en": r"$X_i$ sind gleichverteilt."},
            {"de": r"$n > 30$.", "en": r"$n > 30$."}
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>X, Y unabhängig. Summe Z = X + Y ist:</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>X, Y independent. Sum Z = X + Y follows:</span>"""
        },
        "options": [
            {"de": "Binomial, wenn X, Y binomial mit selbem p.", "en": "Binomial, wenn X, Y binomial mit selbem p."},
            {"de": "Normalverteilt, wenn X, Y normal mit selben Parametern.", "en": "Normalverteilt, wenn X, Y normal mit selben Parametern."},
            {"de": "Standardnormal, wenn X, Y standardnormal.", "en": "Standardnormal, wenn X, Y standardnormal."},
            {"de": "Normal, wenn X, Y standardnormal.", "en": "Normal, wenn X, Y standardnormal."}
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Produktion $n=2000$. Zurückweisung wenn $>200$ defekt. Gesucht max $p$, damit mit 95% W'keit *nicht* zurückgewiesen ($k \le 200$).</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Production $n=2000$. Rejection if $>200$ defective. Find max $p$ such that with 95% probability it is *not* rejected ($k \le 200$).</span>"""
        },
        "options": [
            {"de": "0.080", "en": "0.080"},
            {"de": "0.090", "en": "0.090"},
            {"de": "0.100", "en": "0.100"},
            {"de": "0.110", "en": "0.110"}
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Seilbahn max 4200kg. 50 Personen, $\mu=80, \sigma=10$. Wahrscheinlichkeit Überlastung?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Cable car max 4200kg. 50 ppl mean 80 SD 10. Overload prob?</span>"""
        },
        "options": [
            {"de": "0.23%", "en": "0.23%"},
            {"de": "2.3%", "en": "2.3%"},
            {"de": "0.02%", "en": "0.02%"},
            {"de": "5%", "en": "5%"}
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Welche Zahl ist KEINER dieser Maße (Mean, Median, Mode)? Datensatz: $\{4, 4, 7, 7, 7, 8, 11, 13, 13, 14, 22\}$</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Which number is NONE of these measures (Mean, Median, Mode)? Dataset: $\{4, 4, 7, 7, 7, 8, 11, 13, 13, 14, 22\}$</span>"""
        },
        "options": [
            {"de": r"$7$", "en": r"$7$"},
            {"de": r"$8$", "en": r"$8$"},
            {"de": r"$9.8$", "en": r"$9.8$"},
            {"de": r"$11$", "en": r"$11$"}
        ],
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>9. Zu Kontrollzwecken werden 1000 Packungen Reis aus der Produktion entnommen und
gewogen. Es stellt sich heraus, dass das Gewicht der Packungen ungefähr normalverteilt ist.
Falls 800 der Packungen zwischen 343.2 Gramm und 356.8 Gramm wiegen, was ist ungefähr
die Varianz des Gewichts?</span>""",
"en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>9. For control purposes, 1000 packages of rice are taken from production and weighed. It turns out that the weight of the packages is approximately normally distributed. If 800 of the packages weigh between 343.2 and 356.8 grams, what is the approximate variance of the weight?</span>"""
        },
        "options": [
            {"de": r"$\sigma^2 \approx 16$", "en": r"$\sigma^2 \approx 16$"},
            {"de": r"$\sigma^2 \approx 25$", "en": r"$\sigma^2 \approx 25$"},
            {"de": r"$\sigma^2 \approx 36$", "en": r"$\sigma^2 \approx 36$"},
            {"de": r"$\sigma^2 \approx 49$", "en": r"$\sigma^2 \approx 49$"}
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>8. Aus einer Stichprobe von 3 Werten berechnet man den Mittelwert (x = 5.5) und die
empirische Varianz (s2 = 4.5; Achtung: gewichtete Varianz mit Faktor 1/n). Somit ist
der Median der zwei Werte notwendigerweise:</span>""",
"en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>8. From a sample of 3 values, the mean ($\bar{x} = 5.5$) and empirical variance ($s^2 = 4.5$) are calculated. The middle of the two values is then necessarily:</span>"""
        },
        "options": [
            {"de": "-1", "en": "-1"},
            {"de": "1", "en": "1"},
            {"de": "4", "en": "4"},
            {"de": "Wir haben nicht genügend Informationen.", "en": "Wir haben nicht genügend Informationen."}
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
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Problem 1 (12 Points)
Part 1A (4 Points)
We have drawn random samples of 100 observations each from the following four distributions V1, V2, V3, and V4:
V1) Normal distribution with expected value $\mu = 0$ and variance $\sigma^2 = 3$. Sample size: $n_1 = 100$.
V2) Exponential distribution with parameter $\lambda = 3$. Sample size: $n_2 = 100$.
V3) Normal distribution with expected value $\mu = 0$ and variance $\sigma^2 = 1$. Sample size: $n_3 = 100$.
V4) Uniform distribution U $[-3, 3]$. Sample size: $n_4 = 100$.
Below are a Boxplot (A), a Histogram (B), an empirical cumulative distribution function (C), and a QQ-Plot (vs. Normal distribution) (D) given for one sample each.
Match the respective graphics (A, B, C, and D) to the corresponding samples (V1, V2, V3, and V4), e.g., V1: D.
Important: Each sample corresponds to exactly one graphic!
A                                                                                   B
1.5
●
10 15 20
●
1.0
0.5
0.0
-2        -1       0       1       2       3
C                                                                                   D
1 2 3
●● ●                                                                                ●●● ●
Empirical Quantiles
●
●●●
●●                                                                                  ●●●●
●
●●                                                                                ●●
●●
●
●●●
●                                                                                 ●
●
0.8
●●●                                                                                ●
●
●●                                                                                  ●
●
●●
●
●                                                                                  ●
●
●●
●
●●
●●●                                                                                ●●
●
●
●●
●
●
●●                                                                                 ●●
●
Fn(x)
0.6
0.4
0.2
0.0
-4
-2
0
2
4
Data
Part 1B (8 Points)
The results of the statistics exam at the University of Hawaii yielded the following frequency table:
Grade    0.7   1.0   1.3   2.0   2.3   3.0   3.7   4.0   4.3   4.7   5.0
ni       1     0     0     0     5     6     6     4     6     4     7
1. (2 Points) Calculate the mean and mode of the sample.
2. (6 Points) Draw a boxplot, calculate the corresponding measures, and draw them in.
If you need more space, make a clear reference on the exam sheet and label the additional sheet clearly as well. Otherwise, the task will not be graded.</span>"""
        },
        "solution": {
            "de": r"**Lösung 1A:**<br>A $\Leftrightarrow$ V2 (Asymmetrisch, viele Ausreißer)<br>B $\Leftrightarrow$ V3 (Glockenkurve)<br>C $\Leftrightarrow$ V1 (S-Kurve)<br>D $\Leftrightarrow$ V4 (QQ-Plot abweichend von Gerade an Rändern)<br><br>**Lösung 1B:**<br>1. Mittelwert = 3.79, Modus = 5.0 (7 Nennungen)<br>2. 25% Quartil = 3.0, Median = 4.0, 75% Quartil = 4.7. IQA = 1.7.",
            "en": r"**Solution 1A:**<br>A $\Leftrightarrow$ V2 (Asymmetric, outliers)<br>B $\Leftrightarrow$ V3 (Bell curve)<br>C $\Leftrightarrow$ V1 (S-curve)<br>D $\Leftrightarrow$ V4 (QQ-plot deviates at tails)<br><br>**Solution 1B:**<br>1. Mean = 3.79, Mode = 5.0 (7 counts)<br>2. 25% Quartile = 3.0, Median = 4.0, 75% Quartile = 4.7. IQR = 1.7."
        }
    },
    "test3_q3": {
        "source": "Test 3, Frage 3",
        "question": {
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>$\text{Var}(3X + Y) = ?$ bei $\text{Corr}(X,Y) = -1$, $\text{Var}(X) = 1$, $\sigma_Y = 2$</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>$\text{Var}(3X + Y) = ?$ given $\text{Corr}(X,Y) = -1$, $\text{Var}(X) = 1$, $\sigma_Y = 2$</span>"""
        },
        "options": [
            {"de": r"$13$", "en": r"$13$"},
            {"de": r"$5$", "en": r"$5$"},
            {"de": r"$4$", "en": r"$4$"},
            {"de": r"$1$", "en": r"$1$"}
        ],
        "correct_idx": 3,
        "solution": {
            "de": r"**Richtig: $1$**<br>$\text{Var}(3X+Y) = 9 \cdot \text{Var}(X) + \text{Var}(Y) + 2 \cdot 3 \cdot 1 \cdot (-1) \cdot \sigma_X \cdot \sigma_Y$<br>$= 9 + 4 - 12 = 1$.",
            "en": r"**Correct: $1$**<br>$\text{Var}(3X+Y) = 9 \cdot \text{Var}(X) + \text{Var}(Y) + 2 \cdot 3 \cdot 1 \cdot (-1) \cdot \sigma_X \cdot \sigma_Y$<br>$= 9 + 4 - 12 = 1$."
        }
    },
    "hs2023_mc2": {
        "source": "HS 2023 Januar, MC #2 (4 Punkte)",
        "type": "mc",
        "question": {
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>2. Zwei unabhängige Zufallsvariablen X1 und X2 sind zwischen -1 und 1 stetig
gleichverteilt.
Welche Aussage über den Mittelwert X̄ = X1 +X
ist falsch?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>2. Two independent random variables $X_1$ and $X_2$ are uniformly distributed between -1 and 1 ($U[-1, 1]$). Which statement about the mean $\bar{X} = \frac{X_1 + X_2}{2}$ is false?</span>"""
        },
        "options": [
            {"de": r"$P(\bar{X} = 0) = 0$", "en": r"$P(\bar{X} = 0) = 0$"},
            {"de": r"$P(|\bar{X}| > 1) = 0$", "en": r"$P(|\bar{X}| > 1) = 0$"},
            {"de": r"$P(\bar{X} < -0.5) = 0.25$", "en": r"$P(\bar{X} < -0.5) = 0.25$"},
            {"de": r"$P(\bar{X} < 0) = 0.5$", "en": r"$P(\bar{X} < 0) = 0.5$"}
        ],
        "correct_idx": 2,
        "solution": {
            "de": r"**Richtig: (c) ist FALSCH**<br>Die Summe zweier Gleichverteilungen ist eine Dreiecksverteilung. Die Masse konzentriert sich um 0. $P(\bar{X} < -0.5) = 0.125 \neq 0.25$.",
            "en": r"**Correct: (c) is FALSE**<br>Sum of two uniforms is triangular. Mass concentrates around 0. $P(\bar{X} < -0.5) = 0.125 \neq 0.25$."
        }
    },
    "hs2023_mc3": {
        "source": "HS 2023 Januar, MC #3 (4 Punkte)",
        "type": "mc",
        "question": {
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>3. Der vollbeladene Ãltanker “Ever Given II“ mit einer Gesamtkapazität von
30000 m3 möchte den Nord-Ostsee-Kanal in Deutschland passieren. Wenn der Tanker mit
mehr als 27040 Tonnen Rohöl beladen ist, würde er auf Grund laufen. Das Gewicht von 1 m3
Rohöl ist unabhängig und identisch verteilt mit Erwartungswert µ = 0.9 und unbekannter
Varianz σ 2 . Unter Verwendung seiner Statistikkenntnisse schätzt der Kapitän die Wahrscheinlichkeit, auf Grund zu laufen, auf 0.2%. Wie gross ist die Varianz σ 2 des Gewichts
von 1 m3 Rohöl?
(a) 0.0064
(b) 0.0802
(c) 193.1477
(d) Nicht genügend Informationen gegeben.</span>""",
"en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>3. The fully loaded oil tanker "Ever Given II" with a total capacity of 30,000 $m^3$ wants to pass through the Kiel Canal in Germany. If the tanker is loaded with more than 27,040 tons of crude oil, it would run aground. The weight of 1 $m^3$ of crude oil is independently and identically distributed with mean $\mu = 0.9$ and unknown variance $\sigma^2$. Using his statistics knowledge, the captain estimates the probability of running aground to be 0.2%. What variance $\sigma^2$ did the captain assume for the weight of 1 $m^3$?
(a) 0.0064
(b) 0.0802
(c) 193.1477
(d) Not enough information given.</span>"""
        },
        "options": [
            {"de": "0.0064", "en": "0.0064"},
            {"de": "0.0802", "en": "0.0802"},
            {"de": "193.1477", "en": "193.1477"},
            {"de": "Nicht genügend Informationen.", "en": "Nicht genügend Informationen."}
        ],
        "correct_idx": 0,
        "solution": {
            "de": r"**Richtig: (a)**<br>Puffer = 40. $z \approx 2.88$ (für 0.002). $40 = 2.88 \cdot \sqrt{30000}\sigma$. $\sigma \approx 0.08 \Rightarrow \sigma^2 = 0.0064$.",
            "en": r"**Correct: (a)**<br>Buffer = 40. $z \approx 2.88$ (for 0.002). $40 = 2.88 \cdot \sqrt{30000}\sigma$. $\sigma \approx 0.08 \Rightarrow \sigma^2 = 0.0064$."
        }
    },
    "hs2022_mc10": {
        "source": "HS 2023 Januar, MC #9 (4 Punkte)",
        "type": "mc",
        "question": {
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>10. Beim Schach sind die Engines viel stärker als die Menschen. Sie sind so stark,
dass gewisse Züge als unmenschlich gelten. Natürlich ist es für einen Menschen möglich,
durch Zufall einen Top-Engine-Zug zu finden, so dass das Finden eines Top-Engine-Zugs
nicht bedeutet, dass sie schummeln. Ein Verdacht, dass ein Spieler schummelt, kommt
auf, wenn dieser Spieler viele Top-Engine-Züge findet. Nehmen wir an, dass die Wahrscheinlichkeit, dass ein sehr starker Spieler durch Zufall einen Top-Engine-Zug findet, p = 0.3
beträgt.
Sie entwickeln einen Algorithmus zum Aufspüren von Betrügern für eine Online-Schachplattform,
der Spieler sperren soll, die in einer Folge von 1000 Zügen mindestens 340 Top-Engine-Züge
finden. Wie hoch ist die Wahrscheinlichkeit, dass Ihr Algorithmus fälschlicherweise einen
sehr starken Spieler als Betrüger einstuft?
(a) 0.1%
(b) 0.3%
(c) 0.5%
(d) 0.7%</span>""",
"en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>10. In chess, engines are much stronger than humans. They are so strong that certain moves are considered inhuman. Of course, it is possible for a human to find a top engine move by chance, so finding a top engine move does not mean they are cheating. Suspicion that a player is cheating arises when this player finds many top engine moves. Let us assume that the probability that a very strong player finds a top engine move by chance is p = 0.3. You are developing an algorithm for detecting cheaters for an online chess platform that wants to ban players who find at least 340 top engine moves in a sequence of 1000 moves. What is the probability that your algorithm incorrectly classifies a very strong player as a cheater?
(a) 0.1%
(b) 0.3%
(c) 0.5%
(d) 0.7%</span>"""
        },
        "options": [
            {"de": "0.1%", "en": "0.1%"},
            {"de": "0.3%", "en": "0.3%"},
            {"de": "0.5%", "en": "0.5%"},
            {"de": "0.7%", "en": "0.7%"}
        ],
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Schätzer für $\mu$:<br>1) $(X_1+X_2)/2$<br>2) $X_1/3 + 2X_2/3$<br>Welcher ist effizienter?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Estimators for $\mu$:<br>1) $(X_1+X_2)/2$<br>2) $X_1/3 + 2X_2/3$<br>Which is more efficient?</span>"""
        },
        "solution": {
            "de": r"**Lösung:** Schätzer 1 ist effizienter (kleinere Varianz: $Var/2$ vs $5Var/9$).",
            "en": r"**Solution:** Estimator 1 is more efficient (lower variance: $Var/2$ vs $5Var/9$)."
        }
    },
    "hs2022_mc8": {
        "source": "HS 2022 Januar, MC #8 (4 Punkte)",
        "type": "mc",
        "question": {
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>8. Sie beobachten eine auf dem Interval [0, b] gleichverteilte Zufallsvariable X. Im
Konkreten beobachten Sie folgende Realisierungen: 1.1, 3.8, 4.2, 0.5, 5.2.
Welche der folgenden Aussagen ist korrekt?
Wie lautet der Maximum-Likelihood-Schätzer für b?
(a) b̂ML = 6.23
(b) b̂ML = 5.20
(c) b̂ML = 5.92
(d) b̂ML = 5.75</span>""",
"en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>8. You observe a random variable X uniformly distributed on the interval $[0, b]$. Specifically, you observe the following realizations: 1.1, 3.8, 4.2, 0.5, 5.2. What is the Maximum-Likelihood Estimator for b?
(a) $\hat{b}_{ML} = 6.23$
(b) $\hat{b}_{ML} = 5.20$
(c) $\hat{b}_{ML} = 5.92$
(d) $\hat{b}_{ML} = 5.75$</span>"""
        },
        "options": [
            {"de": r"$\hat{b}_{ML} = 6.23$", "en": r"$\hat{b}_{ML} = 6.23$"},
            {"de": r"$\hat{b}_{ML} = 5.20$", "en": r"$\hat{b}_{ML} = 5.20$"},
            {"de": r"$\hat{b}_{ML} = 5.92$", "en": r"$\hat{b}_{ML} = 5.92$"},
            {"de": r"$\hat{b}_{ML} = 5.75$", "en": r"$\hat{b}_{ML} = 5.75$"}
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Poisson $X$, $\mu=\lambda$. ML-Schätzer für $\lambda$?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Poisson $X$, $\mu=\lambda$. ML estimator for $\lambda$?</span>"""
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>$n=100$, $\bar{x}=10$, $\sigma=2$ known. $95\%$ KI für $\mu$?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>$n=100$, $\bar{x}=10$, $\sigma=2$ known. $95\%$ CI for $\mu$?</span>"""
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Anteil $p$. $n=400$, $k=80$ ($20\%$). $95\%$ KI für $p$?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Proportion $p$. $n=400$, $k=80$ ($20\%$). $95\%$ CI for $p$?</span>"""
        },
        "solution": {
            "de": r"**Lösung:** $0.2 \pm 1.96 \cdot \sqrt{0.2 \cdot 0.8/400} = 0.2 \pm 0.0392 = [0.1608, 0.2392]$",
            "en": r"**Solution:** $0.2 \pm 1.96 \cdot \sqrt{0.2 \cdot 0.8/400} = 0.2 \pm 0.0392 = [0.1608, 0.2392]$"
        }
    },
    "hs2023_mc10": {
        "source": "HS 2023 Januar, MC #10 (4 Punkte)",
        "type": "mc",
        "question": {
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>10. Sei x1 , x2 , ..., xn eine Stichprobe unabhängiger und identischer (I.I.D) Zufallsvariablen X.
Welcher der folgenden Schätzer des Erwartungswerts von X ist erwartungstreu?</span>""",
"en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>10. Let $x_1, x_2, \ldots, x_n$ be a sample of independent and identically distributed (i.i.d.) random variables $X$. Which of the following estimators of the expected value of $X$ is unbiased?</span>"""
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>10. Für θ > 1 sei X1 , X2 , . . . , Xn eine unabhängige Folge in [1, θ] gleichverteilter Zufallsvariablen, Xi ∼ U [1, θ]. Wir betrachten den Schätzer θ̂ = n2 (x1 + x2 + . . . + xn ) für den Parameter
θ. Welche der folgenden Aussagen über θ̂ trifft zu?</span>""",
"en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>10. For $\theta > 1$, let $X_1, X_2, \ldots, X_n$ be an independent sequence of random variables uniformly distributed on $[1, \theta]$, $X_i \sim U[1, \theta]$. We consider the estimator $\hat{\theta} = \frac{2}{n} (x_1 + x_2 + \ldots + x_n)$ for the parameter $\theta$. Which of the following statements about $\hat{\theta}$ is true?</span>"""
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Aufgabe 5 (20 Punkte)
Wir betrachten eine stetige Verteilung mit folgender Dichtefunktion:
$$f(x) = \begin{cases} \frac{\alpha}{x^{\alpha+1}} & \text{für } x \ge 1 \\ 0 & \text{sonst} \end{cases}$$
wobei $\alpha > 0$ ein unbekannter Parameter ist. Wir wollen einen Schätzer für den Parameter $\alpha$ finden.
1. (7 Punkte) Bestimmen Sie den Maximum Likelihood Schätzer für $\alpha$ basierend auf $n$ unabhängigen identisch verteilten Beobachtungen $X_1, \dots, X_n$ einer Zufallsvariablen mit der obigen Dichtefunktion $f$.
2. (2 Punkte) Berechnen Sie den Maximum Likelihood Schätzer für die folgende konkrete Stichprobe:
$x_1=11.0, x_2=16.4, x_3=27.9, x_4=15.9$
3. (7 Punkte) Bestimmen Sie einen Momentenmethodeschätzer für $\alpha > 1$ basierend auf $n$ unabhängigen identisch verteilten Beobachtungen $X_1, \dots, X_n$. Sie müssen für diese Teilaufgabe annehmen, dass $\alpha > 1$ ist, da ansonsten der Erwartungswert nicht definiert (unendlich) ist.
4. (2 Punkte) Berechnen Sie den Momentenmethodeschätzer für die obige Stichprobe.
5. (2 Punkte) Vergleichen Sie den Maximum Likelihood Schätzer und den Momentenmethodeschätzer für die obige Stichprobe. Ist der Momentenschätzer hier sinnvoll?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Problem 5 (20 Points)
We consider a continuous distribution with the following density function:
$$f(x) = \begin{cases} \frac{\alpha}{x^{\alpha+1}} & \text{for } x \ge 1 \\ 0 & \text{otherwise} \end{cases}$$
where $\alpha > 0$ is an unknown parameter. We want to find an estimator for the parameter $\alpha$.
1. (7 Points) Determine the Maximum Likelihood Estimator (MLE) for $\alpha$ based on $n$ independent identically distributed observations $X_1, \dots, X_n$ of a random variable with the above density function $f$.
2. (2 Points) Calculate the MLE for the following specific sample:
$x_1=11.0, x_2=16.4, x_3=27.9, x_4=15.9$
3. (7 Points) Determine a Method of Moments estimator for $\alpha > 1$ based on $n$ independent identically distributed observations $X_1, \dots, X_n$. You must assume for this part that $\alpha > 1$, as otherwise the expected value is undefined (infinite).
4. (2 Points) Calculate the Method of Moments estimator for the above sample.
5. (2 Points) Compare the MLE and the Method of Moments estimator for the above sample. Is the Method of Moments estimator sensible here?</span>"""
        },
        "solution": {
            "de": r"**Lösung:**<br>1. $\hat{\alpha}_{MLE} = \frac{n}{\sum \ln x_i}$.<br>2. $\hat{\alpha} \approx 0.35$. (Achtung: Dichte braucht $\alpha > 0$.)<br>3. $E[X] = \frac{\alpha}{\alpha-1}$. Auflösen nach $\alpha$: $\hat{\alpha}_{MM} = \frac{\bar{x}}{\bar{x}-1}$.<br>4. $\bar{x}=17.8 \Rightarrow \hat{\alpha} \approx 1.06$.<br>5. Momentenmethode nur für $\alpha > 1$ definiert.",
            "en": r"**Solution:**<br>1. $\hat{\alpha}_{MLE} = \frac{n}{\sum \ln x_i}$.<br>2. $\hat{\alpha} \approx 0.35$. (Note: Density needs $\alpha > 0$.)<br>3. $E[X] = \frac{\alpha}{\alpha-1}$. Solve for $\alpha$: $\hat{\alpha}_{MM} = \frac{\bar{x}}{\bar{x}-1}$.<br>4. $\bar{x}=17.8 \Rightarrow \hat{\alpha} \approx 1.06$.<br>5. Method of Moments only defined for $\alpha > 1$."
        }
    },
}

QUESTIONS_9 = {
    "hs2023_mc5": {
        "source": "HS 2023 Januar, MC #5 (4 Punkte)",
        "type": "mc",
        "question": {
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Konfidenzintervall für Durchschnittliche Füllmenge. $Var=10$. Stichprobe ($n=10$): 501, 495, 503, 498, 500, 498, 497, 503, 497, 501. Gesucht: 95% KI (symmetrisch).</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Confidence Interval for mean fill amount. $Var=10$. Sample ($n=10$): 501, 495, 503, 498, 500, 498, 497, 503, 497, 501. Find symmetric 95% CI.</span>"""
        },
        "options": [
            {"de": r"$[495.0, 503.6]$", "en": r"$[495.0, 503.6]$"},
            {"de": r"$[496.5, 502.1]$", "en": r"$[496.5, 502.1]$"},
            {"de": r"$[498.0, 500.6]$", "en": r"$[498.0, 500.6]$"},
            {"de": r"$[497.34, 501.26]$", "en": r"$[497.34, 501.26]$"}
        ],
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
        "source": "HS 2024 Januar, MC #1 (4 Punkte)",
        "type": "mc",
        "question": {
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>1. Wir beobachten die Realisierungen von 25 Zufallsvariablen, die jeweils unabhängig
voneinander aus derselben Normalverteilung mit unbekanntem Erwartungswert µ und bekannter Varianz σ 2 = 0.5 gezogen werden. Wir möchten folgenden Hypothesentest durchführen:
$H_0: \mu = 0.5$ gegen $H_1: \mu \ge 0.5$ mit einem Signifikanzniveau von $\alpha = 5\%$. Für welchen Wertebereich des Stichprobenmittelwertes $\bar{x}$ wird die Hypothese $H_0$ verworfen?
Geben Sie den grösstmöglichen Bereich an.</span>""",
"en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>1. We observe the realizations of 25 random variables, which are each drawn independently from the same normal distribution with unknown expectation $\mu$ and known variance $\sigma^2 = 0.5$. We want to perform the following hypothesis test: $H_0: \mu = 0.5$ against $H_1: \mu \ge 0.5$ with a significance level of $\alpha = 5\%$. For which range of values of the sample mean $\bar{x}$ is the hypothesis $H_0$ rejected? State the largest possible range.</span>"""
        },
        "options": [
            {"de": r"$\bar{x} > 0.66$", "en": r"$\bar{x} > 0.66$"},
            {"de": r"$\bar{x} > 0.73$", "en": r"$\bar{x} > 0.73$"},
            {"de": r"$\bar{x} > 0.78$", "en": r"$\bar{x} > 0.78$"},
            {"de": r"$\bar{x} > 1.64$", "en": r"$\bar{x} > 1.64$"}
        ],
        "correct_idx": 1,
        "solution": {
            "de": r"**Richtig: (b)**<br>Standardfehler $SE = \sqrt{0.5/25} \approx 0.1414$.<br>Kritischer Wert (einseitig 5%): $z = 1.645$.<br>Grenze: $\mu_0 + 1.645 \cdot SE = 0.5 + 0.232 = 0.732$.",
            "en": r"**Correct: (b)**<br>Standard Error $SE = \sqrt{0.5/25} \approx 0.1414$.<br>Critical value (one-sided 5%): $z = 1.645$.<br>Limit: $\mu_0 + 1.645 \cdot SE = 0.5 + 0.232 = 0.732$."
        }
    },
    "hs2024_mc8": {
        "source": "HS 2024 Januar, MC #8 (4 Punkte)",
        "type": "mc",
        "question": {
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>8. Angenommen, X ∼ N (µ, σ 2 ) mit σ 2 = 5. Wir wollen die Hypothese H0 : µ = 8
gegen H1 : µ ̸= 8 mit nur 5 Beobachtungen testen. Ein MLE-Schätzwert von µ steht uns zur
Verfügung und beträgt µ̂ = 4.95. Wie gross ist der p-Wert des obigen Tests?</span>""",
"en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>8. Assume $X \sim N(\mu, 5)$ ($ \sigma^2=5 $). We want to test the hypothesis $H_0: \mu = 8$ against $H_1: \mu \neq 8$ with only 5 observations. An MLE estimate of $\mu$ is available and is $\hat{\mu} = 4.95$. What is the p-value of the above test?</span>"""
        },
        "options": [
            {"de": "0.0011", "en": "0.0011"},
            {"de": "0.0022", "en": "0.0022"},
            {"de": "0.1738", "en": "0.1738"},
            {"de": "0.3476", "en": "0.3476"}
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>$\bar{x} = 218$. $H_0: \mu=210$. $n=225$ ($\sigma^2$ bekannt -> Z-Test).</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>$\bar{x} = 218$. $H_0: \mu=210$. $n=225$ ($\sigma^2$ known -> Z-test).</span>"""
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>t-Test. $n=16$, $\bar{x}=10$, $s=2$. $H_0: \mu=12$. Teststatistik?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>t-Test. $n=16$, $\bar{x}=10$, $s=2$. $H_0: \mu=12$. Test statistic?</span>"""
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>$p$-Wert $= 0.03$. $\alpha = 0.05$. Entscheidung?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>$p$-value $= 0.03$. $\alpha = 0.05$. Decision?</span>"""
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Eine Schätzfunktion heisst erwartungstreu, wenn sie symmetrisch um ihren Erwartungswert verteilt ist.</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>An estimator is unbiased if it is symmetrically distributed around its expectation.</span>"""
        },
        "options": [
            {"de": "Richtig", "en": "Richtig"},
            {"de": "Falsch", "en": "Falsch"}
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Effiziente Schätzungen sind im Vorlesungskontext immer auch erwartungstreu.</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Efficient estimators are always unbiased (in lecture context).</span>"""
        },
        "options": [
            {"de": "Richtig", "en": "Richtig"},
            {"de": "Falsch", "en": "Falsch"}
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Erwartungstreue Schätzfunktionen sind konsistent.</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Unbiased estimators are consistent.</span>"""
        },
        "options": [
            {"de": "Richtig", "en": "Richtig"},
            {"de": "Falsch", "en": "Falsch"}
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Schätzer sind Zufallsvariablen.</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Estimators are random variables.</span>"""
        },
        "options": [
            {"de": "Richtig", "en": "Richtig"},
            {"de": "Falsch", "en": "Falsch"}
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Ein erwartungstreuer Schätzer hat stets einen kleineren MSE als ein verzerrter Schätzer.</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>An unbiased estimator always has a lower MSE than a biased one.</span>"""
        },
        "options": [
            {"de": "Richtig", "en": "Richtig"},
            {"de": "Falsch", "en": "Falsch"}
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>$\bar{X}$. Welche Aussagen sind richtig?<br>(a) $Var(\bar{X}) = \sigma^2/n$.<br>(b) $\bar{X}$ konsistent.<br>(c) $\bar{X}$ standardnormalverteilt.</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>$\bar{X}$. True?<br>(a) $Var(\bar{X}) = \sigma^2/n$.<br>(b) Consistent.<br>(c) Standard Normal.</span>"""
        },
        "options": [
            {"de": "a) und b)", "en": "a) und b)"},
            {"de": "b) und c)", "en": "b) und c)"},
            {"de": "a) und c)", "en": "a) und c)"},
            {"de": "Nur a)", "en": "Nur a)"}
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Wann ist ein linearer Schätzer $\sum w_i X_i$ erwartungstreu?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>When is a linear estimator $\sum w_i X_i$ unbiased?</span>"""
        },
        "options": [
            {"de": "Immer.", "en": "Immer."},
            {"de": r"Wenn $\sum w_i = 0$.", "en": r"Wenn $\sum w_i = 0$."},
            {"de": r"Wenn $\sum w_i = 1$.", "en": r"Wenn $\sum w_i = 1$."},
            {"de": r"Wenn $w_i = 1/n$.", "en": r"Wenn $w_i = 1/n$."}
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>$E[Y] = \frac{1}{3+\lambda}$. Momentenschätzer für $\lambda$?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>$E[Y] = \frac{1}{3+\lambda}$. MOM estimator for $\lambda$?</span>"""
        },
        "options": [
            {"de": r"$\bar{X}$", "en": r"$\bar{X}$"},
            {"de": r"$\frac{1}{\bar{X}} + 3$", "en": r"$\frac{1}{\bar{X}} + 3$"},
            {"de": r"$\frac{1}{\bar{X}} - 3$", "en": r"$\frac{1}{\bar{X}} - 3$"},
            {"de": r"$\frac{1}{3+\bar{X}}$", "en": r"$\frac{1}{3+\bar{X}}$"}
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Momentenmethode und MLE liefern stets gleiche Ergebnisse?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>MOM and MLE always yield same results?</span>"""
        },
        "options": [
            {"de": "Richtig", "en": "Richtig"},
            {"de": "Falsch", "en": "Falsch"}
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>MLE sind nie erwartungstreu?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>MLE are never unbiased?</span>"""
        },
        "options": [
            {"de": "Richtig", "en": "Richtig"},
            {"de": "Falsch", "en": "Falsch"}
        ],
        "correct_idx": 1,
        "solution": {
             "de": r"**Richtig: Falsch**<br>$\bar{X}$ bei Normalverteilung ist MLE und erwartungstreu.",
             "en": r"**Correct: False**<br>$\bar{X}$ in Normal dist is MLE and unbiased."
        }
    },
    "test5_mc3": {
        "source": "Test 5, Q3",
        "type": "mc",
        "question": {
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>$X_i \sim U[1, \theta]$. Schätzer $\hat{\theta} = \frac{2}{n}\sum X_i$.</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>$X_i \sim U[1, \theta]$. Est $\hat{\theta} = \frac{2}{n}\sum X_i$.</span>"""
        },
        "options": [
            {"de": r"Varianz ist $\frac{(\theta-1)^2}{3n}$", "en": r"Varianz ist $\frac{(\theta-1)^2}{3n}$"},
            {"de": "Erwartungstreu", "en": "Erwartungstreu"},
            {"de": "Konsistent", "en": "Konsistent"},
            {"de": "Bias ...", "en": "Bias ..."}
        ],
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Systematischer Fehler beim Schätzen heißt Bias.</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Systematic error in estimation is called Bias.</span>"""
        },
        "options": [
            {"de": "Richtig", "en": "Richtig"},
            {"de": "Falsch", "en": "Falsch"}
        ],
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Ein Schätzer ist positiv verzerrt (Bias > 0). Überschätzt oder unterschätzt er im Mittel?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Positive bias (Bias > 0). Does it over- or underestimate on average?</span>"""
        },
        "options": [
            {"de": "Überschätzt", "en": "Überschätzt"},
            {"de": "Unterschätzt", "en": "Unterschätzt"}
        ],
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Wichtigstes Ziel beim Schätzen ist es, Schätzer mit kleinen Varianzen zu finden.</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Main goal is finding estimators with small variances.</span>"""
        },
        "options": [
            {"de": "Richtig", "en": "Richtig"},
            {"de": "Falsch", "en": "Falsch"}
        ],
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Maximierung der Loglikelihood und Likelihood führt zum selben Ergebnis (Schätzer).</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Maximizing Loglikelihood vs Likelihood yields the same estimator.</span>"""
        },
        "options": [
            {"de": "Richtig", "en": "Richtig"},
            {"de": "Falsch", "en": "Falsch"}
        ],
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Exponential $Y$. Stichprobe (1, 2, 3, 1). Likelihood $L(\theta)$?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Exp $Y$. Sample (1, 2, 3, 1). Likelihood $L(\theta)$?</span>"""
        },
        "options": [
            {"de": r"$(1 \cdot e^{-\theta})^2 ...$", "en": r"$(1 \cdot e^{-\theta})^2 ...$"},
            {"de": r"$(\theta \cdot e^{-\theta})^1 ...$", "en": r"$(\theta \cdot e^{-\theta})^1 ...$"},
            {"de": r"$(\theta \cdot e^{-1\theta})^2 (\theta \cdot e^{-2\theta})^1 (\theta \cdot e^{-3\theta})^1$", "en": r"$(\theta \cdot e^{-1\theta})^2 (\theta \cdot e^{-2\theta})^1 (\theta \cdot e^{-3\theta})^1$"},
            {"de": "...", "en": "..."}
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Rechteckverteilung $[\theta, \theta+1]$.<br>(a) $E[X]$, $Var[X]$.<br>(b) Bias von $\bar{X}$?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Uniform $[\theta, \theta+1]$. (a) Moments. (b) Bias of mean?</span>"""
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Bernoulli $\pi$. Schätzer $\hat{\pi}$ vs Laplace Smoothing $T = \frac{\sum X + 1}{n+2}$.</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Bernoulli. MLE vs Laplace Smoothing.</span>"""
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Momentenschätzer herleiten für:<br>(a) Exponential<br>(b) Rechteck $[\theta-0.5, \theta+0.5]$</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>MOM for (a) Exp (b) Uniform.</span>"""
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Binomial $B(n,p)$. n,p unbekannt. Momentenschätzer?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Binomial $B(n,p)$. n,p unknown. MOM?</span>"""
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Zusammenhang Konfidenzniveau und Intervallbreite?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Relation confidence level and interval width?</span>"""
        },
        "options": [
            {"de": "Niveau größer -> Intervall kleiner", "en": "Niveau größer -> Intervall kleiner"},
            {"de": "Niveau größer -> Intervall größer", "en": "Niveau größer -> Intervall größer"},
            {"de": "Keine Beziehung", "en": "Keine Beziehung"}
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Grenzen von Konfidenzintervallen sind zufällig.</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>CI boundaries are random.</span>"""
        },
        "options": [
            {"de": "Richtig", "en": "Richtig"},
            {"de": "Falsch", "en": "Falsch"}
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Länge des KI ist größer, je größer der Parameter ist.</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Length of CI increases with parameter magnitude.</span>"""
        },
        "options": [
            {"de": "Richtig", "en": "Richtig"},
            {"de": "Falsch", "en": "Falsch"}
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
             "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>$n=300, \sigma=5, \bar{x}=50$. 95% KI?</span>""",
             "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>$n=300, \sigma=5, \bar{x}=50$. 95% CI?</span>"""
        },
        "options": [
            {"de": r"$50 \pm 0.57$", "en": r"$50 \pm 0.57$"},
            {"de": r"$50 \pm 0.28$", "en": r"$50 \pm 0.28$"},
            {"de": r"$50 \pm 1.96$", "en": r"$50 \pm 1.96$"},
            {"de": r"$50 \pm 0.03$", "en": r"$50 \pm 0.03$"}
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Normalverteilt $\mu=400, \sigma^2=25$ ($\sigma=5$). 95% Intervall?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Normal $\mu=400, \sigma=5$. 95% interval?</span>"""
        },
        "options": [
            {"de": "[391.8, 408.2]", "en": "[391.8, 408.2]"},
            {"de": "[390.2, 409.8]", "en": "[390.2, 409.8]"},
            {"de": "[393.6, 406.4]", "en": "[393.6, 406.4]"},
            {"de": "[351.0, 449.0]", "en": "[351.0, 449.0]"}
        ],
        "correct_idx": 1,
        "solution": {
            "de": r"**Richtig: [390.2, 409.8]**<br>$400 \pm 1.96(5) = 400 \pm 9.8$.",
            "en": r"**Correct: [390.2, 409.8]**<br>$400 \pm 1.96(5) = 400 \pm 9.8$."
        }
    }
}


# 10. Hypothesentests (Hypothesis Testing)
QUESTIONS_10_5_EXTRA = {
    "uebung6_prob2": {
        "source": "Übung 6, Probe #2",
        "type": "problem",
        "question": {
             "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Schrittlänge. $\sigma=0.2, n=7, \bar{x}=85.186$. Teste $H_0: \mu \le 85$ ($\alpha=0.01$).</span>""",
             "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Step length. $\sigma=0.2, n=7, \bar{x}=85.186$. Test $H_0: \mu \le 85$ ($\alpha=0.01$).</span>"""
        },
        "options": [
            {"de": "Verwerfen", "en": "Verwerfen"},
            {"de": "Nicht verwerfen", "en": "Nicht verwerfen"}
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
             "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Internetsessions. $\bar{x}=140.5$. Ist Dauer signifikant < 148? ($\alpha=0.01$).</span>""",
             "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Internet sessions. $\bar{x}=140.5$. Is duration sig. < 148? ($\alpha=0.01$).</span>"""
        },
        "options": [
            {"de": "Ja (Verwerfen)", "en": "Ja (Verwerfen)"},
            {"de": "Nein (Nicht verwerfen)", "en": "Nein (Nicht verwerfen)"}
        ],
        "correct_idx": 0,
        "solution": {
             "de": r"**Richtig: Ja**<br>$Z = -2.39$. Kritisch $-2.33$. $-2.39 < -2.33$.",
             "en": r"**Correct: Yes**<br>$Z = -2.39$. Critical $-2.33$. $-2.39 < -2.33$."
        }
    },
    "test1_mc1": {
        "source": "Test 1, Q1",
        "type": "mc",
        "question": {
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Statistik-Vorlesung: VWL (42m, 93w), BWL (78m, 87w). Eine Hörerin wird gewählt. Wahrscheinlichkeit, dass sie BWLerin ist?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Stats class: Econ (42m, 93f), Bus (78m, 87f). A female student is chosen. Probability she is Business?</span>"""
        },
        "options": [
            {"de": "0.31", "en": "0.31"},
            {"de": "0.29", "en": "0.29"},
            {"de": "0.71", "en": "0.71"},
            {"de": "0.48", "en": "0.48"}
        ],
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>$P(A)=0.6, P(B)=0.7, P(\bar{A} \cap B)=0.1$. Berechne $P(A \cap \bar{B})$.</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>$P(A)=0.6, P(B)=0.7, P(\bar{A} \cap B)=0.1$. Find $P(A \cap \bar{B})$.</span>"""
        },
        "options": [
            {"de": "0", "en": "0"},
            {"de": "0.1", "en": "0.1"},
            {"de": "0.2", "en": "0.2"},
            {"de": "0.3", "en": "0.3"}
        ],
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>A, B disjunkt, P(A), P(B)>0. Welche Aussage trifft zu?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Let A and B be two disjoint events with $P(A) > 0$ and $P(B) > 0$. Which of the following statements is true for the conditional probability $P(A | B)$?</span>"""
        },
        "options": [
            {"de": r"$P(\bar{A} \cap \bar{B}) ...$", "en": r"$P(\bar{A} \cap \bar{B}) ...$"},
            {"de": r"$P(A \cap B) > ...$", "en": r"$P(A \cap B) > ...$"},
            {"de": r"$P(A|B) = P(B|A)$", "en": r"$P(A|B) = P(B|A)$"},
            {"de": r"$P(A \cup B) < ...$", "en": r"$P(A \cup B) < ...$"}
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>$P(A) = 0.5$ und $P(B | A) = 0.6$. Dann gilt:</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>$P(A) = 0.5$ and $P(B | A) = 0.6$. Then:</span>"""
        },
        "options": [
            {"de": r"$P(B \cap A) = 0.3$", "en": r"$P(B \cap A) = 0.3$"},
            {"de": r"$P(B \cap A) = 0.83$", "en": r"$P(B \cap A) = 0.83$"},
            {"de": r"$P(B \cap A) = 0.5$", "en": r"$P(B \cap A) = 0.5$"},
            {"de": r"$P(B \cap A) = 0.6$", "en": r"$P(B \cap A) = 0.6$"}
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>$P(B | A) = 0$. Dann gilt:</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>$P(B | A) = 0$. Then:</span>"""
        },
        "options": [
            {"de": r"$P(B \cap A) = 0$", "en": r"$P(B \cap A) = 0$"},
            {"de": r"$P(B \cap A) = P(A) \cdot P(B)$", "en": r"$P(B \cap A) = P(A) \cdot P(B)$"},
            {"de": r"$P(B \cap A) = 1$", "en": r"$P(B \cap A) = 1$"},
            {"de": r"$P(B \cup A) = 1$", "en": r"$P(B \cup A) = 1$"}
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>A und B sind zwei Ereignisse, wobei B eine Teilmenge von A ist ($B \subset A$). Dann gilt:</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>A and B are events, where B is a subset of A ($B \subset A$). Then:</span>"""
        },
        "options": [
            {"de": r"$P(A | B) = 1$", "en": r"$P(A | B) = 1$"},
            {"de": r"$P(A | B) = P(A)/P(B)$", "en": r"$P(A | B) = P(A)/P(B)$"},
            {"de": r"$P(A | B) = 0$", "en": r"$P(A | B) = 0$"},
            {"de": "Nicht genügend Informationen.", "en": "Nicht genügend Informationen."}
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>A und B sind zwei Ereignisse, die sich gegenseitig ausschliessen (disjunkt). Dann gilt:</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>A and B are two mutually exclusive (disjoint) events. Then the following holds:</span>"""
        },
        "options": [
            {"de": r"$P(A | B) = 1$", "en": r"$P(A | B) = 1$"},
            {"de": r"$P(A | B) = P(A)/P(B)$", "en": r"$P(A | B) = P(A)/P(B)$"},
            {"de": r"$P(A | B) = 0$", "en": r"$P(A | B) = 0$"},
            {"de": "Nicht genügend Informationen.", "en": "Nicht genügend Informationen."}
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Aus 'A impliziert B' ($A \subseteq B$) folgt ($P(A)>0$):</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>From 'A implies B' ($A \subseteq B$) follows ($P(A)>0$):</span>"""
        },
        "options": [
            {"de": r"$P(A | B) \ge P(A)$", "en": r"$P(A | B) \ge P(A)$"},
            {"de": r"$P(A | B) < P(A)$", "en": r"$P(A | B) < P(A)$"},
            {"de": r"$P(A | B) \ge P(B)$", "en": r"$P(A | B) \ge P(B)$"},
            {"de": r"$P(B | A) > 0$", "en": r"$P(B | A) > 0$"}
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Aus 'A und B sind unvereinbar' folgt ($P(A)>0$):</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>From 'A and B are mutually exclusive' follows ($P(A)>0$):</span>"""
        },
        "options": [
            {"de": r"$P(A \cap B) = P(A)P(B)$", "en": r"$P(A \cap B) = P(A)P(B)$"},
            {"de": r"$P(A \cup B) = P(A) + P(B)$", "en": r"$P(A \cup B) = P(A) + P(B)$"},
            {"de": r"$P(A \cap B) = 0$", "en": r"$P(A \cap B) = 0$"},
            {"de": r"$P(A | B) = P(A)$", "en": r"$P(A | B) = P(A)$"}
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>$P(A)=0.6, P(B)=0.8, P(A \cap B)=0.4, P(C)=0.3, C \subset A$. Dann gilt:</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>$P(A)=0.6, P(B)=0.8, P(A \cap B)=0.4, P(C)=0.3, C \subset A$. Then:</span>"""
        },
        "options": [
            {"de": "A und B sind unvereinbar.", "en": "A und B sind unvereinbar."},
            {"de": "A und B sind abhängig.", "en": "A und B sind abhängig."},
            {"de": r"$A \cup B = S$", "en": r"$A \cup B = S$"},
            {"de": r"$P(C | A) = 2/3$", "en": r"$P(C | A) = 2/3$"}
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>$P(A)=0.1, P(B)=0.5$. Dann gilt:</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>$P(A)=0.1, P(B)=0.5$. Then:</span>"""
        },
        "options": [
            {"de": r"$P(A \cap B) = 0.05$", "en": r"$P(A \cap B) = 0.05$"},
            {"de": r"$P(A \cap B) = 0.6$", "en": r"$P(A \cap B) = 0.6$"},
            {"de": r"$P(A \cap B) = P(A | B)$", "en": r"$P(A \cap B) = P(A | B)$"},
            {"de": "Nicht genügend Informationen.", "en": "Nicht genügend Informationen."}
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>$P(A)=1/3, P(B)=1/2, P(B|A)=1/3$. Dann gilt:</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>$P(A)=1/3, P(B)=1/2, P(B|A)=1/3$. Then:</span>"""
        },
        "options": [
            {"de": r"$P(A | B) = 1/6$", "en": r"$P(A | B) = 1/6$"},
            {"de": r"$P(A | B) = 1/9$", "en": r"$P(A | B) = 1/9$"},
            {"de": r"$P(A | B) = 2/9$", "en": r"$P(A | B) = 2/9$"},
            {"de": r"$P(A | B) = 1/2$", "en": r"$P(A | B) = 1/2$"}
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>$P(A \cap B \cap C) = P(A)P(B)P(C)$. Dann gilt:</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>$P(A \cap B \cap C) = P(A)P(B)P(C)$. Then:</span>"""
        },
        "options": [
            {"de": "A, B, C sind unabhängig.", "en": "A, B, C sind unabhängig."},
            {"de": "A und C sind unabhängig.", "en": "A und C sind unabhängig."},
            {"de": "A, B, C sind nicht unabhängig.", "en": "A, B, C sind nicht unabhängig."},
            {"de": "Nicht genügend Informationen für Unabhängigkeit.", "en": "Nicht genügend Informationen für Unabhängigkeit."}
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
                    "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Zeichnen Sie das Baumdiagramm für diesen Prozess. (Für diese Online-Aufgabe: Beschreiben Sie die Wahrscheinlichkeiten für die Pfade 'UUU' und 'UUD').</span>""",
                    "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Draw the tree diagram. (For this online task: Describe the probabilities for paths 'UUU' and 'UUD').</span>"""
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
                     "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Berechnen Sie die Wahrscheinlichkeit für 3x Hoch (UUU).</span>""",
                     "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Calculate the probability for 3x Up (UUU).</span>"""
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
                    "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Berechnen Sie die Wahrscheinlichkeit, dass die Aktie am 3. Tag steigt ($U_3$).</span>""",
                    "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Calculate the probability that the stock goes up on Day 3 ($U_3$).</span>"""
                },
                "solution": {
                    "de": r"**Lösung: 0.5**<br>Wir müssen alle Pfade summieren, die mit U enden:<br>• $UUU: 0.165$<br>• $UDU: 0.5 \cdot 0.45 \cdot 0.5 = 0.1125$<br>• $DUU: 0.5 \cdot 0.45 \cdot 0.5 = 0.1125$<br>• $DDU: 0.5 \cdot 0.55 \cdot 0.4 = 0.11$<br>Summe: $0.165 + 0.1125 + 0.1125 + 0.11 = 0.5$.",
                    "en": r"**Solution: 0.5**<br>Sum all paths ending in U:<br>• $UUU: 0.165$<br>• $UDU: 0.1125$<br>• $DUU: 0.1125$<br>• $DDU: 0.11$<br>Total: $0.5$."
                }
            }
        ],
    }
}
QUESTIONS_10_5.update(QUESTIONS_10_5_EXTRA)

QUESTIONS_2_6_EXTRA = {

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
                    "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Modell Christopher: 4 Richtungen (N, E, S, W) gleichwahrscheinlich. Berechne die Wahrscheinlichkeit bei 2 Schritten, die Distanz nach Westen zu verringern (oder anzukommen?). (Annahme: Er muss 'Westen' treffen oder Distanz verringern? Lösung impliziert 9/16).</span>""",
                    "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Christopher's model: 4 directions (N, E, S, W) equally likely. Calculate probability to make progress West in 2 steps.</span>"""
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
                    "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Modell Diego: 8 Richtungen (N, NE, E, SE, S, SW, W, NW). Wahrscheinlichkeit?</span>""",
                    "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Diego's model: 8 directions. Probability?</span>"""
                },
                "solution": {
                    "de": "**Lösung: 25/64**",
                    "en": "**Solution: 25/64**"
                }
            }
        ],
    }
}
QUESTIONS_2_6.update(QUESTIONS_2_6_EXTRA)

QUESTIONS_3_7 = {
    "hs2024_mc11": {
        "source": "HS 2024 Januar, MC #11",
        "type": "mc",
        "question": {
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>11. Ruben und Jochen spielen das folgende Spiel. Eine faire Münze wird geworfen.
Wenn Kopf fällt, zahlt Jochen 1 CHF an Ruben. Wenn Zahl fällt, zahlt Ruben 1 CHF
an Jochen. Sie spielen das Spiel für eine gegebene Anzahl n an Runden. Sei X Rubens
Gesamtgewinn nach n Runden und Y Jochens Gesamtgewinn nach n Runden. Welche der
folgenden Aussagen ist wahr?
Hinweis: Beachten Sie, dass Gewinne auch negativ sein können. Der Begriff bezieht sich auf
den Betrag, den der Spieler verdient oder verloren hat (wenn negativ).</span>""",
"en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>11. Ruben and Jochen play the following game. A fair coin is tossed. If heads, Jochen pays 1 CHF to Ruben. If tails, Ruben pays 1 CHF to Jochen. They play the game for a given number $n$ of rounds. Let $X$ be Ruben's total winnings after $n$ rounds and $Y$ Jochen's total winnings after $n$ rounds. Which of the following statements is true?<br><br><i>Note: Observe that winnings can also be negative. The term refers to the amount the player has earned or lost (if negative).</i></span>"""
        },
        "options": [
            {"de": "X und Y haben dieselbe Verteilung.", "en": "X und Y haben dieselbe Verteilung."},
            {"de": "X = Y", "en": "X = Y"},
            {"de": "X und Y sind unabhängig.", "en": "X und Y sind unabhängig."},
            {"de": "Keine der obigen.", "en": "Keine der obigen."}
        ],
        "correct_idx": 0,
        "solution": {
            "de": r"**Richtig: (a)**<br>Die Verteilung der Gewinne beim fairen Münzwurf ist symmetrisch um 0. Daher ist die Verteilung von $X$ identisch mit der von $-X$ ($=Y$).",
            "en": r"**Correct: (a)**<br>The distribution of gains in a fair coin toss is symmetric around 0. Thus the distribution of $X$ is identical to that of $-X$ ($=Y$)."
        }
    }
}
QUESTIONS_4_9 = {}
QUESTIONS_5_5_EXTRA = {
    "hs2023_prob2": {
        "source": "HS 2023 Januar, Problem 2 (15 Punkte)",
        "type": "problem",
        "question": {
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Problem 2 (15 Punkte)
“Es ist nicht schwer, Entscheidungen zu treffen, wenn du deine Werte kennst“
In Anlehnung an Roy Disneys profunden Erkenntnissen untersucht Professor O., wie die Chance
eines Unternehmens, einen Kredit zu erhalten, mit den persönlichen Werten der Kreditsachbearbeiter in Bezug auf Nachhaltigkeit zusammenhängt. Um dieses Ziel zu erreichen, untersucht
er Unternehmen, die allesamt für ihr Engagement im Bereich Nachhaltigkeit bekannt sind. Er
definiert die folgenden Ereignisse:
 A: Der Kredit für ein Unternehmen wird bewilligt.
 A: Der Kredit für ein Unternehmen wird nicht bewilligt.
 B : Der Kreditsachbearbeiter legt in seinen persönlichen Ãberzeugungen groÃen Wert auf
Nachhaltigkeit. (Grüner Sachbearbeiter ).
 B: Der Kreditsachbearbeiter legt in seinen persönlichen Ãberzeugungen keinen groÃen
Wert auf Nachhaltigkeit. (Brauner Sachbearbeiter ).
Kreditsachbearbeiter werden den Unternehmen zufällig zugewiesen, und die Wahrscheinlichkeit,
dass ein Sachbearbeiter ein grüner Sachbearbeiter ist, beträgt 0,5. Die restliche Sachbearbeiter werden als braune Sachbearbeiter eingestuft. Die Wahrscheinlichkeit für eine Kreditzusage
liegt bei 0,7. Des Weiteren beträgt die Wahrscheinlichkeit einer Kreditzusage, gegeben dass der
zuständige Sachbearbeiter ein grüner Sachbearbeiter ist, 0,8.
1. (4 Punkte) Veranschaulichen Sie das oben beschriebene Problem, indem Sie alle Wahrscheinlichkeiten in die folgende Kontingenztabelle eintragen:
B         nicht B    B ∪ nicht B
A
nicht A
A ∪ nicht A
2. (5 Punkte) Berechnen Sie die folgenden Wahrscheinlichkeiten:
 P(A ∩ B)
 P(A|B)
 P(A ∪ B)
3. (2 Punkte) Sind die Ereignisse A und B voneinander unabhängig? Begründen Sie Ihre
Antwort.
4. (4 Punkte) Um Einblicke in die Entscheidungsfindung der Sachbearbeiter zu gewinnen,
führt Professor O. persönliche Interviews mit 8 Kreditsachbearbeitern durch.
 Wie hoch ist die Wahrscheinlichkeit, dass von den 8 befragten Sachbearbeitern nur der
erste ein brauner Sachbearbeiter ist?
 Wie hoch ist die Wahrscheinlichkeit, dass von den 8 befragten Sachbearbeitern 4 grüne
Sachbearbeiter und 4 braune Sachbearbeiter sind?
beschriften Sie auch das zusätzliche Blatt klar und deutlich. Die Aufgabe wird sonst nicht gewertet.</span>""",
"en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Problem 2 (15 Points)
"It's not hard to make decisions when you know what your values are."
Inspired by Roy Disney's profound insights, Professor O. investigates how a company's chance of receiving a loan is related to the loan officers' personal values regarding sustainability. To achieve this goal, he examines companies that are all known for their commitment to sustainability.
He defines the following events:
- A: The loan for a company is approved.
- A^c: The loan for a company is not approved.
- B: The loan officer places great value on sustainability in their personal beliefs. (Green Officer).
- B^c: The loan officer does not place great value on sustainability in their personal beliefs. (Brown Officer).
Loan officers are randomly assigned to companies, and the probability that an officer is a green officer is 0.5. The remaining officers are classified as brown officers. The probability of a loan approval is 0.7. Furthermore, the probability of a loan approval, given that the responsible officer is a green officer, is 0.8.
1. (4 Points) Illustrate the problem described above by entering all probabilities into the following contingency table:
B         not B    B \cup not B
A
not A
A \cup not A
2. (5 Points) Calculate the following probabilities:
- P(A \cap B)
- P(A|B)
- P(A \cup B)
3. (2 Points) Are events A and B independent? Justify your answer.
4. (4 Points) To gain insights into the decision-making of the officers, Professor O. conducts personal interviews with 8 loan officers.
- What is the probability that of the 8 interviewed officers, only the first one is a Brown Officer?
- What is the probability that of the 8 interviewed officers, 4 are Green Officers and 4 are Brown Officers?
Label the additional sheet clearly as well. Otherwise, the task will not be graded.</span>"""
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
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Problem 4 (15 Punkte)
Hinweis: Stellen Sie sicher, dass Sie Ihre Berechnungen für die folgenden Fragen im Detail angeben. Wenn Sie einfach die richtige Antwort ohne Herleitung schreiben, erhalten Sie nicht die volle
Punktzahl.
Seien X und Y zwei Zufallsvariablen. Folgende Informationen sind bekannt:
 X hat die folgende Wahrscheinlichkeitsdichtefunktion
{︄
$(4ae^{ax})^{-1}$ für $x \ge 0$
$f_X(x) =$
0          sonst.
 Y hat die folgende stetige kumulierte Verteilungsfunktion
)︂ für y < 1
{︄
FY (y) =        (︂
$1 + b(3y^3 - 2y^2)$ für $y \ge 1$
 X und Y sind unabhängig.
1. (3 Punkte) Bestimmen Sie die Konstante a.
2. (3 Punkte) Bestimmen Sie die Konstante b.
3. (3 Punkte) Bestimmen Sie die gemeinsame Wahrscheinlichkeitsdichtefunktion fX,Y (x, y).
4. (6 Punkte) Bestimmen Sie den Erwartungswert von Z = XY .
beschriften Sie auch das zusätzliche Blatt klar und deutlich. Die Aufgabe wird sonst nicht gewertet.
beschriften Sie auch das zusätzliche Blatt klar und deutlich. Die Aufgabe wird sonst nicht gewertet.</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Problem 4 (15 Points)
Hint: Make sure to provide your calculations for the following questions in detail. If you simply write the correct answer without derivation, you will not receive full points.
Let X and Y be two random variables. The following information is known:
- X has the following probability density function: $f_X(x) = (4ae^{ax})^{-1}$ for $x \ge 0$, 0 otherwise.
- Y has the following continuous cumulative distribution function: $F_Y(y) = 0$ for $y < 1$, $1 + b(3y^{-3} - 2y^{-2})$ for $y \ge 1$.
- X and Y are independent.
1. (3 Points) Determine the constant a.
2. (3 Points) Determine the constant b.
3. (3 Points) Determine the joint probability density function $f_{X,Y}(x, y)$.
4. (6 Points) Determine the expected value of $Z = XY$.
Label the additional sheet clearly as well. Otherwise, the task will not be graded.</span>"""
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
                    "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Teil 4A: Bestimmen Sie die Konstante $a$.</span>""",
                    "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Part 4A: Determine the constant $a$.</span>"""
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
                    "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Teil 4A: Sind $X$ und $Y$ unabhängig?</span>""",
                    "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Part 4A: Are $X$ and $Y$ independent?</span>"""
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
                    "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Teil 4B: Berechnen Sie $P(X \le Y)$.</span>""",
                    "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Part 4B: Calculate $P(X \le Y)$.</span>"""
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
                    "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Teil 4B: Zeigen Sie, dass $c = 2/e$.</span>""",
                    "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Part 4B: Show that $c = 2/e$.</span>"""
                },
                "solution": {
                    "de": r"**Lösung:**<br>Doppelintegral berechnen.<br>$\int_1^e \int_0^1 c(x + x/y) dx dy = 1$.<br>$\int_0^1 x(1+1/y) dx = [\frac{1}{2}x^2]_0^1 (1+1/y) = \frac{1}{2}(1+1/y)$.<br>$\int_1^e \frac{c}{2}(1+1/y) dy = \frac{c}{2} [y + \ln(y)]_1^e = \frac{c}{2} (e+1 - 1 - 0) = \frac{c}{2} e$.<br>Gleich 1 setzen: $\frac{c e}{2} = 1 \Rightarrow c = 2/e$.",
                    "en": r"**Solution:**<br>Calculate double integral.<br>Result is $\frac{c e}{2} = 1 \Rightarrow c = 2/e$."
                }
            }
        ],
    }
}

QUESTIONS_5_5.update(QUESTIONS_5_5_EXTRA)



QUESTIONS_7_6 = {
    "hs2023_prob1": {
        "source": "HS 2023 Januar, Problem 1 (12 Punkte)",
        "type": "problem",
        "question": {
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Aufgabe 1 (12 Punkte)
Teil 1A (4 Punkte)
Aus jeder der vier Verteilungen F1 , F2 , F3 und F4 wird eine Zufallsstichprobe von Beobachtungen
gezogen:
F1 ) Poissonverteilung mit λ = 50.
Stichprobenumfang n1 = 200
F2 ) Gleichverteilung auf dem Intervall [14, 26].
Stichprobenumfang n2 = 200
F3 ) Normalverteilung mit µ = 20 und σ 2 = 4.
Stichprobenumfang n3 = 200
F4 ) Binomialverteilung mit n = 200 und p = 0.2.
Stichprobenumfang n4 = 200
Die folgenden Diagramme zeigen empirische Verteilungsfuktionen und Histogramme der entsprechenden Stichproben (F1 , F2 , F3 und F4 ). Ordne jedem Diagramm die entsprechende Verteilung
zu, z.B. F1 : a
Hinweis: Jeder Graph entspricht genau einer der vier Verteilungen F1 , F2 , F3 und F4 .
Teil 1B (8 Punkte)
Die Höchstgeschwindigkeit von zehn zufällig gewählten Autos lautet wie folgt:
180, 195, 240, 185, 230, 300, 290, 180, 235, 280
1. (3 Punkte) Berechnen Sie den Mittelwert, den Modus und den Interquartilsabstand für die
Höchstgeschwindigkeiten der Autos.
2. (5 Punkte) Zeichne Sie ein Histogramm der Höchstgeschwindigkeiten der Autos.
beschriften Sie auch das zusätzliche Blatt klar und deutlich. Die Aufgabe wird sonst nicht gewertet.</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Problem 1 (12 Points)
Part 1A (4 Points)
A random sample of observations is drawn from each of the four distributions F1, F2, F3, and F4:
F1) Poisson distribution with $\lambda = 50$. Sample size $n_1 = 200$.
F2) Uniform distribution on the interval $[14, 26]$. Sample size $n_2 = 200$.
F3) Normal distribution with $\mu = 20$ and $\sigma^2 = 4$. Sample size $n_3 = 200$.
F4) Binomial distribution with $n = 200$ and $p = 0.2$. Sample size $n_4 = 200$.
The following diagrams show empirical distribution functions and histograms of the corresponding samples (F1, F2, F3, and F4). Match each diagram to the corresponding distribution, e.g., F1: a.
Hint: Each graph corresponds to exactly one of the four distributions F1, F2, F3, and F4.
Part 1B (8 Points)
The top speed of ten randomly chosen cars is as follows:
180, 195, 240, 185, 230, 300, 290, 180, 235, 280
1. (3 Points) Calculate the mean, the mode, and the interquartile range for the top speeds of the cars.
2. (5 Points) Draw a histogram of the top speeds of the cars.
Label the additional sheet clearly as well. Otherwise, the task will not be graded.</span>"""
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
                    "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Teil 1A: Beschreiben Sie die Charakteristika für die Zuordnung (z.B. Schiefe, Symmetrie).</span>""",
                    "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Part 1A: Describe the characteristics for matching (e.g., skewness, symmetry).</span>"""
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
                    "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Teil 1B: Berechnen Sie Median und Modus der Salatverkäufe.</span>""",
                    "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Part 1B: Calculate Median and Mode of salad sales.</span>"""
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
                     "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Teil 1B: Berechnen Sie die Grenzen für den Boxplot (Q1, Q3, Whiskers).</span>""",
                     "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Part 1B: Calculate boxplot limits (Q1, Q3, Whiskers).</span>"""
                },
                "solution": {
                    "de": r"**Lösung:**<br>Q1 (25%): 261.<br>Q3 (75%): 345.<br>IQR: $345-261 = 84$.<br>Whiskers: $[Q1 - 1.5 IQR, Q3 + 1.5 IQR] = [135, 471]$. Alle Daten liegen innerhalb.",
                    "en": r"**Solution:**<br>Q1: 261, Q3: 345.<br>IQR: 84.<br>Whiskers: $[135, 471]$."
                }
            }
        ],
    }
}
QUESTIONS_8_4 = {
    "hs2023_prob5": {
        "source": "HS 2023 Januar, Problem 5 (15 Punkte)",
        "type": "problem",
        "question": {
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Problem 5 (15 Punkte)
Teil 5A (7 Punkte)
Betrachten Sie die folgende Wahrscheinlichkeitsdichtefunktion:
$$f_X(x; \lambda) = \begin{cases} \frac{2x}{\lambda^2} e^{-(x/\lambda)^2} & \text{für } x \ge 0 \\ 0 & \text{für } x < 0 \end{cases}$$
mit unbekanntem Parameter $\lambda > 0$.
Berechnen Sie den Maximum-Likelihood-Schätzer für $\lambda$ auf der Grundlage einer Zufallsstichprobe $X_1, \dots, X_n$, die aus der oben erwähnten Verteilung gezogen wurde.

Teil 5B (8 Punkte)
Nehmen wir an, dass die in der Tabelle 1 gezeigte Daten die Realisierungen einer Zufallsvariable $Y$ mit Wahrscheinlichkeitsdichtefunktion (PMF) sind:
$$p_Y(y) = \begin{cases} \frac{1}{\theta} & \text{für } y \in \{1, \dots, \theta\} \\ 0 & \text{sonst} \end{cases}$$
1. (4 Punkte) Berechnen Sie einen Momentenschätzer für $\theta$ auf Grundlage einer Zufallsstichprobe $Y_1, \dots, Y_n$.
Hinweis: $\sum_{i=1}^K i = \frac{K(K+1)}{2}$.
2. (2 Punkte) Berechnen Sie den Maximum-Likelihood-Schätzer für $\theta$ auf Grundlage einer Zufallsstichprobe $Y_1, \dots, Y_n$.
3. (2 Punkte) Berechnen Sie anhand der Beobachtungsdaten in Tabelle 1 die Werte der Momentenschätzer und Maximum-Likelihood-Schätzer für $\theta$.

Tabelle 1: Beobachtungen der Zufallsvariable $Y$
$y_1 = 1, y_2 = 4, y_3 = 3, y_4 = 4, y_5 = 2$</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Problem 5 (15 Points)
Part 5A (7 Points)
Consider the following probability density function:
$$f_X(x; \lambda) = \begin{cases} \frac{2x}{\lambda^2} e^{-(x/\lambda)^2} & \text{for } x \ge 0 \\ 0 & \text{for } x < 0 \end{cases}$$
with unknown parameter $\lambda > 0$.
Calculate the Maximum Likelihood Estimator for $\lambda$ based on a random sample $X_1, \dots, X_n$ drawn from the above distribution.

Part 5B (8 Points)
Assume the data shown in Table 1 are realizations of a random variable $Y$ with probability mass function (PMF):
$$p_Y(y) = \begin{cases} \frac{1}{\theta} & \text{for } y \in \{1, \dots, \theta\} \\ 0 & \text{otherwise} \end{cases}$$
1. (4 Points) Calculate a Method of Moments estimator for $\theta$ based on a random sample $Y_1, \dots, Y_n$.
Hint: $\sum_{i=1}^K i = \frac{K(K+1)}{2}$.
2. (2 Points) Calculate the Maximum Likelihood Estimator for $\theta$ based on a random sample $Y_1, \dots, Y_n$.
$y_1 = 1, y_2 = 4, y_3 = 3, y_4 = 4, y_5 = 2$</span>"""
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
                    "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Berechnen Sie den Momentenschätzer $\hat{\lambda}_{MM}$.</span>""",
                    "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Calculate the Method of Moments estimator $\hat{\lambda}_{MM}$.</span>"""
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
                    "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Berechnen Sie den Maximum-Likelihood-Schätzer $\hat{\lambda}_{MLE}$.</span>""",
                    "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Calculate the Maximum Likelihood Estimator $\hat{\lambda}_{MLE}$.</span>"""
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
                    "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Berechnen Sie den Schätzwert für die Daten: 0.5, 0.25, 0.15. (Hinweis: Die Daten sind nicht ganzzahlig, theoretisch problematisch für Poisson, aber hier rein rechnerisch gemeint).</span>""",
                    "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Calculate the estimate for the data: 0.5, 0.25, 0.15. (Note: Data is non-integer, theoretically problematic for Poisson, but meant computationally).</span>"""
                },
                "solution": {
                    "de": r"**Lösung:** $\bar{X} = (0.5+0.25+0.15)/3 = 0.9/3 = 0.3$.",
                    "en": r"**Solution:** $\bar{X} = 0.3$."
                }
            }
        ],
    }
}
QUESTIONS_9_4 = {
    "hs2024_mc4": {
        "source": "HS 2024 Januar, MC #4",
        "type": "mc",
        "question": {
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>4. Das Gewicht einer Packung Nudeln ist normalverteilt mit dem Erwartungswert
µ = 500 und der Varianz σ 2 = 40. Finden Sie das korrekte symmetrische Konfidenzintervall
für das erwartete Gewicht einer einzelnen Packung: das Konfidenzintervall muss um das
mittlere Gewicht zentriert sein und 99% aller Nudelpackungen enthalten.</span>""",
"en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>4. The weight of a pack of pasta is normally distributed with expectation $\mu = 500$ and variance $\sigma^2 = 40$. Find the correct symmetric confidence interval for the expected weight of a single pack: the confidence interval must be centered around the mean weight and contain 99% of all pasta packs.</span>"""
        },
        "options": [
            {"de": "[396.97 ; 603.03]", "en": "[396.97 ; 603.03]"},
            {"de": "[483.71 ; 516.29]", "en": "[483.71 ; 516.29]"},
            {"de": "[485.29 ; 514.71]", "en": "[485.29 ; 514.71]"},
            {"de": "[487.60 ; 512.40]", "en": "[487.60 ; 512.40]"}
        ],
        "correct_idx": 1,
        "solution": {
            "de": r"**Richtig: (b)**<br>Gesucht ist das Schwankungsintervall für einen *Einzelwert* $X$ (nicht Mittelwert).<br>$500 \pm z_{0.995} \cdot \sigma = 500 \pm 2.576 \cdot \sqrt{40} \approx 500 \pm 16.29$.",
            "en": r"**Correct: (b)**<br>Prediction interval for a *single value* $X$ (not mean).<br>$500 \pm z_{0.995} \cdot \sigma = 500 \pm 2.576 \cdot \sqrt{40} \approx 500 \pm 16.29$."
        }
    }
}
QUESTIONS_11_1 = {}

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