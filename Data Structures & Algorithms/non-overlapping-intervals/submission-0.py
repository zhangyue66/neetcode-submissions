class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 1:
            return 0
        ans = 0
        intervals.sort()
        prevEnd = intervals[0][1]

        for i in range(1,len(intervals)):
            start,end = intervals[i]
            if prevEnd > start:
                ans += 1
                prevEnd = min(prevEnd, end)
            else:
                # no overlap
                prevEnd = end
        return ans