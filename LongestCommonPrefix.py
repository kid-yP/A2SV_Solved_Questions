class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for i in range(len(strs)):
            for j in range(min(len(prefix), len(strs[i]))):
                if strs[i][j] != prefix[j]:
                    prefix = prefix[:j]
                    break
            else:
                if len(strs[i]) < len(prefix):
                    prefix = strs[i]
        return prefix
