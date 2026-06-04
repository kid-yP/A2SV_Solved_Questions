class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> None:
        rootX, rootY = self.find(x), self.find(y)
        if rootX == rootY:
            return
        if self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        elif self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        edgeList.sort(key=lambda x: x[2])
        
        queries = [(p, q, limit, i) for i, (p, q, limit) in enumerate(queries)]
        queries.sort(key=lambda x: x[2])
        
        uf = UnionFind(n)
        res = [False] * len(queries)
        edge_idx = 0
        
        for p, q, limit, i in queries:
            while edge_idx < len(edgeList) and edgeList[edge_idx][2] < limit:
                u, v, w = edgeList[edge_idx]
                uf.union(u, v)
                edge_idx += 1
            res[i] = (uf.find(p) == uf.find(q))
        
        return res