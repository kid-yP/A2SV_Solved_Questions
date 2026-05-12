class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
    
        heap = [(-freq, word) for word, freq in count.items()]
        heapq.heapify(heap)
        
        result = [heapq.heappop(heap)[1] for _ in range(k)]
        return result