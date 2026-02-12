class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        x = len(nums) // 2
        for dom, cnt in cnt.items():
            if cnt > x:
                dominant = dom
                tot_count = cnt
                break

        left = 0
        for i in range(len(nums) - 1):
            if nums[i] == dominant:
                left += 1
            left_size = i + 1
            right_size = len(nums) - left_size

            if left > left_size // 2 and (tot_count - left) > right_size // 2:
                return i
        return -1
        #This code is dedicated to Marel
