class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # citations.sort(reverse = True)
        # h = 0

        # for idx, cnt in enumerate(citations):
        #     if cnt >= idx + 1:
        #         h = idx + 1
        #     else:
        #         break
        
        # return h

        # Counting sort
        n = len(citations)
        count = [0] * (n + 1)

        for cit in citations:
            if cit >= n:
                count[n] += 1
            else:
                count[cit] += 1
        
        total = 0
        for i in range(n, -1, -1):
            total += count[i]
            if total >= i:
                return i
        return 0
