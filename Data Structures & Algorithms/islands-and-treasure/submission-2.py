class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions =[[-1,0],[1,0],[0,-1],[0,1]]
        rows,cols =len(grid),len(grid[0])
        
        def bfs(r,c,step):
            queue = deque([(r,c,step)])
            visited = [[False]*cols  for j in range(rows)]
            
            while queue:
                r,c,step = queue.popleft()
                visited[r][c] = True

                if grid[r][c] == 0:
                    return step

                for dr,dc in directions:
                    if 0<=dr+r<=rows-1 and 0<=dc+c<=cols-1 and visited[dr+r][dc+c] == False and grid[dr+r][dc+c] != -1:
                        
                        queue.append((dr+r,dc+c,step+1))
                        visited[dr+r][dc+c] =True
                        

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] ==2147483647:
                    grid[i][j] = bfs(i,j,0)

                

