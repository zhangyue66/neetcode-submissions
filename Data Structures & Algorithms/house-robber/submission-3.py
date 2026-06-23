class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return nums[0]
        n = len(nums)
        dp =[0]*n
        dp[0] = nums[0]
        dp[1] = max(nums[1],dp[0])

        for i in range(2,n):
            dp[i] = max(dp[i-1],dp[i-2]+nums[i])

        print(dp)

        return max(dp[-1],dp[-2])