class Solution:

    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        steps = [0] * n
        steps[0], steps[1] = 1, 2
        res = 0
        for i in range(n-2):
            steps[i + 2] = steps[i] + steps[i + 1]
        return steps[-1]