class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        
        n = len(nums)
        mid = n // 2
        
        if n % 2 == 1:
            return float(nums[mid])
        else:
            return (nums[mid - 1] + nums[mid]) / 2.0
