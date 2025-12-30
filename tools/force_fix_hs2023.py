
def fix_hs2023_leak_v4():
    path = 'data/exam_questions.py'
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    start_leak_idx = -1
    signature = "1.50    0.0668" 
    
    for i, line in enumerate(lines):
        if signature in line:
            start_leak_idx = i
            print(f"Found leak start at {i+1}") # 4955
            break
            
    if start_leak_idx == -1:
        print("Could not find leak start signature.")
        return
        
    end_leak_idx = -1
    # Look for the solution key of THIS question 
    
    for i in range(start_leak_idx, min(start_leak_idx + 1000, len(lines))):
        if '"solution": {' in line or '"solution": {' in lines[i]:
             # Double check loose match
             if "solution" in lines[i] and ":" in lines[i] and "{" in lines[i]:
                end_leak_idx = i
                print(f"Found solution block start at {i+1}")
                break
                
    if end_leak_idx == -1:
        print("Could not find solution block.")
        return
        
    # We want to delete from start_leak_idx (inclusive)
    # Up to end_leak_idx - 1 (exclusive of the }, line).
    # Wait. lines[end_leak_idx] is "solution": {
    # lines[end_leak_idx - 1] is },
    # We want to KEEP lines[end_leak_idx - 1].
    # So we want the new list to be:
    # lines[:start_leak_idx] + lines[end_leak_idx - 1:]
    
    print(f"Deleting from {start_leak_idx+1} to {end_leak_idx-1} (lines)")
    
    new_lines = lines[:start_leak_idx] + lines[end_leak_idx - 1:]
    
    with open(path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    print("Success. File saved.")

if __name__ == "__main__":
    fix_hs2023_leak_v4()
