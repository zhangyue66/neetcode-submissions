class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()

        def dfs(i,cur=[]):
            if sum(cur) == target:
                ans.append(cur[:])
                return

            if sum(cur) > target or i == len(candidates):
                return

            for j in range(i,len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                cur.append(candidates[j])
                dfs(j+1,cur[:])
                cur.pop()

        dfs(0,[])

        return ans