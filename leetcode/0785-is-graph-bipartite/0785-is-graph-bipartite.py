class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [-1] * n

        def dfs(node, color):
            colors[node] = color
            for neighbor in graph[node]:
                if colors[neighbor] == -1:
                    if not dfs(neighbor, 1 - color):
                        return False
                elif colors[neighbor] == color:
                    return False
            return True

        for i in range(n):
            if colors[i] == -1:
                if not dfs(i, 0):
                    return False
        return True