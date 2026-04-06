class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        radius = 0
        
        for house in houses:
            idx = bisect.bisect_left(heaters, house)
            
            left = house - heaters[idx-1] if idx > 0 else float('inf')
            
            right = heaters[idx] - house if idx < len(heaters) else float('inf')
            
            nearest = min(left, right)
            
            radius = max(radius, nearest)
    
        return radius