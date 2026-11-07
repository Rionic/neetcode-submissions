class Solution:
    def numSquares(self, n: int) -> int:
        
        # dp[i] = (1 + dp[n - square], dp[i])

        dp = [0] + [n] * n
        for i in range(1, n + 1):
            j = 1
            while j**2 <= i:
                dp[i] = min(dp[i], 1 + dp[i - j**2])
                j += 1
        return dp[-1]