import ast
import os
import glob
from collections import defaultdict

DATA_DIR = "/Users/luis/Downloads/Study.Smart/data"

def extract_keys_from_file(filepath):
    """Extracts question IDs from a python file using AST."""
    with open(filepath, "r") as f:
        try:
            tree = ast.parse(f.read())
        except SyntaxError:
            print(f"SyntaxError in {filepath}")
            return set()
            
    keys = set()
    for node in tree.body:
        if isinstance(node, ast.Assign):
            # Case 1: Variable name itself is the ID (e.g. hs2024_mc1 = {...})
            for target in node.targets:
                if isinstance(target, ast.Name):
                    name = target.id
                    if any(name.startswith(p) for p in ["hs", "uebung", "test", "prob", "mc"]):
                        keys.add(name)
            
            # Case 2: Dictionary assignment (e.g. HS_2015_STAGING = {"hs2015_mc1": ...})
            if isinstance(node.value, ast.Dict):
                for key_node in node.value.keys:
                    if isinstance(key_node, ast.Constant): # Python 3.8+
                        val = key_node.value
                        if isinstance(val, str) and any(val.startswith(p) for p in ["hs", "uebung", "test", "prob", "mc"]):
                            keys.add(val)
                    elif isinstance(key_node, ast.Str): # Python <3.8
                        val = key_node.s
                        if isinstance(val, str) and any(val.startswith(p) for p in ["hs", "uebung", "test", "prob", "mc"]):
                            keys.add(val)
    return keys

def get_implemented_questions(exam_questions_path):
    """Extracts all keys from QUESTIONS_* dictionaries in exam_questions.py"""
    with open(exam_questions_path, "r") as f:
        try:
            tree = ast.parse(f.read())
        except SyntaxError:
            print(f"SyntaxError in {exam_questions_path}")
            return set()

    keys = set()
    for node in tree.body:
        if isinstance(node, ast.Assign):
            # Look for variable names starting with QUESTIONS_
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id.startswith("QUESTIONS_"):
                     if isinstance(node.value, ast.Dict):
                        for key_node in node.value.keys:
                            if isinstance(key_node, ast.Constant):
                                keys.add(key_node.value)
                            elif isinstance(key_node, ast.Str):
                                keys.add(key_node.s)
    return keys

def main():
    staging_files = glob.glob(os.path.join(DATA_DIR, "staging_*.py"))
    
    implemented_keys = get_implemented_questions(os.path.join(DATA_DIR, "exam_questions.py"))
    
    print(f"Total Implemented Questions Found: {len(implemented_keys)}")
    
    missing_map = defaultdict(list)
    
    for s_file in staging_files:
        s_keys = extract_keys_from_file(s_file)
        basename = os.path.basename(s_file)
        
        # Determine missing
        missing = [k for k in s_keys if k not in implemented_keys]
        if missing:
            missing_map[basename] = sorted(missing)

    print("\n--- MISSING QUESTIONS ---")
    if not missing_map:
        print("None! All staging questions are implemented.")
    else:
        for fname, q_ids in missing_map.items():
            print(f"\n[{fname}] ({len(q_ids)} missing)")
            for q in q_ids:
                print(f"  - {q}")

if __name__ == "__main__":
    main()
