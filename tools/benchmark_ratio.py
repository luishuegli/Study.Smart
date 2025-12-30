
import re
import sys
import os
sys.path.append(os.getcwd())
from data.exam_questions import QUESTIONS_HS2015, QUESTIONS_HS2024

def clean_text(text):
    # Remove HTML tags for fair length comparison
    text = re.sub(r'<[^>]+>', '', text)
    # Remove whitespace noise
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def calculate_benchmark():
    keys = [
        ('hs2015_prob5', QUESTIONS_HS2015), 
        ('hs2024_mc9', QUESTIONS_HS2024),
        ('hs2024_mc3', QUESTIONS_HS2024)
    ]
    
    print(f"{'ID':<15} | {'DE Len':<6} | {'EN Len':<6} | {'Ratio':<6}")
    print("-" * 50)
    
    total_de = 0
    total_en = 0
    
    for q_id, q_source in keys:
        q_data = q_source.get(q_id)
        if q_data:
            de = clean_text(q_data['question']['de'])
            en = clean_text(q_data['question']['en'])
            ratio = len(en) / len(de)
            print(f"{q_id:<15} | {len(de):<6} | {len(en):<6} | {ratio:.3f}")
            total_de += len(de)
            total_en += len(en)
            
    print("-" * 50)
    print(f"Average Ratio: {total_en / total_de:.3f}")

if __name__ == "__main__":
    calculate_benchmark()
