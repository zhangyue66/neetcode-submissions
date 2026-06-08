class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(r,c):
            from collections import deque
            queue = deque()
            visited.add((r,c))
            queue.append((r,c))
            while queue:
                r, c = queue.popleft()
                # check up,down,left,right nodes
                directions = [[-1,0],[1,0],[0,-1],[0,1]]
                for dr,dc in directions:
                    if r+dr in range(rows) and c+dc in range(cols) and (r+dr,c+dc) not in visited and grid[r+dr][c+dc] == "1":
                        queue.append((r+dr,c+dc))
                        visited.add((r+dr,c+dc))



        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    islands += 1
        return islands
