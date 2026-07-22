class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        n = len(arr)
        max_val = [[0] * n for _ in range(n)]
        for i in range(n):
            max_val[i][i] = arr[i]
            for j in range(i+1, n):
                max_val[i][j] = max(max_val[i][j-1], arr[j])
        
        dp = [[0] * n for _ in range(n)]
        
        for length in range(2, n+1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = float('inf')
                for k in range(i, j):
                    cost = dp[i][k] + dp[k+1][j] + max_val[i][k] * max_val[k+1][j]
                    dp[i][j] = min(dp[i][j], cost)
        
        return dp[0][n-1]