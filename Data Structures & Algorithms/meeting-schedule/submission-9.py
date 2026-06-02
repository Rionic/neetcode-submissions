"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        si = sorted(intervals, key=lambda x: x.start)
        
        for i in range(len(si)-1):
            if si[i].end > si[i+1].start:
                return False

        return True 
