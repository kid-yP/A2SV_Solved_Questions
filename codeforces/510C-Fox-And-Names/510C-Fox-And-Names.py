from collections import deque
n = int(input())
names = [input().strip() for _ in range(n)]

graph = [[] for _ in range(26)]
indeg = [0] * 26

for i in range(n - 1):
    s = names[i]
    t = names[i + 1]
    
    found = False
    
    for j in range(min(len(s), len(t))):
        if s[j] != t[j]:
            u = ord(s[j]) - ord('a')
            v = ord(t[j]) - ord('a')
            graph[u].append(v)
            indeg[v] += 1
            found = True
            break
    
    if not found and len(s) > len(t):
        print("Impossible")
        exit()

q = deque()
for i in range(26):
    if indeg[i] == 0:
        q.append(i)

res = []

while q:
    u = q.popleft()
    res.append(u)
    
    for v in graph[u]:
        indeg[v] -= 1
        if indeg[v] == 0:
            q.append(v)

if len(res) != 26:
    print("Impossible")
else:
    print(''.join(chr(x + ord('a')) for x in res))