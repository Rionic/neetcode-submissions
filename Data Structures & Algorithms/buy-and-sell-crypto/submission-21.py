class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r, maxp = 0, 1, 0

        while r < len(prices):
            diff = prices[r] - prices[l]
            if diff > maxp:
                maxp = diff
            if prices[r] < prices[l]:
                l = r
            r += 1

        return maxp