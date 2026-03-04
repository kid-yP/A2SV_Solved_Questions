class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        prefix_mod = {0: -1}
        curr_sum = 0

        if k == 0:
            for i in range(n - 1):
                if nums[i] == 0 and nums[i + 1] == 0:
                    return True
            return False

        for i in range(n):
            curr_sum += nums[i]
            remainder = curr_sum % k

            if remainder in prefix_mod:
                if i - prefix_mod[remainder] >= 2:
                    return True
            else:
                prefix_mod[remainder] = i

        return False
