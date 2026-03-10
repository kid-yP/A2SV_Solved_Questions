n, m = map(int, input().split())
s = []
for _ in range(n):
    s.append(input())
query = []
q = int(input())
for _ in range(q):
    query.append(list(map(int, input().split())))

p = [[0 for _ in range(m+1)] for _ in range(n+1)]
matrix = [[0 for _ in range(m+1)] for _ in range(n+1)]

for i in range(1, n + 1):
    for j in range(2, m + 1):
        matrix[i][j] = 1 if s[i-1][j-2] == "." and s[i-1][j-1] == "." else 0

for i in range(2,n+1):
    for j in range(1,m+1):
        p[i][j] = 1 if s[i-2][j-1] == "." and s[i-1][j-1] == "." else 0
        
for i in range(1,n+1):
    for j in range(1,m+1):
        matrix[i][j] += matrix[i][j-1] + matrix[i-1][j] - matrix[i-1][j-1]
        
for j in range(1,m+1):
    for i in range(1,n+1):
        p[i][j] += p[i-1][j] + p[i][j-1] - p[i-1][j-1]

for r1,c1,r2,c2 in query:
    if r1 == r2 and c1 == c2:
        print(0)
        continue
    
    output = p[r2][c2]-p[r2][c1-1]-p[r1][c2] +p[r1][c1-1] + matrix[r2][c2]-matrix[r2][c1] - matrix[r1-1][c2] + matrix[r1-1][c1]
    
    print(output)