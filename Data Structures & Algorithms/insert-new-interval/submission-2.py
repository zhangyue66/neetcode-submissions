class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        ans = []

        found = False
        for interval in intervals:
            if interval[0] < newInterval[0]:
                ans.append(interval)
            elif interval[0] >= newInterval[0] and not found:
                ans.append(newInterval)
                ans.append(interval)
                found = True
            else:
                ans.append(interval)

        if not found:
            ans.append(newInterval)

        stack = []
        for interval in ans:
            if not stack:
                stack.append(interval)
            else:
                if interval[0] <= stack[-1][1]:
                    cur = stack.pop()
                    start = cur[0]
                    end = max(cur[1],interval[0],interval[1])
                    stack.append([start,end])
                else:
                    stack.append(interval)
        return list(stack)
