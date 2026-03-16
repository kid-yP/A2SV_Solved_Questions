class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n = len(nums)
        op = 0

        for i in range(n - 2, -1, -1):
            if nums[i] > nums[i + 1]:
                k = (nums[i] + nums[i + 1] - 1) // nums[i + 1]
                op += k - 1
                nums[i] = nums[i] // k
        
        return op