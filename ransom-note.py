class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq1 = Counter(ransomNote)
        freq2 = Counter(magazine)

        for ch, cnt in freq1.items():
            if cnt > freq2[ch]:
                return False
        
        return True
