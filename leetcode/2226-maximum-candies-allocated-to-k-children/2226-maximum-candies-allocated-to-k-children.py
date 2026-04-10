class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        left, right = 1, max(candies)
        ans = 0

        while left <= right:
            mid = (left + right) // 2
            
            children = sum(pile // mid for pile in candies)

            if children >= k:
                left = mid + 1
            else:
                right = mid - 1
        
        return right