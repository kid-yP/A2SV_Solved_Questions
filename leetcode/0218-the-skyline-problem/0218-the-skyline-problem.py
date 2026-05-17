class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        edges = []
        for l, r, h in buildings:
            edges.append((l, -h, r))
            edges.append((r, 0, 0))
        
        edges.sort()
        
        result = []
        heap = [(0, float("inf"))]
        prev_height = 0
        
        for x, neg_h, r in edges:
            if neg_h < 0:
                heapq.heappush(heap, (neg_h, r))
            else:
                while heap and heap[0][1] <= x:
                    heapq.heappop(heap)
            
            curr_height = -heap[0][0]
            if curr_height != prev_height:
                result.append([x, curr_height])
                prev_height = curr_height
        
        return result