class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        res = []
        total = 0
        
        for l , r in costs:
            res.append([l - r, l , r])
        res.sort()
        
        for i in range(n // 2):
            total += res[i][1]
        
        for i in range(n // 2 , n):
            total += res[i][2]
        
        return total 