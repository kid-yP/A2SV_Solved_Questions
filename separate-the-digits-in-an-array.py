class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            num = str(num)
            for i in num:
                ans.append(int(i))
        
        return ans
