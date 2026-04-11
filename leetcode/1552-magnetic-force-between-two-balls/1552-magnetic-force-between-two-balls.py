class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
    
        def can_place(force):
            count = 1
            last_pos = position[0]
            for pos in position[1:]:
                if pos - last_pos >= force:
                    count += 1
                    last_pos = pos
                    if count >= m:
                        return True
            return False
        
        low, high = 1, position[-1] - position[0]
        result = 0
        
        while low <= high:
            mid = (low + high) // 2
            if can_place(mid):
                result = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return result