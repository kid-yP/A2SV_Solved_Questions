class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr_perm):
            if len(curr_perm) == len(nums):
                ans.append(curr_perm[:])
                return
            
            for num in nums:
                if num in curr_perm:
                    continue

                curr_perm.append(num)
                backtrack(curr_perm)
                curr_perm.pop()
        
        ans = []
        backtrack([])
        return ans