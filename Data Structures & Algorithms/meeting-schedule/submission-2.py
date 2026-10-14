"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x:x.start)
        a = []
        for interval in intervals:
            s, e = interval.start, interval.end
            if not a:
                a.append((s,e))
            if a[-1][1] <= s:
                a.append((s,e))
        return len(a) == len(intervals)