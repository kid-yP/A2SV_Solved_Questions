class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        rows, cols = len(matrix), len(matrix[0])
        heights = [0] * cols
        max_area = 0
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0
            max_area = max(max_area, self.largestRectangleArea(heights))
        return max_area

    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        n = len(heights)
        for i in range(n + 1):
            cur = heights[i] if i < n else 0
            while stack and heights[stack[-1]] > cur:
                h = heights[stack.pop()]
                left = stack[-1] if stack else -1
                width = i - left - 1
                max_area = max(max_area, h * width)
            stack.append(i)
        return max_area