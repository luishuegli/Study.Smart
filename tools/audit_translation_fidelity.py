
import re
import sys
import os

# Add parent dir to path to import data
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from data.exam_questions import QUESTIONS_1_1, QUESTIONS_1_2, QUESTIONS_1_3, QUESTIONS_1_4, QUESTIONS_1_5, QUESTIONS_1_6, QUESTIONS_1_7, QUESTIONS_1_9, QUESTIONS_1_10, QUESTIONS_1_11
    from data.exam_questions import QUESTIONS_2_1, QUESTIONS_2_2, QUESTIONS_2_3, QUESTIONS_2_4, QUESTIONS_2_5, QUESTIONS_2_6
    from data.exam_questions import QUESTIONS_3_1, QUESTIONS_3_2, QUESTIONS_3_3, QUESTIONS_3_4, QUESTIONS_3_5, QUESTIONS_3_6, QUESTIONS_3_7
    from data.exam_questions import QUESTIONS_4_2, QUESTIONS_4_3, QUESTIONS_4_4, QUESTIONS_4_5, QUESTIONS_4_6, QUESTIONS_4_7, QUESTIONS_4_8, QUESTIONS_4_9
    from data.exam_questions import QUESTIONS_5_1, QUESTIONS_5_2, QUESTIONS_5_3, QUESTIONS_5_4, QUESTIONS_5_5
    from data.exam_questions import QUESTIONS_6, QUESTIONS_6_3
    from data.exam_questions import QUESTIONS_7, QUESTIONS_7_6
    from data.exam_questions import QUESTIONS_8, QUESTIONS_8_4
    from data.exam_questions import QUESTIONS_9, QUESTIONS_9_4
    from data.exam_questions import QUESTIONS_10, QUESTIONS_10_5
    from data.exam_questions import QUESTIONS_11_1
except ImportError:
    # Fallback if imports fail (e.g., path issues)
    print("Error importing data. Make sure to run from project root.")
    sys.exit(1)

ALL_DICTS = [
    QUESTIONS_1_1, QUESTIONS_1_2, QUESTIONS_1_3, QUESTIONS_1_4, QUESTIONS_1_5, QUESTIONS_1_6, QUESTIONS_1_7, QUESTIONS_1_9, QUESTIONS_1_10, QUESTIONS_1_11,
    QUESTIONS_2_1, QUESTIONS_2_2, QUESTIONS_2_3, QUESTIONS_2_4, QUESTIONS_2_5, QUESTIONS_2_6,
    QUESTIONS_3_1, QUESTIONS_3_2, QUESTIONS_3_3, QUESTIONS_3_4, QUESTIONS_3_5, QUESTIONS_3_6, QUESTIONS_3_7,
    QUESTIONS_4_2, QUESTIONS_4_3, QUESTIONS_4_4, QUESTIONS_4_5, QUESTIONS_4_6, QUESTIONS_4_7, QUESTIONS_4_8, QUESTIONS_4_9,
    QUESTIONS_5_1, QUESTIONS_5_2, QUESTIONS_5_3, QUESTIONS_5_4, QUESTIONS_5_5,
    QUESTIONS_6, QUESTIONS_6_3,
    QUESTIONS_7, QUESTIONS_7_6,
    QUESTIONS_8, QUESTIONS_8_4,
    QUESTIONS_9, QUESTIONS_9_4,
    QUESTIONS_10, QUESTIONS_10_5,
    QUESTIONS_11_1
]

def clean_html(text):
    text = re.sub(r'<[^>]+>', '', text)
    text = text.replace('\n', ' ').strip()
    return text

def check_fidelity():
    count_scanned = 0
    flagged_items = []
    
    print("Starting Deep Audit...")
    
    # Thresholds
    # Benchmark was ~0.90. 
    # User suggested 20% diff is okay (0.80).
    # We flag anything < 0.80 as "Potential Content Loss".
    THRESHOLD_RATIO = 0.80
    
    for q_dict in ALL_DICTS:
        for q_id, data in q_dict.items():
            count_scanned += 1
            
            if 'question' not in data or 'de' not in data['question'] or 'en' not in data['question']:
                continue
                
            de_raw = data['question']['de']
            en_raw = data['question']['en']
            
            de_text = clean_html(de_raw)
            en_text = clean_html(en_raw)
            
            len_de = len(de_text)
            len_en = len(en_text)
            
            if len_de == 0: continue
            
            ratio = len_en / len_de
            issues = []
            
            # 1. Ratio Check
            if ratio < THRESHOLD_RATIO:
                severity = "CRITICAL" if ratio < 0.50 else "WARNING"
                issues.append(f"Short Translation ({int(ratio*100)}% of DE)")
                
            # 2. Prefix Check
            de_prefix_match = re.search(r'^\d+\.\s+\(\d+\s+Punkte\)', de_text)
            en_prefix_match = re.search(r'^\d+\.\s+\(\d+\s+Points\)', en_text)
            
            if de_prefix_match and not en_prefix_match:
                issues.append("Missing Point Prefix")
            
            # 3. Placeholder Check (Identical Text)
            # If EN text is identical to DE text (rare but possible placeholder)
            if de_text.strip() == en_text.strip() and len_de > 20:
                 issues.append("Identical Content (Untranslated?)")
                 
            if issues:
                flagged_items.append({
                    "id": q_id,
                    "ratio": ratio,
                    "issues": issues,
                    "de_preview": de_text[:50].replace('\n', ' '),
                    "en_preview": en_text[:50].replace('\n', ' ')
                })

    # Generate Markdown Report
    report_path = "/Users/luis/.gemini/antigravity/brain/84471815-7c82-4414-88ee-b1360d03ff82/fidelity_report.md"
    with open(report_path, "w") as f:
        f.write("# Global English Fidelity Report (Deep Scan)\n\n")
        f.write(f"**Total Scanned:** {count_scanned}\n")
        f.write(f"**Flagged Items:** {len(flagged_items)}\n")
        f.write(f"**Threshold:** < {int(THRESHOLD_RATIO*100)}% Length Ratio\n\n")
        
        f.write("| ID | Ratio | Issues | Preview |\n")
        f.write("|---|---|---|---|\n")
        
        # Sort by Ratio (ascending - worst first)
        flagged_items.sort(key=lambda x: x['ratio'])
        
        for item in flagged_items:
            ratio_str = f"{item['ratio']:.2f}"
            issues_str = ", ".join(item['issues'])
            f.write(f"| `{item['id']}` | **{ratio_str}** | {issues_str} | {item['en_preview']}... |\n")
            
    print(f"Report generated at {report_path}")
    print(f"Flagged {len(flagged_items)} items for review.")

if __name__ == "__main__":
    check_fidelity()
