class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        row = len(grid)
        col = len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j] < 0:
                    count += 1
                
        return count
