class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        def findRight():
            left, right = 0, n - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right  

        def findLeft():
            left, right = 0, n - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left  

        left = findLeft()
        right = findRight()

        if left <= right:
            return [left, right]
        else:
            return [-1, -1]