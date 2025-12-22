# Course Data with Full Hierarchy
# Derived from User Images (Statistik Skript VWL)

COURSES = {
    "vwl": {
        "title": "Statistik für VWL",
        "description": "Grundlagen der Statistik für Volkswirte.",
        "progress": 0.0,
        "color": "#10b981",
        "topics": [
            {
                "id": "topic_1", 
                "title": {"de": "1. Grundlagen der Wahrscheinlichkeit", "en": "1. Basics of Probability"}, 
                "status": "open",
                "slide_range": (7, 92),
                "subtopics": [
                    {"id": "1.1", "title": {"de": "1.1 Ereignisse, Ereignisraum und Ereignismenge", "en": "1.1 Events, Sample Space and Sets"}, "slide_start": 8},
                    {"id": "1.2", "title": {"de": "1.2 Das Rechnen mit Ereignissen", "en": "1.2 Operations with Events"}, "slide_start": 19},
                    {"id": "1.3", "title": {"de": "1.3 Der Wahrscheinlichkeitsbegriff", "en": "1.3 The Concept of Probability"}, "slide_start": 27},
                    {"id": "1.4", "title": {"de": "1.4 Axiomatik der Wahrscheinlichkeitstheorie", "en": "1.4 Axioms of Probability Theory"}, "slide_start": 41},
                    {"id": "1.5", "title": {"de": "1.5 Wichtige Regeln (Additionssatz)", "en": "1.5 Important Rules (Addition Law)"}, "slide_start": 44},
                    {"id": "1.6", "title": {"de": "1.6 Wahrscheinlichkeitsräume", "en": "1.6 Probability Spaces"}, "slide_start": 50},
                    {"id": "1.7", "title": {"de": "1.7 Bedingte Wahrscheinlichkeit und stochastische Unabhängigkeit", "en": "1.7 Conditional Probability and Independence"}, "slide_start": 64},
                    {"id": "1.8", "title": {"de": "1.8 Totale Wahrscheinlichkeit", "en": "1.8 Total Probability"}, "slide_start": 77},
                    {"id": "1.9", "title": {"de": "1.9 Das Bayes-Theorem", "en": "1.9 Bayes' Theorem"}, "slide_start": 85},
                ]
            },
            {
                "id": "topic_2", 
                "title": {"de": "2. Elementare Kombinatorik", "en": "2. Elementary Combinatorics"}, 
                "status": "open",
                "slide_range": (93, 104),
                "subtopics": [
                    {"id": "2.1", "title": {"de": "2.1 Fakultät und Binomialkoeffizient", "en": "2.1 Factorial and Binomial Coefficient"}, "slide_start": 94},
                    {"id": "2.2", "title": {"de": "2.2 Das Fundamentalprinzip der Kombinatorik", "en": "2.2 Fundamental Principle of Combinatorics"}, "slide_start": 97},
                    {"id": "2.3", "title": {"de": "2.3 Permutationen", "en": "2.3 Permutations"}, "slide_start": 99},
                    {"id": "2.4", "title": {"de": "2.4 Kombinationen", "en": "2.4 Combinations"}, "slide_start": 101},
                    {"id": "2.5", "title": {"de": "2.5 Variationen", "en": "2.5 Variations"}, "slide_start": 103},
                ]
            },
            {
                "id": "topic_3", 
                "title": {"de": "3. Zufallsvariablen", "en": "3. Random Variables"}, 
                "status": "open",
                "slide_range": (105, 172),
                "subtopics": [
                    {"id": "3.1", "title": {"de": "3.1 Die Verteilungsfunktion", "en": "3.1 Distribution Function"}, "slide_start": 117},
                    {"id": "3.2", "title": {"de": "3.2 Diskrete Zufallsvariablen", "en": "3.2 Discrete Random Variables"}, "slide_start": 125},
                    {"id": "3.3", "title": {"de": "3.3 Stetige Zufallsvariablen", "en": "3.3 Continuous Random Variables"}, "slide_start": 129},
                    {"id": "3.4", "title": {"de": "3.4 Erwartungswerte von Zufallsvariablen", "en": "3.4 Expected Values"}, "slide_start": 138},
                    {"id": "3.5", "title": {"de": "3.5 Varianz", "en": "3.5 Variance"}, "slide_start": 156},
                    {"id": "3.6", "title": {"de": "3.6 Standardisieren", "en": "3.6 Standardization"}, "slide_start": 169},
                ]
            },
            {
                "id": "topic_4", 
                "title": {"de": "4. Stochastische Modelle und spezielle Verteilungen", "en": "4. Stochastic Models and Special Distributions"}, 
                "status": "open",
                "slide_range": (173, 217),
                "subtopics": [
                    {"id": "4.1", "title": {"de": "4.1 Gleichförmige Verteilung (diskret)", "en": "4.1 Uniform Distribution (discrete)"}, "slide_start": 176},
                    {"id": "4.2", "title": {"de": "4.2 Bernoulli-Verteilung (diskret)", "en": "4.2 Bernoulli Distribution (discrete)"}, "slide_start": 183},
                    {"id": "4.3", "title": {"de": "4.3 Binomialverteilung (diskret)", "en": "4.3 Binomial Distribution (discrete)"}, "slide_start": 187},
                    {"id": "4.4", "title": {"de": "4.4 Poisson-Verteilung (diskret)", "en": "4.4 Poisson Distribution (discrete)"}, "slide_start": 195},
                    {"id": "4.5", "title": {"de": "4.5 Rechteckverteilung (stetig)", "en": "4.5 Uniform Distribution (continuous)"}, "slide_start": 201},
                    {"id": "4.6", "title": {"de": "4.6 Exponentialverteilung (stetig)", "en": "4.6 Exponential Distribution (continuous)"}, "slide_start": 205},
                    {"id": "4.7", "title": {"de": "4.7 Normalverteilung (stetig)", "en": "4.7 Normal Distribution (continuous)"}, "slide_start": 209},
                ]
            },
            {
                "id": "topic_5", 
                "title": {"de": "5. Mehrdimensionale Zufallsvariablen", "en": "5. Multidimensional Random Variables"}, 
                "status": "open",
                "slide_range": (218, 260),
                "subtopics": [
                    {"id": "5.1", "title": {"de": "5.1 Gemeinsame Verteilung und Randverteilungen", "en": "5.1 Joint Distribution and Marginal Distributions"}, "slide_start": 223},
                    {"id": "5.2", "title": {"de": "5.2 Bedingte Verteilungen und stochastische Unabhängigkeit", "en": "5.2 Conditional Distributions and Stochastic Independence"}, "slide_start": 240},
                    {"id": "5.3", "title": {"de": "5.3 Kovarianz und Korrelationskoeffizient", "en": "5.3 Covariance and Correlation Coefficient"}, "slide_start": 248},
                    {"id": "5.4", "title": {"de": "5.4 Summe von zwei oder mehreren Zufallsvariablen", "en": "5.4 Sum of Two or More Random Variables"}, "slide_start": 254},
                ]
            },
            {
                "id": "topic_6", 
                "title": {"de": "6. Der zentrale Grenzwertsatz", "en": "6. Central Limit Theorem"}, 
                "status": "open",
                "slide_range": (261, 277),
                "subtopics": []
            },
            {
                "id": "topic_7", 
                "title": {"de": "7. Beschreibende/Deskriptive Statistik", "en": "7. Descriptive Statistics"}, 
                "status": "open",
                "slide_range": (278, 312),
                "subtopics": [
                    {"id": "7.1", "title": {"de": "7.1 Häufigkeitsverteilung, Histogramm und Verteilungsfunktion", "en": "7.1 Frequency Distribution, Histogram and Distribution Function"}, "slide_start": 281},
                    {"id": "7.2", "title": {"de": "7.2 Messzahlen zur Beschreibung statistischer Verteilungen", "en": "7.2 Measures for Describing Statistical Distributions"}, "slide_start": 289},
                    {"id": "7.3", "title": {"de": "7.3 Boxplot", "en": "7.3 Box Plot"}, "slide_start": 302},
                    {"id": "7.4", "title": {"de": "7.4 Quantile-Quantile Plot", "en": "7.4 Quantile-Quantile Plot"}, "slide_start": 305},
                    {"id": "7.5", "title": {"de": "7.5 Streudiagramm", "en": "7.5 Scatter Plot"}, "slide_start": 310},
                ]
            },
            {
                "id": "topic_8", 
                "title": {"de": "8. Schätzung unbekannter Parameter: Punktschätzung", "en": "8. Point Estimation of Unknown Parameters"}, 
                "status": "open",
                "slide_range": (313, 360),
                "subtopics": [
                    {"id": "8.1", "title": {"de": "8.1 Intuitiv heuristische Ansätze für Schätzfunktionen", "en": "8.1 Intuitive Heuristic Approaches for Estimating Functions"}, "slide_start": 318},
                    {"id": "8.2", "title": {"de": "8.2 Eigenschaften von Punktschätzungen", "en": "8.2 Properties of Point Estimations"}, "slide_start": 328},
                    {"id": "8.3", "title": {"de": "8.3 Methoden zur Konstruktion von Schätzfunktionen", "en": "8.3 Methods for Constructing Estimating Functions"}, "slide_start": 346},
                ]
            },
            {
                "id": "topic_9", 
                "title": {"de": "9. Intervallschätzungen-Konfidenzintervalle", "en": "9. Interval Estimations - Confidence Intervals"}, 
                "status": "open",
                "slide_range": (361, 374),
                "subtopics": [
                    {"id": "9.1", "title": {"de": "9.1 Konzept des Konfidenzintervalls", "en": "9.1 Concept of the Confidence Interval"}, "slide_start": 362},
                    {"id": "9.2", "title": {"de": "9.2 Ableitung von Konfidenzintervallen (bei grossen Stichproben)", "en": "9.2 Derivation of Confidence Intervals (for large samples)"}, "slide_start": 366},
                    {"id": "9.3", "title": {"de": "9.3 Zusammenhang mit Hypothesentests", "en": "9.3 Connection with Hypothesis Tests"}, "slide_start": 370},
                ]
            },
            {
                "id": "topic_10", 
                "title": {"de": "10. Hypothesentests", "en": "10. Hypothesis Tests"}, 
                "status": "open",
                "slide_range": (375, 394),
                "subtopics": [
                    {"id": "10.1", "title": {"de": "10.1 Arten von Hypothesen", "en": "10.1 Types of Hypotheses"}, "slide_start": 376},
                    {"id": "10.2", "title": {"de": "10.2 Kritischer Bereich und Teststatistik", "en": "10.2 Critical Region and Test Statistics"}, "slide_start": 379},
                    {"id": "10.3", "title": {"de": "10.3 Gütefunktion und Arten von Fehlern", "en": "10.3 Power Function and Types of Errors"}, "slide_start": 383},
                    {"id": "10.4", "title": {"de": "10.4 Der p-Wert", "en": "10.4 The p-Value"}, "slide_start": 392},
                ]
            },
        ]
    }
}
