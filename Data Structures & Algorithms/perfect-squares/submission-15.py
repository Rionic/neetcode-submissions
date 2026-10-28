class Solution:
    def numSquares(self, n: int) -> int:
        # All possible combinations. n = 12
        # 1 + 1 + ... + 1 -> 12
        # 4 + 1 + ... + 1 -> 9
        # 4 + 4 + 1 + 1 + 1 + 1 -> 6
        # 4 + 4 + 4 -> 3
        # 9 + 1 + 1 + 1 -> 4
        # 9 + 4  X  Too high!

        # Choosing 4, leave us with 8 to solve. -> 1 + dp[8]
        # dp[i] could represent ps up to i
        # [0, 1, 2, 3, 1, 2, 3, 4, 2, 1]
        # Might be like coin change were we pick a coin (square), subtract from total, and try each coin (ps) up to that total

        dp = [float('inf') for num in range(n + 1)]
        dp[0] = 0
        perf_squares = [x for x in range(1, n + 1) if x == math.floor(math.sqrt(x))**2]
        # Consider using isqrt(x) for large x
        for num in range(1, n + 1):

            for square in perf_squares:
                if square > num:
                    break
                dp[num] = min(dp[num], 1 + dp[num - square])
        return dp[-1]
