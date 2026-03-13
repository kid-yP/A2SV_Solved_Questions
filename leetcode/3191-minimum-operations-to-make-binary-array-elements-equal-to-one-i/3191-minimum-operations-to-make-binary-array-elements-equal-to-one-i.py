class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        q = deque()
        operations = 0
        
        for i in range(n):
            while q and q[0] + 3 <= i:
                q.popleft()
            
            effective = nums[i] ^ (len(q) % 2)
            
            if effective == 0:
                if i + 2 >= n:
                    return -1
                q.append(i)
                operations += 1
        
        return operations