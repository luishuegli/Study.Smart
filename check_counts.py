import sys
import os

# Add project root to sys.path
sys.path.append(os.getcwd())

try:
    from data.exam_questions import (
        QUESTIONS_1_7, QUESTIONS_1_9, QUESTIONS_1_11,
        QUESTIONS_3_4, QUESTIONS_3_7,
        QUESTIONS_4_7,
        QUESTIONS_5_3,
        QUESTIONS_9_4,
        QUESTIONS_10_5
    )

    topics = {
        "1.7": QUESTIONS_1_7,
        "1.9": QUESTIONS_1_9,
        "1.11": QUESTIONS_1_11,
        "3.4": QUESTIONS_3_4,
        "3.7": QUESTIONS_3_7,
        "4.7": QUESTIONS_4_7,
        "5.3": QUESTIONS_5_3,
        "9.4": QUESTIONS_9_4,
        "10.5": QUESTIONS_10_5
    }

    for t_id, q_dict in topics.items():
        print(f"{t_id}: {len(q_dict)}")

except ImportError as e:
    print(f"Error importing modules: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
