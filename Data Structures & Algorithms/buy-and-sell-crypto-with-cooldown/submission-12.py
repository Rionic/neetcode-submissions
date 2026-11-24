class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buying, selling, buying2 = 0, 0, 0

        for i in range(len(prices) -1, -1, -1):
            new_buying = max(buying, selling - prices[i])
            new_selling = max(selling, buying2 + prices[i])
            buying2 = buying
            selling = new_selling
            buying = new_buying
        
        return buying

        
        # dp = {}

        # def dfs(i, buying):
        #     if i >= len(prices):
        #         return 0

        #     if (i, buying) in dp:
        #         return dp[(i, buying)]

        #     best = 0
        #     if buying:
        #         best = max(
        #             dfs(i + 1, buying), 
        #             dfs(i + 1, not buying) - prices[i]
        #             )

        #     if not buying:
        #         best = max(
        #             dfs(i + 1, buying),
        #             dfs(i + 2, not buying) + prices[i]
        #         )

        #     dp[(i, buying)] = best
        #     return dp[(i, buying)]


        # return dfs(0, True)