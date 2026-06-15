class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def dfs(cur=[],seen=set()):
            if len(cur) == len(nums):
                ans.append(cur[:])
                return

            for num in nums:
                if num not in seen:
                    cur.append(num)
                    seen.add(num)
                    dfs(cur[:],seen)
                    # undo
                    seen.remove(num)
                    cur.pop()

                
        dfs([],set())

        return ans