
def normalize_file():
    path = 'data/exam_questions.py'
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace U+2212 (Minus Sign) with ASCII hyphen
    new_content = content.replace('\u2212', '-')
    
    # Replace U+02C6 (Modifier Letter Circumflex Accent) with ASCII ^ if implies power?
    # Or just remove if garbage. In "0.25^ p ^ 0.5", it likely meant power or just noise.
    # Let's replace with ^ just in case.
    new_content = new_content.replace('\u02c6', '^')
    
    # Replace U+02DC (Small Tilde) with ASCII ~
    new_content = new_content.replace('\u02dc', '~')
    
    if content != new_content:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Normalized unicode characters.")
    else:
        print("No changes needed.")

if __name__ == "__main__":
    normalize_file()
