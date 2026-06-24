class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # use dp (bottom up )
        n = len(nums)
        dp = [False] * n
        dp[-1] = True

        for i in range(n-2,-1,-1):
            jump_distance = min(nums[i]+i,n)
            for j in range(i+1,jump_distance+1):
                if dp[j] is True:
                    dp[i] = True
                    break
        return dp[0]
