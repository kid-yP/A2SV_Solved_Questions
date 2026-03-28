class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        self.res = float('inf')
        
        def backtrack(i, distribution):
            if i == len(cookies):
                self.res = min(self.res, max(distribution))
                return
            
            for child in range(k):
                distribution[child] += cookies[i]
                backtrack(i + 1, distribution)
                distribution[child] -= cookies[i]
                
                if distribution[child] == 0:
                    break
        
        backtrack(0, [0] * k)
        return self.res