import re

def fix_duplicates(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace two consecutive indented closing brackets with one
    # Pattern: (whitespace)],\n(same whitespace)],
    # We use regex to match specific 8-space indent to be safe, or generic.
    
    # Generic: (\s+)\],\n\1\],
    # Replace with: \1],
    
    new_content = re.sub(r'(\n\s+)\],\n\s+\],', r'\1],', content)
    
    # Run loop to catch triples if any (though regex sub handles sequential non-overlapping?)
    # re.sub non-overlapping. So triplicates might become duplicates. Run twice?
    # Or strict loop.
    
    if new_content != content:
        print("Fixed duplicates.")
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
    else:
        print("No duplicates found.")

if __name__ == "__main__":
    fix_duplicates("data/exam_questions.py")
