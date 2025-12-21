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
                    {"id": "1.5", "title": {"de": "1.5 Wichtige Regeln der Wahrscheinlichkeitsrechnung", "en": "1.5 Important Rules of Probability"}, "slide_start": 44},
                    {"id": "1.6", "title": {"de": "1.6 Wahrscheinlichkeitsräume", "en": "1.6 Probability Spaces"}, "slide_start": 50},
                    {"id": "1.7", "title": {"de": "1.7 Bedingte Wahrscheinlichkeit und stochastische Unabhängigkeit", "en": "1.7 Conditional Probability and Independence"}, "slide_start": 64},
                    {"id": "1.8", "title": {"de": "1.8 Totale Wahrscheinlichkeit", "en": "1.8 Total Probability"}, "slide_start": 77},
                    {"id": "1.9", "title": {"de": "1.9 Das Bayes-Theorem", "en": "1.9 Bayes' Theorem"}, "slide_start": 85},
                ]
            },
            {
                "id": "topic_2", 
                "title": "2. Elementare Kombinatorik", 
                "status": "open",
                "slide_range": (93, 104),
                "subtopics": [
                    {"id": "2.1", "title": "2.1 Fakultät und Binomialkoeffizient", "slide_start": 94},
                    {"id": "2.2", "title": "2.2 Das Fundamentalprinzip der Kombinatorik", "slide_start": 97},
                    {"id": "2.3", "title": "2.3 Permutationen", "slide_start": 99},
                    {"id": "2.4", "title": "2.4 Kombinationen", "slide_start": 101},
                    {"id": "2.5", "title": "2.5 Variationen", "slide_start": 103},
                ]
            },
            {
                "id": "topic_3", 
                "title": "3. Zufallsvariablen", 
                "status": "open",
                "slide_range": (105, 172),
                "subtopics": [
                    {"id": "3.1", "title": "3.1 Die Verteilungsfunktion", "slide_start": 117},
                    {"id": "3.2", "title": "3.2 Diskrete Zufallsvariablen", "slide_start": 125},
                    {"id": "3.3", "title": "3.3 Stetige Zufallsvariablen", "slide_start": 129},
                    {"id": "3.4", "title": "3.4 Erwartungswerte von Zufallsvariablen", "slide_start": 138},
                    {"id": "3.5", "title": "3.5 Varianz", "slide_start": 156},
                    {"id": "3.6", "title": "3.6 Standardisieren", "slide_start": 169},
                ]
            },
            {
                "id": "topic_4", 
                "title": "4. Stochastische Modelle und spezielle Verteilungen", 
                "status": "open",
                "slide_range": (173, 217),
                "subtopics": [
                    {"id": "4.1", "title": "4.1 Gleichförmige Verteilung (diskret)", "slide_start": 176},
                    {"id": "4.2", "title": "4.2 Bernoulli-Verteilung (diskret)", "slide_start": 183},
                    {"id": "4.3", "title": "4.3 Binomialverteilung (diskret)", "slide_start": 187},
                    {"id": "4.4", "title": "4.4 Poisson-Verteilung (diskret)", "slide_start": 195},
                    {"id": "4.5", "title": "4.5 Rechteckverteilung (stetig)", "slide_start": 201},
                    {"id": "4.6", "title": "4.6 Exponentialverteilung (stetig)", "slide_start": 205},
                    {"id": "4.7", "title": "4.7 Normalverteilung (stetig)", "slide_start": 209},
                ]
            },
            {
                "id": "topic_5", 
                "title": "5. Mehrdimensionale Zufallsvariablen", 
                "status": "open",
                "slide_range": (218, 260),
                "subtopics": [
                    {"id": "5.1", "title": "5.1 Gemeinsame Verteilung und Randverteilungen", "slide_start": 223},
                    {"id": "5.2", "title": "5.2 Bedingte Verteilungen und stochastische Unabhängigkeit", "slide_start": 240},
                    {"id": "5.3", "title": "5.3 Kovarianz und Korrelationskoeffizient", "slide_start": 248},
                    {"id": "5.4", "title": "5.4 Summe von zwei oder mehreren Zufallsvariablen", "slide_start": 254},
                ]
            },
            {
                "id": "topic_6", 
                "title": "6. Der zentrale Grenzwertsatz", 
                "status": "open",
                "slide_range": (261, 277),
                "subtopics": []
            },
            {
                "id": "topic_7", 
                "title": "7. Beschreibende/Deskriptive Statistik", 
                "status": "open",
                "slide_range": (278, 312),
                "subtopics": [
                    {"id": "7.1", "title": "7.1 Häufigkeitsverteilung, Histogramm und Verteilungsfunktion", "slide_start": 281},
                    {"id": "7.2", "title": "7.2 Messzahlen zur Beschreibung statistischer Verteilungen", "slide_start": 289},
                    {"id": "7.3", "title": "7.3 Boxplot", "slide_start": 302},
                    {"id": "7.4", "title": "7.4 Quantile-Quantile Plot", "slide_start": 305},
                    {"id": "7.5", "title": "7.5 Streudiagramm", "slide_start": 310},
                ]
            },
            {
                "id": "topic_8", 
                "title": "8. Schätzung unbekannter Parameter: Punktschätzung", 
                "status": "open",
                "slide_range": (313, 360),
                "subtopics": [
                    {"id": "8.1", "title": "8.1 Intuitiv heuristische Ansätze für Schätzfunktionen", "slide_start": 318},
                    {"id": "8.2", "title": "8.2 Eigenschaften von Punktschätzungen", "slide_start": 328},
                    {"id": "8.3", "title": "8.3 Methoden zur Konstruktion von Schätzfunktionen", "slide_start": 346},
                ]
            },
            {
                "id": "topic_9", 
                "title": "9. Intervallschätzungen-Konfidenzintervalle", 
                "status": "open",
                "slide_range": (361, 374),
                "subtopics": [
                    {"id": "9.1", "title": "9.1 Konzept des Konfidenzintervalls", "slide_start": 362},
                    {"id": "9.2", "title": "9.2 Ableitung von Konfidenzintervallen (bei grossen Stichproben)", "slide_start": 366},
                    {"id": "9.3", "title": "9.3 Zusammenhang mit Hypothesentests", "slide_start": 370},
                ]
            },
            {
                "id": "topic_10", 
                "title": "10. Hypothesentests", 
                "status": "open",
                "slide_range": (375, 394),
                "subtopics": [
                    {"id": "10.1", "title": "10.1 Arten von Hypothesen", "slide_start": 376},
                    {"id": "10.2", "title": "10.2 Kritischer Bereich und Teststatistik", "slide_start": 379},
                    {"id": "10.3", "title": "10.3 Gütefunktion und Arten von Fehlern", "slide_start": 383},
                    {"id": "10.4", "title": "10.4 Der p-Wert", "slide_start": 392},
                ]
            },
        ]
    }
}
