class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        dp = {}

        def dfs(i, buying):
            if i >= len(prices):
                return 0

            if (i, buying) in dp:
                return dp[(i, buying)]

            best = 0
            if buying:
                best = max(
                    dfs(i + 1, buying), 
                    dfs(i + 1, not buying) - prices[i]
                    )

            if not buying:
                best = max(
                    dfs(i + 1, buying),
                    dfs(i + 2, not buying) + prices[i]
                )

            dp[(i, buying)] = best
            return dp[(i, buying)]


        return dfs(0, True)