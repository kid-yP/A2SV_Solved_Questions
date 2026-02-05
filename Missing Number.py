class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        curr_sum = sum(nums)
        original_sum = 0
        #original_sum = (n*(n + 1)) // 2
        for i in range(n + 1):
           original_sum += i
        return original_sum - curr_sum
