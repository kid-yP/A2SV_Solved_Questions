class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        keep = 0
        swap = 1

        for i in range(1, n):
            new_keep = float('inf')
            new_swap = float('inf')

            if nums1[i-1] < nums1[i] and nums2[i-1] < nums2[i]:
                new_keep = min(new_keep, keep)

            if nums2[i-1] < nums1[i] and nums1[i-1] < nums2[i]:
                new_keep = min(new_keep, swap)

            if nums1[i-1] < nums2[i] and nums2[i-1] < nums1[i]:
                new_swap = min(new_swap, keep + 1)

            if nums2[i-1] < nums2[i] and nums1[i-1] < nums1[i]:
                new_swap = min(new_swap, swap + 1)

            keep, swap = new_keep, new_swap

        return min(keep, swap)