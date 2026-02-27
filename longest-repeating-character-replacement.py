class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        max_count = 0

        left = 0
        for right in range(len(s)):
            count[ord(s[right]) - ord('A')] += 1
            max_count = max(max_count, count[ord(s[right]) - ord('A')])

            if (right - left + 1) - max_count > k:
                count[ord(s[left]) - ord('A')] -= 1
                left += 1

        return len(s) - left 
