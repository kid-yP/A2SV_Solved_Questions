class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def subarrayCount(nums: List[int], k: int) -> int:
            count = defaultdict(int)
            num_count = 0
            left = 0
            total = 0

            for right in range(len(nums)):
                if count[nums[right]] == 0:
                    num_count += 1
                count[nums[right]] += 1
                
                while num_count > k:
                    count[nums[left]] -= 1
                    if count[nums[left]] == 0:
                        num_count -= 1
                    left += 1

                total += right - left + 1
            return total

        return subarrayCount(nums, k) - subarrayCount(nums, k - 1)
