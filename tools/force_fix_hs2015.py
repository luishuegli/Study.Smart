
def fix_hs2015_leak():
    path = 'data/exam_questions.py'
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    start_idx = -1
    end_idx = -1
    
    for i, line in enumerate(lines):
        if '"hs2015_prob5": {' in line:
            start_idx = i
        if 'QUESTIONS_9 = {' in line:
            end_idx = i
            break # Found the next section, stop.
            
    if start_idx != -1 and end_idx != -1:
        # We found the range.
        # But wait, end_idx is QUESTIONS_9. We want to cut UNTIL the closing brace of the previous section?
        # The leak is inside hs2015_prob5. 
        # So we can replace lines[start_idx : end_idx] with the CLEAN content + the closing of dictionary?
        
        # Actually, QUESTIONS_HS2015 ends before QUESTIONS_9.
        # Let's inspect the lines just before end_idx to preserve the closing bracket of the DICT.
        
        # We will replace from `start_idx` (inclusive) to `end_idx` (exclusive).
        # But we need to make sure we don't delete the `}` closing QUESTIONS_HS2015 if it's there.
        # Let's verify line end_idx-1.
        
        # New Content
        clean_entry = r'''    "hs2015_prob5": {
        "source": "HS 2015, Aufgabe 5 (20 Punkte)",
        "type": "problem",
        "question": {
            "de": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Aufgabe 5 (20 Punkte)
Wir betrachten eine stetige Verteilung mit folgender Dichtefunktion:
$$f(x) = \begin{cases} \frac{\alpha}{x^{\alpha+1}} & \text{für } x \ge 1 \\ 0 & \text{sonst} \end{cases}$$
wobei $\alpha > 0$ ein unbekannter Parameter ist. Wir wollen einen Schätzer für den Parameter $\alpha$ finden.
1. (7 Punkte) Bestimmen Sie den Maximum Likelihood Schätzer für $\alpha$ basierend auf $n$ unabhängigen identisch verteilten Beobachtungen $X_1, \dots, X_n$ einer Zufallsvariablen mit der obigen Dichtefunktion $f$.
2. (2 Punkte) Berechnen Sie den Maximum Likelihood Schätzer für die folgende konkrete Stichprobe:
$x_1=11.0, x_2=16.4, x_3=27.9, x_4=15.9$
3. (7 Punkte) Bestimmen Sie einen Momentenmethodeschätzer für $\alpha > 1$ basierend auf $n$ unabhängigen identisch verteilten Beobachtungen $X_1, \dots, X_n$. Sie müssen für diese Teilaufgabe annehmen, dass $\alpha > 1$ ist, da ansonsten der Erwartungswert nicht definiert (unendlich) ist.
4. (2 Punkte) Berechnen Sie den Momentenmethodeschätzer für die obige Stichprobe.
5. (2 Punkte) Vergleichen Sie den Maximum Likelihood Schätzer und den Momentenmethodeschätzer für die obige Stichprobe. Ist der Momentenschätzer hier sinnvoll?</span>""",
            "en": r"""<span style='font-family: "Source Serif Pro", "Cambria", serif; font-size: 20px;'>Problem 5 (20 Points)
We consider a continuous distribution with the following density function:
$$f(x) = \begin{cases} \frac{\alpha}{x^{\alpha+1}} & \text{for } x \ge 1 \\ 0 & \text{otherwise} \end{cases}$$
where $\alpha > 0$ is an unknown parameter. We want to find an estimator for the parameter $\alpha$.
1. (7 Points) Determine the Maximum Likelihood Estimator (MLE) for $\alpha$ based on $n$ independent identically distributed observations $X_1, \dots, X_n$ of a random variable with the above density function $f$.
2. (2 Points) Calculate the MLE for the following specific sample:
$x_1=11.0, x_2=16.4, x_3=27.9, x_4=15.9$
3. (7 Points) Determine a Method of Moments estimator for $\alpha > 1$ based on $n$ independent identically distributed observations $X_1, \dots, X_n$. You must assume for this part that $\alpha > 1$, as otherwise the expected value is undefined (infinite).
4. (2 Points) Calculate the Method of Moments estimator for the above sample.
5. (2 Points) Compare the MLE and the Method of Moments estimator for the above sample. Is the Method of Moments estimator sensible here?</span>"""
        },
        "solution": {
            "de": r"**Lösung:**<br>1. $\hat{\alpha}_{MLE} = \frac{n}{\sum \ln x_i}$.<br>2. $\hat{\alpha} \approx 0.35$. (Achtung: Dichte braucht $\alpha > 0$.)<br>3. $E[X] = \frac{\alpha}{\alpha-1}$. Auflösen nach $\alpha$: $\hat{\alpha}_{MM} = \frac{\bar{x}}{\bar{x}-1}$.<br>4. $\bar{x}=17.8 \Rightarrow \hat{\alpha} \approx 1.06$.<br>5. Momentenmethode nur für $\alpha > 1$ definiert.",
            "en": r"**Solution:**<br>1. $\hat{\alpha}_{MLE} = \frac{n}{\sum \ln x_i}$.<br>2. $\hat{\alpha} \approx 0.35$. (Note: Density needs $\alpha > 0$.)<br>3. $E[X] = \frac{\alpha}{\alpha-1}$. Solve for $\alpha$: $\hat{\alpha}_{MM} = \frac{\bar{x}}{\bar{x}-1}$.<br>4. $\bar{x}=17.8 \Rightarrow \hat{\alpha} \approx 1.06$.<br>5. Method of Moments only defined for $\alpha > 1$."
        }
    },
}

'''
        # We need to preserve the closing block of the file if needed.
        # Check lines[end_idx]. It is QUESTIONS_9 = {
        # lines[end_idx-1] is usually blank or }
        
        # We will replace everything from start_idx up to end_idx with clean_entry
        # BUT clean_entry includes the closing brace `}` for the Dict `QUESTIONS_HS2015`.
        
        print(f"Replacing lines {start_idx} to {end_idx} with clean entry.")
        
        # Logic: slice replacement
        new_lines = lines[:start_idx] + [clean_entry] + lines[end_idx:]
        
        with open(path, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        print("Success.")

if __name__ == "__main__":
    fix_hs2015_leak()
