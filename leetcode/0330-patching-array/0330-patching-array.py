class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        l = len(nums)
        miss, patches, i = 1, 0, 0
        while miss <= n:
            if i < l and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                miss += miss
                patches += 1

        return patches