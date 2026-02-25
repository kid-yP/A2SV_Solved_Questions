class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        freq = {ch: i for i, ch in enumerate(s)}
        output = []
        left, right = 0, 0

        for i, ch in enumerate(s):
            right = max(right, freq[ch])
            if i == right:
                output.append(right - left + 1)
                left = i + 1
        return output
