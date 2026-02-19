class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse = True)
        n = (len(piles) // 3)
        count = 0

        for i in range(1, 2 * n, 2):
            count += piles[i]
        
        return count
