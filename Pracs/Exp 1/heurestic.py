import random

def print_board(board):
    for row in board:
        print(' '.join(row))

def check_winner(board):
    # Check rows, columns, and diagonals for a winner
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '-':  # Rows
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != '-':  # Columns
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != '-':  # Diagonal 1
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != '-':  # Diagonal 2
        return board[0][2]
    # Check for draw
    if all(board[i][j] != '-' for i in range(3) for j in range(3)):
        return 'Draw'
    return None

def heuristic_move(board):
    # Try to win
    for i in range(3):
        for j in range(3):
            if board[i][j] == '-':
                board[i][j] = 'X'
                if check_winner(board) == 'X':
                    return (i, j)
                board[i][j] = '-'

    # Block opponent
    for i in range(3):
        for j in range(3):
            if board[i][j] == '-':
                board[i][j] = 'O'
                if check_winner(board) == 'O':
                    return (i, j)
                board[i][j] = '-'

    # Forking strategy
    if board[1][1] == '-':
        return (1, 1)

    # Center Strategy
    if board[0][0] == '-' or board[0][2] == '-' or board[2][0] == '-' or board[2][2] == '-':
        corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
        random.shuffle(corners)
        for corner in corners:
            if board[corner[0]][corner[1]] == '-':
                return corner

    # Random move
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == '-':
            return (row, col)

def user_move(board):
    while True:
        try:
            row = int(input("Enter row (0, 1, 2): "))
            col = int(input("Enter column (0, 1, 2): "))
            if board[row][col] == '-':
                board[row][col] = 'O'
                break
            else:
                print("Cell already occupied. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def tic_tac_toe():
    board = [['-' for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic Tac Toe!")
    print_board(board)
    while True:
        # User's move
        print("User's turn (O)")
        user_move(board)
        print_board(board)
        winner = check_winner(board)
        if winner:
            if winner == 'Draw':
                print("It's a draw!")
            else:
                print("User wins!")
            break

        # Computer's move
        print("Computer's turn (X)")
        row, col = heuristic_move(board)
        board[row][col] = 'X'
        print_board(board)
        winner = check_winner(board)
        if winner:
            if winner == 'Draw':
                print("It's a draw!")
            else:
                print("Computer wins!")
            break

if __name__ == "__main__":
    tic_tac_toe()