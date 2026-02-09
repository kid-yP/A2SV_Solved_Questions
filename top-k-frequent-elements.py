class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f_count = defaultdict(int)
        res = []

        for num in nums:
            f_count[num] += 1
        
        items = list(f_count.items())
        items.sort(key=lambda x: x[1], reverse=True)

        res = []
        for i in range(k):
            res.append(items[i][0])

        return res
