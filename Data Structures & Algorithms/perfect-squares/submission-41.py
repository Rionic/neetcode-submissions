class Solution:
    def numSquares(self, n: int) -> int:
        
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for num in range(1, n + 1):
            j = 1
            while j ** 2 <= num:
                dp[num] = min(dp[num], 1 + dp[num - j**2])

                j += 1
        return dp[n]