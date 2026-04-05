class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        memo = {}

        def dfs(start):
            if start in memo:
                return memo[start]
            if start == len(s):
                return [""]

            sentences = []
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in word_set:
                    for sub in dfs(end):
                        if sub:
                            sentences.append(word + " " + sub)
                        else:
                            sentences.append(word)
            memo[start] = sentences
            return sentences

        return dfs(0)