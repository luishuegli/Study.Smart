import ast
import json
import re

def check_coverage(py_path, json_path):
    # 1. Load Mapped Keys
    with open(json_path, 'r', encoding='utf-8') as f:
        mapped_data = json.load(f)
    mapped_keys = set(mapped_data.keys())
    
    # 2. Load All HS Keys from Python
    with open(py_path, 'r', encoding='utf-8') as f:
        tree = ast.parse(f.read())
        
    all_hs_keys = []
    
    for node in tree.body:
        if isinstance(node, ast.Assign) and isinstance(node.value, ast.Dict):
            for i, k in enumerate(node.value.keys):
                key = k.value if isinstance(k, ast.Constant) else k.s
                # Filter for Exam keys (hsXXXX)
                if key and str(key).startswith("hs2"): # HS2015, HS2022, HS2023, HS2024
                    # Exclude HS2024 as it was done manually/previously? 
                    # User asked about "every single question". So check all.
                    all_hs_keys.append(key)
                elif key and str(key).startswith("hs2015"):
                    all_hs_keys.append(key)

    total = len(all_hs_keys)
    restored = len([k for k in all_hs_keys if k in mapped_keys])
    missing = [k for k in all_hs_keys if k not in mapped_keys]
    
    print(f"Total HS Keys found: {total}")
    print(f"Restored (Mapped): {restored}")
    print(f"Missing: {len(missing)}")
    print("--- MISSING KEYS ---")
    for k in sorted(missing):
        print(k)

if __name__ == "__main__":
    check_coverage("data/exam_questions.py", "data/id_to_text.json")
