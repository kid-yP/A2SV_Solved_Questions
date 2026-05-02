class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        
        mn, mx = min(nums), max(nums)
        if mn == mx:
            return 0
        
        n = len(nums)
        gap = max(1, (mx - mn) // (n - 1))
        bucket_count = (mx - mn) // gap + 1
        
        bucket_min = [float('inf')] * bucket_count
        bucket_max = [float('-inf')] * bucket_count
        used = [False] * bucket_count
        
        for num in nums:
            idx = (num - mn) // gap
            bucket_min[idx] = min(bucket_min[idx], num)
            bucket_max[idx] = max(bucket_max[idx], num)
            used[idx] = True
        
        prev_max = mn
        max_gap = 0
        for i in range(bucket_count):
            if not used[i]:
                continue
            max_gap = max(max_gap, bucket_min[i] - prev_max)
            prev_max = bucket_max[i]
        
        return max_gap
