t = int(input())
for _ in range(t):
    n = int(input())
    a = input().strip()
    b = input().strip()
    
    zeros = 0
    ones = 0
    valid = [False] * n
    
    for i in range(n):
        if a[i] == '0':
            zeros += 1
        else:
            ones += 1
        if zeros == ones:
            valid[i] = True
    
    flipped = False
    possible = True
    
    for i in range(n - 1, -1, -1):
        current = a[i]
        if flipped:
            if current == '0':
                current = '1'
            else:
                current = '0'

        
        if current != b[i]:
            if valid[i]:
                flipped = not flipped
            else:
                possible = False
                break
    
    print("YES" if possible else "NO")
