class Solution:
    def findValidPair(self, s: str) -> str:
        cnt = Counter(s)

        for i in range(len(s) - 1):
            a, b = s[i], s[i + 1]
            if a!=b:
                if cnt[a] == int(a) and cnt[b] == int(b):
                    return a + b
        
        return ""
