class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq1 = Counter(sorted(nums1))
        freq2 = Counter(sorted(nums2))
        res = []
        for num, cnt in freq1.items():
            if num in freq2:
                res.append(num)
        return res
