class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        if m == 0:
            return 0

        i = 0
        while i <= n - m:
            j = 0
            while j < m and haystack[i + j] == needle[j]:
                j += 1
            if m == j:
                return i
            i += 1
        return -1
