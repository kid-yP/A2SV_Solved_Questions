class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #Dictionary
        n = len(temperatures)
        stack = []
        mp = {}

        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                prev_day = stack.pop()
                mp[prev_day] = i - prev_day
            stack.append(i)

        for i in stack:
            mp[i] = 0

        return [mp[i] for i in range(n)]
        #Prefix sum

        # stack = []
        # n = len(temperatures)
        # prefix_sum = [0] * n

        # for i, temp in enumerate(temperatures):
        #     while stack and temperatures[i] > temperatures[stack[-1]]:
        #         prev = stack.pop()
        #         prefix_sum[prev] = i - prev
        #     stack.append(i)
        
        # return prefix_sum