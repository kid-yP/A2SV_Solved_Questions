class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq_s = Counter(s)
        res = []

        for ch in order:
            if ch in freq_s:
                res.append(ch * freq_s[ch])
                del freq_s[ch]
        
        for ch, cnt in freq_s.items():
            res.append(ch * cnt)
        
        return "".join(res)
