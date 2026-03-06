class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remainder_cnt = {0: 1}
        p_sum = 0
        result = 0

        for num in nums:
            p_sum += num

            remainder = p_sum % k

            if remainder < 0:
                remainder += k
            
            if remainder in remainder_cnt:
                result += remainder_cnt[remainder]

            if remainder in remainder_cnt:
                remainder_cnt[remainder] += 1
            else:
                remainder_cnt[remainder] = 1

        return result