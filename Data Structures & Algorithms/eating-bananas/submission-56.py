class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)
        def eat(rate):
            hours = 0
            for p in piles:
                hours += math.ceil(p/rate)
            return hours <= h
        
        while lo <= hi:
            m = (lo + hi)//2
            if eat(m):
                hi = m - 1
            else:
                lo = m + 1
        return lo
