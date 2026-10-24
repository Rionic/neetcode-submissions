class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        s = []
        result = [0] * len(temperatures)
        # (i, t)
        for i, t in enumerate(temperatures):
            
            while s and s[-1][1] < t:
                j, temp = s.pop()
                result[j] = i - j
            s.append((i, t))

        return result
            