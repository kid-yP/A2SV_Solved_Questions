class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        n = len(nums)

        res = []
        for num in cnt:
            if cnt[num] > n / 3:
                res.append(num)

        
        return res
