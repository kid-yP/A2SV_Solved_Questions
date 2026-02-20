class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        #sorting
        nums.sort()
        n = len(nums)
        threshold = n // 3
        res = []
        
        i = 0
        while i < n:
            j = i
            while j < n and nums[j] == nums[i]:
                j += 1
            if j - i > threshold:
                res.append(nums[i])
            i = j
        
        return res

        # cnt = Counter(nums)
        # n = len(nums)

        # res = []
        # for num in cnt:
        #     if cnt[num] > n / 3:
        #         res.append(num)

        
        # return res

        
