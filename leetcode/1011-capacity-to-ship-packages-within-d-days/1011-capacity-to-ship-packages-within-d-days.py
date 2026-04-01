class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def validate(capacity):
            curr_sum = 0
            day_cnt = 1

            for weight in weights:
                curr_sum += weight
                if curr_sum > capacity:
                    day_cnt += 1
                    curr_sum = weight

                    if day_cnt > days:
                        return False
            
            return True
        
        low = max(weights)
        high = sum(weights)

        while low <= high:
            mid = (low + high) // 2
            if validate(mid):
                high = mid - 1
            else:
                low = mid + 1
        
        return low