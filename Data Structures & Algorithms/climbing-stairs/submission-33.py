class Solution:
    def climbStairs(self, n: int) -> int:
        
        one, two = 0, 1

        for i in range(n):
            three = one + two
            one = two
            two = three
        
        return two
