class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxp = -1

        for r in range(len(prices)):
            if prices[r] - prices[l] > maxp:
                maxp = prices[r] - prices[l]
            if prices[r] < prices[l]:
                l = r
                
        return maxp