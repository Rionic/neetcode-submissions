class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        # dp = [0, 1, 2, 3, 4, 1, 2, 3, 4, 5,  1,  2, 3]
        for a in range(1, amount + 1):
            for c in coins: # [1, 5, 10]
                if c > a: break
                dp[a] = min(1 + dp[a - c], dp[a])

        return dp[-1] if dp[-1] != float("inf") else -1
