import random

# Function to print the Tic Tac Toe board
def print_board(board):
    for row in board:
        print(' '.join(row))

# Function to check if any player has won the game
def check_winner(board, player):
    # Check rows and columns
    for i in range(3):
        if all(cell == player for cell in board[i]) or all(board[j][i] == player for j in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Function to check if the board is full (game is a draw)
def is_board_full(board):
    return all(cell != '-' for row in board for cell in row)

# Function to evaluate the board position
def evaluate_board(board):
    # Check if computer wins
    if check_winner(board, 'X'):
        return 1
    # Check if human wins
    elif check_winner(board, 'O'):
        return -1
    # Game is a draw
    elif is_board_full(board):
        return 0
    # Game is not over yet
    else:
        return None

# Function to generate all possible next moves for a given board position
def generate_moves(board, player):
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == '-':
                new_board = [row[:] for row in board]  # Create a copy of the board
                new_board[i][j] = player
                moves.append(new_board)
    return moves

# Brute-force minimax algorithm with move table
def minimax(board, player):
    # Base case: evaluate the board position
    result = evaluate_board(board)
    if result is not None:
        return result

    # Generate all possible next moves
    next_moves = generate_moves(board, player)

    # Recursively evaluate each move and choose the best one
    if player == 'X':
        best_score = -float('inf')
        for move in next_moves:
            score = minimax(move, 'O')
            best_score = max(best_score, score)
    else:
        best_score = float('inf')
        for move in next_moves:
            score = minimax(move, 'X')
            best_score = min(best_score, score)

    return best_score

# Function to make a computer move using the minimax algorithm
def computer_move(board):
    best_score = -float('inf')
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == '-':
                new_board = [row[:] for row in board]  # Create a copy of the board
                new_board[i][j] = 'X'
                score = minimax(new_board, 'O')
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    return best_move

# Main function to play the Tic Tac Toe game
def play_tic_tac_toe():
    board = [['-' for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic Tac Toe!")
    print_board(board)
    while True:
        # Human's move
        while True:
            try:
                row = int(input("Enter row (0, 1, 2): "))
                col = int(input("Enter column (0, 1, 2): "))
                if board[row][col] == '-':
                    board[row][col] = 'O'
                    break
                else:
                    print("Cell already occupied. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Please enter a valid row and column.")

        print_board(board)
        if check_winner(board, 'O'):
            print("Congratulations! You win!")
            break
        elif is_board_full(board):
            print("It's a draw!")
            break

        # Computer's move
        row, col = computer_move(board)
        board[row][col] = 'X'
        print("Computer's move:")
        print_board(board)
        if check_winner(board, 'X'):
            print("Computer wins!")
            break
        elif is_board_full(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_tic_tac_toe()



