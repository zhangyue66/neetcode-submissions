class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.ans = []

        def dfs(cur=[],index=0):
            if index >= len(nums):
                return
            if sum(cur[:]) > target:
                return
            if sum(cur[:]) == target:
                self.ans.append(cur[:])
                return 



            for j in range(index,len(nums)):
                cur.append(nums[j])
                dfs(cur[:],j)
                cur.pop()
                # dfs(cur[:],index+1)

        dfs([],0)

        return self.ans