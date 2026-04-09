class Solution:
    def findMin(self, nums: List[int]) -> int:
        # return min(nums)

        #Binary Search
        n = len(nums)
        left, right = 0, n - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        return nums[left]