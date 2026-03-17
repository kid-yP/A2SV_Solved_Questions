class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        def winnerIndex(n: int, k: int) -> int:
            if n == 0:
                return 0
            
            return (winnerIndex(n - 1, k) + k) % n

        return winnerIndex(n, k) + 1