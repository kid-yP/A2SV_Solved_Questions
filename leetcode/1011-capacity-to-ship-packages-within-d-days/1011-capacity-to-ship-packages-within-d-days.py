class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShip(capacity):
            needed_days = 1
            current = 0
            for w in weights:
                if current + w > capacity:
                    needed_days += 1
                    current = 0
                current += w
            return needed_days <= days
        
        left, right = max(weights), sum(weights)
        
        while left < right:
            mid = (left + right) // 2
            if canShip(mid):
                right = mid
            else:
                left = mid + 1
        
        return left