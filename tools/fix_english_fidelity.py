
import re
import sys
import os

# Add parent dir to path to import data
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

path = "data/exam_questions.py"

def fix_prefixes():
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.split('\n')

def fix_prefixes():
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.split('\n')
    fixed_count = 0
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Match DE start line with prefix
        de_match = re.search(r'"de": r?"""<span[^>]*>\s*(\d+)\.\s+\((\d+)\s+Punkte\)', line)
        
        if de_match:
            q_num = de_match.group(1)
            points = de_match.group(2)
            
            # Search forward for the EN line (limit search to avoid runaway)
            j = i + 1
            found_en = False
            while j < len(lines) and j < i + 20: # Heuristic limit
                en_line = lines[j]
                
                # Check for EN start
                if '"en":' in en_line:
                    found_en = True
                    
                    # Check if already fixed
                    if re.search(rf'{q_num}\.\s+\({points}\s+Points\)', en_line):
                        break # Already good
                    
                    # Regex to inject
                    # Matches: "en": r"""<span...>CONTENT</span>"""
                    en_match = re.search(r'("en": r?"""<span[^>]*>)(.*)(</span>""")', en_line)
                    
                    if en_match:
                        prefix_part = en_match.group(1)
                        content_part = en_match.group(2)
                        suffix_part = en_match.group(3)
                        
                        # Fix: Don't double inject if some prefix exists but maybe wrong format?
                        # For now, simplistic injection.
                        
                        new_content = f"{q_num}. ({points} Points) {content_part}"
                        new_line = f'{prefix_part}{new_content}{suffix_part}'
                        
                        lines[j] = new_line
                        fixed_count += 1
                        print(f"Fixed: Q{q_num} ({points} Pts)")
                    
                    break # Stop searching for EN after finding it
                
                j += 1
        
        i += 1

    if fixed_count > 0:
        with open(path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))
        print(f"Successfully fixed {fixed_count} prefixes.")
    else:
        print("No prefixes needed fixing.")

if __name__ == "__main__":
    fix_prefixes()
