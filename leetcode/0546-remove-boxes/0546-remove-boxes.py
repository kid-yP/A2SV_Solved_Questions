class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        n = len(boxes)

        @lru_cache(None)
        def dp(l, r, k):
            if l > r:
                return 0

            while l < r and boxes[l] == boxes[l+1]:
                l += 1
                k += 1
            res = dp(l+1, r, 0) + (k+1)**2

            for i in range(l+1, r+1):
                if boxes[i] == boxes[l]:
                    res = max(res, dp(l+1, i-1, 0) + dp(i, r, k+1))
            return res

        return dp(0, n-1, 0)