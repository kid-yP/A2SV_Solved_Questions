class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        people.sort()
        count = 0
        left, right = 0, n - 1
        
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
            right -= 1
            count += 1
            
        return count
