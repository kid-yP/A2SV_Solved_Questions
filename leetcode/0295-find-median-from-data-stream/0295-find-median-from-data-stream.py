class MedianFinder:        
    def __init__(self):
        self.low = []   # max-heap (store negatives)
        self.high = []  # min-heap

    def addNum(self, num: int) -> None:
        # Step 1: push into max-heap
        heapq.heappush(self.low, -num)
        
        # Step 2: balance by moving largest from low to high
        heapq.heappush(self.high, -heapq.heappop(self.low))
        
        # Step 3: ensure low has equal or more elements
        if len(self.high) > len(self.low):
            heapq.heappush(self.low, -heapq.heappop(self.high))

    def findMedian(self) -> float:
        if len(self.low) > len(self.high):
            return -self.low[0]
        else:
            return (-self.low[0] + self.high[0]) / 2.0

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()