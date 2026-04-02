class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        self.res = []
        def backtrack(path):
            if len(path) == n:
                self.res.append("".join(path))
                return

            for ch in ['a', 'b', 'c']:
                if not path or path[-1] != ch:
                    path.append(ch)
                    backtrack(path)
                    path.pop()
                    
        backtrack([])
        
        if k > len(self.res):
            return ""
        
        return self.res[k-1]
