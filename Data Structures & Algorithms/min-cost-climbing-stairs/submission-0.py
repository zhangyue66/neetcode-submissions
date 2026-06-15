class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        dp = [0]*(n+1)
        dp[0] = 0
        dp[1] = 0
        
        for j in range(2,n+1):
            dp[j] = min(dp[j-1] + cost[j-1], dp[j-2]+ cost[j-2])

        return dp[-1]