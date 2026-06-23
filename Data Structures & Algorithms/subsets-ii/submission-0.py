class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        self.ans = []

        def dfs(cur=[],index=0):
            if index >= len(nums):
                self.ans.append(cur[:])
                return

            cur.append(nums[index])

            dfs(cur[:],index+1)

            cur.pop()
            while index + 1 <= len(nums)-1 and nums[index] == nums[index+1]:
                index += 1
            dfs(cur[:],index+1)

        dfs([],0)

        return self.ans