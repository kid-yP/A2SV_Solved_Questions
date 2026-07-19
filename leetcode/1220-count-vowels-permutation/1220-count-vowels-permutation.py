class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10**9 + 7
        
        a = e = i = o = u = 1
        
        for _ in range(1, n):
            new_a = (e + i + u) % MOD
            new_e = (a + i) % MOD
            new_i = (e + o) % MOD
            new_o = i % MOD
            new_u = (i + o) % MOD
            
            a, e, i, o, u = new_a, new_e, new_i, new_o, new_u
        
        return (a + e + i + o + u) % MOD