"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x.start)
        heap = []
        for interval in intervals:
            s, e = interval.start, interval.end
            if not heap:
                heapq.heappush(heap, e)
            else:
                if s >= heap[0]:
                    heapq.heappop(heap)
                heapq.heappush(heap, e)
        return len(heap)