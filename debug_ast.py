import ast

def debug_node(file_path, target_id="hs2023_mc6"):
    with open(file_path, 'r', encoding='utf-8') as f:
        source = f.read()
    
    tree = ast.parse(source)
    lines = source.splitlines(keepends=True)
    
    for node in tree.body:
        if isinstance(node, ast.Assign) and isinstance(node.value, ast.Dict):
            for i, k in enumerate(node.value.keys):
                key = k.value if isinstance(k, ast.Constant) else k.s
                if key == target_id:
                    print(f"Found {key}")
                    q_val = node.value.values[i]
                    for j, sub_k in enumerate(q_val.keys):
                        sub_key = sub_k.value if isinstance(sub_k, ast.Constant) else sub_k.s
                        if sub_key == "question":
                            question_dict = q_val.values[j]
                            for m, lang_k in enumerate(question_dict.keys):
                                lang = lang_k.value if isinstance(lang_k, ast.Constant) else lang_k.s
                                if lang == "de":
                                    de_node = question_dict.values[m]
                                    print(f"DE Node: Lines {de_node.lineno}-{de_node.end_lineno}")
                                    print(f"Start Col: {de_node.col_offset}, End Col: {de_node.end_col_offset}")
                                    
                                    # Show extracted text from source
                                    s_line = de_node.lineno - 1
                                    e_line = de_node.end_lineno - 1
                                    
                                    if s_line == e_line:
                                        raw = lines[s_line][de_node.col_offset:de_node.end_col_offset]
                                    else:
                                        raw = lines[s_line][de_node.col_offset:]
                                        for l in range(s_line+1, e_line):
                                            raw += lines[l]
                                        raw += lines[e_line][:de_node.end_col_offset]
                                        
                                    print("--- RAW CONTENT ---")
                                    print(raw)
                                    print("--- END RAW ---")
                                    
                                    # Check suffix
                                    suffix = lines[e_line][de_node.end_col_offset:]
                                    print(f"--- SUFFIX (Line {e_line+1}) ---")
                                    print(repr(suffix))

if __name__ == "__main__":
    debug_node("data/exam_questions.py")
