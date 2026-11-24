class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Remove the interval which overlaps with the greatest number of intervals. 
        intervals.sort()
        res = [intervals[0]]
        removals = 0
        for i in range(1, len(intervals)):
            if res[-1][1] <= intervals[i][0]:
                res.append(intervals[i])
            else:
                if intervals[i][1] < res[-1][1]:
                    res[-1] = intervals[i] 
                removals += 1

        return removals
        