
import re

def check_balance():
    with open('data/exam_questions.py', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    in_triple_double = False
    start_line = -1
    
    for i, line in enumerate(lines):
        # Remove escaped quotes? Triple quotes usually don't have escapes like \""" commonly.
        # But let's simple count occurrences of """
        
        count = line.count('"""')
        
        if count > 0:
            # If odd number of """, state flips
            if count % 2 != 0:
                if not in_triple_double:
                    in_triple_double = True
                    start_line = i + 1
                    print(f"Line {i+1}: Opened triple-double quote (Current State: OPEN)")
                else:
                    in_triple_double = False
                    print(f"Line {i+1}: Closed triple-double quote (Current State: CLOSED)")
            else:
                 pass # Even number means Open then Close (or Close then Open), state remains same
                 
    if in_triple_double:
        print(f"ERROR: File ended with UNCLOSED triple-double quote starting around Line {start_line}")
    else:
        print("SUCCESS: Triple-double quotes match.")

if __name__ == "__main__":
    check_balance()
