
import re

def audit_duplicates():
    path = 'data/exam_questions.py'
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    keys_found = {} # key -> list of (line_num, en_length)
    
    current_key = None
    current_key_line = -1
    
    # Regex to find keys
    key_pattern = re.compile(r'^\s+"([^"]+)": \{')
    
    # Simple state machine
    for i, line in enumerate(lines):
        match = key_pattern.match(line)
        if match:
            current_key = match.group(1)
            current_key_line = i + 1
            if current_key not in keys_found:
                keys_found[current_key] = []
            
            # Now specifically look for "en": ... inside this block
            # We scan until we hit the next key or end of file
            en_len = 0
            for j in range(i+1, min(i+1000, len(lines))):
                if key_pattern.match(lines[j]):
                    break # Next key
                if '"en":' in lines[j]:
                    en_len = len(lines[j])
                    break
            
            keys_found[current_key].append({
                "line": current_key_line,
                "en_len": en_len
            })

    # Report
    print("Duplicate Audit Report:")
    print("=======================")
    count = 0
    for key, instances in keys_found.items():
        if len(instances) > 1:
            count += 1
            print(f"Key: {key}")
            for inst in instances:
                print(f"  - Line {inst['line']}: EN Size {inst['en_len']}")
            print("-" * 20)
            
    print(f"Total Duplicates: {count}")

if __name__ == "__main__":
    audit_duplicates()
