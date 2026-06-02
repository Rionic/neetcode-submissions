class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 0, 1

        for i in range(1, n+1):
            three = one + two
            one = two
            two = three

        return two