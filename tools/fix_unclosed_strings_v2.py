
import re

def fix_unclosed_strings_v2():
    path = 'data/exam_questions.py'
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    fixed_count = 0
    in_de_block = False
    
    for i in range(len(lines)):
        line = lines[i]
        
        # Check for multi-line DE start
        if ('"de": r"""' in line or '"de": """' in line) and not line.strip().endswith('""",'):
             # Verify it's not a one-liner with internal quotes (rare)
             # Basic count check: if odd number of triples, it opens.
             if line.count('"""') % 2 != 0:
                 in_de_block = True
                 continue
        
        if in_de_block:
            # Critical Check: Does this line start with "en": ?
            # And does it look like the start of the English block?
            # e.g. "en": r"""
            
            stripped = line.strip()
            if stripped.startswith('"en":'):
                # We hit EN key, but we are still in_de_block!
                # This implies DE wasn't closed.
                # However, we must be careful. If DE *contains* "en": text? Unlikely in this file structure.
                # But notice: If DE was NOT closed, the Python parser considers this line part of the string.
                # So we are fixing the SOURCE code.
                
                # Check if the previous line closed it?
                # If previous line ends with """, then in_de_block should have been false.
                # But we handle "closed" check below.
                
                # We need to inject """, at the end of the previous line (or on its own line).
                print(f"Fixing unclosed string detected at Line {i+1} (EN key found while DE open)")
                
                # Append to previous line
                lines[i-1] = lines[i-1].rstrip() + '""",\n'
                fixed_count += 1
                in_de_block = False # We just closed it
                continue
            
            # Check if this line actually closes the string
            if '"""' in line:
                # If we find """, we assume it closes.
                # Be careful: "en": r""" has """.
                # But we handled the "startswith en" case ABOVE.
                # So if we reach here, and find """, it's a legitimate close (or end of DE text).
                in_de_block = False
    
    if fixed_count > 0:
        with open(path, 'w', encoding='utf-8') as f:
            f.writelines(lines)
        print(f"Successfully fixed {fixed_count} unclosed strings.")
    else:
        print("No unclosed strings found via pattern.")

if __name__ == "__main__":
    fix_unclosed_strings_v2()
