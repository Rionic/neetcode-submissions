class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)
        def eat(piles, h, rate):
            for p in piles:
                h -= math.ceil(p/rate)
                if h < 0:
                    return False
            return True
        
        while lo <= hi:
            m = (lo + hi)//2
            if eat(piles, h, m):
                hi = m - 1
            else:
                lo = m + 1
        return lo
