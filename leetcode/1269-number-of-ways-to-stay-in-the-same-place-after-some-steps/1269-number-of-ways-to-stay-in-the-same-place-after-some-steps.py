class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10**9 + 7
        limit = min(arrLen, steps + 1)
        
        dp = [0] * limit
        dp[0] = 1
        
        for _ in range(steps):
            new_dp = [0] * limit
            for pos in range(limit):
                if dp[pos] == 0:
                    continue
                new_dp[pos] = (new_dp[pos] + dp[pos]) % MOD
                if pos - 1 >= 0:
                    new_dp[pos - 1] = (new_dp[pos - 1] + dp[pos]) % MOD
                if pos + 1 < limit:
                    new_dp[pos + 1] = (new_dp[pos + 1] + dp[pos]) % MOD
            dp = new_dp
        
        return dp[0] % MOD