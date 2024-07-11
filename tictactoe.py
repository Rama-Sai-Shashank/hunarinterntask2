def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 10)
def check_win(board, mark):
    for row in board:
        if all(s == mark for s in row):
            return True
    for col in range(3):
        if all(row[col] == mark for row in board):
            return True
    if all(board[i][i] == mark for i in range(3)) or all(board[i][2 - i] == mark for i in range(3)):
        return True
    return False
def check_draw(board):
    return all(all(cell != " " for cell in row) for row in board)
def player_move(board, mark):
    while True:
        try:
            move = int(input(f"Player {mark}, enter your move (1-9): ")) - 1
            if move < 0 or move >= 9:
                raise ValueError
            row, col = divmod(move, 3)
            if board[row][col] == " ":
                board[row][col] = mark
                break
            else:
                print("This space is already taken.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")
def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    while True:
        print_board(board)
        player_move(board, current_player)
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        if check_draw(board):
            print_board(board)
            print("The game is a draw!")
            break
        current_player = "O" if current_player == "X" else "X"
tic_tac_toe()
