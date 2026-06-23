class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        self.ans = []

        def dfs(cur=[],index=0):
            if index >= len(nums):
                self.ans.append(cur[:])
                return
                

            cur.append(nums[index])
            dfs(cur[:],index+1)

            cur.pop()
            dfs(cur[:],index+1)

        dfs([],0)
        return self.ans

            