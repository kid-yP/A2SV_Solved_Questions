class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = [""] * len(s)
        for i, ch in enumerate(s):
            res[indices[i]] = ch

        return "".join(res)
