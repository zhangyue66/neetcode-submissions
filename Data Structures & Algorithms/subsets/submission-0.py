class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        ans = []

        
        def dfs(i,nums,subset=[]):
            if i > len(nums) -1:
                ans.append(subset[:])
                return
            
            subset.append(nums[i])
            dfs(i+1,nums,subset[:])

            subset.remove(nums[i])
            dfs(i+1,nums,subset[:])

        dfs(0,nums,[])

        return ans
