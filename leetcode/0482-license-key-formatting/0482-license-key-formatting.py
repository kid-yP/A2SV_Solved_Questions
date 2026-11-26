class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        clean = s.replace('-', '').upper()
        if not clean:
            return ""
        first_len = len(clean) % k
        if first_len == 0:
            first_len = k
        res = [clean[:first_len]]
        for i in range(first_len, len(clean), k):
            res.append(clean[i:i+k])
        return '-'.join(res)