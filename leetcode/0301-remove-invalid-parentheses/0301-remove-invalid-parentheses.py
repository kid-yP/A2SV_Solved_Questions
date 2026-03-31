class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        res = set()

        left_remove, right_remove = 0, 0
        for ch in s:
            if ch == "(":
                left_remove += 1
            elif ch == ")":
                if left_remove > 0:
                    left_remove -= 1
                else:
                    right_remove += 1

        def isValid(string):
            count = 0
            for ch in string:
                if ch == "(":
                    count += 1
                elif ch == ")":
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        def dfs(index, path, left_count, right_count, left_remove, right_remove):
            if index == len(s):
                if left_remove == 0 and right_remove == 0 and isValid(path):
                    res.add(path)
                return

            ch = s[index]

            if ch == "(" and left_remove > 0:
                dfs(index + 1, path, left_count, right_count, left_remove - 1, right_remove)
            if ch == ")" and right_remove > 0:
                dfs(index + 1, path, left_count, right_count, left_remove, right_remove - 1)

            if ch not in "()":
                dfs(index + 1, path + ch, left_count, right_count, left_remove, right_remove)
            elif ch == "(":
                dfs(index + 1, path + ch, left_count + 1, right_count, left_remove, right_remove)
            elif ch == ")" and left_count > right_count:
                dfs(index + 1, path + ch, left_count, right_count + 1, left_remove, right_remove)

        dfs(0, "", 0, 0, left_remove, right_remove)
        return list(res)
