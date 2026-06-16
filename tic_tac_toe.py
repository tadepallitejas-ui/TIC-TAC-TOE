def print_board(board):
    """Renders the current state of the board."""
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")



def check_win(board, player):
    """Checks if the given player has won the game."""
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]

    for condition in win_conditions:
        if (
            board[condition[0]]
            == board[condition[1]]
            == board[condition[2]]
            == player
        ):
            return True

    return False


def check_tie(board):
    """Checks if the board is full (a tie game)."""
    return all(space in ["X", "O"] for space in board)


def play_game():
    """Main game loop."""
    # Initialize the board with numbers 1-9
    board = [str(i) for i in range(1, 10)]
    current_player = "X"
    game_on = True

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while game_on:
        try:
            choice = int(
                input(f"Player {current_player}'s turn. Choose a position (1-9): ")
            ) - 1

            if choice < 0 or choice > 8:
                print("Invalid choice! Please pick a number between 1 and 9.")
                continue

            if board[choice] in ["X", "O"]:
                print("That spot is already taken! Try again.")
                continue

        except ValueError:
            print("Please enter a valid number.")
            continue

        # Place the player's marker
        board[choice] = current_player
        print_board(board)

        # Check for win or tie
        if check_win(board, current_player):
            print(f"🎉 Congratulations! Player {current_player} wins! 🎉")
            game_on = False

        elif check_tie(board):
            print("It's a tie! 🤝")
            game_on = False

        else:
            # Switch players
            current_player = "O" if current_player == "X" else "X"


# Start the game
if name == "main":
    play_game()
