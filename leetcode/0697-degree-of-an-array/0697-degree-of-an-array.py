class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        first = {}
        last = {}
        count = defaultdict(int)
        
        for i, num in enumerate(nums):
            if num not in first:
                first[num] = i
            last[num] = i
            count[num] += 1
        
        degree = max(count.values())
        ans = len(nums)
        
        for num in count:
            if count[num] == degree:
                ans = min(ans, last[num] - first[num] + 1)
        
        return ans