import re
import json
import os
import ast

def load_exam_keys(py_file_path):
    """
    Parses data/exam_questions.py using AST to find all question keys and their sources.
    Returns: { "hs2023_mc1": "HS 2023 Januar, MC #1", ... }
    """
    with open(py_file_path, 'r', encoding='utf-8') as f:
        tree = ast.parse(f.read())
    
    key_map = {}
    
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id.startswith("QUESTIONS"):
                    if isinstance(node.value, ast.Dict):
                        for i, k in enumerate(node.value.keys):
                            if isinstance(k, ast.Constant): # Python 3.8+
                                key = k.value
                            elif isinstance(k, ast.Str): # Python <3.8
                                key = k.s
                            else:
                                continue
                                
                            # Find 'source' in the value dict
                            val = node.value.values[i]
                            source_str = ""
                            if isinstance(val, ast.Dict):
                                for j, vk in enumerate(val.keys):
                                    v_key_name = vk.value if isinstance(vk, ast.Constant) else vk.s
                                    if v_key_name == "source":
                                        v_val = val.values[j]
                                        source_str = v_val.value if isinstance(v_val, ast.Constant) else v_val.s
                                        break
                            
                            if key and source_str:
                                key_map[key] = source_str
    return key_map

def parse_normalized_text(year, text_path):
    """
    Parses clean_HS_20xx.txt into structure:
    {
        "mc": {"1": "Text...", "2": "Text..."},
        "problem": {"1": "Text...", ...}
    }
    """
    with open(text_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    data = {"mc": {}, "problem": {}}
    
    # State Machine approach
    mode = "MC" # Default start, but check first line
    buffer = []
    current_key = None
    
    for line in lines:
        line = line.strip()
        if not line: continue
        
        # Check for Problem Header
        # "Problem 1", "Aufgabe 1", "Teil 2A", "Task 1"
        prob_match = re.match(r'^(Problem|Aufgabe)\s+(\d+)', line)
        if prob_match:
            # Save previous
            if current_key:
                section_dict = data["problem"] if mode == "PROBLEM" else data["mc"]
                section_dict[current_key] = "\n".join(buffer).strip()
            
            mode = "PROBLEM"
            current_key = prob_match.group(2) # Problem Number
            buffer = [line]
            continue
        
        # Check for MC Numbering (only in MC mode)
        # e.g. "1. (4 Punkte)"
        mc_match = re.match(r'^(\d+)\.\s+\(\d+\s+Punkte\)', line)
        
        # Avoid capturing sub-questions inside problems (e.g. "1. (3 Punkte)")
        # Heuristic: If we are in PROBLEM mode, we stay there until next Problem/Aufgabe header?
        # But wait, exams might switch back? Unlikely.
        # However, sub-questions inside problems often start with "1." too.
        # So we only switch key if we are in MC mode.
        
        if mode == "MC" and mc_match:
            if current_key:
                # Save previous MC
                data["mc"][current_key] = "\n".join(buffer).strip()
            
            current_key = mc_match.group(1)
            buffer = [line]
        else:
            # Append to buffer
            if current_key: # Only buffer if we have started a question
                buffer.append(line)
            
    # Save last
    if current_key:
        section_dict = data["problem"] if mode == "PROBLEM" else data["mc"]
        section_dict[current_key] = "\n".join(buffer).strip()

    return data

def main():
    py_path = "data/exam_questions.py"
    key_map = load_exam_keys(py_path)
    
    years = ["2015", "2022", "2023", "2024"]
    final_output = {}
    
    for year in years:
        txt_path = f"data/exams/clean_HS_{year}.txt"
        if not os.path.exists(txt_path):
            continue
            
        print(f"Mapping HS {year}...")
        parsed_data = parse_normalized_text(year, txt_path)
        
        # Match keys
        # Key format: hs2022_mc1 -> "HS 2022 ..., MC #1"
        
        for k, v in key_map.items():
            if f"HS {year}" in v or f"HS_{year}" in v or f"HS{year}" in k: # Hybrid matching
                # Determine type and number
                q_num = None
                q_type = None
                
                if "MC #" in v or "MC" in v:
                    q_type = "mc"
                    # Try explicit "MC #1"
                    if "MC #" in v:
                        q_num = v.split("MC #")[1].split()[0].replace(',', '').strip()
                    elif "MC" in v:
                         # Fallback regex on key or source
                         match = re.search(r'MC\s+(\d+)', v)
                         if match:
                             q_num = match.group(1)
                
                if not q_num and "mc" in k:
                     match = re.search(r'mc(\d+)', k)
                     if match:
                         q_type = "mc"
                         q_num = match.group(1)

                if "Problem" in v or "Aufgabe" in v or "prob" in k:
                    q_type = "problem"
                    # Pattern: "HS 2023 ..., Problem 1" or "Aufgabe 1"
                    # Or check key: hs2022_prob1
                    
                    # Try extracting from source string
                    prob_match = re.search(r'(Problem|Aufgabe)\s+(\d+)', v)
                    if prob_match:
                        q_num = prob_match.group(2)
                    else:
                        # Try extracting from key
                        match = re.search(r'prob(\d+)', k)
                        if match:
                            q_num = match.group(1)
                
                if q_type and q_num:
                    # Look up in parsed data
                    if q_type in parsed_data and q_num in parsed_data[q_type]:
                        final_output[k] = parsed_data[q_type][q_num]
                    
    # Save mapping
    with open("data/id_to_text.json", "w", encoding='utf-8') as f:
        json.dump(final_output, f, indent=2, ensure_ascii=False)
        
    print(f"Mapped {len(final_output)} questions.")

if __name__ == "__main__":
    main()
