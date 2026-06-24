class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float('inf')]*n
        dp[-1] = 0

        for i in range(n-2,-1,-1):
            jump_step = min(nums[i]+i+1,n)
            for j in range(i+1,jump_step):
                dp[i] = min(dp[j]+1,dp[i])

        print(dp)
        return dp[0]