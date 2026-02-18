class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        #counting sort
        count = [0] * 101

        for num in nums:
            count[num] += 1
        
        for i in range(1, 101):
            count[i] += count[i - 1]

        res = []
        for num in nums:
            res.append(count[num - 1] if num > 0 else 0)
        return res
        
        #selection sort
        # n = len(nums)
        # count = 0
        # res = []

        # for i in range(n):
        #     count = 0
        #     for j in range(n):
        #         if nums[i] > nums[j]:
        #             count += 1
        #     res.append(count)

        # return res
