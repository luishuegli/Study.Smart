import re

def fix_corruption(path):
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    new_lines = []
    for i, line in enumerate(lines):
        # Fix 1: Missing "options": key and indentation
        # Pattern: Line starts with "[" exactly
        if line.startswith("["):
            # Assume it belongs to 8-space indent level
            new_line = '        "options": [\n'
            new_lines.append(new_line)
            print(f"Fixed missing key at line {i+1}")
            continue

        # Fix 2: Debris after closing bracket
        # Pattern: "        ]   r"..."
        # Or just "   ]" followed by r string
        match = re.search(r'^\s*\]\s+r?".*?"', line)
        if match:
            # Replace with closed bracket and comma
            new_line = '        ],\n'
            new_lines.append(new_line)
            print(f"Fixed debris at line {i+1}")
            continue
            
        # Fix 3: Comma check (if previous sed missed something)
        # If line is "        ]" and next line is "correct_idx", ensure comma.
        # Hard to do in single pass without lookahead, but sed did this mostly.
        
        new_lines.append(line)

    with open(path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

if __name__ == "__main__":
    fix_corruption("data/exam_questions.py")
