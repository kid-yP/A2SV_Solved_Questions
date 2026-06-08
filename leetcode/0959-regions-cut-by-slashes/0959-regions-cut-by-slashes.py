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
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        uf = UnionFind(4 * n * n)

        def idx(i, j, k):
            # k = 0: top, 1: right, 2: bottom, 3: left
            return (i * n + j) * 4 + k

        for i in range(n):
            for j in range(n):
                c = grid[i][j]
                # indices for 4 triangles
                top, right, bottom, left = idx(i,j,0), idx(i,j,1), idx(i,j,2), idx(i,j,3)

                if c == '/':
                    uf.union(top, left)
                    uf.union(right, bottom)
                elif c == '\\':
                    uf.union(top, right)
                    uf.union(bottom, left)
                else:  # space
                    uf.union(top, right)
                    uf.union(right, bottom)
                    uf.union(bottom, left)

                # connect with neighbors
                if i+1 < n:  # bottom of current with top of below
                    uf.union(bottom, idx(i+1,j,0))
                if j+1 < n:  # right of current with left of right neighbor
                    uf.union(right, idx(i,j+1,3))

        # counting distinct regions
        roots = set()
        for x in range(4*n*n):
            roots.add(uf.find(x))
        return len(roots)
