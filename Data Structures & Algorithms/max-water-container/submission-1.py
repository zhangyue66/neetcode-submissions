class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = -float('inf')

        # use brute force - o(n) big O
        n = len(heights)
        for i in range(n-1):
            for j in range(i+1,n):
                square = (j-i)*(min(heights[i], heights[j]))
                ans = max(ans,square)
        return ans