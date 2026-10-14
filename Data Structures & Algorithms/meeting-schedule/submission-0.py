"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        ans = []
        for interval in intervals:
            s, e = interval.start, interval.end
            if not ans or ans[-1][1] <= s:
                ans.append([s,e])
        return len(ans) == len(intervals)
