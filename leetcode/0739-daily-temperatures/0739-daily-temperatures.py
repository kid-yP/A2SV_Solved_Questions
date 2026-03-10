class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        prefix_sum = [0] * n

        for i, temp in enumerate(temperatures):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev = stack.pop()
                prefix_sum[prev] = i - prev
            stack.append(i)
        
        return prefix_sum