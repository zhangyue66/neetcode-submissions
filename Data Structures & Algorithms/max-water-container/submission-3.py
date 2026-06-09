class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # two pointer with bog O(n)
        i,j = 0,len(heights)-1
        ans = -float('inf')
        while i < j:
            area = (j-i) * min(heights[i],heights[j])
            ans = max(ans,area)
            if heights[i] <= heights[j]:
                i += 1
            else:
                j -= 1
        return ans