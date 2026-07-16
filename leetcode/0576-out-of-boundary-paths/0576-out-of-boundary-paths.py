class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9 + 7
        from functools import lru_cache
        
        @lru_cache(None)
        def dfs(moves_left, r, c):
            if r < 0 or r >= m or c < 0 or c >= n:
                return 1
            if moves_left == 0:
                return 0
            
            total = 0
            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                total += dfs(moves_left - 1, r + dr, c + dc)
            
            return total % MOD
        
        return dfs(maxMove, startRow, startColumn)