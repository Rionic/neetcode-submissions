class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        dp = {}

        def dfs(i, buying):
            if i == len(prices):
                return 0

            if (i, buying) in dp:
                return dp[(i, buying)]            

            if buying:
                wait = dfs(i + 1, buying)
                act = dfs(i + 1, not buying) - prices[i]
            else:
                wait = dfs(i + 1, buying)
                act = dfs(i + 1, not buying) + prices[i]

            best = max(wait, act)

            dp[(i, buying)] = best

            return dp[(i, buying)]

        
        return dfs(0, True)