class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        moves = [(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]
        
        dp = [[[0.0]*n for _ in range(n)] for _ in range(k+1)]
        dp[0][row][column] = 1.0
        
        for step in range(1, k+1):
            for i in range(n):
                for j in range(n):
                    for dx, dy in moves:
                        x, y = i+dx, j+dy
                        if 0 <= x < n and 0 <= y < n:
                            dp[step][i][j] += dp[step-1][x][y] / 8.0
        
        return sum(dp[k][i][j] for i in range(n) for j in range(n))