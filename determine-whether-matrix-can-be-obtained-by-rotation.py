class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rotate(mat):
            n = len(mat)

            for i in range(n):
                for j in range(i + 1, n):
                    mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
            
            for row in mat:
                row.reverse()

        for _ in range(4):
            if mat == target:
                return True
            rotate(mat)

        return False

        #[list(row) for row in zip(*mat[::-1])]
