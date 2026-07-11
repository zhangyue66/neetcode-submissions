class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        m,n = len(grid),len(grid[0])
        island_count = 0
        directions =[[-1,0],[1,0],[0,-1],[0,1]]

        def dfs(r,c):
            if grid[r][c] == "0":
                return 

            
            grid[r][c] = '0'

            for dr,dc in directions:
                if 0<=r+dr<m and 0<=c+dc<n:
                    dfs(dr+r,dc+c)


        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i,j)
                    island_count += 1

        return island_count