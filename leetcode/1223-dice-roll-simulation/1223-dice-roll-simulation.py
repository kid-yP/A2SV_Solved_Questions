class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        MOD = 10**9 + 7
        dp = [[[0]*(16) for _ in range(6)] for _ in range(n+1)]
        
        for face in range(6):
            dp[1][face][1] = 1
        
        for step in range(2, n+1):
            for face in range(6):
                for prevFace in range(6):
                    for count in range(1, rollMax[prevFace]+1):
                        if dp[step-1][prevFace][count] == 0:
                            continue
                        if face == prevFace:
                            if count < rollMax[face]:
                                dp[step][face][count+1] = (dp[step][face][count+1] + dp[step-1][face][count]) % MOD
                        else:
                            dp[step][face][1] = (dp[step][face][1] + dp[step-1][prevFace][count]) % MOD
        
        ans = 0
        for face in range(6):
            for count in range(1, rollMax[face]+1):
                ans = (ans + dp[n][face][count]) % MOD
        return ans