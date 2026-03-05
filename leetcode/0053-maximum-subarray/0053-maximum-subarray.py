class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #PREFIX SUM
        prefix_sum = 0
        max_sum = float('-inf')

        for num in nums:
            prefix_sum += num
            max_sum = max(max_sum, prefix_sum)
            if prefix_sum < 0:
                prefix_sum = 0
        return max_sum