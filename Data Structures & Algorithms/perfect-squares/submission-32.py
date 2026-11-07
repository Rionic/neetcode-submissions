class Solution:
    def numSquares(self, n: int) -> int:
        
        # dp[i] = (1 + dp[n - square], dp[i])

        squares = [i**2 for i in range(1, math.floor(math.sqrt(n)) + 1)]
        dp = [n] * (n + 1)
        dp[0] = 0
        # n = 13
        # [0, 1, 4, 9]
        # dp = [0, 1, i, i]
        for i in range(1, n + 1):
            
            for square in squares:
                if square <= i:
                    dp[i] = min(dp[i], 1 + dp[i - square])
        return dp[-1]