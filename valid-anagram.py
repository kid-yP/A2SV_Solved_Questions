class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        x = list(sorted(s))
        y = list(sorted(t))
        if x == y:
            return True
        else:
            return False
