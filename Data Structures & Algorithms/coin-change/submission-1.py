class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        visited = {}

        ans = float('inf')

        def dfs(cur_amount,coin_count):
            nonlocal ans

            if cur_amount == 0:
                ans= min(ans,coin_count)
                return

            if cur_amount < 0:
                return

            if cur_amount in visited and visited[cur_amount] <= coin_count:
                return
            
            visited[cur_amount] = coin_count

            for coin in coins:
                
                dfs(cur_amount-coin,coin_count+1)

        dfs(amount,0)

        return ans if ans != float('inf') else -1

