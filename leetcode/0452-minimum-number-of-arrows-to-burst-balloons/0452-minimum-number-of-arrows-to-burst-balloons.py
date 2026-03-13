class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        count = 1   
        points.sort(key = lambda x :x[1])
        latest_end = points[0][1]

        for i in range(1, len(points)):
            if points[i][0] > latest_end:
                count += 1
                latest_end = points[i][1]
            
        return count