class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        days = [0] * len(temperatures)
        s = []
        for i in range(0, len(temperatures)):
            while s and s[-1][0] < temperatures[i]:
                _, pos = s.pop()
                days[pos] = i - pos
            s.append([temperatures[i], i])

        return days