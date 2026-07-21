class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans = float('inf')

        for num in nums:
            ans = min(ans,num)
        return ans 