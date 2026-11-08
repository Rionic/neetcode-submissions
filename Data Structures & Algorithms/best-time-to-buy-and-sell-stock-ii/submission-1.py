class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        cash, hold = 0, -prices[0]
        dp = [0] * len(prices)

        for p in prices[1:]:
            # Prev day we had cash: wait, or buy
            new_cash = max(cash, hold + p)
            # Prev day we had stock: wait, or sell
            new_hold = max(hold, cash - p)
            cash = new_cash
            hold = new_hold

        return max(cash, hold)