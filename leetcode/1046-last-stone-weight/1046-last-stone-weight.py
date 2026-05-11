class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-s for s in stones]
        heapq.heapify(max_heap)
        
        while len(max_heap) > 1:
            y = -heapq.heappop(max_heap)  # heaviest
            x = -heapq.heappop(max_heap)  # second heaviest
            if y != x:
                heapq.heappush(max_heap, -(y - x))
        
        return -max_heap[0] if max_heap else 0