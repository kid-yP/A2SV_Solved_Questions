class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            self.p = [[0]]
            return

        k, s = len(matrix), len(matrix[0])
        self.p = [[0] * (s + 1) for _ in range(k + 1)]

        for i in range(1, k + 1):
            for j in range(1, s + 1):
                self.p[i][j] = (matrix[i - 1][j - 1]
                                + self.p[i][j - 1]
                                + self.p[i - 1][j]
                                - self.p[i - 1][j - 1])

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (self.p[row2 + 1][col2 + 1]
                - self.p[row1][col2 + 1]
                - self.p[row2 + 1][col1]
                + self.p[row1][col1])