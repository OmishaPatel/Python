
def isValidSudoku(board):
    row, col, block = set(), set(), set()
    for i in range(9):
        for j in range(9):
            if (board[i][j] != '.'):
                r_key = (i, board[i][j])
                c_key = (j, board[i][j])
                b_key =( i//3, j//3, board[i][j])
                
                if(r_key in row) or(c_key in col) or(b_key in block):
                    return False
                row.add(r_key)
                col.add(c_key)
                block.add(b_key)
    return True


board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(isValidSudoku(board))