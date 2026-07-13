class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        # Your exact ocean boundary setup (fixed variable shadowing)
        pacific = set((0, j) for j in range(n))
        for i in range(m):
            pacific.add((i, 0))

        atlantic = set((m - 1, j) for j in range(n))
        for i in range(m):
            atlantic.add((i, n - 1))

        # Tracks if the CURRENT connected downward component hits the oceans
        self.can_p = False
        self.can_a = False

        def dfs(r, c, visited):
            # If this cell is part of an ocean shore, flag it!
            if (r, c) in pacific:
                self.can_p = True
            if (r, c) in atlantic:
                self.can_a = True

            visited.add((r, c))

            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                    # Water flows downhill or flat (>=)
                    if heights[r][c] >= heights[nr][nc]:
                        dfs(nr, nc, visited)

        ans = []
        # Loop through every cell exactly like your original structure
        for r in range(m):
            for c in range(n):
                self.can_p = False
                self.can_a = False
                
                # Find EVERY cell water can branch out to from here
                dfs(r, c, set())
                
                # If the network reached both oceans, it's a valid starting point!
                if self.can_p and self.can_a:
                    ans.append([r, c])

        return ans