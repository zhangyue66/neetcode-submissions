class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions =[[-1,0],[1,0],[0,-1],[0,1]]
        visited = set()
        rows,cols =len(grid),len(grid[0])

        def dfs(r,c):
            if r < 0 or r >rows-1 or c < 0 or c > cols-1 or (r,c) in visited or grid[r][c] == 0:
                return 0

            visited.add((r,c))

            area = 1
            for dr,dc in directions:
                area += dfs(dr+r,dc+c)

            return area
            

        ans = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    ans = max(ans,dfs(i,j))
        return ans

