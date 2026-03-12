class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        min_i = nums[0]

        for j in range(1, len(nums)):

            while stack and nums[j] >= stack[-1][0]:
                stack.pop()

            if stack and nums[j] > stack[-1][1]:
                return True

            stack.append((nums[j], min_i))
            min_i = min(min_i, nums[j])

        return False