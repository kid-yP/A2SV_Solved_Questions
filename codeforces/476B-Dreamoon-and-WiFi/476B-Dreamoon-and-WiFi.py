def backtrack(i, pos):
    global total, good
    
    if i == len(s2):
        total += 1
        if pos == target:
            good += 1
        return
    
    if s2[i] == '+':
        backtrack(i + 1, pos + 1)
    elif s2[i] == '-':
        backtrack(i + 1, pos - 1)
    else:  # '?'
        backtrack(i + 1, pos + 1)
        backtrack(i + 1, pos - 1)

backtrack(0, 0)

print(good / total)