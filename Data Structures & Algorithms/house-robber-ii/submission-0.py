class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return nums[0]
        
        dp = [0]*n

        # rob first house
        dp[0] = nums[0]
        dp[1] = max(dp[0],nums[1])

        for i in range(2,n-1):
            dp[i] = max(dp[i-1],nums[i]+dp[i-2])
        print(dp)


        dp2=[0]*n

        #dont rob first house
        dp2[1] = nums[1]

        for i in range(2,n):
            dp2[i] = max(dp2[i-1],nums[i]+dp2[i-2])
        print(dp2)

        return max(max(dp),max(dp2))
