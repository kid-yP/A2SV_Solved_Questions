class Solution:
    def createSortedArray(self, instructions):
        MOD = 10**9 + 7
        
        max_val = max(instructions)
        tree = [0] * (max_val + 1)

        def update(i):
            while i <= max_val:
                tree[i] += 1
                i += i & -i

        def query(i):
            s = 0
            while i > 0:
                s += tree[i]
                i -= i & -i
            return s

        cost = 0
        
        for i, x in enumerate(instructions):
            less = query(x - 1)
            greater = i - query(x)
            cost = (cost + min(less, greater)) % MOD
            update(x)

        return cost