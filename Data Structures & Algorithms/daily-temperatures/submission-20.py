class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = [[temperatures[0], 0]]
        days = [0] * len(temperatures)
        # i = 6
        # [30,38,30,36,35,40,28]
        # [(40, 5) (28, 6)]
        # [1, 4, 1, 2, 1, 0, 0]
        for i in range(1, len(temperatures)):
            print(s, days)
            while s != [] and s[-1][0] < temperatures[i]: # Warmer day found
                _, pos = s.pop()
                print('pop', _, pos)
                days[pos] = i - pos
            s.append([temperatures[i], i])

        return days