"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = sorted([pair.start for pair in intervals])
        ends = sorted([pair.end for pair in intervals])
        s, e = 0, 0
        max_days = 0
        cur_days = 0

        while s < len(starts):
            if ends[e] > starts[s]:
                s += 1 
                cur_days += 1
            else:
                e += 1
                cur_days -= 1
            max_days = max(max_days, cur_days)
        
        return max_days
            
