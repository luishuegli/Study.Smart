
import re

def deduplicate_exec():
    path = 'data/exam_questions.py'
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    # Regex for top-level keys (4 spaces indentation)
    # Exclude commented lines
    key_pattern = re.compile(r'^    "([^"]+)": \{')
    
    seen_keys = set()
    deletion_ranges = [] # List of (start_idx, end_idx) INCLUSIVE
    
    i = 0
    while i < len(lines):
        line = lines[i]
        match = key_pattern.match(line)
        
        if match:
            key = match.group(1)
            
            if key in seen_keys:
                print(f"Duplicate Key Found: {key} at line {i+1}")
                # This is a duplicate. Mark for deletion.
                start_del = i
                
                # Find end of this block.
                # Format is usually:
                #     "key": {
                #         ...
                #     },
                # We look for a line starting with '    },' or just '    }'
                
                end_del = -1
                # Scan forward
                bracket_depth = 1 # We just passed the opening {
                
                for j in range(i+1, len(lines)):
                    # Simple indentation heuristic:
                    # If we find a line '    },' or '    }' (4 spaces), it closes the block.
                    # BUT internal blocks like "solution": { ... } also end with 8 spaces.
                    # We look for 4 spaces closing brace.
                    
                    # Better heuristic: Count braces? No, raw strings might contain braces.
                    # Indentation is reliable here.
                    
                    if lines[j].startswith('    },') or lines[j].strip() == '    },':
                        end_del = j
                        break
                    if lines[j].startswith('    }') and lines[j].strip() == '    }':
                        end_del = j
                        break
                
                if end_del != -1:
                    # Check if next line is empty or comma?
                    # Usually '    },' is followed by newline.
                    print(f"  -> Marking deletion from {start_del+1} to {end_del+1}")
                    deletion_ranges.append((start_del, end_del))
                    i = end_del # Skip forward
                else:
                    print(f"  -> CRITICAL: Could not find closing brace for {key} at {i+1}. Skipping.")
                    
            else:
                seen_keys.add(key)
        
        i += 1
        
    if not deletion_ranges:
        print("No duplicates found.")
        return

    # Delete ranges in reverse order
    deletion_ranges.sort(key=lambda x: x[0], reverse=True)
    
    for start, end in deletion_ranges:
        print(f"Deleting lines {start+1}-{end+1}")
        # Delete the slice
        # +1 on end because slice end is exclusive
        del lines[start : end+1]
        
    with open(path, 'w', encoding='utf-8') as f:
        f.writelines(lines)
    print("File saved.")

if __name__ == "__main__":
    deduplicate_exec()
