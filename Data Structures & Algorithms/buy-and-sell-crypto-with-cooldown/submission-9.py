class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = {} 

        def dfs(i, buying):
            if i >= len(prices):
                return 0

            if (i, buying) in best:
                return best[(i, buying)]

            if buying:
                wait = dfs(i + 1, buying)
                sell = dfs(i + 1, not buying) - prices[i]
            else:
                wait = dfs(i + 1, buying)
                sell = dfs(i + 2, not buying) + prices[i]
            
            best[(i, buying)] = max(sell, wait)
            return best[(i, buying)]

        return dfs(0, True)