class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        pal = [[False]*n for _ in range(n)]
        
        for r in range(n):
            for l in range(r+1):
                if s[l] == s[r] and (r-l <= 2 or pal[l+1][r-1]):
                    pal[l][r] = True
        
        dp = [0]*n
        
        for i in range(n):
            if pal[0][i]:
                dp[i] = 0
            else:
                dp[i] = i
                for j in range(1, i+1):
                    if pal[j][i]:
                        dp[i] = min(dp[i], dp[j-1] + 1)
        
        return dp[-1]