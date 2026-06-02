"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        ints = sorted(intervals, key=lambda x: x.start)

        for i in range(len(ints) - 1):

            if ints[i].end > ints[i + 1].start:
                return False

        return True

