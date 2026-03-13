class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_dq = deque()
        max_dq = deque()
        left = 0
        max_len = 0

        for right in range(len(nums)):
            while min_dq and nums[right] < nums[min_dq[-1]]:
                min_dq.pop()
            while max_dq and nums[right] > nums[max_dq[-1]]:
                max_dq.pop()

            min_dq.append(right)
            max_dq.append(right)

            while nums[max_dq[0]] - nums[min_dq[0]] > limit:
                left += 1
                if min_dq[0] < left:
                    min_dq.popleft()
                if max_dq[0] < left:
                    max_dq.popleft()

            max_len = max(max_len, right - left + 1)

        return max_len