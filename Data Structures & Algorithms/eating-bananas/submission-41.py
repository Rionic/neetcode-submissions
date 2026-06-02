class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
    # Input: piles = [25,10,23,4], h = 4
    # Speeds: [1,2,3,4,...25]
    # m = 13, 19, 22, 23, 24, 25
    # time = 6, 6, 6, 6,  5,  4
        def eat(speed):
            time = 0
            for pile in piles:
                time += math.ceil(pile/speed)
            return time


        l , r = 1, max(piles)
        res = r # Max possible speed, which always works
        while l <= r:
            m = (l + r) // 2
            print('eating with rate', m)
            time = eat(m)
            print('time taken', time)
            if time <= h:
                res = m
                r = m - 1
            elif time > h: # We are too slow, use faster rate
                l = m + 1
        return res
        



