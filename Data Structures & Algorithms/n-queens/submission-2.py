class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # use hash map to enhance

        board = [['.']*n for _ in range(n)]
        self.ans = []
        
        cols,diag_left,diag_right=set(),set(),set()


        def dfs(row):
            if row == n:
                self.ans.append([''.join(r) for r in board])
                return

            for col in range(n):
                if col in cols or row+col in diag_right or row-col in diag_left:
                    continue
                
                board[row][col] = "Q"
                cols.add(col)
                diag_right.add(row+col)
                diag_left.add(row-col)

                dfs(row+1)

                cols.remove(col)
                diag_right.remove(row+col)
                diag_left.remove(row-col)

                #back tracking
                board[row][col] = "."

        dfs(0)
        return self.ans

