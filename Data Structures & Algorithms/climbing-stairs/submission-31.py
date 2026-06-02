class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 2

        for i in range(2, n):
            three = one + two
            one = two
            two = three

        return two if n!=1 else one