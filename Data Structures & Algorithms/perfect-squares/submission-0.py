class Solution:
    def numSquares(self, n: int) -> int:
        # n = 12 -> 4 + 4 + 4
        # [1, 4, 9]
        # splitNum(12, 0) -> 9, splitNum(3, 1)
        # splitNum(3, 1) -> 1, splitNum(2, 2)
        # splitNum(2, 2) -> 1 splitNum(1, 3)
        # splitNum(1, 3) -> 1, base (9+1+1+1) = 4 splits


        self.dp = {}

        def splitNum(n):
            if n == 0:
                return 0
            if n in self.dp: # we've seen this split before. WE KNOW THE OPTIMAL FOR THIS 
                return self.dp[n]

            best = float('inf')
            square = math.floor(math.sqrt(n))
            while square > 0:
                splits = splitNum(n - square**2) + 1
                best = min(splits, best)
                square -= 1
            self.dp[n] = best
            return best

        return splitNum(n)