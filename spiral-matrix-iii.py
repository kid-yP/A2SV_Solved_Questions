class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        result = []
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        steps = 1
        r, c = rStart, cStart
        result.append([r, c])
        
        while len(result) < rows * cols:
            for d in range(4):
                dr, dc = directions[d]
                for _ in range(steps):
                    r += dr
                    c += dc
                    if 0 <= r < rows and 0 <= c < cols:
                        result.append([r, c])
                if d % 2 == 1:
                    steps += 1
        return result
