class Solution:
    def nearestPalindromic(self, n: str) -> str:
        L = len(n)
        num = int(n)
        candidates = set()
        candidates.add(10**(L - 1) - 1)
        candidates.add(10**L + 1)
        
        half = n[:(L + 1) // 2]
        half_int = int(half)
        
        for i in [-1, 0, 1]:
            prefix = str(half_int + i)
            if L % 2 == 0:
                pal = prefix + prefix[::-1]
            else:
                pal = prefix + prefix[:-1][::-1]
            candidates.add(int(pal))
        
        candidates.discard(num)
        
        min_diff = float('inf')
        ans = None
        for cand in candidates:
            diff = abs(cand - num)
            if diff < min_diff or (diff == min_diff and cand < ans):
                min_diff = diff
                ans = cand
        
        return str(ans)