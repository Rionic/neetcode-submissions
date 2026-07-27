class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('+inf')] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):

            for coin in coins:
                if coin > amount:
                    break
                dp[a] = min(dp[a - coin] + 1, dp[a])

        if dp[-1] == float('inf'):
            return -1
        return dp[-1]
                
