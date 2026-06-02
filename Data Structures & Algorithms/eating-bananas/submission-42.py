class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def eat(speed):
            time = 0
            for pile in piles:
                time += math.ceil(pile/speed)
            return time

        l , r = 1, max(piles)
        res = r # Max possible speed, which always works
        while l <= r:
            m = (l + r) // 2
            time = eat(m)
            if time <= h:
                res = m
                r = m - 1
            elif time > h: # We are too slow, use faster rate
                l = m + 1
        return res
        



