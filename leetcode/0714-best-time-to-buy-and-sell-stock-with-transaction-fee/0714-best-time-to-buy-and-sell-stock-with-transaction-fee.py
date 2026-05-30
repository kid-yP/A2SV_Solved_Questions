class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        hold, cash = -prices[0], 0
        
        for i in range(1, n):
            hold = max(hold, cash - prices[i])
            cash = max(cash, hold + prices[i] - fee)
        
        return cash