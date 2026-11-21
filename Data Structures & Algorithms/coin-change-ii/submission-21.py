class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1 # 1 way to sum to a=1 (take no coins)
        # dp[i] = # ways to sum up to that amount

        for c in coins:

            for a in range(1, amount):
                if c > a:
                    break
                dp[a] += dp[a - c]

        dp[amount]

        
        dp = {}

        def dfs(i, rem):
            if rem == 0:
                return 1
            if (i, rem) in dp:
                return dp[(i, rem)]
            ways = 0

            for j in range(i, len(coins)):
                if rem - coins[j] >= 0:
                    ways += dfs(j, rem - coins[j])

            dp[(i, rem)] =  ways    
            return dp[(i, rem)]

        return dfs(0, amount)