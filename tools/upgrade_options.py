import ast
import json

def upgrade_options(py_path):
    with open(py_path, 'r', encoding='utf-8') as f:
        source = f.read()
    
    tree = ast.parse(source)
    lines = source.splitlines(keepends=True)
    replacements = []
    
    for node in tree.body:
        if isinstance(node, ast.Assign) and isinstance(node.value, ast.Dict):
            for i, k in enumerate(node.value.keys):
                # Inside a question dict
                q_val = node.value.values[i]
                if isinstance(q_val, ast.Dict):
                    for j, sub_k in enumerate(q_val.keys):
                        key_name = sub_k.value if isinstance(sub_k, ast.Constant) else sub_k.s
                        if key_name == "options":
                            opt_node = q_val.values[j]
                            if isinstance(opt_node, ast.List):
                                # Check elements
                                needs_upgrade = False
                                for elt in opt_node.elts:
                                    if isinstance(elt, ast.Constant): # Python 3.8+ strings are Constants
                                        needs_upgrade = True
                                        break
                                
                                if needs_upgrade:
                                    # Convert current list to dict list
                                    # We need to extract the raw strings carefully
                                    # This is tricky with AST if we want to preserve r-strings or fancy formatting.
                                    # Simplest approach: Use the range of the list and replace it with new text.
                                    
                                    # Extract items
                                    new_items = []
                                    for elt in opt_node.elts:
                                        if isinstance(elt, ast.Constant):
                                            val = elt.value
                                            # Create dict representation
                                            # We use repr() to safe-encode, but we want r"" if LaTeX
                                            # Heuristic: if '$' in val, use r"".
                                            
                                            def to_repr(s):
                                                if "\\" in s or "$" in s:
                                                    return 'r"' + s.replace('"', '\\"') + '"'
                                                return json.dumps(s, ensure_ascii=False)

                                            item_str = f'{{"de": {to_repr(val)}, "en": {to_repr(val)}}}'
                                            new_items.append(item_str)
                                        elif isinstance(elt, ast.Dict):
                                            # Already dict, keep source text?
                                            # Hard to extract exact source without tokens.
                                            # Re-serialize
                                            # This is risky if we mix types.
                                            pass
                                            
                                    replacement_text = "[\n            " + ",\n            ".join(new_items) + "\n        ]"
                                    
                                    replacements.append({
                                        "start": opt_node.lineno,
                                        "end": opt_node.end_lineno,
                                        "col": opt_node.col_offset,
                                        "end_col": opt_node.end_col_offset,
                                        "text": replacement_text
                                    })

    # Apply reverse
    replacements.sort(key=lambda x: x["start"], reverse=True)
    
    for rep in replacements:
        s = rep["start"] - 1
        e = rep["end"] - 1
        # Extract surrounding context if single line but we always replace full node?
        # Actually list can be multiline.
        
        # If single line list: lines[s] = ...
        if s == e:
            lines[s] = lines[s][:rep["col"]] + rep["text"] + lines[s][rep["end_col"]:]
        else:
            # Start
            lines[s] = lines[s][:rep["col"]] + rep["text"]
            # Middle delete
            for k in range(s+1, e):
                lines[k] = ""
            # End
            lines[e] = lines[e][rep["end_col"]:]
            
    with open(py_path, 'w', encoding='utf-8') as f:
        f.write("".join(lines))
        
    print(f"Upgraded {len(replacements)} option lists.")

if __name__ == "__main__":
    upgrade_options("data/exam_questions.py")
