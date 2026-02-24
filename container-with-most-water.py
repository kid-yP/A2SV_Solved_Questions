class Solution:
    def maxArea(self, height: List[int]) -> int: 
        n = len(height)
        left = 0
        right = n - 1
        area = 0

        while left < right:
            current_area = min(height[left], height[right]) * (right - left)
            area = max(area, current_area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return area
