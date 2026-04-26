from collections import deque

t = int(input())
for _ in range(t):
    n = int(input())
    s = [input().strip() for _ in range(n)]
    
    adj = [[] for _ in range(n + 1)]
    indeg = [0] * (n + 1)
    
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if s[i - 1][j - 1] == '1':
                adj[i].append(j)
                indeg[j] += 1
            else:
                adj[j].append(i)
                indeg[i] += 1
    
    q = deque()
    for i in range(1, n + 1):
        if indeg[i] == 0:
            q.append(i)
    
    perm = []
    while q:
        u = q.popleft()
        perm.append(u)
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    
    print(*perm)