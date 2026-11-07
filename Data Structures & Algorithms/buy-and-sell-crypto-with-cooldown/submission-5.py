class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = {} # (i, buy/sell): profit

        def dfs(i, state):
            if i >= len(prices):
                return 0

            if (i, state) in best:
                return best[(i, state)]

            if state == 'buy':
                profit_wait = dfs(i + 1, 'buy')
                profit_sell = dfs(i + 1, 'sell') - prices[i]
            elif state == 'sell':
                profit_wait = dfs(i + 1, 'sell')
                profit_sell = dfs(i + 2, 'buy') + prices[i]
            
            best[(i, state)] = max(profit_sell, profit_wait)
            return best[(i, state)]

        # prices = [1, 3, 4, 0, 4]
        #          -1  3     0  4
        # p = -1
        return dfs(0, 'buy')