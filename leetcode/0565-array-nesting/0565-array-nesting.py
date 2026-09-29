class Solution:
    def arrayNesting(self, nums: list[int]) -> int:
        n = len(nums)
        visited = [False] * n
        max_len = 0
        for i in range(n):
            if not visited[i]:
                count = 0
                cur = i
                while not visited[cur]:
                    visited[cur] = True
                    cur = nums[cur]
                    count += 1
                max_len = max(max_len, count)
        return max_len