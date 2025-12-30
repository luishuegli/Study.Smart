
def fix_translation():
    path = 'data/exam_questions.py'
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # 1. Find hs2015_prob1
    start_idx = -1
    for i, line in enumerate(lines):
        if '"hs2015_prob1": {' in line:
            start_idx = i
            break
            
    if start_idx == -1:
        print("Key not found")
        return
        
    # 2. Find "en": ... inside this block
    en_idx = -1
    for i in range(start_idx, start_idx + 200):
        if 'Match the distributions to the plots.<br>V1' in lines[i]:
            en_idx = i
            break
            
    if en_idx == -1:
        print("EN line not found")
        return
        
    print(f"Found EN at line {en_idx+1}")
    
    # 3. Replace the line
    new_text = r"""            "en": r""" + '"' + r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Problem 1 (12 Points)
Part 1A (4 Points)
We have drawn random samples of 100 observations each from the following four distributions V1, V2, V3, and V4:
V1) Normal distribution with expected value $\mu = 0$ and variance $\sigma^2 = 3$. Sample size: $n_1 = 100$.
V2) Exponential distribution with parameter $\lambda = 3$. Sample size: $n_2 = 100$.
V3) Normal distribution with expected value $\mu = 0$ and variance $\sigma^2 = 1$. Sample size: $n_3 = 100$.
V4) Uniform distribution U $[-3, 3]$. Sample size: $n_4 = 100$.
Below are a Boxplot (A), a Histogram (B), an empirical cumulative distribution function (C), and a QQ-Plot (vs. Normal distribution) (D) given for one sample each.
Match the respective graphics (A, B, C, and D) to the corresponding samples (V1, V2, V3, and V4), e.g., V1: D.
Important: Each sample corresponds to exactly one graphic!
A                                                                                   B
1.5
●
10 15 20
●
1.0
0.5
0.0
-2        -1       0       1       2       3
C                                                                                   D
1 2 3
●● ●                                                                                ●●● ●
Empirical Quantiles
●
●●●
●●                                                                                  ●●●●
●
●●                                                                                ●●
●●
●
●●●
●                                                                                 ●
●
0.8
●●●                                                                                ●
●
●●                                                                                  ●
●
●●
●
●                                                                                  ●
●
●●
●
●●
●●●                                                                                ●●
●
●
●●
●
●
●●                                                                                 ●●
●
Fn(x)
0.6
0.4
0.2
0.0
-4
-2
0
2
4
Data
Part 1B (8 Points)
The results of the statistics exam at the University of Hawaii yielded the following frequency table:
Grade    0.7   1.0   1.3   2.0   2.3   3.0   3.7   4.0   4.3   4.7   5.0
ni       1     0     0     0     5     6     6     4     6     4     7
1. (2 Points) Calculate the mean and mode of the sample.
2. (6 Points) Draw a boxplot, calculate the corresponding measures, and draw them in.
If you need more space, make a clear reference on the exam sheet and label the additional sheet clearly as well. Otherwise, the task will not be graded.</span>""" + '"' + "\n"

    lines[en_idx] = new_text
    
    with open(path, 'w', encoding='utf-8') as f:
        f.writelines(lines)
    print("Success")

if __name__ == "__main__":
    fix_translation()
