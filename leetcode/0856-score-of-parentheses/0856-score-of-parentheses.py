class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]

        for ch in s:
            if ch == '(':
                stack.append(0)
            else:
                temp = stack.pop()
                stack[-1] += max(2 * temp, 1)
        
        return stack[0]