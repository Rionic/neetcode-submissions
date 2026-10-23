class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        max_profit = 0
        for r in range(len(prices)):
            profit = prices[r] - prices[l]
            max_profit = max(profit, max_profit)
            if profit < 0:
                l = r

        return max_profit
