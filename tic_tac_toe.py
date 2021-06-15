def main():
    # '_' is a common way to write loop in python when we dont have to use iterator, basically its a throwaway value
    board = [['_' for _ in range(3)] for _ in range(3)]
    is_x = True
    game_over = False
    while not game_over:
        print_board(board)
        try:
            user_input = input_conversion(select_square())
            place_piece(user_input,is_x,board)
        except ValueError:
            print("Sorry, please select a square 1-9 that is unoccupied")
            continue
        game_over = who_won(board) or is_draw(board)
        is_x = not is_x
        
#function to print the board
def print_board(board):
    #using list comprehension it can also slow down the program
    [print(row) for row in board]
    # for row in board:
    #     print(row)
#function to convert number to position on board
def input_conversion(user_input):
    #subtracting 1 so the range is 0-8 to use floor division and modulo
    user_input -= 1
    # returning tuple
    return (user_input // 3, user_input % 3)
# function to place the letter x or o
def place_piece(user_input,is_x, board):
    i,j = user_input
    if board[i][j] == '_':
        board[i][j] = "X" if is_x else "O"
    else:
        raise ValueError

# getting user input
def select_square():
    user_input = int(input("Select a square (1-9): "))
    #chained conditions are faster because middle value only need to be evaluated once and are considered more pythonic
    if not 1 <= user_input <=9:
        raise ValueError
    return user_input
# function to check for a draw
def is_draw(board):
    for row in board:
        for item in row:
            if item == "_":
                return False
    print_board(print)
    print("It's a tie! No more moves left.")
    return True 
def who_won(board):
    winner = None
    for i in range(3):
        #horizontal
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != '_':
            winner = board[i][0]
            break
        #vertical
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != '_':
            winner = board[0][i]
            break
    #diagonal
    if board[1][1] != '_':
        if (board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]):
            winner = board[1][1]
    if winner is not None:
        print_board(board)
        print(f"{winner} is the winner!")
        return True
    return False

if __name__ == "__main__":
    main()