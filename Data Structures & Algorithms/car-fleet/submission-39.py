class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # if not speed: return 0
        s = []

        for i in range(len(position)):
            s.append([position[i],
                        speed[i],
                        (target-position[i])/speed[i]])
        s = sorted(s, key=lambda x: x[0])
        fleets = 1

        car = s.pop()
        while s:
            if s[-1][2] > car[2]: # New fleet formed
                car = s.pop()
                fleets += 1
            else: # Collision. tte remains the same
                s.pop()

        return fleets





