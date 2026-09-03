class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def can_split(limit: int) -> bool:
            subarrays = 1
            current_sum = 0
            for num in nums:
                if num > limit:
                    return False
                if current_sum + num > limit:
                    subarrays += 1
                    current_sum = num
                else:
                    current_sum += num
            return subarrays <= k

        lo = max(nums)
        hi = sum(nums)
        
        while lo < hi:
            mid = (lo + hi) // 2
            if can_split(mid):
                hi = mid
            else:
                lo = mid + 1

        return lo