# Database of Exam Questions
# Structure:
# "topic_id": [
#     {
#         "id": "unique_id",
#         "source": "Exam Name/Year",
#         "question_text": "Markdown string",
#         "options": {"A": "...", "B": "..."},
#         "correct_answer": "A",
#         "solution_text": "Markdown reasoning"
#     }
# ]

EXAM_QUESTIONS = {
    "descr_stats": [
        {
            "id": "q1_hs23_mock",
            "source": "HS 2023, Task 1 (Mock)",
            "question_text": r"""
            Given a dataset with $Q_1=10$ and $IQR=20$. 
            What is the **Upper Outlier Limit** according to Tukey's rule?
            """,
            "options": {
                "A": "30",
                "B": "40",
                "C": "50",
                "D": "60"
            },
            "correct_answer": "D",
            "solution_text": r"""
            **Step-by-Step Logic:**
            1. **Find Q3:** We know $IQR = Q_3 - Q_1$.
               - $20 = Q_3 - 10 \implies Q_3 = 30$.
            2. **Apply Tuple:** Limit = $Q_3 + 1.5 \cdot IQR$.
            3. **Calculate:** Limit = $30 + 1.5(20) = 30 + 30 = 60$.
            
            Therefore, **(D)** is correct.
            """
        },
        {
            "id": "q2_intro_mock",
            "source": "Introductory Exercise",
            "question_text": "Which measure is **least** affected by outliers?",
            "options": {
                "A": "Mean (Arithmetic Average)",
                "B": "Standard Deviation",
                "C": "Median",
                "D": "Range"
            },
            "correct_answer": "C",
            "solution_text": """
            **Reasoning:**
            - The **Mean** and **Standard Deviation** calculate using *every* value, so one huge number shifts them significantly.
            - The **Range** is literally determined by the outliers (Min/Max).
            - The **Median** is the middle value. Changing the extremes does not affect the middle, making it **robust** against outliers.
            """
        }
    ]
}
