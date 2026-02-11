class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        freq = Counter()

        for response in responses:
            unique_word = set(response)
            for word in unique_word:
                freq[word] += 1

        max_freq = max(freq.values())
        most_common = [word for word, count in freq.items() if count == max_freq]

        return min(most_common)
