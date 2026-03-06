class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        modulo = 10**9 + 7
        n = len(nums)

        p = [0] * (n + 1)

        for start, end in requests:
            p[start] += 1
            if end + 1 < n:
                p[end + 1] -= 1
        
        for i in range(1, n):
            p[i] += p[i - 1]
        p = p[:-1]

        nums.sort(reverse=True)
        p.sort(reverse=True)

        tot = 0
        for i in range(n):
            tot = (tot + nums[i] * p[i]) % modulo
        
        return tot