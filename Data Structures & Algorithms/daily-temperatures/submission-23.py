class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = [[temperatures[0], 0]]
        days = [0] * len(temperatures)
        for i in range(1, len(temperatures)):
            while s and s[-1][0] < temperatures[i]:
                _, pos = s.pop()
                days[pos] = i - pos
            s.append([temperatures[i], i])

        return days