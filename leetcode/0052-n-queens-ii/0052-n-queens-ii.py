class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()
        diag1 = set()
        diag2 = set()
        
        def backtrack(r):
            if r == n:
                return 1
            count = 0
            for c in range(n):
                if c in cols or (r - c) in diag1 or (r + c) in diag2:
                    continue
                cols.add(c)
                diag1.add(r - c)
                diag2.add(r + c)
                
                count += backtrack(r + 1)
                
                cols.remove(c)
                diag1.remove(r - c)
                diag2.remove(r + c)
            return count
        
        return backtrack(0)        