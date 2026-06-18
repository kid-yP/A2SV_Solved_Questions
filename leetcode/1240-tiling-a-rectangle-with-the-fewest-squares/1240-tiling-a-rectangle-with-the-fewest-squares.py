class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        self.ans = max(n, m)

        grid = [[0]*m for _ in range(n)]

        def dfs(count):
            if count >= self.ans:
                return

            for i in range(n):
                for j in range(m):
                    if grid[i][j] == 0:
                        x, y = i, j
                        break
                else:
                    continue
                break
            else:
                self.ans = min(self.ans, count)
                return

            max_len = min(n-x, m-y)
            while max_len > 0:
                can_place = True
                for i in range(x, x+max_len):
                    for j in range(y, y+max_len):
                        if grid[i][j] == 1:
                            can_place = False
                            break
                    if not can_place:
                        break

                if can_place:
                    for i in range(x, x+max_len):
                        for j in range(y, y+max_len):
                            grid[i][j] = 1
                    dfs(count+1)
                    for i in range(x, x+max_len):
                        for j in range(y, y+max_len):
                            grid[i][j] = 0
                max_len -= 1

        dfs(0)
        return self.ans
