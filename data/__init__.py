"""
Data module for Study.Smart
Contains course configuration and exam questions.
"""

from data.courses import COURSES
from data.exam_questions import (
    get_question,
    get_all_questions_for_topic,
    QUESTIONS_1_1,
    QUESTIONS_1_2,
    QUESTIONS_1_7,
    QUESTIONS_1_8,
    QUESTIONS_1_9,
    QUESTIONS_1_11, # NEW
    QUESTIONS_2_3,
    QUESTIONS_2_4,
    QUESTIONS_2_5,
    QUESTIONS_2_6, # NEW
    QUESTIONS_3_1,
    QUESTIONS_3_2,
    QUESTIONS_3_4,
    QUESTIONS_3_5,
    QUESTIONS_3_7, # NEW
    QUESTIONS_4_2,
    QUESTIONS_4_3,
    QUESTIONS_4_4,
    QUESTIONS_4_6,
    QUESTIONS_4_7,
    QUESTIONS_4_9, # NEW
    QUESTIONS_5_5, # NEW (Was QUESTIONS_5 which maps to 5_3, but we might want explicit 5.5)
    QUESTIONS_5,
    QUESTIONS_6,
    QUESTIONS_6_3, # NEW
    QUESTIONS_7_6, # NEW
    QUESTIONS_8,
    QUESTIONS_8_4, # NEW
    QUESTIONS_9_4, # NEW
    QUESTIONS_10,
    QUESTIONS_10_5, # NEW
    QUESTIONS_11_1 # NEW
)

__all__ = [
    'COURSES',
    'get_question',
    'get_all_questions_for_topic',
    'QUESTIONS_1_1',
    'QUESTIONS_1_2',
    'QUESTIONS_1_7',
    'QUESTIONS_1_8',
    'QUESTIONS_1_9',
    'QUESTIONS_1_11',
    'QUESTIONS_2_3',
    'QUESTIONS_2_4',
    'QUESTIONS_2_5',
    'QUESTIONS_2_6',
    'QUESTIONS_3_1',
    'QUESTIONS_3_2',
    'QUESTIONS_3_4',
    'QUESTIONS_3_5',
    'QUESTIONS_3_7',
    'QUESTIONS_4_2',
    'QUESTIONS_4_3',
    'QUESTIONS_4_4',
    'QUESTIONS_4_6',
    'QUESTIONS_4_7',
    'QUESTIONS_4_9',
    'QUESTIONS_5',
    'QUESTIONS_5_5',
    'QUESTIONS_6',
    'QUESTIONS_6_3',
    'QUESTIONS_8',
    'QUESTIONS_8_4',
    'QUESTIONS_7_6', # Missing above
    'QUESTIONS_9_4',
    'QUESTIONS_10',
    'QUESTIONS_10_5',
    'QUESTIONS_11_1'
]
