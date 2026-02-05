class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        count = defaultdict(int)

        for i in range(len(nums)):
            count[nums[i]] += 1
        
        for c in count:
            if count[c] > 1:
                res.append(c)

        return res
