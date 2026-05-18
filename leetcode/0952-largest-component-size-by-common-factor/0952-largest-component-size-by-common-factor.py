class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        n = max(nums)
        parent = {}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        for num in nums:
            parent[num] = num

        spf = [0] * (n+1)
        for i in range(2, n+1):
            if spf[i] == 0:
                for j in range(i, n+1, i):
                    if spf[j] == 0:
                        spf[j] = i

        factor_map = {}
        for num in nums:
            x = num
            while x > 1:
                p = spf[x]
                if p not in factor_map:
                    factor_map[p] = num
                else:
                    union(num, factor_map[p])
                while x % p == 0:
                    x //= p

        count = {}
        for num in nums:
            root = find(num)
            count[root] = count.get(root, 0) + 1

        return max(count.values())
