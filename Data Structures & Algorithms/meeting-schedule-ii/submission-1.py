"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) <= 1:
            return len(intervals)
        intervals.sort(key=lambda x:x.start)
        
        import heapq
        heap = [intervals[0].end]
        heapq.heapify(heap)

        for i in range(1,len(intervals)):
            if heap:
                if heap[0]> intervals[i].start:
                    heapq.heappush(heap,intervals[i].end)
                else:
                    heapq.heappop(heap)
                    heapq.heappush(heap,intervals[i].end)
            else:
                heapq.heappush(heap,intervals[i].end)

        return len(heap)

