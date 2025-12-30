import re

path = "data/exam_questions.py"

def scan():
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    for i, line in enumerate(lines):
        # Look for P(...) = int
        # Regex: P\s*\(.*?\)\s*=\s*\d{2,}\s
        # matches P(A) = 21 
        matches = re.finditer(r'P\s*\(.*?\)\s*=\s*(\d{2,})', line)
        for m in matches:
            print(f"Line {i+1}: {m.group(0)} (Value: {m.group(1)})")
            
        # Look for fractions in options maybe? like "14" instead of "1/4"
        # Harder to regex without context.
        # But HS2024 MC3 options were 14, 13, 34, 56.
        # "(a) 14"
        if re.search(r'\([a-d]\)\s*\d{2,}\n', line): # option line? often inside string literal with \n
             print(f"Line {i+1} (Option?): {line.strip()[:50]}...")

if __name__ == "__main__":
    scan()
