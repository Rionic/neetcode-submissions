class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        i = 1
        res = [intervals[0]]

        while i < len(intervals):
            start2, end2 = intervals[i][0], intervals[i][1]
            start1, end1 = res[-1][0], res[-1][1]

            if start2 <= end1:
                res[-1][1] = max(end1, end2)
            else:
                res.append([start2, end2])
            
            i += 1

        return res

