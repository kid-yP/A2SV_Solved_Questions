class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def validate(k):
            hrs = 0
            for pile in piles:
                hrs += ceil(pile / k)
                if hrs > h:
                    return False

            return True
        
        low = 1
        high = max(piles)
        while low <= high:
            k = (low + high) // 2
            if validate(k):
                high = k - 1
            else:
                low = k + 1
        
        return low