class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        self.ans = []
        nums = [i for i in range(1,n+1)]

        def dfs(cur = [],index=0):
            if len(cur) == k:
                self.ans.append(cur[:])
                return
            if index >= len(nums):
                return

            cur.append(nums[index])
            dfs(cur[:],index+1)
            cur.pop()
            dfs(cur[:],index+1)

            
        dfs([],0)
        return self.ans
