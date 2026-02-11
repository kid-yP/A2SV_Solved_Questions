class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        return "".join(chars * cnt for chars, cnt in sorted(freq.items(), key=lambda x: x[1], reverse = True))
