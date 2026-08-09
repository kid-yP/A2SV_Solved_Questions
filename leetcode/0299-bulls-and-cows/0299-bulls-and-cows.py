class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        countS = [0] * 10
        countG = [0] * 10

        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                countS[ord(s) - 48] += 1
                countG[ord(g) - 48] += 1

        cows = sum(min(countS[i], countG[i]) for i in range(10))
        return f"{bulls}A{cows}B"