class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)
        self.count = n
    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        rootX, rootY = self.find(x), self.find(y)
        if rootX == rootY:
            return False
        if self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        elif self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1
        self.count -= 1
        return True

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        aliceUF = UnionFind(n)
        bobUF = UnionFind(n)
        removable = 0

        for t, u, v in edges:
            if t == 3:
                usedAlice = aliceUF.union(u, v)
                usedBob = bobUF.union(u, v)
                if not usedAlice and not usedBob:
                    removable += 1

        for t, u, v in edges:
            if t == 1:
                if not aliceUF.union(u, v):
                    removable += 1

        for t, u, v in edges:
            if t == 2:
                if not bobUF.union(u, v):
                    removable += 1

        if aliceUF.count != 1 or bobUF.count != 1:
            return -1
        return removable