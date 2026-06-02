class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        max_profit = 0
        # [10,1,5,6,7,0,9]
        while r < len(prices):
            profit = prices[r] - prices[l]
            if  profit > max_profit:
                max_profit = profit
                r += 1
            elif prices[r] <= prices[l]:
                l = r
                r += 1
            else:
                r += 1

        return max_profit
