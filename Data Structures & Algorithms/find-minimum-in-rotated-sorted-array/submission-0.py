class Solution:
    def findMin(self, nums: List[int]) -> int:
        # brute force
        ans = float('inf')
        for num in nums:
            ans = min(ans,num)
        return ans