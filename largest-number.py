class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        n = len(nums)

        for i in range(n):
            max_idx = i
            for j in range(i + 1, n):
                if nums[j] + nums[max_idx] > nums[max_idx] + nums[j]:
                    max_idx = j
            nums[i], nums[max_idx] = nums[max_idx], nums[i]

        result = ''.join(nums)

        return '0' if result[0] == '0' else result
