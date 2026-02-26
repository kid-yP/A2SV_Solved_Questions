t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
 
    result = []
    result.append(p[0])
    for i in range(1, len(p) - 1):
        if (p[i] > p[i - 1] and p[i] > p[i + 1]) or (p[i] < p[i + 1] and p[i] < p[i - 1]):
            result.append(p[i])
    
    result.append(p[n-1])
 
    print(len(result))
    print(*result)
