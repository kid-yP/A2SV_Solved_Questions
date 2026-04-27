class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        
        m, n = len(heights), len(heights[0])
        
        def bfs(starts):
            visited = set(starts)
            queue = deque(starts)
            while queue:
                r, c = queue.popleft()
                for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                        if heights[nr][nc] >= heights[r][c]:
                            visited.add((nr, nc))
                            queue.append((nr, nc))
            return visited
        
        pacific_starts = [(0, c) for c in range(n)] + [(r, 0) for r in range(m)]
        atlantic_starts = [(m-1, c) for c in range(n)] + [(r, n-1) for r in range(m)]
        
        pacific_reach = bfs(pacific_starts)
        atlantic_reach = bfs(atlantic_starts)
        
        result = list(pacific_reach & atlantic_reach)
        return result