class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        target = total // k
        nums.sort(reverse=True)
        n = len(nums)
        if nums[0] > target:
            return False
        
        used = [False] * n
        
        def backtrack(start: int, curr_sum: int, subsets_done: int) -> bool:
            if subsets_done == k - 1:
                return True  # remaining elements must sum to target
            if curr_sum == target:
                return backtrack(0, 0, subsets_done + 1)
            
            for i in range(start, n):
                if used[i] or curr_sum + nums[i] > target:
                    continue
                # skip duplicates
                if i > 0 and not used[i-1] and nums[i] == nums[i-1]:
                    continue
                used[i] = True
                if backtrack(i + 1, curr_sum + nums[i], subsets_done):
                    return True
                used[i] = False
                # pruning: if curr_sum == 0, we couldn't fill the subset from this start
                if curr_sum == 0:
                    return False
            return False
        
        return backtrack(0, 0, 0)