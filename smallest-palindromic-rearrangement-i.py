class Solution:
    def smallestPalindrome(self, s: str) -> str:
        freq = Counter(s)
        left, middle = [], ""
        
        for ch in sorted(freq.keys()):
            count = freq[ch]
            left.append(ch * (count // 2))
            if count % 2 == 1:
                middle = ch
        
        left_str = "".join(left)
        return left_str + middle + left_str[::-1]
