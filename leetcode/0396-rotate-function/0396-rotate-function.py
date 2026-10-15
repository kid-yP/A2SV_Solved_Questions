class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        f = sum(i * nums[i] for i in range(n))
        ans = f

        for k in range(1, n):
            f += total - n * nums[n - k]
            if f > ans:
                ans = f

        return ans