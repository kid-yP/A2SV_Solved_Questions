class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = [(et, pt, i) for i, (et, pt) in enumerate(tasks)]
        tasks.sort()
        
        result = []
        heap = []
        time = 0
        i = 0
        n = len(tasks)
        
        while i < n or heap:
            while i < n and tasks[i][0] <= time:
                et, pt, idx = tasks[i]
                heapq.heappush(heap, (pt, idx))
                i += 1
            
            if heap:
                pt, idx = heapq.heappop(heap)
                time += pt
                result.append(idx)
            else:
                time = tasks[i][0]
        
        return result