class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        freq = {0 : -1}
        
        p = 0
        if k == 0:
            for i in range(n - 1):
                if nums[i] == 0 and nums[i + 1] == 0:
                    return True
            return False

        for i in range(n):
            p += nums[i]
            remainder = p % k

            if remainder in freq:
                if i - freq[remainder] >= 2:
                    return True
            else:
                freq[remainder] = i

        return False