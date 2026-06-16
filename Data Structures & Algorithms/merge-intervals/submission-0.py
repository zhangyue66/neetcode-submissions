class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals

        intervals.sort(key=lambda x:x[0])

        ans = []

        for interval in intervals:
            if not ans:
                ans.append(interval)
            else:
                if interval[0] <= ans[-1][1]:
                    if interval[1] > ans[-1][1]:
                        ans[-1][1] = interval[1]
                else:
                    ans.append(interval)

        return ans