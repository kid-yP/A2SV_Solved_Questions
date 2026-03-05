class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        p_cnt = {0: 1}
        p_sum = 0
        res = 0

        for num in nums:
            p_sum += num
            
            if p_sum - goal in p_cnt:
                res += p_cnt[p_sum - goal]
            
            if p_sum in p_cnt:
                p_cnt[p_sum] += 1
            else:
                p_cnt[p_sum] = 1

        return res
