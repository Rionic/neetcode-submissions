class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        top = intervals[0]
        removals = 0
        for i in range(1, len(intervals)):
            if top[1] <= intervals[i][0]:
                top = intervals[i]
            else:
                if intervals[i][1] < top[1]:
                    top = intervals[i] 
                removals += 1

        return removals
        