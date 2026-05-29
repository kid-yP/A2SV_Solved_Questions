class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        
        def rob_linear(houses):
            prev, curr = 0, 0
            for money in houses:
                prev, curr = curr, max(curr, prev + money)
            return curr
        
        case1 = rob_linear(nums[:-1])
        case2 = rob_linear(nums[1:])
        
        return max(case1, case2)