class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        for i in range(len(prices)):
            if i == 0:
                # no previous date to buy
                ans = max(0,ans)
            else:
                for j in range(i):
                    ans = max(ans, prices[i] - prices[j])
        return ans
