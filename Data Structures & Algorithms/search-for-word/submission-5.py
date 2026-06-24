class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows,cols = len(board),len(board[0])
        n = len(word)
        visited = set()
        directions = [[-1,0],[1,0],[0,-1],[0,1]]

        def dfs(index,r,c):
            if r < 0 or r>=rows or c<0 or c>=cols or (r,c) in visited or board[r][c] != word[index]:
                return False

            if index==n-1 and board[r][c] == word[index]:
                return True
                
            if index > len(word):
                return False

            if 0<=r<rows and 0<=c<cols and board[r][c] == word[index] and (r,c) not in visited:
                visited.add((r,c))
                for dr,dc in directions:
                    if 0<=dr+r<rows and 0<=dc+c<cols:
                        if dfs(index+1,r+dr,c+dc):
                            return True
                visited.remove((r,c))
            return False

        found = False
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    found = dfs(index=0,r=i,c=j)
                    if found:
                        return found
        return found
            