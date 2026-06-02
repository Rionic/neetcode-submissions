class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # [[1,2],[3,5],[4,8],[8,10]]
        # [4,8]
        if not intervals:
            return [newInterval]
        i = 0
        while i < len(intervals) and intervals[i][0] < newInterval[0]:
            i += 1
        intervals.insert(i, newInterval)
        new = []

        for i, iv in enumerate(intervals):
            if new and new[-1][1] >= iv[0]:
                new[-1][1] = max(new[-1][1], iv[1])
            else:
                new.append(iv)

        return new