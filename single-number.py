class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nat = Counter(nums)

        kid = []
        for num in nums:
            if nat[num] == 1:
                kid.append(num)
        
        return kid[0]
