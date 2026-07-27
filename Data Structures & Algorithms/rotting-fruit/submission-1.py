class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return -1
        directions = [[1,0],[-1,0],[0,-1],[0,1]]
        ans = 0

        rows,cols = len(grid),len(grid[0])
        visited = set()
        queue = deque([])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))  # Start each rotten orange at minute 0

        while queue:
            r,c,ans = queue.popleft()
            visited.add((r,c))

            for dr,dc in directions:
                if 0<=r+dr<=rows-1 and 0<=c+dc<=cols-1 and (dr+r,dc+c) not in visited and grid[dr+r][dc+c] == 1:
                    grid[dr+r][dc+c] = 2
                    queue.append((dr+r,dc+c,ans+1))
                    # print(grid)

        #print(grid)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
        return ans