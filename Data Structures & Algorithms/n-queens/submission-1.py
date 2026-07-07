class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.ans = []

        board = [["."]*n for _ in range(n)]

        def check_safety(r,c,board):
            # check same column above current row ( row - 1 )
            row = r - 1
            while row >= 0:
                if board[row][c] == 'Q':
                    return False # not safe
                else:
                    row -= 1
            # check diag left (also above current row)
            row = r - 1
            col = c - 1
            while row >= 0 and col >= 0:
                if board[row][col] == "Q":
                    return False
                else:
                    row -= 1
                    col -= 1

            # check diag right (also above current row)
            row = r -1 
            col = c+1
            while row >= 0 and col <= n-1:
                if board[row][col] == "Q":
                    return False
                else:
                    row -= 1
                    col += 1

            return True # safe

        def dfs(row):
            if row > n-1:
                temp = [''.join(row) for row in board]
                # print(temp)
                self.ans.append(temp)
                return
            for col in range(n):
                if check_safety(row,col,board):
                    board[row][col] = "Q"
                    dfs(row+1)
                    board[row][col] = "."
                    # dfs(row+1)

        dfs(0)
        return self.ans
