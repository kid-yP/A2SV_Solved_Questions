class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        graph = [[] for _ in range(n)]
        
        for i in range(n):
            x1, y1, r1 = bombs[i]
            for j in range(n):
                if i == j: continue
                x2, y2, _ = bombs[j]
                if (x1 - x2)**2 + (y1 - y2)**2 <= r1**2:
                    graph[i].append(j)
        
        def bfs(start):
            visited = set([start])
            queue = deque([start])
            while queue:
                node = queue.popleft()
                for nei in graph[node]:
                    if nei not in visited:
                        visited.add(nei)
                        queue.append(nei)
            return len(visited)
        
        return max(bfs(i) for i in range(n))