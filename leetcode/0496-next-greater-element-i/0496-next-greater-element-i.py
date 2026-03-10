class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        mp = {}

        for num in nums2:
            while stack and num > stack[-1]:
                mp[stack.pop()] = num
            stack.append(num)

        for num in stack:
            mp[num] = -1

        return [mp[num] for num in nums1]