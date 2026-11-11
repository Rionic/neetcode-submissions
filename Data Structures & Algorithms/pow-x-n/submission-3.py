class Solution:
    def myPow(self, x: float, n: int) -> float:
        # helper(3, 0) -> 1
        # helper(3, 1) -> 3
        # helper(3, 2) -> 9
        # helper(3, 4) -> 81
        # helper(3, 8) -> 81 * 81
        def helper(x, n):
            if x == 0: return 0
            if n == 0: return 1
            
            res = helper(x, n // 2)

            return res * res if n % 2 == 0 else x * res * res


        res = helper(x, abs(n))
        
        return res if n >= 0 else 1 / res

        # 3^10 = 3^5^2
        # 3  9    27
        # 11 1001 11011
        
        # 2^5 = 2^4 + sum(2^3 2^2 2^1 2^0 + 1) 
        # 2^n = sum(2^n-1..2^0 1)