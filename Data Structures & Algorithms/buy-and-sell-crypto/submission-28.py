class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        max_profit = 0
        # [10,1,5,6,7,0,9]
        for r in range(len(prices)):
            profit = prices[r] - prices[l]
            if  profit > max_profit:
                max_profit = profit
            elif prices[r] <= prices[l]:
                l = r

        return max_profit
