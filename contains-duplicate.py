class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        cnt_nums = Counter(nums)

        for num in cnt_nums:
            if cnt_nums[num] > 1:
                return True
        
        return False
