import ast
import json
import os

STYLE_PREFIX = r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>"""
STYLE_SUFFIX = r"""</span>"""

def restore_questions(py_file_path, map_file_path):
    # 1. Load Map
    with open(map_file_path, 'r', encoding='utf-8') as f:
        text_map = json.load(f)
        
    # 2. Read Source
    with open(py_file_path, 'r', encoding='utf-8') as f:
        source_code = f.read()
    
    # 3. Parse AST
    tree = ast.parse(source_code)
    
    replacements = []
    
    # 4. Traverse
    for node in tree.body:
        if isinstance(node, ast.Assign):
            # Check if assignment to QUESTIONS_... implies a dict
            if isinstance(node.value, ast.Dict):
                # Iterate keys (exam ids)
                for i, k_node in enumerate(node.value.keys):
                    if isinstance(k_node, ast.Constant):
                        q_id = k_node.value
                    elif isinstance(k_node, ast.Str):
                        q_id = k_node.s
                    else:
                        continue
                        
                    if q_id in text_map:
                        # Found a question to restore
                        q_val = node.value.values[i]
                        
                        # Find 'question' -> 'de'
                        if isinstance(q_val, ast.Dict):
                            de_node = None
                            for j, sub_k in enumerate(q_val.keys):
                                sub_k_name = sub_k.value if isinstance(sub_k, ast.Constant) else sub_k.s
                                if sub_k_name == "question":
                                    question_dict = q_val.values[j]
                                    if isinstance(question_dict, ast.Dict):
                                        for m, lang_k in enumerate(question_dict.keys):
                                            lang_name = lang_k.value if isinstance(lang_k, ast.Constant) else lang_k.s
                                            if lang_name == "de":
                                                de_node = question_dict.values[m]
                                                break
                                    break
                            
                            if de_node:
                                # Prepare replacement
                                new_text_raw = text_map[q_id]
                                # Create formatted string
                                new_text_content = f'{STYLE_PREFIX}{new_text_raw}{STYLE_SUFFIX}'
                                # Python repr to handle escaping safely, but we want r"""...""" preferrably
                                # Simplest is to manually verify formatting.
                                # But `repr()` might give single quotes.
                                # Let's construct a raw triple-quote string.
                                # Escape triple quotes inside content
                                escaped_content = new_text_content.replace('"""', '\\"\\"\\"')
                                replacement_str = 'r"""' + escaped_content + '"""'
                                
                                replacements.append({
                                    "start_lineno": de_node.lineno,
                                    "start_col_offset": de_node.col_offset,
                                    "end_lineno": de_node.end_lineno,
                                    "end_col_offset": de_node.end_col_offset,
                                    "text": replacement_str
                                })

    # 5. Apply Replacements (Reverse Order)
    replacements.sort(key=lambda x: (x["start_lineno"], x["start_col_offset"]), reverse=True)
    
    lines = source_code.splitlines(keepends=True)
    
    for rep in replacements:
        s_line = rep["start_lineno"] - 1
        e_line = rep["end_lineno"] - 1
        s_col = rep["start_col_offset"]
        e_col = rep["end_col_offset"]
        text = rep["text"]
        
        # Handle multi-line replacement
        if s_line == e_line:
            line = lines[s_line]
            lines[s_line] = line[:s_col] + text + line[e_col:]
        else:
            # Start line
            lines[s_line] = lines[s_line][:s_col] + text
            # Middle lines - DELETE
            for l in range(s_line + 1, e_line):
                lines[l] = "" # Mark for removal or just empty
            # End line
            lines[e_line] = lines[e_line][e_col:]
            
    # Rejoin and clean empty lines if needed (though "" works fine)
    new_code = "".join(lines)
    
    with open(py_file_path, 'w', encoding='utf-8') as f:
        f.write(new_code)
        
    print(f"Restored {len(replacements)} questions.")

if __name__ == "__main__":
    restore_questions("data/exam_questions.py", "data/id_to_text.json")
