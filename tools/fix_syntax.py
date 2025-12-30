import re

def fix_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    new_lines = []
    for i, line in enumerate(lines):
        stripped = line.rstrip()
        
        # Case 1: Same line "en":
        # e.g. ..."""            "en": ...
        # Regex to find `"""` followed by whitespace and `"en":`
        # But verify it's the `de` string end.
        
        if '"""' in line and '"en":' in line:
            # Check if comma missing
            if '""", "en":' not in line and '""","en":' not in line:
                # Replace
                # Use split to be safe?
                # ..."""            "en": ...
                # Be careful not to match inside string.
                # Assuming "en": is the key.
                # pattern: r'"""\s*"en":'
                line = re.sub(r'"""(\s*)"en":', r'""",\1"en":', line)
                
        new_lines.append(line)
        
    # Pass 2: Multiline
    # If line ends with `"""` and next line starts with `"en":`
    final_lines = []
    for i in range(len(new_lines)):
        line = new_lines[i]
        next_line = new_lines[i+1] if i+1 < len(new_lines) else ""
        
        stripped = line.strip()
        next_stripped = next_line.strip()
        
        if stripped.endswith('"""') and not stripped.endswith('""",'):
            # Check if next line is "en":
            if next_stripped.startswith('"en":'):
                # Add comma to current line
                # Need to preserving original newline char
                if line.endswith('\n'):
                    line = line[:-1] + ",\n"
                else:
                    line = line + ","
        
        final_lines.append(line)
        
    with open(path, 'w', encoding='utf-8') as f:
        f.writelines(final_lines)
    print("Fixed syntax.")

if __name__ == "__main__":
    fix_file("data/exam_questions.py")
