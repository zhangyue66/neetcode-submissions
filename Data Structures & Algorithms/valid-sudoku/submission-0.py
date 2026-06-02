class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # check row
        for row in range(9):
            seen = set()
            for col in range(9):
                if board[row][col] == '.':
                    continue
                if board[row][col] in seen:
                    return False
                else:
                    seen.add(board[row][col])

        # check column
        for col in range(9):
            seen = set()
            for row in range(9):
                if board[row][col] == '.':
                    continue
                if board[row][col] in seen:
                    return False
                else:
                    seen.add(board[row][col])
        
        # check 3x3
        for box_r in range(0,9,3):
            for box_c in range(0,9,3):
                seen = set()

                for r in range(box_r,box_r+3):
                    for c in range(box_c,box_c+3):
                        if board[r][c] == '.':
                            continue
                        if board[r][c] in seen:
                            return False
                        else:
                            seen.add(board[r][c])
        return True