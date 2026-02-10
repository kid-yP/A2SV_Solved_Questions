class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum = sum(x for x in nums if x % 2 == 0) 
        res = []
        
        for val, idx in queries: 
            old_val = nums[idx] 
        
            if old_val % 2 == 0: 
                even_sum -= old_val 
            
            nums[idx] += val 
            new_val = nums[idx]
            
            if new_val % 2 == 0: 
                even_sum += new_val
            res.append(even_sum) 
            
        return res
