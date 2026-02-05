class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_count = Counter(chars)
        res = 0
            
        for word in words:
            words_char_count = Counter(word)
            for i in range(len(word)):
                if words_char_count[word[i]] > chars_count[word[i]]:
                    break
            else:
                res += len(word)
        return res
