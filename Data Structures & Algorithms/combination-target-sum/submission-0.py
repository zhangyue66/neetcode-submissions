class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []

        def dfs(i,cur=[]):
            if sum(cur) == target:
                ans.append(cur)
                return

            if sum(cur) > target:
                return 
            
            for j in range(i,len(nums)):
                cur.append(nums[j])
                dfs(j,cur[:])
                cur.pop()

        dfs (0,[])
        return ans
