class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles) # eating rates from [1...max]
        res = r

        while l <= r:
            m = (l + r)//2
            time = 0
            for pile in piles:
                time += math.ceil(pile/m)

            if time > h: # we need a higher rate
                l = m + 1
            else: # potential answer
                res = min(m, res)
                r = m - 1
        return res


