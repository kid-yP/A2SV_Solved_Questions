class Solution:
    def replaceWords(self, dictionary: list[str], sentence: str) -> str:
        roots = set(dictionary)
        max_len = max(map(len, dictionary))
        res = []
        for word in sentence.split():
            for i in range(1, min(len(word), max_len) + 1):
                prefix = word[:i]
                if prefix in roots:
                    word = prefix
                    break
            res.append(word)
        return " ".join(res)