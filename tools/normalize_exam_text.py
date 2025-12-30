import re
import sys
import os

def normalize_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()

    # 1. Remove Page Breaks and Headers/Footers
    # Pattern: Page numbers and common headers often appear around form feed \x0c
    # We'll split by form feed and process pages, or just regex replace common footer patterns
    
    # Remove Form Feed characters (page breaks)
    text = text.replace('\x0c', '\n')
    
    lines = text.split('\n')
    cleaned_lines = []
    
    for line in lines:
        line = line.strip()
        
        # Skip empty lines
        if not line:
            continue
            
        # Skip page numbers (heuristic: simple digits alone, or "Page X", "Seite X")
        # HS2022/23 often have just numbers at bottom center or "Problem X (15 Punkte)" at top
        if re.match(r'^\d+$', line):
            continue
            
        # Skip common headers
        if "Verwenden Sie diese Seite" in line:
            continue
        if "Falls Sie mehr Platz" in line:
            continue
        if "das zusätzliche Blatt" in line:
            continue
        if "Standardnormalverteilung" in line and "Verteilungsfunktion" in line:
            # Skip tables tables tables
            continue

        cleaned_lines.append(line)

    # Rejoin
    text = '\n'.join(cleaned_lines)
    
    # 2. Fix Hyphenation (word-\nbreak)
    # Be careful not to merge lists.
    # Pattern: word ending in -, followed by newline, followed by lowercase word
    text = re.sub(r'(\w+)-\n([a-zäöü])', r'\1\2', text)
    
    # 3. Fix simple line breaks within sentences
    # Pattern: Line ends with char, next line starts with char. 
    # This is tricky because of lists.
    # Heuristic: If line ends with letter/comma, and next line starts with letter.
    # For now, let's keep newlines but normalize paragraph breaks.
    
    # 4. Fix Mojibake (Double-encoded UTF-8)
    # Common in HS 2023
    replacements = {
        "Ã¤": "ä",
        "Ã¼": "ü",
        "Ã¶": "ö",
        "ÃY": "ß", # Check this
        "Ã": "ß",  # Sometimes it gets cut off?
        "â": "'",
        "â": "-",
        "â¦": "...",
        # Add more specific pairs if seen
    }
    # More robust approach: try to encode latin1 then decode utf-8
    try:
        # This handles the case where it was read as UTF-8 but the file actually contained 
        # UTF-8 sequences that were interpreted as Windows-1252 or Latin-1 characters 
        # and then saved back as UTF-8.
        # e.g. the byte 0xC3 for 'Ã' is actually the first byte of a 2-byte UTF-8 seq.
        # But here we have the character 'Ã' (U+0041 U+0303) followed by '¤'.
        # Wait, 'Ã' is 'A' with tilde. That's NOT 'Ã' (U+00C3).
        # Let's check the hex bytes if possible.
        # 'Ã' is often how PDF extractors normalize 'Ã' + combining chars.
        
        # Simple string replace is safer for now based on observed patterns.
        text = text.replace("Ã¤", "ä")
        text = text.replace("Ã¼", "ü",)
        text = text.replace("Ã¶", "ö")
        # Fix known broken ones from view_file output
        # "unabhÃ¤ngig" -> "unabhängig"
        pass
    except Exception:
        pass
        
    return text

def process_year(year):
    input_path = f"data/exams/HS_{year}_questions.txt"
    output_path = f"data/exams/clean_HS_{year}.txt"
    
    if not os.path.exists(input_path):
        print(f"Skipping {year}: {input_path} not found")
        return

    print(f"Processing HS {year}...")
    normalized = normalize_text(input_path)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(normalized)
    
    print(f"Saved to {output_path}")

if __name__ == "__main__":
    years = ["2015", "2022", "2023", "2024"]
    for year in years:
        process_year(year)
