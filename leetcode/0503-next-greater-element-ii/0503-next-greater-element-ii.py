class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums += nums
        stack = []
        mp = {}

        for i in range(n * 2):
            while stack and nums[i] > nums[stack[-1]]:
                mp[stack.pop()] = nums[i]

            stack.append(i)

        for i in range(len(stack)):
            mp[stack[i]] = -1

        return [mp[num] for num in range(len(nums) // 2)]