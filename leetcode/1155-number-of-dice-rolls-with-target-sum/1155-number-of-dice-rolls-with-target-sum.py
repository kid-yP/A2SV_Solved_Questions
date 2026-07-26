class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9 + 7

        if target > n * k:
            return 0

        dp = [0] * (target + 1)
        dp[0] = 1

        for _ in range(n):
            new_dp = [0] * (target + 1)
            for s in range(target + 1):
                if dp[s] == 0:
                    continue
                for face in range(1, k + 1):
                    if s + face <= target:
                        new_dp[s + face] = (new_dp[s + face] + dp[s]) % MOD
            dp = new_dp

        return dp[target]