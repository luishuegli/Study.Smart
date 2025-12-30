import re

SOURCE_FILE = "/Users/luis/Downloads/Study.Smart/data/exams/HS_2024_questions.txt"

def extract_questions():
    with open(SOURCE_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    # Regex to capture "N. (4 Punkte) ... text ... (a)"
    # It stops before the options start (a)
    # Questions 1-12
    
    questions = {}
    
    # Pattern explanation:
    # ^\s*(\d+)\.\s+\(4 Punkte\)\s+  -> Start of question "1. (4 Punkte) "
    # (.*?)                          -> The Question Text (lazy)
    # (?=\n\s*\(a\))                 -> Lookahead for option (a)
    
    pattern = re.compile(r"^\s*(\d+)\.\s+\(4 Punkte\)\s+(.*?)(?=\n\s*\(a\))", re.DOTALL | re.MULTILINE)
    
    matches = pattern.findall(content)
    
    for num_str, text in matches:
        # Clean up newlines and hyphens
        # Replace newlines with space, but keep double newlines as paragraphs?
        # Actually, for LaTeX consistency, better to keep paragraphs.
        
        cleaned_text = text.strip()
        # Remove hyphenation at line breaks (e.g. "Wahrscheinlich-\nkeit" -> "Wahrscheinlichkeit")
        cleaned_text = re.sub(r"(\w)-\n\s*(\w)", r"\1\2", cleaned_text)
        
        # Replace single newlines with space, double with <br>
        # First, split by empty lines
        paragraphs = re.split(r'\n\s*\n', cleaned_text)
        final_paragraphs = []
        for p in paragraphs:
            # Join lines in paragraph
            p_clean = " ".join([l.strip() for l in p.splitlines()])
            final_paragraphs.append(p_clean)
            
        final_text = "<br><br>".join(final_paragraphs)
        
        questions[int(num_str)] = final_text
        
    return questions

if __name__ == "__main__":
    q_data = extract_questions()
    for k in sorted(q_data.keys()):
        if 1 <= k <= 4:
            print(f"--- Q{k} ---")
            print(q_data[k])
            print("\n")
