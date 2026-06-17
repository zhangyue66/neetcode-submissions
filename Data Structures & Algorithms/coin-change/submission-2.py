class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp soulition - dp[7] = min(dp[6]+1,dp[3]+1,dp[2]+1)
        n = len(coins)
        dp = [float('inf')]*(amount+1)
        dp[0] = 0

        for i in range(1,amount+1):
            # i is the current amount
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i],1+dp[i-coin])

        print(dp)
        return dp[amount] if dp[amount] != float('inf') else -1