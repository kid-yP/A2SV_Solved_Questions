class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        count = (len(b) + len(a) - 1) // len(a)
        for k in (count, count + 1):
            if b in a * k:
                return k
        return -1