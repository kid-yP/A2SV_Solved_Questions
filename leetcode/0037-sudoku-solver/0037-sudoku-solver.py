class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        grid = collections.defaultdict(set)

        
        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    val = board[r][c]
                    cols[c].add(val)
                    rows[r].add(val)
                    grid[(r//3,c//3)].add(val)



        def dfs(r,c):
            if r == 9:
                return True

            if c == 9:
                return dfs(r+1,0)
            
            if board[r][c] != ".":
                return dfs(r,c+1)



            for k in range(1,10):
                val = str(k)

                if val in cols[c] or val in rows[r] or val in grid[(r//3,c//3)]:                    
                    continue

                board[r][c] = val
                cols[c].add(val)
                rows[r].add(val)
                grid[(r//3,c//3)].add(val)

                if dfs(r,c+1):
                    return True
                
                board[r][c] = "."
                cols[c].remove(val)
                rows[r].remove(val)
                grid[(r//3,c//3)].remove(val)

            return False



        dfs(0,0)