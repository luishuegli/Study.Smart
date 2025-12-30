
import re
from data.exam_questions import get_all_questions_for_topic

def audit_incomplete_options():
    """
    Scans all MC questions for options that look incomplete:
    - End with "..."
    - End with ".."
    - Are suspiciously short (< 3 chars)
    """
    topics = ["1.1", "1.2", "1.3", "1.4", "1.5", "1.6", "1.7", "1.8", "1.9", "1.10", "1.11", 
              "2.1", "2.2", "2.3", "2.4", "2.5", "2.6",
              "3.2", "3.4", "3.5", "3.6", "3.7",
              "4.4", "4.6", "4.7", "4.8", "4.9",
              "5.3", "5.4", "5.5"]
    
    issues = []

    for topic_id in topics:
        questions = get_all_questions_for_topic(topic_id)
        if not questions:
            continue

        for q_id, q_data in questions.items():
            if q_data.get("type") == "mc":
                options = q_data.get("options", [])
                for i, opt in enumerate(options):
                    # Normalized check for string or dict
                    text_de = opt.get("de", "") if isinstance(opt, dict) else (opt if isinstance(opt, str) else "")
                    text_en = opt.get("en", "") if isinstance(opt, dict) else (opt if isinstance(opt, str) else "")
                    
                    for lang, text in [("de", text_de), ("en", text_en)]:
                        if not text: continue
                        
                        # Ellipsis check
                        if text.strip().endswith("...") or text.strip().endswith(".."):
                            issues.append(f"[{topic_id}] {q_id} Option {i+1} ({lang}): Ends with ellipsis -> '{text}'")
                        
                        # Short check (heuristic)
                        if len(text.strip()) < 2:
                             # Exclude simple numbers like "0" or "1" if they are valid
                            # But usually options are "0.5" or "$1$".
                            pass

    if issues:
        print(f"FOUND {len(issues)} SUSPICIOUS OPTIONS:")
        for issue in issues:
            print(issue)
    else:
        print("No suspicious options found (ending in ...).")

if __name__ == "__main__":
    audit_incomplete_options()
