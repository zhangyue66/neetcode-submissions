from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        n = len(word)
        visited = set()
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def dfs(index, r, c):
            # Base Case: Successfully matched every character up to index n
            if index == n:
                return True

            # Validity Gate: Check boundaries, character matching, and visited state safely
            if 0 <= r < rows and 0 <= c < cols and board[r][c] == word[index] and (r, c) not in visited:
                visited.add((r, c))
                
                # Let the next frame evaluate if the coordinates are valid or out-of-bounds
                for dr, dc in directions:
                    if dfs(index + 1, r + dr, c + dc):
                        return True
                        
                visited.remove((r, c))
                # return False
                
            return False

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if dfs(0, i, j):
                        return True
        return False