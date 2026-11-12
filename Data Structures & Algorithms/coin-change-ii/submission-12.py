class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = {}

        def dfs(i, remaining):
            if remaining == 0:
                return 1
            if remaining < 0 or i == len(coins):
                return 0

            if (i, remaining) in dp:
                return dp[(i, remaining)]

            dp[(i, remaining)] = dfs(i, remaining - coins[i]) + dfs(i + 1, remaining)

            return dp[(i, remaining)]

        return dfs(0, amount)