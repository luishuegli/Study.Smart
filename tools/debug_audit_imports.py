
import sys
import os

# Add parent dir to path to import data
sys.path.append(os.getcwd())

print("Attempting imports...")

from data.exam_questions import QUESTIONS_1_1, QUESTIONS_1_2, QUESTIONS_1_3, QUESTIONS_1_4, QUESTIONS_1_5, QUESTIONS_1_6, QUESTIONS_1_7, QUESTIONS_1_9, QUESTIONS_1_10, QUESTIONS_1_11
print("1.x OK")
from data.exam_questions import QUESTIONS_2_1, QUESTIONS_2_2, QUESTIONS_2_3, QUESTIONS_2_4, QUESTIONS_2_5, QUESTIONS_2_6
print("2.x OK")
from data.exam_questions import QUESTIONS_3_1, QUESTIONS_3_2, QUESTIONS_3_3, QUESTIONS_3_4, QUESTIONS_3_5, QUESTIONS_3_6, QUESTIONS_3_7
print("3.x OK")
from data.exam_questions import QUESTIONS_4_2, QUESTIONS_4_3, QUESTIONS_4_4, QUESTIONS_4_5, QUESTIONS_4_6, QUESTIONS_4_7, QUESTIONS_4_8, QUESTIONS_4_9
print("4.x OK")
from data.exam_questions import QUESTIONS_5_1, QUESTIONS_5_2, QUESTIONS_5_3, QUESTIONS_5_4, QUESTIONS_5_5
print("5.x OK")
from data.exam_questions import QUESTIONS_6, QUESTIONS_6_3
print("6.x OK")
from data.exam_questions import QUESTIONS_7, QUESTIONS_7_6
print("7.x OK")
from data.exam_questions import QUESTIONS_8, QUESTIONS_8_4
print("8.x OK")
from data.exam_questions import QUESTIONS_9, QUESTIONS_9_4
print("9.x OK")
from data.exam_questions import QUESTIONS_10, QUESTIONS_10_5
print("10.x OK")
from data.exam_questions import QUESTIONS_11_1
print("11.x OK")

print("All imports successful!")
