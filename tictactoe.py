import random

# Prints game board
def print_board (board):
    print("\nCurrent Board:")
    for i in range(3):
        print(" | ".join(board[i]))
        if i < 2:
            print ("-" * 5)
    print()  # Add an empty line for better readability

# Function to check for a win or draw
def check_winner (board, player):
    # Check rows, columns, and diagonals
    for i in range (3):
        if all ([board[i][j] == player for j in range (3)]):  # Row
            return True
        if all ([board[j][i] == player for j in range (3)]):  # Column
            return True
    if all ([board[i][i] == player for i in range (3)]):  # Diagonal
        return True
    if all ([board[i][2 - i] == player for i in range (3)]):  # Anti-diagonal
        return True
    return False

# Function to check for a draw
def check_draw (board):
    return all ([board[i][j] != ' ' for i in range(3) for j in range(3)])

# Function to get validated user input
def get_move (current_player):
    while True:
        move = input (f"Player {current_player}, enter your move as 'row,col' (e.g., 0,2): ")
        try:
            row, col = map(int, move.replace(' ', '').split(','))
            if row not in range(3) or col not in range(3):
                print("Row and column must be between 0 and 2. Please try again.")
                continue
            return row, col
        except ValueError:
            print("Invalid format. Please enter row and column separated by a comma (e.g., 1,2).")

# Function for computer to make a move
def computer_move (board, computer_player):
    available_moves = [(i, j) for i in range (3) for j in range (3) if board[i][j] == ' ']
    if available_moves:
        move = random.choice(available_moves)
        print (f"Computer chooses to place '{computer_player}' at position {move[0]}, {move[1]}")
        return move
    return None

# Main game loop
def tic_tac_toe ():
    print ("Welcome to Tic-Tac-Toe!")
    print ("Players take turns to enter their move by specifying the row and column numbers (0, 1, or 2).")
    print ("For example, to place at row 1, column 2, enter: 1,2\n")
    
    board = [[' ' for _ in range(3)] for _ in range(3)]
    
    # Choose game mode
    while True:
        mode = input("Select game mode:\n1. Player vs Player\n2. Player vs Computer\nEnter 1 or 2: ")
        if mode == '1':
            game_mode = 'PvP'
            break
        elif mode == '2':
            game_mode = 'PvC'
            break
        else:
            print("Invalid selection. Please enter 1 or 2.")
    
    current_player = 'X'
    computer_player = 'O' if game_mode == 'PvC' else None
    
    while True:
        print_board (board)
        
        # actual game
        if game_mode == 'PvC' and current_player == computer_player:
            row, col = computer_move (board, computer_player)
        else:
            row, col = get_move (current_player)
        
        # invalid input
        if board[row][col] != ' ':
            print ("That space is already taken! Try again.\n")
            continue
        
        board[row][col] = current_player
        
        # checks to see who won
        if check_winner (board, current_player):
            print_board (board)
            winner = "Computer" if game_mode == 'PvC' and current_player == computer_player else f"Player {current_player}"
            print(f"{winner} wins!")
            break
        
        # in case of a draw
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        
        # Switch player
        if game_mode == 'PvP':
            current_player = 'O' if current_player == 'X' else 'X'
        elif game_mode == 'PvC':
            current_player = 'O' if current_player == 'X' else 'X'

    # Option to play again
    while True:
        replay = input("Do you want to play again? (y/n): ").lower()
        if replay == 'y':
            tic_tac_toe()
            break
        elif replay == 'n':
            print("Thanks for playing Tic-Tac-Toe!")
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

# Run the game
if __name__ == "__main__":
    tic_tac_toe()



