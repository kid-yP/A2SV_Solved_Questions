class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]
        self.rank = [1] * (n+1)
 
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
 
    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)
 
        if rx == ry:
            return
 
        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
        elif self.rank[rx] > self.rank[ry]:
            self.parent[ry] = rx
        else:
            self.parent[ry] = rx
            self.rank[rx] += 1
 
 
 
 
n,m,k=map(int,input().split())
 
for _ in range(m):
    input()
 
operations=[]
 
for _ in range(k):
    t,u,v=input().split()
    operations.append((t,int(u),int(v)))
 
dsu=DSU(n)
 
answers=[]
for t, u, v in reversed(operations):
 
    if t == "ask":
        if dsu.find(u) == dsu.find(v):
            answers.append("YES")
        else:
            answers.append("NO")
 
    else: 
        dsu.union(u, v)
 
answers.reverse()
 
for ans in answers:
    print(ans)
