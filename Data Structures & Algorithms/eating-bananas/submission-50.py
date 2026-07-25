class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minRate, maxRate = 1, max(piles)
        best = max(piles)
        def eat(piles, h, rate):
            for p in piles:
                h -= math.ceil(p/rate)
                if h < 0:
                    return False
            return True
        
        while minRate <= maxRate:
            m = math.ceil((minRate + maxRate)//2)
            if eat(piles, h, m):
                maxRate = m - 1
                best = min(m, best)
            else:
                minRate = m + 1
        return best
