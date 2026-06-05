class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        if n == 1:
            return [0]

        stack = []
        ans = [0] * n
        for i,t in enumerate(temperatures):
            if not stack:
                stack.append((i,t))
            else:
                if stack[-1] and stack[-1][1] < t:
                    while stack and stack[-1][1] < t:
                        index,temp = stack.pop()
                        ans[index] = i - index
                    stack.append((i,t))
                elif stack[-1] and stack[-1][1] >= t:
                    stack.append((i,t))

        return ans
                

