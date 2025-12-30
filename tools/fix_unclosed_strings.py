
import re

def fix_unclosed_strings():
    path = 'data/exam_questions.py'
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    fixed_count = 0
    in_de_block = False
    de_start_index = -1
    
    for i in range(len(lines)):
        line = lines[i]
        stripped = line.strip()
        
        # Detect start of DE multi-line string
        # Pattern: "de": r""" or "de": """
        # And make sure it doesn't close on the same line
        if ('"de": r"""' in line or '"de": """' in line) and not line.strip().endswith('""",'):
            # Double check it doesn't close later in the same line (e.g. one-liner)
            # count triple quotes
            if line.count('"""') % 2 != 0: 
                in_de_block = True
                de_start_index = i
                continue
        
        if in_de_block:
            # Check if this line CLOSES the block
            if '"""' in line:
                in_de_block = False
                continue
            
            # Check if we hit "en": WITHOUT closing
            if '"en":' in line:
                # We found the bug!
                # Logic: We are at the EN line (e.g. `            "en": r"""...`)
                # We need to insert `""",` BEFORE this line, or append it to the PREVIOUS line.
                
                # Check previous line
                prev_line = lines[i-1].rstrip()
                
                # Append to previous line
                print(f"Fixing unclosed string at Line {i} (Question block starting {de_start_index})")
                lines[i-1] = prev_line + '""",\n'
                
                fixed_count += 1
                in_de_block = False # Reset
                
    if fixed_count > 0:
        with open(path, 'w', encoding='utf-8') as f:
            f.writelines(lines)
        print(f"Successfully fixed {fixed_count} unclosed strings.")
    else:
        print("No unclosed strings found via heuristic.")

if __name__ == "__main__":
    fix_unclosed_strings()
