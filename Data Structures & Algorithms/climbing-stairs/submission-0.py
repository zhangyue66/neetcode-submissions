class Solution:
    def climbStairs(self, n: int) -> int:
        if n  <= 2:
            return n

        nums =[0]*(n+1)
        nums[1] = 1
        nums[2] = 2
        for i in range(3,n+1):
            nums[i] = nums[i-1] + nums[i-2]
        return nums[-1]
        